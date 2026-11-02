"""Cache primary papers and official documentation, preserving scope and file identity."""
from pathlib import Path
import runpy,json
ROOT=Path(__file__).resolve().parents[1]
base=runpy.run_path(str(ROOT/'scripts/research-deep-learning.py'))
OUT=ROOT/'artifacts/wavelet-analysis/sources';REC=ROOT/'docs/research/wavelet-analysis-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
ROWS=[]
def add(id,title,authors,url,supports,year,publication,kind='original_paper',doi=None):
    r=dict(id='wa-'+id,title=title,authors=authors,url=url,supports=supports,year=year,publication=publication,kind=kind,access='fulltext')
    if doi:r['doi']=doi
    ROWS.append(r)
add('mallat','A Theory for Multiresolution Signal Decomposition: The Wavelet Representation','Stéphane G. Mallat','https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf','多分辨分析、正交分解、尺度空间与滤波器组；本文明确理论分辨率索引与软件分解层号方向。','1989','IEEE TPAMI 11(7):674–693',doi='10.1109/34.192463')
add('daubechies','Orthonormal Bases of Compactly Supported Wavelets','Ingrid Daubechies','https://math.duke.edu/~ingrid/publications/cpam41-1988.pdf','紧支撑正交小波、消失矩与滤波器构造；不将零均值单独当作可容许性的充分条件。','1988','CPAM 41:909–996',doi='10.1002/cpa.3160410705')
add('torrence','A Practical Guide to Wavelet Analysis','Christopher Torrence; Gilbert P. Compo','https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf','CWT、Morlet尺度与傅里叶周期、影响锥和噪声背景；正文另说明精确零均值修正、L2单位和选定边界约定。','1998','BAMS 79(1):61–78',doi='10.1175/1520-0477(1998)079<0061:APGTWA>2.0.CO;2')
add('coherence','Application of the cross wavelet transform and wavelet coherence to geophysical time series','Aslak Grinsted; John C. Moore; Svetlana Jevrejeva','https://npg.copernicus.org/articles/11/561/2004/npg-11-561-2004.pdf','交叉小波、时间尺度平滑、相干与相位；未将地球物理实例转述为听觉或因果证据。','2004','Nonlinear Processes in Geophysics 11:561–566',doi='10.5194/npg-11-561-2004')
add('pitfalls','Cross wavelet analysis: significance testing and pitfalls','Douglas Maraun; Jürgen Kurths','https://npg.copernicus.org/articles/11/505/2004/npg-11-505-2004.pdf','背景过程、交叉谱解释与显著性陷阱；独立检验算例不等于相关时频像素的有效检验数。','2004','Nonlinear Processes in Geophysics 11:505–514',doi='10.5194/npg-11-505-2004')
add('scattering','Group Invariant Scattering','Stéphane Mallat','https://www.di.ens.fr/~mallat/College/CPAM-Mallat-Scat.pdf','固定小波、模和平均构造散射表示；只定位与学习滤波器的区别，不声称所有深层模型等价。','2012','CPAM 65:1331–1398',doi='10.1002/cpa.21413')
add('donoho','De-Noising by Soft-Thresholding','David L. Donoho','https://stacks.stanford.edu/file/jz383pc7441/jz383pc7441_EFS-NSF-409.pdf','原始作者技术报告中的软阈值、正交高斯噪声与通用阈值；引用1992报告版本，不冒充读取1995期刊排版。','1992','Stanford Statistics, Technical Report EFS NSF 409；后发表于IEEE TIT 41(3), 1995')
for id,title,path,support in [
('wavelets','Wavelets','wavelets','小波族、正交和双正交属性、滤波器与db4命名。'),
('cwt','Continuous Wavelet Transform (CWT)','cwt','尺度频率换算、采样周期仅改变频率、低尺度混叠；本地1.8.0不使用较新文档precision参数。'),
('dwt','Discrete Wavelet Transform (DWT)','dwt-discrete-wavelet-transform','分析系数、层号、长度和最大有用层数。'),
('idwt','Inverse Discrete Wavelet Transform (IDWT)','idwt-inverse-discrete-wavelet-transform','合成、系数顺序与相同边界模式。'),
('boundary','Signal extension modes','signal-extension-modes','zero、symmetric、periodic与periodization不是同一延拓；边界和系数计数。'),
('swt','Stationary Wavelet Transform','swt-stationary-wavelet-transform','不降采样、冗余、长度整除与能量分配的三个附加条件。'),
('iswt','Inverse Stationary Wavelet Transform','iswt-inverse-stationary-wavelet-transform','SWT合成与归一化一致性。'),
('packets','Wavelet Packets','wavelet-packets','两支递归、节点、自然顺序与频率顺序；名义带宽不意味着理想砖墙。'),
('threshold','Thresholding functions','thresholding-functions','软硬阈值与收缩定义；本文通用阈值只在独立同方差高斯正交模型下解释。'),
('coefficients','Handling DWT Coefficients','dwt-coefficient-handling','多层系数打包、形状与重建；本文另验证有限正交矩阵。')]:
    add(id,title,'PyWavelets developers','https://pywavelets.readthedocs.io/en/stable/ref/'+path+'.html',support,'stable文档快照；2026-11-02核对','PyWavelets 官方文档','official_documentation');ROWS[-1]['access']='documentation'
if __name__=='__main__':
    from concurrent.futures import ThreadPoolExecutor
    original_fetch=base['fetch'];original_fetch.__globals__.update(OUT=OUT)
    def fetch(row):
        r=original_fetch(row)
        if row['id']=='wa-donoho' and r['status']=='failed':
            import hashlib
            from pypdf import PdfReader
            data=(OUT/'wa-donoho.pdf').read_bytes();reader=PdfReader(OUT/'wa-donoho.pdf')
            assert len(reader.pages)==39
            r=dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=0,pdf_pages=39,checked_at='2026-11-02',extraction_method='Scanned report; scoped visual inspection of PDF pages 3–8; no OCR text claimed')
        return r
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','doi','url','access','supports'];refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/wavelet-analysis-references.ts').write_text("import type { Reference } from './references';\nexport const waveletAnalysisReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
