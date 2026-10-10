"""Archive bibliographic records and original abstracts for the local auditory development entry."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, urllib.request, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-development-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
DOIS={'dev-hepper-1994': '10.1136/fn.71.2.f81', 'dev-partanen-2013': '10.1073/pnas.1302159110', 'dev-eimas-1971': '10.1126/science.171.3968.303', 'dev-werker-1984': '10.1016/S0163-6383(84)80022-3', 'dev-kuhl-1992': '10.1126/science.1736364', 'dev-kuhl-2003': '10.1073/pnas.1532872100', 'dev-maye-2002': '10.1016/S0010-0277(01)00157-3', 'dev-saffran-1996': '10.1126/science.274.5294.1926', 'dev-moore-2007': '10.1080/14992020701383019', 'dev-werner-2001': '10.1121/1.1365112', 'dev-observer-1987': '10.1037/0012-1649.23.5.627', 'dev-litovsky-2005': '10.1121/1.1873913', 'dev-buss-2017': '10.1121/1.4979936', 'dev-leibold-2016': '10.1097/AUD.0000000000000270', 'dev-sharma-2002': '10.1097/00003446-200212000-00004', 'dev-kral-2000': '10.1093/cercor/10.7.714', 'dev-ching-2017': '10.1542/peds.2016-4274', 'dev-tomblin-2015': '10.1097/AUD.0000000000000219', 'dev-werker-2024': '10.1016/j.infbeh.2024.101935'}
DOIS['dev-bruner-2025']='10.1016/j.clinsp.2025.100841'
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
