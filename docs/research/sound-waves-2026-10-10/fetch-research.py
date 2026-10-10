"""Fetch public scholarly materials and record reproducible discovery, not article evidence by itself."""
from pathlib import Path
import concurrent.futures
import importlib.util
import json
import urllib.request

OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('oa', 'C:/Users/mengq/.codex/skills/deep-research/scripts/openalex_research.py')
oa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)

def discover(name, action):
    try:
        data = action()
        (OUT / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        return {'query': name, 'count': len(data) if isinstance(data, list) else 1, 'status': 'ok'}
    except BaseException as e:
        return {'query': name, 'status': 'failed', 'error': str(e)}

tasks = [
 ('openalex-speed-seed', lambda: oa.simplify(oa.request('/works/https://doi.org/10.1063/5.0294663'))),
 ('openalex-speed-backward', lambda: oa.list_works({'filter': 'cited_by:W4416929043'}, 100)),
 ('openalex-speed-forward', lambda: oa.list_works({'filter': 'cites:W4416929043'}, 20)),
 ('openalex-environment-search', lambda: oa.list_works({'search': 'Weather conditions determine attenuation and speed of sound'}, 5)),
 ('openalex-environment-backward', lambda: oa.list_works({'filter': 'cited_by:W2802623310'}, 100)),
]
# 'cited_by' returns the works referenced by the seed; 'cites' returns later citing works.
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    report = list(pool.map(lambda pair: discover(*pair), tasks))
(OUT / 'discovery-status.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False))
