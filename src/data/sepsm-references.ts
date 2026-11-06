import type { Reference } from './references';

export const sepsmReferences: Record<string, Reference> = {
  "sepsm-mr": {
    "title": "A multi-resolution envelope-power based model for speech intelligibility",
    "authors": "Søren Jørgensen; Stephan D. Ewert; Torsten Dau",
    "year": "2013",
    "publication": "JASA 134, 436–446",
    "doi": "10.1121/1.4807563",
    "url": "https://pubmed.ncbi.nlm.nih.gov/23862819/",
    "access": "abstract",
    "supports": "原始摘要核查评估条件及结论；公式、窗长与图表另核对作者学位论文第 4 章。"
  },
  "sepsm-amt11": {
    "title": "joergensen2011 — model source",
    "authors": "AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/joergensen2011_code.php",
    "access": "documentation",
    "supports": "实际核查并运行主函数。调制频带、DC 归一化和功率下限以执行语句为准。"
  },
  "sepsm-amt13": {
    "title": "joergensen2013 — model source",
    "authors": "AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/joergensen2013_code.php",
    "access": "documentation",
    "supports": "核查并运行分窗、功率限制和积分代码。阅读可选理想观察者分支；本站计算仅使用 SNRenv 输出。"
  },
  "sepsm-thesis": {
    "title": "Modeling speech intelligibility based on the signal-to-noise envelope power ratio",
    "authors": "Søren Jørgensen",
    "year": "2014",
    "publication": "Technical University of Denmark, Contributions to Hearing Research 15",
    "url": "https://orbit.dtu.dk/files/89308152/S%C3%B8ren_J%C3%B8rgensen_PhDThesis2014.pdf",
    "access": "fulltext",
    "supports": "作者学位论文第 2、4 章，尤其是图 4.3–4.5、整合次序、有效调制通道以及局限。与原论文属同一研究系列。"
  },
  "sepsm-demo": {
    "title": "demo_joergensen2013 — example with CLUE sentences",
    "authors": "AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/demos/demo_joergensen2013_code.php",
    "access": "documentation",
    "supports": "核查参考材料、输入声级约定和仅适用于 CLUE 示例的观察者参数。"
  },
  "sepsm-corr": {
    "title": "Predicting speech intelligibility based on a correlation metric in the envelope power spectrum domain",
    "authors": "Helia Relaño-Iborra; Tobias May; Johannes Zaar; Christoph Scheidiger; Torsten Dau",
    "year": "2016",
    "publication": "JASA 140, 2670–2679",
    "doi": "10.1121/1.4964505",
    "url": "https://pubmed.ncbi.nlm.nih.gov/27794330/",
    "access": "abstract",
    "supports": "原始研究的摘要，对比相位抖动、理想时频分离、起伏干扰及混响，并报告该变体的局限。"
  },
  "sepsm-periodicity": {
    "title": "Predicting the effects of periodicity on the intelligibility of masked speech: An evaluation of different modelling approaches and their limitations",
    "authors": "Kurt Steinmetzger; Johannes Zaar; Helia Relaño-Iborra; Stuart Rosen; Torsten Dau",
    "year": "2019",
    "publication": "JASA 146, 2562–2576",
    "doi": "10.1121/1.5129050",
    "url": "https://doi.org/10.1121/1.5129050",
    "access": "fulltext",
    "supports": "同组材料下比较功率与相关后端，检验周期性掩蔽声条件及前端分辨能力。"
  },
  "sepsm-jansen": {
    "title": "Advantages of Fluctuating Noise for Measuring Speech Intelligibility in Listeners With Hearing Loss",
    "authors": "Theresa Jansen; Kirsten C. Wagener; Inga Holube; Laura Hartog; Christopher F. Hauth; Saskia Ibelings; Jonte Kriebel; Dirk Oetting",
    "year": "2026",
    "publication": "Trends in Hearing 30",
    "doi": "10.1177/23312165261464687",
    "url": "https://pubmed.ncbi.nlm.nih.gov/42389812/",
    "access": "abstract",
    "supports": "人体测量的对照条件同时改变掩蔽声起伏与空间位置；仅用于说明模型推广需要哪些控制。"
  }
};
