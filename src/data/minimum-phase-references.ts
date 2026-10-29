import type { Reference } from './references';

export const minimumPhaseReferences: Record<string, Reference> = {
  'mp-smith-filters': {
    title: 'Introduction to Digital Filters with Audio Applications — Minimum-Phase Filters',
    authors: 'Julius O. Smith III', year: '2007', publication: 'W3K Publishing；作者在线教材 DSPRelated 镜像',
    url: 'https://dsprelated.com/freebooks/filters/Minimum_Phase_Filters.html', access: 'fulltext',
    supports: '阅读定义、零点条件、能量前置定理与最小相位/全通分解相关段落。本文算例和图为独立解析计算，不转载教材图片。',
  },
  'mp-smith-spectral': {
    title: 'Spectral Audio Signal Processing — Minimum-Phase Filter Design', authors: 'Julius O. Smith III',
    year: '2011', publication: 'W3K Publishing；作者在线教材 DSPRelated 镜像',
    url: 'https://www.dsprelated.com/freebooks/sasp/Minimum_Phase_Filter_Design.html', access: 'fulltext',
    supports: '阅读对数幅度、相位、Hilbert关系与因果复倒谱解释；与前项为同一作者教材，不能当作独立实验重复证据。',
  },
  'mp-rceps': {
    title: 'rceps — Real cepstrum and minimum-phase reconstruction', authors: 'The MathWorks, Inc.',
    year: '访问于2026-10-29', publication: 'Signal Processing Toolbox 官方文档，R2026b',
    url: 'https://www.mathworks.com/help/signal/ref/rceps.html', access: 'documentation',
    supports: '核对实倒谱定义、倒谱窗与最小相位重建算法；有限DFT输出的边界由本文进一步说明。',
  },
  'mp-scipy': {
    title: 'scipy.signal.minimum_phase', authors: 'SciPy community', year: '访问于2026-10-29',
    publication: 'SciPy 官方在线 API 文档（访问页面标示 v1.18.0）',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.minimum_phase.html', access: 'documentation',
    supports: '核对线性相位FIR输入、homomorphic/hilbert方法、FFT长度及half=True/False对长度和目标幅度的不同含义。本地执行版本另存。',
  },
  'mp-kulkarni-1999': {
    title: 'Sensitivity of human subjects to head-related transfer-function phase spectra',
    authors: 'Abhijit Kulkarni; S. K. Isabelle; H. Steven Colburn', year: '1999',
    publication: 'The Journal of the Acoustical Society of America, 105(5), 2821–2840',
    doi: '10.1121/1.426898', url: 'https://pubmed.ncbi.nlm.nih.gov/10335633/', access: 'abstract',
    supports: '读取并在推送前直接打开PubMed页面复核摘要：四间隔二选一辨别、修改HRTF相位、低频ITD条件及仅限消声短响应的结论。访问范围为摘要，未声称取得全文。',
  },
  'mp-kulkarni-2004': {
    title: 'Infinite-impulse-response models of the head-related transfer function',
    authors: 'Abhijit Kulkarni; H. Steven Colburn', year: '2004',
    publication: 'The Journal of the Acoustical Society of America, 115(4), 1714–1728',
    doi: '10.1121/1.1650332', url: 'https://pubmed.ncbi.nlm.nih.gov/15101650/', access: 'abstract',
    supports: '读取摘要与书目：HRTF有理传递函数加延迟建模及全极点/极零模型比较；不复述未核实的阶数、误差或听测数值。',
  },
  'mp-inverse': {
    title: 'inv — Invert dynamic system models', authors: 'The MathWorks, Inc.', year: '访问于2026-10-29',
    publication: 'Control System Toolbox 官方文档，R2026b',
    url: 'https://www.mathworks.com/help/control/ref/inputoutputmodel.inv.html', access: 'documentation',
    supports: '核对逆系统及直通矩阵可逆条件。连续时间严格真有理系统的逆不一定可实现，正文用一阶低通独立推导说明。',
  },
};
