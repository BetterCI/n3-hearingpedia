"""Retrieve primary-study abstracts and metadata; no secrets or private data."""
import concurrent.futures, json, sys, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).parent
QUERIES = {
 'wilson': 'EXT_ID:1857418 AND SRC:MED',
 'abi': 'EXT_ID:19546832 AND SRC:MED',
 'ami': 'EXT_ID:16936570 AND SRC:MED',
 'opto': 'EXT_ID:31036812 AND SRC:MED',
 'kell': 'DOI:10.1016/j.neuron.2018.03.044',
 'roux': 'DOI:10.1016/j.cell.2006.08.040',
 'almoyed': 'DOI:10.15252/emmm.201809396',
 'jiang': 'DOI:10.1038/s41586-026-10393-y',
 'regeneration': 'DOI:10.1093/pnasnexus/pgae445',
 'brons': 'DOI:10.1177/2331216514553924',
 'wu': 'DOI:10.1097/AUD.0000000000000672',
 'shannon': 'TITLE:"Speech recognition with primarily temporal cues"',
 'niparko': 'TITLE:"Spoken language development in children following cochlear implantation"',
 'hybrid': 'DOI:10.1002/lary.25451',
 'friesen': 'DOI:10.1121/1.1381538',
}

def get(item):
 key, query = item
 url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query':query,'format':'json','resultType':'core','pageSize':3})
 try:
  with urllib.request.urlopen(url,timeout=35) as r: data=json.load(r)
  rows=data.get('resultList',{}).get('result',[])
  record={'key':key,'query':query,'url':url,'checked_at':'2026-11-24','records':rows}
  (OUT/(key+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
  return {'key':key,'results':[{'title':r.get('title'),'authors':r.get('authorString'),'year':r.get('pubYear'),'doi':r.get('doi'),'pmcid':r.get('pmcid'),'abstract':r.get('abstractText')} for r in rows]}
 except Exception as e: return {'key':key,'error':str(e)}

if __name__=='__main__':
 sys.stdout.reconfigure(encoding='utf-8')
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for result in pool.map(get,QUERIES.items()): print(json.dumps(result,ensure_ascii=False))
