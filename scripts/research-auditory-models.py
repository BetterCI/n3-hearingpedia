"""Archive original metadata/abstracts for the local computational models article."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,urllib.request,urllib.parse,sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-computational-models-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
DOIS={
'acm-comparison':'10.1051/aacus/2022008',
'acm-amt':'10.1051/aacus/2022011',
'acm-mechanics':'10.1152/physrev.2001.81.3.1305',
'acm-erb':'10.1016/0378-5955(90)90170-T',
'acm-meddis':'10.1121/1.393460',
'acm-zilany':'10.1121/1.4837815',
'acm-bruce':'10.1016/j.heares.2017.12.016',
'acm-verhulst':'10.1016/j.heares.2017.12.018',
'acm-dau':'10.1121/1.420344',
'acm-jeffress':'10.1037/h0061495',
'acm-durlach':'10.1121/1.1918675',
'acm-breebaart':'10.1121/1.1383297',
'acm-breebaart-test':'10.1121/1.1383299',
'acm-sepsm':'10.1121/1.3621502',
'acm-stoi':'10.1109/TASL.2011.2114881',
'acm-haspi':'10.1016/j.specom.2020.05.001',
'acm-model-matched':'10.1371/journal.pbio.2005127',
'acm-kell':'10.1016/j.neuron.2018.03.044',
'acm-saddler':'10.1038/s41467-021-27366-6',
'acm-connear':'10.1038/s42256-020-00286-8',
'acm-icnet':'10.1038/s42256-025-01104-9'}
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Hearingpedia original source verification'})
 with urllib.request.urlopen(req,timeout=20) as r:return json.load(r)
def source(item):
 key,doi=item; row={'id':key,'doi':doi,'checked_at':'2026-10-10','errors':[]}
 try:
  q=urllib.parse.urlencode({'query':'DOI:"'+doi+'"','format':'json','resultType':'core','pageSize':1})
  data=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+q)['resultList']['result']
  row['europe_pmc']=data[0] if data else None
 except Exception as e:row['errors'].append('Europe PMC: '+str(e))
 try:
  msg=fetch('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))['message']
  row['crossref']={k:msg.get(k) for k in ['title','author','container-title','published','published-print','volume','issue','page','URL','type','abstract']}
 except Exception as e:row['errors'].append('Crossref: '+str(e))
 return row
with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(source,DOIS.items()))
(OUT/'verified-metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in rows:
 e=r.get('europe_pmc') or {}; c=r.get('crossref') or {}
 print(json.dumps({'id':r['id'],'doi':r['doi'],'title':e.get('title') or c.get('title'),'abstract':e.get('abstractText') or c.get('abstract'),'errors':r['errors']},ensure_ascii=False))
