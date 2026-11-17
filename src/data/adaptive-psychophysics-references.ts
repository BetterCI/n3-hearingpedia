import type { Reference } from './references';

export const adaptivePsychophysicsReferences: Record<string, Reference> = {
  'adaptive-kontsevich-1999': {
    title: 'Bayesian adaptive estimation of psychometric slope and threshold',
    authors: 'Leonid L. Kontsevich; Christopher W. Tyler', year: '1999', publication: 'Vision Research, 39(16), 2729–2737',
    doi: '10.1016/S0042-6989(98)00285-5', url: 'https://www.psychophysics.ethz.ch/Downloads/protected/Kontsevich.pdf', access: 'fulltext',
    supports: '2026-11-17：读取原文PDF的模型、联合后验与预期信息选点相关内容；不将视觉任务中的试次数与精度外推为听觉通用规格。',
  },
  'adaptive-watson-2017': {
    title: 'QUEST+: A general multidimensional Bayesian adaptive psychometric method',
    authors: 'Andrew B. Watson', year: '2017', publication: 'Journal of Vision, 17(3), 10',
    doi: '10.1167/17.3.10', url: 'https://pubmed.ncbi.nlm.nih.gov/28355623/', access: 'abstract',
    supports: '2026-11-17：原始摘要搜索索引核对多维刺激、参数与反应框架；出版方全文403，PubMed打开正文不完整。仅支持方法范围，不报告效率数值或全文实现细节。',
  },
  'adaptive-psychopy': {
    title: 'psychopy.data: StairHandler, QuestHandler, PsiHandler and QuestPlusHandler',
    authors: 'PsychoPy contributors', year: '2026-11-17访问', publication: 'PsychoPy official API documentation',
    url: 'https://psychopy.org/api/data.html', access: 'documentation',
    supports: '读取官方API的阶梯规则、applyInitialRule、步长坐标、范围及nTrials与nReversals共同停止条件；用于实现核对，不表示运行验证第三方包。教学模拟使用独立代码。',
  },
};
