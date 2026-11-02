import type { Reference } from './references';
export const stochasticProcessesReferences: Record<string, Reference> = {
  "sp-processes": {
    "title": "Random Processes",
    "authors": "Alan V. Oppenheim; George C. Verghese",
    "year": "2010",
    "publication": "MIT 6.011, Signals, Systems and Inference，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/f240d88581626352c6a17eb2872504aa_MIT6_011S10_chap09.pdf",
    "access": "fulltext",
    "supports": "实现与总体、联合分布、高斯、WSS和遍历；本文白而依赖、宽而非严平稳反例另行构造。"
  },
  "sp-psd": {
    "title": "Power Spectral Density",
    "authors": "Alan V. Oppenheim; George C. Verghese",
    "year": "2010",
    "publication": "MIT 6.011, Signals, Systems and Inference，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/8075041184d566103ce7c3f69afc5e75_MIT6_011S10_chap10.pdf",
    "access": "fulltext",
    "supports": "Wiener–Khinchin、谱表示、白噪声、LTI与谱因子；本文固定实过程和每Hz双侧谱约定，保留谱线与广义白噪声边界。"
  },
  "sp-wiener": {
    "title": "Wiener Filtering",
    "authors": "Alan V. Oppenheim; George C. Verghese",
    "year": "2010",
    "publication": "MIT 6.011, Signals, Systems and Inference，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/f135b328c7448bf21c4939ea9ff8f8fb_MIT6_011S10_chap11.pdf",
    "access": "fulltext",
    "supports": "正交性、因果和非因果最优线性估计；三抽头正规方程与全时域理想谱解按信息范围分别比较。"
  },
  "sp-mmse": {
    "title": "Estimation with Minimum Mean Square Error",
    "authors": "Alan V. Oppenheim; George C. Verghese",
    "year": "2010",
    "publication": "MIT 6.011, Signals, Systems and Inference，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-011-introduction-to-communication-control-and-signal-processing-spring-2010/f3ed10bd2a49c9ec2baf3dddb5242862_MIT6_011S10_chap08.pdf",
    "access": "fulltext",
    "supports": "条件期望MMSE和线性投影LMMSE的区别；不把一般非高斯问题的线性最优当全局MMSE。"
  },
  "sp-wss": {
    "title": "Wide-Sense Stationary Processes and LTI Filtering",
    "authors": "MIT 6.011 课程：George C. Verghese; Alan V. Oppenheim; Peter Hagelstein",
    "year": "2018",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/b6554551f64bd5f75ff3f4ff4f0a23f6_MIT6_011S18lec16.pdf",
    "access": "fulltext",
    "supports": "WSS与相关、稳定LTI映射；本文输出谱与互谱采用明确相关方向。"
  },
  "sp-filtering": {
    "title": "LTI Filtering of WSS Processes",
    "authors": "MIT 6.011 课程：George C. Verghese; Alan V. Oppenheim; Peter Hagelstein",
    "year": "2018",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/aff4e7915b3de35e2481d62b444d71ee_MIT6_011S18lec17.pdf",
    "access": "fulltext",
    "supports": "随机输入滤波、方差与相关；零初始状态瞬态不冒充全历史稳态。"
  },
  "sp-spectral": {
    "title": "Power Spectral Density",
    "authors": "MIT 6.011 课程：George C. Verghese; Alan V. Oppenheim; Peter Hagelstein",
    "year": "2018",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/e6d7ee6c7901199ddec42d9e75ffbe1b_MIT6_011S18lec18.pdf",
    "access": "fulltext",
    "supports": "PSD、均方值与频率归一化；数字弧度谱与每Hz密度不混用。"
  },
  "sp-wkt": {
    "title": "Einstein–Wiener–Khinchin Theorem, PSD Applications, Modeling Filters",
    "authors": "MIT 6.011 课程：George C. Verghese; Alan V. Oppenheim; Peter Hagelstein",
    "year": "2018",
    "publication": "MIT OpenCourseWare 官方课程讲义",
    "url": "https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/9657e9035276a86c632ffcf6f0ec0bc2_MIT6_011S18lec19.pdf",
    "access": "fulltext",
    "supports": "相关与谱、谱线和整形滤波；普通密度存在的条件与一般谱测度分开。"
  },
  "sp-poisson": {
    "title": "Poisson Processes",
    "authors": "Robert G. Gallager",
    "year": "2011",
    "publication": "MIT 6.262 Discrete Stochastic Processes，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/3a19ce0e02d0008877351bfa24f3716a_MIT6_262S11_chap02.pdf",
    "access": "fulltext",
    "supports": "齐次Poisson计数、独立平稳增量和指数间隔；计数本身不平稳，不当神经不应期模型。"
  },
  "sp-markov": {
    "title": "Finite-state Markov Chains",
    "authors": "Robert G. Gallager",
    "year": "2011",
    "publication": "MIT 6.262 Discrete Stochastic Processes，作者课程书",
    "url": "https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/3558b08622765d26c2b0a7d2eeeac885_MIT6_262S11_chap03.pdf",
    "access": "fulltext",
    "supports": "条件Markov性、转移矩阵、平稳初分布与有限不可约非周期链收敛；不将时齐性当平稳。"
  },
  "sp-basic": {
    "title": "Basic Concepts of Random Processes",
    "authors": "Hossein Pishro-Nik",
    "year": "2014；在线版2026-11-02核对",
    "publication": "Introduction to Probability, Statistics, and Random Processes，作者官方网站",
    "url": "https://www.probabilitycourse.com/chapter10/10_1_0_basic_concepts.php",
    "access": "fulltext",
    "supports": "时间与取值空间分别分类；过程与一条实现不等同。"
  },
  "sp-stationary": {
    "title": "Stationary Processes",
    "authors": "Hossein Pishro-Nik",
    "year": "2014；在线版2026-11-02核对",
    "publication": "Introduction to Probability, Statistics, and Random Processes，作者官方网站",
    "url": "https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php",
    "access": "fulltext",
    "supports": "有限维分布的时移不变；WSS与严格平稳的条件和区别。"
  },
  "sp-brownian": {
    "title": "Brownian Motion: definition and properties",
    "authors": "Hossein Pishro-Nik",
    "year": "2014；在线版2026-11-02核对",
    "publication": "Introduction to Probability, Statistics, and Random Processes，作者官方网站",
    "url": "https://www.probabilitycourse.com/chapter11/11_4_2_definition_and_some_properties.php",
    "access": "fulltext",
    "supports": "Brownian连续路径、独立平稳高斯增量、非平稳状态及min(s,t)协方差；未进行随机微积分教学或实测扩散拟合。"
  },
  "sp-welch": {
    "title": "scipy.signal.welch",
    "authors": "SciPy developers",
    "year": "stable快照2026-11-02；本地1.17.1",
    "publication": "SciPy 官方文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.welch.html",
    "access": "documentation",
    "supports": "分段窗、重叠、density和detrend；未把重叠段数当独立自由度。"
  },
  "sp-periodogram": {
    "title": "scipy.signal.periodogram",
    "authors": "SciPy developers",
    "year": "stable快照2026-11-02；本地1.17.1",
    "publication": "SciPy 官方文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html",
    "access": "documentation",
    "supports": "密度标度、每Hz单位、窗平方和与单侧折叠；短例显式关闭去均值。"
  },
  "sp-csd": {
    "title": "scipy.signal.csd",
    "authors": "SciPy developers",
    "year": "stable快照2026-11-02；本地1.17.1",
    "publication": "SciPy 官方文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.csd.html",
    "access": "documentation",
    "supports": "官方Pxy使用conj(X)Y，核对本文S_yx的方向约定。"
  },
  "sp-coherence": {
    "title": "scipy.signal.coherence",
    "authors": "SciPy developers",
    "year": "stable快照2026-11-02；本地1.17.1",
    "publication": "SciPy 官方文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.coherence.html",
    "access": "documentation",
    "supports": "需要平滑/分段的平方相干；单个未平滑谱点的比值可恒为1，不能作因果证据。"
  },
  "sp-lfilter": {
    "title": "scipy.signal.lfilter",
    "authors": "SciPy developers",
    "year": "stable快照2026-11-02；本地1.17.1",
    "publication": "SciPy 官方文档",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html",
    "access": "documentation",
    "supports": "因果差分滤波及零初态与zi；本文AR独立指定平稳初值，有限FIR去掉历史不完整的起始位置。"
  }
};
