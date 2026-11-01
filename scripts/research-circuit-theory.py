"""Cache author/official circuit sources with hashes; original diagrams are not copied."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/circuit-theory/sources';OUT.mkdir(parents=True,exist_ok=True)
COURSE='https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/resources/'
SOURCES={
'ct-lumped':'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l1/',
'ct-kirchhoff':COURSE+'03_kirchhoff1/',
'ct-node':COURSE+'nodal_mesh_methd/',
'ct-linear':COURSE+'linear_crct_ana/',
'ct-dependent':COURSE+'06_dep_source1/',
'ct-elements':COURSE+'capactr_inductr/',
'ct-impedance':COURSE+'09_sss/',
'ct-phasor':COURSE+'sss_phsor_impdce/',
'ct-filters':COURSE+'12_filters/',
'ct-resonance':COURSE+'resonance_qfactr/',
'ct-first':COURSE+'transient1_rl_rc/',
'ct-first-complete':COURSE+'trns1_rc_lc_rlc1/',
'ct-second':COURSE+'16_transint_rlc2/',
'ct-opamp':COURSE+'22_op_amps1/',
'ct-active':COURSE+'23_op_amps2/',
'ct-feedback':COURSE+'24_op_amps3/',
'ct-diode':COURSE+'17_diodes1/',
'ct-energy':'https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/resources/6002_l22/',
'ct-laplace':'https://eecs6302.mit.edu/_static/fall21/extras/siebert2.pdf',
'ct-mutual':'https://openstax.org/books/university-physics-volume-2/pages/14-1-mutual-inductance',
'ct-power':'https://openstax.org/books/university-physics-volume-2/pages/15-4-power-in-an-ac-circuit',
'ct-ti-specs':'https://www.ti.com/lit/an/sloa011b/sloa011b.pdf',
'ct-noise':'https://www.analog.com/en/resources/app-notes/an-940.html',
'ct-mic':'https://www.analog.com/en/resources/analog-dialogue/articles/understanding-microphone-sensitivity.html',
'ct-probe':'https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf',
}
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=35) as r:return r.read(),r.url
def fetch(item):
    key,url=item
    try:
        data,final=get(url);resource=url
        if '/resources/' in url:
            soup=BeautifulSoup(data,'html.parser')
            candidates=[urljoin(final,a.get('href','')) for a in soup.select('a[href]') if a.get('href','').split('?')[0].lower().endswith('.pdf')]
            if not candidates:raise ValueError('No PDF on course resource page')
            resource=candidates[0];data,final=get(resource)
        if data.startswith(b'%PDF'):
            path=OUT/(key+'.pdf');path.write_bytes(data)
            subprocess.run(['pdftotext','-layout',str(path),str(OUT/(key+'.txt'))],check=True,capture_output=True)
            text=(OUT/(key+'.txt')).read_text(encoding='utf-8')
        else:
            (OUT/(key+'.html')).write_bytes(data);soup=BeautifulSoup(data,'html.parser')
            main=soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            text=main.get_text('\n',strip=True);(OUT/(key+'.txt')).write_text(text,encoding='utf-8')
        return {'id':key,'url':url,'content_url':resource,'resolved_url':final,'status':'fetched','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'text_characters':len(text),'checked_at':'2026-11-02'}
    except Exception as e:return {'id':key,'url':url,'status':'failed','error':str(e)}
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,SOURCES.items()))
    (ROOT/'docs/research/circuit-theory-2026-11-02/source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for r in rows:print(r['id'],r['status'],r.get('text_characters',r.get('error')))
