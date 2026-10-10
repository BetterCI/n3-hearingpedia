"""Record bounded citation discovery and accessible evidence for a new entry."""
from pathlib import Path
import importlib.util
import json
import concurrent.futures
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/comparative-hearing-2026-10-10'
OUT.mkdir(parents=True, exist_ok=True)
SKILL = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
spec = importlib.util.spec_from_file_location('openalex', SKILL / 'openalex_research.py')
oa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)

def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Hearingpedia literature verification'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def discovery():
    jobs = [
        ('topic', lambda: oa.list_works({'search': 'comparative hearing sound localization hair cell regeneration', 'sort': 'relevance_score:desc'}, 8)),
    ]
    for tag, doi in [('owl', '10.1523/JNEUROSCI.10-10-03227.1990'), ('fly', '10.1007/BF00193432'), ('bird', '10.1126/science.3381101')]:
        def expand(tag=tag, doi=doi):
            seed = oa.request('/works/' + urllib.parse.quote('https://doi.org/' + doi, safe=':/'))
            save(tag + '-seed.json', oa.simplify(seed))
            ids = [x.rsplit('/', 1)[-1] for x in seed.get('referenced_works', [])][:8]
            back = oa.list_works({'filter': 'openalex:' + '|'.join(ids)}, 8) if ids else []
            forward = oa.list_works({'filter': 'cites:' + seed['id'].rsplit('/', 1)[-1], 'sort': 'cited_by_count:desc'}, 8)
            save(tag + '-backward.json', back)
            save(tag + '-forward.json', forward)
            return {'seed': seed['id'], 'backward': len(back), 'forward': len(forward)}
        jobs.append((tag, expand))
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        fs = {pool.submit(fn): tag for tag, fn in jobs}
        for f in concurrent.futures.as_completed(fs):
            tag = fs[f]
            try:
                result = f.result()
                save(tag + '-discovery.json', result)
                print(tag, 'saved', len(result) if isinstance(result, list) else result)
            except BaseException as e:
                errors.append({'stage': tag, 'error': str(e)})
                print(tag, 'unavailable', str(e)[:160])
    save('discovery-errors.json', errors)

def evidence():
    pmcs = ['PMC8171922', 'PMC12029790', 'PMC10238092', 'PMC6936466', 'PMC3593961', 'PMC34340', 'PMC7382275', 'PMC4954978', 'PMC9587988']
    records = []
    def one(pmc):
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/' + pmc + '/fullTextXML'
        try:
            cached = OUT / (pmc + '-text.json')
            if cached.exists():
                return json.loads(cached.read_text(encoding='utf-8'))
            raw = fetch(url)
            (OUT / (pmc + '.xml')).write_bytes(raw)
            doc = ET.fromstring(raw)
            paragraphs = [{'section': '', 'text': ''.join(p.itertext()).strip()} for p in doc.findall('.//body//p')]
            abstracts = [''.join(p.itertext()).strip() for p in doc.findall('.//abstract//p')]
            doi = next((x.text for x in doc.findall('.//article-id') if x.get('pub-id-type') == 'doi'), None)
            title = ''.join(doc.find('.//article-title').itertext())
            rec = {'pmc': pmc, 'url': url, 'title': title, 'doi': doi, 'abstract': abstracts, 'paragraphs': paragraphs, 'access': 'fulltext'}
            save(pmc + '-text.json', rec)
            return rec
        except BaseException as e:
            return {'pmc': pmc, 'url': url, 'error': str(e)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(one, pmcs))
    save('fulltext-access.json', [{k: v for k, v in r.items() if k != 'paragraphs'} for r in records])
    for r in records:
        print(r.get('pmc'), r.get('doi'), r.get('title'), r.get('error', ''))
        print('Body paragraphs:', len(r.get('paragraphs', [])))

def metadata():
    dois = ['10.1016/S1095-6433(00)00232-4', '10.1523/JNEUROSCI.10-10-03227.1990', '10.1038/86049', '10.1126/science.2063209', '10.7554/eLife.84760', '10.1073/pnas.2001105117', '10.1073/pnas.1821722116', '10.1371/journal.pone.0252330', '10.1007/BF00193432', '10.1038/srep29957', '10.3390/mi16040451', '10.1126/science.3381100', '10.1126/science.3381101', '10.1073/pnas.97.22.11714', '10.1016/j.heares.2012.11.019', '10.1016/j.heares.2024.109170', '10.1038/s42003-022-04098-x']
    def one(doi):
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': 'DOI:' + doi, 'format': 'json', 'resultType': 'core'})
        try:
            data = json.loads(fetch(url))
            r = data['resultList']['result'][0]
            r['requested_doi'] = doi
            return r
        except BaseException as e:
            return {'requested_doi': doi, 'error': str(e)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(one, dois))
    save('verified-metadata.json', records)
    for r in records:
        print(json.dumps({k: r.get(k) for k in ['requested_doi', 'title', 'authorString', 'pubYear', 'pmcid', 'abstractText', 'error']}, ensure_ascii=False))

if __name__ == '__main__':
    {'discovery': discovery, 'evidence': evidence, 'metadata': metadata}[sys.argv[-1]]()
