import type { Reference } from './references';

export const strfReferences: Record<string, Reference> = {
  "strf-normalization": {
    "title": "Estimating spatio-temporal receptive fields of auditory and visual neurons from their responses to natural stimuli",
    "authors": "Frédéric E. Theunissen; Stephen V. David; Nandini C. Singh; Anne Hsu; William E. Vinje; Jack L. Gallant",
    "year": "2001",
    "publication": "Network: Computation in Neural Systems 12, 289–316",
    "url": "https://hearingbrain.org/pdf/TheunissenEtAl2001a.pdf",
    "access": "fulltext",
    "supports": "作者公开全文的方法部分：刺激—响应互相关、输入自相关及对自然刺激的估计。"
  },
  "strf-calabrese": {
    "title": "A Generalized Linear Model for Estimating Spectrotemporal Receptive Fields from Responses to Natural Sounds",
    "authors": "Ana Calabrese; Joseph W. Schumacher; David M. Schneider; Liam Paninski; Sarah M. N. Woolley",
    "year": "2011",
    "publication": "PLoS ONE 6, e16104",
    "doi": "10.1371/journal.pone.0016104",
    "url": "https://doi.org/10.1371/journal.pone.0016104",
    "access": "abstract",
    "supports": "原始研究的摘要与书目。核查斑胸草雀中脑、两类刺激、稀疏先验与归一化反向相关的比较。"
  },
  "strf-nems": {
    "title": "NEMS auditory data fitting tutorial and single-unit demonstration data",
    "authors": "Laboratory of Brain, Hearing, and Behavior",
    "year": "核查于 2026 年",
    "publication": "LBHB/NEMS，固定版本 6b979b8，TAR010c-18-2",
    "url": "https://github.com/LBHB/NEMS/blob/6b979b8233c922646b1516a6dee107bcfdb1400e/tutorials/02_auditory_data_fit.py",
    "access": "documentation",
    "supports": "与同版本的数据加载器核对采样率、训练与测试字段、A1 单元和 PSTH。实际读取固定哈希数据，以本站估计器重算。"
  },
  "strf-reliability": {
    "title": "Measuring the Performance of Neural Models",
    "authors": "Oliver Schoppe; Nicol S. Harper; Ben D. B. Willmore; Andrew J. King; Jan W. H. Schnupp",
    "year": "2016",
    "publication": "Frontiers in Computational Neuroscience 10, 10",
    "doi": "10.3389/fncom.2016.00010",
    "url": "https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2016.00010/full",
    "access": "fulltext",
    "supports": "核查原始相关、重复试次、噪声上限与模型性能指标之间的区别。"
  },
  "strf-gain": {
    "title": "Contrast Gain Control in Auditory Cortex",
    "authors": "Neil C. Rabinowitz; Ben D. B. Willmore; Jan W. H. Schnupp; Andrew J. King",
    "year": "2011",
    "publication": "Neuron 70, 1178–1191",
    "doi": "10.1016/j.neuron.2011.04.030",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3133688/",
    "access": "fulltext",
    "supports": "原研究对比雪貂不同谱时对比度下的响应及输出曲线，支持背景依赖增益。"
  },
  "strf-wingert": {
    "title": "Convolutional neural network models describe the encoding subspace of local circuits in auditory cortex",
    "authors": "Jereme C. Wingert; Satyabrata Parida; Sam V. Norman-Haignere; Stephen V. David",
    "year": "2026",
    "publication": "Nature Neuroscience 29, 876–887",
    "doi": "10.1038/s41593-026-02216-0",
    "url": "https://www.nature.com/articles/s41593-026-02216-0",
    "access": "abstract",
    "supports": "核对正式期刊版摘要与书目。雪貂自然声音记录、CNN 提取多轴子空间及非线性组合。"
  }
};
