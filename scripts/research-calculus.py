"""Cache official textbook sections and numerical API documentation for a scoped audit."""
from pathlib import Path
from urllib.request import Request,build_opener,ProxyHandler
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/calculus/sources';REC=ROOT/'docs/research/calculus-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
SECTIONS=[
('calc-functions',1,'1-1-review-of-functions','1.1 Review of Functions'),
('calc-limit',1,'2-5-the-precise-definition-of-a-limit','2.5 The Precise Definition of a Limit'),
('calc-continuity',1,'2-4-continuity','2.4 Continuity'),
('calc-derivative',1,'3-1-defining-the-derivative','3.1 Defining the Derivative'),
('calc-rules',1,'3-6-the-chain-rule','3.6 The Chain Rule'),
('calc-mvt',1,'4-4-the-mean-value-theorem','4.4 The Mean Value Theorem'),
('calc-taylor',2,'6-3-taylor-and-maclaurin-series','6.3 Taylor and Maclaurin Series'),
('calc-integral',1,'5-2-the-definite-integral','5.2 The Definite Integral'),
('calc-ftc',1,'5-3-the-fundamental-theorem-of-calculus','5.3 The Fundamental Theorem of Calculus'),
('calc-techniques',2,'3-1-integration-by-parts','3.1 Integration by Parts'),
('calc-improper',2,'3-7-improper-integrals','3.7 Improper Integrals'),
('calc-series',2,'5-2-infinite-series','5.2 Infinite Series'),
('calc-partial',3,'4-3-partial-derivatives','4.3 Partial Derivatives'),
('calc-differentiable',3,'4-4-tangent-planes-and-linear-approximations','4.4 Tangent Planes and Linear Approximations'),
('calc-gradient',3,'4-6-directional-derivatives-and-the-gradient','4.6 Directional Derivatives and the Gradient'),
('calc-multiple',3,'5-1-double-integrals-over-rectangular-regions','5.1 Double Integrals over Rectangular Regions'),
('calc-ode',2,'4-5-first-order-linear-equations','4.5 First-order Linear Equations'),
('calc-numerical',2,'3-6-numerical-integration','3.6 Numerical Integration'),
('calc-substitution',1,'5-5-substitution','5.5 Substitution'),
('calc-polar',3,'5-3-double-integrals-in-polar-coordinates','5.3 Double Integrals in Polar Coordinates'),
]
ROWS=[dict(id=i,title=t,volume=v,url=f'https://openstax.org/books/calculus-volume-{v}/pages/{slug}',access='fulltext') for i,v,slug,t in SECTIONS]
ROWS+=[dict(id='calc-ivp-api',title='scipy.integrate.solve_ivp',url='https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html',access='documentation')]
ROWS+=[dict(id='calc-trapezoid-api',title='scipy.integrate.trapezoid',url='https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.trapezoid.html',access='documentation')]
def fetch(row):
    try:
        cached=OUT/(row['id']+'.html')
        if cached.exists():
            data=cached.read_bytes();final=row['url']
        else:
            opener=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
            with opener.open(Request(row['url'],headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=30) as r:data=r.read();final=r.url
        soup=BeautifulSoup(data,'html.parser')
        main=soup.select_one('[data-type="page"]') or soup.select_one('article') or soup.select_one('main') or soup
        for el in main.select('script,style,nav'):el.decompose()
        txt=main.get_text('\n',strip=True)
        assert len(txt)>1800 and 'checking your browser' not in txt[:500].lower()
        (OUT/(row['id']+'.html')).write_bytes(data);(OUT/(row['id']+'.txt')).write_text(txt,encoding='utf-8')
        return dict(**row,status='fetched',resolved_url=final,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),checked_at='2026-11-02')
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:result=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(total=len(result),fetched=sum(r['status']=='fetched' for r in result),failures=[r for r in result if r['status']!='fetched'])))
