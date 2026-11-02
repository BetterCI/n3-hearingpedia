"""Cache and hash scoped primary teaching sources and official API documentation."""
from pathlib import Path
from urllib.request import Request,build_opener,ProxyHandler
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json,hashlib,io
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/optimization-methods/sources'
REC=ROOT/'docs/research/optimization-methods-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
LECTURES=[
('opt-intro','L01_introduction','Introduction'),
('opt-first','L02_first_order_optimality_conditions','First-order optimality conditions'),
('opt-convex','L04_convex_functions','Convex functions and sufficiency of normal cones'),
('opt-kkt','L07_kkt','Functional constraints, Lagrange multipliers, and KKT conditions'),
('opt-dual','L08_lagrangian_duality','Lagrangian duality'),
('opt-gradient','L12_gradient_descent','Gradient descent and descent lemmas'),
('opt-projection','L14_mirror_descent','Projected gradient descent and mirror descent'),
('opt-sgd','L15_sgd','Stochastic gradient descent and empirical risk minimization'),
('opt-newton','L17_newton','Hessians, preconditioning, and Newton’s method'),
('opt-barrier','L20_barrier','Central path and interior-point methods')]
ROWS=[dict(id=i,title=t,url='https://www.mit.edu/~gfarina/2025/67220s25_'+s+'/',kind='MIT_lecture',access='fulltext') for i,s,t in LECTURES]
ROWS += [dict(id=i,title=t,url=u,kind=k,access='documentation' if k=='official_API' else 'fulltext') for i,t,u,k in [
('opt-prox','Proximal Gradient Descent (and Acceleration)','https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/prox-grad.pdf','CMU_lecture'),
('opt-bfgs','Quasi-Newton Methods','https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/quasi-newton.pdf','CMU_lecture'),
('opt-subgrad','Subgradient Methods','https://web.stanford.edu/class/ee364b/lectures/subgrad_method_notes.pdf','Stanford_notes'),
('opt-nlsq','Nonlinear least squares','https://fncbook.com/python/nlsq/','author_textbook'),
('opt-minimize-api','scipy.optimize.minimize','https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html','official_API'),
('opt-slsqp-api','minimize(method=SLSQP)','https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html','official_API'),
('opt-lsq-api','scipy.optimize.least_squares','https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html','official_API')]]
def get(url):
    op=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
    with op.open(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source check'}),timeout=40) as r:
        return r.read(),r.url
def fetch(row):
    try:
        ext='.pdf' if row['url'].endswith('.pdf') else '.html'
        path=OUT/(row['id']+ext)
        data=path.read_bytes() if path.exists() else get(row['url'])[0]
        path.write_bytes(data)
        text=''
        pdf_url=None
        if ext=='.html':
            soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('article') or soup.select_one('main') or soup
            for x in main.select('script,style,nav'):x.decompose()
            text=main.get_text(' ',strip=True)
            if row['kind']=='MIT_lecture':
                links=[a.get('href') for a in soup.select('a[href]') if '.pdf' in a.get('href','')]
                assert links, 'missing lecture PDF'
                pdf_url=urljoin(row['url'],links[0]);pdf_path=OUT/(row['id']+'.pdf')
                pdf=pdf_path.read_bytes() if pdf_path.exists() else get(pdf_url)[0]
                pdf_path.write_bytes(pdf)
                # The HTML font remaps letters to private-use glyphs; use the
                # linked author PDF's readable text for scientific inspection.
                text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(pdf)).pages)
        else:text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(data)).pages)
        assert len(text)>1800,(row['id'],len(text))
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8')
        result=dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(text),checked_at='2026-11-02')
        if pdf_url:result.update(pdf_url=pdf_url,pdf_bytes=len(pdf),pdf_sha256=hashlib.sha256(pdf).hexdigest())
        return result
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[r for r in rows if r['status']!='fetched'])))
