import type { Reference } from './references';

export const auditoryModelReferences: Record<string, Reference> = {
  "acm-comparison": {
    "title": "A comparative study of eight human auditory models of monaural processing",
    "authors": "Alejandro Osses Vecchi; Léo Varnet; Laurel H. Carney; Torsten Dau; Ian C. Bruce; Sarah Verhulst; Piotr Majdak",
    "year": "2022",
    "publication": "Acta Acustica, 6, 17",
    "doi": "10.1051/aacus/2022008",
    "url": "https://doi.org/10.1051/aacus/2022008",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要、机构原文首页及可访问Introduction与模型分类相关段：八个单耳模型比较，输出与配置可比性；不是所有模型的完整排名。"
  },
  "acm-amt": {
    "title": "AMT 1.x: A toolbox for reproducible research in auditory modeling",
    "authors": "Piotr Majdak; Clara Hollomey; Robert Baumgartner",
    "year": "2022",
    "publication": "Acta Acustica, 6, 19",
    "doi": "10.1051/aacus/2022011",
    "url": "https://doi.org/10.1051/aacus/2022011",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：AMT的文档、数据、demonstrations与experiments复现组织；数量为2022论文背景，不当作当前模型总数。"
  },
  "acm-mechanics": {
    "title": "Mechanics of the Mammalian Cochlea",
    "authors": "Luis Robles; Mario A. Ruggero",
    "year": "2001",
    "publication": "Physiological Reviews, 81, 3, 1305-1352",
    "doi": "10.1152/physrev.2001.81.3.1305",
    "url": "https://doi.org/10.1152/physrev.2001.81.3.1305",
    "access": "abstract",
    "supports": "2026-10-10：原始综述摘要：哺乳类基底膜行波、级依赖调谐和压缩；用于生理目标，不将教学幂律视作完整耳蜗。"
  },
  "acm-erb": {
    "title": "Derivation of auditory filter shapes from notched-noise data",
    "authors": "Brian R Glasberg; Brian C.J Moore",
    "year": "1990",
    "publication": "Hearing Research, 47, 1-2, 103-138",
    "doi": "10.1016/0378-5955(90)90170-T",
    "url": "https://doi.org/10.1016/0378-5955(90)90170-T",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：凹口噪声反推滤波器，非对称、耳机/外中耳传递与离频聆听影响；不把拟合功率形状等同完整时域处理。"
  },
  "acm-meddis": {
    "title": "Simulation of mechanical to neural transduction in the auditory receptor",
    "authors": "Ray Meddis",
    "year": "1986",
    "publication": "The Journal of the Acoustical Society of America, 79, 3, 702-711",
    "doi": "10.1121/1.393460",
    "url": "https://doi.org/10.1121/1.393460",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：递质释放、回收与损失假设，放电及适应现象；不将功能拟合视为唯一突触机制。"
  },
  "acm-zilany": {
    "title": "Updated parameters and expanded simulation options for a model of the auditory periphery",
    "authors": "Muhammad S. A. Zilany; Ian C. Bruce; Laurel H. Carney",
    "year": "2014",
    "publication": "The Journal of the Acoustical Society of America, 135, 1, 283-286",
    "doi": "10.1121/1.4837815",
    "url": "https://doi.org/10.1121/1.4837815",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：猫外周现象模型的参数与均值/方差改进、不应期影响；物种及输出方式需按实现核对。"
  },
  "acm-bruce": {
    "title": "A phenomenological model of the synapse between the inner hair cell and auditory nerve: Implications of limited neurotransmitter release sites",
    "authors": "Ian C. Bruce; Yousof Erfani; Muhammad S.A. Zilany",
    "year": "2018",
    "publication": "Hearing Research, 360, 40-54",
    "doi": "10.1016/j.heares.2017.12.016",
    "url": "https://doi.org/10.1016/j.heares.2017.12.016",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：有限释放位点模型整合入Zilany外周前端，放电统计与前向掩蔽改进；未报告人类临床诊断性能。"
  },
  "acm-verhulst": {
    "title": "Computational modeling of the human auditory periphery: Auditory-nerve responses, evoked potentials and hearing loss",
    "authors": "Sarah Verhulst; Alessandro Altoè; Viacheslav Vasilkov",
    "year": "2018",
    "publication": "Hearing Research, 360, 55-75",
    "doi": "10.1016/j.heares.2017.12.018",
    "url": "https://doi.org/10.1016/j.heares.2017.12.018",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：人类外周—脑干模型、IHC/AN与群体ABR/EFR验证、增益损失与突触病变模拟；不将逆问题写成个体唯一诊断。"
  },
  "acm-dau": {
    "title": "Modeling auditory processing of amplitude modulation. I. Detection and masking with narrow-band carriers",
    "authors": "Torsten Dau; Birger Kollmeier; Armin Kohlrausch",
    "year": "1997",
    "publication": "The Journal of the Acoustical Society of America, 102, 5, 2892-2905",
    "doi": "10.1121/1.420344",
    "url": "https://doi.org/10.1121/1.420344",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：调制滤波器组、窄带噪声调制检测与掩蔽；阈值和载波限制，不把调制通道视为已确认的特定细胞。"
  },
  "acm-jeffress": {
    "title": "A place theory of sound localization.",
    "authors": "Lloyd A. Jeffress",
    "year": "1948",
    "publication": "Journal of Comparative and Physiological Psychology, 41, 1, 35-39",
    "doi": "10.1037/h0061495",
    "url": "https://doi.org/10.1037/h0061495",
    "access": "metadata",
    "supports": "2026-10-10：Crossref与PubMed书目核对，用于1948年声音定位理论的历史节点；延迟线相关结构解释另据Breebaart原始摘要。"
  },
  "acm-durlach": {
    "title": "Equalization and Cancellation Theory of Binaural Masking-Level Differences",
    "authors": "N. I. Durlach",
    "year": "1963",
    "publication": "The Journal of the Acoustical Society of America, 35, 8, 1206-1218",
    "doi": "10.1121/1.1918675",
    "url": "https://doi.org/10.1121/1.1918675",
    "access": "abstract",
    "supports": "2026-10-10：Crossref所存原始摘要：均衡与相消、内部误差、指定双耳掩蔽刺激；不推广为全脑唯一双耳处理。"
  },
  "acm-breebaart": {
    "title": "Binaural processing model based on contralateral inhibition. I. Model structure",
    "authors": "Jeroen Breebaart; Steven van de Par; Armin Kohlrausch",
    "year": "2001",
    "publication": "The Journal of the Acoustical Society of America, 110, 2, 1074-1088",
    "doi": "10.1121/1.1383297",
    "url": "https://doi.org/10.1121/1.1383297",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：左右外周、对侧抑制、双耳内部表征与中心决策；双耳延迟/级差与检测读出。"
  },
  "acm-breebaart-test": {
    "title": "Binaural processing model based on contralateral inhibition. III. Dependence on temporal parameters",
    "authors": "Jeroen Breebaart; Steven van de Par; Armin Kohlrausch",
    "year": "2001",
    "publication": "The Journal of the Acoustical Society of America, 110, 2, 1105-1117",
    "doi": "10.1121/1.1383299",
    "url": "https://doi.org/10.1121/1.1383299",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：固定参数的三间隔虚拟观察者、时间条件及模型未能覆盖的周期ITD和带宽相关差异阈。"
  },
  "acm-sepsm": {
    "title": "Predicting speech intelligibility based on the signal-to-noise envelope power ratio after modulation-frequency selective processing",
    "authors": "Søren Jørgensen; Torsten Dau",
    "year": "2011",
    "publication": "The Journal of the Acoustical Society of America, 130, 3, 1475-1487",
    "doi": "10.1121/1.3621502",
    "url": "https://doi.org/10.1121/1.3621502",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要与作者机构摘要：调制域SNRenv和理想观察者、稳态语音形噪声/混响/谱减条件；不推广为全部语言和背景。"
  },
  "acm-stoi": {
    "title": "An Algorithm for Intelligibility Prediction of Time–Frequency Weighted Noisy Speech",
    "authors": "Cees H. Taal; Richard C. Hendriks; Richard Heusdens; Jesper Jensen",
    "year": "2011",
    "publication": "IEEE Transactions on Audio, Speech, and Language Processing, 19, 7, 2125-2136",
    "doi": "10.1109/TASL.2011.2114881",
    "url": "https://doi.org/10.1109/TASL.2011.2114881",
    "access": "abstract",
    "supports": "2026-10-10：作者机构原始PDF检索可见第一页摘要及Crossref书目：STOI与含时频加权的噪声言语实验相关；原文直接打开失败，未宣称阅读全文。"
  },
  "acm-haspi": {
    "title": "The Hearing-Aid Speech Perception Index (HASPI) Version 2",
    "authors": "James M. Kates; Kathryn H. Arehart",
    "year": "2021",
    "publication": "Speech Communication, 131, 35-46",
    "doi": "10.1016/j.specom.2020.05.001",
    "url": "https://doi.org/10.1016/j.specom.2020.05.001",
    "access": "abstract",
    "supports": "2026-10-10：出版方原始摘要及检索可见方法介绍：HASPI v2外周听损、参考/处理信号、包络调制与网络映射；仅核对相关可见段，未宣称完整原文阅读。"
  },
  "acm-model-matched": {
    "title": "Neural responses to natural and model-matched stimuli reveal distinct computations in primary and nonprimary auditory cortex",
    "authors": "Sam V. Norman-Haignere; Josh H. McDermott",
    "year": "2018",
    "publication": "PLOS Biology, 16, 12, e2005127",
    "doi": "10.1371/journal.pbio.2005127",
    "url": "https://doi.org/10.1371/journal.pbio.2005127",
    "access": "fulltext",
    "supports": "2026-10-10：PLOS原文Abstract、Author summary、Introduction及Results方法假设：自然/模型匹配刺激与初级/非初级fMRI差异，保留池化与匹配范围。"
  },
  "acm-kell": {
    "title": "A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy",
    "authors": "Alexander J.E. Kell; Daniel L.K. Yamins; Erica N. Shook; Sam V. Norman-Haignere; Josh H. McDermott",
    "year": "2018",
    "publication": "Neuron, 98, 3, 630-644.e16",
    "doi": "10.1016/j.neuron.2018.03.044",
    "url": "https://doi.org/10.1016/j.neuron.2018.03.044",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：语音/音乐任务优化网络、人类错误与fMRI层级预测；网络层不是解剖脑区等同物。"
  },
  "acm-saddler": {
    "title": "Deep neural network models reveal interplay of peripheral coding and stimulus statistics in pitch perception",
    "authors": "Mark R. Saddler; Ray Gonzalez; Josh H. McDermott",
    "year": "2021",
    "publication": "Nature Communications, 12, 1",
    "doi": "10.1038/s41467-021-27366-6",
    "url": "https://doi.org/10.1038/s41467-021-27366-6",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：改变外周时域保真与训练声音统计，检验音高行为；优化任务不自动确立人脑算法。"
  },
  "acm-connear": {
    "title": "A convolutional neural-network model of human cochlear mechanics and filter tuning for real-time applications",
    "authors": "Deepak Baby; Arthur Van Den Broucke; Sarah Verhulst",
    "year": "2021",
    "publication": "Nature Machine Intelligence, 3, 2, 134-143",
    "doi": "10.1038/s42256-020-00286-8",
    "url": "https://doi.org/10.1038/s42256-020-00286-8",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要：CoNNear混合机制/神经网络、未训练的耳蜗测试刺激、级依赖调谐与加速；教师拟合和独立生理验证应区分。"
  },
  "acm-icnet": {
    "title": "Modelling neural coding in the auditory midbrain with high resolution and accuracy",
    "authors": "Fotios Drakopoulos; Lloyd Pellatt; Shievanie Sabesan; Yiqing Xia; Andreas Fragner; Nicholas A. Lesica",
    "year": "2025",
    "publication": "Nature Machine Intelligence, 7, 9, 1478-1493",
    "doi": "10.1038/s42256-025-01104-9",
    "url": "https://doi.org/10.1038/s42256-025-01104-9",
    "access": "abstract",
    "supports": "2026-10-10：原始摘要及出版方Discussion相关可见段：麻醉沙鼠下丘多单元、非平稳性、复杂声预测与限制；不视为清醒人类皮层或行为模型。"
  },
  "acm-hohmann-doc": {
    "title": "HOHMANN2002 — Invertible Gammatone filterbank",
    "authors": "Auditory Modeling Toolbox contributors",
    "year": "核对2026-10-10",
    "publication": "AMT 1.6.0 documentation",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/hohmann2002.php",
    "access": "documentation",
    "supports": "2026-10-10：官方文档：中心频率、ERB密度、阶数与带宽参数，数字实现需要验证；不将默认值写成普遍生理常数。"
  },
  "acm-verhulst-code": {
    "title": "Verhulstetal2018Model — model code version 1.2",
    "authors": "HearingTechnology / Alessandro Altoè; Sarah Verhulst and contributors",
    "year": "核对2026-10-10",
    "publication": "Author-maintained implementation",
    "url": "https://github.com/HearingTechnology/Verhulstetal2018Model",
    "access": "documentation",
    "supports": "2026-10-10：作者README：1.2版IC/CN更新及M1/M3/M5重标定、示例与许可；公开可读不意味着所有模型相同许可。"
  },
  "acm-dau-doc": {
    "title": "DAU1997 — monaural auditory internal representation",
    "authors": "Auditory Modeling Toolbox contributors",
    "year": "核对2026-10-10",
    "publication": "AMT 1.6.0 documentation",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/dau1997.php",
    "access": "documentation",
    "supports": "2026-10-10：官方接口文档：声学滤波、半波整流/低通、适应环和调制滤波的内部输出；函数调用本身不直接输出行为成绩。"
  },
  "acm-eeg-2026": {
    "title": "A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound",
    "authors": "Thomas J. Stoll; Ross K. Maddox",
    "year": "2026",
    "publication": "arXiv:2609.20595v2, 2026-09-24（预印本，未同行评审）",
    "doi": "10.48550/arXiv.2609.20595",
    "url": "https://arxiv.org/abs/2609.20595v2",
    "access": "abstract",
    "publicationType": "preprint",
    "supports": "2026-10-10：作者预印本摘要及版本页：双耳波形到连续EEG、ABR/TRF/BIC多范式验证目标；未声称会议录用或个体听损诊断有效。"
  }
};
