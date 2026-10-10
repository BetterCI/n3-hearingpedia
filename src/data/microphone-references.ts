import type { Reference } from './references';

export const microphoneReferences: Record<string, Reference> = {
  "mic-dpa-essentials": {
    "title": "Microphone technology – the essentials",
    "authors": "DPA Microphones",
    "year": "n.d.",
    "publication": "制造商官方工程说明",
    "url": "https://www.dpamicrophones.com/mic-university/technology/microphone-technology-the-essentials/",
    "access": "documentation",
    "supports": "读取压力／梯度及组合、动圈／带式／电容分类和声场影响段；支持声路与读出分类。本站方向模型和球面积分为独立教学推导，不转载原图或采用营销比较。"
  },
  "mic-bk-handbook": {
    "title": "Microphone Handbook, Volume 1 (BE 1447–12, March 2019)",
    "authors": "Brüel & Kjær",
    "year": "2019",
    "publication": "Brüel & Kjær 官方技术手册，所核版本155页",
    "url": "https://www.bksv.com/doc/be1447.pdf",
    "access": "documentation",
    "supports": "取得PDF并核对版本页，选读PDF第25–26页声场、第32–34页恒电荷与驻极体、第89–93页场响应和噪声、第147–148页校准与检查段；未逐页通读，未转载整本手册、原图或旧标准实施条款。补充核对第37–38页均压和低频响应。"
  },
  "mic-sessler-1962": {
    "title": "Self-Biased Condenser Microphone with High Capacitance",
    "authors": "G. M. Sessler; J. E. West",
    "year": "1962",
    "publication": "The Journal of the Acoustical Society of America, 34(11), 1787–1788",
    "url": "https://doi.org/10.1121/1.1909130",
    "access": "abstract",
    "supports": "核对OpenAlex摘要与Crossref元数据，并以作者所在机构技术词汇页交叉核对书目和驻极体机制；只引用无需外加直流极化的原理，不转录未核对全文的性能。注意此处为11期单数Microphone，区别于DOI 10.1121/1.1937012的12期补刊复数标题。",
    "doi": "10.1121/1.1909130"
  },
  "mic-tu-electret": {
    "title": "Electret Condenser Microphone (ECM)",
    "authors": "Institut für Nachrichtentechnik, Technische Universität Darmstadt",
    "year": "n.d.",
    "publication": "作者研究机构官方技术词汇页",
    "url": "https://www.nt.tu-darmstadt.de/ehemalige_fachgebiete_nt/elektroakustik_nt/forschung_ea/glossar_ea_nt/ecm_ea_nt/index.en.jsp",
    "access": "documentation",
    "supports": "读取驻极体薄膜、膜／背极两种安排、声压引起交流输出和1962论文书目；不使用网页旧市场份额估计或据此声称当今市场状态。"
  },
  "mic-hybrid-2026": {
    "title": "A capacitive-piezoelectric hybrid MEMS microphone with signal fusion for enhancing signal-to-noise ratio",
    "authors": "Yangyang Guan; Michael Schneider; Dongsheng Li; Hemin Zhang; Jing Mi; Alexander Bertrand; Sina Sadeghpour; Chen Wang; Huicong Liu; Christ Glorieux; Michael Kraft",
    "year": "2026",
    "publication": "Microsystems & Nanoengineering, 12, 136",
    "url": "https://www.nature.com/articles/s41378-026-01251-y",
    "access": "fulltext",
    "supports": "通过Europe PMC XML选读结构、Measurement Setup、Frequency Response、Noise Floor、Signal Fusion与Conclusion；核对14×14 mm管、19.2 V偏置、1 kHz灵敏度与SNR。论文按1 kHz噪声密度换算的数值不当作宽带A计权噪声指标；直接混合低于压电模式是反例。本站等噪声平均例子不是论文权重复刻。",
    "doi": "10.1038/s41378-026-01251-y"
  },
  "mic-dpa-specs": {
    "title": "How to read microphone specifications",
    "authors": "Eddy Bøgh Brixen",
    "year": "n.d.",
    "publication": "DPA Microphones 官方技术说明",
    "url": "https://www.dpamicrophones.com/mic-university/technology/how-to-read-microphone-specifications/",
    "access": "documentation",
    "supports": "读取Directional pattern、Sensitivity、Equivalent noise、Maximum SPL、Dynamic range与SNR相关段；采用参考条件和指标区别，不采用网页中泛化的主观响度或消费者评价。"
  },
  "mic-dpa-proximity": {
    "title": "Proximity effect in microphones explained – how it affects different sound sources",
    "authors": "Eddy Bøgh Brixen",
    "year": "n.d.",
    "publication": "DPA Microphones 官方技术说明",
    "url": "https://www.dpamicrophones.com/mic-university/background-knowledge/proximity-effect-in-microphones-explained/",
    "access": "documentation",
    "supports": "读取点／线／面源、额外幅度梯度和角度条件；不把具体乐器示例扩展为普遍声源分类。本站纯梯度点声源公式和曲线为显式假设下的独立推导，未复制产品测试曲线。"
  },
  "mic-iec61094-3": {
    "title": "IEC 61094-3:2016: Primary method for free-field calibration of laboratory standard microphones by the reciprocity technique",
    "authors": "International Electrotechnical Commission",
    "year": "2016",
    "publication": "IEC 官方标准目录",
    "url": "https://webstore.iec.ch/en/publication/25105",
    "access": "documentation",
    "supports": "核对公开范围与2016版本：复自由场灵敏度、实验室标准等适用器件、专业设备和人员条件。未获取完整标准，不转录互易实验步骤。"
  },
  "mic-iec61094-5": {
    "title": "IEC 61094-5:2016: Methods for pressure calibration of working standard microphones by comparison",
    "authors": "International Electrotechnical Commission",
    "year": "2016",
    "publication": "IEC 官方标准目录",
    "url": "https://webstore.iec.ch/en/publication/24988",
    "access": "documentation",
    "supports": "核对公开范围：工作标准／相关适用传声器的压力比较校准，参考传声器与频率条件；未读付费条款。"
  },
  "mic-iec61094-8": {
    "title": "IEC 61094-8:2012: Methods for determining the free-field sensitivity of working standard microphones by comparison",
    "authors": "International Electrotechnical Commission",
    "year": "2012",
    "publication": "IEC 官方标准目录",
    "url": "https://webstore.iec.ch/en/publication/4492",
    "access": "documentation",
    "supports": "读取公开范围：工作标准传声器自由场比较法及近似自由场与后处理条件；不据目录声称具体实验符合性。"
  },
  "mic-iec60942": {
    "title": "IEC 60942:2017: Electroacoustics – Sound calibrators",
    "authors": "International Electrotechnical Commission",
    "year": "2017",
    "publication": "IEC 官方标准目录",
    "url": "https://webstore.iec.ch/en/publication/30045",
    "access": "documentation",
    "supports": "公开范围与版本核对：LS、1、2等级声校准器，实验室及现场用途。全文付费，未获得完整条款；不把等级与某台设备合格结论混同。"
  },
  "mic-iec-calibrators": {
    "title": "MT 17 Sound calibrators",
    "authors": "IEC Technical Committee 29",
    "year": "n.d.",
    "publication": "IEC 官方工作组说明",
    "url": "https://tc29.iec.ch/groups-and-teams-within-tc29/mt-17-sound-calibrators-new/",
    "access": "documentation",
    "supports": "读取已知声压、频率、指定器件与配置、整体灵敏度检查及压力灵敏度用途说明；支持单点现场检查的用途，不声称因此已检验宽带方向响应。"
  },
  "mic-chung-2004": {
    "title": "Challenges and Recent Developments in Hearing Aids: Part I. Speech Understanding in Noise, Microphone Technologies and Noise Reduction Algorithms",
    "authors": "King Chung",
    "year": "2004",
    "publication": "Trends in Amplification, 8(3), 83–124",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4111442/",
    "access": "fulltext",
    "supports": "读取PMC正文3.1.1机制、方向性与整机声场、混响和实验室／现场差异相关段，作为早期方法背景综述；不转录临床效应量或据此推荐现代具体产品，未逐段通读整篇。",
    "doi": "10.1177/108471380400800302"
  },
  "mic-shure-sm58": {
    "title": "SM58 User Guide",
    "authors": "Shure",
    "year": "n.d.",
    "publication": "Shure 官方产品手册",
    "url": "https://www.shure.com/en-US/docs/guide/SM58",
    "access": "documentation",
    "supports": "核对Type为Dynamic (moving coil)、Polar Pattern为Cardioid、位置与近讲提示；仅用于照片型号说明和该产品特定条件，不把营销措辞或型号响应扩展为全部动圈话筒。"
  }
};
