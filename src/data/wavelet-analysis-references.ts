import type { Reference } from './references';
export const waveletAnalysisReferences: Record<string, Reference> = {
  "wa-mallat": {
    "title": "A Theory for Multiresolution Signal Decomposition: The Wavelet Representation",
    "authors": "Stéphane G. Mallat",
    "year": "1989",
    "publication": "IEEE TPAMI 11(7):674–693",
    "doi": "10.1109/34.192463",
    "url": "https://www.di.ens.fr/~mallat/papiers/MallatTheory89.pdf",
    "access": "fulltext",
    "supports": "多分辨分析、正交分解、尺度空间与滤波器组；本文明确理论分辨率索引与软件分解层号方向。"
  },
  "wa-daubechies": {
    "title": "Orthonormal Bases of Compactly Supported Wavelets",
    "authors": "Ingrid Daubechies",
    "year": "1988",
    "publication": "CPAM 41:909–996",
    "doi": "10.1002/cpa.3160410705",
    "url": "https://math.duke.edu/~ingrid/publications/cpam41-1988.pdf",
    "access": "fulltext",
    "supports": "紧支撑正交小波、消失矩与滤波器构造；不将零均值单独当作可容许性的充分条件。"
  },
  "wa-torrence": {
    "title": "A Practical Guide to Wavelet Analysis",
    "authors": "Christopher Torrence; Gilbert P. Compo",
    "year": "1998",
    "publication": "BAMS 79(1):61–78",
    "doi": "10.1175/1520-0477(1998)079<0061:APGTWA>2.0.CO;2",
    "url": "https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf",
    "access": "fulltext",
    "supports": "CWT、Morlet尺度与傅里叶周期、影响锥和噪声背景；正文另说明精确零均值修正、L2单位和选定边界约定。"
  },
  "wa-coherence": {
    "title": "Application of the cross wavelet transform and wavelet coherence to geophysical time series",
    "authors": "Aslak Grinsted; John C. Moore; Svetlana Jevrejeva",
    "year": "2004",
    "publication": "Nonlinear Processes in Geophysics 11:561–566",
    "doi": "10.5194/npg-11-561-2004",
    "url": "https://npg.copernicus.org/articles/11/561/2004/npg-11-561-2004.pdf",
    "access": "fulltext",
    "supports": "交叉小波、时间尺度平滑、相干与相位；未将地球物理实例转述为听觉或因果证据。"
  },
  "wa-pitfalls": {
    "title": "Cross wavelet analysis: significance testing and pitfalls",
    "authors": "Douglas Maraun; Jürgen Kurths",
    "year": "2004",
    "publication": "Nonlinear Processes in Geophysics 11:505–514",
    "doi": "10.5194/npg-11-505-2004",
    "url": "https://npg.copernicus.org/articles/11/505/2004/npg-11-505-2004.pdf",
    "access": "fulltext",
    "supports": "背景过程、交叉谱解释与显著性陷阱；独立检验算例不等于相关时频像素的有效检验数。"
  },
  "wa-scattering": {
    "title": "Group Invariant Scattering",
    "authors": "Stéphane Mallat",
    "year": "2012",
    "publication": "CPAM 65:1331–1398",
    "doi": "10.1002/cpa.21413",
    "url": "https://www.di.ens.fr/~mallat/College/CPAM-Mallat-Scat.pdf",
    "access": "fulltext",
    "supports": "固定小波、模和平均构造散射表示；只定位与学习滤波器的区别，不声称所有深层模型等价。"
  },
  "wa-donoho": {
    "title": "De-Noising by Soft-Thresholding",
    "authors": "David L. Donoho",
    "year": "1992",
    "publication": "Stanford Statistics, Technical Report EFS NSF 409；后发表于IEEE TIT 41(3), 1995",
    "url": "https://stacks.stanford.edu/file/jz383pc7441/jz383pc7441_EFS-NSF-409.pdf",
    "access": "fulltext",
    "supports": "原始作者技术报告中的软阈值、正交高斯噪声与通用阈值；引用1992报告版本，不冒充读取1995期刊排版。"
  },
  "wa-wavelets": {
    "title": "Wavelets",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/wavelets.html",
    "access": "documentation",
    "supports": "小波族、正交和双正交属性、滤波器与db4命名。"
  },
  "wa-cwt": {
    "title": "Continuous Wavelet Transform (CWT)",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/cwt.html",
    "access": "documentation",
    "supports": "尺度频率换算、采样周期仅改变频率、低尺度混叠；本地1.8.0不使用较新文档precision参数。"
  },
  "wa-dwt": {
    "title": "Discrete Wavelet Transform (DWT)",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/dwt-discrete-wavelet-transform.html",
    "access": "documentation",
    "supports": "分析系数、层号、长度和最大有用层数。"
  },
  "wa-idwt": {
    "title": "Inverse Discrete Wavelet Transform (IDWT)",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/idwt-inverse-discrete-wavelet-transform.html",
    "access": "documentation",
    "supports": "合成、系数顺序与相同边界模式。"
  },
  "wa-boundary": {
    "title": "Signal extension modes",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/signal-extension-modes.html",
    "access": "documentation",
    "supports": "zero、symmetric、periodic与periodization不是同一延拓；边界和系数计数。"
  },
  "wa-swt": {
    "title": "Stationary Wavelet Transform",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/swt-stationary-wavelet-transform.html",
    "access": "documentation",
    "supports": "不降采样、冗余、长度整除与能量分配的三个附加条件。"
  },
  "wa-iswt": {
    "title": "Inverse Stationary Wavelet Transform",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/iswt-inverse-stationary-wavelet-transform.html",
    "access": "documentation",
    "supports": "SWT合成与归一化一致性。"
  },
  "wa-packets": {
    "title": "Wavelet Packets",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/wavelet-packets.html",
    "access": "documentation",
    "supports": "两支递归、节点、自然顺序与频率顺序；名义带宽不意味着理想砖墙。"
  },
  "wa-threshold": {
    "title": "Thresholding functions",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/thresholding-functions.html",
    "access": "documentation",
    "supports": "软硬阈值与收缩定义；本文通用阈值只在独立同方差高斯正交模型下解释。"
  },
  "wa-coefficients": {
    "title": "Handling DWT Coefficients",
    "authors": "PyWavelets developers",
    "year": "stable文档快照；2026-11-02核对",
    "publication": "PyWavelets 官方文档",
    "url": "https://pywavelets.readthedocs.io/en/stable/ref/dwt-coefficient-handling.html",
    "access": "documentation",
    "supports": "多层系数打包、形状与重建；本文另验证有限正交矩阵。"
  }
};
