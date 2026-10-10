import type { Reference } from './references';

export const amFmReferences: Record<string, Reference> = {
  'amfm-mathworks-analog': {
    title: 'Analog Baseband Modulation', authors: 'MathWorks', year: '官方文档（2026-10-10 核验）', publication: 'Communications Toolbox 官方文档',
    url: 'https://www.mathworks.com/help/comm/ug/analog-baseband-modulation.html', access: 'documentation',
    supports: '阅读一般载波模型及 AM、FM、PM 定义；用于区分幅度与相位轨迹。本文采样条件另依据实际边带与数值误差核验，未将简化载波采样条件推广为所有 FM 的充分条件。',
  },
  'amfm-mathworks-modulate': {
    title: 'modulate — Modulation', authors: 'MathWorks', year: '官方文档（2026-10-10 核验）', publication: 'Signal Processing Toolbox 官方文档',
    url: 'https://www.mathworks.com/help/signal/ref/modulate.html', access: 'documentation',
    supports: '阅读 am、amdsb-tc、fm、pm 等方法定义和参数：默认 am 为抑制载波形式；FM 累积调制输入，PM 直接改变相位。未实际运行 MATLAB，也未把默认参数当作心理声学刺激规范。',
  },
  'amfm-nist-bessel': {
    title: 'DLMF §10.12 — Generating Function and Associated Series', authors: 'NIST Digital Library of Mathematical Functions',
    year: '在线数学参考（2026-10-10 核验）', publication: 'NIST DLMF, Bessel Functions',
    url: 'https://dlmf.nist.gov/10.12', access: 'documentation',
    supports: '阅读生成函数与 Jacobi–Anger 展开；支持正弦 FM 的贝塞尔边带系数。图中符号、FFT 系数、截断阶数和平方和由本文独立计算，不是听觉实验结果。',
  },
  'amfm-amt-dau': {
    title: 'dau1997 — Modulation filterbank model', authors: 'Auditory Modeling Toolbox', year: 'AMT 1.6.0 文档（2026-10-10 核验）',
    publication: 'Auditory Modeling Toolbox 官方模型文档', url: 'https://amtoolbox.org/amt-1.6.0/doc/models/dau1997.php', access: 'documentation',
    supports: '阅读滤波、整流、低通、适应环和调制滤波器的结构及 fc / mfc 输出说明；未实际运行工具箱、拟合阈值或验证神经回路。',
  },
  'amfm-moore-sek-1995': {
    title: 'Effects of carrier frequency, modulation rate, and modulation waveform on the detection of modulation and the discrimination of modulation type (amplitude modulation versus frequency modulation)',
    authors: 'Brian C. J. Moore; Aleksander Sęk', year: '1995', publication: 'Journal of the Acoustical Society of America, 97(4), 2468–2478',
    doi: '10.1121/1.411967', url: 'https://pubmed.ncbi.nlm.nih.gov/7714263/', access: 'abstract',
    supports: '阅读原始摘要：载波、速率、波形及匹配检测显著性后的 AM/FM 类型辨别。未读取全文阈值曲线，未据此指定普适速率分界。',
  },
  'amfm-moore-sek-1996': {
    title: 'Detection of frequency modulation at low modulation rates: evidence for a mechanism based on phase locking',
    authors: 'Brian C. J. Moore; Aleksander Sęk', year: '1996', publication: 'Journal of the Acoustical Society of America, 100(4 Pt 1), 2320–2331',
    doi: '10.1121/1.417941', url: 'https://pubmed.ncbi.nlm.nih.gov/8865639/', access: 'abstract',
    supports: '阅读原始摘要：随载波及调制速率变化的附加 AM 干扰，为慢速 FM 时间编码解释提供行为证据。不是直接神经记录，也未读取全文参数表。',
  },
  'amfm-whiteford-place-2020': {
    title: 'The role of cochlear place coding in the perception of frequency modulation', authors: 'Kelly L. Whiteford; Heather A. Kreft; Andrew J. Oxenham',
    year: '2020', publication: 'eLife, 9, e58468', doi: '10.7554/eLife.58468', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7556860/', access: 'fulltext',
    supports: '通过 Europe PMC 原文 XML 阅读摘要、讨论中统一位置编码与替代解释、FM/AM 检测与跨载波 AM 相干辨别方法和参与者筛选；并核对期刊图页。未复现阈值数据；相关与模拟任务不能证明时间编码完全不存在。',
  },
  'amfm-corbett-2026': {
    title: 'Detecting continuous and discrete frequency changes as a function of spectral resolvability and modulation rate',
    authors: 'Penelope J. Corbett; Kelly L. Whiteford; Andrew J. Oxenham', year: '2026', publication: 'JASA Express Letters, 6(7), 074401',
    doi: '10.1121/10.0044323', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC13339214/', access: 'fulltext',
    supports: '阅读原文 XML 摘要、参与者、连续 FM 与离散音序列、程序、结果及讨论相关段落；已发表期刊论文，非预印本。用于限定简单侧带解析或频率快照预测，未把它解释成否定所有 FM-to-AM 转换。',
  },
  'amfm-moore-age-2019': {
    title: 'Effects of Age and Hearing Loss on the Discrimination of Amplitude and Frequency Modulation for 2- and 10-Hz Rates',
    authors: 'Brian C. J. Moore; S. Mariathasan; Aleksander P. Sęk', year: '2019', publication: 'Trends in Hearing, 23',
    doi: '10.1177/2331216519853963', url: 'https://pubmed.ncbi.nlm.nih.gov/31250705/', access: 'abstract',
    supports: '阅读原始摘要：匹配检测效率后的类型辨别，年龄和听损相关差异及个体异质性。全文 XML 获取失败，未声称读取全部方法或把任务作为独立临床诊断。',
  },
};
