import type { Reference } from './references';

const book=(section:string,title:string,supports:string):Reference=>({title,authors:'Wulfram Gerstner; Werner M. Kistler; Richard Naud; Liam Paninski',year:'2014',publication:'Neuronal Dynamics, Cambridge University Press / EPFL author-hosted online edition, '+section.replace('.S','.'),url:'https://neuronaldynamics.epfl.ch/online/Ch'+section+'.html',access:'fulltext',supports});

export const computationalNeuroscienceReferences: Record<string, Reference> = {
  'cn-intro':book('1.S1','Elements of Neuronal Systems','读取理想脉冲神经元、脉冲列与突触术语；正文不重复旧版中胶质不参与信息处理等过度概括，不把事件模型当所有细胞的描述。'),
  'cn-lif':book('1.S3','Integrate-And-Fire Models','读取被动RC、时间常数、阈值、复位与恒定输入解。100 MΩ、200 pF及不应期参数为本站设定，发放率解析式自主推导。'),
  'cn-lif-limits':book('1.S4','Limitations of the Leaky Integrate-and-Fire Model','读取适应、反跳、分流与空间结构限制；不将普通LIF宣称为自然产生全部神经元发放型态。'),
  'cn-hh-original':{title:'A quantitative description of membrane current and its application to conduction and excitation in nerve',authors:'A. L. Hodgkin; A. F. Huxley',year:'1952',publication:'The Journal of Physiology, 117(4), 500–544',doi:'10.1113/jphysiol.1952.sp004764',url:'https://isn.ucsd.edu/courses/beng207/reading/Hodgkin_Huxley_1952_jp.pdf',access:'fulltext',supports:'读取原始论文开篇与电流/门控数学形式，明确来自鱿鱼巨轴突实验；正文不混合1952电压原点与后世绝对电压参数，不复制原始图或数值。'},
  'cn-hh-equations':book('2.S2','Hodgkin-Huxley Model','读取电流守恒、m³h与n⁴、门控动力学及单位面积参数。该网页表格采用特定皮层参数，正文不误称为原始鱿鱼参数。'),
  'cn-synapses':book('3.S1','Synapses','读取电导乘驱动力与指数突触核，分清向外/向内电流的符号。本站分流阶跃为被动模型，未模拟动作电位。'),
  'cn-compartments':book('3.S4','Compartmental Models','读取树突空间离散、相邻隔室轴向耦合与参数复杂性；不宣称所有详细模型都必须把活性通道限于胞体。'),
  'cn-rate':book('7.S2','Mean Firing Rate','读取时间计数、跨重复PSTH、群体平均及Fano因子，分别说明平均方式和窗口。'),
  'cn-isi':book('7.S3','Interval distribution and coefficient of variation','读取ISI、平均间隔与CV；齐次Poisson的指数间隔和CV=1只按指定模型使用。'),
  'cn-likelihood':book('9.S2','Likelihood of a spike train','读取连续时间强度、事件乘积与积分补偿项、离散生存概率；正文明确计数Poisson与0/1事件的区别。'),
  'cn-glm':book('10.S2','Statistical Formulation of Encoding Models','读取条件分布、最大似然、正则化和历史耦合扩展。带脉冲历史的条件强度模型不称为具有无条件独立增量的Poisson过程。'),
  'cn-encoding':book('11.S2','Encoding Models in Systems Neuroscience','读取LNP、感受野与历史滤波；听觉时频核为原创指定权重，不将负权重等同抑制性突触。'),
  'cn-strf':{title:'Spectral-temporal receptive fields of nonlinear auditory neurons obtained using natural sounds',authors:'Frédéric E. Theunissen; Kamal Sen; Allison J. Doupe',year:'2000',publication:'The Journal of Neuroscience, 20(6), 2315–2331',doi:'10.1523/JNEUROSCI.20-06-02315.2000',url:'https://pubmed.ncbi.nlm.nih.gov/10704507/',access:'abstract',supports:'读取原始摘要：鸟类听觉前脑，鸟鸣与随机音点条件下STRF差异及预测；不据摘要复述未核验样本数或把鸟类结果当人类皮层定论。'},
  'cn-decoding':book('11.S3','Decoding','读取编码模型贝叶斯反演、刺激先验与读出条件；两Poisson模型的决策界与准确率为独立教学计算。'),
  'cn-rates':book('15.S3','Rate models','读取Wilson–Cowan类活动方程、增益与瞬态近似；率模型不自动保持完整脉冲网络的瞬态与稳定性。'),
  'cn-stability':book('4.S3','Phase plane analysis','读取固定点、零流线、Jacobian及特征值实部判断。正文分别限定局部线性化与非线性全局行为。'),
  'cn-hebb':book('19.S2','Models of Hebbian learning','读取局部共同活动、Oja约束和配对STDP模型；双指数参数为本站设定，未伪装成实验拟合。'),
  'cn-bi-poo':{title:'Synaptic modifications in cultured hippocampal neurons: dependence on spike timing, synaptic strength, and postsynaptic cell type',authors:'Guo-qiang Bi; Mu-ming Poo',year:'1998',publication:'The Journal of Neuroscience, 18(24), 10464–10472',doi:'10.1523/JNEUROSCI.18-24-10464.1998',url:'https://pubmed.ncbi.nlm.nih.gov/9852584/',access:'abstract',supports:'读取原始摘要中培养大鼠海马神经元、时序、初始突触强度与靶细胞类型依赖；不把pre-before-post增强宣布为所有突触共同规律。'},
  'cn-reward':book('19.S4','Reward-based learning','读取行为成功信号、延迟信用分配与资格迹；正文以抽象奖励调节规则解释，不将某个调节变量直接等同所有多巴胺活动。'),
  'cn-validation':book('10.S3','Evaluating Goodness-of-fit','读取独立测试集、过拟合、脉冲似然、时间重标度与多指标检验。本文留出计数模型只验证指定生成过程。'),
  'cn-rescaling':{title:'The time-rescaling theorem and its application to neural spike train data analysis',authors:'Emery N. Brown; Riccardo Barbieri; Valérie Ventura; Robert E. Kass; Loren M. Frank',year:'2002',publication:'Neural Computation, 14(2), 325–346',doi:'10.1162/08997660252741149',url:'https://pubmed.ncbi.nlm.nih.gov/11802915/',access:'abstract',supports:'核对原始摘要和正式DOI：条件强度积分变换与拟合优度应用；理论细节另据EPFL 10.3，不声称仅凭一张检验图证明模型为真。'},
  'cn-brian-units':{title:'Physical units',authors:'Brian 2 developers',year:'访问于2026-11-02',publication:'Brian 2 official documentation',url:'https://brian2.readthedocs.io/en/stable/user/units.html',access:'documentation',supports:'读取物理量、SI前缀及维度不匹配检查；正文NumPy例子使用显式SI转换，未依赖未安装Brian或声称官方示例即本站代码。'},
  'cn-coding':book('7.S6','The Problem of Neural Coding','读取计数、跨重复平均与下游可利用读出的区别；不把实验者能估计的PSTH直接当脑内可用信号。'),
};
