import type { Reference } from './references';

export const objectiveSpeechEvaluationReferences: Record<string, Reference> = {
  "ose-p800": {
    "title": "Methods for subjective determination of transmission quality",
    "authors": "ITU-T",
    "year": "1996",
    "publication": "Recommendation ITU-T P.800",
    "url": "https://www.itu.int/rec/T-REC-P.800/en",
    "access": "documentation",
    "supports": "2026-11-06：官方目录确认现行条目；MOS定义与主观评分说明亦结合NISQA原文引言。未声称执行完整标准实验。"
  },
  "ose-p835": {
    "title": "Subjective test methodology for evaluating speech communication systems and terminals providing noise suppression functionality",
    "authors": "ITU-T",
    "year": "2026",
    "publication": "Recommendation ITU-T P.835 (07/2026)",
    "url": "https://www.itu.int/rec/T-REC-P.835-202607-I/en",
    "access": "documentation",
    "supports": "2026-11-06：官方目录与公开Summary：2026-07-29批准，SIG/BAK/OVRL三维评价及适用配置；未访问受限标准正文。2022年DNSMOS使用当时框架，不冒称采用2026修订。"
  },
  "ose-vankuyk-2018": {
    "title": "An Evaluation of Intrusive Instrumental Intelligibility Metrics",
    "authors": "Steven Van Kuyk; W. Bastiaan Kleijn; Richard C. Hendriks",
    "year": "2018",
    "publication": "IEEE/ACM Transactions on Audio, Speech, and Language Processing, 26(11), 2153–2166",
    "url": "https://pure.tudelft.nl/ws/portalfiles/portal/50160817/An_Evaluation_of_Intrusive_Instrumental_Intelligibility_Metrics.pdf",
    "access": "fulltext",
    "supports": "2026-11-06：作者机构接收稿Abstract与Introduction、正式书目；支持12种指标、跨失真泛化与开发数据接触的限制。不将旧版本排名推广到当前所有模型。",
    "doi": "10.1109/TASLP.2018.2856374"
  },
  "ose-hasqi-2014": {
    "title": "The Hearing-Aid Speech Quality Index (HASQI) Version 2",
    "authors": "James M. Kates; Kathryn H. Arehart",
    "year": "2014",
    "publication": "Journal of the Audio Engineering Society, 62(3), 99–117",
    "url": "https://aes.org/publications/elibrary/elibrary-page/?id=17126",
    "access": "abstract",
    "supports": "2026-11-06：出版方摘要与Crossref：外周听损模型、包络／精细结构及长期谱成分，线性与非线性项相乘。未复现模型。",
    "doi": "10.17743/jaes.2014.0006"
  },
  "ose-kates-overview": {
    "title": "An overview of the HASPI and HASQI metrics for predicting speech intelligibility and speech quality for normal hearing, hearing loss, and hearing aids",
    "authors": "James M. Kates; Kathryn H. Arehart",
    "year": "2022",
    "publication": "Hearing Research, 426, 108608",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10833438/",
    "access": "fulltext",
    "supports": "2026-11-06：作者方法综述；通过出版社及PMC可检索正文读取Introduction、3.1、3.2、5.7、5.8与Conclusions段落，支持不同参考模型、声级／听力及个体推广边界。PMC直接页遇验证页，全文XML请求失败；未取得完整本地全文。",
    "doi": "10.1016/j.heares.2022.108608"
  },
  "ose-p862": {
    "title": "Perceptual evaluation of speech quality (PESQ): An objective method for end-to-end speech quality assessment of narrow-band telephone networks and speech codecs",
    "authors": "ITU-T",
    "year": "2001（2024撤销）",
    "publication": "Recommendation ITU-T P.862",
    "url": "https://www.itu.int/rec/T-REC-P.862/en",
    "access": "documentation",
    "supports": "2026-11-06：官方条目明确P.862/1/2/3在2024-01-05撤销；支持历史标准身份及版本区分，不宣称本次执行标准参考实现。"
  },
  "ose-p863": {
    "title": "Perceptual objective listening quality prediction",
    "authors": "ITU-T",
    "year": "2018（含2020修订条目）",
    "publication": "Recommendation ITU-T P.863",
    "url": "https://www.itu.int/rec/T-REC-P.863/en",
    "access": "documentation",
    "supports": "2026-11-06：官方现行目录与2018版Summary：预测ACR听音质量、窄带与全带模式、20 kHz全带上限及一致性检查；未读取全部算法附件。"
  },
  "ose-dnsmos-2022": {
    "title": "DNSMOS P.835: A Non-Intrusive Perceptual Objective Speech Quality Metric to Evaluate Noise Suppressors",
    "authors": "Chandan K. A. Reddy; Vishak Gopal; Ross Cutler",
    "year": "2022",
    "publication": "ICASSP 2022, 886–890",
    "url": "https://arxiv.org/abs/2110.01763",
    "access": "fulltext",
    "supports": "2026-11-06：作者论文PDF摘要、引言及相关方法；模型学习P.835的SIG/BAK/OVRL人类评分。Crossref核对正式会议版本；官方GitHub补充实现入口，不作为行为获益证明。",
    "doi": "10.1109/ICASSP43922.2022.9746108"
  },
  "ose-nisqa-2021": {
    "title": "NISQA: A Deep CNN-Self-Attention Model for Multidimensional Speech Quality Prediction with Crowdsourced Datasets",
    "authors": "Gabriel Mittag; Babak Naderi; Assmaa Chehadi; Sebastian Möller",
    "year": "2021",
    "publication": "Interspeech 2021, 2127–2131",
    "url": "https://www.isca-archive.org/interspeech_2021/mittag21_interspeech.html",
    "access": "fulltext",
    "supports": "2026-11-06：ISCA论文PDF摘要与引言／模型说明：通信领域、总体质量与四个维度；不把特定数据集验证推广为普适。",
    "doi": "10.21437/Interspeech.2021-299"
  },
  "ose-sisdr-2019": {
    "title": "SDR – Half-Baked or Well Done?",
    "authors": "Jonathan Le Roux; Scott Wisdom; Hakan Erdogan; John R. Hershey",
    "year": "2019",
    "publication": "ICASSP 2019, 626–630",
    "url": "https://www.merl.com/publications/TR2019-013",
    "access": "fulltext",
    "supports": "2026-11-06：作者机构论文第2节特别是2.3及式4–5；投影定义与尺度边界。本文用独立正交正弦信号教学计算，不冒称感知实验。",
    "doi": "10.1109/ICASSP.2019.8683855"
  },
  "ose-p808": {
    "title": "Subjective evaluation of speech quality with a crowdsourcing approach",
    "authors": "ITU-T",
    "year": "2021",
    "publication": "Recommendation ITU-T P.808 (06/2021)",
    "url": "https://www.itu.int/rec/T-REC-P.808/en",
    "access": "documentation",
    "supports": "2026-11-06：官方现行目录和公开方法范围；支持众包语音评分方法身份，不宣称本次执行了标准或阅读全部规范。"
  },
  "ose-voicemos-2024": {
    "title": "The VoiceMOS Challenge 2024: Beyond Speech Quality Prediction",
    "authors": "Wen-Chin Huang; Szu-Wei Fu; Erica Cooper; Ryandhimas E. Zezario; Tomoki Toda; Hsin-Min Wang; Junichi Yamagishi; Yu Tsao",
    "year": "2024",
    "publication": "IEEE Spoken Language Technology Workshop (SLT), 803–810",
    "url": "https://arxiv.org/abs/2409.07001",
    "access": "fulltext",
    "supports": "2026-11-06：作者机构PDF摘要、引言与赛道说明；高质量合成、歌声与少标签增强语音是不同域。按正式会议年记2024，未把所有系统称为通用MOS模型。",
    "doi": "10.1109/SLT61566.2024.10832295"
  },
  "ose-fuse-2025": {
    "title": "FUSE: Universal Speech Enhancement using Multi-Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge",
    "authors": "Nabarun Goswami; Tatsuya Harada",
    "year": "2025",
    "publication": "Interspeech 2025, 883–887",
    "url": "https://www.isca-archive.org/interspeech_2025/goswami25_interspeech.html",
    "access": "fulltext",
    "supports": "2026-11-06：ISCA官方摘要及论文Table 1/2和结论段；生成阶段感知指标与SDR的权衡是特定系统结果，不概括为波形下降总是无害。",
    "doi": "10.21437/Interspeech.2025-251"
  }
};
