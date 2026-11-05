"""Reproduce bibliographic and one-hop discovery checks (public APIs)."""
from pathlib import Path
import json, subprocess, sys, urllib.request, urllib.parse, concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/speech-enhancement-and-noise-reduction-2026-11-06'
SKILL=Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
DOIS=['10.1109/TASSP.1979.1163209','10.1109/TASSP.1984.1164453','10.1109/89.928915','10.1016/j.specom.2010.12.003','10.1109/TASL.2009.2025790','10.1109/TASLP.2018.2842159','10.1121/1.4820893','10.1121/1.2766778','10.23919/EUSIPCO63174.2024.10714927','10.1609/aaai.v40i39.40562','10.1109/TASLP.2015.2512042']
def metadata(doi):
    try:
        with urllib.request.urlopen('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''),timeout=40) as r:m=json.load(r)['message']
        return {'doi':doi,'status':200,**{k:m.get(k) for k in ['title','author','container-title','volume','issue','page','published','abstract']}}
    except Exception as e:return {'doi':doi,'error':str(e)}
def discovery(name,args):
    p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'openalex_research.py'),*args],capture_output=True,encoding='utf-8')
    data=json.loads(p.stdout) if not p.returncode else {'error':p.stderr}
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data
if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(metadata,DOIS))
    (OUT/'bibliographic-check.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in records:print(r['doi'],r.get('status',r.get('error')),r.get('title'))
    discovery('openalex-search.json',['search','speech enhancement noise reduction intelligibility','--limit','20'])
    seed=discovery('openalex-seed.json',['work','https://doi.org/10.1109/TASLP.2018.2842159'])
    if seed.get('id'):
        for name,args in [('backward',['references',seed['id'],'--limit','20']),('forward',['citations',seed['id'],'--limit','20']),('recent',['search','generative speech enhancement','--sort','publication_date:desc','--limit','20'])]:
            discovery('openalex-'+name+'.json',args)
        p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'judge_relevance.py'),'--topic','Speech enhancement and noise reduction: statistical estimators, complex masks, multichannel filtering, streaming constraints, human intelligibility and generative content fidelity. Recent period 2024-01-01 to 2026-11-06.',str(OUT/'openalex-seed.json')],capture_output=True,encoding='utf-8',check=True)
        (OUT/'screening-prompt.txt').write_text('\n'.join(l.rstrip() for l in p.stdout.splitlines()).rstrip()+'\n',encoding='utf-8')
