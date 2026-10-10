"""Bounded scholarly discovery; source retrieval is not a claim of full-text review."""
from pathlib import Path
import importlib.util, json, urllib.request, urllib.parse, concurrent.futures, sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/electroacoustic-transducer-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
sys.stdout.reconfigure(encoding='utf-8')
SKILL=Path('C:/Users/mengq/.codex/skills/deep-research/scripts')
sp=importlib.util.spec_from_file_location('oa',SKILL/'openalex_research.py')
oa=importlib.util.module_from_spec(sp);sp.loader.exec_module(oa)
def save(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Hearingpedia literature research'}),timeout=35) as r:return r.read()
queries=[('principles','electroacoustic transducer lumped parameter loudspeaker'),('microphones','MEMS microphone capacitive piezoelectric'),('recent','MEMS loudspeaker in ear modeling')]
save('scope.json',{'question':'How do electrical, mechanical and acoustic coupling, load and measurement references determine auditory transducer performance?','recent_range':['2021-01-01','2026-10-10'],'classics':'No start-date restriction','searches':queries,'limits':'6 results per query; 6 backward and 6 forward results per seed. Primary research contextualizes mechanisms; official standards scope and application notes support engineering definitions. No claim of exhaustive review.'})
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
jobs +=[(tag,lambda t=tag,d=d:seed(t,d)) for tag,d in [('becker','10.1016/j.snr.2025.100319'),('equalization','10.3390/mi16060655')]]
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
for doi in ['10.1016/j.snr.2025.100319','10.3390/mi16060655']:
    tag='becker' if 'snr' in doi else 'equalization'
    try:save(tag+'-crossref.json',json.loads(fetch('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe='')))['message'])
    except Exception as e:save(tag+'-crossref-error.json',{'error':str(e)})
    if tag=='equalization':
        try:
            r=json.loads(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':'DOI:'+doi,'format':'json','resultType':'core'})))['resultList']['result'][0]
            save('equalization-europepmc.json',r)
            if r.get('pmcid'):(OUT/'equalization.xml').write_bytes(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/'+r['pmcid']+'/fullTextXML'))
        except Exception as e:save('equalization-fulltext-error.json',{'error':str(e)})
print('Deduplicated candidates:',len(dedup),'discovery failures:',len(errors))
