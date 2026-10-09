import type { Reference } from './references';

export const psychoacousticsReferences: Record<string, Reference> = {
  'psychoacoustics-fastl-2007': {
    title: 'Psychoacoustics: Facts and Models (3rd edition)',
    authors: 'Hugo Fastl; Eberhard Zwicker', year: '2007', publication: 'Springer Berlin, Heidelberg',
    doi: '10.1007/978-3-540-68888-4', url: 'https://link.springer.com/book/10.1007/978-3-540-68888-4', access: 'metadata',
    supports: '核对出版方公开内容简介、目录及第三版书目；支持学科范围与研究方向的概括。未访问付费章节，不用其书目支持具体实验数值。',
  },
  'psychoacoustics-stanislaw-1999': {
    title: 'Calculation of signal detection theory measures',
    authors: 'Harold Stanislaw; Natasha Todorov', year: '1999', publication: 'Behavior Research Methods, Instruments, & Computers, 31(1), 137–149',
    doi: '10.3758/BF03207704', url: 'https://www.jessicagrahn.com/uploads/6/0/8/5/6085172/stanislawtodorovdprim1999.pdf', access: 'fulltext',
    supports: '已阅读公开原文的 yes/no、d′、c、ROC、不同任务与极端比例处理相关段落；正态等方差假设下区分敏感性与判据。文中教学例的数值另由脚本计算。',
  },
  'psychoacoustics-soranzo-2014': {
    title: 'PSYCHOACOUSTICS: a comprehensive MATLAB toolbox for auditory testing',
    authors: 'Alessandro Soranzo; Massimo Grassi', year: '2014', publication: 'Frontiers in Psychology, 5, 712',
    doi: '10.3389/fpsyg.2014.00712', url: 'https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00712/full', access: 'fulltext',
    supports: '已阅读全文阈值、任务、刺激采样、staircase、PEST、MLP 与实验实现章节；用于经典范式及程序比较，不将工具默认参数视为普遍推荐。',
  },
  'psychoacoustics-quest-1983': {
    title: 'Quest: A Bayesian adaptive psychometric method',
    authors: 'Andrew B. Watson; Denis G. Pelli', year: '1983', publication: 'Perception & Psychophysics, 33(2), 113–120',
    doi: '10.3758/BF03202828', url: 'https://link.springer.com/article/10.3758/BF03202828', access: 'abstract',
    supports: '核对出版方原始摘要与书目；支持以当前 Bayesian 阈值估计选取刺激的程序思路，不据摘要描述完整实现或比较所有算法效率。',
  },
  'psychoacoustics-wichmann-ii-2001': {
    title: 'The psychometric function: II. Bootstrap-based confidence intervals and sampling',
    authors: 'Felix A. Wichmann; N. Jeremy Hill', year: '2001', publication: 'Perception & Psychophysics, 63(8), 1314–1329',
    doi: '10.3758/BF03194545', url: 'https://courses.washington.edu/matlab1/pdf/Wichmann_Hill_2001b.pdf', access: 'fulltext',
    supports: '已阅读公开原文的 bootstrap、阈值与斜率置信区间、采样布局及模型错配章节；区间需要相应模型与采样条件。',
  },
  'psychoacoustics-schuett-2016': {
    title: 'Painfree and accurate Bayesian estimation of psychometric functions for (potentially) overdispersed data',
    authors: 'Heiko H. Schütt; Stefan Harmeling; Jakob H. Macke; Felix A. Wichmann', year: '2016', publication: 'Vision Research, 122, 105–123',
    doi: '10.1016/j.visres.2016.02.002', url: 'https://www.mackelab.org/pubs/Schuett_Harmeling_Macke_Wichmann_2016.pdf', access: 'fulltext',
    supports: '已阅读原文的二项/Beta-二项模型、过度离散、状态非稳定与推断章节；适用框架不自动确定变异的感知或设备来源。',
  },
  'psychoacoustics-mok-2024': {
    title: 'Web-based psychoacoustics: Hearing screening, infrastructure, and validation',
    authors: 'Brittany A. Mok; Vibha Viswanathan; Agudemu Borjigin; Ravinderjit Singh; Homeira Kafi; Hari M. Bharadwaj', year: '2024 (online 2023)', publication: 'Behavior Research Methods, 56(3), 1433–1448',
    doi: '10.3758/s13428-023-02101-9', url: 'https://link.springer.com/article/10.3758/s13428-023-02101-9', access: 'fulltext',
    supports: '已阅读作者公开 PDF 的刺激与环境限制、筛查、再邀请样本及经典任务验证章节；支持经过筛选和验证的在线任务作为补充，不等同临床测听或任意设备的绝对声级校准。',
  },
  'psychoacoustics-woods-2017': {
    title: 'Headphone screening to facilitate web-based auditory experiments',
    authors: 'Kevin J. P. Woods; Max H. Siegel; James Traer; Josh H. McDermott', year: '2017', publication: 'Attention, Perception, & Psychophysics, 79(7), 2064–2072',
    doi: '10.3758/s13414-017-1361-2', url: 'https://mcdermottlab.mit.edu/papers/Woods_etal_2017_headphone_screening.pdf', access: 'fulltext',
    supports: '已阅读作者原文的反相三音任务、实验室播放方式验证与在线结果；用于耳机筛查逻辑，不将通过筛查视为声压校准或正常听力证明。',
  },
  'psychoacoustics-grassi-web-2024': {
    title: 'PSYCHOACOUSTICS-WEB: A free online tool for the estimation of auditory thresholds',
    authors: 'Massimo Grassi; Andrea Felline; Niccolò Orlandi; Mattia Toffanin; Gnana Prakash Goli; Hurcan Andrei Senyuva; Mauro Migliardi; Giulio Contemori', year: '2024', publication: 'Behavior Research Methods, 56(7), 7465–7481',
    doi: '10.3758/s13428-024-02430-3', url: 'https://link.springer.com/article/10.3758/s13428-024-02430-3', access: 'fulltext',
    supports: '已通过 Europe PMC 阅读原文的变换升降规则、六类预置任务、实验实现与讨论；介绍 2024 年论文中的工具与验证范围，不声称核对未来版本全部设备兼容性。',
  },
  'psychoacoustics-nist-wilson': {
    title: '7.2.4.1. Confidence intervals',
    authors: 'National Institute of Standards and Technology; SEMATECH', year: '访问于 2026-10-09', publication: 'NIST/SEMATECH e-Handbook of Statistical Methods',
    url: 'https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm', access: 'documentation',
    supports: '已阅读官方方法文档的 Wilson 二项比例区间定义、上下限公式及术语说明；正文两组预设计数的区间另由脚本计算，不是文档实测数据。',
  },
};
