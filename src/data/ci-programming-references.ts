import type { Reference } from './references';

export const ciProgrammingReferences: Record<string, Reference> = {
  'cip-aaa-2019': {
    title: 'Clinical Practice Guideline: Cochlear Implants', authors: 'American Academy of Audiology.', year: '2019',
    publication: 'American Academy of Audiology, July 2019',
    url: 'https://www.audiology.org/wp-content/uploads/2021/05/CochlearImplantPracticeGuidelines.pdf', access: 'fulltext',
    supports: '2026-11-17阅读官方指南的信号处理、编程及随访相关段落，重点为第50–55页：行为与客观测量结合、参数条件、舒适可听和后续验证。指南不规定适合所有人的固定程序；本文不提供可直接输入设备的处方。'
  },
  'cip-asha-portal': {
    title: 'Cochlear Implants', authors: 'American Speech-Language-Hearing Association.', year: '未标年（2026-11-17核验）',
    publication: 'ASHA Practice Portal', url: 'https://www.asha.org/practice-portal/professional-issues/cochlear-implants/', access: 'documentation',
    supports: '阅读Sound Processor Programming及团队照护相关段落：初次刺激与随访、装置检查、个体化行为和客观测量、康复协作；不把某中心复诊时间表写成通用标准。'
  },
  'cip-vaerenberg-2014': {
    title: 'Cochlear Implant Programming: A Global Survey on the State of the Art', authors: 'Vaerenberg B, Smits C, De Ceulaer G, et al.', year: '2014',
    publication: 'The Scientific World Journal, 2014, 501738', doi: '10.1155/2014/501738',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3932199/', access: 'abstract',
    supports: '2026-11-17核对书目、摘要及公开检索到的编程实践与讨论段，说明中心间流程差异和历史调查性质；未将2014年的频次、比例或设备实践当作2026年现状。'
  },
  'cip-mueller-2025': {
    title: 'Recommendations for selection of target parameters and process recommendations for audiological and technical functional testing of cochlear implant',
    authors: 'Müller A, Blümer M, Dziemba OC, et al.', year: '2025', publication: 'HNO, 73, 348–356', doi: '10.1007/s00106-025-01629-w',
    url: 'https://link.springer.com/article/10.1007/s00106-025-01629-w', access: 'fulltext',
    supports: '2026-11-17阅读出版方开放摘要及技术功能检查流程：阻抗、电压矩阵、eCAP、eSRT与必要时eABR，质量控制和长期记录；这是德国专业组织共识建议，不表述为中国强制标准。PMC直接入口遇验证，改读出版方。'
  },
  'cip-cochlear-pulse-2024': {
    title: 'Clinical Programing Series: Pulse Width', authors: 'Duran S; Cochlear.', year: '2024', publication: 'Cochlear ProNews, 7 October 2024',
    url: 'https://pronews.cochlear.com/clinical-programing-series-pulse-width/', access: 'documentation',
    supports: '2026-11-17阅读厂商专业说明：相宽、compliance及速率/maxima的耦合。仅支持所述系统的参数约束，不把厂商默认值推广为所有品牌或以官方材料替代疗效试验；等电荷不等于等响另据Zhou 2020。'
  },
  'cip-saoji-2021': {
    title: 'Effect of exceeding compliance voltage on speech perception in cochlear implants', authors: 'Saoji AA, Adkins WJ, Olund AP, Nelson-Bakkum ER, Koka K.', year: '2021',
    publication: 'Hearing Research, 400, 108112', doi: '10.1016/j.heares.2020.108112', url: 'https://pubmed.ncbi.nlm.nih.gov/33253993/', access: 'abstract',
    supports: '2026-11-17核对原始摘要和书目：超过电压顺应范围导致脉冲削顶，研究其言语识别影响；不转述未完整读取的分组数值，不将屏幕设定值当作实际交付刺激。'
  },
  'cip-devos-2018': {
    title: 'Use of Electrically Evoked Compound Action Potentials for Cochlear Implant Fitting: A Systematic Review',
    authors: 'de Vos JJ, Biesheuvel JD, Briaire JJ, Boot PS, van Gendt MJ, Dekkers OM, Fiocco M, Frijns JHM.', year: '2018',
    publication: 'Ear and Hearing, 39(3), 401–411', doi: '10.1097/AUD.0000000000000495', url: 'https://pubmed.ncbi.nlm.nih.gov/28945656/', access: 'abstract',
    supports: '2026-11-17阅读原始摘要：32项研究的偏倚与群体相关问题，ECAP阈值不能简单换算为个体T/C水平。不据相关性推断听觉感受或日常识别能力。'
  },
  'cip-holder-esrt-2023': {
    title: 'Cochlear Implant Upper Stimulation Levels: eSRT vs. Loudness Scaling', authors: 'Holder JT, Henry MR, MacDonald AE, Gifford RH.', year: '2023',
    publication: 'Otology & Neurotology, 44(9), e667–e672', doi: '10.1097/MAO.0000000000003988', url: 'https://pubmed.ncbi.nlm.nih.gov/37621113/', access: 'abstract',
    supports: '2026-11-17核对原始摘要索引：18位成人20耳的双盲即时比较，eSRT引导MAP的部分识别与音质结果更好。PMC直接入口遇验证；不称为长期随机试验或对所有儿童的效果证明。'
  },
  'cip-holder-mean-2025': {
    title: 'eSRT Versus Population Mean: Setting Upper Stimulation Levels in Adult Cochlear Implant Users', authors: 'Holder JT, MacDonald A, Gifford RH.', year: '2025',
    publication: 'Otology & Neurotology Open, 5(2), e071', doi: '10.1097/ONO.0000000000000071', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12208637/', access: 'fulltext',
    supports: '2026-11-17阅读开放全文方法与结果：177位特定Cochlear成人资料，比较eSRT引导上限和软件群体均值；有电极与时间点缺失、器械和脉冲参数筛选。仅用于群体参考与个体测量区别，不作为所有默认MAP无效的证据。'
  },
  'cip-morton-remote-2025': {
    title: 'Remote Programming of Adult and Pediatric Cochlear Implant Recipients: Clinical Trial Results',
    authors: 'Morton S, Dwyer B, Dwyer N, Holden L, Iannuzzi K, Lewis K, Nelson M, Brown C, Agrawal S, Stein A, Passmore C, Galster J, Zlomke S, Firszt J.', year: '2025',
    publication: 'Otology & Neurotology Open, 5(3), e073', doi: '10.1097/ONO.0000000000000073', url: 'https://pubmed.ncbi.nlm.nih.gov/41017799/', access: 'abstract',
    supports: '2026-11-17阅读PubMed原始摘要及利益关系：5个美国中心、17位至少6个月CI经验者、同一受试者远程与现场程序的安静语句识别比较。结果限于该平台、人群与终点，不能扩展为所有开机、并发症和家庭声场测试等效；部分作者为厂商雇员。'
  },
  'cip-zhou-phase-2020': {
    title: 'Effect of pulse phase duration on forward masking and spread of excitation in cochlear implant listeners', authors: 'Zhou N, Zhu Z, Dong L, Galvin JJ 3rd.', year: '2020',
    publication: 'PLOS ONE, 15(7), e0236179', doi: '10.1371/journal.pone.0236179', url: 'https://pubmed.ncbi.nlm.nih.gov/32687516/', access: 'abstract',
    supports: '2026-11-17阅读原始摘要及PMC公开结果段：10只成人CI耳、等响的长短相宽刺激，电流、电荷、总体掩蔽和归一化扩散指标不等价；不把更窄的扩散直接推断为言语获益。'
  }
};
