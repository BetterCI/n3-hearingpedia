"""Cache primary teaching/handbook sources for targeted mathematical audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/mathematical-physics-methods/sources';OUT.mkdir(parents=True,exist_ok=True)
REC=ROOT/'docs/research/mathematical-physics-methods-2026-11-02';REC.mkdir(parents=True,exist_ok=True)
MIT='https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/resources/'
IV='https://www.math.toronto.edu/ivrii/PDE-textbook/'
SOURCES={
'mm-problem':IV+'Chapter1/S1.2.html',
'mm-classify':IV+'Chapter1/S1.3.html',
'mm-heat':MIT+'heateqni/',
'mm-wave':MIT+'waveeqni/',
'mm-multi':MIT+'pde3d/',
'mm-fourier':MIT+'fourtran/',
'mm-green':MIT+'greensfn/',
'mm-sl':IV+'Chapter4/S4.2.html',
'mm-orthogonal':IV+'Chapter4/S4.3.html',
'mm-coordinates':IV+'Chapter6/S6.3.html',
'mm-energy':IV+'Chapter2/S2.7.html',
'mm-variational':IV+'Chapter10/S10.1.html',
'mm-distribution':IV+'Chapter11/S11.1.html',
'mm-bessel':'https://dlmf.nist.gov/10.2',
'mm-bessel-zeros':'https://dlmf.nist.gov/10.21',
'mm-bessel-integral':'https://dlmf.nist.gov/10.22',
'mm-legendre':'https://dlmf.nist.gov/14.2',
'mm-harmonics':'https://dlmf.nist.gov/14.30',
'mm-laplace':'https://eecs6302.mit.edu/_static/fall21/extras/siebert2.pdf',
'mm-numerics':'https://math.mit.edu/icg/resources/notes325.pdf',
}
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=40) as r:return r.read(),r.url
def fetch(item):
    key,url=item
    try:
        data,final=get(url);resource=url
        if '/resources/' in url and not data.startswith(b'%PDF'):
            soup=BeautifulSoup(data,'html.parser')
            links=[urljoin(final,a['href']) for a in soup.select('a[href]') if a['href'].split('?')[0].lower().endswith('.pdf')]
            if not links:raise ValueError('Missing PDF link')
            resource=links[0];data,final=get(resource)
        if data.startswith(b'%PDF'):
            p=OUT/(key+'.pdf');p.write_bytes(data)
            subprocess.run(['pdftotext','-layout',str(p),str(OUT/(key+'.txt'))],check=True,capture_output=True)
            txt=(OUT/(key+'.txt')).read_text(encoding='utf-8')
        else:
            (OUT/(key+'.html')).write_bytes(data);soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            txt=main.get_text('\n',strip=True);(OUT/(key+'.txt')).write_text(txt,encoding='utf-8')
        return dict(id=key,url=url,content_url=resource,resolved_url=final,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),checked_at='2026-11-02')
    except Exception as e:return dict(id=key,url=url,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,SOURCES.items()))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for row in rows:print(row['id'],row['status'],row.get('text_characters',row.get('error')))
