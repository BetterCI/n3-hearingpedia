import type { Reference } from './references';

export const speechAudiometryReferences: Record<string, Reference> = {
  'speech-audiometry-quicksin': {
    title: 'Development of a quick speech-in-noise test for measuring signal-to-noise ratio loss in normal-hearing and hearing-impaired listeners',
    authors: 'Killion MC, Niquette PA, Gudmundsen GI, Revit LJ, Banerjee S.', year: '2004',
    publication: 'The Journal of the Acoustical Society of America, 116(4 Pt 1), 2395–2405', doi: '10.1121/1.1784440',
    url: 'https://pubmed.ncbi.nlm.nih.gov/15532670/', access: 'abstract',
    supports: '2026-10-09核对PubMed原始摘要：预录不同SNR序列、关键词50%估计、匹配参考的SNR loss及列表变异。仅用于方法区别，不移用原研究精度为所有测试精度，不转录计分公式或勘误涉及参数。'
  },
  'speech-audiometry-fitzgerald-2024': {
    title: 'Speech-in-Noise Assessment in the Routine Audiologic Test Battery: Relationship to Perceived Auditory Disability',
    authors: 'Fitzgerald MB, Ward KM, Gianakas SP, Smith ML, Blevins NH, Swanson AP.', year: '2024',
    publication: 'Ear and Hearing, 45(4), 816–826', doi: '10.1097/AUD.0000000000001472',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11175785/', access: 'fulltext',
    supports: '2026-10-09阅读原始摘要及Europe PMC同论文全文XML的Materials and Methods、Discussion：1633名成人的单机构回顾资料、耳别WRQ和QuickSIN、SSQ12-Speech5；高频听阈不对称受限。HFPTA与QuickSIN解释部分自评差异，WRQ未增加显著预测贡献；不作因果、普遍替代或疗效结论。'
  },
  'speech-audiometry-cmnbio-2022': {
    title: 'Development and Validation of a Mandarin Chinese Adaptation of AzBio Sentence Test (CMnBio)',
    authors: 'Xi X, Wang Y, Shi Y, Gao R, Li S, Qiu X, Wang Q, Xu L.', year: '2022',
    publication: 'Trends in Hearing, 26, 23312165221134007', doi: '10.1177/23312165221134007',
    url: 'https://people.ohio.edu/xul/xi2022trends.pdf', access: 'fulltext',
    supports: '2026-10-09阅读作者Ohio University存档论文PDF的方法、结果与二项模型部分：正常听力声码器筛选后，在30名经过词语表现筛选的成人CI使用者中安静验证，保留26组列表。关键词计数不等于独立项目数；不推广为所有儿童、低表现者或噪声条件常模。不转载原图。'
  },
  'speech-audiometry-carney-2007': {
    title: 'Critical Difference Table for Word Recognition Testing Derived Using Computer Simulation',
    authors: 'Carney E, Schlauch RS.', year: '2007',
    publication: 'Journal of Speech, Language, and Hearing Research, 50(5), 1203–1209', doi: '10.1044/1092-4388(2007/084)',
    url: 'https://pubs.asha.org/doi/10.1044/1092-4388%282007/084%29', access: 'abstract',
    supports: '2026-10-09阅读出版社结构化摘要：模拟更新10、25、50、100词连续两次识词的95%临界范围；未取得付费全文，不转载临界差异表。本站Wilson教学区间是单次比例估计，并非该文临界范围。'
  },
  'speech-audiometry-nist': {
    title: '7.2.4.1. Confidence intervals', authors: 'NIST / SEMATECH', year: '未标年（2026-10-09核验）',
    publication: 'e-Handbook of Statistical Methods', url: 'https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm', access: 'documentation',
    supports: '已阅读官方Wilson比例区间公式及名称注释。正文和图4独立计算20/25、40/50、80/100双侧95%区间（z=1.96），明确独立同概率二项假设；不冒充词表重测范围、患者误差线或两次差异判断。'
  },
  'speech-audiometry-azbio-2012': {
    title: 'Development and validation of the AzBio sentence lists',
    authors: 'Spahr AJ, Dorman MF, Litvak LM, Van Wie S, Gifford RH, Loizou PC, Loiselle LM, Oakes T, Cook S.', year: '2012',
    publication: 'Ear and Hearing, 33(1), 112–117', doi: '10.1097/AUD.0b013e31822c2549',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4643855/', access: 'fulltext',
    supports: '2026-10-09阅读PMC引言、材料构建、List Equivalency Validation与原始摘要：从CI模拟构建后在真实CI使用者验证列表，并分析个体列表变异和二项近似。仅支持材料验证与统计条件，不引入美国植入候选标准或转载原图。'
  },
  'speech-audiometry-din-2025': {
    title: 'Validation of a smartphone-based digits-in-noise hearing test in Mandarin Chinese',
    authors: 'Gu X, Mima Y, Swanepoel DW, Smits C, Li J, Wang S, Fu X.', year: '2025',
    publication: 'International Journal of Audiology, 64(11), 1138–1145', doi: '10.1080/14992027.2025.2473051',
    url: 'https://pubmed.ncbi.nlm.nih.gov/40042200/', access: 'abstract',
    supports: '2026-10-09核对PubMed出版信息与原始摘要：191名成人、不同双耳刺激条件，与PTA比较，支持具体普通话手机DIN实现用于筛查。未阅读全文；不转录筛查界限为通用常模，不宣称任何手机／耳机均已验证。'
  },
};
