import type { Reference } from './references';

const course = 'https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-spring-2006/';
const lecture = (title: string, file: string, supports: string): Reference => ({
  title, authors: 'Munther A. Dahleh; MIT OpenCourseWare', year: '2006',
  publication: 'MIT 6.041 / 6.431 Probabilistic Systems Analysis and Applied Probability',
  url: course + file, access: 'fulltext', supports,
});
const scipy = (name: string, supports: string): Reference => ({
  title: `scipy.stats.${name}`, authors: 'SciPy contributors', year: '访问于2026-11-01',
  publication: 'SciPy 官方文档', url: `https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.${name}.html`,
  access: 'documentation', supports,
});
export const probabilityTheoryReferences: Record<string, Reference> = {
  'prob-mit-models': lecture('Lecture 1: Probability Models and Axioms', 'e93a3d8242ae1c6e75f7ea9c0a2aa3bf_lec01.pdf', '读取样本空间、事件、公理及模型与现实区别相关讲义正文；听觉四格样本空间与概率数值为原创设定。'),
  'prob-mit-bayes': lecture('Lecture 2: Conditioning and Bayes’ Rule', 'cb76456ea51cc93d2a50452b3be9ddc6_lec02.pdf', '读取条件概率、全概率、贝叶斯与决策段落；有声/报告有声的教学表及先验变化曲线为独立计算，不是原讲义雷达数据。'),
  'prob-mit-independence': lecture('Lecture 3: Independence', '742af76fecc70951d06ca0fca77c4b13_lec03.pdf', '读取独立事件、条件化可改变独立性及整组独立相关正文；听者层级反应例为本站自主推导。'),
  'prob-mit-discrete': lecture('Lecture 5: Discrete Random Variables, PMFs and Expectations', '965eca66579cdce0556d578f7bc69e58_lec05.pdf', '读取随机变量、实现值、概率质量、二项变量及期望段落；40试次例的组合计数、矩与概率由数学公式和独立数值核对。'),
  'prob-mit-continuous': lecture('Lecture 8: Continuous Random Variables I', 'a376cbc00b176ce0efd7202248e6bcb7_lec08.pdf', '读取可检索的连续变量、PDF、CDF与期望主题；密度归一化、正态积分和声压单位另用SciPy官方定义及独立积分核对，不宣称从文本提取缺失的公式。'),
  'prob-mit-conditional-moments': lecture('Lecture 13: Iterated Expectations and Conditional Variance', '2fdbe66e754da70976262f31e9be3f7b_lec13.pdf', '读取条件期望、迭代期望和条件方差相关正文；全方差恒等式与两类听者反应例为本站展开推导及枚举核对。'),
  'prob-mit-covariance': lecture('Lecture 14: Prediction, Covariance and Correlation', 'ae6088f5d8ade5c8bbbe779d8de73fab_lec14.pdf', '读取协方差、相关、不相关不推出独立及相关变量和的方差段落；平均降噪、共享噪声与零协方差反例独立推导。'),
  'prob-mit-lln': lecture('Lecture 15: Weak Law of Large Numbers', '77258a6b71c4a22502f11ddc7858b0a0_lec15.pdf', '读取依概率收敛、独立同分布有限矩及Chebyshev段落；累计正确率图为固定随机种子的教学模拟。'),
  'prob-mit-clt': lecture('Lecture 22: Central Limit Theorem', '76e66ae14d4a88936b9b3922cfc6f31a_lec22.pdf', '读取标准化、有限方差和CDF收敛而非PMF/PDF收敛的说明；正文图用二项精确概率质量除以网格间距，仅作形状比较。'),
  'prob-scipy-binom': scipy('binom', '核对二项分布支持集、PMF及sf接口；本站用组合数直接求和独立验证尾概率，不把模拟序列当作指定30/40的实测数据。'),
  'prob-scipy-poisson': scipy('poisson', '核对泊松分布PMF与参数；声事件计数仅为假定齐次泊松过程的教学模型，不将真实神经放电说成普遍满足独立增量。'),
  'prob-scipy-beta': scipy('beta', '核对Beta密度、形状参数及ppf；Beta-Binomial更新由正文将先验与似然相乘自主推导，数值积分另行核验。'),
  'prob-heeger-sdt': {title: 'Signal Detection Theory', authors: 'David Heeger', year: '访问于2026-11-01', publication: 'New York University，作者课程讲义', url: 'https://www.cns.nyu.edu/~david/handouts/sdt/sdt.html', access: 'fulltext', supports: '读取内部证据分布、判据、命中/虚报和ROC解释；等方差高斯的d′=1.5以及两间隔差变量公式为本文原创解析例，不声称拟合真实听者。'},
  'prob-mit-process': {title: 'Signals, Systems and Inference — Chapter 9: Random Processes', authors: 'Alan V. Oppenheim; George C. Verghese', year: '2010', publication: 'MIT 6.011 课程完整讲义，第9章及10.2.3节', url: 'https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/a6bddaee5966f6e73450e6fe79ab0566_MIT6_011S10_notes.pdf', access: 'fulltext', supports: '读取第9章过程实现、联合高斯、宽平稳、遍历性及10.2.3的白/有色与整形滤波段落；AR(1)协方差和共享偏置例为本文独立推导，不声称阅读全文250页。'},
};
