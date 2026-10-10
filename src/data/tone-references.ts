import type { Reference } from './references';

export const toneReferences: Record<string, Reference> = {
  'tones-sfu-simple': {
    title: 'Handbook for Acoustic Ecology — Simple Tone', authors: 'Simon Fraser University, Sonic Studio',
    year: '未标注页面出版年（2026-10-10 核验）', publication: 'SFU 声学生态学手册',
    url: 'https://www.sfu.ca/sonic-studio-webdav/cmns/Handbook5/handbook/Simple_Tone.html', access: 'fulltext',
    supports: '阅读定义与术语差异：本文明确采用单一正弦频率的声学定义，不将“听起来只有一个音高”作为纯音判据。',
  },
  'tones-sfu-complex': {
    title: 'Handbook for Acoustic Ecology — Complex Tone', authors: 'Simon Fraser University, Sonic Studio',
    year: '未标注页面出版年（2026-10-10 核验）', publication: 'SFU 声学生态学手册',
    url: 'https://www.sfu.ca/sonic-studio-webdav/cmns/Handbook5/handbook/Complex_Tone.html', access: 'fulltext',
    supports: '阅读多频率分量定义与用语不一致说明；不采用页面将复合音响度简单概括为各分量响度相加的句子。',
  },
  'tones-mit-series': {
    title: 'MAS.160 Signals, Systems and Information for Media Technology — Recitation 3', authors: 'MIT MAS.160 课程',
    year: '2007', publication: 'MIT OpenCourseWare',
    url: 'https://ocw.mit.edu/courses/mas-160-signals-systems-and-information-for-media-technology-fall-2007/6533cd190b17ad896f055390f5bf85d4_rec3.pdf', access: 'fulltext',
    supports: '阅读 PDF 第 11–15、32–36 页的傅里叶级数、正弦与叠加、削波例；不转载图，不执行讲义中的高增益播放代码。',
  },
  'tones-sfu-analysis': {
    title: 'Handbook for Acoustic Ecology — Fourier Analysis', authors: 'Simon Fraser University, Sonic Studio',
    year: '未标注页面出版年（2026-10-10 核验）', publication: 'SFU 声学生态学手册',
    url: 'https://www.sfu.ca/sonic-studio-webdav/cmns/Handbook5/handbook/Fourier_Analysis.html', access: 'fulltext',
    supports: '阅读周期信号的正弦分解、幅度相位及真实乐器的时变结构；不采用“耳朵执行傅里叶分析”作为字面神经机制，不转载原图。',
  },
  'tones-unsw-linear': {
    title: 'Physclips — Linear and non-linear superposition', authors: 'Joe Wolfe / UNSW School of Physics',
    year: '未标注出版年（2026-10-10 核验）', publication: 'UNSW Physclips',
    url: 'https://animations.physics.unsw.edu.au/jw/linear-non-linear-superposition.html', access: 'fulltext',
    supports: '阅读线性相加与非线性电路对照，核对线性叠加不新增频率、非线性可生成组合分量；未采用页面二极管近似公式或转载演示。',
  },
  'tones-openstax-beats': {
    title: 'University Physics Volume 1 — 17.6 Beats', authors: 'William Moebs; Samuel J. Ling; Jeff Sanny',
    year: '2016', publication: 'OpenStax / Rice University',
    url: 'https://openstax.org/books/university-physics-volume-1/pages/17-6-beats', access: 'fulltext',
    supports: '阅读两频率叠加与差频拍率；本文选相近频率教学例，独立区分有符号调制因子与非负幅度包络，不把任意大的频差都称为可听的慢拍。',
  },
  'tones-numpy-rfft': {
    title: 'NumPy Reference — numpy.fft.rfft', authors: 'NumPy Developers',
    year: '官方在线文档（2026-10-10 核验）', publication: 'NumPy 官方文档',
    url: 'https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html', access: 'documentation',
    supports: '阅读实输入的非负频率输出、长度、归一化及零填充参数；生成脚本使用本机 NumPy 1.26.4，未假称运行在线文档所示版本。',
  },
  'tones-scipy-spectral': {
    title: 'SciPy User Guide — Spectral Analysis', authors: 'SciPy Community',
    year: '官方在线文档（2026-10-10 核验）', publication: 'SciPy 官方信号处理指南',
    url: 'https://docs.scipy.org/doc/scipy/tutorial/signal.html#spectral-analysis', access: 'documentation',
    supports: '阅读 Spectral Analysis 的有限时长正弦、采样与窗、幅度和密度标度及相位相关段落；图和数值由本文独立计算，不照抄文档中有限区间均方值的简化为任意时长精确式。',
  },
  'tones-scipy-periodogram': {
    title: 'SciPy Reference — scipy.signal.periodogram', authors: 'SciPy Community',
    year: '官方在线文档（2026-10-10 核验）', publication: 'SciPy 官方文档',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html', access: 'documentation',
    supports: '阅读 spectrum 与 density、单双边谱和窗归一化的官方定义；未运行该函数复现文档示例，本文图由 NumPy 显式计算。',
  },
  'tones-audacity-tone': {
    title: 'Audacity Manual — Tone', authors: 'Audacity Team',
    year: '官方在线文档（2026-10-10 核验）', publication: 'Audacity 官方手册',
    url: 'https://manual.audacityteam.org/man/tone.html', access: 'documentation',
    supports: '阅读波形、频率、数字幅度与时长字段；未实际运行 Audacity，不把软件数字幅度字段当作校准声压级或主观响度。',
  },
  'tones-whiteford-2023': {
    title: 'Sensitivity to Frequency Modulation is Limited Centrally', authors: 'Kelly L. Whiteford; Andrew J. Oxenham',
    year: '2023', publication: 'Journal of Neuroscience, 43(20), 3687–3695', doi: '10.1523/JNEUROSCI.0995-22.2023',
    url: 'https://pubmed.ncbi.nlm.nih.gov/37028932/', access: 'abstract',
    supports: '阅读原始摘要与书目：低 F0、高频谐波的 FM 检测支持中枢限制解释；没有据摘要声称直接记录人类听神经或否定所有锁相机制。',
  },
  'tones-guest-2024': {
    title: 'Limitations in human auditory spectral analysis at high frequencies', authors: 'Daniel R. Guest; Neha Rajappa; Andrew J. Oxenham',
    year: '2024', publication: 'Journal of the Acoustical Society of America, 156(1), 326–340', doi: '10.1121/10.0026475',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11240212/', access: 'fulltext',
    supports: '阅读摘要、引言、方法和结果相关原文段落：谱轮廓任务、整体声级随机变化及高频条件的限制；不把某项轮廓判断较差写成所有高频听觉丧失，不复现样本数据或阈值。',
  },
};
