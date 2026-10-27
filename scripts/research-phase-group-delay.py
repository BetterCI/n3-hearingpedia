"""Bounded discovery and citation expansion for the phase/group delay entry."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import importlib.util
import json
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/phase-and-group-delay-2026-10-27'
OUT.mkdir(parents=True, exist_ok=True)
skill = Path('C:/Users/mengq/.codex/skills/deep-research/scripts/openalex_research.py')
spec = importlib.util.spec_from_file_location('openalex_research', skill)
oa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)

jobs = {
    'search-audibility': lambda: oa.list_works({'search': 'group delay distortion audibility', 'sort': 'relevance_score:desc'}, 15),
    'search-oae': lambda: oa.list_works({'search': 'otoacoustic emission phase gradient delay', 'sort': 'relevance_score:desc'}, 15),
    'search-ha-recent': lambda: oa.list_works({'search': 'hearing aid processing delay', 'filter': 'from_publication_date:2023-01-01,to_publication_date:2026-10-27', 'sort': 'relevance_score:desc'}, 15),
    'seed-equalization': lambda: oa.simplify(oa.request('/works/https://doi.org/10.1109/TASLP.2021.3087969')),
    'seed-oae-method': lambda: oa.simplify(oa.request('/works/https://doi.org/10.1121/1.4730916')),
}
results = {}
def run_jobs(tasks):
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = {pool.submit(fn): name for name, fn in tasks.items()}
        for future in as_completed(futs):
            name = futs[future]
            try:
                value = future.result()
                results[name] = value
                (OUT / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
                print(name, 'saved', len(value) if isinstance(value, list) else value.get('id'), flush=True)
            except BaseException as exc:
                (OUT / (name + '-error.txt')).write_text(str(exc), encoding='utf-8')
                print(name, type(exc).__name__, flush=True)
run_jobs(jobs)
expansion = {}
for key in ['seed-equalization', 'seed-oae-method']:
    if key not in results:
        continue
    work = results[key]
    oid = oa.normalize_id(work['id'])
    refids = '|'.join(oa.normalize_id(x) for x in work['referenced_works'][:30])
    if refids:
        expansion[key+'-backward'] = lambda ids=refids: oa.list_works({'filter': 'openalex:'+ids}, 30)
    expansion[key+'-forward'] = lambda wid=oid: oa.list_works({'filter': 'cites:'+wid+',to_publication_date:2026-10-27', 'sort': 'publication_date:desc'}, 20)
run_jobs(expansion)

# Public full-text XML is saved as source material, without republishing it.
def fulltext(pmc):
    url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Hearingpedia research (source verification)'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    root = ET.fromstring(raw)
    cache = ROOT / 'artifacts/phase-group-delay-sources'
    cache.mkdir(parents=True, exist_ok=True)
    (cache / (pmc+'.xml')).write_bytes(raw)
    paragraphs = [''.join(x.itertext()) for x in root.iter() if x.tag in ['article-title','abstract','p','title','table']]
    (cache / (pmc+'.txt')).write_text('\n\n'.join(paragraphs), encoding='utf-8')
    return {'url': url, 'characters': sum(map(len, paragraphs))}
run_jobs({pmc: lambda p=pmc: fulltext(p) for pmc in ['PMC2914235','PMC3427360','PMC11638989','PMC13009764','PMC10805375']})

pool = {}
for name, data in results.items():
    if isinstance(data, list):
        for work in data:
            identity = (work.get('doi') or work.get('id') or work['title']).lower()
            if identity not in pool:
                pool[identity] = {**work, 'discovery_routes': []}
            pool[identity]['discovery_routes'].append(name)
(OUT/'candidate-pool.json').write_text(json.dumps(list(pool.values()), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print('deduplicated candidates', len(pool), flush=True)
