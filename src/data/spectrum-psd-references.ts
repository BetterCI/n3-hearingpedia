import type { Reference } from './references';

export const spectrumPsdReferences: Record<string, Reference> = {
  'spectrum-nist-levels': {
    title: 'NIST Guide to the SI — Chapter 8, §8.7 Logarithmic quantities and units', authors: 'National Institute of Standards and Technology',
    year: '官方网页（页面更新 2025-08-18；2026-10-10 核验）', publication: 'NIST Special Publication 811 在线指南',
    url: 'https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8', access: 'documentation',
    supports: '阅读 §8.7 的场量 / 功率量对数级、20 log 与 10 log 以及声压参考 20 μPa 示例；支持显式报告参考量。未把一般 SI 指南当作声级计性能或噪声暴露评价标准。',
  },
  'spectrum-scipy-welch': {
    title: 'SciPy Reference — scipy.signal.welch', authors: 'SciPy Community',
    year: '官方文档（2026-10-10 核验）', publication: 'SciPy 官方文档',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html', access: 'documentation',
    supports: '阅读参数、Notes 与例子：分段平均、单侧折叠、density / spectrum 单位、两标度的 ENBW 比值和 Hann 重叠建议；演示采用显式参数，不依赖在线文档版本的默认窗。实际数值使用本地 SciPy 1.17.1，未将零填充当作提高真实频率分辨能力。',
  },
  'spectrum-mit-psd': {
    title: 'Signals, Systems and Inference — Chapter 10: Power Spectral Density',
    authors: 'Alan V. Oppenheim; George C. Verghese', year: '2010', publication: 'MIT OpenCourseWare, 6.011',
    url: 'https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/8075041184d566103ce7c3f69afc5e75_MIT6_011S10_chap10.pdf',
    access: 'fulltext', supports: '阅读 PDF 第 1–4 页及相关滤波说明：WSS、自相关与 PSD、频带积分、有限记录期望和遍历性。本文使用 Hz 约定，未直接混用讲义的角频率归一化；未转载图。',
  },
  'spectrum-numpy-fft': {
    title: 'NumPy Reference — Discrete Fourier Transform', authors: 'NumPy Developers',
    year: '官方文档（2026-10-10 核验）', publication: 'NumPy 官方文档',
    url: 'https://numpy.org/doc/stable/reference/routines.fft.html', access: 'documentation',
    supports: '阅读 Implementation details、Normalization、Real and Hermitian transforms：默认正变换不缩放、逆变换缩放及实信号对称。本文另明确幅度与功率标度，不把 abs(FFT) 或 abs(FFT)^2 自动认定为校准谱。',
  },
  'spectrum-harris-1978': {
    title: 'On the use of windows for harmonic analysis with the discrete Fourier transform',
    authors: 'Fredric J. Harris', year: '1978', publication: 'Proceedings of the IEEE, 66(1), 51–83',
    doi: '10.1109/PROC.1978.10837', url: 'https://web.mit.edu/xiphmont/Public/windows.pdf', access: 'fulltext',
    supports: '阅读原论文 PDF 第 1–4、6–7 页相关有限记录、泄漏、等效噪声带宽、相干增益及重叠相关段落；扫描 OCR 有误，公式与官方实现文档交叉核对，数值由本文独立计算。',
  },
  'spectrum-heinzel-2002': {
    title: 'Spectrum and spectral density estimation by the Discrete Fourier transform (DFT), including a comprehensive list of window functions and some new flat-top windows',
    authors: 'G. Heinzel; A. Rüdiger; R. Schilling', year: '2002', publication: 'Max Planck Institute for Gravitational Physics, technical report, 15 February 2002',
    url: 'https://pure.mpg.de/pubman/item/item_152164_1/component/file_152163/395068.pdf', access: 'abstract',
    supports: '核对机构记录和 PDF 首页可检索原始摘要：报告强调 spectrum 与 density 通过 ENBW 关联。直接下载 403，未声称阅读完整报告、窗口目录或复现其平顶窗。',
  },
  'spectrum-welch-1967': {
    title: 'The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms',
    authors: 'Peter D. Welch', year: '1967', publication: 'IEEE Transactions on Audio and Electroacoustics, 15(2), 70–73',
    doi: '10.1109/TAU.1967.1161901',
    url: 'https://research.ibm.com/publications/the-use-of-fast-fourier-transform-for-the-estimation-of-power-spectra-a-method-based-on-time-averaging-over-short-modified-periodograms',
    access: 'abstract', supports: '阅读作者所属 IBM Research 的原始摘要与书目：分段、修正周期图与平均的历史方法。具体实现和参数另由 SciPy / MATLAB 官方文档核对，未声称读到原论文全部推导。',
  },
  'spectrum-pwelch': {
    title: 'MATLAB Signal Processing Toolbox — pwelch', authors: 'MathWorks',
    year: '官方文档（2026-10-10 核验）', publication: 'MathWorks 官方文档',
    url: 'https://www.mathworks.com/help/signal/ref/pwelch.html', access: 'documentation',
    supports: '阅读输入参数、输出单位、频率约定、分段截取、默认 Hamming 及置信区间说明；用于跨软件比较和不确定性边界，没有实际运行 MATLAB，没有使用产品版本新特性作为研究证据。',
  },
  'spectrum-dpss': {
    title: 'SciPy Reference — scipy.signal.windows.dpss', authors: 'SciPy Community',
    year: '官方文档（2026-10-10 核验）', publication: 'SciPy 官方文档',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.dpss.html', access: 'documentation',
    supports: '阅读 DPSS、时间半带宽积、窗口数、sym 与归一化、插值可能破坏正交性说明；正文为方法解释，未计算多窗谱图或复现 DPSS 数据。',
  },
  'spectrum-pmtm': {
    title: 'MATLAB Signal Processing Toolbox — pmtm', authors: 'MathWorks',
    year: '官方文档（2026-10-10 核验）', publication: 'MathWorks 官方文档',
    url: 'https://www.mathworks.com/help/signal/ref/pmtm.html', access: 'documentation',
    supports: '阅读 More About 的 Thomson 多窗法、Slepian 序列与加权说明，核对同记录多窗和 Welch 不同、NW 与窗口数及单侧规则；没有运行 MATLAB 或把所有窗口估计声称为独立。',
  },
  'spectrum-debias-2024': {
    title: 'Debiasing Welch’s method for spectral density estimation',
    authors: 'Lachlan C. Astfalck; Adam M. Sykulski; Edward J. Cripps', year: '2024',
    publication: 'Biometrika, 111(4), 1313–1329', doi: '10.1093/biomet/asae033',
    url: 'https://academic.oup.com/biomet/article/111/4/1313/7703280', access: 'fulltext',
    supports: '取得 Imperial 机构仓储的出版 PDF，阅读第 1–4 页摘要、引言和定义及相关方法说明；短段变异与有限样本偏差取舍、偏差校正方向。没有复现论文模拟或声学/海浪数据，没有声称该方法对所有声音均更优。',
  },
  'spectrum-bias-2025': {
    title: 'Bias correction of quadratic spectral estimators',
    authors: 'Lachlan C. Astfalck; Adam M. Sykulski; Edward J. Cripps', year: '2025',
    publication: 'Biometrika, 112(3), asaf033', doi: '10.1093/biomet/asaf033',
    url: 'https://spiral.imperial.ac.uk/entities/publication/bd6e074d-b90a-4eda-b794-dad9af6f2317', access: 'abstract',
    supports: '阅读 Imperial 机构仓储原始摘要并核对已发表期刊、DOI、日期；研究把偏差校正扩展到更一般二次谱估计。没有阅读全文、复现算法或将同作者两篇论文当独立重复实验。',
  },
  'spectrum-ni-output': {
    title: 'Expected Output of the FFT Power Spectrum and PSD VI in LabVIEW?', authors: 'National Instruments',
    year: '2024（页面更新 2024-01-02；2026-10-10 核验）', publication: 'NI 官方支持文档',
    url: 'https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000kGPYSA2&l=en-US', access: 'documentation',
    supports: '阅读可检索的官方完整 Solution：输入量平方与每 Hz 单位。直接打开失败，未声称运行 LabVIEW；分贝参考和归一化由本文显式定义，不沿用界面缩写推定校准。',
  },
};
