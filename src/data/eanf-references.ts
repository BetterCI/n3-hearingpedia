import type { Reference } from './references';

export const eanfReferences: Record<string, Reference> = {
  "eanf-rattay": {
    "title": "A model of the electrically excited human cochlear neuron. I. Contribution of neural substructures to the generation and propagation of spikes",
    "authors": "Rattay F, Lutter P, Felix H.",
    "year": "2001",
    "publication": "Hear Res 153, 43-63",
    "doi": "10.1016/s0378-5955(00)00256-2",
    "url": "https://doi.org/10.1016/s0378-5955(00)00256-2",
    "access": "abstract",
    "supports": "原始摘要：人耳蜗神经元亚结构、起始位置、传播和外周突丢失。"
  },
  "eanf-comparison": {
    "title": "Comparison of Multi-Compartment Cable Models of Human Auditory Nerve Fibers",
    "authors": "Bachmaier R, Encke J, Obando-Leitón M, Hemmert W, Bai S.",
    "year": "2019",
    "publication": "Front Neurosci 13, 1173",
    "doi": "10.3389/fnins.2019.01173",
    "url": "https://doi.org/10.3389/fnins.2019.01173",
    "access": "fulltext",
    "supports": "核查共同模拟框架、节点电极位置、单脉冲阈值定义、表 1 及模型间差异。"
  },
  "eanf-goldwyn": {
    "title": "A point process framework for modeling electrical stimulation of the auditory nerve",
    "authors": "Goldwyn JH, Rubinstein JT, Shea-Brown E.",
    "year": "2012",
    "publication": "J Neurophysiol 108, 1430-1452",
    "doi": "10.1152/jn.00095.2012",
    "url": "https://doi.org/10.1152/jn.00095.2012",
    "access": "fulltext",
    "supports": "核查条件强度、相对离散度、时值、时间抖动与成对脉冲约束的定义。"
  },
  "eanf-alifp": {
    "title": "An Adaptive Leaky-Integrate and Firing Probability Model of an Electrically Stimulated Auditory Nerve Fiber",
    "authors": "Felsheim RC, Dietz M.",
    "year": "2024",
    "publication": "Trends Hear 28, 23312165241286742",
    "doi": "10.1177/23312165241286742",
    "url": "https://doi.org/10.1177/23312165241286742",
    "access": "fulltext",
    "supports": "模型论文及作者公开全文。核查概率混合表示、条件时间分布、时间效应和物种验证范围。"
  },
  "eanf-miller": {
    "title": "Electrically evoked single-fiber action potentials from cat: responses to monopolar, monophasic stimulation",
    "authors": "Miller CA, Abbas PJ, Robinson BK, Rubinstein JT, Matsuoka AJ.",
    "year": "1999",
    "publication": "Hear Res 130, 197-218",
    "doi": "10.1016/s0378-5955(99)00012-x",
    "url": "https://doi.org/10.1016/s0378-5955(99)00012-x",
    "access": "abstract",
    "supports": "猫单纤维、单极单相刺激、潜伏期与抖动，用于说明兴奋部位推断需保留实验条件。"
  },
  "eanf-heffer": {
    "title": "Examining the auditory nerve fiber response to high rate cochlear implant stimulation: chronic sensorineural hearing loss and facilitation",
    "authors": "Heffer LF, Sly DJ, Fallon JB, White MW, Shepherd RK, O'Leary SJ.",
    "year": "2010",
    "publication": "J Neurophysiol 104, 3124-3135",
    "doi": "10.1152/jn.00500.2010",
    "url": "https://doi.org/10.1152/jn.00500.2010",
    "access": "abstract",
    "supports": "原始豚鼠高脉率脉冲列、不同耳聋历程及易化实验，和 2026 年再分析使用同一记录系列。"
  },
  "eanf-individual": {
    "title": "Towards model-based characterization of individual electrically stimulated nerve fibers",
    "authors": "Felsheim RC, Sly DJ, O'Leary SJ, Dietz M.",
    "year": "2026",
    "publication": "PLoS Comput Biol 22, e1013342",
    "doi": "10.1371/journal.pcbi.1013342",
    "url": "https://doi.org/10.1371/journal.pcbi.1013342",
    "access": "fulltext",
    "supports": "原始记录系列、筛选后 118 条纤维、模型局限段及误差较大的响应模式。"
  },
  "eanf-briaire": {
    "title": "Unraveling the electrically evoked compound action potential",
    "authors": "Briaire JJ, Frijns JH.",
    "year": "2005",
    "publication": "Hear Res 205, 143-156",
    "doi": "10.1016/j.heares.2005.03.020",
    "url": "https://doi.org/10.1016/j.heares.2005.03.020",
    "access": "abstract",
    "supports": "原始摘要：单纤维波形对记录 eCAP 的贡献及传播解释的边界。"
  },
  "eanf-cap": {
    "title": "A Computational Model of the Electrically or Acoustically Evoked Compound Action Potential in Cochlear Implant Users With Residual Hearing",
    "authors": "Kipping D, Zhang Y, Nogueira W.",
    "year": "2024",
    "publication": "IEEE Trans Biomed Eng 71, 3192-3203",
    "doi": "10.1109/tbme.2024.3410686",
    "url": "https://doi.org/10.1109/tbme.2024.3410686",
    "access": "abstract",
    "supports": "正式期刊摘要：三维场、单神经元事件与记录贡献，以及人类数据对照和绝对幅度偏差。"
  },
  "eanf-eas": {
    "title": "A Computational Model of a Single Auditory Nerve Fiber for Electric-Acoustic Stimulation",
    "authors": "Kipping D, Nogueira W.",
    "year": "2022",
    "publication": "J Assoc Res Otolaryngol 23, 835-858",
    "doi": "10.1007/s10162-022-00870-2",
    "url": "https://doi.org/10.1007/s10162-022-00870-2",
    "access": "fulltext",
    "supports": "核对声电耦合与非耦合模型及对起始响应预测的局限。"
  },
  "eanf-amt": {
    "title": "felsheim2024 — model implementation",
    "authors": "Rebecca C. Felsheim; AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/models/felsheim2024_code.php",
    "access": "documentation",
    "supports": "与执行文件逐行核对（忽略行尾）；阴极触发、膜滤波、路径合并、逐脉冲分布。另核对本版本默认参数文件。"
  },
  "eanf-demo": {
    "title": "demo_felsheim2024 — demonstration of aLIFP",
    "authors": "Rebecca C. Felsheim; AMT contributors",
    "year": "核查于 2026 年",
    "publication": "Auditory Modeling Toolbox 1.6.0",
    "url": "https://amtoolbox.org/amt-1.6.0/doc/demos/demo_felsheim2024_code.php",
    "access": "documentation",
    "supports": "核查示例数值标度和 1 MHz 采样率；同版绘图函数将输入乘以 1,000 后标 mA。"
  }
};
