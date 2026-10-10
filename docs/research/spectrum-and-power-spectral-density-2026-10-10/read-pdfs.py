"""Fetch authoritative source PDFs and extract reading copies, not site figures."""
from pathlib import Path
import json
import sys
import urllib.request
from pypdf import PdfReader
sys.stdout.reconfigure(encoding='utf-8')
out=Path(__file__).resolve().parent
sources=[
 ('heinzel-2002','https://pure.mpg.de/pubman/item/item_152164_1/component/file_152163/395068.pdf'),
 ('harris-1978','https://www.fceia.unr.edu.ar/prodivoz/Harris_1978.pdf'),
 ('debiased-2024','https://spiral.imperial.ac.uk/server/api/core/bitstreams/d63ed9c7-28c7-47ab-9924-89f15d7523d6/content')
]
status=[]
for name,url in sources:
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Hearingpedia source verification'})
        with urllib.request.urlopen(req,timeout=30) as response: data=response.read()
        assert data[:4]==b'%PDF', 'Not a PDF'
        pdf=out/(name+'.pdf'); pdf.write_bytes(data)
        reader=PdfReader(pdf)
        text='\n\n'.join('=== PDF PAGE '+str(i+1)+' ===\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages))
        (out/(name+'-reading.txt')).write_text(text,encoding='utf-8')
        status.append({'name':name,'url':url,'status':'downloaded_and_extracted','pages':len(reader.pages),'reading_status':'not yet read; separate notes record ranges'})
    except Exception as e: status.append({'name':name,'url':url,'status':'failed','reason':str(e)})
(out/'pdf-access.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(status,ensure_ascii=False))
