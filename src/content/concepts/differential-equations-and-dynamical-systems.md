---
title: "微分方程与动力系统"
english: "Differential Equations and Dynamical Systems"
slug: "differential-equations-and-dynamical-systems"
summary: "从变化率、初值和解的存在唯一性进入线性振动、相图、非线性稳定性、极限环与分岔，再区分连续和离散混沌、偏微分方程及数值证据；用可复算模型理解一条解与一类演化的关系。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "微分方程", "动力系统", "初值问题", "相图", "极限环", "分岔", "混沌"]
aliases: ["Differential Equations and Dynamical Systems", "微分方程与动力学", "常微分方程与动力系统", "动力系统基础"]
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
  - {label: "研究对象", value: "由变化规律和初始状态决定的演化，以及一类轨道的结构与长期行为"}
  - {label: "核心区别", value: "局部存在、唯一、全局延续、稳定、周期与混沌需要分别判断"}
  - {label: "研究连接", value: "声学振动、波与扩散、膜电位和网络模型、反馈及计算仿真"}
  - {label: "重要边界", value: "线性化、相图和有限仿真各有适用范围，形状像振荡或混沌不构成证明"}
references: ["dds-existence", "dds-separable", "dds-linear", "dds-autonomous", "dds-second", "dds-forced", "dds-systems", "dds-jordan", "dds-linearization", "dds-nonhyperbolic", "dds-limit", "dds-heat", "dds-wave", "dds-bifurcation", "dds-phase", "dds-contraction", "dds-cycle", "dds-hopf", "dds-poincare", "dds-lorenz", "dds-lyap-exponent", "dds-logistic", "dds-lyapunov", "dds-ivp-api", "dds-picard"]
order: 1018
---

**微分方程**（differential equations）用未知函数及其导数之间的关系描述变化规律；**动力系统**（dynamical systems）进一步研究状态如何随时间演化、轨道怎样组织，以及长期行为如何随初值和参数改变。前者常从“怎样求解”进入，后者还问“即使没有显式公式，能否判断稳定、振荡、分岔或预测边界”。[1](#ref-dds-existence)[14](#ref-dds-bifurcation)

声学振动、波传播、扩散、膜电位、神经网络和反馈回路都可能采用微分方程模型。但写出方程只是一种建模选择，还需说明变量、单位、初始与边界条件、参数来源，以及哪些观察能够检验模型。[控制理论](../control-theory/)更侧重如何改变动态，本篇更侧重解及其演化结构；[数学物理方法](../mathematical-physics-methods/)则进一步发展连续场、边界与求解工具。

十幅图和全部程序是指定模型的原创教学绘图与复算，不是听者、动物、房间或器件实测。经典反例与标准模型用于解释数学边界，不宣称它们直接验证了某种听觉机制。文末有三个短程序，并提供[完整实验脚本](/n3-hearingpedia/code/differential-equations-and-dynamical-systems/experiments.py)。

多稳态与吸引域、鞍结瓶颈、超/亚临界Hopf、周期轨道的Floquet稳定性、慢快振荡、同步及混沌证据，可配合[非线性动力学](../nonlinear-dynamics/)进一步阅读；两篇共同保留局部判据、全局行为与有限数值计算的边界。

从机械质量、弹性与阻尼出发，系统学习共振、模态、声压与净声强、三类阻抗、分贝和管腔边界，可配合基础课程[振动与声学基础](../vibrations-and-acoustics/)阅读；该篇另用可复算模型核对单位、相位与能量。

## 阅读准备与独立阅读

**起步知识。** 会读曲线、理解正负号和“每单位时间改变多少”即可先看方向场。导数是局部变化率，积分是变化率的累积；矩阵、特征值和复数会在需要处说明。严格定理证明、一般偏微分方程和混沌理论仍需后续数学训练。

**随用随补。** 状态x可以是一个数，也可以是向量；向量是一列描述系统当前情况的数。矩阵Ax表示按行乘积求和，特征值帮助识别线性模态的增长、衰减与旋转。长度采用 $\|x\|_2=\sqrt{\sum_i x_i^2}$；不同物理单位的分量先按明确尺度归一化，避免把米和米每秒直接当作同一种量相加。

**分层阅读。** 第一遍看初值、爆破、振动、相图和能量。第二遍读唯一性、线性化、极限环与分岔。第三遍再看返回映射、混沌指标、偏微分方程和计算核验。需要推导时按点补读[微积分](../calculus/)、[线性代数](../linear-algebra/)、[概率论](../probability-theory/)及[数值分析](../numerical-analysis/)，不把完整修完这些课程设为阅读门槛。

教学计算统一使用τ=t/T₀、T₀=1秒，撇号表示对τ求导；状态按各自尺度无量纲化。PDE另用ξ=x/L₀表示归一化空间位置。归一化角频率ω对应ω/(2πT₀) Hz；真实模型仍须报告位移、声压、电压、扩散系数等物理单位，不能把本篇数值直接解释为实测参数。

## 从变化规律到初值问题

### 方程约束变化 初值选择一条解

常微分方程（ODE）的未知函数只依赖一个独立变量，例如x′=f(τ,x)。一个解是在某个区间内可微、逐点满足方程的函数；加入x(τ₀)=x₀后构成初值问题。不能只写一个输出数组，就省略它对应的方程、初态和时间区间。

例x′=1.2x(1−x)中，状态很小且为正时增长，为1时变化率为0，大于1时下降。初值为0时解恒为0；正初值的解为

$$
x(\tau)=\frac{1}{1+(1/x_0-1)e^{-1.2\tau}},
\qquad x_0>0.
$$

不同初值生成不同曲线，但都服从同一个变化率规律。图1用短箭头表示每个位置的斜率；箭头给局部方向，整条曲线还须满足初始条件及连续演化。

### 阶数 线性与自治是不同分类

阶数由出现的最高阶导数决定。q″+aq′+bq=g(τ)是二阶方程，需要两个初始数据；若最高阶系数退化为0，不能继续无条件按原阶数处理。线性表示未知函数及其导数只以线性方式出现，系数可以依赖时间；x′+sin(τ)x=τ仍是线性的，x′+sin(x)=0则不是。

自治方程x′=f(x)不显含时间，其向量场在每一时刻相同。非自治方程x′=f(τ,x)还依赖外部时间；必要时可增加一个满足τ′=1的变量，把它改写成更高维自治系统。偏微分方程（PDE）的未知量依赖时间和空间等多个变量，初值通常是一整个函数，还需相应边界条件。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/slope-initial.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/slope-initial.svg" alt="Logistic微分方程的方向场和四个初值下的解，正初值趋向1而零初值保持零。" width="1400" height="550" loading="lazy" /></a><figcaption>图1　同一方程不等于只有同一条曲线。x′=1.2x(1−x)，初值分别0、0.15、0.6和1.4，横轴τ∈[0,6]；左侧箭头仅为方向显示，长度作归一化。纵轴不是声压、发放率或实测人口，而是无量纲教学状态。</figcaption></figure>

## 解何时存在 唯一并能够延续

### 局部Lipschitz条件限制状态差异的放大

有限维初值问题的一个常用充分条件是：初值位于定义域内部，f关于时间与状态连续，并在附近对状态满足局部Lipschitz条件。其含义是可取有限L，使同一时间的两状态满足‖f(τ,x)−f(τ,y)‖≤L‖x−y‖；相应邻域内的时间使用同一个界。Picard–Lindelöf定理由此保证局部存在且唯一。[25](#ref-dds-picard)

若f对状态的一阶偏导在邻域内连续，是容易检查的更强充分条件。充分条件不等于必要条件：定理假设不满足，只能说这条定理不能直接使用，不能立刻宣称没有解或不唯一。[1](#ref-dds-existence)

仅有连续性不足以保证唯一。x′=2√|x|、x(0)=0允许先在0等待任意c≥0，再取x(τ)=(τ−c)²，也允许始终保持0；接点的一阶导数也满足方程。这里无法把同一初值解释为唯一确定的未来。

### 光滑方程也可能有限时间爆破

x′=x²、x(0)=1的解为1/(1−τ)，包含初始时刻的最大存在区间是(−∞,1)。右端非常光滑，解却在τ→1⁻时无界。因此局部存在唯一不保证对任意长时间都有有限解；把分母越过0后的另一段表达拼接过来，不是原初值问题的连续延续。[1](#ref-dds-existence)[25](#ref-dds-picard)

在一个有限时间端点之前，如果(τ,x(τ))始终留在定义域内部的某个闭且有界的区域（紧集）内，右端保持上述正则性，就可把解延拓过该端点；若接近定义域边界或状态无界，则需要另外分析。这里把时间也纳入定义域检查，避免漏掉时间系数本身的奇点。求解器在爆破附近失败可能反映模型的有限寿命，但一次失败也不能单独证明爆破。

### 连续依赖不等于长期预测永远准确

同一右端满足Lipschitz界、两条解始终处于该界覆盖的共同区域时，初值差可由 $e^{L|\tau-\tau_0|}\|x_0-y_0\|$ 控制。这说明有限时间的小初值误差有相应上界；时间变长时上界可能很大，不能把连续依赖误读为无限期可预测。[25](#ref-dds-picard)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/existence-uniqueness.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/existence-uniqueness.svg" alt="连续但非Lipschitz方程允许不同等待时间的解；另一个光滑方程的解在有限时间无界。" width="1400" height="550" loading="lazy" /></a><figcaption>图2　不同假设对应不同结论。左图x′=2√|x|、x(0)=0，展示等待0、1和2后启动及恒零解；右图是另一方程x′=x²、x(0)=1，仅绘τ≤0.97并标出终点1，不把竖线当作数值解已到达无穷。全部量归一化。</figcaption></figure>

## 解析方法如何揭示线性与受迫振动

### 分离变量与积分因子都需要保留条件

对x′=a(τ)b(x)，在b(x)≠0的区域可分离为dx/b(x)=a(τ)dτ，再积分并施加初值。除以b(x)时可能丢掉b(x)=0对应的平衡解；图1的x=0和x=1就应单独保留。隐式解还需说明选定分支、定义域以及能否跨过奇点。[2](#ref-dds-separable)

对线性方程x′+a(τ)x=b(τ)，积分因子M(τ)=exp(∫a(τ)dτ)把左端变成(Mx)′，因此Mx等于∫Mb再加积分常数。这把方程转为累积计算，而不是要求记住每个输入形状的现成答案。[3](#ref-dds-linear)

齐次线性方程的解可叠加；非齐次方程的解是“一个特解加任意齐次解”。两个对应同一非零输入的解直接相加，通常会把输入也加倍，不能把齐次叠加规则无条件套用。

### 二阶方程可以化成一阶状态系统

机械例m q̈+bq̇+kq=F(t)中，m>0为质量，b为黏性阻尼，k为刚度，F为力。取状态(q,q̇)便得到两个一阶方程；在原物理尺度中，质量、阻尼和刚度分别与kg、kg/s、N/m对应。初始位移与初始速度都需要给出。

常系数齐次方程的指数试探q=eˢᵗ给出特征多项式，实根、复根和重根决定基本解。若有重根，可能需要t eˢᵗ等附加项，而不只是重复写同一个指数。对有阻尼振子，ω₀=√(k/m)为无阻尼自然角频率，ζ=b/(2√(mk))为阻尼比。[5](#ref-dds-second)

### 共振取决于阻尼 输入与观察量

图3的归一化方程为q″+4ζq′+4q=0.4cos(ωτ)，初始位移与速度均0。ζ=0、ω=2时恰好共振，解为0.1τsin(2τ)，振幅随时间增长；加入ζ=0.1后，同频输入的稳态幅值有限。[6](#ref-dds-forced)

阻尼情况下位移稳态幅值为0.4/√[(4−ω²)²+(4ζω)²]。一般标准振子的位移幅值峰在ω₀√(1−2ζ²)，要求0<ζ<1/√2；这不是所有阻尼下都存在的非零频率峰。速度、位移和不同电路输出的峰值也可能不同，应先明确观察量。幅值变大更不自动证明非线性极限环或真实听觉放大机制。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/forced-oscillation.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/forced-oscillation.svg" alt="无阻尼共振位移持续增长而有阻尼响应有界，稳态幅频曲线的峰值随阻尼改变。" width="1400" height="550" loading="lazy" /></a><figcaption>图3　共振与自持振荡要分开。左图ω=2、ζ为0与0.1，时间区间[0,30]；右图分别计算ζ=0.1和0.5的稳态位移幅值。左图含零初态暂态，右图是稳态公式，二者不是相同的观测时刻。归一化位移与强迫量不代表具体器件。</figcaption></figure>

## 从一条解到相空间中的流

### 状态空间与轨道的含义

状态空间的每一点代表一种当前状态。自治方程x′=f(x)在各点给出一个速度向量；随时间得到的x(τ)称为轨迹，轨迹在状态空间中经过的点集称为轨道。满足f(x⋆)=0的点是平衡点。相图把这些方向、平衡和轨道放在一起，不以时间为某一个坐标轴。[4](#ref-dds-autonomous)[9](#ref-dds-linearization)

在解唯一的自治系统完整状态空间中，两条轨道若相交，就属于同一轨道，不能相交后再分叉。不同投影中曲线交叉并不违反唯一性；非自治系统在同一状态、不同外部时间的速度也可不同，必要时须把时间一起纳入状态。

在实直线上的一维光滑自治流中，非平衡解沿方向单调移动，不会产生非平凡周期轨道。二维相图可以出现旋转与闭轨，离散映射还可能折叠并合并不同状态；不能用同一条维数直觉概括所有动力系统。

### 矩阵指数描述常系数线性流

对常矩阵A的系统x′=Ax，矩阵指数描述初态的传播：

$$
x(\tau)=e^{A\tau}x_0.
$$

矩阵指数通过幂级数或等价线性演化定义，不是对矩阵每个元素分别取指数。加入输入g(τ)后，变常数公式把初态项与 $\int_0^\tau e^{A(\tau-s)}g(s)\,ds$ 相加。这里A为常矩阵；若A随时间变，通常需要基本解矩阵，不能随意用exp(∫A)代替，除非满足相应可交换等条件。[7](#ref-dds-systems)

图4的结点沿实方向衰减，焦点一边旋转一边衰减，鞍点同时有收缩与扩张方向，中心则沿闭合轨道运动。常系数线性系统的所有特征值实部严格为负时才渐近稳定；纯虚特征值还需检查重根及Jordan结构，不能只看“实部不大于0”。[8](#ref-dds-jordan)

即使全部特征值为负，也可能先放大再衰减。例如A=[[-1,10],[0,−1]]、x₀=(0,1)给出 $x_1(\tau)=10\tau e^{-\tau}$，先到10/e再回落。渐近稳定描述长期趋势，并不保证任意范数从起点就单调下降。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/linear-phase-portraits.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/linear-phase-portraits.svg" alt="四个线性系统的方向场与轨道，分别展示稳定结点、稳定焦点、鞍点和中心。" width="1400" height="900" loading="lazy" /></a><figcaption>图4　相图的横纵轴都是状态分量。四个常矩阵及其位置在图中标出，各用三个相同初态(1.5,0.6)、(−0.6,1.4)、(1.1,−1.3)，彩色圆点为起点；轨道用矩阵指数传播τ∈[0,12]，超出显示框的部分不画。中心的闭轨族没有单独吸引附近轨道。</figcaption></figure>

## 非线性稳定性与能量方法

### 局部线性化能回答哪些问题

对足够光滑的自治系统，在平衡点附近令δx=x−x⋆，一阶近似为δx′≈Jδx，J是f的偏导数组成的Jacobian。没有特征值实部为0的平衡点称为双曲平衡点；在相应光滑条件下，线性化保留其局部定性轨道结构，但不保证相同振幅、时间标度或全局吸引域。[9](#ref-dds-linearization)

若所有特征值实部为负，平衡点局部渐近稳定；有正实部方向则不稳定。若出现零实部，线性化可能不足以判断：x′=−x³与x′=x³在0处的线性化都是0，稳定性却相反。非双曲点往往需要高阶项、Lyapunov方法或中心流形等进一步分析。[10](#ref-dds-nonhyperbolic)

### 稳定与渐近稳定不等于同一个结论

Lyapunov稳定表示小初始偏差使轨迹始终留在指定小邻域；渐近稳定还要求轨迹最终回到平衡点。指数稳定进一步用指数界控制衰减。对局部Lipschitz系统，若找到连续可微V，原点处V=0、附近非零处V>0，且沿轨迹V′≤0，可给出局部稳定证据；若非零处V′<0，可得局部渐近稳定。[23](#ref-dds-lyapunov)

V可以是物理能量，也可以是为证明构造的函数。V′仅半负时，还需检查解能长期停留的最大不变集，不能直接宣布收敛到原点。全局结论还要求全局范围、轨迹延续与适当有界性；把局部图画得更大不等于证明全局稳定。

### 阻尼摆为何收敛 无阻尼摆为何有闭轨

取θ′=v、v′=−sinθ−γv。函数V=v²/2+1−cosθ满足V′=−γv²；γ=0时能量守恒，低能量轨道围绕下垂平衡点闭合。γ>0时，虽然v=0处V′暂时为0，但除平衡点外轨道不能一直留在那里。

在包含θ=0、满足|θ|<π且V<2的势阱内，可用适当紧的正不变子水平集和LaSalle分析说明收敛到(0,0)。这不表示整个实角度轴上任意初态都收敛到同一个0；其他势阱、上方平衡和角度周期性都需要区分。[15](#ref-dds-phase)[23](#ref-dds-lyapunov)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/pendulum-energy.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/pendulum-energy.svg" alt="同一摆初态在无阻尼时沿闭轨运动，在阻尼下盘旋接近平衡，能量曲线分别守恒和下降。" width="1400" height="550" loading="lazy" /></a><figcaption>图5　能量恒等式比单条曲线提供更多信息。初态θ=1.4 rad、v=0，γ取0与0.4；初能量约0.8300，小于势垒2。数值积分采用DOP853、rtol=10⁻¹¹、atol=10⁻¹³、max_step=0.03，τ∈[0,20]。能量守恒或耗散另外用解析导数和独立积分核对。</figcaption></figure>

## 周期轨道 极限环与返回映射

### 闭合曲线何时才是极限环

周期解满足x(τ+T)=x(τ)，T>0；非平衡周期轨道若在邻近没有其他周期轨道，称为极限环。极限环可以稳定、不稳定或具有单侧吸引性，并不是“极限环”一词本身就意味着吸引。

无阻尼摆或线性中心附近有连续一族闭轨，任意邻域都有别的周期轨道，因此单条闭轨不属于孤立极限环。受周期输入驱动产生的稳态振荡，也不能在没有说明外部驱动与状态扩展的情况下直接称为自治系统的自持极限环。[11](#ref-dds-limit)[17](#ref-dds-cycle)

### 一个半径方程可精确解释轨道吸引

取x′=μx−2y−(x²+y²)x、y′=2x+μy−(x²+y²)y。令r=√(x²+y²)，非零处极坐标给出r′=μr−r³、角速度2。μ=1时，r=1为稳定极限环，半径小于或大于1的非零轨道都接近单位圆，周期为π。[18](#ref-dds-hopf)

吸引的是轨道集合，而不是每个初态最终落到同一个固定点。不同初相位可以一直保留相位差；这称为相应的轨道稳定性。接近平衡点与接近周期轨道是两类不同问题，不能只比较某一时刻的坐标是否一致。

### Poincaré截面把连续流变成迭代问题

在轨道横穿的截面上记录相邻返回点，得到Poincaré返回映射。横截要求流不沿着截面走；返回是否定义，还取决于轨道确实再次到达。周期轨道对应返回映射的固定点，附近返回点的收缩或扩张帮助判断其横向稳定性。[19](#ref-dds-poincare)

图6可取y=0、x>0且向上穿越的截面；每次绕一圈返回，径向扰动的一阶倍数为 $e^{-2\pi}$，约0.001867。沿周期轨道的相位方向则不具有同样收缩，这正是“轨道稳定”而非“每个点都吸引”的区别。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/limit-cycle-hopf.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/limit-cycle-hopf.svg" alt="Hopf正规形中从单位圆内外出发的轨道接近同一周期轨道，半径解趋向1而角度持续变化。" width="1400" height="550" loading="lazy" /></a><figcaption>图6　用精确半径解展示稳定极限环。μ=1、角速度2，r(0)分别0.2与2，初相位0，τ∈[0,10]；半径满足r′=r−r³，图中虚线为r=1。原点是另一个不稳定平衡点，非零轨道不会最终停在圆周某个固定位置。</figcaption></figure>

## 参数变化与分岔

### 分岔改变的是演化结构

参数改变导致平衡点数量、稳定性、周期轨道或其他定性结构发生变化，称为分岔。分岔图通常以参数为横轴，而不是时间；稳定分支和不稳定分支也不等于一次实验记录的上下波动。

鞍结正规形x′=μ−x²在μ>0有两个平衡点：+√μ稳定、−√μ不稳定；μ=0相遇，μ<0时没有实平衡点。叉形正规形x′=μx−x³则始终有0平衡点，μ>0时新增±√μ两个稳定分支，而0失稳。[14](#ref-dds-bifurcation)

叉形的理想对称结构不能无条件代表一般参数系统，轻微破坏对称就可能改变分岔形态。正规形是带有条件的局部模型，不是所有非线性系统都能逐项照搬的全局公式。

### Hopf分岔把平衡与周期轨道连起来

图6系统在μ<0时原点稳定，在μ=0附近一对复特征值穿过虚轴，μ>0出现半径√μ的稳定周期轨道，这是超临界Hopf分岔的标准例子。一般Hopf结论需要孤立的共轭特征值对、非零频率、随参数横穿虚轴，以及决定幅值的相应非线性系数不退化等条件；仅看到特征值实部为0，并不能断言必有稳定极限环。[18](#ref-dds-hopf)

亚临界Hopf、周期轨道的鞍结和全局分岔还可能给出不同的稳定性、跳变和滞后。数据中的突然转变只能提出分岔假设，还需参数变化、模型及可替代解释的核查，不能凭一张曲线确定分岔类型。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/bifurcation-branches.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/bifurcation-branches.svg" alt="鞍结与超临界叉形的平衡分支，实线稳定、虚线不稳定，参数跨过0时结构改变。" width="1400" height="550" loading="lazy" /></a><figcaption>图7　两个不同正规形的分岔图。横轴μ∈[−1,1]，纵轴为平衡位置；蓝实线表示所画非临界分支稳定，红虚线表示不稳定，灰点标出μ=0。临界点需用非线性项另判，图线不是状态随时间的运动路径。</figcaption></figure>

## 离散动力系统与倍周期

### 迭代映射不能直接套用连续流的结论

离散系统xₙ₊₁=F(xₙ)每次更新一步，可来自返回映射、采样模型或本身就是离散过程。固定点满足F(x⋆)=x⋆，对应每步保持不变；若F可微且|F′(x⋆)|<1，标量固定点局部渐近稳定，|F′|>1则不稳定，|F′|=1时仍需进一步分析。

连续时间看特征值实部，离散时间看更新因子的模，两种判据不能互换。一般离散映射还可能不可逆，使不同状态下一步合并；例如下方Logistic映射中，x与1−x得到同一输出。这与唯一光滑ODE的流有重要区别。

### Logistic映射与Logistic微分方程不是同一个模型

映射F(x)=r x(1−x)，0≤r≤4时把[0,1]映回[0,1]，但它不是图1方程的精确单位时间更新。r=3.2时，非零固定点已失稳，却有稳定二周期，两个值约0.51304和0.79946；两步导数乘积为0.16，小于1。[22](#ref-dds-logistic)

随r继续增加，可出现倍周期序列、周期窗口与混沌区域。图8只作有限暂态舍弃和有限迭代采样，窄窗口、很长暂态或临界缓慢不能靠图上点数少就排除。

r=4是经典的初值敏感例子，但不是每个初值都生成非周期序列：x₀=0.25会到0.75并保持在那里。正的典型指数不能改写为“每条轨道都同样混沌”；计算机有限精度下，确定的有界迭代还最终受有限状态集合限制。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/discrete-logistic-map.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/discrete-logistic-map.svg" alt="Logistic离散映射有限迭代的分岔采样，以及r=4时两个相近初值序列的距离变化。" width="1400" height="550" loading="lazy" /></a><figcaption>图8　连续与离散模型不可混名。左图650个r值覆盖[2.8,4]，每个从0.123456789出发，舍弃1500步，再画140步；散点层在SVG中栅格化以控制文件体积。右图r=4、两初值相差10⁻¹⁰，共70次更新，显示下限10⁻¹⁶。横轴步数不等于秒。</figcaption></figure>

## 连续系统中的混沌与预测边界

### 不规则外观不能独立证明混沌

确定系统仍可能在有界长期运动中对初值高度敏感。周期、准周期、复杂暂态、外部随机驱动和确定混沌需要区分；宽频谱、相图像“毛线团”或两条曲线分离都不是单独的充分证据。

在足够光滑的二维自治平面流中，若前向轨迹被限制在适当紧区域、其ω极限集不含平衡点，Poincaré–Bendixson结论将该长期极限集约束为周期轨道。这类条件排除了直接照搬三维Lorenz式的混沌图景；受迫二维系统、离散映射、非光滑系统或PDE不应无条件套用同一限制。[11](#ref-dds-limit)

这里ω极限集指沿时间趋向无穷时，轨迹子序列可能接近的所有极限点，不是频率ω。定理中的紧性、平衡点条件、连续时间和自治性都影响结论，缺少条件时不应仅按“有几个变量”作判断。

### Lorenz模型说明确定性与可预测性不同

图9采用三个耦合方程

$$
\begin{aligned}
x'&=\sigma(y-x),\\
y'&=x(\rho-z)-y,\\
z'&=xy-\beta z,
\end{aligned}
$$

其中σ=10、ρ=28、β=8/3。它是经典三维连续混沌模型，曲线围绕两个区域不规则切换。图中初态(1,1,1)，另一个初态只把第一分量增加10⁻⁸，二者先接近，随后距离显著增大；这展示有限时间敏感性，不能把画出的有限轨迹本身当成混沌证明。[20](#ref-dds-lorenz)

其向量场散度为−(σ+1+β)=−41/3，说明光滑流的相空间体积收缩。但体积收缩不等于每条距离都缩短，也不单独保证轨迹有界或系统混沌；这些结论需要其他结构和分析。[16](#ref-dds-contraction)

### Lyapunov指数衡量沿轨道的扰动增长

对光滑系统，小扰动由变分方程δx′=Df(x(τ))δx传播。Lyapunov指数研究这种线性化扰动的长期平均对数增长率，最大指数对应最强扩张方向；数值计算常需要暂态舍弃、反复归一化和时间收敛检查。它与用于稳定性证明的Lyapunov函数V是不同对象。[21](#ref-dds-lyap-exponent)

局部鞍点也有扩张方向，正的局部增长还须结合有界长期运动等结构解释。两条有限差轨迹最终因活动范围而饱和，不能把饱和后的距离继续拟合为指数。混沌轨迹的长期逐点预测与长期统计量也不是同一任务；改变积分精度后晚期轨道分离，并不自动说明哪一条程序写错。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/lorenz-sensitivity.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/lorenz-sensitivity.svg" alt="经典Lorenz三维轨迹及两个相差很小初值的有限时间距离，展示确定模型的预测敏感性。" width="1400" height="550" loading="lazy" /></a><figcaption>图9　指定参数下的数值展示。左图仅画基准轨迹τ∈[5,40]，右图距离覆盖[0,45]；DOP853、rtol=10⁻¹¹、atol=10⁻¹³、max_step=0.025，每0.01输出。纵轴对数、下限10⁻¹⁶；没有用这条距离曲线给出经认证的长期指数或一般混沌证明。</figcaption></figure>

## 偏微分方程 初始形状与边界

### 空间场需要函数作为状态

热方程uτ=κuξξ描述扩散，κ>0；波动方程uττ=c²uξξ描述传播，c>0。一个需要初始场u(ξ,0)，另一个还需初始速度uτ(ξ,0)，二者都需要相应空间边界条件。状态是一整个函数，不能因写了一个字母u就当作一维状态。

图10取ξ∈[0,1]、两端u=0、初形sin(πξ)+0.25sin(3πξ)，波动初速为0。正弦满足这些固定端条件，空间求二阶导后给出−n²π²倍，所以可逐模态求解：热模态按exp(−κn²π²τ)衰减，波模态按cos(cnπτ)振荡。[12](#ref-dds-heat)[13](#ref-dds-wave)

归一化κ=0.08对应物理扩散系数0.08L₀²/T₀，归一化c=1对应物理传播速度L₀/T₀。改变固定端、自由端、周期边界或外部源，会改变允许模态和能量关系，不能只改变公式中的几个系数就视为同一问题。

### 位移为零不等于能量已经消失

在相应光滑性和固定端条件下，热方程的∫u²/2随时间下降，其导数为−κ∫uξ²。无阻尼波动方程的能量为∫(uτ²+c²uξ²)/2，可以在动能与形变能之间交换并保持总量。

本例在τ=0.5时波的位移场恰好为0，但速度场不为0；总能量仍为25π²/64≈3.85531。只看一帧位移图就说“振动消失”会遗漏状态的一部分。进一步可读[波动方程与Helmholtz方程](../wave-equation/)与[泛函分析](../functional-analysis/)，理解函数空间、算子和连续模型的收敛范围。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/pde-heat-wave.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/differential-equations-and-dynamical-systems/pde-heat-wave.svg" alt="相同固定端初始形状在热方程下平滑衰减，在无阻尼波动方程下变形与反相；半时刻位移为零但能量不为零。" width="1400" height="550" loading="lazy" /></a><figcaption>图10　不同演化律不能只凭图形相似混同。热κ=0.08，波c=1，初形与边界见正文，时间分别0、0.2、0.5和1；曲线由两个精确模态相加，不含空间离散误差。波在0.5时位移为0，能量储存在速度场中，全部场量归一化。</figcaption></figure>

## 数值轨迹怎样成为可信证据

### 离散算法可以改变稳定性和不变量

Euler法xₙ₊₁=xₙ+h f(τₙ,xₙ)是对连续流的近似，不是原方程本身。对x′=−a x、a>0，其更新因子为1−ah；要求幅值严格衰减需0<h<2/a，步长过大可把真实衰减变成数值发散。对无阻尼振子，显式Euler还可能使数值能量持续上升。

刚性问题可能同时包含很快衰减的扰动和缓慢观察变化。例如x′=−1000(x−cosτ)−sinτ、x(0)=1的真解只是cosτ，但显式Euler的扰动稳定性仍受快尺度约束。减小输出间隔并不自动缩小内部积分步长；辛方法、隐式方法或高阶方法各有条件，也不是一个名称就能解决所有长期误差。

### 初值 边界 误差与模型有效性分别核查

一次可复查计算至少记录方程、变量尺度、参数、初态、边界、积分区间、方法与容差。再检查解析解或守恒/耗散关系、步长与容差加密、独立算法、事件与定义域，以及不同初值下是否出现新的行为。混沌问题的比较要区分短时逐点误差和长期统计量，不能要求任意长时两种有限精度轨道完全重合。

SciPy solve_ivp的rtol、atol控制相应局部误差估计，不是一般真实全局误差的严格上界；t_eval指定输出时刻，不是内部步长上限，后者可用max_step限制。还应检查success、message、事件、终止时刻和数据尺度，不把“返回成功”当作存在唯一性、稳定或混沌的证书。[24](#ref-dds-ivp-api)

最后，数学模型内部自洽不等于模型已解释真实听觉。参数拟合、统计不确定性与干预预测需要独立数据及适当实验设计；[计算神经科学](../computational-neuroscience/)和[生物物理学](../biophysics/)可提供应用场景，但不能只根据某条轨迹像神经脉冲就确认生理机制。

## 可复算练习与学习连接

### 练习一 核对初值 解与平衡分支

把数值解与解析解比较，同时保留分离变量时可能丢失的零解。这个误差检查只针对指定区间和模型。

```python
import numpy as np
from scipy.integrate import solve_ivp
t=np.linspace(0,6,301)
for x0 in [0.,.15,.6,1.4]:
    sol=solve_ivp(lambda t,x:1.2*x*(1-x),(0,6),[x0],
        t_eval=t,method="DOP853",rtol=1e-10,atol=1e-12,max_step=.05)
    exact=np.zeros_like(t) if x0==0 else 1/(1+(1/x0-1)*np.exp(-1.2*t))
    error=np.max(np.abs(sol.y[0]-exact))
    assert sol.success and error<1e-8
    print(x0,error,sol.y[0,-1])
```

### 练习二 验证极限环的半径与返回周期

用事件记录y=0的向上穿越；除去起始事件后，相邻返回约隔π。积分的是完整二维方程，半径用独立解析式对照。

```python
import numpy as np
from scipy.integrate import solve_ivp
def rhs(t,z):
    x,y=z
    r2=x*x+y*y
    return [(1-r2)*x-2*y,2*x+(1-r2)*y]
def crossing(t,z):
    return z[1]
crossing.direction=1
crossing.terminal=False
t=np.linspace(0,12,601)
sol=solve_ivp(rhs,(0,12),[.2,0.],t_eval=t,events=crossing,
    method="DOP853",rtol=1e-10,atol=1e-12,max_step=.03)
radius=np.linalg.norm(sol.y,axis=0)
exact=1/np.sqrt(1+24*np.exp(-2*t))
events=sol.t_events[0]
events=events[events>1e-8]
assert sol.success and np.max(np.abs(radius-exact))<1e-8
assert np.allclose(np.diff(events),np.pi,atol=1e-8,rtol=0)
print("returns",events,"radius error",np.max(np.abs(radius-exact)))
```

### 练习三 区分ODE流和离散映射的稳定判据

核对r=3.2的二周期和两步导数，再验证r=4的特殊周期初值。它不是用有限迭代来证明所有轨道混沌。

```python
import numpy as np
r=3.2
cycle=np.array([(r+1-np.sqrt((r-3)*(r+1)))/(2*r),
                (r+1+np.sqrt((r-3)*(r+1)))/(2*r)])
F=lambda x:r*x*(1-x)
assert np.allclose(F(cycle),cycle[::-1])
multiplier=np.prod(r*(1-2*cycle))
assert np.isclose(multiplier,.16) and abs(multiplier)<1
x=.25
exception=[x]
for _ in range(3):
    x=4*x*(1-x)
    exception.append(x)
assert exception==[.25,.75,.75,.75]
print("two-cycle",cycle,"multiplier",multiplier,"exception",exception)
```

可以继续回答：为什么局部唯一仍允许有限时间爆破？为什么图4中心的闭轨不是极限环？V′≤0还缺什么才能判定收敛？分岔图为何不能当作时间响应？二维受迫系统为什么不能直接套用二维自治平面流的限制？波的位移为0时还有什么状态需要看？

继续学习可按问题进入[控制理论](../control-theory/)的反馈与估计、[数学物理方法](../mathematical-physics-methods/)的定解与连续场、[信号与系统](../signals-and-systems/)的输入输出、[数值分析](../numerical-analysis/)的误差与稳定，以及[泛函分析](../functional-analysis/)的空间与算子。它们是按需补读的入口，不是本篇之前必须全部修完的清单。

本文针对性核对13个Lebl作者教材章节、9份MIT Rothman课程讲义、1个MIT作者Lyapunov章节、1份CMU存在唯一性讲义和1份SciPy官方接口资料；它们不是25项独立实验研究。在线SciPy文档为1.18.0，本篇程序运行于1.17.1。公式、标准反例、独立数值计算与页面另作核验，仍保留AI辅助编写、draft和待专业审阅状态。
