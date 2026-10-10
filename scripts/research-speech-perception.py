"""Archive public bibliographic metadata and abstracts for this editorial draft."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, urllib.request, urllib.parse, shutil, os

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/research/speech-perception-2026-10-10'
OUT.mkdir(parents=True, exist_ok=True)
DOIS = {
 'speech-shortlist-2008':'10.1037/0033-295X.115.2.357',
 'speech-trace-1986':'10.1016/0010-0285(86)90015-0',
 'speech-oden-1978':'10.1037/0033-295X.85.3.172',
 'speech-liberman-1957':'10.1037/h0044417',
 'speech-mcmurray-2002':'10.1016/S0010-0277(02)00157-9',
 'speech-ganong-1980':'10.1037/0096-1523.6.1.110',
 'speech-kleinschmidt-2015':'10.1037/a0038695',
 'speech-norris-2003':'10.1016/S0010-0285(03)00006-9',
 'speech-saffran-1996':'10.1126/science.274.5294.1926',
 'speech-werker-1984':'10.1121/1.390988',
 'speech-dev-1984':'10.1016/S0163-6383(84)80022-3',
 'speech-mcgurk-1976':'10.1038/264746a0',
 'speech-language-2025':'10.1038/s41586-025-09748-8',
 'speech-motor-1985':'10.1016/0010-0277(85)90021-6',
 'speech-reduction-2021':'10.3758/s13423-021-01924-x',
}
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Hearingpedia editorial source verification'})
 with urllib.request.urlopen(req,timeout=25) as response:return json.load(response)
def source(item):
 key,doi=item
 result={'id':key,'doi':doi,'checked_at':'2026-10-10','errors':[]}
 try:
  msg=fetch('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))['message']
  result['crossref']={k:msg.get(k) for k in ['title','author','container-title','published','published-online','published-print','volume','issue','page','URL','type']}
 except Exception as e:result['errors'].append('Crossref: '+str(e))
 try:
  query=urllib.parse.urlencode({'query':'DOI:"'+doi+'"','format':'json','resultType':'core','pageSize':1})
  records=fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+query)['resultList']['result']
  result['europe_pmc']=records[0] if records else None
 except Exception as e:result['errors'].append('Europe PMC: '+str(e))
 return result
with ThreadPoolExecutor(max_workers=5) as pool:records=list(pool.map(source,DOIS.items()))
(OUT/'verified-metadata.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for name in ['openalex','backward']:
 path=Path(os.environ['TEMP'])/('hearingpedia-speech-'+name+'.json')
 if path.exists():shutil.copyfile(path,OUT/(name+'.json'))
print(json.dumps([{'id':r['id'],'title':(r.get('crossref') or {}).get('title'),
 'pmid':(r.get('europe_pmc') or {}).get('id'), 'abstract':(r.get('europe_pmc') or {}).get('abstractText'),
 'errors':r['errors']} for r in records],ensure_ascii=True))
