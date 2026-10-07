import type { Reference } from './references';

export const measurementSceneReferences: Record<string, Reference> = {
  "pure-tone-audiometry-asha": {
    "title": "Guidelines for Manual Pure-Tone Threshold Audiometry",
    "authors": "American Speech-Language-Hearing Association.",
    "year": "2005",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.asha.org/policy/GL2005-00014/",
    "access": "fulltext",
    "supports": "用于手动测听的刺激、阈值搜索、反应、记录与质量控制；与 BSA 的有限试次判据分别说明。"
  },
  "pure-tone-audiometry-iso8253": {
    "title": "ISO 8253-1:2010: Acoustics—Audiometric test methods—Part 1: Pure-tone air and bone conduction audiometry",
    "authors": "International Organization for Standardization.",
    "year": "2010",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.iso.org/standard/43601.html",
    "access": "documentation",
    "supports": "2026 年复审确认；未依据公开目录转录或声称满足全部标准条款。"
  },
  "pure-tone-audiometry-gb16296": {
    "title": "GB/T 16296.1-2018：声学 测听方法 第1部分：纯音气导和骨导测听法",
    "authors": "国家市场监督管理总局／国家标准化管理委员会.",
    "year": "2018",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=15FA516450541B002840E88B4863F4BA",
    "access": "documentation",
    "supports": "核对名称、采用标准及现行状态；不把目录信息当作全部规范内容。"
  },
  "pure-tone-audiometry-bsa": {
    "title": "Recommended procedure: Pure-tone air-conduction and bone-conduction threshold audiometry with and without masking",
    "authors": "British Society of Audiology.",
    "year": "2018",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.thebsa.org.uk/wp-content/uploads/2024/01/Recommended-Procedure-Pure-Tone-Audiometry-2018.pdf",
    "access": "fulltext",
    "supports": "用于行为程序、跨耳听见和平台方法；截至核查日 BSA 当前指南目录仍列该版本，2024 年征求修订意见不等于已发布新版。"
  },
  "pure-tone-audiometry-iso3891": {
    "title": "ISO 389-1:2017: Reference equivalent threshold sound pressure levels for pure tones and supra-aural earphones",
    "authors": "International Organization for Standardization.",
    "year": "2017",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.iso.org/standard/69855.html",
    "access": "documentation",
    "supports": "用于压耳式耳机参考零点；未转录参考值表格。"
  },
  "pure-tone-audiometry-iso3892": {
    "title": "ISO 389-2:1994: Reference equivalent threshold sound pressure levels for pure tones and insert earphones",
    "authors": "International Organization for Standardization.",
    "year": "1994",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.iso.org/standard/4378.html",
    "access": "documentation",
    "supports": "用于插入式耳机参考条件；不向非标准耳机转移参考值。"
  },
  "pure-tone-audiometry-iso3893": {
    "title": "ISO 389-3:2016: Reference equivalent threshold vibratory force levels for pure tones and bone vibrators",
    "authors": "International Organization for Standardization.",
    "year": "2016",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.iso.org/standard/59759.html",
    "access": "documentation",
    "supports": "用于骨导振动力参考框架；未引用未取得的数值表格。"
  },
  "pure-tone-audiometry-symbols": {
    "title": "Audiometric Symbols",
    "authors": "American Speech-Language-Hearing Association.",
    "year": "1990",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.asha.org/policy/GL1990-00006/",
    "access": "fulltext",
    "supports": "用于听力图坐标、耳别、气骨导、掩蔽与无反应符号。"
  },
  "pure-tone-audiometry-adult-assessment": {
    "title": "Hearing Loss in Adults",
    "authors": "American Speech-Language-Hearing Association.",
    "year": "检索于 2026-10-07",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.asha.org/practice-portal/clinical-topics/hearing-loss/",
    "access": "documentation",
    "supports": "用于气骨导及综合评价框架；网页核查日期为 2026-10-07。"
  },
  "pure-tone-audiometry-who": {
    "title": "World report on hearing",
    "authors": "World Health Organization.",
    "year": "2021",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.who.int/publications/i/item/9789240020481",
    "access": "documentation",
    "supports": "用于频率／耳别明确的平均指标与功能、交流及参与的评价框架。"
  },
  "pure-tone-audiometry-psychometric": {
    "title": "The psychometric function: I. Fitting, sampling, and goodness of fit",
    "authors": "Wichmann, F. A., & Hill, N. J.",
    "year": "2001",
    "publication": "Perception & Psychophysics, 63",
    "url": "https://doi.org/10.3758/BF03194544",
    "access": "fulltext",
    "supports": "用于概率模型、虚报／失误与拟合边界；不把通用拟合规则等同临床阈值程序。",
    "doi": "10.3758/BF03194544"
  },
  "pure-tone-audiometry-false-gap": {
    "title": "False air-bone gaps at 4 kHz in listeners with normal hearing and sensorineural hearing loss",
    "authors": "Margolis, R. H., Eikelboom, R. H., Johnson, C., Ginter, S. M., Swanepoel, D. W., & Moore, B. C. J.",
    "year": "2013",
    "publication": "International Journal of Audiology, 52",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23713469/",
    "access": "abstract",
    "supports": "用于孤立 4 kHz 差值的校准与测量解释，不作任意设备或个体的纠正公式。",
    "doi": "10.3109/14992027.2013.792437"
  },
  "pure-tone-audiometry-osha": {
    "title": "29 CFR 1910.95: Occupational noise exposure",
    "authors": "Occupational Safety and Health Administration.",
    "year": "检索于 2026-10-07",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.95",
    "access": "documentation",
    "supports": "仅用于说明特定职业监测指标的定义；不作为我国职业诊断规范。"
  },
  "pure-tone-audiometry-high-frequency": {
    "title": "Evaluation of a Fast Method to Measure High-Frequency Audiometry Based on Bayesian Learning",
    "authors": "Casolani, C., Borhan-Azad, A., Sørensen, R. S., Schlittenlacher, J., & Epp, B.",
    "year": "2024",
    "publication": "Trends in Hearing, 28",
    "url": "https://doi.org/10.1177/23312165231225545",
    "access": "fulltext",
    "supports": "用于 8–16 kHz 的方法比较与频率相关变异；不据扩展高频异常直接判断突触损伤。",
    "doi": "10.1177/23312165231225545"
  },
  "pure-tone-audiometry-swanepoel": {
    "title": "Smartphone hearing screening with integrated quality control and data management",
    "authors": "Swanepoel, D. W., Myburgh, H. C., Howe, D. M., Mahomed, F., & Eikelboom, R. H.",
    "year": "2014",
    "publication": "International Journal of Audiology",
    "url": "https://pubmed.ncbi.nlm.nih.gov/24998412/",
    "access": "abstract",
    "supports": "用于移动筛查的校准、环境监测和质量控制，限于被验证系统。",
    "doi": "10.3109/14992027.2014.920965"
  },
  "pure-tone-audiometry-guo": {
    "title": "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry",
    "authors": "Guo, Z., Yu, G., Zhou, H., Wang, X., Lu, Y., & Meng, Q.",
    "year": "2021",
    "publication": "Trends in Hearing, 25",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8606721/",
    "access": "fulltext",
    "supports": "用于电声／行为校准、反应时间和方法比较；不把特定耳机的验证推广至全部产品。",
    "doi": "10.1177/23312165211057367"
  },
  "pure-tone-audiometry-anc": {
    "title": "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control",
    "authors": "Zhou, H., Zhou, H., Guo, Z., & Meng, Q.",
    "year": "2024，在线发表",
    "publication": "International Journal of Audiology",
    "url": "https://doi.org/10.1080/14992027.2024.2428854",
    "access": "fulltext",
    "supports": "用于主动降噪、噪声条件和平均绝对差；验证样本与设备条件限定外推范围。",
    "doi": "10.1080/14992027.2024.2428854"
  },
  "pure-tone-audiometry-song": {
    "title": "Fast, Continuous Audiogram Estimation Using Machine Learning",
    "authors": "Song, X. D., Wallace, B. M., Gardner, J. R., Ledbetter, N. M., Weinberger, K. Q., & Barbour, D. L.",
    "year": "2015",
    "publication": "Ear and Hearing, 36",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4709018/",
    "access": "abstract",
    "supports": "用于连续估计路线与模型失配问题；不据有限阅读重建完整实验软件。",
    "doi": "10.1097/AUD.0000000000000186"
  },
  "pure-tone-audiometry-bal-paper": {
    "title": "Audiogram estimation using Bayesian active learning",
    "authors": "Schlittenlacher, J., Turner, R. E., & Moore, B. C. J.",
    "year": "2018",
    "publication": "The Journal of the Acoustical Society of America, 144",
    "url": "https://research.manchester.ac.uk/en/publications/audiogram-estimation-using-bayesian-active-learning/",
    "access": "abstract",
    "supports": "用于两类任务、连续估计和反应判据偏差；模型实现另核对仓库。",
    "doi": "10.1121/1.5047436"
  },
  "pure-tone-audiometry-bal-code": {
    "title": "BALaudiogram",
    "authors": "Cambridge Machine Learning Group.",
    "year": "检索于 2026-10-07",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://github.com/cambridge-mlg/BALaudiogram",
    "access": "documentation",
    "supports": "核对 MATLAB 实现、GPML 依赖、耳机校正和检查试次；不声称已运行完整听力测量系统。"
  },
  "pure-tone-audiometry-psignifit": {
    "title": "python-psignifit",
    "authors": "Wichmann Lab.",
    "year": "检索于 2026-10-07",
    "publication": "专业指南／标准／官方工具资料",
    "url": "https://github.com/wichmann-lab/python-psignifit",
    "access": "documentation",
    "supports": "用于心理测量函数分析工具入口；不替代设备校准与临床程序。"
  },
  "pure-tone-audiometry-auto-review": {
    "title": "Validity of automated threshold audiometry: a systematic review and meta-analysis",
    "authors": "Mahomed, F., Swanepoel, D. W., Eikelboom, R. H., & Soer, M.",
    "year": "2013",
    "publication": "Ear and Hearing, 34",
    "url": "https://pubmed.ncbi.nlm.nih.gov/24165302/",
    "access": "abstract",
    "supports": "用于自动方法验证证据的范围；属于综述，不计为单独临床实验。",
    "doi": "10.1097/01.aud.0000436255.53747.a4"
  },
  "pure-tone-audiometry-digital-review": {
    "title": "Digital Approaches to Automated and Machine Learning Assessments of Hearing: Scoping Review",
    "authors": "Wasmann, J. W., Pragt, L., Eikelboom, R., & Swanepoel, D. W.",
    "year": "2022",
    "publication": "Journal of Medical Internet Research, 24",
    "url": "https://www.jmir.org/2022/2/e32581/",
    "access": "fulltext",
    "supports": "用于自动化类型、使用环境与技术成熟度；正式出版年份为 2022，不使用检索索引中的 2021 年代替。",
    "doi": "10.2196/32581"
  },
  "pure-tone-audiometry-carhart": {
    "title": "Preferred Method For Clinical Determination Of Pure-Tone Thresholds",
    "authors": "Carhart, R., & Jerger, J. F.",
    "year": "1959",
    "publication": "Journal of Speech and Hearing Disorders, 24",
    "url": "https://doi.org/10.1044/jshd.2404.330",
    "access": "metadata",
    "supports": "仅用于方法史；当前操作细节依据可访问的专业指南。",
    "doi": "10.1044/jshd.2404.330"
  },
  "speech-reception-threshold-asha": {
    "title": "Determining Threshold Level for Speech",
    "authors": "American Speech-Language-Hearing Association",
    "year": "1988",
    "publication": "ASHA Guidelines",
    "url": "https://www.asha.org/policy/GL1988-00008/",
    "access": "fulltext",
    "supports": "SRT／SDT 名称、任务、传统临床流程、耳别及相互核对；不把历史指南中设备相关数值推广为任意换能器标准。"
  },
  "speech-reception-threshold-iso": {
    "title": "ISO 8253-3:2022: Acoustics—Audiometric test methods—Part 3: Speech audiometry",
    "authors": "International Organization for Standardization",
    "year": "2022",
    "publication": "ISO 8253-3:2022",
    "url": "https://www.iso.org/standard/74049.html",
    "access": "metadata",
    "supports": "材料验证、计分单位、言语声级及识别／检测定义；未取得全部付费正文，不声称符合全部条款。"
  },
  "speech-reception-threshold-gb": {
    "title": "GB/T 16296.3-2017：声学 测听方法 第3部分：言语测听",
    "authors": "国家质量监督检验检疫总局／国家标准化管理委员会",
    "year": "2017",
    "publication": "国家标准",
    "url": "https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=D2E8C47E28E5BA7271FBCFA30489B1AF",
    "access": "metadata",
    "supports": "核对标准名称与现行状态；未以目录推断全部测量步骤。"
  },
  "speech-reception-threshold-manual": {
    "title": "AA222 使用说明书（中文版）",
    "authors": "Interacoustics",
    "year": "2022",
    "publication": "厂商官方手册，D-0113176-F，2022/12",
    "url": "https://www.interacoustics.com/images/files/manuals/zh/D-0113176-F_2022_12_Instructions_for_use_AA222_ZH.pdf",
    "access": "metadata",
    "supports": "仅用于核对“言语接受阈”这一中文译法确有使用，不作为所有设备的操作依据。"
  },
  "speech-reception-threshold-adult": {
    "title": "Hearing Loss in Adults",
    "authors": "American Speech-Language-Hearing Association",
    "year": "网页资料",
    "publication": "ASHA Practice Portal",
    "url": "https://www.asha.org/practice-portal/clinical-topics/hearing-loss/",
    "access": "metadata",
    "supports": "综合评价、反应能力与言语测听指标；核查日期 2026-10-07。"
  },
  "speech-reception-threshold-zhu": {
    "title": "Development and validation of the Mandarin disyllable recognition test",
    "authors": "Zhu, M., Wang, X., & Fu, Q.-J.",
    "year": "2012",
    "publication": "Acta Otolaryngologica, 132(8), 855–861",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5847333/",
    "access": "fulltext",
    "supports": "普通话材料、声调与语音成分平衡、声码器条件下的词表检验；该文固定水平实验不是临床 SRT 常模。",
    "doi": "10.3109/00016489.2011.653668"
  },
  "speech-reception-threshold-hint": {
    "title": "Development of the Hearing In Noise Test for the measurement of speech reception thresholds in quiet and in noise",
    "authors": "Nilsson, M., Soli, S. D., & Sullivan, J. A.",
    "year": "1994",
    "publication": "The Journal of the Acoustical Society of America, 95(2), 1085–1099",
    "url": "https://pubmed.ncbi.nlm.nih.gov/8132902/",
    "access": "abstract",
    "supports": "句子材料、整体计分、校准与自适应测量路线；未把其列表误差当作所有测试精度。",
    "doi": "10.1121/1.408469"
  },
  "speech-reception-threshold-mhint": {
    "title": "Development of the Mandarin Hearing in Noise Test (MHINT)",
    "authors": "Wong, L. L. N., Soli, S. D., Liu, S., Han, N., & Huang, M.-W.",
    "year": "2007",
    "publication": "Ear and Hearing, 28(2 Suppl), 70S–74S",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17496652/",
    "access": "abstract",
    "supports": "两种普通话版本、安静／噪声条件、句子识别和空间呈现；不转用跨版本常模。",
    "doi": "10.1097/AUD.0b013e31803154d0"
  },
  "speech-reception-threshold-levitt": {
    "title": "Transformed Up-Down Methods in Psychoacoustics",
    "authors": "Levitt, H.",
    "year": "1971",
    "publication": "The Journal of the Acoustical Society of America, 49(2B), 467–477",
    "url": "https://pubmed.ncbi.nlm.nih.gov/5541744/",
    "access": "abstract",
    "supports": "特定升降规则与目标概率的经典方法入口；不把所有自适应算法视为同一规则。",
    "doi": "10.1121/1.1912375"
  },
  "speech-reception-threshold-atomic": {
    "title": "Sparse representation of speech using an atomic speech model",
    "authors": "Kong, F., Zhou, H., Zheng, N., & Meng, Q.",
    "year": "2025",
    "publication": "The Journal of the Acoustical Society of America, 157(3), 1899–1911",
    "url": "https://pubmed.ncbi.nlm.nih.gov/40106275/",
    "access": "abstract",
    "supports": "仅用于说明原子率阈值采用另一自变量与量纲，不与临床分贝数值互换。",
    "doi": "10.1121/10.0036144"
  },
  "speech-reception-threshold-wichmann": {
    "title": "The psychometric function: I. Fitting, sampling, and goodness of fit",
    "authors": "Wichmann, F. A., & Hill, N. J.",
    "year": "2001",
    "publication": "Perception & Psychophysics, 63, 1293–1313",
    "url": "https://courses.washington.edu/matlab1/pdf/Wichmann_Hill_2001a.pdf",
    "access": "fulltext",
    "supports": "模型渐近线、失误、拟合与采样；本文逻辑斯蒂反解由给定公式自行推导。",
    "doi": "10.3758/BF03194544"
  },
  "speech-reception-threshold-thornton": {
    "title": "Speech-Discrimination Scores Modeled as a Binomial Variable",
    "authors": "Thornton, A. R., & Raffin, M. J. M.",
    "year": "1978",
    "publication": "Journal of Speech and Hearing Research, 21(3), 507–518",
    "url": "https://pubs.asha.org/doi/abs/10.1044/jshr.2103.507",
    "access": "abstract",
    "supports": "词语识别分数的抽样变异；不把百分比区间直接转为自适应阈值的分贝区间。",
    "doi": "10.1044/jshr.2103.507"
  },
  "speech-reception-threshold-bilger": {
    "title": "Psychometric Equivalence of Recorded Spondaic Words as Test Items",
    "authors": "Bilger, R. C., Matthies, M. L., Meyer, T. A., & Griffiths, S. K.",
    "year": "1998",
    "publication": "Journal of Speech, Language, and Hearing Research, 41(3), 516–526",
    "url": "https://pubs.asha.org/doi/10.1044/jslhr.4103.516",
    "access": "abstract",
    "supports": "识别难度与斜率、词集大小和声学归一化的区别；不据摘要重建临床词表。",
    "doi": "10.1044/jslhr.4103.516"
  },
  "speech-reception-threshold-psignifit": {
    "title": "python-psignifit: Python implementation of psignifit, for psychometric function estimation",
    "authors": "Wichmann Lab",
    "year": "代码仓库",
    "publication": "作者公开代码与文档",
    "url": "https://github.com/wichmann-lab/python-psignifit",
    "access": "documentation",
    "supports": "拟合工具与阈值参数解释；未运行真实 SRT 评估系统。"
  },
  "speech-reception-threshold-nissen": {
    "title": "Psychometrically equivalent trisyllabic words for speech reception threshold testing in Mandarin",
    "authors": "Nissen, S. L., Harris, R. W., Jennings, L.-J., Eggett, D. L., & Buck, H.",
    "year": "2005",
    "publication": "International Journal of Audiology, 44(7), 391–399",
    "url": "https://pubmed.ncbi.nlm.nih.gov/16136789/",
    "access": "abstract",
    "supports": "普通话三音节词的函数测量、选择和水平调整；不宣称覆盖所有人群与地区。",
    "doi": "10.1080/14992020500147672"
  },
  "speech-reception-threshold-chen": {
    "title": "Development of the mandarin hearing in noise test for children",
    "authors": "Chen, Y., & Wong, L. L. N.",
    "year": "2020",
    "publication": "International Journal of Audiology, 59(9), 707–712",
    "url": "https://www.tandfonline.com/doi/full/10.1080/14992027.2020.1750717",
    "access": "fulltext",
    "supports": "儿童材料、词表及年龄相关参考；作者署名依出版方 PDF 的两位作者，检索库重复 Chen 项不照录。",
    "doi": "10.1080/14992027.2020.1750717"
  },
  "speech-reception-threshold-vermiglio": {
    "title": "The relationship between high-frequency pure-tone hearing loss, hearing in noise test (HINT) thresholds, and the articulation index",
    "authors": "Vermiglio, A. J., Soli, S. D., Freed, D. J., & Fisher, L. M.",
    "year": "2012",
    "publication": "Journal of the American Academy of Audiology, 23(10)",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23169195/",
    "access": "abstract",
    "supports": "该样本中纯音平均值与安静／稳态噪声识别的不同关系；不推断所有噪声任务均不受听力图影响。",
    "doi": "10.3766/jaaa.23.10.4"
  },
  "speech-reception-threshold-plomp": {
    "title": "A Signal-to-Noise Ratio Model for the Speech-Reception Threshold of the Hearing Impaired",
    "authors": "Plomp, R.",
    "year": "1986",
    "publication": "Journal of Speech and Hearing Research, 29(2), 146–154",
    "url": "https://pubmed.ncbi.nlm.nih.gov/3724108/",
    "access": "abstract",
    "supports": "安静阈值、额外信噪比及助听模型的功能区分；不把模型失真参数解释为单一病变。",
    "doi": "10.1044/jshr.2902.146"
  },
  "speech-reception-threshold-fade-paper": {
    "title": "A simulation framework for auditory discrimination experiments: Revealing the importance of across-frequency processing in speech perception",
    "authors": "Schädler, M. R., Warzybok, A., Ewert, S. D., & Kollmeier, B.",
    "year": "2016",
    "publication": "The Journal of the Acoustical Society of America, 139(5), 2708–2722",
    "url": "https://pubmed.ncbi.nlm.nih.gov/27250164/",
    "access": "abstract",
    "supports": "FADE、不同特征与稳态／调制噪声阈值预测；不将模型预测视为临床实测。",
    "doi": "10.1121/1.4948772"
  },
  "speech-reception-threshold-bsa": {
    "title": "Assessment of speech understanding in noise in adults with hearing difficulties",
    "authors": "British Society of Audiology",
    "year": "2019",
    "publication": "BSA Practice Guidance",
    "url": "https://www.thebsa.org.uk/wp-content/uploads/2023/10/OD104-80-BSA-Practice-Guidance-Speech-in-Noise-FINAL.Feb-2019.pdf",
    "access": "fulltext",
    "supports": "噪声测试、参考结果和信噪比损失、助听评价应用；不沿用旧文所列产品销售状态作为当前信息。"
  },
  "speech-reception-threshold-fade-code": {
    "title": "FADE: A Simulation Framework for Auditory Discrimination Experiments",
    "authors": "Schädler, M. R.",
    "year": "代码仓库",
    "publication": "作者代码与 README",
    "url": "https://github.com/m-r-s/fade",
    "access": "documentation",
    "supports": "输入标度、Linux／HTK 依赖、示例及语料授权要求；未安装执行第三方测量软件。"
  },
  "speech-reception-threshold-plomp-reliability": {
    "title": "Improving the reliability of testing the speech reception threshold for sentences",
    "authors": "Plomp, R., & Mimpen, A. M.",
    "year": "1979",
    "publication": "Audiology, 18(1), 43–52",
    "url": "https://pubmed.ncbi.nlm.nih.gov/760724/",
    "access": "abstract",
    "supports": "通过材料筛选建立可靠的句子阈值测试；本文不转用其误差为一般精度。",
    "doi": "10.3109/00206097909072618"
  },
  "speech-reception-threshold-smits": {
    "title": "Development and validation of an automatic speech-in-noise screening test by telephone",
    "authors": "Smits, C., Kapteyn, T. S., & Houtgast, T.",
    "year": "2004",
    "publication": "International Journal of Audiology",
    "url": "https://pubmed.ncbi.nlm.nih.gov/14974624/",
    "access": "abstract",
    "supports": "数字噪声电话筛查的开发与验证；参考值限于对应语言与版本。",
    "doi": "10.1080/14992020400050004"
  },
  "speech-reception-threshold-zin": {
    "title": "The Chinese Zodiac-in-Noise Test: An Internet-Based Speech-in-Noise Test for Large-Scale Hearing Screening",
    "authors": "Zhou, H., Meng, Q., Liu, X., Wu, P., Shang, S., Xiao, W., Kang, Y., Li, J., Wang, Y., & Zheng, N.",
    "year": "2024（在线 2023）",
    "publication": "Ear and Hearing, 45(2)",
    "url": "https://pubmed.ncbi.nlm.nih.gov/38062570/",
    "access": "abstract",
    "supports": "生肖三元组、噪声阈值和筛查验证；不把线上参与样本解释为总体患病率。",
    "doi": "10.1097/AUD.0000000000001441"
  },
  "speech-reception-threshold-aladdin": {
    "title": "Automatic development of speech-in-noise hearing tests using machine learning",
    "authors": "Polspoel, S., Moore, D. R., Swanepoel, D. W., Kramer, S. E., & Smits, C.",
    "year": "2025",
    "publication": "Scientific Reports, 15, 12878",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12000381/",
    "access": "fulltext",
    "supports": "合成数字、自动识别辅助材料调整与荷兰语／英语真人验证；不声称中文版本已验证。",
    "doi": "10.1038/s41598-025-96312-z"
  },
  "auditory-scene-analysis-bregman": {
    "title": "Auditory Scene Analysis: The Perceptual Organization of Sound.",
    "authors": "Bregman AS.",
    "year": "1990",
    "publication": "MIT Press",
    "url": "https://direct.mit.edu/books/monograph/3887/Auditory-Scene-AnalysisThe-Perceptual-Organization",
    "access": "abstract",
    "supports": "出版社书目信息及章节目录；用于理论框架，不声称逐章全文核查。",
    "doi": "10.7551/mitpress/1486.001.0001"
  },
  "auditory-scene-analysis-darwin": {
    "title": "Auditory grouping.",
    "authors": "Darwin CJ.",
    "year": "1997",
    "publication": "Trends in cognitive sciences",
    "url": "https://doi.org/10.1016/s1364-6613(97)01097-8",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1016/s1364-6613(97)01097-8"
  },
  "auditory-scene-analysis-objects": {
    "title": "What is an auditory object?",
    "authors": "Griffiths TD, Warren JD.",
    "year": "2004",
    "publication": "Nature Reviews Neuroscience",
    "url": "https://pubmed.ncbi.nlm.nih.gov/15496866/",
    "access": "abstract",
    "supports": "原始摘要及书目信息；概念定义与争议。",
    "doi": "10.1038/nrn1538"
  },
  "auditory-scene-analysis-texture": {
    "title": "Sound texture perception via statistics of the auditory periphery: evidence from sound synthesis.",
    "authors": "McDermott JH, Simoncelli EP.",
    "year": "2011",
    "publication": "Neuron",
    "url": "https://doi.org/10.1016/j.neuron.2011.06.032",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1016/j.neuron.2011.06.032"
  },
  "auditory-scene-analysis-mesgarani": {
    "title": "Selective cortical representation of attended speaker in multi-talker speech perception.",
    "authors": "Mesgarani N, Chang EF.",
    "year": "2012",
    "publication": "Nature",
    "url": "https://doi.org/10.1038/nature11020",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1038/nature11020"
  },
  "auditory-scene-analysis-cusimano": {
    "title": "Listening with generative models.",
    "authors": "Cusimano M, Hewitt LB, McDermott JH.",
    "year": "2024",
    "publication": "Cognition",
    "url": "https://doi.org/10.1016/j.cognition.2024.105874",
    "access": "abstract",
    "supports": "原始摘要、作者论文及项目资料：生成模型、错觉与自然混合声音；未引用量化性能。",
    "doi": "10.1016/j.cognition.2024.105874"
  },
  "auditory-scene-analysis-coherence": {
    "title": "Temporal coherence in the perceptual organization and cortical representation of auditory scenes.",
    "authors": "Elhilali M, Ma L, Micheyl C, Oxenham AJ, Shamma SA.",
    "year": "2009",
    "publication": "Neuron",
    "url": "https://doi.org/10.1016/j.neuron.2008.12.005",
    "access": "abstract",
    "supports": "核查原始摘要：同步与交替条件的人类知觉、雪貂皮层响应及模型结论；全文接口未取得。",
    "doi": "10.1016/j.neuron.2008.12.005"
  },
  "auditory-scene-analysis-bizley": {
    "title": "The what, where and how of auditory-object perception.",
    "authors": "Bizley JK, Cohen YE.",
    "year": "2013",
    "publication": "Nature Reviews Neuroscience",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4082027/",
    "access": "abstract",
    "supports": "开放正文相关段及原始摘要：对象、身份和知觉层次。",
    "doi": "10.1038/nrn3565"
  },
  "auditory-scene-analysis-attention": {
    "title": "Effects of attention and unilateral neglect on auditory stream segregation.",
    "authors": "Carlyon RP, Cusack R, Foxton JM, Robertson IH.",
    "year": "2001",
    "publication": "Journal of experimental psychology. Human perception and performance",
    "url": "https://doi.org/10.1037//0096-1523.27.1.115",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1037//0096-1523.27.1.115"
  },
  "auditory-scene-analysis-onset": {
    "title": "Grouping Frequency Components of Vowels: When is a Harmonic not a Harmonic?",
    "authors": "Darwin CJ, Sutherland NS.",
    "year": "1984",
    "publication": "Quarterly Journal of Experimental Psychology A",
    "url": "https://journals.sagepub.com/doi/10.1080/14640748408402155",
    "access": "abstract",
    "supports": "出版社原始摘要：元音谐波起止时间、分组与适应控制。",
    "doi": "10.1080/14640748408402155"
  },
  "auditory-scene-analysis-streamproperties": {
    "title": "Properties of auditory stream formation.",
    "authors": "Moore BCJ, Gockel HE.",
    "year": "2012",
    "publication": "Philosophical Transactions of the Royal Society B",
    "url": "https://pubmed.ncbi.nlm.nih.gov/22371614/",
    "access": "abstract",
    "supports": "核查摘要及图注：频率、时序、非频谱线索与双稳态；不引用具体普遍阈值。",
    "doi": "10.1098/rstb.2011.0355"
  },
  "auditory-scene-analysis-prediction": {
    "title": "Predictability effects in auditory scene analysis: a review.",
    "authors": "Bendixen A.",
    "year": "2014",
    "publication": "Frontiers in neuroscience",
    "url": "https://doi.org/10.3389/fnins.2014.00060",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.3389/fnins.2014.00060"
  },
  "auditory-scene-analysis-oxenham": {
    "title": "Pitch perception and auditory stream segregation: implications for hearing loss and cochlear implants.",
    "authors": "Oxenham AJ.",
    "year": "2008",
    "publication": "Trends in amplification",
    "url": "https://doi.org/10.1177/1084713808325881",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1177/1084713808325881"
  },
  "auditory-scene-analysis-broadband": {
    "title": "Broadband Auditory Stream Segregation by Hearing-Impaired and Normal-Hearing Listeners.",
    "authors": "Valentine S, Lentz JJ.",
    "year": "2008",
    "publication": "Journal of Speech, Language, and Hearing Research",
    "url": "https://pubs.asha.org/doi/10.1044/1092-4388%282008/07-0193%29",
    "access": "abstract",
    "supports": "出版社原始摘要及作者信息：宽带非谐波刺激下组间未见显著差异，不能外推所有任务。",
    "doi": "10.1044/1092-4388(2008/07-0193)"
  },
  "auditory-scene-analysis-shamma": {
    "title": "Temporal coherence and attention in auditory scene analysis.",
    "authors": "Shamma SA, Elhilali M, Micheyl C.",
    "year": "2011",
    "publication": "Trends in neurosciences",
    "url": "https://doi.org/10.1016/j.tins.2010.11.002",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1016/j.tins.2010.11.002"
  },
  "auditory-scene-analysis-precedence": {
    "title": "The precedence effect.",
    "authors": "Litovsky RY, Colburn HS, Yost WA, Guzman SJ.",
    "year": "1999",
    "publication": "Journal of the Acoustical Society of America",
    "url": "https://pubmed.ncbi.nlm.nih.gov/10530009/",
    "access": "abstract",
    "supports": "原始摘要：直达声与反射声的知觉和定位关系。",
    "doi": "10.1121/1.427914"
  },
  "auditory-scene-analysis-automatic": {
    "title": "Automaticity and primacy of auditory streaming: Concurrent subjective and objective measures.",
    "authors": "Billig AJ, Carlyon RP.",
    "year": "2016",
    "publication": "Journal of experimental psychology. Human perception and performance",
    "url": "https://doi.org/10.1037/xhp0000146",
    "access": "fulltext",
    "supports": "已核查开放全文及摘要：主观与行为测量、自动组织和注意效应。",
    "doi": "10.1037/xhp0000146"
  },
  "auditory-scene-analysis-initial": {
    "title": "The initial phase of auditory and visual scene analysis.",
    "authors": "Hupé JM, Pressnitzer D.",
    "year": "2012",
    "publication": "Philosophical transactions of the Royal Society of London. Series B, Biological sciences",
    "url": "https://doi.org/10.1098/rstb.2011.0368",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1098/rstb.2011.0368"
  },
  "auditory-scene-analysis-bistable": {
    "title": "Temporal dynamics of auditory and visual bistability reveal common principles of perceptual organization.",
    "authors": "Pressnitzer D, Hupé JM.",
    "year": "2006",
    "publication": "Current biology : CB",
    "url": "https://doi.org/10.1016/j.cub.2006.05.054",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1016/j.cub.2006.05.054"
  },
  "auditory-scene-analysis-models": {
    "title": "Computational Models of Auditory Scene Analysis: A Review.",
    "authors": "Szabó BT, Denham SL, Winkler I.",
    "year": "2016",
    "publication": "Frontiers in neuroscience",
    "url": "https://doi.org/10.3389/fnins.2016.00524",
    "access": "fulltext",
    "supports": "已核查开放全文：模型分类、解释范围与互补关系。",
    "doi": "10.3389/fnins.2016.00524"
  },
  "auditory-scene-analysis-teki": {
    "title": "Segregation of complex acoustic scenes based on temporal coherence.",
    "authors": "Teki S, Chait M, Kumar S, Shamma S, Griffiths TD.",
    "year": "2013",
    "publication": "eLife",
    "url": "https://doi.org/10.7554/elife.00699",
    "access": "fulltext",
    "supports": "已核查开放全文及摘要：随机图形—背景任务和时域相干模型。",
    "doi": "10.7554/elife.00699"
  },
  "auditory-scene-analysis-continuity": {
    "title": "The continuity illusion adapts to the auditory scene.",
    "authors": "Riecke L, Mendelsohn D, Schreiner C, Formisano E.",
    "year": "2009",
    "publication": "Hearing research",
    "url": "https://doi.org/10.1016/j.heares.2008.10.006",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1016/j.heares.2008.10.006"
  },
  "auditory-scene-analysis-global": {
    "title": "Global not local masker features govern the auditory continuity illusion.",
    "authors": "Riecke L, Micheyl C, Oxenham AJ.",
    "year": "2012",
    "publication": "The Journal of neuroscience : the official journal of the Society for Neuroscience",
    "url": "https://doi.org/10.1523/jneurosci.6261-11.2012",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1523/jneurosci.6261-11.2012"
  },
  "auditory-scene-analysis-mcwalter": {
    "title": "Adaptive and Selective Time Averaging of Auditory Scenes.",
    "authors": "McWalter R, McDermott JH.",
    "year": "2018",
    "publication": "Current Biology",
    "url": "https://pubmed.ncbi.nlm.nih.gov/29681472/",
    "access": "abstract",
    "supports": "原始摘要与作者项目资料：纹理整合时间及选择性。",
    "doi": "10.1016/j.cub.2018.03.049"
  },
  "auditory-scene-analysis-chatterjee": {
    "title": "Auditory stream segregation with cochlear implants: A preliminary report.",
    "authors": "Chatterjee M, Sarampalis A, Oba SI.",
    "year": "2006",
    "publication": "Hearing research",
    "url": "https://doi.org/10.1016/j.heares.2006.09.001",
    "access": "abstract",
    "supports": "原始摘要与 PubMed 图注：直接电刺激初步研究；个体差异，不作全体使用者结论。",
    "doi": "10.1016/j.heares.2006.09.001"
  },
  "auditory-scene-analysis-figurebrain": {
    "title": "Brain bases for auditory stimulus-driven figure-ground segregation.",
    "authors": "Teki S, Chait M, Kumar S, von Kriegstein K, Griffiths TD.",
    "year": "2011",
    "publication": "The Journal of neuroscience : the official journal of the Society for Neuroscience",
    "url": "https://doi.org/10.1523/jneurosci.3788-10.2011",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1523/jneurosci.3788-10.2011"
  },
  "auditory-scene-analysis-ding": {
    "title": "Emergence of neural encoding of auditory objects while listening to competing speakers.",
    "authors": "Ding N, Simon JZ.",
    "year": "2012",
    "publication": "Proceedings of the National Academy of Sciences of the United States of America",
    "url": "https://doi.org/10.1073/pnas.1205381109",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1073/pnas.1205381109"
  },
  "auditory-scene-analysis-crossmodal": {
    "title": "Cross-modal and non-sensory influences on auditory streaming.",
    "authors": "Carlyon RP, Plack CJ, Fantini DA, Cusack R.",
    "year": "2003",
    "publication": "Perception",
    "url": "https://doi.org/10.1068/p5035",
    "access": "abstract",
    "supports": "核查原始摘要及书目信息；未引用未核查的样本量或数值结果。",
    "doi": "10.1068/p5035"
  },
  "auditory-scene-analysis-neural2026": {
    "title": "Real-time brain-controlled selective hearing enhances speech perception in multi-talker environments.",
    "authors": "Choudhari V, Nentwich M, Johnson S, Herrero JL, Bickel S, Mehta AD, Friedman D, Flinker A, Chang EF, Mesgarani N.",
    "year": "2026",
    "publication": "Nature neuroscience",
    "url": "https://doi.org/10.1038/s41593-026-02281-5",
    "access": "abstract",
    "supports": "已核查出版社摘要及结果、方法段：四人颅内闭环；另一个群体评价输出音频。",
    "doi": "10.1038/s41593-026-02281-5"
  },
  "auditory-scene-analysis-amt": {
    "title": "The Auditory Modeling Toolbox: official documentation.",
    "authors": "Auditory Modeling Toolbox contributors.",
    "year": "检索于 2026-10-07",
    "publication": "软件文档",
    "url": "https://amtoolbox.org/doc.php",
    "access": "metadata",
    "supports": "官方文档入口；未执行工具箱或宣称完整场景模型可用。"
  },
  "auditory-scene-analysis-bass": {
    "title": "Bayesian auditory scene synthesis: code repository.",
    "authors": "Cusimano M and collaborators.",
    "year": "检索于 2026-10-07",
    "publication": "研究代码",
    "url": "https://github.com/mcusi/bass",
    "access": "metadata",
    "supports": "核查 README：参考代码，作者明确说明不是完整可执行软件包。"
  },
  "auditory-scene-analysis-sts": {
    "title": "STSstep: Sound Texture Synthesis with texture morphs and steps.",
    "authors": "McWalter R.",
    "year": "检索于 2026-10-07",
    "publication": "研究代码",
    "url": "https://github.com/rmcwalter/STSstep",
    "access": "metadata",
    "supports": "核查官方 README：MATLAB 文件、minFunc 和 LTFAT 依赖；未运行纹理合成。"
  },
  "auditory-scene-analysis-asteroid": {
    "title": "Asteroid: audio source separation toolkit.",
    "authors": "Asteroid contributors.",
    "year": "检索于 2026-10-07",
    "publication": "研究软件",
    "url": "https://github.com/asteroid-team/asteroid",
    "access": "metadata",
    "supports": "核查官方 README：PyTorch、数据集配方及额外依赖；未运行分离模型。"
  }
};
