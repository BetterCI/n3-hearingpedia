import type { Reference } from './references.ts';

// Source records and reading scope: docs/research/core-eight.
export const coreEightReferences: Record<string, Reference> = {
  "freyman-1999": {
    "title": "The role of perceived spatial separation in the unmasking of speech",
    "authors": "Freyman RL, Helfer KS, McCall DD, Clifton RK.",
    "year": "1999",
    "publication": "The Journal of the Acoustical Society of America, 106(6), 3578-3588",
    "doi": "10.1121/1.428211",
    "url": "https://pubmed.ncbi.nlm.nih.gov/10615698/",
    "access": "abstract",
    "supports": "用优先效应区分感知分离与声学双耳收益；噪声和竞争言语结果分别解释。"
  },
  "hall-cmr-1984": {
    "title": "Detection in noise by spectro-temporal pattern analysis",
    "authors": "Hall JW, Haggard MP, Fernandes MA.",
    "year": "1984",
    "publication": "The Journal of the Acoustical Society of America, 76(1), 50-56",
    "doi": "10.1121/1.391005",
    "url": "https://pubmed.ncbi.nlm.nih.gov/6747111/",
    "access": "abstract",
    "supports": "跨频带包络一致性与共同调制去掩蔽的经典原始实验。"
  },
  "amt-dau1997": {
    "title": "dau1997: Linear filtering for monaural masking (improved)",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/dau1997.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对听觉分频、包络、适应和调制滤波器组及内部表征输出，未运行实现。对应Dau、Kollmeier与Kohlrausch于1997年发表的幅度调制检测、掩蔽及整合模型。"
  },
  "amt-breebaart2001": {
    "title": "breebaart2001: Binaural masking level differences",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/breebaart2001.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对左右输入、外周处理、兴奋—抑制表示及返回值，未运行实现。"
  },
  "moore-recruitment-2004": {
    "title": "A revised model of loudness perception applied to cochlear hearing loss",
    "authors": "Moore BC, Glasberg BR.",
    "year": "2004",
    "publication": "Hearing research, 188(1-2), 70-88",
    "doi": "10.1016/s0378-5955(03)00347-2",
    "url": "https://pubmed.ncbi.nlm.nih.gov/14759572/",
    "access": "abstract",
    "supports": "正常和耳蜗性听力损失的响度模型，特别核对阈值附近斜率、重振和双耳关系。"
  },
  "iso-226-2023": {
    "title": "ISO 226:2023 — Acoustics — Normal equal-loudness-level contours",
    "authors": "International Organization for Standardization",
    "year": "2023",
    "publication": "ISO",
    "url": "https://www.iso.org/standard/83117.html",
    "access": "documentation",
    "supports": "核对官方范围及公开预览印刷页2—4的公式（1）、条件和表1；未读取付费完整标准。"
  },
  "iso226-revision-2024": {
    "title": "Revision of ISO 226 “Normal Equal-Loudness-Level Contours” from 2003 to 2023 edition: The background and results",
    "authors": "Suzuki, Y.; Takeshima, H.; Kurakata, K.",
    "year": "2024",
    "publication": "Acoustical Science and Technology, 45(1), 1–8",
    "url": "https://doi.org/10.1250/ast.e23.66",
    "access": "fulltext",
    "supports": "公开全文选读第2—3节；绘图公式按标准预览核对。"
  },
  "brand-2002": {
    "title": "An adaptive procedure for categorical loudness scaling",
    "authors": "Brand T, Hohmann V.",
    "year": "2002",
    "publication": "The Journal of the Acoustical Society of America, 112(4), 1597-1604",
    "doi": "10.1121/1.1502902",
    "url": "https://pubmed.ncbi.nlm.nih.gov/12398465/",
    "access": "abstract",
    "supports": "自适应类别响度标定；正常听力与感音神经性听力损失各10人的方法评价。"
  },
  "iso-532-3": {
    "title": "ISO 532-3:2023 — Acoustics — Methods for calculating loudness — Part 3: Moore-Glasberg-Schlittenlacher method",
    "authors": "International Organization for Standardization",
    "year": "2023",
    "publication": "ISO",
    "url": "https://www.iso.org/standard/69856.html",
    "access": "documentation",
    "supports": "核对官方公开范围和版本；未读取付费标准全文，也未验证软件的标准符合性。"
  },
  "mosqito-model": {
    "title": "Loudness calculation implementations",
    "authors": "MoSQITo",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://mosqito.readthedocs.io/en/latest/source/reference/mosqito.sq_metrics.loudness.loudness_zwtv.loudness_zwtv.html",
    "access": "documentation",
    "supports": "项目官方文档与仓库说明；核对ISO 532-1方法、声压单位、声场选择与总响度／比响度返回值。未运行实现或独立验证全部测试信号。"
  },
  "amt-moore2016": {
    "title": "moore2016: Binaural loudness model",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/moore2016.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对帕单位、32千赫兹采样、短时与长时输出及2018年时间常数修订；保留文档对实现尚未完整的说明，未进行标准符合性验证。"
  },
  "iso-532-1": {
    "title": "ISO 532-1:2017 — Acoustics — Methods for calculating loudness — Part 1: Zwicker method",
    "authors": "International Organization for Standardization",
    "year": "2017",
    "publication": "ISO",
    "url": "https://www.iso.org/standard/63077.html",
    "access": "documentation",
    "supports": "核对官方公开范围和版本；未读取付费标准全文，也未验证软件的标准符合性。"
  },
  "iso-532-2": {
    "title": "ISO 532-2:2017 — Acoustics — Methods for calculating loudness — Part 2: Moore-Glasberg method",
    "authors": "International Organization for Standardization",
    "year": "2017",
    "publication": "ISO",
    "url": "https://www.iso.org/standard/63078.html",
    "access": "documentation",
    "supports": "核对官方公开范围和版本；未读取付费标准全文，也未验证软件的标准符合性。"
  },
  "middlebrooks-1991": {
    "title": "Sound localization by human listeners",
    "authors": "Middlebrooks JC, Green DM.",
    "year": "1991",
    "publication": "Annual review of psychology, 42, 135-159",
    "doi": "10.1146/annurev.ps.42.020191.001031",
    "url": "https://pubmed.ncbi.nlm.nih.gov/2018391/",
    "access": "abstract",
    "supports": "历史综述支持方向线索的基本框架；不沿用其中关于运动加工等问题的历史结论作为现今定论。"
  },
  "distance-2016": {
    "title": "Auditory distance perception in humans: a review of cues, development, neuronal bases, and effects of sensory loss",
    "authors": "Kolarik AJ, Moore BC, Zahorik P, Cirstea S, Pardhan S.",
    "year": "2016",
    "publication": "Attention, perception & psychophysics, 78(2), 373-395",
    "doi": "10.3758/s13414-015-1015-1",
    "url": "https://pubmed.ncbi.nlm.nih.gov/26590050/",
    "access": "abstract",
    "supports": "距离知觉综述；区分声级、混响、频谱及经验，不把声级直接换算距离。"
  },
  "hofman-1998": {
    "title": "Relearning sound localization with new ears",
    "authors": "Hofman PM, Van Riswick JG, Van Opstal AJ.",
    "year": "1998",
    "publication": "Nature neuroscience, 1(5), 417-421",
    "doi": "10.1038/1633",
    "url": "https://pubmed.ncbi.nlm.nih.gov/10196533/",
    "access": "abstract",
    "supports": "耳廓模具改变频谱线索后的定位再学习；不推断任意虚拟声场均能立即适应。"
  },
  "litovsky-precedence-2001": {
    "title": "Investigation of the relationship among three common measures of precedence: Fusion, localization dominance, and discrimination suppression",
    "authors": "Litovsky, R. Y., & Shinn-Cunningham, B. G.",
    "year": "2001",
    "publication": "The Journal of the Acoustical Society of America, 109(1), 346–358.",
    "doi": "10.1121/1.1328792",
    "url": "https://www.cmu.edu/dietrich/psychology/shinn/publications/pdfs/2001/2001jasa_litovsky.pdf",
    "access": "fulltext",
    "supports": "原始研究；公开全文选读摘要、引言与测量定义，核对三类指标及其可分离性。"
  },
  "pastore-precedence-2019": {
    "title": "The impact of peripheral mechanisms on the precedence effect",
    "authors": "Pastore, M. T., & Braasch, J.",
    "year": "2019",
    "publication": "The Journal of the Acoustical Society of America, 146(1), 425.",
    "doi": "10.1121/1.5116680",
    "url": "https://pubmed.ncbi.nlm.nih.gov/31370612/",
    "access": "abstract",
    "supports": "原始研究；摘要与书目核对。PMC全文页面返回验证提示，未将其记作本轮全文阅读。用于刺激持续时间、起始结构及相对声级的解释。"
  },
  "tolnai-precedence-2014": {
    "title": "The precedence effect and its buildup and breakdown in ferrets and humans",
    "authors": "Tolnai, S., Litovsky, R. Y., & King, A. J.",
    "year": "2014",
    "publication": "The Journal of the Acoustical Society of America",
    "doi": "10.1121/1.4864486",
    "url": "https://pubmed.ncbi.nlm.nih.gov/24606278/",
    "access": "abstract",
    "supports": "原始研究；Europe PMC摘要与书目核对。用于刺激历史与先后方向关系改变的影响，不据此指定唯一神经机制。"
  },
  "brown-precedence-2013": {
    "title": "The precedence effect: Fusion and lateralization measures for headphone stimuli lateralized by interaural time and level differences",
    "authors": "Brown, A. D., & Stecker, G. C.",
    "year": "2013",
    "publication": "The Journal of the Acoustical Society of America, 133(5), 2883–2898.",
    "doi": "10.1121/1.4796113",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23654394/",
    "access": "abstract",
    "supports": "原始研究；Europe PMC正式摘要与书目核对，未通读全文。用于重复序列下融合与定位主导的分离及耳间线索依赖。"
  },
  "xia-precedence-2010": {
    "title": "Physiological and Psychophysical Modeling of the Precedence Effect",
    "authors": "Xia, J., Brughera, A., Colburn, H. S., & Shinn-Cunningham, B.",
    "year": "2010",
    "publication": "Journal of the Association for Research in Otolaryngology, 11, 495–513.",
    "doi": "10.1007/s10162-010-0212-9",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2914243/",
    "access": "fulltext",
    "supports": "原始建模研究；公开全文选读模型框架与预测范围。未确认作者独立维护的公开代码，未运行模型。"
  },
  "amt-lindemann1986": {
    "title": "lindemann1986: Binaural activity map based on cross-correlation",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/lindemann1986.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对互相关、对侧抑制与活动图输出。文档区分原始Lindemann模型与后续时间变化实现，并列出1986年两篇原始论文；未运行实现。"
  },
  "amt-baumgartner2014": {
    "title": "baumgartner2014: Localization in sagittal planes",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/baumgartner2014.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对目标、模板、方向响应概率和数据依赖；文档列出Baumgartner、Majdak与Laback的2014年原始论文，未运行实现。"
  },
  "how-vocode-2024": {
    "title": "How to vocode: Using channel vocoders for cochlear-implant research",
    "authors": "Cychosz M, Winn MB, Goupell MJ.",
    "year": "2024",
    "publication": "The Journal of the Acoustical Society of America, 155(4), 2407-2437",
    "doi": "10.1121/10.0025274",
    "url": "https://pubmed.ncbi.nlm.nih.gov/38568143/",
    "access": "abstract",
    "supports": "核对正式发表摘要、公开目录与作者代码说明；PMC全文XML获取失败，机构库下载未获得有效PDF，未声称本轮通读全文。用于方法框架；信号处理公式为教学概括。"
  },
  "kopsch-2025": {
    "title": "Acoustic simulation of cochlear implant sound to approximate the perceptual experience of electric hearing",
    "authors": "Kopsch AC, Plontke SK, Rahne T.",
    "year": "2025",
    "publication": "Scientific reports, 15(1), 38997",
    "doi": "10.1038/s41598-025-25711-z",
    "url": "https://europepmc.org/articles/PMC12595112",
    "access": "fulltext",
    "supports": "2026-10-09 已通过 Europe PMC 阅读原文的参与者、声级与呈现、优化流程、跨句比较及限制。15 位德语语后聋成人 SSD-CI；原句均值与标准差 9.7±0.5，新句 8.4±1.5、8.9±1.3，属同一批听者。仅支持同说话人的材料泛化，年龄相关对侧耳听力判据、选择条件及主观评分限制推广。"
  },
  "listenlab-repository": {
    "title": "Praat Vocoder",
    "authors": "Winn, M. B. / ListenLab",
    "year": "访问日期 2026-10-05",
    "publication": "作者代码及说明",
    "url": "https://github.com/ListenLab/Vocoder",
    "access": "documentation",
    "supports": "已阅读作者README的载波、分析与合成、通道交互和参数说明；未执行软件或独立验证全部功能。"
  },
  "nidcd-sudden": {
    "title": "Sudden Deafness",
    "authors": "National Institute on Deafness and Other Communication Disorders",
    "year": "访问日期 2026-10-05",
    "publication": "NIDCD",
    "url": "https://www.nidcd.nih.gov/health/sudden-deafness",
    "access": "documentation",
    "supports": "官方患者教育资料；仅支持突然听力下降需及时医疗评估，未提供个体用药建议。"
  },
  "skoe-2010": {
    "title": "Auditory brain stem response to complex sounds: a tutorial",
    "authors": "Skoe E, Kraus N.",
    "year": "2010",
    "publication": "Ear and hearing, 31(3), 302-324",
    "doi": "10.1097/aud.0b013e3181cdb272",
    "url": "https://pubmed.ncbi.nlm.nih.gov/20084007/",
    "access": "abstract",
    "supports": "复杂声音诱发反应的方法教程；来源解释同时采用2019年多来源证据更新。"
  },
  "achieve-2023": {
    "title": "Hearing intervention versus health education control to reduce cognitive decline in older adults with hearing loss in the USA (ACHIEVE): a multicentre, randomised controlled trial",
    "authors": "Lin FR, Pike JR, Albert MS, Arnold M, Burgard S, Chisolm T, Couper D, Deal JA, Goman AM, Glynn NW, Gmelin T, Gravens-Mueller L, Hayden KM, Huang AR, Knopman D, Mitchell CM, Mosley T, Pankow JS, Reed NS, Sanchez V, Schrack JA, Windham BG, Coresh J, ACHIEVE Collaborative Research Group.",
    "year": "2023",
    "publication": "Lancet (London, England), 402(10404), 786-797",
    "doi": "10.1016/s0140-6736(23)01406-x",
    "url": "https://pubmed.ncbi.nlm.nih.gov/37478886/",
    "access": "abstract",
    "supports": "随机试验主要认知结局整体未显著改善，预先规定的不同招募人群分析与主要结果分开陈述。"
  },
  "achieve-communication-2024": {
    "title": "Effect of hearing intervention on communicative function: A secondary analysis of the ACHIEVE randomized controlled trial",
    "authors": "Sanchez VA, Arnold ML, Garcia Morales EE, Reed NS, Faucette S, Burgard S, Calloway HN, Coresh J, Deal JA, Goman AM, Gravens-Mueller L, Hayden KM, Huang AR, Mitchell CM, Mosley TH, Pankow JS, Pike JR, Schrack JA, Sherry L, Weycker JM, Lin FR, Chisolm TH, ACHIEVE Collaborative Study.",
    "year": "2024",
    "publication": "Journal of the American Geriatrics Society, 72(12), 3784-3799",
    "doi": "10.1111/jgs.19185",
    "url": "https://pubmed.ncbi.nlm.nih.gov/39266468/",
    "access": "abstract",
    "supports": "同一随机试验的次级自评交流结局；半年改善并维持至三年，不替代主要认知结局。"
  },
  "amt-zilany2014": {
    "title": "zilany2014: Auditory-nerve model",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/zilany2014.php",
    "access": "documentation",
    "supports": "AMT 1.6.0文档；核对毛细胞功能、自发放电率及物种选项和响应输出。原始模型：Zilany、Bruce与Carney，Updated parameters and expanded simulation options for a model of the auditory periphery，JASA 135，283–286（2014）；未运行实现。"
  },
  "verhulst-model-2018": {
    "title": "Computational modeling of the human auditory periphery: Auditory-nerve responses, evoked potentials and hearing loss",
    "authors": "Verhulst, S., Altoè, A., & Vasilkov, V.",
    "year": "2018",
    "publication": "Hearing Research, 360, 55–75.",
    "doi": "10.1016/j.heares.2017.12.018",
    "url": "https://backoffice.biblio.ugent.be/download/8575023/8575061",
    "access": "fulltext",
    "supports": "原始建模研究；核对摘要、公开全文模型范围及作者实现说明，不将整体模型当作完整皮层诱发电位模型。"
  },
  "verhulst-code": {
    "title": "Verhulstetal2018Model",
    "authors": "HearingTechnology",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://github.com/HearingTechnology/Verhulstetal2018Model",
    "access": "documentation",
    "supports": "作者README与版本说明；核对1.2版脑干阶段和缩放更新、听损配置及示例入口。遵循仓库UGent学术许可，未运行第三方代码。"
  },
  "oxenham-pitch-2012": {
    "title": "Pitch perception",
    "authors": "Oxenham AJ.",
    "year": "2012",
    "publication": "The Journal of neuroscience : the official journal of the Society for Neuroscience, 32(39), 13335-13338",
    "doi": "10.1523/jneurosci.3815-12.2012",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23015422/",
    "access": "abstract",
    "supports": "周期性与音高关系、可分辨谐波及知觉组织；区分物理基频和感知音高。"
  },
  "xu-1997": {
    "title": "Contextual tonal variations in Mandarin",
    "authors": "Xu, Y.",
    "year": "1997",
    "publication": "Journal of Phonetics, 25(1), 61–83",
    "doi": "10.1006/jpho.1996.0034",
    "url": "https://www.sciencedirect.com/science/article/abs/pii/S0095447096900340",
    "access": "abstract",
    "supports": "核对出版商原始摘要与书目；相邻声调的延续和预期效应，支持语境依赖的基频轨迹。"
  },
  "librosa-libri1": {
    "title": "LibriSpeech 5703-47212-0000 / librosa libri1",
    "authors": "LibriSpeech / librosa; Garth Comira (reader)",
    "year": "访问日期 2026-10-06",
    "publication": "Example audio",
    "url": "https://librosa.org/doc/latest/recordings.html",
    "access": "documentation",
    "supports": "官方示例与许可证已核对，实际文件已分析；CC BY 4.0。"
  },
  "praat-pitch-ac": {
    "title": "Sound: To Pitch (raw autocorrelation); Sound.to_pitch_ac",
    "authors": "Praat / Parselmouth",
    "year": "访问日期 2026-10-06",
    "publication": "Official documentation",
    "url": "https://parselmouth.readthedocs.io/en/stable/api_reference.html#parselmouth.Sound.to_pitch_ac",
    "access": "documentation",
    "supports": "核对方法与接口说明；实际计算版本和参数见图件来源记录。"
  },
  "camacho-2008": {
    "title": "A sawtooth waveform inspired pitch estimator for speech and music",
    "authors": "Camacho A, Harris JG.",
    "year": "2008",
    "publication": "The Journal of the Acoustical Society of America, 124(3), 1638-1652",
    "doi": "10.1121/1.2951592",
    "url": "https://pubmed.ncbi.nlm.nih.gov/19045655/",
    "access": "abstract",
    "supports": "SWIPE及其变体的频谱匹配方法；不把原始数据集比较写成当前通用优劣排序。"
  },
  "crepe-repository": {
    "title": "CREPE: A Convolutional REpresentation for Pitch Estimation",
    "authors": "Kim JW, Salamon J, Li P, Bello JP; MARL",
    "year": "2018；仓库核查 2026-10-05",
    "publication": "作者代码仓库及 ICASSP 2018 论文入口",
    "url": "https://github.com/marl/crepe",
    "access": "documentation",
    "supports": "核对单声源波形输入、预训练模型与输出说明；不沿用历史最优性能声明。"
  },
  "librosa-pyin": {
    "title": "librosa.pyin",
    "authors": "librosa",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://librosa.org/doc/0.11.0/generated/librosa.pyin.html",
    "access": "documentation",
    "supports": "官方版本化文档；核对概率候选、维特比解码、有声判定与参数。包含Mauch与Dixon（2014）概率YIN原始方法及de Cheveigné与Kawahara（2002）YIN论文入口；未在本词条语料上运行概率YIN。"
  },
  "moerel-2014": {
    "title": "An anatomical and functional topography of human auditory cortical areas",
    "authors": "Moerel M, De Martino F, Formisano E.",
    "year": "2014",
    "publication": "Frontiers in neuroscience, 8, 225",
    "doi": "10.3389/fnins.2014.00225",
    "url": "https://pubmed.ncbi.nlm.nih.gov/25120426/",
    "access": "abstract",
    "supports": "人类听觉皮层拓扑与个体差异的综述性综合；支持多指标区域划分，不提供唯一固定地图。"
  },
  "dick-2012": {
    "title": "In vivo functional and myeloarchitectonic mapping of human primary auditory areas",
    "authors": "Dick F, Tierney AT, Lutti A, Josephs O, Sereno MI, Weiskopf N.",
    "year": "2012",
    "publication": "The Journal of neuroscience : the official journal of the Society for Neuroscience, 32(46), 16095-16105",
    "doi": "10.1523/jneurosci.1712-12.2012",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23152594/",
    "access": "abstract",
    "supports": "结构髓鞘与功能频率映射相结合的人类研究；核心区镜像梯度不等于全皮层只有两张地图。"
  },
  "amt-verhulst2018": {
    "title": "verhulst2018: Cochlear transmission-line model including a model of the brainstem",
    "authors": "Auditory Modeling Toolbox",
    "year": "访问日期 2026-10-06",
    "publication": "官方文档与代码",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/verhulst2018.php",
    "access": "documentation",
    "supports": "AMT 1.6.0接口文档；核对声压输入、位置／频率选取、机械与神经输出以及波Ⅰ、Ⅲ、Ⅴ字段；原始2018年论文标题以作者仓库及出版记录为准，未运行模型。"
  },
  "coffey-2019": {
    "title": "Evolving perspectives on the sources of the frequency-following response",
    "authors": "Coffey EBJ, Nicol T, White-Schwoch T, Chandrasekaran B, Krizman J, Skoe E, Zatorre RJ, Kraus N.",
    "year": "2019",
    "publication": "Nature communications, 10(1), 5036",
    "doi": "10.1038/s41467-019-13003-w",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6834633/",
    "access": "fulltext",
    "supports": "频率跟随反应的皮层下及皮层来源；不同刺激和记录下贡献不同。"
  },
  "picton-assr-2003": {
    "title": "Human auditory steady-state responses",
    "authors": "Picton TW, John MS, Dimitrijevic A, Purcell D.",
    "year": "2003",
    "publication": "International journal of audiology, 42(4), 177-219",
    "doi": "10.3109/14992020309101316",
    "url": "https://pubmed.ncbi.nlm.nih.gov/12790346/",
    "access": "abstract",
    "supports": "稳态反应的调制速率、觉醒状态、频域分析和来源差异。"
  },
  "naatanen-2007": {
    "title": "The mismatch negativity (MMN) in basic research of central auditory processing: a review",
    "authors": "Näätänen R, Paavilainen P, Rinne T, Alho K.",
    "year": "2007",
    "publication": "Clinical neurophysiology : official journal of the International Federation of Clinical Neurophysiology, 118(12), 2544-2590",
    "doi": "10.1016/j.clinph.2007.04.026",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17931964/",
    "access": "abstract",
    "supports": "失匹配负波与声音变化加工的综述；差异波的实验条件和机制解释需分开。"
  },
  "polich-2007": {
    "title": "Updating P300: an integrative theory of P3a and P3b",
    "authors": "Polich J.",
    "year": "2007",
    "publication": "Clinical neurophysiology : official journal of the International Federation of Clinical Neurophysiology, 118(10), 2128-2148",
    "doi": "10.1016/j.clinph.2007.04.019",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17573239/",
    "access": "abstract",
    "supports": "P3a与P3b的注意、任务和记忆关联；不视为单一认知能力诊断。"
  },
  "widmann-2015": {
    "title": "Digital filter design for electrophysiological data--a practical approach",
    "authors": "Widmann A, Schröger E, Maess B.",
    "year": "2015",
    "publication": "Journal of neuroscience methods, 250, 34-46",
    "doi": "10.1016/j.jneumeth.2014.08.002",
    "url": "https://pubmed.ncbi.nlm.nih.gov/25128257/",
    "access": "abstract",
    "supports": "电生理数字滤波的方法与伪迹；零相位不等于没有时间扩散。"
  },
  "maris-2007": {
    "title": "Nonparametric statistical testing of EEG- and MEG-data",
    "authors": "Maris E, Oostenveld R.",
    "year": "2007",
    "publication": "Journal of neuroscience methods, 164(1), 177-190",
    "doi": "10.1016/j.jneumeth.2007.03.024",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17517438/",
    "access": "abstract",
    "supports": "非参数检验和多重比较的方法框架；簇层面推断不等于逐点显著。"
  },
  "mtrf-toolbox": {
    "title": "The Multivariate Temporal Response Function (mTRF) Toolbox: A MATLAB Toolbox for Relating Neural Signals to Continuous Stimuli",
    "authors": "Crosse, M. J., Di Liberto, G. M., Bednar, A., & Lalor, E. C.",
    "year": "2016",
    "publication": "Frontiers in Human Neuroscience, 10, 604.",
    "doi": "10.3389/fnhum.2016.00604",
    "url": "https://github.com/mickcrosse/mTRF-Toolbox",
    "access": "documentation",
    "supports": "本轮核对作者仓库的前向／反向框架、交叉验证和保留测试示例及原始论文书目；未通读原始论文或运行脑电模型。正文公式为该线性框架的教学表达。"
  }
};
