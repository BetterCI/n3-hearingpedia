import type { Reference } from './references';
export const nonlinearDynamicsReferences: Record<string, Reference> = {
  "nd-scalar": {
    "title": "Flows and Bifurcations in One Dimension",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec2-3.pdf",
    "access": "fulltext",
    "supports": "标量流、分岔分支与滞后；本文另选固定参数截面并推导折点和瓶颈时间。"
  },
  "nd-phase": {
    "title": "Pendulum and Stability in Two Dimensional Systems",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec4-5.pdf",
    "access": "fulltext",
    "supports": "相空间、势能、稳定与吸引域；区分局部稳定、多稳态和全局结论。"
  },
  "nd-dissipation": {
    "title": "Dissipation and Contraction of Volumes in Phase Space",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec6-7.pdf",
    "access": "fulltext",
    "supports": "散度、相体积收缩；负散度不推出所有方向收缩或混沌。"
  },
  "nd-cycles": {
    "title": "Forced Oscillators and Limit Cycles",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec8-9.pdf",
    "access": "fulltext",
    "supports": "自持与强迫振荡、极限环及Van der Pol；本篇参数、能量与数值另行计算。"
  },
  "nd-hopf": {
    "title": "Bifurcations in Two Dimensions",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec10-11.pdf",
    "access": "fulltext",
    "supports": "超/亚临界Hopf、环的折叠；不沿用讲义鞍结小节mu符号笔误。"
  },
  "nd-spectral": {
    "title": "Spectral Analysis for Dynamical Systems",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec12-14.pdf",
    "access": "fulltext",
    "supports": "频谱与动力学观察，谱线和连续谱的解释；宽谱不当作混沌充分证据。"
  },
  "nd-poincare": {
    "title": "Poincaré Sections",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec15-16.pdf",
    "access": "fulltext",
    "supports": "横截面、返回映射、周期轨道与乘子；本文Hopf乘子用变分方程独立核对。"
  },
  "nd-strange": {
    "title": "Introduction to Strange Attractors",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec19.pdf",
    "access": "fulltext",
    "supports": "吸引子、几何与不规则轨道；不凭投影形状证明混沌。"
  },
  "nd-lorenz": {
    "title": "Lorenz Equations",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec20-21.pdf",
    "access": "fulltext",
    "supports": "Lorenz模型、平衡、耗散与参数；本篇QR指数为有限时长数值而非定理证明。"
  },
  "nd-lyapunov": {
    "title": "Lyapunov Exponents",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec24.pdf",
    "access": "fulltext",
    "supports": "沿轨道变分、重归一化与长期平均；正指数不能脱离有界、典型轨道等背景解释。"
  },
  "nd-maps": {
    "title": "Period Doubling Route to Chaos",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec25-27.pdf",
    "access": "fulltext",
    "supports": "Logistic映射、周期乘子、倍周期与窗口；r=4典型指数与特殊轨道分开。"
  },
  "nd-intermittency": {
    "title": "Intermittency (and Quasiperiodicity)",
    "authors": "Daniel H. Rothman",
    "year": "2022",
    "publication": "MIT 12.006J/18.353J/2.050J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/12-006j-nonlinear-dynamics-chaos-fall-2022/mit12_006jf22_lec28.pdf",
    "access": "fulltext",
    "supports": "间歇、准周期及不同混沌路径；不声称复杂系统都走同一路径。"
  },
  "nd-normalforms": {
    "title": "Bifurcations: Baby Normal Forms",
    "authors": "Rodolfo R. Rosales",
    "year": "2004课程；文件内日期另保留",
    "publication": "MIT 18.385J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/bca4134c39b52afdaf62d05e0e76afc6_babynormalforms.pdf",
    "access": "fulltext",
    "supports": "正规形与非退化条件、局部坐标变换及截断范围；叉形依赖结构/对称性。"
  },
  "nd-weak": {
    "title": "Weakly Nonlinear Oscillators",
    "authors": "Rodolfo R. Rosales",
    "year": "2004课程；文件内日期另保留",
    "publication": "MIT 18.385J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/fdf8ddfa718fb2686f3a0d4e1e3976d9_wklynloscilator.pdf",
    "access": "fulltext",
    "supports": "慢幅相、平均方法与弱非线性；谐波平衡分支仅为候选近似，不代替稳定性分析。"
  },
  "nd-hopf-proof": {
    "title": "Hopf Bifurcations",
    "authors": "Rodolfo R. Rosales",
    "year": "2004课程；文件内日期另保留",
    "publication": "MIT 18.385J，作者官方课程讲义",
    "url": "https://ocw.mit.edu/courses/18-385j-nonlinear-dynamics-and-chaos-fall-2004/945f716b937b06cf5b5fcdeb591d18e2_hopfbif.pdf",
    "access": "fulltext",
    "supports": "Hopf条件与局部振荡；纯虚特征值不是单独充分条件。"
  },
  "nd-cochlea": {
    "title": "Auditory sensitivity provided by self-tuned critical oscillations of hair cells",
    "authors": "Sébastien Camalet; Thomas Duke; Frank Jülicher; Jacques Prost",
    "year": "2000",
    "publication": "PNAS 97(7):3183–3188；作者开放稿",
    "doi": "10.1073/pnas.97.7.3183",
    "url": "https://arxiv.org/pdf/physics/0003100",
    "access": "fulltext",
    "supports": "原始临界振荡听觉建模；本文仅用归一化共振Hopf正规形推导立方根响应，不验证真实耳蜗参数、自调谐或临床获益。"
  },
  "nd-surrogates": {
    "title": "Surrogate time series",
    "authors": "Thomas Schreiber; Andreas Schmitz",
    "year": "2000",
    "publication": "Physica D 142:346–382；作者开放稿",
    "doi": "10.1016/S0167-2789(00)00043-9",
    "url": "https://arxiv.org/pdf/chao-dyn/9909037",
    "access": "fulltext",
    "supports": "原作者替代数据方法与零假设、非平稳性及误判；拒绝指定随机零假设不等于证明确定性混沌。"
  },
  "nd-ivp": {
    "title": "scipy.integrate.solve_ivp",
    "authors": "SciPy developers",
    "year": "stable快照；2026-11-02核对，本地1.17.1",
    "publication": "SciPy 官方接口文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html",
    "access": "documentation",
    "supports": "rtol/atol、内部步长、输出采样及事件语义；局部误差容差不是严格真实全局误差界。"
  }
};
