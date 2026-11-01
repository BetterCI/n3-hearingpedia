"""Cache primary functional-analysis teaching sources and metadata, not a literature review."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json,hashlib,subprocess,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/functional-analysis/sources';OUT.mkdir(parents=True,exist_ok=True)
REC=ROOT/'docs/research/functional-analysis-2026-11-02';REC.mkdir(parents=True,exist_ok=True)
INDEX='https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/pages/lecture-notes-and-readings/'
LECTURES={1:'fa-norm',2:'fa-operator',3:'fa-baire',4:'fa-inverse',5:'fa-hb',6:'fa-double',13:'fa-lp',14:'fa-hilbert',15:'fa-basis',16:'fa-fourier',17:'fa-riesz',18:'fa-adjoint',19:'fa-compact',20:'fa-spectrum',21:'fa-selfadj',22:'fa-spectral',23:'fa-dirichlet'}
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=40) as r:return r.read(),r.url
def sources():
    data,final=get(INDEX);(OUT/'course-index.html').write_bytes(data)
    soup=BeautifulSoup(data,'html.parser');out={}
    for a in soup.select('a[href]'):
        label=a.get_text(' ',strip=True);m=re.match(r'Lecture (\d+):',label)
        if m and '(PDF)' in label and int(m[1]) in LECTURES:
            out.setdefault(LECTURES[int(m[1])],urljoin(final,a['href']))
    if len(out)!=len(LECTURES):raise ValueError(out)
    out['fa-weak']='https://terrytao.wordpress.com/2009/02/21/245b-notes-11-the-strong-and-weak-topologies/'
    out['fa-lm']='https://www.math.ntnu.no/emner/MA8502/2024h/lectures/html/chapter_01/functional_analysis.html'
    data,url=get(out['fa-lm']);soup=BeautifulSoup(data,'html.parser')
    link=next(a for a in soup.select('a[href]') if 'brief review on function spaces' in a.get_text(' ',strip=True).lower())
    out['fa-sobolev']=urljoin(url,link['href'])
    out['fa-regularization']='https://www.imm.dtu.dk/~pcha/Regutools/RTv4manual.pdf'
    out['fa-fixedpoint']='https://wiki.math.ntnu.no/linearmethods/generalexistencetheorems'
    return out
def fetch(item):
    key,url=item
    try:
        data,final=get(url);resource=url
        if '/resources/' in url and not data.startswith(b'%PDF'):
            soup=BeautifulSoup(data,'html.parser')
            links=[urljoin(final,a['href']) for a in soup.select('a[href]') if a['href'].split('?')[0].lower().endswith('.pdf')]
            if not links:raise ValueError('Missing PDF')
            resource=links[0];data,final=get(resource)
        if data.startswith(b'%PDF'):
            p=OUT/(key+'.pdf');p.write_bytes(data);subprocess.run(['pdftotext','-layout',str(p),str(OUT/(key+'.txt'))],check=True,capture_output=True)
            txt=(OUT/(key+'.txt')).read_text(encoding='utf-8')
        else:
            (OUT/(key+'.html')).write_bytes(data);soup=BeautifulSoup(data,'html.parser');main=soup.select_one('main') or soup.select_one('article') or soup
            for el in main.select('script,style,nav'):el.decompose()
            txt=main.get_text('\n',strip=True);(OUT/(key+'.txt')).write_text(txt,encoding='utf-8')
        return dict(id=key,url=url,content_url=resource,resolved_url=final,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),checked_at='2026-11-02')
    except Exception as e:return dict(id=key,url=url,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,sources().items()))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for row in rows:print(row['id'],row['status'],row.get('text_characters',row.get('error')))
