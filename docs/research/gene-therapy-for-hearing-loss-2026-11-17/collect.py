import json, urllib.request, urllib.parse, pathlib, concurrent.futures
out=pathlib.Path('docs/research/gene-therapy-for-hearing-loss-2026-11-17')
qs={'roux':'DOI:10.1016/j.cell.2006.08.040','lv':'DOI:10.1016/S0140-6736(23)02874-X','wang':'DOI:10.1038/s41591-024-03023-5','dboto':'DOI:10.1056/NEJMoa2400521','jiang':'DOI:10.1038/s41586-026-10393-y','sequential':'DOI:10.1038/s41591-026-04505-4','akil':'TITLE:"Dual AAV-mediated gene therapy restores hearing in a DFNB9 mouse model"','almoyed':'TITLE:"A dual-AAV approach restores fast exocytosis"','gao':'TITLE:"Treatment of autosomal dominant hearing loss by in vivo delivery"','yeh':'TITLE:"In vivo base editing restores sensory transduction"','askew':'TITLE:"Tmc gene therapy restores auditory function"','dbmouse':'TITLE:"Functional, sustained recovery of hearing"','regeneration':'TITLE:"Atoh1" AND TITLE:"Gfi1" AND TITLE:"Pou4f3"','qi':'TITLE:"AAV-mediated gene therapy restores hearing" AND FIRST_PDATE:[2025-01-01 TO 2025-12-31]'}
def run(it):
 k,q=it; u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=3&query='+urllib.parse.quote(q)
 try:
  d=json.load(urllib.request.urlopen(u,timeout=35)); (out/(k+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
  return k,[{'title':x['title'],'doi':x.get('doi'),'author':x.get('authorString'),'year':x.get('pubYear'),'journal':x.get('journalInfo',{}).get('journal',{}).get('title'),'abstract':x.get('abstractText'),'pmcid':x.get('pmcid')} for x in d['resultList']['result']]
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for k,v in ex.map(run,qs.items()):print(json.dumps({k:v},ensure_ascii=False))
