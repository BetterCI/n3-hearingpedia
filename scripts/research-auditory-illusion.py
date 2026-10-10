"""Archive verified original metadata and abstracts for the local illusion entry."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, urllib.request, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-illusion-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
DOIS={
'ai-riecke':'10.1523/JNEUROSCI.2713-07.2007',
'ai-petkov':'10.1016/j.neuron.2007.02.031',
'ai-warren':'10.1126/science.167.3917.392',
'ai-leonard':'10.1038/ncomms13619',
'ai-shepard':'10.1121/1.1919362',
'ai-scale':'10.1121/1.380573',
'ai-octave':'10.1038/251307a0',
'ai-chambers':'10.1037/0096-1523.28.6.1288',
'ai-deutsch-reply':'10.1037/0096-1523.30.2.355',
'ai-tritone':'10.2307/40285337',
'ai-song':'10.1121/1.3562174',
'ai-language':'10.3389/fpsyg.2016.00662',
'ai-mcgurk':'10.1038/264746a0',
'ai-mcgurk-limit':'10.3758/s13414-016-1238-9',
'ai-bistability':'10.1016/j.cub.2006.05.054',
'ai-ci':'10.1016/j.heares.2013.12.003',
'ai-song-2025':'10.1016/j.cognition.2024.105933',
'ai-bird-2025':'10.1038/s41467-025-63182-y'}
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
 e=r.get('europe_pmc') or {};c=r.get('crossref') or {}
 print(json.dumps({'id':r['id'],'title':e.get('title') or c.get('title'),'abstract':e.get('abstractText') or c.get('abstract'),'errors':r['errors']},ensure_ascii=False))
