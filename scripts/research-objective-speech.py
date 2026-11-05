"""Reproducible discovery and metadata checks; no private data or credentials."""
from pathlib import Path
import json, subprocess, sys, urllib.request, urllib.parse, concurrent.futures
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'docs/research/objective-speech-evaluation-2026-11-06'
SKILL = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
DOIS = ['10.1109/TASL.2011.2114881','10.1109/TASLP.2016.2585878',
 '10.1016/j.specom.2020.05.001','10.17743/jaes.2014.0006','10.1121/10.0017546',
 '10.1109/ICASSP.2019.8683855','10.1109/ICASSP43922.2022.9746108',
 '10.21437/Interspeech.2021-299','10.1109/TASLP.2018.2856374',
 '10.1109/SLT61566.2024.10832295','10.1177/23312165261422005',
 '10.1016/j.heares.2022.108608','10.21437/Interspeech.2025-251']
def meta(doi):
    try:
        with urllib.request.urlopen('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''),timeout=50) as r:
            m=json.load(r)['message']
        return {'doi':doi,'status':200, **{k:m.get(k) for k in ['title','author','container-title','volume','issue','page','published','abstract']}}
    except Exception as e: return {'doi':doi,'error':str(e)}
def discovery(name,args):
    p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'openalex_research.py'),*args],capture_output=True,encoding='utf-8',check=True)
    data=json.loads(p.stdout)
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data
if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: records=list(pool.map(meta,DOIS))
    (OUT/'bibliographic-check.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in records: print(r['doi'],r.get('status',r.get('error')),r.get('title'))
    discovery('openalex-search.json',['search','objective speech intelligibility quality evaluation','--limit','20'])
    seed=discovery('openalex-seed.json',['work','https://doi.org/10.1109/TASLP.2018.2856374'])
    for name,args in [('backward',['references',seed['id'],'--limit','20']),('forward',['citations',seed['id'],'--limit','20']),('recent',['search','speech quality assessment','--sort','publication_date:desc','--limit','20'])]:
        discovery('openalex-'+name+'.json',args)
    p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'judge_relevance.py'),'--topic','Objective speech intelligibility and quality: target, reference, hearing loss, generalization and validation',str(OUT/'openalex-seed.json')],capture_output=True,encoding='utf-8',check=True)
    (OUT/'screening-prompt.txt').write_text(p.stdout,encoding='utf-8')
