import type { Reference } from './references.ts';

export const zwickerReferences: Record<string, Reference> = {
  "zwicker-fastl2024": {
    "title": "Eberhard Zwicker – Zum 100. Geburtstag",
    "authors": "Hugo Fastl",
    "year": "2024",
    "publication": "Akustik Journal 01/24, 7–15",
    "url": "https://www.dega-akustik.de/fileadmin/dega-akustik.de/publikationen/akustik-journal/24-01/akustik_journal_2024_01_online_artikel1.pdf",
    "access": "fulltext",
    "supports": "下载整期PDF，选读印刷7–15页相关段落；渲染并检查第7页。核对1924-01-15出生、1990-11-22去世、1950学位、1952博士、1956任教资格及研究访问。历史照片署名T. Zwicker，未核实开放许可，仅链接。"
  },
  "zwicker-tumhistory": {
    "title": "Die Münchener Schule der Psychoakustik",
    "authors": "Hugo Fastl",
    "year": "n.d.",
    "publication": "Technische Universität München, institutional historical essay, 16 pages; accessed 2026-10-10",
    "url": "https://mediatum.ub.tum.de/doc/1138439/98963.pdf",
    "access": "fulltext",
    "supports": "下载机构存档，选读PDF第1–5页：磁带录音与调制可听性研究动机、1967创设教席与Terhardt到慕尼黑、1971 Fastl加入及多种听觉维度。属于后来的历史回顾，不冒称当时实验日志；PDF未注明可核实出版日期，不推定年代。"
  },
  "zwicker-asa": {
    "title": "Acoustical Society of America Awards",
    "authors": "Acoustical Society of America",
    "year": "n.d.",
    "publication": "Official award recipients; accessed 2026-10-10",
    "url": "https://acousticalsociety.org/acoustical-society-of-america-awards/",
    "access": "documentation",
    "supports": "核对1987 Silver Medal in Psychological and Physiological Acoustics获奖名单。不是ASA Gold Medal。"
  },
  "zwicker-dega": {
    "title": "Helmholtz-Medaille",
    "authors": "Deutsche Gesellschaft für Akustik",
    "year": "n.d.",
    "publication": "Official award recipients; accessed 2026-10-10",
    "url": "https://www.dega-akustik.de/preise-grants/helmholtz-medaille",
    "access": "documentation",
    "supports": "核对1991 Eberhard Zwicker，名单明确posthum；不写未经核实的同名奖项或在世授奖。"
  },
  "zwicker-band1957": {
    "title": "Critical Band Width in Loudness Summation",
    "authors": "E. Zwicker; G. Flottorp; S. S. Stevens",
    "year": "1957",
    "publication": "The Journal of the Acoustical Society of America, 29(5), 548–557",
    "url": "https://www.ee.columbia.edu/~dpwe/e6820/papers/ZwicFS57-crband.pdf",
    "access": "fulltext",
    "supports": "下载Columbia大学存档的原刊扫描PDF；渲染选读印刷548页摘要、引言、研究分工与GENERAL PROCEDURE。固定总SPL扩宽噪声、纯音间隔和等响匹配；耳机双耳、约1秒信号与0.5秒间隔、从两侧夹逼等响。未通读10页或提取原始数据；图1为独立声学算术。纠正候选DOI 1.1908965（实际为另一篇耳蜗模型论文）。",
    "doi": "10.1121/1.1908963"
  },
  "zwicker-bark1961": {
    "title": "Subdivision of the Audible Frequency Range into Critical Bands (Frequenzgruppen)",
    "authors": "Eberhard Zwicker",
    "year": "1961",
    "publication": "The Journal of the Acoustical Society of America, 33(2), 248",
    "url": "https://doi.org/10.1121/1.1908630",
    "access": "metadata",
    "supports": "核对出版社提交的Crossref书目、作者、1961与248页。未取得原信件全文；24带与范围的具体描述另据Völk 2015原文，不用书目冒称测量数据。",
    "doi": "10.1121/1.1908630"
  },
  "zwicker-analytic1980": {
    "title": "Analytical expressions for critical-band rate and critical bandwidth as a function of frequency",
    "authors": "E. Zwicker; E. Terhardt",
    "year": "1980",
    "publication": "The Journal of the Acoustical Society of America, 68(5), 1523–1525",
    "url": "https://doi.org/10.1121/1.385079",
    "access": "abstract",
    "supports": "读取原出版社提交Crossref的摘要及书目：将表格关系写为便于计算的解析式。未阅读全文；正文两式与Völk 2015原文式1、9交叉核对，数值由本站计算。",
    "doi": "10.1121/1.385079"
  },
  "zwicker-volk2015": {
    "title": "Updated analytical expressions for critical bandwidth and critical-band rate",
    "authors": "Florian Völk",
    "year": "2015",
    "publication": "DAGA 2015 Nürnberg, 1181–1184",
    "url": "https://pub.dega-akustik.de/DAGA_2015/data/articles/000054.pdf",
    "access": "fulltext",
    "supports": "读取原会议PDF概念说明、式1/9及范围限制：临界带无固定频率位置、经典CBW与ERB定义不同、24带与15.5kHz表格；低频对称带宽跨负频率及高频外推限制。未复现其新拟合或宣称新公式实测优越；本页使用1980经典式。"
  },
  "zwicker-scharf1965": {
    "title": "A model of loudness summation",
    "authors": "Eberhard Zwicker; Bertram Scharf",
    "year": "1965",
    "publication": "Psychological Review, 72(1), 3–26",
    "url": "https://pubmed.ncbi.nlm.nih.gov/14296451/",
    "access": "abstract",
    "supports": "核对PubMed/Crossref元数据；PubMed没有摘要。另读取原发表论文摘要和引言的公开索引文本（载体另记台账）：心理物理建模、掩蔽图形、specific loudness及积分。未阅读全文；积分解释另据Fastl 2005公开作者章节，图3为任意指定轮廓。",
    "doi": "10.1037/h0021703"
  },
  "zwicker-quality2005": {
    "title": "Psycho-acoustics and sound quality",
    "authors": "Hugo Fastl",
    "year": "2005",
    "publication": "In Communication Acoustics, Springer, 139–162",
    "url": "https://mediatum.ub.tum.de/doc/1138438/416706.pdf",
    "access": "fulltext",
    "supports": "下载24页作者章节，选读方法、3.1响度、3.2尖锐度、粗糙度/起伏强度及意义、品牌与视觉相关段落。特定响度面积、包络/后掩蔽/时间积分功能与评价任务边界。没有逐项复现模型、复制图或验证烦扰预测；TUM书目核对章页与DOI。",
    "doi": "10.1007/3-540-27437-5_6"
  },
  "zwicker-program1991": {
    "title": "Program for calculating loudness according to DIN 45631 (ISO 532B)",
    "authors": "Eberhard Zwicker; Hugo Fastl; Ulrich Widmann; Kenji Kurakata; Sonoko Kuwano; Seiichiro Namba",
    "year": "1991",
    "publication": "Journal of the Acoustical Society of Japan (E), 12(1), 39–42",
    "url": "https://www.jstage.jst.go.jp/article/ast1980/12/1/12_1_39/_article",
    "access": "fulltext",
    "supports": "下载4页原刊PDF，选读39页摘要/引言及42页注记：1990-09-10收稿、1991刊出、IBM兼容机到NEC PC-9801的BASIC适配、当时DIN/ISO 532B稳态计算、强时变需额外非线性加权。未执行程序或检查全部代码；不冒称2017版实现。",
    "doi": "10.1250/ast.12.39"
  },
  "zwicker-iso1": {
    "title": "ISO 532-1:2017 — Acoustics — Methods for calculating loudness — Part 1: Zwicker method",
    "authors": "ISO",
    "year": "2017",
    "publication": "Official public scope, edition 1 and 2017-11 corrected version; accessed 2026-10-10",
    "url": "https://www.iso.org/standard/63077.html",
    "access": "documentation",
    "supports": "读取公开范围与生命周期：规定条件下健康听觉、稳态及时变两种方法、由特定响度算响度、有害效应评价在范围之外。未购买或通读58页标准。页面记录2024-11-01待修订与开发中后继，正文按2017版本说明，不称永远最新。"
  },
  "zwicker-iso2": {
    "title": "ISO 532-2:2017 — Acoustics — Methods for calculating loudness — Part 2: Moore-Glasberg method",
    "authors": "ISO",
    "year": "2017",
    "publication": "Official public scope, edition 1; accessed 2026-10-10",
    "url": "https://www.iso.org/standard/63078.html",
    "access": "documentation",
    "supports": "读取公开范围：稳态、健康听觉成人、单耳/双耳、Moore–Glasberg算法及有害效应评价不在范围内。未通读28页标准或运行参考代码；生命周期已有待修订后继。"
  },
  "zwicker-after1964": {
    "title": "“Negative Afterimage” in Hearing",
    "authors": "Eberhard Zwicker",
    "year": "1964",
    "publication": "The Journal of the Acoustical Society of America, 36(12), 2413–2415",
    "url": "https://doi.org/10.1121/1.1919373",
    "access": "abstract",
    "supports": "读取出版社提交Crossref的原摘要及书目：凹口噪声停止后的衰减音调，音高在凹口频率内，原摘要给定约60dB/1分钟等特定条件。未阅读全文、无通用发生率或演示处方。图4的2–3kHz为自选理想示意、横轴非定量。",
    "doi": "10.1121/1.1919373"
  },
  "zwicker-norena2003": {
    "title": "Neural correlates of an auditory afterimage in primary auditory cortex",
    "authors": "A. J. Noreña; J. J. Eggermont",
    "year": "2003",
    "publication": "Journal of the Association for Research in Otolaryngology, 4(3), 312–328",
    "url": "https://pubmed.ncbi.nlm.nih.gov/14690050/",
    "access": "abstract",
    "supports": "读取原摘要：氯胺酮麻醉猫、不同凹口噪声与白噪声、多单位放电率/相关及刺激后变化、作者称potential correlates。PMC全文请求返回验证码，未据此宣称全文阅读或猫有主观音调报告。",
    "doi": "10.1007/s10162-002-3039-1"
  },
  "zwicker-review2025": {
    "title": "The Zwicker tone as a model to investigate auditory processing and tinnitus: a scoping review",
    "authors": "Jude L. R. Barker; Derek J. Hoare; Magdalena Sereda; Joseph Sollini",
    "year": "2025",
    "publication": "Frontiers in Neuroscience, 19, 1656934",
    "url": "https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1656934/full",
    "access": "fulltext",
    "supports": "选读公开原文Introduction、Methods人类研究范围、Discussion的条件与个体差异、临床联系尚待检验。Crossref核对作者与2025-08-22。PMC直连失败后用原出版社全文，未复制图、未把后效当作诊断或疗法，未以综述发生率泛化全部人群。",
    "doi": "10.3389/fnins.2025.1656934"
  },
  "zwicker-florentine1979": {
    "title": "A model of loudness summation applied to noise-induced hearing loss",
    "authors": "Mary Florentine; Eberhard Zwicker",
    "year": "1979",
    "publication": "Hearing Research, 1(2), 121–132",
    "url": "https://pubmed.ncbi.nlm.nih.gov/521397/",
    "access": "abstract",
    "supports": "读取原摘要索引：正常及噪声性听力损失观察者、响度总和与窄带掩蔽、重振和频率选择性降低需修改模型参数。未获取全文、无患者样本量或具体增益处方。",
    "doi": "10.1016/0378-5955(79)90023-6"
  },
  "zwicker-mathworks": {
    "title": "acousticLoudness — Perceived loudness of acoustic signal",
    "authors": "MathWorks",
    "year": "n.d.",
    "publication": "Official MATLAB Audio Toolbox documentation, R2026b page; accessed 2026-10-10",
    "url": "https://www.mathworks.com/help/audio/ref/acousticloudness.html",
    "access": "documentation",
    "supports": "读取当前官方接口：校准因子、声场、ISO方法、TimeVarying、特定响度和N5超过率定义。仅作为使用条件示例，未运行函数、未作完整标准一致性检验；数字归一化不能代替声压校准。"
  }
};
