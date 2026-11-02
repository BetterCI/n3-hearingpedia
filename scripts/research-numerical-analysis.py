"""Retrieve scoped author textbook chapters and official implementation documentation."""
from pathlib import Path
from urllib.request import Request,build_opener,ProxyHandler
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/numerical-analysis/sources';REC=ROOT/'docs/research/numerical-analysis-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
CHAPTERS=[
('na-float','floating-point','Floating-point numbers'),
('na-conditioning','conditioning','Problems and conditioning'),
('na-stability','stability','Stability'),
('na-condition-number','condition-number','Conditioning of linear systems'),
('na-pivoting','pivoting','Row pivoting'),
('na-qr','qr','The QR factorization'),
('na-svd','svd','Singular value decomposition'),
('na-fixed-point','fixed-point','Fixed-point iteration'),
('na-newton','newton','Newton’s method'),
('na-interp-stability','stability-1','Stability of polynomial interpolation'),
('na-splines','splines','Cubic splines'),
('na-fd','fd-converge','Convergence of finite differences'),
('na-integration','integration','Numerical integration'),
('na-adaptive','adaptive','Adaptive integration'),
('na-rk','rk','Runge–Kutta methods'),
('na-absstab','absstab-diffusion','Absolute stability'),
('na-stiff','stiffness','Stiffness'),
('na-bvp','linear','Collocation for linear problems'),
('na-cg','minrescg','MINRES and conjugate gradients'),
('na-precond','precond','Preconditioning')]
ROWS=[dict(id=i,title=t,url='https://fncbook.com/python/'+slug+'/',access='fulltext',kind='author_textbook') for i,slug,t in CHAPTERS]
ROWS += [dict(id=i,title=t,url=u,access='documentation',kind='official_API') for i,t,u in [
('na-brent-api','scipy.optimize.brentq','https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html'),
('na-interp-api','Interpolation (scipy.interpolate)','https://docs.scipy.org/doc/scipy/tutorial/interpolate.html'),
('na-ivp-api','scipy.integrate.solve_ivp','https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html'),
('na-sparse-api','scipy.sparse.linalg.spsolve','https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.spsolve.html'),
('na-cg-api','scipy.sparse.linalg.cg','https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html')]]
def fetch(row):
    try:
        p=OUT/(row['id']+'.html')
        if p.exists():data=p.read_bytes();final=row['url']
        else:
            op=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
            with op.open(Request(row['url'],headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=30) as r:data=r.read();final=r.url
        soup=BeautifulSoup(data,'html.parser')
        main=soup.select_one('article') or soup.select_one('main') or soup
        for el in main.select('script,style,nav'):el.decompose()
        txt=main.get_text(' ',strip=True)
        assert len(txt)>1800 and 'checking your browser' not in txt[:600].lower()
        p.write_bytes(data);(OUT/(row['id']+'.txt')).write_text(txt,encoding='utf-8')
        return dict(**row,status='fetched',resolved_url=final,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),checked_at='2026-11-02')
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:result=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(total=len(result),fetched=sum(r['status']=='fetched' for r in result),failures=[r for r in result if r['status']!='fetched'])))
