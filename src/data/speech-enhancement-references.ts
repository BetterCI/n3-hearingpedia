import type { Reference } from './references';

export const speechEnhancementReferences: Record<string, Reference> = {
  "se-wang-chen-2018": {
    "title": "Supervised Speech Separation Based on Deep Learning: An Overview",
    "authors": "DeLiang Wang; Jitong Chen",
    "year": "2018",
    "publication": "IEEE/ACM Transactions on Audio, Speech, and Language Processing, 26(10), 1702-1726",
    "doi": "10.1109/TASLP.2018.2842159",
    "url": "https://jitongchen.com/papers/overview_taslp2018.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：作者公开全文：任务范围、掩蔽目标与泛化背景；综述用作导航，临床和具体系统结论另引原始研究。"
  },
  "se-boll-1979": {
    "title": "Suppression of acoustic noise in speech using spectral subtraction",
    "authors": "S. Boll",
    "year": "1979",
    "publication": "IEEE Transactions on Acoustics, Speech, and Signal Processing, 27(2), 113-120",
    "doi": "10.1109/TASSP.1979.1163209",
    "url": "https://course.ece.cmu.edu/~ece491/homework/Boll79.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：已读取CMU公开论文PDF的算法及残余噪声段落。原文主要为幅度谱减；词条另列功率谱减教学变体，不声称是原文逐式复现。"
  },
  "se-ephraim-1984": {
    "title": "Speech enhancement using a minimum-mean square error short-time spectral amplitude estimator",
    "authors": "Y. Ephraim; D. Malah",
    "year": "1984",
    "publication": "IEEE Transactions on Acoustics, Speech, and Signal Processing, 32(6), 1109-1121",
    "doi": "10.1109/TASSP.1984.1164453",
    "url": "https://malah.net.technion.ac.il/files/2017/08/Ephraim_Speech_Enhancement_ASSP84.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：作者PDF摘要、检索可读的决策导向段落及出版元数据：短时谱幅度MMSE与先验SNR；不声称核对全文每个公式。维纳图为本站独立代数推导。"
  },
  "se-martin-2001": {
    "title": "Noise power spectral density estimation based on optimal smoothing and minimum statistics",
    "authors": "R. Martin",
    "year": "2001",
    "publication": "IEEE Transactions on Speech and Audio Processing, 9(5), 504-512",
    "doi": "10.1109/89.928915",
    "url": "https://www.csd.uoc.gr/~hy578/2005/projects/ieee_sp_tsap_2001009_05jul_0504mart.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：公开原论文PDF摘要及方法导言：最小统计量、无需硬VAD及最小值偏差补偿；未照抄具体参数。"
  },
  "se-paliwal-2011": {
    "title": "The importance of phase in speech enhancement",
    "authors": "Kuldip Paliwal; Kamil Wójcicki; Benjamin Shannon",
    "year": "2011",
    "publication": "Speech Communication, 53(4), 465-494",
    "doi": "10.1016/j.specom.2010.12.003",
    "url": "https://www.sciencedirect.com/science/article/abs/pii/S0167639310002086",
    "access": "abstract",
    "supports": "2026-11-06：出版方摘要和引言：32 ms窗条件下理想与非理想相位实验，不能把oracle结果当部署性能。"
  },
  "se-complex-2016": {
    "title": "Complex Ratio Masking for Monaural Speech Separation",
    "authors": "Donald S. Williamson; Yuxuan Wang; DeLiang Wang",
    "year": "2016",
    "publication": "IEEE/ACM Transactions on Audio, Speech, and Language Processing, 24(3), 483-492",
    "doi": "10.1109/TASLP.2015.2512042",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4826046/",
    "access": "abstract",
    "supports": "2026-11-06：Europe PMC原始摘要：同时估计复数掩蔽实虚部；文中两个相量案例为本站独立代数演示，不是论文实验数据。"
  },
  "se-souden-2010": {
    "title": "On Optimal Frequency-Domain Multichannel Linear Filtering for Noise Reduction",
    "authors": "M. Souden; J. Benesty; S. Affes",
    "year": "2010",
    "publication": "IEEE Transactions on Audio, Speech, and Language Processing, 18(2), 260-276",
    "doi": "10.1109/TASL.2009.2025790",
    "url": "https://www.wirelesslab.ca/File/pdf_files/journals/J042.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：作者机构公开17页PDF：多通道维纳／MVDR约束与噪声失真折中。本站采用已知传递向量的标准形式和自设阵列，不冒充原文仿真复现。"
  },
  "se-deepfilter-2023": {
    "title": "DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement",
    "authors": "Hendrik Schröter; Alberto N. Escalante-B.; Tobias Rosenkranz; Andreas Maier",
    "year": "2023",
    "publication": "Interspeech 2023, Show & Tell, 2008–2009",
    "url": "https://www.isca-archive.org/interspeech_2023/schroter23b_interspeech.html",
    "access": "fulltext",
    "supports": "2026-11-06：ISCA会议PDF第2–4节；48 kHz、20 ms窗、10 ms步长、两帧前视与40 ms延迟；RTF 0.19限定原文CPU和实现。作者顺序按会议PDF，未沿用不同顺序的arXiv元数据。"
  },
  "se-close-2024": {
    "title": "Hallucination in Perceptual Metric-Driven Speech Enhancement Networks",
    "authors": "George Close; Thomas Hain; Stefan Goetze",
    "year": "2024",
    "publication": "2024 32nd European Signal Processing Conference (EUSIPCO), 21-25",
    "doi": "10.23919/EUSIPCO63174.2024.10714927",
    "url": "https://www.eurasip.org/Proceedings/Eusipco/Eusipco2024/pdfs/0000021.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：EUSIPCO原论文全文：预测器作为训练目标可能引入伪迹，主观评价验证其可察觉性；不泛化为所有生成式网络的行为。"
  },
  "se-pase-2026": {
    "title": "PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement",
    "authors": "Xiaobin Rong; Qinwen Hu; Mansur Yesilbursa; Kamil Wojcicki; Jing Lu",
    "year": "2026",
    "publication": "Proceedings of the AAAI Conference on Artificial Intelligence, 40(39), 32826-32834",
    "doi": "10.1609/aaai.v40i39.40562",
    "url": "https://arxiv.org/html/2511.13300v1",
    "access": "fulltext",
    "supports": "2026-11-06：AAAI出版记录与Crossref核对2026卷期；出版全文受访问限制，实际读取作者arXiv:2511.13300v1全文的方法及评价段落。仅概述表征去噪、双流重建和保真目标，不引用最终版数值或宣称普遍领先。"
  },
  "se-hu-2007": {
    "title": "A comparative intelligibility study of single-microphone noise reduction algorithms",
    "authors": "Yi Hu; Philipos C. Loizou",
    "year": "2007",
    "publication": "The Journal of the Acoustical Society of America, 122(3), 1777-1786",
    "doi": "10.1121/1.2766778",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17927437/",
    "access": "abstract",
    "supports": "2026-11-06：Europe PMC原始摘要：8算法、4噪声、0与5 dB、正常听者；一个噪声条件例外，未得显著改善不解释为所有条件严格零效应。"
  },
  "se-healy-2013": {
    "title": "An algorithm to improve speech recognition in noise for hearing-impaired listeners",
    "authors": "Eric W. Healy; Sarah E. Yoho; Yuxuan Wang; DeLiang Wang",
    "year": "2013",
    "publication": "The Journal of the Acoustical Society of America, 134(4), 3029-3038",
    "doi": "10.1121/1.4820893",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3799726/",
    "access": "abstract",
    "supports": "2026-11-06：Europe PMC原始摘要：学习掩蔽、训练测试句子不同、所测噪声下正常和听损听者获益；不推出所有陌生噪声或日常设备均有相同改善。"
  }
};
