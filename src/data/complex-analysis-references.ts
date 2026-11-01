import type { Reference } from './references';
const mit=(title:string,file:string,supports:string):Reference=>({title,authors:'Jeremy Orloff; MIT OpenCourseWare',year:'2018',publication:'MIT 18.04 Complex Variables with Applications',url:'https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/'+file,access:'fulltext',supports});
const smith=(title:string,page:string,supports:string):Reference=>({title,authors:'Julius O. Smith III',year:'2007',publication:'Introduction to Digital Filters with Audio Applications；作者在线教材',url:'https://www.dsprelated.com/freebooks/filters/'+page+'.html',access:'fulltext',supports});
const scipy=(name:string,supports:string):Reference=>({title:'scipy.signal.'+name,authors:'SciPy contributors',year:'访问于2026-11-02',publication:'SciPy 官方文档',url:'https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.'+name+'.html',access:'documentation',supports});
export const complexAnalysisReferences:Record<string,Reference>={
 'ca-mit-algebra':mit('Topic 1: Complex Algebra and the Complex Plane','6eae09885b0fab3f068e31752198abea_MIT18_04S18_topic1.pdf','读取复平面、指数、幅角、根及对数分支相关说明；声压相量、延迟及叠加数值为本文原创，不把复数编码视为额外物理声压。'),
 'ca-mit-analytic':mit('Topic 2: Analytic Functions','330e301bd727c7bdaa679cf44cb75fe3_MIT18_04S18_topic2.pdf','读取复导数、方向限制、Cauchy–Riemann、解析与调和函数相关说明；正文三个差商及单点CR不足的反例独立推导，部分PDF公式文本提取缺项，不冒称全部扫描公式完成OCR核验。'),
 'ca-mit-cauchy':mit('Topic 3: Line Integrals and Cauchy’s Theorem','1968cab6de7c96ead1c83001459a007b_MIT18_04S18_topic3.pdf','读取参数曲线、路径积分、单连通与闭路积分相关段落；正文单位圆积分直接参数化复算，保留定义域与方向条件。'),
 'ca-mit-formula':mit('Topic 4: Cauchy’s Integral Formula','b1a90df19f643b974555bbbb93138a48_MIT18_04S18_topic4.pdf','读取积分公式与高阶导数相关说明；正文圆周内函数值例与数值系数核验为独立计算，不将边界公式用于有未处理奇点的域。'),
 'ca-mit-series':mit('Topic 7: Taylor and Laurent Series','dff6a0c70eefb1e23bb87f8524361801_MIT18_04S18_topic7.pdf','读取Taylor、Laurent、系数积分与环域依赖段落；一极点内外两套展开和误差公式为本站自主推导，区分局部Taylor与Z变换收敛域。'),
 'ca-mit-residue':mit('Topic 8: Residue Theorem','3c58ce71ec6f7573804221d76158a0bd_MIT18_04S18_topic8.pdf','读取孤立奇点、留数、简单极点与留数定理说明；逆Z提取系数含原点额外极点，已用不同半径圆周独立核验，不只计算传函自身的极点。'),
 'ca-mit-integrals':mit('Topic 9: Definite Integrals Using the Residue Theorem','f69bc227ae476839819fb18e5b283072_MIT18_04S18_topic9.pdf','读取上半平面半圆闭合与实积分方法；1/(1+w²)的弧积分界和一阶低通面积为自主展开并用实轴积分核对，不把传函面积当作实测声能。'),
 'ca-mit-laplace':mit('Topic 12: Laplace Transform','1b1cbc6540b338b58b7bc1b1cc1f280b_MIT18_04S18_topic12.pdf','读取Laplace定义、复频率与极点相关讲义说明；本文使用显式双边定义，另计算一阶因果模型的收敛半平面，不把不同变换约定或s/z平面稳定条件混用。'),
 'ca-smith-one-pole':smith('One-Pole Transfer Functions','One_Pole_Transfer_Functions','读取同一有理式、双边序列、ROC与因果/反因果稳定解释；正文a=0.8的两套序列为独立计算。'),
 'ca-smith-poles':smith('Pole-Zero Analysis','Pole_Zero_Analysis_I','读取约分后的零极点、增益因子及几何距离解释；两共轭极点的衰减与准确峰频由自主公式核验，不照搬未说明因果与ROC的一般稳定概括。'),
 'ca-scipy-freqz':scipy('freqz','核对数字滤波器系数、H(e^{jω})、fs与频率单位；使用本地SciPy 1.17.1，在线文档版本不是执行版本。'),
 'ca-scipy-lfilter':scipy('lfilter','核对固定有理滤波器与零初始条件的时域运算；将原始差分递推、解析脉冲响应、直接卷积和接口输出独立比较。'),
};
