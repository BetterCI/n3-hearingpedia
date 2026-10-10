"""Discovery only: actual citation and reading status are recorded separately."""
from pathlib import Path
import concurrent.futures
import importlib.util
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = Path(__file__).resolve().parent
base = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
def module(name):
    spec = importlib.util.spec_from_file_location(name, base / (name+'.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
oa = module('openalex_research')
judge = module('judge_relevance')
seeds = {}
for name, doi in [('spectral-analysis','10.1121/10.0026475'),('phase-resolvability','10.1121/1.409970')]:
    seeds[name] = oa.simplify(oa.request('/works/https://doi.org/'+doi))
    (OUT/(name+'-seed.json')).write_text(json.dumps(seeds[name],ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/(name+'-screening-prompt.txt')).write_text(judge.build_prompt(seeds[name],'Pure and complex tones: signal components, phase, spectral analysis and limits of auditory perception'),encoding='utf-8')
tasks = []
for name, seed in seeds.items():
    wid = seed['id'].rsplit('/',1)[-1]
    tasks += [(name+'-backward', {'filter':'cited_by:'+wid},15), (name+'-recent-forward', {'filter':'cites:'+wid+',from_publication_date:2021-01-01,to_publication_date:2026-10-10'},5)]
def fetch(task):
    name, params, limit=task
    try:
        data = oa.list_works(params,limit)
        (OUT/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        return {'query':name,'parameters':params,'requested_limit':limit,'returned':len(data),'status':'ok'}
    except BaseException as e:
        return {'query':name,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,tasks))
(OUT/'discovery-status.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False))
