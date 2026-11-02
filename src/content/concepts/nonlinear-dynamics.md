---
title: "非线性动力学"
english: "Nonlinear Dynamics"
slug: "nonlinear-dynamics"
summary: "作为《微分方程与动力系统》的配套篇，从多稳态、吸引域与正规形深入鞍结瓶颈、滞后、超临界与亚临界Hopf、周期轨道稳定性、慢快振荡、受迫响应和同步，再用映射、变分方程及替代数据思想区分混沌判据、数值证据与实验解释。"
categories: ["research-methods", "acoustics", "neuroscience"]
tags: ["基础课程", "非线性动力学", "分岔", "多稳态", "极限环", "同步", "混沌", "Lyapunov指数"]
aliases: ["非线性动力系统", "非线性动力学与混沌", "Nonlinear Dynamical Systems", "Nonlinear Dynamics and Chaos"]
level: ["undergraduate", "graduate"]
status: draft
depth: in-depth
last_updated: "2026-11-02"
literature_checked_at: "2026-11-02"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
knowledge_area: "methods"
kind: "course"
key_facts:
  - {label: "课程定位", value: "配合微分方程与动力系统，深入结构变化、多稳态、振荡、同步与混沌"}
  - {label: "核心区分", value: "非线性不等于混沌；局部失稳、全局吸引、滞后和数值误差分别检验"}
  - {label: "研究连接", value: "非线性共振、临界振荡、神经节律与耦合；模型机制需另与数据对应"}
  - {label: "证据边界", value: "不规则波形、宽谱、低维投影或一个正有限指数都不是普遍混沌证书"}
references: ["nd-scalar", "nd-phase", "nd-dissipation", "nd-cycles", "nd-hopf", "nd-spectral", "nd-poincare", "nd-strange", "nd-lorenz", "nd-lyapunov", "nd-maps", "nd-intermittency", "nd-normalforms", "nd-weak", "nd-hopf-proof", "nd-cochlea", "nd-surrogates", "nd-ivp"]
order: 1022
---

**非线性动力学**（nonlinear dynamics）研究不满足线性叠加规律的演化系统，尤其关注多稳态、振幅相关的振动、分岔、同步、慢快转换和混沌怎样产生。非线性是方程或演化映射的结构性质，不是“不规则”的同义词；一个非线性系统可以趋于静止、稳定地周期振荡，也可以在某些参数范围内表现复杂演化。[13](#ref-nd-normalforms)[4](#ref-nd-cycles)

本篇与[微分方程与动力系统](../differential-equations-and-dynamical-systems/)配套。前篇建立初值问题、存在唯一、相图与动力学概览；本篇进一步分析临界点附近的结构、多稳态之间的转换、周期轨道的稳定性，以及怎样形成可信的混沌数值证据。需要的概念在使用处补充，不要求先完整修完配套课程。

十幅图、三个短程序和[完整实验脚本](/n3-hearingpedia/code/nonlinear-dynamics/experiments.py)均为原创指定模型的教学复算，不是耳蜗、神经系统、听者、器件或真实录音的实测。声音与生理例子帮助连接研究问题，但相似的相图不能单独确认某种生物机制。

## 阅读准备与独立阅读

**起步知识。** 会读函数曲线、理解正负号与“随时间增加还是减少”即可进入多稳态和分岔图。导数描述变化率；状态是一组决定模型后续演化的变量；参数在一次固定模型的演化中保持不变，除非明确规定随时间变化。

**随用随补。** 平衡是变化率为零的状态；吸引表示附近轨迹长期靠近；稳定表示小扰动不会造成指定意义上的大偏离。Jacobian是局部偏导数矩阵，特征值描述线性近似的增长与旋转。后文会区分平衡特征值、周期轨道乘子和长期Lyapunov指数。

**分层阅读。** 第一遍读势阱、滞后、Hopf、振荡和同步图；第二遍复算导数、正规形和返回映射；第三遍再读变分方程、QR指数与数据推断。可按需参照[微积分](../calculus/)、[线性代数](../linear-algebra/)、[数值分析](../numerical-analysis/)及[数理统计](../mathematical-statistics/)，不把整门先修课作为阅读门槛。

本文以τ=t/T₀表示归一化时间，撇号为对τ求导，状态也按相应尺度归一化。角频率ω换成实际Hz时要除以2πT₀，指数换成每秒时要除以T₀；不直接把模型中的1解释为1 Pa、1 V或1 Hz。不同物理单位的状态先分别定标，再谈距离与误差。

## 非线性改变什么 从多稳态与吸引域开始

### 叠加失效不意味着所有现象都复杂

线性齐次系统的解可按常数线性组合；非线性方程通常不具有这一性质。例如x′=x−x³中的立方项会把两个状态之和的变化率与分别求变化率后相加区分开。系统是否自治、是否受迫、是否随机，则是另外的分类：非线性自治系统仍可以很规则，线性随机系统也可以呈现不规则波形。[2](#ref-nd-phase)

图1取

$$
\begin{aligned}
x'&=x-x^3=-V'(x),\\
V(x)&=x^4/4-x^2/2,\\
\frac{dV}{d\tau}&=-(x-x^3)^2\leq0.
\end{aligned}
$$

这里V是数学势函数，V′(x)表示对状态x求导。平衡为−1、0、1，右端导数1−3x²在±1为−2，在0为1，因此两侧平衡局部渐近稳定，中间平衡不稳定。负初值趋向−1，正初值趋向1，零初值保持零；同一参数并不对应唯一最终状态。

### 吸引域与分隔边界

**吸引集合**是不变且吸引某个邻域轨道的集合；不变表示从集合内出发的演化仍留在其中。渐近稳定平衡与吸引极限环是常见例子，严格的“吸引子”定义还可能增加最小性等要求。**吸引域**是长期趋向指定吸引集合的初始状态集合；图1中两个稳定平衡的吸引域分别为负、正半轴，0位于分隔边界。高维系统的边界可能由鞍点的稳定流形等结构组织，不能仅凭一条观测轨迹恢复整个吸引域。[2](#ref-nd-phase)

**局部渐近稳定**不等于全局唯一吸引。**多稳态**表示同一组参数下存在多个稳定长期状态；短暂扰动能否触发转换取决于扰动后的状态是否越过吸引域边界。这个确定性例子没有噪声，也没有周期振荡，不能把任何一次跳变都解释为随机逃逸或混沌。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/basins-potential.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/basins-potential.svg" alt="双阱势函数和不同初值趋向两个稳定平衡的轨迹" width="1400" height="550" loading="lazy" /></a><figcaption>图1　同一标量模型x′=x−x³，±1稳定、0不稳定。势函数沿轨迹不增；两侧初值进入不同吸引域。这里只比较确定性初值，不模拟热噪声、神经状态或声学双稳态实测。</figcaption></figure>

## 局部线性化与正规形 怎样缩减问题

### 双曲平衡与失效边界

在平衡x⋆附近写η=x−x⋆，光滑系统的线性近似为η′=Jη，其中J为Jacobian。若所有特征值实部非零，平衡称为**双曲**；全为负可判局部渐近稳定，有正实部则不稳定。双曲性帮助联系局部非线性轨道结构与线性近似，但不保证全局吸引域、振幅和时间尺度完全相同。[2](#ref-nd-phase)

当特征值实部为零，线性化可能无法判断。例如x′=−x³和x′=x³在0的Jacobian均为0，前者渐近稳定，后者不稳定。线性化未给结论，不等于系统一定失稳，也不等于必须混沌。

### 正规形保留局部关键项

**正规形**通过局部坐标、参数变换及适当截断，把临界附近的方程化成便于比较的结构；**中心流形**在相应光滑性和谱条件下，把非双曲附近的局部分析约化到临界方向。它们不是任意删除高阶项的许可，也不是说远离临界点仍有相同精度。[13](#ref-nd-normalforms)[15](#ref-nd-hopf-proof)

常见的一参数标量原型如下。稳定性在各分支内部按对状态的导数判断，临界点本身另作非线性分析。

| 类型 | 选定正规形 | 局部结构与前提 |
| --- | --- | --- |
| 鞍结 | x′=μ−x² | μ>0时有稳定√μ与不稳定−√μ；μ<0时无平衡，要求通常的非退化条件 |
| 跨临界 | x′=μx−x² | 0与μ两分支相交并交换稳定性；依赖保持这些分支的模型结构 |
| 超临界叉形 | x′=μx−x³ | μ>0出现两个稳定非零平衡，原点失稳；通常依赖x→−x对称性或相应约束 |
| Hopf | 一对共轭特征值穿过虚轴 | 还要非零穿越速率、非退化非线性系数及其余谱条件，不能只看纯虚特征值 |

这些都是局部原型。给叉形方程加入非零常量偏置通常会破坏对称分支结构，不能坚持它仍是原来完全对称的叉形分岔。[1](#ref-nd-scalar)[13](#ref-nd-normalforms)

## 鞍结 瓶颈与滞后 参数轴不是时间轴

### 临界减速与消失后的慢通过

对x′=μ−x²，μ>0的稳定平衡x*=√μ附近扰动满足η′≈−2√μη，局部松弛时间为1/(2√μ)。μ接近0时恢复变慢；该结论来自具体导数，不意味着所有“接近临界”的系统都遵循同一指数。[1](#ref-nd-scalar)

平衡消失后也可能留下慢通过区域。选取另一个等价取向的原型x′=ε+x²，ε>0，从−L走到L的时间为

$$
T(\varepsilon,L)=\frac2{\sqrt\varepsilon}
\arctan\!\left(\frac L{\sqrt\varepsilon}\right).
$$

固定L>0、ε→0⁺时，T渐近为π/√ε。L=1、ε=0.01时T≈29.4226。这是通过有限区间的**瓶颈时间**，不是极限环周期，也不是越过爆破解继续积分的许可；x′=ε+x²在足够长时间后本身可爆破。[5](#ref-nd-hopf)

### 两个折点怎样形成准静态滞后

取x′=h+x−x³，平衡满足h=x³−x。折点由1−3x²=0给出，参数位置为h=±2/(3√3)≈±0.38490。中间范围有三个平衡：外侧两个稳定，中间一个不稳定。[13](#ref-nd-normalforms)

如果系统缓慢沿某个稳定分支运行，噪声与有限速率效应可忽略，并在折点失去该分支后转到另一稳定状态，那么上、下扫参可走不同路径，形成**准静态滞后**。图2画的是固定参数的平衡分支，不是一条实际扫参时间曲线。真实扫参还可能有动态延迟、初态依赖和噪声诱发提前跃迁，需要单独给出h(τ)和扰动模型。

推广为x′=h+μx−x³时，折线可参数化为μ=3x²、h=−2x³；两支折线在(μ,h)=(0,0)汇合，构成尖点组织的一种显式例子。固定μ=1的图只是这张两参数结构的截面，不应把一条S形曲线本身当成完整两参数分岔图。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/folds-bottleneck.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/folds-bottleneck.svg" alt="固定偏置下的S形平衡分支，以及另一个鞍结原型的瓶颈时间" width="1400" height="550" loading="lazy" /></a><figcaption>图2　左图横轴h是参数，实线稳定、虚线不稳定，折点±0.38490；不把实线当真实扫参轨迹。右图为x′=ε+x²、L=1的解析过境时间与ε→0⁺渐近式，两个面板不是同一条方程的不同时间段。</figcaption></figure>

## Hopf分岔 从静止到自持振荡

### 超临界Hopf的幅度与频率

把二维状态写成复数z=x+iy，考虑已明确归一化的正规形

$$
\begin{aligned}
z'&=(\mu+i\omega_0)z-(1+ic)|z|^2z,\\
r'&=\mu r-r^3,\\
\theta'&=\omega_0-cr^2.
\end{aligned}
$$

其中r=|z|≥0，θ为相位，ω₀≠0，c控制振幅相关的频率偏移。μ<0时原点吸引；μ>0时原点失稳，并出现半径r*=√μ的吸引极限环。其角频率为ω₀−cμ，只在该量非零时对应周期轨道；在足够小的μ附近由ω₀≠0保证。[5](#ref-nd-hopf)[15](#ref-nd-hopf-proof)

在μ=0，径向方程为r′=−r³，r(τ)=r₀/√(1+2r₀²τ)，仍趋于0，但为代数衰减。不能看到线性化纯虚特征值就断言“严格中性”或“已经存在稳定振荡”。一般Hopf定理还需特征值横穿虚轴，以及第一Lyapunov系数非零等条件；该系数的数值依赖约定，其符号用于区分相应正规形的超/亚临界结构。

### 临界压缩与听觉建模的连接

给正规形加入F e^(iωτ)，在c=0、ω=ω₀的精确共振下，转到旋转坐标可求同相锁定解，其幅度满足r³−μr=F。μ=0且F>0时r=F^(1/3)，增益r/F=F^(−2/3)；μ<0、小F时则有r≈F/|μ|。

这说明一个明确模型如何产生非线性压缩与临界敏感性，也提示临界附近恢复较慢、相位约化可能更脆弱。临界振荡曾用于毛细胞听觉敏感性的理论建模，但图3没有验证真实耳蜗必处于μ=0、能够自动调谐，或能直接预测听阈和临床获益。失谐、c≠0、噪声及额外状态都会改变响应关系。[16](#ref-nd-cochlea)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/hopf-critical-response.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/hopf-critical-response.svg" alt="超临界Hopf极限环和临界与亚阈值的共振幅度曲线" width="1400" height="550" loading="lazy" /></a><figcaption>图3　左图μ=0.2、ω₀=2π、c=0，初始半径0.12与0.8趋向√0.2。右图是精确共振下锁定幅度的代数关系，μ=0与−0.2；归一化幅度和驱动不对应实测声压或听觉增益。</figcaption></figure>

## 亚临界Hopf与大幅度振荡 为什么要交代饱和项

### 不稳定小环不等于稳定大环

亚临界的三次径向原型r′=μr+r³在μ<0时可有不稳定小环；它本身不提供稳定的大幅度环，某些初值还会有限时间无界。不能只写正三次项，就画出未由方程保证的稳定大振荡。[5](#ref-nd-hopf)

为构造一个全局有饱和的教学例子，这里**显式选择**五次扩展：

$$
\begin{aligned}
r'&=r(\mu+r^2-r^4),\\
\theta'&=2\pi,\qquad u=r^2,\\
u_\pm&=\frac{1\pm\sqrt{1+4\mu}}2.
\end{aligned}
$$

只把实且正的u当作非零环。−1/4<μ<0时，原点稳定、r₋=√u₋的小环不稳定、r₊=√u₊的大环稳定；径向导数在非零环为2u(1−2u)。两个环在μ=−1/4折叠，原点在μ=0改变稳定性。

### 环也能成为吸引域边界

μ=−0.15时，两个半径约0.42869与0.90345。初始半径小于不稳定环时趋向原点，大于它时趋向大环。静止与振荡的共存、跃迁和准静态滞后都由这个**指定五次模型**给出；一般亚临界Hopf附近的局部定理不能单独保证远处还有这样的稳定环。

五次扩展只是选择的一种饱和方式。真实系统可能存在其他吸引子、全局连接或额外分岔，不能把此图套成所有亚临界系统的完整全局结构。[15](#ref-nd-hopf-proof)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/subcritical-hysteresis.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/subcritical-hysteresis.svg" alt="五次径向模型的稳定与不稳定半径分支，以及三个初始半径的演化" width="1400" height="550" loading="lazy" /></a><figcaption>图4　μ=−0.15的两环半径约0.42869与0.90345；小环分隔原点与大环吸引域。左图为固定参数分支，不是真实扫参时间曲线。稳定大环来自显式−r⁵项，不由亚临界三次项独自保证。</figcaption></figure>

## 周期轨道的稳定性 返回映射与Floquet乘子

### 极限环稳定允许相位留下差异

**极限环**是孤立周期轨道；谐振子的连续闭轨族不构成孤立极限环。说周期轨道吸引，通常指距离那条轨道趋近，而非所有初态最终在每个时刻都与同一参考解完全重合；相位差可以保留。[4](#ref-nd-cycles)

选一个与流横截的截面，在同一方向记录返回点，得到Poincaré返回映射。周期轨道对应返回映射的固定点，p周期轨道也可能对应若干次返回后的固定点。需要说明截面、方向和最短返回约定；擦边事件、漏掉交点及重复计数都可能制造错误分支。[7](#ref-nd-poincare)

### 沿周期解积分变分方程

对周期解x*(τ)、周期T，线性扰动满足

$$
\begin{aligned}
\Phi'&=J(x_*(\tau))\Phi,\quad\Phi(0)=I,\\
M&=\Phi(T).
\end{aligned}
$$

M称为单周期矩阵，其特征值为**Floquet乘子**。自治光滑系统的非平凡周期轨道有沿时间平移方向的乘子1；横向乘子模小于1给出相应局部轨道吸引，模大于1表示不稳定，落在单位圆上则需进一步分析。Poincaré映射关注除去流方向后的横向结构。[7](#ref-nd-poincare)

在前面的μ>0 Hopf例中，径向扰动满足δr′≈−2μδr，因此横向乘子为exp(−2μT)。μ=0.2、ω₀=2π、c=0时T=1，乘子为1和约0.670320；文末把完整二维变分方程积分后独立求特征值，与径向解析值核对。乘子不是每单位时间的指数：若转成指数，需取ln|m|/T。

## Van der Pol 弱非线性与慢快振荡

### 能量输入与耗散同时存在

考虑x″−μ(1−x²)x′+x=0，μ>0。记v=x′、E=(x²+v²)/2，则E′=μ(1−x²)v²。|x|<1时能量可能增加，|x|>1时减少；“阻尼”为负的区间与大幅度耗散共同支持自持振荡，而不是外部正弦强迫。[4](#ref-nd-cycles)

该经典方程在μ>0时具有唯一稳定极限环，其结论依赖具体Liénard结构；单看“有一部分负阻尼”不足以证明任何方程都恰好有一个稳定环。μ=0时退回线性中心和闭轨族，不能说仍有同样孤立的吸引环。

μ很小时，令x≈A(τ)cos(τ+φ)，弱非线性平均给出首阶慢幅度式A′≈(μA/2)(1−A²/4)，稳定幅度近似2。这是渐近近似，未声称任意μ下振幅、相位和周期都由这一式精确给出。[14](#ref-nd-weak)

### 大μ下的慢快结构

定义y=x−x³/3−v/μ，慢时间s=τ/μ、ε=μ^(−2)，原方程可写为

$$
\begin{aligned}
\varepsilon\frac{dx}{ds}&=x-x^3/3-y,\\
\frac{dy}{ds}&=x.
\end{aligned}
$$

ε很小时，轨迹在立方曲线附近慢行，再在折点附近快速转换；冻结y的快子系统在|x|>1的外支有负局部导数。这个分解解释图5的弛张振荡，但折点附近不能把ε直接设为0后继续假装近似处处一致。更复杂慢快系统还可能出现不同结构，不能仅凭尖锐波形就判断存在同一机制。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/van-der-pol.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/van-der-pol.svg" alt="Van der Pol在小μ与大μ下的波形和相轨道" width="1400" height="550" loading="lazy" /></a><figcaption>图5　μ分别0.2与5，初态(x,v)=(0.5,0)，舍弃前160时间单位，绘到200。大μ呈慢快交替；两条曲线不特意对齐相位。全部为数值教学状态，非毛细胞或神经发放记录。</figcaption></figure>

## Duffing受迫振动 共振弯曲不等于混沌

### 立方刚度与高次谐波

选择x″+2ζx′+x+αx³=Fcos(Ωτ)。ζ≥0是归一化阻尼，α为立方刚度系数，F为驱动幅度。正α在此约定下硬化；负α可给局部软化，但纯负四次势能在远处不再有下界，不能据局部软化模型保证全局有界。[14](#ref-nd-weak)

取基波近似x≈Acos(Ωτ−φ)，用cos³θ=(3cosθ+cos3θ)/4并暂时忽略三次谐波，得到一阶谐波平衡关系：

$$
\begin{aligned}
D(A,\Omega)&=1+3\alpha A^2/4-\Omega^2,\\
F^2&=A^2\{D^2+(2\zeta\Omega)^2\}.
\end{aligned}
$$

自由振荡的相应近似骨干线为Ω≈√(1+3αA²/4)。它是小振幅、弱非线性视角的近似，不是含任意高次谐波的精确频率。相位滞后还需根据D与2ζΩ所在象限计算，不能只取不辨象限的反正切。[14](#ref-nd-weak)

### 多个代数根需要进一步判定

图6在ζ=0.05、α=1、F=0.2下绘出全部正幅度候选根。某些频率处有多个根，不等于每个根都对应真实稳定周期解；较大幅度处被忽略谐波的误差也可能增大。稳定性需用平均系统、周期轨道变分或其他适用分析继续判断，跳跃还取决于实际扫参路径与暂态。

受迫Duffing在其他参数下可以出现复杂行为，但“幅频曲线弯曲”“有谐波”或“有滞后”本身均不是混沌证据。二阶受迫系统还要保留外驱相位；若把它自治化，状态维数增加，不能直接套无外驱平面自治系统的限制。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/duffing-balance.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/duffing-balance.svg" alt="硬化与软化的小振幅骨干线，以及硬化Duffing的一阶谐波平衡候选幅度" width="1400" height="550" loading="lazy" /></a><figcaption>图6　左图只绘A≤0.7的近似关系；负α的远场有界性未获保证。右图全部正实候选根都用同色，不标成稳定或不稳定，不冒充精确扫频响应或混沌分岔。</figcaption></figure>

## 相位约化与同步 锁定不要求相位差为零

### 振幅何时可以暂时不跟踪

在具有稳定极限环、横向恢复足够快且扰动较弱等条件下，可用渐近相位描述主要演化，并通过相位响应函数与平均得到简化的相位动力学。接近Hopf临界点时横向恢复可能很慢，强迫也可能显著改变振幅，此时仅保留相位未必合适。[14](#ref-nd-weak)[5](#ref-nd-hopf)

为给出可完整复算的例子，选定约化模型ψ′=Δ−Ksinψ，K≥0。ψ为振子相对驱动的相位差，Δ为失谐，K为有效耦合；它不是所有振子的通用精确方程。|Δ|<K时有稳定锁定解ψ*=arcsin(Δ/K)，其线性恢复率为−√(K²−Δ²)；另一个相位平衡不稳定。

### 锁定区 滑移与边界

图7中的楔形区域是该模型的1:1锁定区，常用Arnold舌语言描述。稳定相位差一般不为零；频率锁定也不要求两个完整波形相同。K=1、Δ=0.4时ψ*≈0.41152 rad，恢复率约−0.91652；接近边界时恢复变慢。

|Δ|>K时没有相位平衡，展开相位持续滑移，其长期平均速率为sgn(Δ)√(Δ²−K²)。这可通过对一整周的时间积分得到；Δ=1.3、K=1时约0.83066 rad/τ。边界|Δ|=K是非双曲情况，不能简单说与内部具有相同指数锁定速度。

**受迫牵引**与**相互同步**要区分；共同驱动也能使两记录呈现相似相位，不能只据锁定图形判断存在直接神经耦合或因果方向。听觉神经中常用的[锁相](../phase-locking/)还包含刺激时序与放电概率的测量含义，不自动等同这个确定性相位方程。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/phase-locking.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/phase-locking.svg" alt="Adler型相位模型的楔形锁定区，以及锁定与相位滑移的时间曲线" width="1400" height="550" loading="lazy" /></a><figcaption>图7　ψ′=Δ−Ksinψ；K=1，Δ=0.4与1.3，初始展开相位2 rad。图中区域只对这个约化模型成立，不把所有同步边界都假定为直线，也不从相似相位推出生物因果耦合。</figcaption></figure>

## 离散映射 倍周期与混沌窗口

### 映射与连续流不能混用维数直觉

离散系统xₙ₊₁=f(xₙ)每一步更新一次；一维映射可以折叠区间、失去可逆性，与满足唯一性的一维实直线自治流不同。以Logistic映射fᵣ(x)=rx(1−x)、0≤r≤4、x∈[0,1]为例，它在该区间保持有界。[11](#ref-nd-maps)

固定点的局部乘子为f′(x*)，模小于1时吸引。p周期轨道的乘子是沿周期导数乘积，而不是把某一步导数单独拿出来判断：m=∏ₖ₌₀^(p−1)f′(xₖ)。乘子通过−1可在适当非退化条件下产生倍周期；通过+1及复杂单位根还可能对应其他分岔，不能只按分支数量命名。

r=3时非零固定点的乘子达到−1。非平凡二周期在3<r<1+√6时吸引，其乘子为−r²+2r+4；r=3.2时约0.16。图8展示连续改变参数时的数值样本、倍周期及周期窗口，不能概括为r越大越随机或所有参数都混沌。

### 典型轨道与特殊初值

r=4时，对Lebesgue几乎处处的区间内初值，典型长期Lyapunov指数为ln2；这一结论与不变密度及正弦平方变量变换有关，不是由一次有限模拟证明。x₀=3/4却给出不稳定固定轨道，序列本身恒定；它的正局部指数不把这条恒定序列变成不规则振荡。[11](#ref-nd-maps)

“几乎处处”允许测度为零的例外，并不等于每一个初值。有限精度计算的可表示状态数有限，某些迭代最终还会落入数值周期；不能把计算机上足够长的一段不重复当成无穷时间非周期性的证明。

倍周期、间歇与准周期失稳是不同的复杂化路径；**准周期**可由不可公度频率形成有界非周期运动，却不必有正最大指数。不同系统不要求经过同一串分岔，更不能仅凭复杂波形倒推出唯一演化路径。[12](#ref-nd-intermittency)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/logistic-chaos.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/logistic-chaos.svg" alt="Logistic映射的数值分岔图和有限步导数平均" width="1400" height="750" loading="lazy" /></a><figcaption>图8　1000个r从2.8到4，各舍弃1600步；上图绘最后128步，下图累计400步log|f′|。下图纵轴截于−2，深尖谷未完整显示；这些是有限精度有限时长样本，不逐参数证明无穷时间吸引子或混沌。</figcaption></figure>

## Lyapunov指数 怎样量化沿轨道的伸长

### 局部特征值 长期指数与Lyapunov函数

沿轨道的微扰满足δx′=J(x(τ))δx；方向随演化改变，所以不能一般地把每个时刻Jacobian的最大特征值平均就当成最大Lyapunov指数。令Φ(0)=I、Φ′=J(x(τ))Φ，对非零初始切向量v，在极限存在时定义

$$
\lambda(v)=\lim_{T\to\infty}\frac1T
\ln\frac{\|\Phi(T)v\|}{\|v\|}.
$$

它描述该方向的渐近单位时间对数增长；适当正则条件下可组织为Lyapunov谱。最大指数对应最强的渐近切向伸长，完整谱可由变分矩阵长期演化和重正交估计。[10](#ref-nd-lyapunov)

**Lyapunov指数**描述沿轨道的切向增长，**Lyapunov函数**是用于稳定性论证的标量函数，两者不是同一概念。正指数也不独自证明混沌：x′=x具有指数1却无界；不稳定平衡或周期轨道也可能具有正横向指数。讨论混沌时还要明确有界不变集合、典型轨道、长期行为与采用的定义。[8](#ref-nd-strange)

混沌在不同数学语境下有不同严格定义，敏感依赖、拓扑混合和正指数并非在任何系统中都可无条件互换。本文将确定性、有界的长期复杂演化作为讨论背景，把有限时间指数作为模型数值证据，不把一项指标当作普适充分必要判据。

### 为什么需要重归一化或QR

直接跟踪两条有限距离轨迹，其间距会受非线性饱和和吸引子尺寸限制；后期log距离斜率趋于0不代表真正切向指数为0。对已知方程，可积分变分方程，定期归一化；完整谱可每隔Δτ把当前演化的切向基做QR分解，以Q重新启动，并累加各|Rᵢᵢ|的对数：

$$
\begin{aligned}
\widehat\lambda_i(T)&=\frac1T\sum_{k=1}^{m}\ln|R_{ii}^{(k)}|,\\
T&=m\Delta\tau.
\end{aligned}
$$

这仍是数值估计。需报告暂态舍弃、累计时间、积分容差、最大内部步长、重正交间隔与敏感性检查。中性方向的有限平均未必恰好为0，不应把小正数或小负数直接解释成分岔已发生。[10](#ref-nd-lyapunov)[18](#ref-nd-ivp)

## Lorenz模型 有界复杂演化与数值证据

选择经典参数σ=10、ρ=28、β=8/3：

$$
\begin{aligned}
x'&=\sigma(y-x),\\
y'&=x(\rho-z)-y,\\
z'&=xy-\beta z.
\end{aligned}
$$

这些状态来自归一化对流模型背景，不是三个实测声压通道。其散度恒为−σ−1−β=−41/3，相体积收缩；这不表示每个方向都收缩，也不单独保证任何负散度系统有界或混沌。[3](#ref-nd-dissipation)[9](#ref-nd-lorenz)

图9以初值(1,1,1)绘出一段暂态后的轨道；另从相同模型预热30时间单位，再累计240单位，按0.5间隔做QR。完整实验脚本及记录保存有限时间指数；正、近零、负方向与相体积收缩和非平稳轨道的常见结构相容，但这一次计算不是Lorenz吸引子存在或混沌的严格证明。

独立检查包括：三个指数之和应接近−41/3，改变累计时间、容差、最大步长和QR间隔后，定性伸长结构应稳健。求和对上只核对总体体积增长，不保证每个指数、每段轨道和所有分岔位置都正确。[9](#ref-nd-lorenz)[10](#ref-nd-lyapunov)

对于光滑平面自治流，Poincaré–Bendixson结论在相应紧性、无平衡等条件下限制极限集合，不能出现同样的Lorenz式吸引子；但外驱相位、时滞、离散映射或更高维状态会改变问题。模型维数与观测通道数也不是同一个量。[4](#ref-nd-cycles)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/lorenz-exponents.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/lorenz-exponents.svg" alt="Lorenz三维轨道和三个QR方向的累计平均指数" width="1400" height="550" loading="lazy" /></a><figcaption>图9　轨道图绘τ=25至65；指数计算另预热30、累计240、每0.5重正交，DOP853的rtol为10⁻⁹、atol为10⁻¹¹、max_step为0.04。有限时间曲线不是数学混沌证明；独立时长和精度检查另有记录。</figcaption></figure>

## 从模型走到数据 为什么混沌检测更困难

### 观测量不等于完整状态

麦克风、电极或运动传感器记录的是测量函数、噪声与处理后的数据；一条标量波形未必足以区分不同内部状态。延迟坐标把y(t)、y(t−Δ)、y(t−2Δ)等并列，可在适当确定性、光滑性和泛型条件下帮助重构状态结构，但不是对任意有限、含噪、非平稳记录都自动成立的恢复保证。[17](#ref-nd-surrogates)

嵌入维数、延迟、采样率、记录长度和滤波会改变结果。邻近点可能只是同一轨迹相邻时刻，实际估计需处理时间相关；噪声可制造表观发散或维数增加，过度滤波也可能制造平滑低维外观。模型中已知Jacobian的QR计算，与只从观测序列估计指数，不是同一证据强度。

### 宽谱 非线性与随机性分别检验

图10对比确定性Logistic序列与独立高斯随机序列，两者都可有不规则波形和宽频谱。宽谱不独自区分确定性混沌与随机过程；反过来，谱线、非正态分布或非线性相关也不能直接提供混沌证书。[6](#ref-nd-spectral)

**替代数据检验**先明确某种零假设，例如给定条件下的线性随机过程或其静态观测变换，再生成符合该假设的替代序列，比较预先指定统计量。拒绝这个零假设，只排除该假设及其适用条件，不等于排除一切随机模型或证明确定性混沌。非平稳性、样本不足和多次调参会改变假阳性解释。[17](#ref-nd-surrogates)

实际听觉、发声和神经节律研究应先记录刺激、任务、测量噪声、伪迹与预处理，区分状态漂移、外部驱动和内部动力学。模型预测、独立数据、参数扰动与可重复效应相互约束，比对单一漂亮图形赋予机制更可靠。可配合[计算神经科学](../computational-neuroscience/)、[生物物理学](../biophysics/)及[控制理论](../control-theory/)阅读。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/nonlinear-dynamics/data-evidence.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/nonlinear-dynamics/data-evidence.svg" alt="确定性Logistic序列和独立高斯随机序列的不规则波形及宽谱" width="1400" height="550" loading="lazy" /></a><figcaption>图10　每条序列8192点，分别中心化并按标准差归一；左图只显示前160点，红线为便于辨认纵向平移4。右图Welch窗长512、采样率1步⁻¹，单位为归一化序列的PSD，不对应声压谱。这里没有实施替代数据显著性检验。</figcaption></figure>

## 三个可以独立运行的小实验

以下使用Python、NumPy与SciPy，已在Python 3.11、NumPy 1.26.4、SciPy 1.17.1运行。所有时间与状态均为归一化量，容差是求解器局部误差控制参数，不是对真实全局误差的严格证明。[18](#ref-nd-ivp)

### 一 计算多稳态分支和折点

先解固定参数平衡，再检查导数；不要把求根成功自动当成稳定。折点处根退化，应结合解析条件而非浮点根的微小虚部判断。

```python
import numpy as np
fold = 2/(3*np.sqrt(3))
print('fold h:', -fold, fold)
for h in [-.5, 0., .5]:
    roots = np.roots([1., 0., -1., -h])
    real = np.sort(roots.real[np.abs(roots.imag) < 1e-9])
    derivative = 1-3*real**2
    print('h, equilibria, derivatives:', h, real, derivative)
    if h == 0.:
        assert np.allclose(real, [-1, 0, 1])
        assert np.allclose(derivative, [-2, 1, -2])
```

### 二 用二维变分方程核对Hopf乘子

μ=0.2、ω₀=2π、c=0，初始点就在已知极限环上，避免把尚未达到周期轨道的暂态误当单周期。积分状态和2×2基本矩阵，最后再求特征值。

```python
import numpy as np
from scipy.integrate import solve_ivp
mu, omega = .2, 2*np.pi
def augmented(t, z):
    x, y = z[:2]
    r2 = x*x+y*y
    state = [(mu-r2)*x-omega*y, omega*x+(mu-r2)*y]
    jac = np.array([[mu-3*x*x-y*y, -omega-2*x*y],
                    [omega-2*x*y, mu-x*x-3*y*y]])
    return np.r_[state, (jac @ z[2:].reshape(2, 2)).ravel()]
initial = np.r_[np.sqrt(mu), 0., np.eye(2).ravel()]
sol = solve_ivp(augmented, (0, 1), initial, method='DOP853',
                rtol=1e-11, atol=1e-13, max_step=.02)
assert sol.success
multipliers = np.linalg.eigvals(sol.y[2:, -1].reshape(2, 2))
assert np.allclose(np.sort(multipliers.real), [np.exp(-.4), 1], atol=1e-9)
assert np.max(np.abs(multipliers.imag)) < 1e-10
print('Floquet multipliers:', multipliers)
```

### 三 对比吸引二周期和典型r=4轨道

同时检查周期乘子与有限步导数平均。这里从已知模型算导数，不是从含噪录音估计指数；r=4的理论典型值ln2不由本次有限迭代证明。

```python
import numpy as np
def series(r, n=20000):
    x = .1234567
    for _ in range(1000):
        x = r*x*(1-x)
    values = []
    for _ in range(n):
        values.append(x)
        x = r*x*(1-x)
    return np.array(values)
r = 3.2
x = series(r)
multiplier = np.prod(r*(1-2*x[-2:]))
assert np.isclose(multiplier, -r*r+2*r+4)
print('r=3.2 cycle and multiplier:', x[-2:], multiplier)
y = series(4.)
exponent = np.mean(np.log(np.abs(4*(1-2*y))))
print('r=4 finite estimate, typical exact value:', exponent, np.log(2))
assert abs(exponent-np.log(2)) < .005
assert 4*.75*(1-.75) == .75
```

## 常见误解与阅读检查

| 容易混淆的说法 | 需要补上的判断 |
| --- | --- |
| 非线性系统都会混沌 | 区分平衡、稳定周期、准周期、混沌与无界演化 |
| 特征值到了虚轴就一定发生Hopf | 检查非零频率、穿越、其余谱与非退化非线性条件 |
| 亚临界Hopf自然保证稳定大环 | 说明局部定理之外的饱和项、全局结构与吸引域 |
| S形分支就是实际滞后时间曲线 | 区分固定参数平衡、稳定性、扫参速率和噪声 |
| 谐波平衡每个正根都稳定 | 检查近似误差、实际周期解及其横向乘子 |
| 同步等于零相位差或直接耦合 | 说明频率关系、相位定义、共同驱动和因果检验 |
| 正有限指数或宽谱证明混沌 | 检查有界背景、典型轨道、时长、数值稳健性与随机零假设 |
| 指数求和与散度一致就全部正确 | 这只核对总体体积增长，个别指数和轨道仍需其他检查 |

读完应能解释多稳态与吸引域，复算折点、瓶颈时间及Hopf乘子，说明相位约化与谐波平衡的假设，并把模型混沌证据与实验推断分开。本篇完成的是定义、来源、解析、数值和页面核查，保留AI辅助草稿及专业审阅待完成标记。
