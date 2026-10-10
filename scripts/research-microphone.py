"""Bounded scholarly discovery; source retrieval is not a claim of full-text review."""
from pathlib import Path
import importlib.util, json, urllib.request, urllib.parse, concurrent.futures, sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/microphone-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
sys.stdout.reconfigure(encoding='utf-8')
SKILL=Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
sp=importlib.util.spec_from_file_location('oa',SKILL/'openalex_research.py')
oa=importlib.util.module_from_spec(sp);sp.loader.exec_module(oa)
# Use requests transport: this host's urllib SSL setup failed with missing CA path.
import requests
def transport(path, params=None):
    r=requests.get('https://api.openalex.org'+path,params=params,timeout=40);r.raise_for_status();return r.json()
oa.request=transport
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def fetch(url):
    r=requests.get(url,timeout=40);r.raise_for_status();return r.content
queries=[('principles','microphone pressure gradient directivity proximity effect'),('microphones','measurement microphone free field calibration'),('recent','MEMS microphone signal noise capacitive piezoelectric')]
save('scope.json',{'question':'How do microphone sensing mechanism, acoustic ports, directionality, noise and calibration affect reproducible auditory research?','recent_range':['2021-01-01','2026-10-10'],'classics':'No start-date restriction','searches':queries,'limits':'6 results per query; 6 backward and 6 forward results per seed. Primary research contextualizes mechanisms; official standards scope and application notes support engineering definitions. No claim of exhaustive review.'})
def search(tag,q):
    p={'search':q,'sort':'relevance_score:desc'}
    if tag=='recent':p['filter']='from_publication_date:2021-01-01,to_publication_date:2026-10-10'
    r=oa.list_works(p,6);save(tag+'-search.json',r);return r
def seed(tag,doi):
    raw=oa.request('/works/'+urllib.parse.quote('https://doi.org/'+doi,safe=':/'))
    save(tag+'-seed.json',oa.simplify(raw))
    ids=[s.rsplit('/',1)[-1] for s in raw.get('referenced_works',[])][:6]
    back=oa.list_works({'filter':'openalex:'+'|'.join(ids)},6) if ids else []
    forward=oa.list_works({'filter':'cites:'+raw['id'].rsplit('/',1)[-1],'sort':'publication_date:desc'},6)
    save(tag+'-backward.json',back);save(tag+'-forward.json',forward)
    return [oa.simplify(raw)]+back+forward
jobs=[(tag,lambda t=tag,q=q:search(t,q)) for tag,q in queries]
jobs +=[(tag,lambda t=tag,d=d:seed(t,d)) for tag,d in [('electret','10.1121/1.1909130'),('hybrid','10.1038/s41378-026-01251-y')]]
pool=[];errors=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
    futures={ex.submit(fn):tag for tag,fn in jobs}
    for f in concurrent.futures.as_completed(futures):
        try:pool.extend(f.result());print(futures[f],'saved')
        except Exception as e:errors.append({'stage':futures[f],'error':str(e)})
dedup={}
for p in pool:
    key=(p.get('doi') or p.get('id') or p.get('title','').strip().lower())
    dedup.setdefault(key,p)
save('candidate-pool.json',list(dedup.values()));save('discovery-errors.json',errors)
for doi in ['10.1121/1.1909130','10.1038/s41378-026-01251-y']:
    tag='electret' if '1121' in doi else 'hybrid'
    try:save(tag+'-crossref.json',json.loads(fetch('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')))['message'])
    except Exception as e:save(tag+'-crossref-error.json',{'error':str(e)})
    if tag=='hybrid':
        try:
            r=json.loads(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'DOI:'+doi,'format':'json','resultType':'core'})))['resultList']['result'][0]
            save('hybrid-europepmc.json',r)
            if r.get('pmcid'):(OUT/'hybrid.xml').write_bytes(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/'+r['pmcid']+'/fullTextXML'))
        except Exception as e:save('hybrid-fulltext-error.json',{'error':str(e)})
print('Deduplicated candidates:',len(dedup),'discovery failures:',len(errors))
