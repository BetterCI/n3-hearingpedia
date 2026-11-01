import type { Reference } from './references';
const iv=(title:string,chapter:string,supports:string):Reference=>({title,authors:'Victor Ivrii',year:'在线教材（2026-11-02核验）',publication:'Partial Differential Equations, University of Toronto, APM346 author textbook',url:'https://www.math.toronto.edu/ivrii/PDE-textbook/'+chapter+'.html',access:'fulltext',supports});
const mit=(title:string,resource:string,supports:string):Reference=>({title,authors:'Matthew J. Hancock',year:'2006',publication:'MIT OpenCourseWare 18.303, Fall 2006, author lecture notes',url:'https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/resources/'+resource+'/',access:'fulltext',supports});
const dl=(title:string,section:string,supports:string):Reference=>({title,authors:'NIST Digital Library of Mathematical Functions',year:'在线版（2026-11-02核验）',publication:'NIST DLMF, §'+section,url:'https://dlmf.nist.gov/'+section,access:'fulltext',supports});
export const mathematicalPhysicsMethodsReferences: Record<string,Reference> = {
 'mm-problem':iv('§1.2 Initial and Boundary Value Problems','Chapter1/S1.2','读取初值、边值、混合定解问题及适定性定义。Neumann相容符号按本文负拉普拉斯约定独立用散度定理推导。'),
 'mm-classify':iv('§1.3 Classification of Equations','Chapter1/S1.3','读取阶数、线性及主部分类；正文二维判别式采用交叉项2B，并限定非退化主部，高维不直接套二维式。'),
 'mm-heat':mit('The 1-D Heat Equation','heateqni','针对性读取热流、能量平衡、分离变量、傅里叶级数、收敛及非齐次问题；非逐页复述。D=0.1等均为原创模型。'),
 'mm-wave':mit('The 1-D Wave Equation','waveeqni','读取理想弦推导、正常模态、初始条件及全线传播；拨弦位置0.3L、系数、重建和频率独立计算，不复制原例题图。'),
 'mm-sl':iv('§4.2 Eigenvalue Problems','Chapter4/S4.2','读取Dirichlet、Neumann、混合及Robin特征问题，核对零模态与特征值可能非正。一般正则自伴SL正交关系由本文分部积分说明。'),
 'mm-orthogonal':iv('§4.3 Orthogonal Systems','Chapter4/S4.3','读取内积、投影、归一、完备性与Hilbert空间框架；正文区分均方与逐点收敛，不由正交单独推出任意展开完备。'),
 'mm-multi':mit('The Heat and Wave Equations in 2D and 3D','pde3d','读取多维场、守恒、拉普拉斯算子、分离与模态，针对与正文有关的章节。声学小扰动式和时谐转换另按固定符号代入检查。'),
 'mm-coordinates':iv('§6.3 Laplace Operator in Different Coordinates','Chapter6/S6.3','读取极/柱/球坐标下拉普拉斯与积分几何；正文把径向权r与面积元联系，区分角向和完整径向解。'),
 'mm-bessel':dl('Definitions: Bessel Equation and Standard Solutions','10.2','核对贝塞尔微分方程、整数阶J与Y的正则/奇异行为；仅在包含原点且要求有限的圆盘模型排除Y，环带不照搬。'),
 'mm-bessel-zeros':dl('Zeros of Bessel Functions and Their Derivatives','10.21','核对函数与导数零点的区别。本站固定膜频率及J0两根由SciPy和独立求根/微分式交叉检验；不把膜边界套到刚壁声管。'),
 'mm-bessel-integral':dl('Integrals, especially Orthogonality Properties','10.22','针对性核对有限区间正交积分与零点归一化相关公式。径向积分带r，对角系数以独立数值积分确认。'),
 'mm-legendre':dl('Differential Equations for Legendre and Related Functions','14.2','读取勒让德方程及端点结构；本文只用整数非负阶多项式，低阶式与正交关系独立用数值积分检查。'),
 'mm-harmonics':dl('Spherical and Spheroidal Harmonics','14.30','读取整数ℓ,m域、定义、归一和相位约定；明确实/复球谐基差异。图只画Pℓ(cosθ)角向因子，未称实际指向性或完整球面场。'),
 'mm-fourier':mit('Infinite Domain Problems and the Fourier Transform','fourtran','读取傅里叶变换、导数、卷积与热方程解；本文明确角波数与逆变换2π，Gaussian尺度与总质量独立积分检查。'),
 'mm-laplace':{title:'The Unilateral Laplace Transform',authors:'William McC. Siebert',year:'1986',publication:'Circuits, Signals, and Systems, MIT Press, Chapter 2, author textbook excerpt hosted by MIT',doi:'10.7551/mitpress/1839.001.0001',url:'https://eecs6302.mit.edu/_static/fall21/extras/siebert2.pdf',access:'fulltext',supports:'读取单边积分、导数初值项、收敛与初态处理相关部分。波动模态变换以本篇方程直接推导，未默认省略初值。'},
 'mm-distribution':iv('§11.1 Distributions','Chapter11/S11.1','读取测试函数、δ与分布导数定义及扩展解概念；一维弱式、H1/H01定义和有限元矩阵为本文明确给出的教学框架，不声称覆盖完整泛函分析。'),
 'mm-green':mit('Method of Green’s Functions','greensfn','读取δ、Green恒等式、核及边值条件的关系。本文负二阶导的分段核为独立一维推导，明确不同于讲义多维Laplacian核的符号约定。'),
 'mm-energy':iv('§2.7 Energy Integral','Chapter2/S2.7','读取波动能量、通量与唯一性应用。弦μ/T能量恒等式、零值端点边界功率及扩散能量衰减以本站独立代入积分核验。'),
 'mm-variational':iv('§10.1 Functionals, Extremums and Variations','Chapter10/S10.1','读取泛函、变分、驻点与极值区别。Poisson能量泛函、Rayleigh商10/L²及变分上界为本文特例推导；一般Robin需边界项，未一概省略。'),
 'mm-numerics':{title:'Waves and Imaging: Class Notes, 18.325 (Draft December 20, 2016)',authors:'Laurent Demanet',year:'2016',publication:'Massachusetts Institute of Technology, author notes',url:'https://math.mit.edu/icg/resources/notes325.pdf',access:'fulltext',supports:'针对性读取§1.2波传播、时谐核与Sommerfeld条件，以及附录B中心差分、CFL及色散；非通读全部144页。原文时间约定转为本文exp(jωt)。热显式格式稳定界、离散特征值与离散色散关系由本站傅里叶/矩阵推导和独立核验给出。'},
};
