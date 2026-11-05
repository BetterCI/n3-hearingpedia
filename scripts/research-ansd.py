"""Public discovery records; requires the local deep-research skill client."""
from pathlib import Path
import json, subprocess, sys, urllib.request, urllib.parse, concurrent.futures
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'docs/research/auditory-neuropathy-spectrum-disorder-2026-11-06'
SKILL = Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
DOIS = ['10.1093/brain/119.3.741','10.3390/jcm9041074','10.1002/wjo2.70003','10.1016/j.cell.2006.08.040','10.1093/brain/awu378','10.1044/1092-4388(2006/029)','10.1080/14992020802665959','10.1097/01.aud.0000224100.30525.ab','10.1097/00003446-199906000-00006','10.1097/MAO.0000000000000997','10.1038/s41586-026-10393-y','10.1056/NEJMoa2400521','10.1016/S0140-6736(23)02874-X']

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
    discovery('openalex-search.json',['search','auditory neuropathy spectrum disorder diagnosis treatment','--limit','20'])
    seed=discovery('openalex-seed.json',['work','https://doi.org/10.3390/jcm9041074'])
    if seed.get('id'):
        for name,args in [('backward',['references',seed['id'],'--limit','25']),('forward',['citations',seed['id'],'--limit','25']),('recent',['search','auditory neuropathy spectrum disorder','--sort','publication_date:desc','--limit','25'])]:
            discovery('openalex-'+name+'.json',args)
        p=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'judge_relevance.py'),'--topic','ANSD: phenotype, CM artifact controls, presynaptic versus postsynaptic lesions, speech function, hearing aids, cochlear implants, OTOF gene therapy; recent period 2024-01-01 to 2026-11-06',str(OUT/'openalex-seed.json')],capture_output=True,encoding='utf-8',check=True)
        (OUT/'screening-prompt.txt').write_text('\n'.join(line.rstrip() for line in p.stdout.splitlines()).rstrip()+'\n',encoding='utf-8')
