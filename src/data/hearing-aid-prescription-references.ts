import type { Reference } from './references';

export const hearingAidPrescriptionReferences: Record<string, Reference> = {
  'prescription-nal-empirical-2012': {
    title: 'NAL-NL2 Empirical Adjustments', authors: 'Keidser G, Dillon H, Carter L, O’Brien A.', year: '2012',
    publication: 'Trends in Amplification, 16(4), 211–223', doi: '10.1177/1084713812468511',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4040825/', access: 'fulltext',
    supports: '2026-10-09核对Introduction、Overall Loudness Adjustments及Evaluation：理论目标与人群偏好修正、年龄和经验等变量及个体差异；不把平均修正当作单个人固定需求。'
  },
  'prescription-nal-r-1986': {
    title: 'The National Acoustic Laboratories’ (NAL) new procedure for selecting the gain and frequency response of a hearing aid',
    authors: 'Byrne D, Dillon H.', year: '1986', publication: 'Ear and Hearing, 7(4), 257–265', doi: '10.1097/00003446-198608000-00007',
    url: 'https://pubmed.ncbi.nlm.nih.gov/3743918/', access: 'abstract',
    supports: '2026-10-09核对原始摘要：由纯音听阈预测线性增益与频率响应的研究依据。未声称核读原始论文全部方程；六频率系数及软件分支另依据固定版本Clarity官方代码。'
  },
  'prescription-dsl-protocols-2005': {
    title: 'Clinical Protocols for Hearing Instrument Fitting in the Desired Sensation Level Method',
    authors: 'Bagatto M, Moodie S, Scollie S, Seewald R, Moodie S, Pumford J, Liu KPR.', year: '2005',
    publication: 'Trends in Amplification, 9(4), 199–226', doi: '10.1177/108471380500900404',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4111495/', access: 'fulltext',
    supports: '2026-10-09核对公开正文的声学转换、RECD和电生理阈值估计段：相容换能器与耦合腔、个体耳道声学、听阈坐标；不提供探管插入操作处方。'
  },
  'prescription-johnson-dillon-2011': {
    title: 'A comparison of gain for adults from generic hearing aid prescriptive methods: Impacts on predicted loudness, frequency bandwidth, and speech intelligibility',
    authors: 'Johnson EE, Dillon H.', year: '2011', publication: 'Journal of the American Academy of Audiology, 22(7), 441–459', doi: '10.3766/jaaa.22.7.5',
    url: 'https://research.manchester.ac.uk/en/publications/a-comparison-of-gain-for-adults-from-generic-hearing-aid-prescrip/', access: 'abstract',
    supports: '2026-10-09核对作者机构收录的原始摘要：假设听力图、各处方软件和响度／言语模型的比较；明确是模型结果，不写成人随机试验。'
  },
  'prescription-lochi-three-2013': {
    title: 'A randomized controlled comparison of NAL and DSL prescriptions for young children: Hearing-aid characteristics and performance outcomes at three years of age',
    authors: 'Ching TYC, Dillon H, Hou S, Zhang V, Day J, Crowe K, Marnane V, Street L, Burns L, Van Buynder P, Flynn C, Thomson J.',
    year: '2013（在线2012）', publication: 'International Journal of Audiology, 52(Suppl 2), S17–S28', doi: '10.3109/14992027.2012.705903',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3659194/', access: 'fulltext',
    supports: '2026-10-09核对Abstract、Method／Hearing-aid fitting：218儿童、NAL-NL1与DSL v4.1初次分配及后续DSL版本变化；语言与功能结果未显著，不解释为逐个等效。'
  },
  'prescription-lochi-five-2018': {
    title: 'Hearing aid fitting and developmental outcomes of children fit according to either the NAL or DSL prescription: fit-to-target, audibility, speech and language abilities',
    authors: 'Ching TYC, Zhang VW, Johnson EE, Van Buynder P, Hou S, Burns L, Button L, Flynn C, McGhie K.',
    year: '2018（在线2017）', publication: 'International Journal of Audiology, 57(Suppl 2), S41–S54', doi: '10.1080/14992027.2017.1380851',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5882607/', access: 'fulltext',
    supports: '2026-10-09核对Abstract及Discussion：232儿童拟合资料、163随机试验，版本混合，低声级可听性、未显著言语语言差异与DSL较高家长功能评分分别报告。'
  },
  'prescription-child-fit-2013': {
    title: 'Characteristics of hearing aid fittings in infants and young children', authors: 'McCreery RW, Bentler RA, Roush PA.', year: '2013',
    publication: 'Ear and Hearing, 34(6), 701–710', doi: '10.1097/AUD.0b013e31828f1033',
    url: 'https://pubmed.ncbi.nlm.nih.gov/23575463/', access: 'abstract',
    supports: '2026-10-09核对原始摘要：以500、1000、2000、4000Hz的RMS目标误差与SII区分目标匹配和可听性；不将研究阈值当作通用验配容差。'
  },
  'prescription-task-audibility-2023': {
    title: 'Task-Dependent Effects of Signal Audibility for Processing Speech: Comparing Performance With NAL-NL2 and DSL v5 Hearing Aid Prescriptions at Threshold and at Suprathreshold Levels in 9- to 17-Year-Olds With Hearing Loss',
    authors: 'Pittman AL, Stewart EC.', year: '2023', publication: 'Trends in Hearing, 27, 23312165231177509', doi: '10.1177/23312165231177509',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10236245/', access: 'fulltext',
    supports: '2026-10-09核对Abstract及Discussion／Implications：16名9—17岁参与者、处方和声级操纵、检测识别与回忆学习的任务依赖；不推广为可听性不重要。'
  },
  'prescription-preference-2023': {
    title: 'Listening Preferences of New Adult Hearing Aid Users: A Registered, Double-Blind, Randomized, Mixed-Methods Clinical Trial of Initial Versus Real-Ear Fit',
    authors: 'Almufarrij I, Dillon H, Adams B, Greval A, Munro KJ.', year: '2023', publication: 'Trends in Hearing, 27, 23312165231189596', doi: '10.1177/23312165231189596',
    url: 'https://journals.sagepub.com/doi/10.1177/23312165231189596', access: 'fulltext',
    supports: '2026-10-09核对原始摘要、Methods及公开作者稿：45名新使用者、两个程序均按即时反馈调整、偏好初始设置与舒适度解释，保留设备、流程及结局限制。'
  },
  'prescription-binaural-loudness-2025': {
    title: 'Prevalence of excess binaural broadband loudness summation in the hearing-impaired population and implications for hearing aid gain targets',
    authors: 'Denk F, Oetting D, Latzel M, Bonsel H, Husstedt H.', year: '2025', publication: 'PLOS ONE, 20(8), e0330517', doi: '10.1371/journal.pone.0330517',
    url: 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0330517', access: 'fulltext',
    supports: '2026-10-09核对Abstract和研究框架：180听损参与者、双耳宽带响度整合及目标比较，个体差异；不宣称某处方长期普遍优效。'
  },
  'prescription-nalnl3-official': {
    title: 'NAL-NL3: The Next Generation Fitting System', authors: 'National Acoustic Laboratories', year: '2025；2026-10-09核验',
    publication: 'NAL官方产品与发布资料', url: 'https://www.nal.gov.au/nal_products/nal-nl3-the-next-generation-fitting-system/', access: 'documentation',
    supports: '核对官方版本沿革、NAL-NL3主体处方、Comfort in Noise与Minimal Hearing Loss模块；官方数据驱动描述只作为开发与用途记录，不作独立疗效证据。'
  },
  'prescription-nalnl3-clinical-2026': {
    title: 'Using NAL-NL3 in clinical practice: a modular NAL fitting system for real-world listening needs', authors: 'Croteau M, Kwok C.', year: '2026',
    publication: 'International Journal of Audiology；2026-06-27在线发表，1–13', doi: '10.1080/14992027.2026.2680131',
    url: 'https://pubmed.ncbi.nlm.nih.gov/42363720/', access: 'abstract',
    supports: '2026-10-09核对PubMed原始摘要：Clinical Note文章类型、三模块及其用途；不把应用说明改写为独立随机优效试验，未声称阅读全文或算法参数。'
  },
  'prescription-nal-philosophy-2026': {
    title: 'Evolving the philosophy: from the NAL rule to NAL-NL3', authors: 'Kitterick PT, Zakis JA, Edwards B.', year: '2026',
    publication: 'International Journal of Audiology；2026-06-24在线发表，1–10', doi: '10.1080/14992027.2026.2690236',
    url: 'https://www.tandfonline.com/doi/full/10.1080/14992027.2026.2690236', access: 'fulltext',
    supports: '2026-10-09核对作者机构出版记录及公开Introduction、The modern era段落：NAL线性与非线性哲学变化、响度标签的简化限制；属于讨论论文，非比较效果综述。'
  },
  'prescription-nalnl3-noise-2026': {
    title: 'A new approach to hearing aid gain prescription for listening in noise: the NAL-NL3 Comfort in Noise Module',
    authors: 'Kitterick PT, Zakis JA, Kwok C, Croteau M, Monaghan JJM et al.', year: '2026',
    publication: 'International Journal of Audiology；2026-09-18在线发表，1–27', doi: '10.1080/14992027.2026.2725523',
    url: 'https://www.tandfonline.com/doi/full/10.1080/14992027.2026.2725523', access: 'fulltext',
    supports: '2026-10-09核对出版社公开正文中的Abstract、研究设计和讨论，以及PubMed书目信息：83名成人、单中心多研究迭代、实验室及日常即时评价、选择性降低增益与噪声舒适偏好；未把未检出言语损害解释为所有场景严格等效。'
  }
};
