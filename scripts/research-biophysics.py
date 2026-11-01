"""Cache author/official teaching sources and original-paper metadata for biophysics."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request,urlopen
from urllib.parse import urljoin,quote
from bs4 import BeautifulSoup
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/biophysics/sources';REC=ROOT/'docs/research/biophysics-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
INDEX='https://ocw.mit.edu/courses/20-430j-fields-forces-and-flows-in-biological-systems-fall-2015/pages/lecture-slides/'
LECT={1:'bp-overview',2:'bp-boltzmann',3:'bp-brownian',4:'bp-fick',6:'bp-binding',9:'bp-electric',10:'bp-migration',11:'bp-electrochem',16:'bp-viscosity',17:'bp-stokes',19:'bp-peclet'}
def get(url):
    with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 Hearingpedia source verification'}),timeout=45) as r:return r.read(),r.url
def sources():
    data,final=get(INDEX);(OUT/'course-index.html').write_bytes(data);soup=BeautifulSoup(data,'html.parser');result={}
    for row in soup.select('tr'):
        cells=row.select('td')
        if not cells:continue
        key=cells[0].get_text(' ',strip=True)
        if key.isdigit() and int(key) in LECT:
            a=row.select_one('a[href]');result[LECT[int(key)]]=urljoin(final,a['href'])
    assert len(result)==len(LECT),result
    for key,sec in [('bp-nernst','2.S1'),('bp-passive','1.S3'),('bp-hh','2.S2'),('bp-synapse','3.S1'),('bp-cable','3.S2')]:
        result[key]='https://neuronaldynamics.epfl.ch/online/Ch'+sec+'.html'
    result['bp-goldman']='https://pmc.ncbi.nlm.nih.gov/articles/PMC2142582/'
    result['bp-endocochlear']='https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='+quote('EXT_ID:18218777 AND SRC:MED')+'&format=json&resultType=core'
    result['bp-ribbon']='https://neuroscience.jhu.edu/files2/publications_Fuchs_P_Fuchs_PA_Nature_Neuroscience_5_147_154.pdf'
    result['bp-hair-text']='https://nba.uth.tmc.edu/neuroscience/s2/chapter12.html'
    for key,q in [('bp-prestin','EXT_ID:10821263 AND SRC:MED'),('bp-prestin-knockout','EXT_ID:12239568 AND SRC:MED'),('bp-met-original','DOI:10.1073/pnas.74.6.2407')]:
        result[key]='https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='+quote(q)+'&format=json&resultType=core'
    result['bp-osmosis']='https://openstax.org/books/chemistry-2e/pages/11-4-colligative-properties'
    return result
def fetch(item):
    key,url=item
    try:
        data,final=get(url);resource=url;access='fulltext'
        if '/resources/' in url and not data.startswith(b'%PDF'):
            soup=BeautifulSoup(data,'html.parser')
            links=[urljoin(final,a['href']) for a in soup.select('a[href]') if a['href'].split('?')[0].lower().endswith('.pdf')]
            if not links:raise ValueError('No PDF link on resource')
            resource=links[0];data,final=get(resource)
        if data.startswith(b'%PDF'):
            p=OUT/(key+'.pdf');p.write_bytes(data);subprocess.run(['pdftotext','-layout',str(p),str(OUT/(key+'.txt'))],check=True,capture_output=True)
            txt=(OUT/(key+'.txt')).read_text(encoding='utf-8')
        elif 'europepmc' in url and 'format=json' in url:
            (OUT/(key+'.json')).write_bytes(data);obj=json.loads(data);paper=obj['resultList']['result'][0]
            txt=json.dumps(paper,ensure_ascii=False,indent=2);(OUT/(key+'.txt')).write_text(txt,encoding='utf-8');access='abstract'
        else:
            (OUT/(key+'.html')).write_bytes(data);soup=BeautifulSoup(data,'html.parser');main=soup.select_one('article') or soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            txt=main.get_text('\n',strip=True);(OUT/(key+'.txt')).write_text(txt,encoding='utf-8')
            if 'checking your browser' in txt[:500].lower() or 'captcha' in txt[:200].lower():raise ValueError('Access challenge, not source text')
            if key=='bp-goldman':access='abstract' # historical HTML abstract; original paper pages are scanned.
        return dict(id=key,url=url,content_url=resource,resolved_url=final,status='fetched',access=access,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(txt),checked_at='2026-11-02')
    except Exception as e:return dict(id=key,url=url,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(fetch,sources().items()))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for row in rows:print(row['id'],row['status'],row.get('text_characters',row.get('error')))
