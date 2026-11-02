"""Fetch official source files; no third-party textbook copies."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json,hashlib,subprocess,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/signals-and-systems/sources';REC=ROOT/'docs/research/signals-and-systems-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
INDEX='https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/lecture-notes/'
LECT={1:'ss-intro',2:'ss-dt',4:'ss-ct',8:'ss-convolution',9:'ss-frequency',15:'ss-fs',16:'ss-ft',17:'ss-dtft',19:'ss-relations',5:'ss-z',6:'ss-laplace',21:'ss-sampling',22:'ss-quantization',10:'ss-feedback',7:'ss-numerics'}
EXTRAS=[
    dict(id='ss-basic-signals',lecture=2,title='Signals and systems: Part I',url='https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec02-1/'),
    dict(id='ss-properties',lecture=3,title='Signals and systems: Part II',url='https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec03-1/'),
    dict(id='ss-lti',lecture=5,title='Properties of linear, time-invariant systems',url='https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec05-1/')
]
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source audit'}),timeout=45) as r:return r.read(),r.url
def fetch(row):
    try:
        data,final=get(row['url']);resource=row['url']
        if not data.startswith(b'%PDF'):
            s=BeautifulSoup(data,'html.parser')
            a=next(a for a in s.select('a[href]') if a['href'].split('?')[0].lower().endswith('.pdf'))
            resource=urljoin(final,a['href']);data,final=get(resource)
        assert data.startswith(b'%PDF')
        p=OUT/(row['id']+'.pdf');p.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(p),str(OUT/(row['id']+'.txt'))],capture_output=True,check=True)
        txt=(OUT/(row['id']+'.txt')).read_text(encoding='utf-8')
        return dict(**row,content_url=resource,resolved_url=final,access='fulltext',status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),copyright_omission_notice=bool(re.search(r'removed.*copyright',txt,re.I)),checked_at='2026-11-02')
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    data,final=get(INDEX);(OUT/'lecture-index.html').write_bytes(data);soup=BeautifulSoup(data,'html.parser');rows=[]
    for tr in soup.select('tr'):
        td=tr.select('td')
        if not td:continue
        n=td[0].get_text(strip=True)
        if not n.isdigit() or int(n) not in LECT:continue
        a=td[1].select_one('a[href]')
        rows.append(dict(id=LECT[int(n)],lecture=int(n),title=re.sub(r'\s*\(PDF.*?\)','',a.get_text(' ',strip=True)),url=urljoin(final,a['href'])))
    assert len(rows)==len(LECT)
    rows.extend(EXTRAS)
    with ThreadPoolExecutor(max_workers=6) as pool:result=list(pool.map(fetch,rows))
    (REC/'source-index.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([dict(id=r['id'],status=r['status'],characters=r.get('text_characters'),omissions=r.get('copyright_omission_notice'),error=r.get('error')) for r in result]))
