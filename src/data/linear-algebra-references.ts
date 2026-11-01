import type { Reference } from './references';

const mit = (title: string, path: string, supports: string): Reference => ({
  title, authors: 'Gilbert Strang; MIT OpenCourseWare', year: '2011',
  publication: 'MIT 18.06SC Linear Algebra', url: `https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/${path}`,
  access: 'fulltext', supports,
});
const numpy = (name: string, supports: string): Reference => ({
  title: `numpy.linalg.${name}`, authors: 'NumPy developers', year: '访问于2026-11-01',
  publication: 'NumPy 官方文档', url: `https://numpy.org/doc/stable/reference/generated/numpy.linalg.${name}.html`,
  access: 'documentation', supports,
});

export const linearAlgebraReferences: Record<string, Reference> = {
  'la-numpy-cond': numpy('cond', '核对二范数条件数及默认 SVD 计算；对称混合矩阵的模式增益和误差放大由本文自主推导。'),
  'la-numpy-solve': numpy('solve', '核对满秩方阵线性方程求解与不满足条件时的接口边界；正文不显式求逆。'),
  'la-numpy-qr': numpy('qr', '核对 reduced 模式的 Q、R 形状；本地将薄 QR 解与 lstsq 的反射模型估计逐项比较。'),
  'la-boyd-regularized': {title: 'Lecture 7: Regularized least-squares and Gauss-Newton method', authors: 'Stephen Boyd', year: '2007', publication: 'Stanford EE263 Autumn 2007–08', url: 'https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/ls-reg.pdf', access: 'fulltext', supports: '读取第1—11页的多目标、增广与正则化最小二乘内容；正文声学矩阵、模式权重推导和数值对照为原创，未使用后半部分 Gauss–Newton 内容。'},
  'la-smith-windowing': {title: 'Spectrum Analysis of a Sinusoid: Windowing, Zero-Padding, and FFT', authors: 'Julius O. Smith III', year: '访问于2026-11-01', publication: 'Mathematics of the DFT，作者在线教材', url: 'https://www.dsprelated.com/freebooks/mdft/Spectrum_Analysis_Sinusoid_Windowing.html', access: 'fulltext', supports: '读取矩形截取、加窗和补零分析段落；本文8点和80点非正交对照及加权Gram表达式为自主计算，不把已知频率拟合等同普遍频率分辨能力。'},
  'la-smith-dft': {title: 'Derivation of the Discrete Fourier Transform (DFT)', authors: 'Julius O. Smith III', year: '访问于2026-11-01', publication: 'Mathematics of the DFT，作者在线教材', url: 'https://www.dsprelated.com/freebooks/mdft/DFT_Derived.html', access: 'fulltext', supports: '读取投影、正弦基与DFT坐标解释；正文八点纯音、幅值、图和音频为本站原创教学计算。'},
  'la-smith-orthogonality': {title: 'Orthogonality of the DFT Sinusoids', authors: 'Julius O. Smith III', year: '访问于2026-11-01', publication: 'Mathematics of the DFT，作者在线教材', url: 'https://www.dsprelated.com/freebooks/mdft/Orthogonality_DFT_Sinusoids.html', access: 'fulltext', supports: '读取N点DFT复指数基的正交推导；结合前章核对有限窗整周期条件，不把任意不同频率的有限片段一概视为正交。'},
  'la-mit-syllabus': mit('18.06SC Linear Algebra: Syllabus', 'pages/syllabus/', '核对课程主题与学习材料组织；本文的听觉研究学习优先级由本站提出，不是 MIT 的听觉课程要求。'),
  'la-mit-basis': mit('Independence, basis, and dimension', '0bbc30e3f1d7933ea07a2d2e9ab050d9_MIT18_06SCF11_Ses1.9sum.pdf', '读取讲义全文，核对线性无关、基、秩与零空间；重复通道的例子为自主教学推导。'),
  'la-mit-projection': mit('Projection matrices and least squares', '198bde3a6536b62989b6cc09495575c1_MIT18_06SCF11_Ses2.3sum.pdf', '读取讲义全文，核对投影、正交残差、最小二乘与列满秩条件；本文向量及滤波器数值未取自讲义。'),
  'la-mit-svd': mit('Singular value decomposition', 'd273f75ee2552a5c3c35ccab37e5edce_MIT18_06SCF11_Ses3.5sum.pdf', '读取讲义全文，核对矩形矩阵分解、正交基与奇异值；本文混合矩阵的模式缩放及岭权重为自主计算和推导。'),
  'la-numpy-lstsq': numpy('lstsq', '核对最小残差解、最小范数解、rcond、秩和奇异值返回值；代码为原创教学例并本地执行。'),
  'la-numpy-eigh': numpy('eigh', '核对实对称／复 Hermitian 输入、列特征向量及特征值升序返回；PCA 教学算例由样本协方差公式自主推导。'),
  'la-numpy-svd': numpy('svd', '核对 full_matrices=False 下的形状、降序奇异值、Vh 与重建约定；不据此支持听觉算法的实际收益。'),
  'la-mne-projection': { title: 'Background on projectors and projections', authors: 'MNE-Python developers',
    year: '访问于2026-11-01', publication: 'MNE-Python 官方教程',
    url: 'https://mne.tools/stable/auto_tutorials/preprocessing/45_projectors_background.html', access: 'documentation',
    supports: '读取投影、子空间、秩降低及 EEG/MEG 信号空间投影段落；未把数学投影等同无损去噪，未执行其真实数据教程。' },
};
