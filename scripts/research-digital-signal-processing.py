"""Cache primary course PDFs and official implementation documentation."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import json,hashlib,subprocess,re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/digital-signal-processing/sources';REC=ROOT/'docs/research/digital-signal-processing-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
INDEX='https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/pages/lecture-notes/'
LECT={7:'dsp-structures',15:'dsp-dft',17:'dsp-spectral',18:'dsp-periodogram',9:'dsp-fir',2:'dsp-phase',8:'dsp-iir',16:'dsp-block',21:'dsp-stft',5:'dsp-rates',10:'dsp-polyphase',6:'dsp-quant'}
APIS={'periodogram':'dsp-periodogram-api','firwin':'dsp-firwin-api','butter':'dsp-butter-api','filtfilt':'dsp-filtfilt-api','stft':'dsp-stft-api','upfirdn':'dsp-upfirdn-api','welch':'dsp-welch-api','resample_poly':'dsp-resample-api','sosfilt':'dsp-sos-api'}
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source check'}),timeout=45) as r:return r.read(),r.url
def fetch(row):
    try:
        data,final=get(row['url']);resource=row['url']
        if 'ocw.mit.edu' in final and not data.startswith(b'%PDF'):
            soup=BeautifulSoup(data,'html.parser')
            a=next(a for a in soup.select('a[href]') if a['href'].split('?')[0].lower().endswith('.pdf'))
            resource=urljoin(final,a['href']);data,final=get(resource)
        if data.startswith(b'%PDF'):
            p=OUT/(row['id']+'.pdf');p.write_bytes(data)
            subprocess.run(['pdftotext','-layout',str(p),str(OUT/(row['id']+'.txt'))],capture_output=True,check=True)
            txt=(OUT/(row['id']+'.txt')).read_text(encoding='utf-8');access='fulltext'
        else:
            (OUT/(row['id']+'.html')).write_bytes(data);soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('article') or soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            txt=main.get_text('\n',strip=True);(OUT/(row['id']+'.txt')).write_text(txt,encoding='utf-8');access='documentation'
            assert len(txt)>1000 and 'checking your browser' not in txt[:500].lower()
        return dict(**row,content_url=resource,resolved_url=final,status='fetched',access=access,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),copyright_omission_notice=bool(re.search(r'removed.*copyright',txt,re.I)),checked_at='2026-11-02')
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    data,final=get(INDEX);(OUT/'lecture-index.html').write_bytes(data);soup=BeautifulSoup(data,'html.parser');rows=[]
    for tr in soup.select('tr'):
        td=tr.select('td')
        if not td:continue
        n=td[0].get_text(strip=True)
        if not n.isdigit() or int(n) not in LECT:continue
        rows.append(dict(id=LECT[int(n)],lecture=int(n),title=re.sub(r'\s*\(\s*PDF\s*\)','',td[1].get_text(' ',strip=True)),url=urljoin(final,td[1].select_one('a[href]')['href'])))
    assert len(rows)==len(LECT)
    rows.extend(dict(id=key,title='scipy.signal.'+name,url='https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.'+name+'.html') for name,key in APIS.items())
    rows.append(dict(id='dsp-adaptive',title='Adaptive Filtering',url='https://home.engineering.iastate.edu/julied/classes/ee524/LectureNotes/l11.pdf'))
    with ThreadPoolExecutor(max_workers=6) as pool:result=list(pool.map(fetch,rows))
    (REC/'source-index.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([dict(id=r['id'],status=r['status'],characters=r.get('text_characters'),error=r.get('error'),omissions=r.get('copyright_omission_notice')) for r in result]))
