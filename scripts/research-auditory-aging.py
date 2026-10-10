"""Archive bibliographic records and original abstracts for the local auditory aging entry."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, urllib.request, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-aging-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
DOIS={'aging-schuknecht-1993': '10.1177/00034894931020S101', 'aging-wu-2020': '10.1523/JNEUROSCI.0937-20.2020', 'aging-genetics-2022': '10.1016/j.ajhg.2022.04.010', 'aging-fullgrabe-2015': '10.3389/fnagi.2014.00347', 'aging-schoof-2014': '10.3389/fnagi.2014.00307', 'aging-hopkins-2011': '10.1121/1.3585848', 'aging-anderson-2012': '10.1523/JNEUROSCI.2176-12.2012', 'aging-presacco-2016': '10.1152/jn.00372.2016', 'aging-levels-2021': '10.1016/j.heares.2020.108117', 'aging-cassarly-2020': '10.1097/AUD.0000000000000746', 'aging-peelle-2011': '10.1523/JNEUROSCI.2559-11.2011', 'aging-lin-2011': '10.1001/archneurol.2010.362', 'aging-mocah-2023': '10.1111/jgs.18241', 'aging-humes-2017': '10.1044/2017_AJA-16-0111', 'aging-social-2025': '10.1001/jamainternmed.2025.1140', 'aging-training-2013': '10.1073/pnas.1213555110', 'aging-cochrane-2026': '10.1002/14651858.CD012023.pub3', 'achieve-2023': '10.1016/S0140-6736(23)01406-X', 'achieve-communication-2024': '10.1111/jgs.19185'}
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Hearingpedia source verification'})
 with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)
def source(item):
 key,doi=item;row={'id':key,'doi':doi,'checked_at':'2026-10-10','errors':[]}
 try:
  msg=fetch('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))['message']
  row['crossref']={k:msg.get(k) for k in ['title','author','container-title','published','published-online','published-print','volume','issue','page','URL','type','abstract']}
 except Exception as e:row['errors'].append('Crossref: '+str(e))
 try:
  query=urllib.parse.urlencode({'query':'DOI:"'+doi+'"','format':'json','resultType':'core','pageSize':1})
  found=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+query)['resultList']['result']
  row['europe_pmc']=found[0] if found else None
 except Exception as e:row['errors'].append('Europe PMC: '+str(e))
 return row
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(source,DOIS.items()))
(OUT/'verified-metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in rows:
 print(json.dumps({'id':r['id'],'title':(r.get('crossref') or {}).get('title'),
 'pmid':(r.get('europe_pmc') or {}).get('id'),'pmcid':(r.get('europe_pmc') or {}).get('pmcid'),
 'abstract':(r.get('europe_pmc') or {}).get('abstractText') or (r.get('crossref') or {}).get('abstract'),
 'errors':r['errors']},ensure_ascii=False))
