"""Cache scoped author textbook pages, MIT lecture PDFs and official API docs."""
from pathlib import Path
from urllib.request import build_opener,ProxyHandler,Request
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
SLUG='differential-equations-and-dynamical-systems'
OUT=ROOT/'artifacts'/SLUG/'sources';REC=ROOT/'docs/research'/f'{SLUG}-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
BOOK=[
('dds-existence','slopefields_section','Slope fields; existence and uniqueness'),
('dds-separable','separable_section','Separable equations'),
('dds-linear','intfactor_section','Linear equations and the integrating factor'),
('dds-autonomous','auteq_section','Autonomous equations'),
('dds-second','sec_ccsol','Constant-coefficient second-order linear ODEs'),
('dds-forced','forcedo_section','Forced oscillations and resonance'),
('dds-systems','linsystems_section','Linear systems of ODEs'),
('dds-jordan','sec_multeigen','Repeated eigenvalues'),
('dds-linearization','linearization_section','Linearization, critical points, and equilibria'),
('dds-nonhyperbolic','nlinstability_section','Stability and classification of isolated critical points'),
('dds-limit','limitcycles_section','Limit cycles'),
('dds-heat','heateq_section','PDEs, separation of variables, and the heat equation'),
('dds-wave','we_section','One-dimensional wave equation')]
LECTURES=[
('dds-bifurcation','2-3','Flows and Bifurcations in One Dimension'),
('dds-phase','4-5','Pendulum and Stability in Two Dimensional Systems'),
('dds-contraction','6-7','Dissipation and Contraction of Volumes in Phase Space'),
('dds-cycle','8-9','Forced Oscillators and Limit Cycles'),
('dds-hopf','10-11','Bifurcations in Two Dimensions'),
('dds-poincare','15-16','Poincare Sections'),
('dds-lorenz','20-21','Lorenz Equations'),
('dds-lyap-exponent','24','Lyapunov Exponents'),
('dds-logistic','25-27','Period Doubling Route to Chaos')]
ROWS=[dict(id=i,title=t,url='https://www.jirka.org/diffyqs/html/'+s+'.html',kind='Lebl_author_textbook',access='fulltext') for i,s,t in BOOK]
ROWS += [dict(id=i,title=t,url='https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/resources/mit12_006jf22_lec'+n+'/',kind='MIT_Rothman',access='fulltext') for i,n,t in LECTURES]
ROWS += [
dict(id='dds-lyapunov',title='Lyapunov Analysis',url='https://underactuated.mit.edu/lyapunov.html',kind='MIT_Tedrake',access='fulltext'),
dict(id='dds-ivp-api',title='scipy.integrate.solve_ivp',url='https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html',kind='official_API',access='documentation')]
ROWS += [dict(id='dds-picard',title='Existence, Uniqueness, etc.',url='https://www.math.cmu.edu/~gautam/c/2026-632/notes/existence.html',kind='CMU_Iyer',access='fulltext')]
def get(url):
    op=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
    with op.open(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=40) as r:return r.read()
def fetch(row):
    try:
        path=OUT/(row['id']+'.html')
        data=path.read_bytes() if path.exists() else get(row['url']);path.write_bytes(data)
        soup=BeautifulSoup(data,'html.parser')
        record=dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),checked_at='2026-11-02')
        if row['kind']=='MIT_Rothman':
            links=[a.get('href') for a in soup.select('a[href]') if a.get('href','').split('?')[0].endswith('.pdf')]
            assert links,'No PDF linked'
            url=urljoin(row['url'],links[0]);pdfpath=OUT/(row['id']+'.pdf')
            pdf=pdfpath.read_bytes() if pdfpath.exists() else get(url);pdfpath.write_bytes(pdf)
            reader=PdfReader(io.BytesIO(pdf));text='\n'.join(p.extract_text() or '' for p in reader.pages)
            record.update(pdf_url=url,pdf_bytes=len(pdf),pdf_sha256=hashlib.sha256(pdf).hexdigest(),pdf_pages=len(reader.pages))
        else:
            main=soup.select_one('main') or soup.select_one('article') or soup
            for x in main.select('script,style,nav'):x.decompose()
            text=main.get_text(' ',strip=True)
        assert len(text)>1000,(row['id'],len(text))
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8');record['text_characters']=len(text)
        return record
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[r for r in rows if r['status']!='fetched'])))
