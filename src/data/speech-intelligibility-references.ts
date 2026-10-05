import type { Reference } from './references';

export const speechIntelligibilityReferences: Record<string, Reference> = {
  "asa-definition": {
    "title": "Speech intelligibility",
    "authors": "Acoustical Society of America",
    "year": "2026年核查",
    "publication": "ASA Standards terminology",
    "url": "https://asastandards.org/terms/speech-intelligibility/",
    "access": "documentation",
    "supports": "查阅术语说明；支持语言单位辨认的定义。"
  },
  "boothroyd-1988": {
    "title": "Mathematical treatment of context effects in phoneme and word recognition",
    "authors": "Boothroyd, A. & Nittrouer, S.",
    "year": "1988",
    "publication": "The Journal of the Acoustical Society of America, 84(1), 101–114",
    "doi": "10.1121/1.396976",
    "url": "https://pubmed.ncbi.nlm.nih.gov/3411038/",
    "access": "abstract",
    "supports": "支持语言语境与部分、整体识别的区别；教学独立词示例不拟合该论文数据。"
  },
  "festen-1990": {
    "title": "Effects of fluctuating noise and interfering speech on the speech-reception threshold for impaired and normal hearing",
    "authors": "Festen, J. M. & Plomp, R.",
    "year": "1990",
    "publication": "The Journal of the Acoustical Society of America, 88(4), 1725–1736",
    "doi": "10.1121/1.400247",
    "url": "https://pubmed.ncbi.nlm.nih.gov/2262629/",
    "access": "abstract",
    "supports": "支持背景起伏、听力状态及可听度解释的范围。"
  },
  "brungart-2001": {
    "title": "Informational and energetic masking effects in the perception of two simultaneous talkers",
    "authors": "Brungart, D. S.",
    "year": "2001",
    "publication": "The Journal of the Acoustical Society of America, 109(3), 1101–1109",
    "doi": "10.1121/1.1345696",
    "url": "https://pubmed.ncbi.nlm.nih.gov/11303924/",
    "access": "abstract",
    "supports": "支持该竞争语音任务中的相似性影响及非单调现象。"
  },
  "hint-1994": {
    "title": "Development of the Hearing in Noise Test for the measurement of speech reception thresholds in quiet and in noise",
    "authors": "Nilsson, M., Soli, S. D. & Sullivan, J. A.",
    "year": "1994",
    "publication": "The Journal of the Acoustical Society of America, 95(2), 1085–1099",
    "doi": "10.1121/1.408469",
    "url": "https://pubmed.ncbi.nlm.nih.gov/8132902/",
    "access": "abstract",
    "supports": "支持材料均衡及句子接收阈测试背景。"
  },
  "mhint-2007": {
    "title": "Development of the Mandarin Hearing in Noise Test (MHINT)",
    "authors": "Wong, L. L. N., Soli, S. D., Liu, S., Han, N. & Huang, M.-W.",
    "year": "2007",
    "publication": "Ear and Hearing, 28(2 Suppl), 70S–74S",
    "doi": "10.1097/AUD.0b013e31803154d0",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17496652/",
    "access": "abstract",
    "supports": "核查开发目的与材料评价路线，不复用未核对的版本常模。"
  },
  "cmnmatrix-2018": {
    "title": "Construction and evaluation of the Mandarin Chinese matrix (CMNmatrix) sentence test for the assessment of speech recognition in noise",
    "authors": "Hu, H., Xi, X., Wong, L. L. N., Hochmuth, S., Warzybok, A. & Kollmeier, B.",
    "year": "2018",
    "publication": "International Journal of Audiology, 57(11), 838–850",
    "doi": "10.1080/14992027.2018.1483083",
    "url": "https://pubmed.ncbi.nlm.nih.gov/30178681/",
    "access": "abstract",
    "supports": "支持50词矩阵、难度均衡、格式差异和练习效应；不把正常听力成人参考值推广到其他群体。"
  },
  "ansi-sii": {
    "title": "Methods for Calculation of the Speech Intelligibility Index",
    "authors": "Acoustical Society of America / ANSI",
    "year": "1997（2024年重确认）",
    "publication": "ASA/ANSI S3.5-1997 (R2024)",
    "url": "https://webstore.ansi.org/search/find?cp=1&f1=Standard%2CPackage&f2=2&f3=34&st=asa&v=50",
    "access": "metadata",
    "supports": "标准名称与2024年重确认信息经官方记录核查；未查阅付费全文，正文仅介绍概念性加权结构。"
  },
  "iec-sti-2020": {
    "title": "Sound system equipment—Part 16: Objective rating of speech intelligibility by speech transmission index",
    "authors": "International Electrotechnical Commission",
    "year": "2020（2025年勘误）",
    "publication": "IEC 60268-16:2020",
    "url": "https://webstore.iec.ch/en/publication/26771",
    "access": "documentation",
    "supports": "页面注明纳入2025年7月勘误；查阅公开范围与限制说明，未查阅标准付费正文。"
  },
  "taal-2011": {
    "title": "An Algorithm for Intelligibility Prediction of Time–Frequency Weighted Noisy Speech",
    "authors": "Taal, C. H., Hendriks, R. C., Heusdens, R. & Jensen, J.",
    "year": "2011",
    "publication": "IEEE Transactions on Audio, Speech, and Language Processing, 19(7), 2125–2136",
    "doi": "10.1109/TASL.2011.2114881",
    "url": "https://doi.org/10.1109/TASL.2011.2114881",
    "access": "abstract",
    "supports": "核查原论文摘要、模型描述及OpenAlex引文入口；不宣称未测试听者或失真的有效性。"
  },
  "jensen-2016": {
    "title": "An Algorithm for Predicting the Intelligibility of Speech Masked by Modulated Noise Maskers",
    "authors": "Jensen, J. & Taal, C. H.",
    "year": "2016",
    "publication": "IEEE/ACM Transactions on Audio, Speech, and Language Processing, 24(11), 2009–2022",
    "doi": "10.1109/TASLP.2016.2585878",
    "url": "https://doi.org/10.1109/TASLP.2016.2585878",
    "access": "abstract",
    "supports": "原论文摘要、作者机构元数据和Crossref书目核查；介绍方法定位，不重建实现参数。"
  },
  "haspi-2021": {
    "title": "The Hearing-Aid Speech Perception Index (HASPI) Version 2",
    "authors": "Kates, J. M. & Arehart, K. H.",
    "year": "2021",
    "publication": "Speech Communication, 131, 35–46",
    "doi": "10.1016/j.specom.2020.05.001",
    "url": "https://doi.org/10.1016/j.specom.2020.05.001",
    "access": "metadata",
    "supports": "书目经Crossref核查；模型介绍结合下一篇公开原始研究中的方法描述。"
  },
  "kates-context-2023": {
    "title": "Extending the Hearing-Aid Speech Perception Index (HASPI): Keywords, sentences, and context",
    "authors": "Kates, J. M.",
    "year": "2023",
    "publication": "The Journal of the Acoustical Society of America, 153(3), 1662–1673",
    "doi": "10.1121/10.0017546",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10257526/",
    "access": "fulltext",
    "supports": "本轮阅读摘要、引言和方法相关描述；支持评分目标、关键词与句子关系及模型表征。"
  },
  "lavandier-2026": {
    "title": "A Binaural Front End for Speech Intelligibility Models: Application to the Hearing-Aid Speech Perception Index (HASPI)",
    "authors": "Lavandier, M., Kates, J. M. & Arehart, K. H.",
    "year": "2026",
    "publication": "Trends in Hearing, 30, 23312165261422005",
    "doi": "10.1177/23312165261422005",
    "url": "https://pubmed.ncbi.nlm.nih.gov/41854306/",
    "access": "abstract",
    "supports": "核查2026-03-19发表记录和摘要；区分正常听力耳机实验与真实听觉设备验证，保留模型失配结果。"
  },
  "rosen-1992": {
    "title": "Temporal information in speech: acoustic, auditory and linguistic aspects",
    "authors": "Rosen, S.",
    "year": "1992",
    "publication": "Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences, 336(1278), 367–373",
    "doi": "10.1098/rstb.1992.0070",
    "url": "https://pubmed.ncbi.nlm.nih.gov/1354376/",
    "access": "abstract",
    "supports": "支持时域包络、周期性与精细结构的描述框架，不视为普遍固定的频率边界。"
  },
  "xu-tone-2002": {
    "title": "Features of stimulation affecting tonal-speech perception: implications for cochlear prostheses",
    "authors": "Xu, L., Tsai, Y. & Pfingst, B. E.",
    "year": "2002",
    "publication": "The Journal of the Acoustical Society of America, 112(1), 247–258",
    "doi": "10.1121/1.1487843",
    "url": "https://pubmed.ncbi.nlm.nih.gov/12141350/",
    "access": "abstract",
    "supports": "支持声调语言线索与声学仿真研究的任务边界；不将仿真成绩当作真实植入者效果。"
  }
};
