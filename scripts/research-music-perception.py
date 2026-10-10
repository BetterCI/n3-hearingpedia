"""Archive bibliographic records and original abstracts for the local music entry."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, urllib.request, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/music-perception-2026-10-10'
OUT.mkdir(parents=True,exist_ok=True)
DOIS={
 'music-dowling-1978':'10.1037/0033-295X.85.4.341',
 'music-krumhansl-1982':'10.1037/0033-295X.89.4.334',
 'music-large-1999':'10.1037/0033-295X.106.1.119',
 'music-nozaradan-2011':'10.1523/JNEUROSCI.0411-11.2011',
 'music-jacoby-2024':'10.1038/s41562-023-01800-9',
 'music-consonance-2010':'10.1016/j.cub.2010.04.019',
 'music-tsimane-2016':'10.1038/nature18635',
 'music-integration-2026':'10.1016/j.cognition.2025.106333',
 'music-song-2022':'10.1016/j.cub.2022.01.069',
 'music-salimpoor-2011':'10.1038/nn.2726',
 'music-cheung-2019':'10.1016/j.cub.2019.09.067',
 'music-mbea-2003':'10.1196/annals.1284.006',
 'music-proms-2012':'10.1371/journal.pone.0052508',
 'music-goldmsi-2014':'10.1371/journal.pone.0089642',
 'music-galvin-2007':'10.1097/01.aud.0000261689.35445.20',
 'music-kong-2004':'10.1097/01.aud.0000120365.97792.2f',
 'music-gfeller-2006':'10.1159/000095608',
 'music-timbre-ci-2008':'10.1121/1.2961171',
 'music-hearingaid-2014':'10.1177/2331216514558271',
 'music-mehr-2019':'10.1126/science.aax0868',
 'music-chen-2008':'10.1093/cercor/bhn042',
 'music-training-2018':'10.1177/2331216518759214',
 'music-mbea-ci-2008':'10.1097/AUD.0b013e318174e787',
}
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
with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(source,DOIS.items()))
(OUT/'verified-metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for r in rows:
 print(json.dumps({'id':r['id'],'title':(r.get('crossref') or {}).get('title'),
 'pmid':(r.get('europe_pmc') or {}).get('id'),'pmcid':(r.get('europe_pmc') or {}).get('pmcid'),
 'abstract':(r.get('europe_pmc') or {}).get('abstractText') or (r.get('crossref') or {}).get('abstract'),
 'errors':r['errors']},ensure_ascii=False))
