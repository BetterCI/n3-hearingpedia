import type { Reference } from './references';

const api = (name: string, supports: string): Reference => ({
  title: `scipy.signal.${name}`, authors: 'SciPy community', year: '访问于2026-10-29',
  publication: 'SciPy 1.18.0 在线方法文档；本地计算为1.17.1',
  url: `https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.${name}.html`,
  access: 'documentation', supports,
});
export const firIirReferences: Record<string, Reference> = {
  'fi-smith-window': {title:'The Scientist and Engineer’s Guide to Digital Signal Processing, Chapter 16: Windowed-Sinc Filters',authors:'Steven W. Smith',year:'1997',publication:'California Technical Publishing；作者公开教材',url:'https://www.dspguide.com/CH16.PDF',access:'fulltext',supports:'读取理想低通、sinc、截断与加窗及频率/时域权衡相关段落。未采用教材中对全部FIR/IIR性能的宽泛排序；图为自行计算。'},
  'fi-smith-recursive': {title:'The Scientist and Engineer’s Guide to Digital Signal Processing, Chapter 19: Recursive Filters',authors:'Steven W. Smith',year:'1997',publication:'California Technical Publishing；作者公开教材',url:'https://www.dspguide.com/CH19.PDF',access:'fulltext',supports:'读取递推、一阶平滑器及响应相关段落；正文一阶衰减时间自行推导和计算，不把递归结构直接等同于无限响应的充分定义。'},
  'fi-smith-cheby': {title:'The Scientist and Engineer’s Guide to Digital Signal Processing, Chapter 20: Chebyshev Filters',authors:'Steven W. Smith',year:'1997',publication:'California Technical Publishing；作者公开教材',url:'https://www.dspguide.com/CH20.PDF',access:'fulltext',supports:'读取Butterworth与Chebyshev响应及波纹换取过渡选择性的相关解释；不引用固定运行速度比值。'},
  'fi-smith-linear': {title:'FIR Filter Design',authors:'MathWorks',year:'访问于2026-10-29',publication:'Signal Processing Toolbox R2026b 官方方法文档',url:'https://www.mathworks.com/help/signal/ug/fir-filter-design.html',access:'documentation',supports:'读取线性相位四型、端点限制及设计分类。未采用其对相位延迟恒定的宽泛概括；正文保留相位常数、符号跳变和零点条件。'},
  'fi-smith-stability': {title:'Stability Revisited',authors:'Julius O. Smith III',year:'在线版，访问于2026-10-29',publication:'Introduction to Digital Filters；作者教材公开镜像',url:'https://www.dsprelated.com/freebooks/filters/Stability_Revisited.html',access:'fulltext',supports:'读取因果不可约有理系统的单位圆极点判据及指数响应；正文用一般BIBO绝对可和判据限定条件，不把仅衰减至零推广为任意系统充分条件。'},
  'fi-smith-df1': {title:'Direct-Form I',authors:'Julius O. Smith III',year:'在线版，访问于2026-10-29',publication:'Introduction to Digital Filters；作者教材公开镜像',url:'https://www.dsprelated.com/freebooks/filters/Direct_Form_I.html',access:'fulltext',supports:'读取差分方程、前馈/反馈负号与直接I型实现，有限精度实现性质。'},
  'fi-smith-df2': {title:'Direct Form II',authors:'Julius O. Smith III',year:'在线版，访问于2026-10-29',publication:'Introduction to Digital Filters；作者教材公开镜像',url:'https://www.dsprelated.com/freebooks/filters/Direct_Form_II.html',access:'fulltext',supports:'读取共享延迟状态、结构等价和内部动态范围相关说明；不声称省状态总能改善数值性能。'},
  'fi-smith-minimum': {title:'Minimum-Phase Filters',authors:'Julius O. Smith III',year:'在线版，访问于2026-10-29',publication:'Introduction to Digital Filters；作者教材公开镜像',url:'https://www.dsprelated.com/freebooks/filters/Minimum_Phase_Filters.html',access:'fulltext',supports:'读取最小相位定义及全通分解相关内容；最小相位与同幅度比较条件、FIR可非线性相位。'},
  'fi-scipy-firwin': api('firwin','核对抽头数、I/II型与奇偶限制、截止的半幅度定义、fs单位和窗函数接口。'),
  'fi-scipy-remez': api('remez','核对加权最小最大误差、频带与权重接口，以及文档列出的1973年方法出处；未冒称阅读全文原始论文。'),
  'fi-scipy-kaiser': api('kaiserord','核对Kaiser经验估阶、过渡宽度按奈奎斯特归一化及须验证实际频响。本地算例额外留出衰减余量。'),
  'fi-scipy-minimum': api('minimum_phase','核对同态法、half=True默认的长度及平方根幅度，half=False的同长度保幅近似。本地用half=False并绘制实际结果。'),
  'fi-scipy-upfirdn': api('upfirdn','核对插值—FIR—抽取与多相实现；支持计算结构而非设备感知收益。'),
  'fi-scipy-butter': api('butter','核对Butterworth半功率临界点、归一化、带通/带阻最终阶数及高阶多项式的数值问题与SOS建议。'),
  'fi-scipy-iirdesign': api('iirdesign','核对按给定原型族和通阻带规格求阶、参数单位、默认椭圆原型与SOS输出；不把最小阶理解为全任务最优。'),
  'fi-scipy-bilinear': api('bilinear','读取双线性代换与频率畸变，核对低层函数不自动预畸变。正文预畸变公式由代换在单位圆上自主推导。'),
  'fi-scipy-sosfilt': api('sosfilt','读取SOS数组排列、转置直接II型、状态输入输出和高阶数值示例。'),
  'fi-scipy-filtfilt': api('filtfilt','读取前后向处理、零相位、阶数及端点规则；正文幅度平方明确限定实系数与理想内部稳态。'),
  'fi-scipy-sosfiltfilt': api('sosfiltfilt','读取二阶节前后向滤波与端点延拓参数；不把有限记录视为全局时不变。'),
  'fi-mne-filtering': {title:'Background information on filtering',authors:'MNE-Python developers',year:'访问于2026-10-29',publication:'MNE-Python 1.13.2 官方方法教程',url:'https://mne.tools/stable/auto_tutorials/preprocessing/25_background_filtering.html',access:'documentation',supports:'读取FIR/IIR、因果/非因果、滤波长度、延迟补偿和时间扩散相关段落；仅支撑预处理方法，不据此给出临床设置或神经响应常模。'},
  'fi-scipy-firls': api('firls','读取最小二乘积分准则及其与最坏误差约束的区别。'),
  'fi-scipy-fftconvolve': api('fftconvolve','读取FFT线性卷积、输出模式、边界与重叠相加入口；不把same模式当作因果流式输出。'),
};
