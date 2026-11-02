"""Scoped author lecture notes, original papers and official solver documentation."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import subprocess,json,hashlib,io
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/nonlinear-dynamics/sources';REC=ROOT/'docs/research/nonlinear-dynamics-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
def get(url):
    errors=[]
    for proxy in [[],['--proxy','http://127.0.0.1:7897']]:
        r=subprocess.run(['curl.exe','-fLsS','--connect-timeout','8','--max-time','35',*proxy,url],capture_output=True,timeout=40)
        if r.returncode==0:return r.stdout
        errors.append(r.stderr.decode(errors='replace'))
    raise RuntimeError(str(errors))
ROWS=[]
for id,title,num,support in [
('scalar','Flows and Bifurcations in One Dimension','2-3','标量流、分岔分支与滞后；本文另选固定参数截面并推导折点和瓶颈时间。'),
('phase','Pendulum and Stability in Two Dimensional Systems','4-5','相空间、势能、稳定与吸引域；区分局部稳定、多稳态和全局结论。'),
('dissipation','Dissipation and Contraction of Volumes in Phase Space','6-7','散度、相体积收缩；负散度不推出所有方向收缩或混沌。'),
('cycles','Forced Oscillators and Limit Cycles','8-9','自持与强迫振荡、极限环及Van der Pol；本篇参数、能量与数值另行计算。'),
('hopf','Bifurcations in Two Dimensions','10-11','超/亚临界Hopf、环的折叠；不沿用讲义鞍结小节mu符号笔误。'),
('spectral','Spectral Analysis for Dynamical Systems','12-14','频谱与动力学观察，谱线和连续谱的解释；宽谱不当作混沌充分证据。'),
('poincare','Poincaré Sections','15-16','横截面、返回映射、周期轨道与乘子；本文Hopf乘子用变分方程独立核对。'),
('strange','Introduction to Strange Attractors','19','吸引子、几何与不规则轨道；不凭投影形状证明混沌。'),
('lorenz','Lorenz Equations','20-21','Lorenz模型、平衡、耗散与参数；本篇QR指数为有限时长数值而非定理证明。'),
('lyapunov','Lyapunov Exponents','24','沿轨道变分、重归一化与长期平均；正指数不能脱离有界、典型轨道等背景解释。'),
('maps','Period Doubling Route to Chaos','25-27','Logistic映射、周期乘子、倍周期与窗口；r=4典型指数与特殊轨道分开。'),
('intermittency','Intermittency (and Quasiperiodicity)','28','间歇、准周期及不同混沌路径；不声称复杂系统都走同一路径。')]:
    ROWS.append(dict(id='nd-'+id,title=title,authors='Daniel H. Rothman',year='2022',publication='MIT 12.006J/18.353J/2.050J，作者官方课程讲义',url='https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec'+num+'.pdf',supports=support,kind='author_lecture',access='fulltext'))
for id,title,resource,support in [
('normalforms','Bifurcations: Baby Normal Forms','babynormalforms','正规形与非退化条件、局部坐标变换及截断范围；叉形依赖结构/对称性。'),
('weak','Weakly Nonlinear Oscillators','wklynloscilator','慢幅相、平均方法与弱非线性；谐波平衡分支仅为候选近似，不代替稳定性分析。'),
('hopf-proof','Hopf Bifurcations','hopfbif','Hopf条件与局部振荡；纯虚特征值不是单独充分条件。')]:
    ROWS.append(dict(id='nd-'+id,title=title,authors='Rodolfo R. Rosales',year='2004课程；文件内日期另保留',publication='MIT 18.385J，作者官方课程讲义',resource='https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/resources/'+resource+'/',supports=support,kind='author_lecture',access='fulltext'))
ROWS.extend([
dict(id='nd-cochlea',title='Auditory sensitivity provided by self-tuned critical oscillations of hair cells',authors='Sébastien Camalet; Thomas Duke; Frank Jülicher; Jacques Prost',year='2000',publication='PNAS 97(7):3183–3188；作者开放稿',doi='10.1073/pnas.97.7.3183',url='https://arxiv.org/pdf/physics/0003100',supports='原始临界振荡听觉建模；本文仅用归一化共振Hopf正规形推导立方根响应，不验证真实耳蜗参数、自调谐或临床获益。',kind='original_paper',access='fulltext'),
dict(id='nd-surrogates',title='Surrogate time series',authors='Thomas Schreiber; Andreas Schmitz',year='2000',publication='Physica D 142:346–382；作者开放稿',doi='10.1016/S0167-2789(00)00043-9',url='https://arxiv.org/pdf/chao-dyn/9909037',supports='原作者替代数据方法与零假设、非平稳性及误判；拒绝指定随机零假设不等于证明确定性混沌。',kind='author_review',access='fulltext'),
dict(id='nd-ivp',title='scipy.integrate.solve_ivp',authors='SciPy developers',year='stable快照；2026-11-02核对，本地1.17.1',publication='SciPy 官方接口文档',url='https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html',supports='rtol/atol、内部步长、输出采样及事件语义；局部误差容差不是严格真实全局误差界。',kind='official_documentation',access='documentation')])
def fetch(row):
    try:
        r=dict(row)
        if 'resource' in r:
            soup=BeautifulSoup(get(r['resource']),'html.parser');links=[a['href'] for a in soup.select('a[href]') if a['href'].split('?')[0].endswith('.pdf')];assert links,r['resource'];r['url']='https://ocw.mit.edu'+links[0] if links[0].startswith('/') else links[0]
        pdf=r['kind']!='official_documentation';path=OUT/(r['id']+('.pdf' if pdf else '.html'))
        # Reuse identical author files already checked in the companion task.
        old=ROOT/'artifacts/differential-equations-and-dynamical-systems/sources'/('dds-'+r['id'][3:]+'.pdf')
        if not path.exists() and old.exists():path.write_bytes(old.read_bytes())
        data=path.read_bytes() if path.exists() else get(r['url']);assert data[:4]==b'%PDF' if pdf else len(data)>1000;path.write_bytes(data)
        if pdf:
            reader=PdfReader(io.BytesIO(data));pages=len(reader.pages);text='\n'.join(p.extract_text() or '' for p in reader.pages);method='pypdf text extraction'
            if len(text)<1000:
                target=OUT/(r['id']+'.txt');subprocess.run(['pdftotext','-layout',str(path),str(target)],check=True,capture_output=True);text=target.read_text(encoding='utf-8');method='Poppler text extraction'
        else:
            soup=BeautifulSoup(data,'html.parser');text=(soup.select_one('main') or soup).get_text(' ',strip=True);pages=None;method='HTML main text'
        assert len(text)>1000,(r['id'],len(text));(OUT/(r['id']+'.txt')).write_text(text,encoding='utf-8')
        return dict(**r,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(text),pdf_pages=pages,checked_at='2026-11-02',extraction_method=method)
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','doi','url','access','supports'];refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/nonlinear-dynamics-references.ts').write_text("import type { Reference } from './references';\nexport const nonlinearDynamicsReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
