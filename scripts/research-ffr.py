"""Public discovery records; requires the local deep-research skill client."""
from pathlib import Path
import json, subprocess, sys, urllib.request, urllib.parse, concurrent.futures
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'docs/research/frequency-following-response-2026-11-06'
SKILL = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
DOIS = ['10.1038/s41467-019-13003-w','10.1016/j.heares.2019.107779',
 '10.1016/j.neuroimage.2018.03.060','10.1016/j.heares.2008.08.004',
 '10.1016/j.heares.2017.01.014','10.1523/ENEURO.0451-21.2021',
 '10.1162/jocn_a_02103','10.1101/2025.05.20.655073','10.1111/ejn.70418',
 '10.1016/j.cogbrainres.2005.05.004','10.1162/jocn.2008.20131',
 '10.1016/j.neuroimage.2010.01.073','10.3389/fnins.2024.1422903',
 '10.1016/j.clinph.2010.07.009','10.1038/s41467-025-62155-5']
def metadata(doi):
    try:
        with urllib.request.urlopen('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''),timeout=40) as r: m=json.load(r)['message']
        return {'doi':doi,'status':200,**{k:m.get(k) for k in ['title','author','container-title','volume','issue','page','published','abstract']}}
    except Exception as e: return {'doi':doi,'error':str(e)}
def discovery(name,args):
    p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'openalex_research.py'),*args],capture_output=True,encoding='utf-8')
    if p.returncode: data={'error':p.stderr}
    else: data=json.loads(p.stdout)
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data
if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: records=list(pool.map(metadata,DOIS))
    (OUT/'bibliographic-check.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in records: print(r['doi'],r.get('status',r.get('error')),r.get('title'))
    discovery('openalex-search.json',['search','auditory frequency following response sources analysis','--limit','20'])
    seed=discovery('openalex-seed.json',['work','https://doi.org/10.1038/s41467-019-13003-w'])
    if seed.get('id'):
        for name,args in [('backward',['references',seed['id'],'--limit','25']),('forward',['citations',seed['id'],'--limit','25']),('recent',['search','auditory frequency following response','--sort','publication_date:desc','--limit','25'])]:
            discovery('openalex-'+name+'.json',args)
        p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'judge_relevance.py'),'--topic','Auditory FFR: distributed sources, recording controls, polarity, statistics, behavior and recent developments',str(OUT/'openalex-seed.json')],capture_output=True,encoding='utf-8',check=True)
        (OUT/'screening-prompt.txt').write_text('\n'.join(line.rstrip() for line in p.stdout.splitlines()).rstrip()+'\n',encoding='utf-8')
