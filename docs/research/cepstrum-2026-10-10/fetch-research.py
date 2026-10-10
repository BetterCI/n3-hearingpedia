"""Bounded scholarly discovery; access and claim verification are separate."""
from pathlib import Path
import concurrent.futures
import importlib.util
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')
OUT = Path(__file__).resolve().parent
base = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
def module(name):
    spec = importlib.util.spec_from_file_location(name, base/(name+'.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
oa, judge = module('openalex_research'), module('judge_relevance')
seeds = {}
for name, doi in [('pitch-1967','10.1121/1.1910339'), ('features-1980','10.1109/TASSP.1980.1163420')]:
    seed = oa.simplify(oa.request('/works/https://doi.org/'+doi))
    seeds[name] = seed
    (OUT/(name+'-seed.json')).write_text(json.dumps(seed,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/(name+'-screening-prompt.txt')).write_text(judge.build_prompt(seed, 'Cepstrum: real/complex and power definitions, source-filter homomorphic separation, quefrency pitch and echoes, liftering, MFCC distinction, CPP robustness and inference limits'),encoding='utf-8')
tasks = [('topic', {'search':'cepstrum speech source filter pitch','sort':'relevance_score:desc'}, 12)]
for name,seed in seeds.items():
    wid=seed['id'].rsplit('/',1)[-1]
    tasks.extend([(name+'-backward',{'filter':'cited_by:'+wid},6), (name+'-recent-forward',{'filter':'cites:'+wid+',from_publication_date:2021-10-10,to_publication_date:2026-10-10'},4)])
def fetch(task):
    name,params,limit=task
    try:
        data=oa.list_works(params,limit)
        (OUT/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        return {'query':name,'parameters':params,'limit':limit,'returned':len(data),'status':'ok'}
    except BaseException as e:
        return {'query':name,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    results=list(pool.map(fetch,tasks))
raw=list(seeds.values())
for result in results:
    if result['status']=='ok': raw.extend(json.loads((OUT/(result['query']+'.json')).read_text(encoding='utf-8')))
unique={}
for w in raw:
    key=(w.get('doi') or w.get('id') or w['title'].lower()).lower()
    unique.setdefault(key,w)
(OUT/'candidate-pool.json').write_text(json.dumps({'raw_records':len(raw),'unique_records':len(unique),'papers':list(unique.values())},ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'discovery-status.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'discovery':results,'raw':len(raw),'unique':len(unique)},ensure_ascii=False))
