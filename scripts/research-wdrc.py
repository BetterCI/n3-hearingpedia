"""Save DOI metadata and reproducible discovery records for the WDRC entry."""
from pathlib import Path
import concurrent.futures, json, subprocess, sys, urllib.request, urllib.parse

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/wide-dynamic-range-compression-2026-11-06'
SKILL = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
DOIS = {
    'wdrc-kates-2005': '10.1177/108471380500900202',
    'wdrc-souza-2002': '10.1177/108471380200600402',
    'moore-compression-speed-2008': '10.1177/1084713808317819',
    'wdrc-jenstad-2005': '10.1044/1092-4388(2005/045)',
    'wdrc-bor-2008': '10.1044/1092-4388(2008/07-0009)',
    'wdrc-gatehouse-2006': '10.1080/14992020500429518',
    'wdrc-may-2018': '10.1177/2331216518790903',
    'wdrc-corey-2021': '10.1121/10.0005314',
    'wdrc-windle-2025': '10.1097/AUD.0000000000001716',
    'wdrc-ellis-2024': '10.1097/AUD.0000000000001469',
    'wdrc-zhang-2025': '10.1177/23312165241309301',
    'wdrc-hassager-2017': '10.1121/1.4984040',
    'wdrc-villchur-1973': '10.1121/1.1913514',
    'keidser-nalnl2-2011': '10.4081/audiores.2011.e24',
    'scollie-dsl5-2005': '10.1177/108471380500900403',
    'prescription-dsl-protocols-2005': '10.1177/108471380500900404',
    'croghan-music-2014': '10.1097/AUD.0000000000000056',
    'wiggins-seeber-2011': '10.1121/1.3652887',
    'kayser-openmha-2022': '10.1016/j.softx.2021.100953',
}

def metadata(item):
    key, doi = item
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='')
    try:
        with urllib.request.urlopen(url, timeout=45) as r:
            m = json.load(r)['message']
        return {'id': key, 'doi': doi, 'status': 200, 'title': m.get('title'),
                'authors': m.get('author'), 'journal': m.get('container-title'),
                'volume': m.get('volume'), 'issue': m.get('issue'), 'page': m.get('page'),
                'published': m.get('published'), 'published_online': m.get('published-online'),
                'abstract': m.get('abstract')}
    except Exception as e:
        return {'id': key, 'doi': doi, 'error': str(e)}

def run_skill(filename, args):
    result = subprocess.run([sys.executable, '-X', 'utf8', str(SKILL/'openalex_research.py'), *args],
                            capture_output=True, encoding='utf-8', check=True)
    data = json.loads(result.stdout)
    (OUT/filename).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return data

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(metadata, DOIS.items()))
    (OUT/'bibliographic-check.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    for r in records:
        print(r['id'], r.get('status', r.get('error')), r.get('title'), r.get('volume'), r.get('issue'), r.get('page'))
    seed = run_skill('openalex-seed.json', ['work', 'https://doi.org/10.1177/2331216518790903'])
    print('seed keys', list(seed)[:8])
    sid = seed['id']
    for name, args in [('openalex-backward.json', ['references', sid, '--limit', '20']),
                       ('openalex-forward.json', ['citations', sid, '--limit', '20']),
                       ('openalex-recent.json', ['search', 'hearing aid compression', '--limit', '15', '--sort', 'publication_date:desc'])]:
        run_skill(name, args)
    prompt = subprocess.run([sys.executable, '-X', 'utf8', str(SKILL/'judge_relevance.py'),
                             '--topic', 'WDRC mechanisms, speech and noise tradeoffs, human outcomes',
                             str(OUT/'openalex-seed.json')], capture_output=True, encoding='utf-8', check=True)
    (OUT/'screening-prompt.txt').write_text(prompt.stdout, encoding='utf-8')
