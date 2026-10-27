import type { Reference } from './references';

export const phaseGroupDelayReferences: Record<string, Reference> = {
  'pd-farina-2000': {
    title: 'Simultaneous Measurement of Impulse Response and Distortion with a Swept-Sine Technique', authors: 'Angelo Farina', year: '2000', publication: 'Audio Engineering Society, 108th Convention, Paper 5093',
    url: 'https://aes.org/publications/elibrary/elibrary-page/?id=10211', access: 'abstract',
    supports: '读取AES官方摘要与会议书目：指数扫频、弱非线性近似时不变系统、与MLS比较，适用扬声器、电声器件与房间测量。未读全文，不转录去卷积实现、谐波分离细节或测量精度参数。',
  },
  'pd-smith-2007': {
    title: 'Introduction to Digital Filters with Audio Applications — Phase and Group Delay; Allpass Filters; Minimum-Phase Filters',
    authors: 'Julius O. Smith III', year: '2007', publication: 'W3K Publishing / 作者公开在线教材（DSPRelated镜像）',
    url: 'https://www.dsprelated.com/freebooks/filters/Phase_Group_Delay.html', access: 'fulltext',
    supports: '读取相位/群延迟定义、展开相位、窄带调制推导，并交叉阅读同书Allpass Filters和Minimum-Phase Filters章节。三章属于同一教材，不当作三项独立证据。本站全通、两路径及误差算例为自主推导和数值教学计算。',
  },
  'pd-mathworks-delay': {
    title: 'Group Delay and Phase Delay', authors: 'The MathWorks, Inc.', year: '访问于2026-10-27', publication: 'Signal Processing Toolbox 官方文档',
    url: 'https://www.mathworks.com/help/signal/ug/delay.html', access: 'documentation',
    supports: '核对两种延迟的定义、对称线性相位FIR的N/2样本群延迟及IIR示例。未沿用页面中对全部稳定IIR的概括；正文只描述常见滤波器和有效频带。',
  },
  'pd-scipy-group-delay': {
    title: 'scipy.signal.group_delay', authors: 'SciPy community', year: '访问于2026-10-27', publication: 'SciPy 官方API文档',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.group_delay.html', access: 'documentation',
    supports: '核对离散时间群延迟、频率坐标fs与返回延迟的样本单位，以及单位圆零极点处群延迟未定义而软件可能返回0的行为。生成脚本另记录本地SciPy 1.17.1实算结果，不把在线文档版本冒充执行版本。',
  },
  'pd-scipy-filtfilt': {
    title: 'scipy.signal.filtfilt', authors: 'SciPy community', year: '访问于2026-10-27', publication: 'SciPy 官方API文档',
    url: 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html', access: 'documentation',
    supports: '读取前后向两次滤波、零相位、有效阶数、端点延拓与瞬态说明；正文幅度平方关系限定为实系数滤波器的理想内部稳态频率响应。',
  },
  'pd-mne-filtering': {
    title: 'Background information on filtering', authors: 'MNE-Python developers', year: '访问于2026-10-27', publication: 'MNE-Python 官方方法教程',
    url: 'https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html', access: 'documentation',
    supports: '阅读因果/非因果、线性相位延迟补偿、滤波时间扩散和低通问题相关段落；仅支持方法解释，不支持具体神经起始时间或临床结论。',
  },
  'pd-liski-2021': {
    title: 'Audibility of Group-Delay Equalization', authors: 'Juho Liski; Aki Mäkivirta; Vesa Välimäki', year: '2021', publication: 'IEEE/ACM Transactions on Audio, Speech, and Language Processing, 29, 2189–2201',
    doi: '10.1109/TASLP.2021.3087969', url: 'https://research.aalto.fi/en/publications/audibility-of-group-delay-equalization/', access: 'abstract',
    supports: '读取作者所在大学研究门户摘要及正式书目：全通操纵、四种刺激、耳机ABX与刺激/正负相对延迟变化的依赖性。未读全文，不将摘要阈值推广为听觉常模或助听器规格。',
  },
  'pd-shera-guinan-2003': {
    title: 'Stimulus-frequency-emission group delay: a test of coherent reflection filtering and a window on cochlear tuning', authors: 'Christopher A. Shera; John J. Guinan Jr.', year: '2003', publication: 'The Journal of the Acoustical Society of America, 113(5), 2762–2772',
    doi: '10.1121/1.1557211', url: 'https://pubmed.ncbi.nlm.nih.gov/12765394/', access: 'abstract',
    supports: '阅读PubMed摘要：猫、豚鼠及人SFOAE群延迟，反射理论、耳蜗基底与顶端解释差异。只概括测量与模型检验，不据摘要推导个体常模或单程传播时长。',
  },
  'pd-shera-tuning-2010': {
    title: 'Otoacoustic Estimation of Cochlear Tuning: Validation in the Chinchilla', authors: 'Christopher A. Shera; John J. Guinan Jr.; Andrew J. Oxenham', year: '2010', publication: 'Journal of the Association for Research in Otolaryngology, 11(3), 343–365',
    doi: '10.1007/s10162-010-0217-4', url: 'https://pubmed.ncbi.nlm.nih.gov/20440634/', access: 'abstract',
    supports: '读取PubMed摘要并核对公开PMC索引中的物种比较讨论：龙猫听神经/OAE资料检验、人类外推的调谐比假设。PMC完整抓取失败，因此保守标为摘要访问，不声称逐段全文审阅。',
  },
  'pd-shera-bergevin-2012': {
    title: 'Obtaining reliable phase-gradient delays from otoacoustic emission data', authors: 'Christopher A. Shera; Christopher Bergevin', year: '2012', publication: 'The Journal of the Acoustical Society of America, 132(2), 927–943',
    doi: '10.1121/1.4730916', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3427360/', access: 'fulltext',
    supports: '经公开PMC网页读取摘要、引言、模型、数值求导及六种估计方法比较相关段落；反射源固有相位波动、相位平滑偏差与多重反射分离。模型研究，不能将某种峰值选择方法视为所有实测响应的通用标准。',
  },
  'pd-roth-2024': {
    title: 'Effect of a processing delay between direct and delayed sound in simulated open fit hearing aids on speech intelligibility in noise', authors: 'Sebastian Roth; Franz-Ullrich Müller; Julian Angermeier; Werner Hemmert; Stefan Zirn', year: '2024（卷号标为2023）', publication: 'Frontiers in Neuroscience, 17, 1257720；在线发表于2024-01-04',
    doi: '10.3389/fnins.2023.1257720', url: 'https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1257720/full', access: 'fulltext',
    supports: '通过公开Europe PMC全文XML核对方法、结果和局限：13名正常听力者、单/双侧开放验配模拟、空间分离噪声SRT、衰减式听损模拟。正文不沿用摘要将SRT由负18.1至负14.7 dB误称decrease的措辞；不把模拟结论推广到真实助听器用户。',
  },
  'pd-susonn-2024': {
    title: 'Individual Differences Underlying Preference for Processing Delay in Open-Fit Hearing Aids', authors: 'Borgný Súsonnudóttir; Borys Kowalewski; Georg Stiefenhofer; Tobias Neher', year: '2024', publication: 'Trends in Hearing, 28, 23312165241298613',
    doi: '10.1177/23312165241298613', url: 'https://journals.sagepub.com/doi/10.1177/23312165241298613', access: 'fulltext',
    supports: '读取出版社摘要及Europe PMC全文XML中参与者、助听器模拟、延迟条件、偏好与谱波纹任务结果：10名正常听力、20名轻中度感音神经性听损，五种延迟。频谱任务与偏好关系是特定模拟条件下的发现，不能直接当个体处方规则。',
  },
  'pd-susonn-2026': {
    title: 'Own-Voice Perception with Different Processing Delays in Open-Fit Hearing Aids', authors: 'Borgný Súsonnudóttir; Lars D. Mosgaard; Georg Stiefenhofer; Pamela E. Souza; Tobias Neher', year: '2026', publication: 'Trends in Hearing, 30, 23312165261435260；在线发表于2026-03-23',
    doi: '10.1177/23312165261435260', url: 'https://journals.sagepub.com/doi/10.1177/23312165261435260', access: 'fulltext',
    supports: '读取出版社全文结果与Table 2、Table 5、Figure 6及Europe PMC全文XML：24名轻中度听损者、原型开放验配、自声，0.5/5/10 ms；区分三条件成对比较多重校正后不显著与问卷0.5/10 ms偏好评分显著，SRD未预测偏好。保留开放耳塞、实验室及增益条件限制。',
  },
  'pd-xia-2024': {
    title: 'Evaluating the Correlation Between Stimulus Frequency Otoacoustic Emission Group Delays and Tuning Sharpness in a Cochlear Model', authors: 'Yiwei Xia; George Samaras; Julien Meaud', year: '2024', publication: 'Journal of the Association for Research in Otolaryngology, 25(6), 575–589',
    doi: '10.1007/s10162-024-00968-9', url: 'https://pubmed.ncbi.nlm.nih.gov/39511036/', access: 'abstract',
    supports: '读取PubMed结构式摘要并核对PMC索引方法段：改变模型微观参数或声级时，调谐展宽和SFOAE延迟缩短的对应可不同。正文只使用摘要可支持的模型条件依赖结论，不据模型宣称临床诊断性能。',
  },
};
