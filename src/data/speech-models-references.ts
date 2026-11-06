import type { Reference } from './references';

export const speechModelsReferences: Record<string, Reference> = {
  "sim-esii": {
    "title": "Extended speech intelligibility index for the prediction of the speech reception threshold in fluctuating noise",
    "authors": "K. S. Rhebergen, N. J. Versfeld, W. A. Dreschler",
    "year": "2006",
    "publication": "JASA 120, 3988–3997",
    "doi": "10.1121/1.2358008",
    "url": "https://doi.org/10.1121/1.2358008",
    "access": "abstract",
    "supports": "起伏噪声中的分时可听度预测、前向掩蔽和行为阈值验证。"
  },
  "sim-fade": {
    "title": "Sentence Recognition Prediction for Hearing-impaired Listeners in Stationary and Fluctuation Noise With FADE: Empowering the Attenuation and Distortion Concept by Plomp With a Quantitative Processing Model",
    "authors": "B. Kollmeier, M. R. Schädler, A. Warzybok, B. T. Meyer, T. Brand",
    "year": "2016",
    "publication": "Trends in Hearing 20",
    "doi": "10.1177/2331216516655795",
    "url": "https://doi.org/10.1177/2331216516655795",
    "access": "fulltext",
    "supports": "德国矩阵句任务，按信噪比训练和测试识别器、听损参数与个体 SRT。"
  },
  "sim-amt-stoi": {
    "title": "taal2011 — Short-time objective intelligibility",
    "authors": "AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/taal2011_code.php",
    "access": "documentation",
    "supports": "核对并运行使用干净与受损信号的双输入实现。"
  },
  "sim-clarity": {
    "title": "Non-intrusive Speech Intelligibility Metric Prediction for Hearing Impaired Individuals",
    "authors": "G. Close, S. Hollands, S. Goetze, T. Hain",
    "year": "2022",
    "publication": "Interspeech, 3483–3487",
    "doi": "10.21437/Interspeech.2022-10182",
    "url": "https://www.isca-archive.org/interspeech_2022/close22_interspeech.html",
    "access": "abstract",
    "supports": "对比客观指标标签与真实听者识别标签，区分训练与推断所需的信号。"
  },
  "sim-zaar": {
    "title": "Predicting speech intelligibility in hearing-impaired listeners using a physiologically inspired auditory model",
    "authors": "J. Zaar, L. H. Carney",
    "year": "2022",
    "publication": "Hearing Research 426, 108553",
    "doi": "10.1016/j.heares.2022.108553",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10560534/",
    "access": "fulltext",
    "supports": "外周非线性、基频附近的起伏、跨通道短时相关，以及正常听力与听损听者的验证范围。"
  }
};
