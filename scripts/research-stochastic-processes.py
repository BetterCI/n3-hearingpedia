"""Scoped author textbooks, lecture PDFs and official DSP documentation."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import runpy,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/stochastic-processes/sources';REC=ROOT/'docs/research/stochastic-processes-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
base=runpy.run_path(str(ROOT/'scripts/research-vibrations-and-acoustics.py'));get=base['get'];fetch=base['fetch'];fetch.__globals__['OUT']=OUT
ROWS=[]
def add(id,title,authors,url,supports,year,publication,kind='author_textbook',pdf=False,resource=False):
    r=dict(id='sp-'+id,title=title,authors=authors,year=year,publication=publication,supports=supports,kind=kind,access='documentation' if kind=='official_documentation' else 'fulltext',pdf=pdf)
    r['resource' if resource else 'url']=url;ROWS.append(r)
for id,title,chapter,support in [
('processes','Random Processes','09','实现与总体、联合分布、高斯、WSS和遍历；本文白而依赖、宽而非严平稳反例另行构造。'),
('psd','Power Spectral Density','10','Wiener–Khinchin、谱表示、白噪声、LTI与谱因子；本文固定实过程和每Hz双侧谱约定，保留谱线与广义白噪声边界。'),
('wiener','Wiener Filtering','11','正交性、因果和非因果最优线性估计；三抽头正规方程与全时域理想谱解按信息范围分别比较。'),
('mmse','Estimation with Minimum Mean Square Error','08','条件期望MMSE和线性投影LMMSE的区别；不把一般非高斯问题的线性最优当全局MMSE。')]:
    add(id,title,'Alan V. Oppenheim; George C. Verghese','https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/resources/mit6_011s10_chap'+chapter+'/',support,'2010','MIT 6.011, Signals, Systems and Inference，作者课程书',pdf=True,resource=True)
for id,title,number,support in [
('wss','Wide-Sense Stationary Processes and LTI Filtering','16','WSS与相关、稳定LTI映射；本文输出谱与互谱采用明确相关方向。'),
('filtering','LTI Filtering of WSS Processes','17','随机输入滤波、方差与相关；零初始状态瞬态不冒充全历史稳态。'),
('spectral','Power Spectral Density','18','PSD、均方值与频率归一化；数字弧度谱与每Hz密度不混用。'),
('wkt','Einstein–Wiener–Khinchin Theorem, PSD Applications, Modeling Filters','19','相关与谱、谱线和整形滤波；普通密度存在的条件与一般谱测度分开。')]:
    add(id,title,'MIT 6.011 课程：George C. Verghese; Alan V. Oppenheim; Peter Hagelstein','https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/resources/mit6_011s18lec'+number+'/',support,'2018','MIT OpenCourseWare 官方课程讲义','author_lecture',pdf=True,resource=True)
for id,title,chapter,support in [('poisson','Poisson Processes','02','齐次Poisson计数、独立平稳增量和指数间隔；计数本身不平稳，不当神经不应期模型。'),('markov','Finite-state Markov Chains','03','条件Markov性、转移矩阵、平稳初分布与有限不可约非周期链收敛；不将时齐性当平稳。')]:
    add(id,title,'Robert G. Gallager','https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/resources/mit6_262s11_chap'+chapter+'/',support,'2011','MIT 6.262 Discrete Stochastic Processes，作者课程书',pdf=True,resource=True)
for id,title,url,support in [
('basic','Basic Concepts of Random Processes','https://www.probabilitycourse.com/chapter10/10_1_0_basic_concepts.php','时间与取值空间分别分类；过程与一条实现不等同。'),
('stationary','Stationary Processes','https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php','有限维分布的时移不变；WSS与严格平稳的条件和区别。'),
('brownian','Brownian Motion: definition and properties','https://www.probabilitycourse.com/chapter11/11_4_0_brownian_motion_wiener_process.php','Brownian连续路径、独立平稳高斯增量、非平稳状态及min(s,t)协方差；未进行随机微积分教学或实测扩散拟合。')]:
    add(id,title,'Hossein Pishro-Nik',url,support,'2014；在线版2026-11-02核对','Introduction to Probability, Statistics, and Random Processes，作者官方网站')
for id,name,support in [('welch','welch','分段窗、重叠、density和detrend；未把重叠段数当独立自由度。'),('periodogram','periodogram','密度标度、每Hz单位、窗平方和与单侧折叠；短例显式关闭去均值。'),('csd','csd','官方Pxy使用conj(X)Y，核对本文S_yx的方向约定。'),('coherence','coherence','需要平滑/分段的平方相干；单个未平滑谱点的比值可恒为1，不能作因果证据。'),('lfilter','lfilter','因果差分滤波及零初态与zi；本文AR独立指定平稳初值，有限FIR去掉历史不完整的起始位置。')]:
    add(id,'scipy.signal.'+name,'SciPy developers','https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.'+name+'.html',support,'stable快照2026-11-02；本地1.17.1','SciPy 官方文档','official_documentation')
if __name__=='__main__':
    # Follow the author's visible next links; repair a root-relative chapter path in its HTML.
    row=next(r for r in ROWS if r['id']=='sp-brownian');chain=[]
    for _ in range(4):
        soup=BeautifulSoup(get(row['url']),'html.parser');heading=soup.find(['h2','h1']);title=heading.get_text(' ',strip=True) if heading else ''
        chain.append(dict(url=row['url'],heading=title))
        if 'Definition' in title or 'Properties' in title:break
        nxt=next(a for a in soup.select('a[href]') if a.get_text(' ',strip=True).lower()=='next');href=nxt['href']
        row['url']=urljoin('https://www.probabilitycourse.com/' if href.startswith('chapter11/') else row['url'],href)
    row['discovery_chain']=chain
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','url','access','supports'];refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/stochastic-processes-references.ts').write_text("import type { Reference } from './references';\nexport const stochasticProcessesReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
