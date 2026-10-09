import type { Reference } from './references';

export const speechRedundancyReferences: Record<string, Reference> = {
  'redundancy-miller-1950': {
    title: 'The Intelligibility of Interrupted Speech', authors: 'Miller GA, Licklider JCR.', year: '1950',
    publication: 'Journal of the Acoustical Society of America, 22(2), 167–173', doi: '10.1121/1.1906584',
    url: 'https://www.mpi.nl/publications/item2364423/intelligibility-interrupted-speech', access: 'fulltext',
    supports: '2026-10-09核对机构存档原始PDF摘要及Interrupted Speech in Quiet：中断速率、保留比例与不同噪声操作；原实验词表、小样本与装置条件限制普遍化。'
  },
  'redundancy-warren-1970': {
    title: 'Perceptual Restoration of Missing Speech Sounds', authors: 'Warren RM.', year: '1970',
    publication: 'Science, 167(3917), 392–393', doi: '10.1126/science.167.3917.392',
    url: 'https://pubmed.ncbi.nlm.nih.gov/5409744/', access: 'abstract',
    supports: '2026-10-09核对PubMed索引摘要及种子后向记录：噪声替换与静音替换导致不同的缺失声音体验；不据此推断一般加噪声提高理解。'
  },
  'redundancy-spectral-1995': {
    title: 'Spectral redundancy: intelligibility of sentences heard through narrow spectral slits',
    authors: 'Warren RM, Riener KR, Bashford JA Jr, Brubaker BS.', year: '1995',
    publication: 'Perception & Psychophysics, 57(2), 175–182', doi: '10.3758/BF03206503',
    url: 'https://pubmed.ncbi.nlm.nih.gov/7885815/', access: 'abstract',
    supports: '2026-10-09核对原始摘要：句子窄带识别依赖中心频率和滤波条件，低效单带组合可产生协同；不把带宽比例换算成信息百分比。'
  },
  'redundancy-schneidman-2003': {
    title: 'Synergy, redundancy, and independence in population codes', authors: 'Schneidman E, Bialek W, Berry MJ II.', year: '2003',
    publication: 'Journal of Neuroscience, 23(37), 11539–11553', doi: '10.1523/JNEUROSCI.23-37-11539.2003',
    url: 'https://pubmed.ncbi.nlm.nih.gov/14684857/', access: 'abstract',
    supports: '2026-10-09核对摘要及公开图注：线索相关、条件相关与对目标的信息关系不同，编码与解码评价不同。本文离散算例为原创教学计算，不是该文数据或语音实验。'
  },
  'redundancy-ci-restoration-2014': {
    title: 'Top-down restoration of speech in cochlear-implant users', authors: 'Bhargava P, Gaudrain E, Başkent D.', year: '2014',
    publication: 'Hearing Research, 309, 113–123', doi: '10.1016/j.heares.2013.12.003',
    url: 'https://pubmed.ncbi.nlm.nih.gov/24368138/', access: 'abstract',
    supports: '2026-10-09核对原始摘要：真实人工耳蜗使用者与正常听力、8通道声码器组的模式不同；部分条件存在恢复，连续感与识别获益分开测量。'
  },
  'redundancy-pitch-resolution-2016': {
    title: 'Pitch and spectral resolution: A systematic comparison of bottom-up cues for top-down repair of degraded speech',
    authors: 'Clarke J, Başkent D, Gaudrain E.', year: '2016', publication: 'Journal of the Acoustical Society of America, 139(1), 395–405',
    doi: '10.1121/1.4939962', url: 'https://pubmed.ncbi.nlm.nih.gov/26827034/', access: 'abstract',
    supports: '2026-10-09核对PubMed检索摘要及作者网站元数据：独立操纵音高和谱分辨，整体识别与填充噪声差值的改变不同；不把模拟器视为真实电刺激。'
  },
  'redundancy-visual-2015': {
    title: 'The effect of visual cues on top-down restoration of temporally interrupted speech, with and without further degradations',
    authors: 'Benard MR, Başkent D.', year: '2015', publication: 'Hearing Research, 328, 24–33', doi: '10.1016/j.heares.2015.06.013',
    url: 'https://research.rug.nl/en/publications/the-effect-of-visual-cues-on-top-down-restoration-of-temporally-i/', access: 'abstract',
    supports: '2026-10-09核对作者机构原始摘要：视频提高整体识别，未改变填充噪声恢复获益；实验包括正常语音、人工耳蜗与电声联合刺激的声学模拟。'
  },
  'redundancy-cortex-2016': {
    title: 'Perceptual restoration of masked speech in human cortex', authors: 'Leonard MK, Baud MO, Sjerps MJ, Chang EF.', year: '2016',
    publication: 'Nature Communications, 7, 13619', doi: '10.1038/ncomms13619',
    url: 'https://www.nature.com/articles/ncomms13619', access: 'fulltext',
    supports: '2026-10-09核对Abstract、Introduction及词对实验说明：人体直接皮层记录连接噪声替换语音的主观报告和声学语音特征表征；保留相关记录和特定样本边界，不当作完整因果机制。'
  },
  'redundancy-nonnative-2016': {
    title: 'Missing phonemes are perceptually restored but differently by native and non-native listeners', authors: 'Ishida M, Arai T.', year: '2016',
    publication: 'SpringerPlus, 5, 713', doi: '10.1186/s40064-016-2479-8',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4908083/', access: 'fulltext',
    supports: '2026-10-09经Europe PMC原文XML核对Abstract、Results和任务：英语母语与日语母语英语二语者、噪声叠加/替换、词/非词及8点相似性评分；不把主观相似性当作识词正确率。'
  },
  'redundancy-prosody-2023': {
    title: 'Quantifying the redundancy between prosody and text',
    authors: 'Wolf L, Pimentel T, Fedorenko E, Cotterell R, Warstadt A, Wilcox EG, Regev TI.', year: '2023',
    publication: 'Proceedings of EMNLP 2023, 9765–9784', doi: '10.18653/v1/2023.emnlp-main.606',
    url: 'https://aclanthology.org/2023.emnlp-main.606/', access: 'fulltext',
    supports: '2026-10-09核对官方摘要、原始PDF结果与Discussion：英语有声书韵律和文本的模型估计互信息，文本未解释全部韵律；模型预测关系不等于听者恢复能力。'
  },
  'redundancy-context-scale-2025': {
    title: 'The time scale of redundancy between prosody and linguistic context',
    authors: 'Regev TI, Ohams C, Xie S, Wolf L, Fedorenko E, Warstadt A, Wilcox EG, Pimentel T.', year: '2025',
    publication: 'Proceedings of ACL 2025 (Volume 1: Long Papers), 30476–30488', doi: '10.18653/v1/2025.acl-long.1471',
    url: 'https://aclanthology.org/2025.acl-long.1471/', access: 'fulltext',
    supports: '2026-10-09核对官方发表版本Abstract、Methods、Results、Limitations：英语有声书前后上下文窗口与韵律条件分布估计；特征差异、朗读语料与模型估计边界，不宣称直接测量人脑记忆。'
  },
};
