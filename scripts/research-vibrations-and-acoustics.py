"""Cache author teaching sources and official documentation with explicit scope."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import subprocess,json,hashlib,io
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/vibrations-and-acoustics/sources';REC=ROOT/'docs/research/vibrations-and-acoustics-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
def get(url):
    errors=[]
    for proxy in [[],['--proxy','http://127.0.0.1:7897']]:
        r=subprocess.run(['curl.exe','-fLsS','--connect-timeout','8','--max-time','30',*proxy,url],capture_output=True,timeout=35)
        if r.returncode==0:return r.stdout
        errors.append(r.stderr.decode(errors='replace'))
    raise RuntimeError(str(errors))
ROWS=[]
def add(id,title,authors,url,supports,kind='author_teaching',pdf=False,year='在线版；2026-11-02核对',publication='作者或机构官方教学资料',resource=False):
    row=dict(id='va-'+id,title=title,authors=authors,year=year,publication=publication,supports=supports,kind=kind,access='documentation' if kind=='official_documentation' else 'fulltext',pdf=pdf)
    row['resource' if resource else 'url']=url;ROWS.append(row)
add('free','Constant-coefficient second-order linear ODEs','Jiří Lebl','https://www.jirka.org/diffyqs/html/sec_ccsol.html','质量弹簧阻尼方程、特征根与欠/临界/过阻尼；本文参数、初值和能量另行复算。')
add('forced','Forced oscillations and resonance','Jiří Lebl','https://www.jirka.org/diffyqs/html/forcedo_section.html','强迫响应及位移峰条件；本文明确速度峰、功率和半功率带宽的不同定义。')
add('modal','Recitation 12 Notes: Modal Analysis','MIT 2.003SC Engineering Dynamics','https://ocw.mit.edu/courses/2-003sc-engineering-dynamics-fall-2011/650ea2d4579aa784f6e46044188560b0_MIT2_003SCF11_rec12note1.pdf','质量与刚度、模态分解与正交；本文两质量矩阵、比例阻尼和直接/模态响应另核对。',pdf=True,year='2011',publication='MIT OpenCourseWare 官方课程讲义')
for id,title,resource,support in [
('measurement','Lecture 1: Sound measurement, rms and peak, lumped elements and waves','lec_1_2004','声压RMS、相位、频谱与集总/分布描述；不从数字采样值自动推声压校准。'),
('lumped','Lecture 7: Circuit descriptions of acoustic elements','lec_7_2004','声学顺性、惯抗、体积速度与电路类比；面积换算及阻抗单位单独核对。'),
('tubes','Lectures 15–16: Tubes, natural frequencies and dimensional equations','lec_15_16','管道模态、端点、输入阻抗与近似；理想开口与真实辐射、损耗分开。')]:
    add(id,title,'MIT 6.551J / HST.714J 课程（讲义未单独署名）','https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/resources/'+resource+'/',support,pdf=True,year='2004',publication='MIT OpenCourseWare 官方课程讲义',resource=True)
add('plane','Lecture 2: One-dimensional traveling waves','MIT 6.551J / HST.714J 课程（讲义未单独署名）','https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/1149b68a00a45f7c67d4a5c24ed08b51_lec_2_2004.pdf','线性声学方程、双向行波、压力/速度与反射；本文固定e^(iωt)和峰值相量。',pdf=True,year='2004',publication='MIT OpenCourseWare 官方课程讲义')
add('spherical','Lecture 3: Spherical waves, near and far field, radiation impedance','MIT 6.551J / HST.714J 课程（讲义未单独署名）','https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/7056ab51d5cb75810bf976ee38ac8f30_lec_3_2004.pdf','球面外向波、反应性与kr；特别保留纯外向球面波净强度仍等于p_rms²/(rho c)这一限定结论。',pdf=True,year='2004',publication='MIT OpenCourseWare 官方课程讲义')
for id,title,url,support in [
('wave-equation','The wave equation for sound','https://www.animations.physics.unsw.edu.au/jw/sound-wave-equation.htm','压强、密度与质点运动，线性化、声速和波方程；不将声速当质点速度。'),
('intensity','Acoustic impedance, intensity and power','https://www.animations.physics.unsw.edu.au/jw/sound-impedance-intensity.htm','声强、复相量与比声阻抗/声阻抗；采用rho=1.2、c=343得411.6，不沿用页中420近似数值。'),
('compliance','Acoustic compliance, inertance and impedance','https://www.animations.physics.unsw.edu.au/jw/compliance-inertance-impedance.htm','声学集总元件与体积流，几何尺度及低频近似。'),
('decibels','dB: What is a decibel?','https://phys.unsw.edu.au/jw/dB.html','功率10log、幅度20log和参考值；本文另明确相关声压叠加和SPL/强度级并非恒等。'),
('pipes','Open vs closed pipes','https://phys.unsw.edu.au/jw/flutes.v.clarinets.html','压力与位移边界、开开和闭开管谐振；理想边界与端修正分开。'),
('helmholtz','Helmholtz resonance','https://phys.unsw.edu.au/jw/Helmholtz.html','气颈惯性与腔体顺性、波长远大于尺度与有效颈长；不从无损模型推吸声。')]:
    add(id,title,'Joe Wolfe / UNSW School of Physics',url,support,publication='UNSW Physclips / Music Acoustics 官方教学资料')
add('ir','Impulse Responses','Room EQ Wizard','https://www.roomeqwizard.com/help/help_en-GB/html/impulseresponse.html','脉冲响应、直达/反射和时窗；本文两抽头例为指定数字模型，未运行REW或测量房间。',kind='official_documentation',publication='REW 官方帮助')
add('eigh','scipy.linalg.eigh','SciPy developers','https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html','实对称广义特征值问题、正定质量矩阵和质量归一化；运行环境SciPy1.17.1。',kind='official_documentation',publication='SciPy 官方接口文档')
add('ivp','scipy.integrate.solve_ivp','SciPy developers','https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html','积分容差、t_eval和内部步长；本篇积分交叉检查不当严格全局误差保证。',kind='official_documentation',publication='SciPy 官方接口文档')
add('diffraction','Diffraction, shadows, beams, Huygens construction','Joe Wolfe / UNSW School of Physics','https://www.animations.physics.unsw.edu.au/jw/light/diffraction-shadows-beams-huygens.html','开口与波长尺度的定性绕射；未用光学演示拟合听觉头影、屏障衰减或方向图。',publication='UNSW Physclips 官方教学资料')
def fetch(row):
    try:
        r=dict(row)
        if 'resource' in r:
            soup=BeautifulSoup(get(r['resource']),'html.parser');links=[a['href'] for a in soup.select('a[href]') if a['href'].split('?')[0].endswith('.pdf')];assert links;r['url']='https://ocw.mit.edu'+links[0] if links[0].startswith('/') else links[0]
        path=OUT/(r['id']+('.pdf' if r['pdf'] else '.html'));data=path.read_bytes() if path.exists() else get(r['url']);assert data[:4]==b'%PDF' if r['pdf'] else len(data)>1000;path.write_bytes(data)
        if r['pdf']:
            reader=PdfReader(io.BytesIO(data));pages=len(reader.pages);text='\n'.join(p.extract_text() or '' for p in reader.pages);method='pypdf text extraction'
            if len(text)<1000:
                target=OUT/(r['id']+'.txt');subprocess.run(['pdftotext','-layout',str(path),str(target)],check=True,capture_output=True);text=target.read_text(encoding='utf-8');method='Poppler text extraction'
        else:
            soup=BeautifulSoup(data,'html.parser');main=soup.select_one('main') or soup
            for e in main.select('script,style,nav'):e.decompose()
            text=main.get_text(' ',strip=True);pages=None;method='HTML article text'
        if r['id']=='va-tubes':method+='; handwritten material visually inspected on PDF pages 1–6, text not treated as reliable transcription'
        assert len(text)>1000,(r['id'],len(text));(OUT/(r['id']+'.txt')).write_text(text,encoding='utf-8')
        return dict(**r,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(text),pdf_pages=pages,checked_at='2026-11-02',extraction_method=method)
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','url','access','supports'];refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/vibrations-and-acoustics-references.ts').write_text("import type { Reference } from './references';\nexport const vibrationsAcousticsReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
