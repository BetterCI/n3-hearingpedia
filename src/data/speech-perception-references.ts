import type { Reference } from './references';

export const speechPerceptionReferences: Record<string, Reference> = {
  'speech-shortlist-2008': {
    title: 'Shortlist B: A Bayesian model of continuous speech recognition', authors: 'Dennis Norris; James M. McQueen', year: '2008',
    publication: 'Psychological Review, 115(2), 357–395', doi: '10.1037/0033-295X.115.2.357',
    url: 'https://www.mpi.nl/publications/item60906/shortlist-b-bayesian-model-continuous-speech-recognition', access: 'abstract',
    supports: '2026-10-10阅读机构原始摘要并核对Crossref：保留不确定性的语音输入、并行词汇假设、前馈结构及分割问题。作者PDF本轮获取失败；图4为通用贝叶斯赔率教学计算，不是该模型实现或结果复现。'
  },
  'speech-trace-1986': {
    title: 'The TRACE model of speech perception', authors: 'James L. McClelland; Jeffrey L. Elman', year: '1986',
    publication: 'Cognitive Psychology, 18(1), 1–86', doi: '10.1016/0010-0285(86)90015-0',
    url: 'https://web.stanford.edu/~jlmcc/papers/McClellandElman86.pdf', access: 'fulltext',
    supports: '2026-10-10阅读作者存档原文首页、Some Important Facts about Speech及结构段：时间重叠、无固定词边界、线索情境依赖、特征—音位—词语单元及激活竞争。仅使用相关段落，未复现程序或逐项核验所有模拟结果。'
  },
  'speech-oden-1978': {
    title: 'Integration of featural information in speech perception', authors: 'Gregg C. Oden; Dominic W. Massaro', year: '1978',
    publication: 'Psychological Review, 85(3), 172–191', doi: '10.1037/0033-295X.85.3.172',
    url: 'https://doi.org/10.1037/0033-295X.85.3.172', access: 'abstract',
    supports: '2026-10-10核对Crossref与PubMed书目，并阅读检索可见的原始PDF首页摘要：独立操纵声学线索、原型匹配与特征整合假设。PubMed无摘要；完整PDF打开失败，不据此报告原试次、效应量或模型拟合参数。本文逻辑斯蒂曲面为独立教学表示。'
  },
  'speech-liberman-1957': {
    title: 'The discrimination of speech sounds within and across phoneme boundaries', authors: 'Alvin M. Liberman; Katherine S. Harris; Howard S. Hoffman; Belver C. Griffith', year: '1957',
    publication: 'Journal of Experimental Psychology, 54(5), 358–368', doi: '10.1037/h0044417',
    url: 'https://pubmed.ncbi.nlm.nih.gov/13481283/', access: 'metadata',
    supports: '2026-10-10核对PubMed与Crossref，PubMed无摘要。仅作类别感知实验传统的历史入口，不报告原数据、样本或刺激数值；图3的起声时间曲线并非该文的原始连续体。'
  },
  'speech-mcmurray-2002': {
    title: 'Gradient effects of within-category phonetic variation on lexical access', authors: 'Bob McMurray; Michael K. Tanenhaus; Richard N. Aslin', year: '2002',
    publication: 'Cognition, 86(2), B33–B42', doi: '10.1016/S0010-0277(02)00157-9',
    url: 'https://pubmed.ncbi.nlm.nih.gov/12435537/', access: 'abstract',
    supports: '2026-10-10阅读PubMed原摘要：英语词语起声时间连续体、四图片眼动任务及类别内连续变化对竞争词注视的影响。只报告摘要范围，不把眼动等同全部词汇处理或推广到所有语言。'
  },
  'speech-ganong-1980': {
    title: 'Phonetic categorization in auditory word perception', authors: 'William F. Ganong III', year: '1980',
    publication: 'Journal of Experimental Psychology: Human Perception and Performance, 6(1), 110–125', doi: '10.1037/0096-1523.6.1.110',
    url: 'https://pubmed.ncbi.nlm.nih.gov/6444985/', access: 'abstract',
    supports: '2026-10-10阅读PubMed摘要：真词／非词与起声时间连续体的类别判断，模糊边界处词汇效应更强。PubMed的DOI字符串含双斜线，本表使用Crossref规范化DOI；不凭边界偏移唯一定位感觉反馈。'
  },
  'speech-kleinschmidt-2015': {
    title: 'Robust speech perception: Recognize the familiar, generalize to the similar, and adapt to the novel', authors: 'Dave F. Kleinschmidt; T. Florian Jaeger', year: '2015',
    publication: 'Psychological Review, 122(2), 148–203', doi: '10.1037/a0038695',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4744792/', access: 'abstract',
    supports: '2026-10-10阅读Europe PMC原始摘要及公开检索片段：不变性问题、说话人／情境分布、理想适应者的识别、泛化与适应。PMC正文打开遇验证页，未据此声称本轮阅读全文或复现拟合。'
  },
  'speech-norris-2003': {
    title: 'Perceptual learning in speech', authors: 'Dennis Norris; James M. McQueen; Anne Cutler', year: '2003',
    publication: 'Cognitive Psychology, 47(2), 204–238', doi: '10.1016/S0010-0285(03)00006-9',
    url: 'https://pubmed.ncbi.nlm.nih.gov/12948518/', access: 'abstract',
    supports: '2026-10-10阅读PubMed与出版页原始摘要：荷兰语词尾模糊摩擦音接触后的类别判断偏移；作者明确区分学习反馈与在线词汇反馈。未以短期实验推断长期康复或普遍迁移效果。'
  },
  'speech-saffran-1996': {
    title: 'Statistical learning by 8-month-old infants', authors: 'Jenny R. Saffran; Richard N. Aslin; Elissa L. Newport', year: '1996',
    publication: 'Science, 274(5294), 1926–1928', doi: '10.1126/science.274.5294.1926',
    url: 'https://pubmed.ncbi.nlm.nih.gov/8943209/', access: 'abstract',
    supports: '2026-10-10阅读原始摘要：8个月婴儿、短时接触人工语流与邻接声音统计关系的分割入口。不将测试差异扩展为自然词义习得；条件概率公式为一般计数定义。'
  },
  'speech-werker-1984': {
    title: 'Phonemic and phonetic factors in adult cross-language speech perception', authors: 'Janet F. Werker; Richard C. Tees', year: '1984',
    publication: 'Journal of the Acoustical Society of America, 75(6), 1866–1878', doi: '10.1121/1.390988',
    url: 'https://pubmed.ncbi.nlm.nih.gov/6747097/', access: 'abstract',
    supports: '2026-10-10阅读原始摘要：成人英语听者的非母语对立，知觉定势、AX任务、训练与间隔影响表现；处理策略变化与感觉丧失的区别。不把成人研究当作婴儿年龄常模。'
  },
  'speech-dev-1984': {
    title: 'Cross-language speech perception: Evidence for perceptual reorganization during the first year of life', authors: 'Janet F. Werker; Richard C. Tees', year: '1984',
    publication: 'Infant Behavior and Development, 7(1), 49–63', doi: '10.1016/S0163-6383(84)80022-3',
    url: 'https://doi.org/10.1016/S0163-6383(84)80022-3', access: 'metadata',
    supports: '2026-10-10核对Crossref原版书目及出版社重刊说明（2002年重刊不作另一项研究）；仅支持发展研究沿革，不报告原婴儿分组、效应值或普遍年龄界限。'
  },
  'speech-mcgurk-1976': {
    title: 'Hearing lips and seeing voices', authors: 'Harry McGurk; John MacDonald', year: '1976',
    publication: 'Nature, 264(5588), 746–748', doi: '10.1038/264746a0',
    url: 'https://pubmed.ncbi.nlm.nih.gov/1012311/', access: 'metadata',
    supports: '2026-10-10核对PubMed与出版页书目，PubMed无摘要；用于发现史定位。效应内容与发现过程另据作者2017年公开回顾，不声称本轮阅读全文。'
  },
  'speech-macdonald-2017': {
    title: 'Hearing Lips and Seeing Voices: the Origins and Development of the “McGurk Effect” and Reflections on Audio–Visual Speech Perception Over the Last 40 Years',
    authors: 'John MacDonald', year: '2017', publication: 'Multisensory Research', doi: '10.1163/22134808-00002548',
    url: 'https://www.cmnh.org/files/resources/hearinglipsandseeingvoicestheoriginsanddev.pdf', access: 'fulltext',
    supports: '2026-10-10阅读作者回顾的摘要及第2—4节：一致／不一致视听材料、配音疑虑与闭眼／睁眼比较。明确属于发现者事后回顾；未转载图像，不据回忆报告原实验效果大小。'
  },
  'speech-language-2025': {
    title: 'Shared and language-specific phonological processing in the human temporal lobe',
    authors: 'Ilina Bhaya-Grossman; Matthew K. Leonard; Yizhen Zhang; Laura Gwilliams; Keith Johnson; Junfeng Lu; Edward F. Chang',
    year: '2026（2025-11-19在线）', publication: 'Nature, 649(8095), 140–151', doi: '10.1038/s41586-025-09748-8',
    url: 'https://pubmed.ncbi.nlm.nih.gov/41261133/', access: 'abstract',
    supports: '2026-10-10核对PubMed与Crossref发表日期，阅读原摘要、公开图注及出版页可见Discussion段。共享声学—语音响应与母语词边界、词频、音序统计及双语结果；未通读Methods，保守登记为摘要访问。临床采样与有限语言限制推广。'
  },
  'speech-motor-1985': {
    title: 'The motor theory of speech perception revised', authors: 'Alvin M. Liberman; Ignatius G. Mattingly', year: '1985',
    publication: 'Cognition, 21(1), 1–36', doi: '10.1016/0010-0277(85)90021-6',
    url: 'https://www.sciencedirect.com/science/article/pii/0010027785900216', access: 'abstract',
    supports: '2026-10-10阅读出版页及作者原文首页可见摘要：预期发音动作、专门加工的理论主张。把它标为候选解释与历史路线，不将理论假设写成当前共识。'
  },
  'speech-reduction-2021': {
    title: 'Does signal reduction imply predictive coding in models of spoken word recognition?',
    authors: 'Sahil Luthra; Monica Y. C. Li; Heejo You; Christian Brodbeck; James S. Magnuson', year: '2021',
    publication: 'Psychonomic Bulletin & Review, 28, 1381–1389', doi: '10.3758/s13423-021-01924-x',
    url: 'https://pubmed.ncbi.nlm.nih.gov/33852158/', access: 'abstract',
    supports: '2026-10-10阅读Europe PMC原始摘要及PubMed检索摘要：TRACE在未显式实现预测编码时也可出现符合预期输入下的某些响应下降。说明单一结果的模型可识别性限制，不否定预测编码全部证据。'
  },
};
