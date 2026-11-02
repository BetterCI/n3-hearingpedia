"""Retrieve official lecture PDFs and implementation documentation; preserve hashes."""
from pathlib import Path
from urllib.request import build_opener,ProxyHandler,Request
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/control-theory/sources';REC=ROOT/'docs/research/control-theory-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
HALL=[
('ctrl-feedback',2,'Block diagrams, the effect of feedback'),
('ctrl-model',3,'Modeling principles'),
('ctrl-response',5,'Dynamic response of closed-loop systems'),
('ctrl-time',6,'Time-domain specifications'),
('ctrl-stability',8,'The Routh criterion'),
('ctrl-errors',9,'Effect of noise, steady-state errors'),
('ctrl-pid',10,'PID control'),
('ctrl-root',11,'The root locus method'),
('ctrl-nyquist',20,'The Nyquist stability criterion'),
('ctrl-margins',23,'Stability margins, Bode gain-phase theorem'),
('ctrl-digital',29,'Digital control, the z-transform'),
('ctrl-hold',31,'Compensator design examples, time delay of ZOH')]
HOW=[
('ctrl-state',5,'Introduction to state-space models'),
('ctrl-controllability',10,'Controllability'),
('ctrl-observer',14,'Open-loop and closed-loop estimators'),
('ctrl-separation',15,'Combined estimators and regulators'),
('ctrl-lqr',18,'Deterministic linear quadratic regulator'),
('ctrl-windup',23,'Anti-windup')]
ROWS=[dict(id=i,title=t,url='https://ocw.mit.edu/courses/16-06-principles-of-automatic-control-fall-2012/resources/mit16_06f12_lecture_'+str(n)+'/',kind='MIT_Hall',access='fulltext') for i,n,t in HALL]
ROWS += [dict(id=i,title=t,url='https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/resources/mit16_30f10_lec'+str(n).zfill(2)+'/',kind='MIT_How_Frazzoli',access='fulltext') for i,n,t in HOW]
ROWS += [dict(id=i,title=t,url=u,kind=k,access='documentation' if k=='official_API' else 'fulltext') for i,t,u,k in [
('ctrl-lyapunov','Lyapunov Analysis','https://underactuated.mit.edu/lyapunov.html','MIT_Tedrake'),
('ctrl-are-api','scipy.linalg.solve_continuous_are','https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve_continuous_are.html','official_API'),
('ctrl-place-api','scipy.signal.place_poles','https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.place_poles.html','official_API'),
('ctrl-discrete-api','scipy.signal.cont2discrete','https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cont2discrete.html','official_API')]]
ROWS += [
dict(id='ctrl-robust',title='Stability robustness (Chapter 20)',url='https://ocw.mit.edu/courses/6-241j-dynamic-systems-and-control-spring-2011/resources/mit6_241js11_chap20/',kind='MIT_textbook',access='fulltext'),
dict(id='ctrl-lqr-conditions',title='Feedback Control Systems, Recitation 7: LQR',url='https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/c2c336c787d150d55873a98dfbd75e0f_MIT16_30F10_rec07.pdf',kind='MIT_recitation',access='fulltext')]
def fetch_data(url):
    op=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
    with op.open(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source check'}),timeout=40) as r:return r.read()
def fetch(row):
    try:
        direct_pdf=row['url'].endswith('.pdf')
        path=OUT/(row['id']+('.pdf' if direct_pdf else '.html'))
        data=path.read_bytes() if path.exists() else fetch_data(row['url']);path.write_bytes(data)
        result=dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),checked_at='2026-11-02')
        if direct_pdf:
            text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(data)).pages)
        elif row['kind'] in ['MIT_Hall','MIT_How_Frazzoli','MIT_textbook']:
            soup=BeautifulSoup(data,'html.parser')
            links=[a.get('href') for a in soup.select('a[href]') if a.get('href','').split('?')[0].endswith('.pdf')]
            assert links,'No PDF linked from resource page'
            url=urljoin(row['url'],links[0]);pdf_path=OUT/(row['id']+'.pdf')
            pdf=pdf_path.read_bytes() if pdf_path.exists() else fetch_data(url);pdf_path.write_bytes(pdf)
            text='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(pdf)).pages)
            result.update(pdf_url=url,pdf_bytes=len(pdf),pdf_sha256=hashlib.sha256(pdf).hexdigest())
        else:
            soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('article') or soup.select_one('main') or soup
            for x in main.select('nav,script,style'):x.decompose()
            text=main.get_text(' ',strip=True)
        assert len(text)>700,(row['id'],len(text))
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8')
        result['text_characters']=len(text);return result
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[r for r in rows if r['status']!='fetched'])))
