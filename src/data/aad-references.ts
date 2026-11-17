import type { Reference } from './references';

export const aadReferences: Record<string, Reference> = {
  'aad-review-2021': {
    title: 'Electroencephalography-Based Auditory Attention Decoding: Toward Neurosteered Hearing Devices', authors: 'Geirnaert S, Vandecappelle S, Alickovic E, de Cheveigné A, Lalor E, Meyer BT, Miran S, Francart T, Bertrand A.', year: '2021',
    publication: 'IEEE Signal Processing Magazine, 38(4), 89–102', doi: '10.1109/MSP.2021.3075932', url: 'https://simongeirnaert.com/publication/eegbased2021geirnaert/', access: 'fulltext',
    supports: '2026-11-17阅读作者页面及PDF摘要、方法框架与第12–13页决策窗口/MESD说明：算法比较和神经引导设备；MESD是基于假设的理论比较量，并非真实切换测量，不沿用旧基准的空间分类排名作为当前无偏结论。'
  },
  'aad-biesmans-2017': {
    title: 'Auditory-Inspired Speech Envelope Extraction Methods for Improved EEG-Based Auditory Attention Detection in a Cocktail Party Scenario', authors: 'Biesmans W, Das N, Francart T, Bertrand A.', year: '2017（在线2016）',
    publication: 'IEEE Transactions on Neural Systems and Rehabilitation Engineering, 25(5), 402–412', doi: '10.1109/TNSRE.2016.2571900', url: 'https://pubmed.ncbi.nlm.nih.gov/27244743/', access: 'abstract',
    supports: '2026-11-17阅读PubMed/Europe PMC原始摘要：滤波器组、幂律压缩与包络提取影响候选匹配；不把一种提取参数写成唯一生理模型。'
  },
  'aad-cnn-2021': {
    title: 'EEG-based detection of the locus of auditory attention with convolutional neural networks', authors: 'Vandecappelle S, Deckers L, Das N, Ansari AH, Bertrand A, Francart T.', year: '2021',
    publication: 'eLife, 10, e56481', doi: '10.7554/eLife.56481', url: 'https://pubmed.ncbi.nlm.nih.gov/33929315/', access: 'abstract',
    supports: '2026-11-17阅读正式期刊原始摘要：不用候选包络的左右空间注意分类。仅用于方法沿革；短窗准确率必须结合后续眼动和试次偏差研究，不照搬为真实设备效果。'
  },
  'aad-yan-2025': {
    title: 'Overestimated performance of auditory attention decoding caused by experimental design in EEG recordings', authors: 'Yan Y, Xu X, Zhu H, Li S, Wang B, Wu X, Chen J.', year: '2025',
    publication: 'Interspeech 2025, 1053–1057', doi: '10.21437/Interspeech.2025-85', url: 'https://www.isca-archive.org/interspeech_2025/yan25_interspeech.html', access: 'abstract',
    supports: '2026-11-17阅读ISCA正式摘要和书目，核对PDF首页：分块与非分块设计、深度模型性能差异及线性重建对照；没有把所有模型差异都归为泄漏，未声称复现原始数据。'
  },
  'aad-ear-2025': {
    title: 'A direct comparison of simultaneously recorded scalp, around-ear and in-ear EEG for neural selective auditory attention decoding to speech', authors: 'Geirnaert S, Kappel SL, Kidmose P.', year: '2025',
    publication: 'Scientific Reports, 15, 41655', doi: '10.1038/s41598-025-25576-2', url: 'https://pubmed.ncbi.nlm.nih.gov/41286316/', access: 'abstract',
    supports: '2026-11-17阅读Europe PMC完整原始摘要与书目：同时记录的三种电极系统、线性重建、60秒窗83.4%/67.2%/61.1%，不推广为耳内设备的固定上限或短时切换效果。出版方打开受限，未声称阅读全文。'
  },
  'aad-switch-2026': {
    title: 'An Open Non-Invasive EEG Dataset for Spontaneous Auditory Attention Switch Decoding', authors: 'Wang X, Ding Y, Ban Y, Wang L, Chen F.', year: '2026',
    publication: 'Scientific Data, 13, 883', doi: '10.1038/s41597-026-07244-w', url: 'https://pubmed.ncbi.nlm.nih.gov/41991955/', access: 'abstract',
    supports: '2026-11-17阅读Europe PMC原始摘要与书目：AASD包括维持与自发切换及基线模型。未下载数据，未核验每个事件标签的操作细节，不把基线结果当成日常闭环部署。'
  },
  'aad-miran-2018': {
    title: 'Real-Time Tracking of Selective Auditory Attention From M/EEG: A Bayesian Filtering Approach', authors: 'Miran S, Akram S, Sheikhattar A, Simon JZ, Zhang T, Babadi B.', year: '2018',
    publication: 'Frontiers in Neuroscience, 12, 262', doi: '10.3389/fnins.2018.00262', url: 'https://pubmed.ncbi.nlm.nih.gov/29765298/', access: 'abstract',
    supports: '2026-11-17阅读Europe PMC原始摘要：自适应滤波、注意标记与状态空间估计，包含固定时滞平滑；在线/近实时算法仍需报告完整延迟和真实切换验证。'
  }
};
