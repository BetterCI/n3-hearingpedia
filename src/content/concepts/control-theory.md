---
title: "控制理论"
english: "Control Theory"
slug: "control-theory"
summary: "从反馈回路与动态模型进入稳定性、根轨迹、频率裕度、灵敏度和PID，再学习可控可观、状态反馈、观测器、LQR及数字实现；用可复算反例区分稳定、性能、鲁棒性与工程验证。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "控制理论", "反馈", "稳定性", "PID", "状态空间", "最优控制"]
aliases: ["Control Theory", "自动控制理论", "反馈控制", "控制系统基础"]
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
  - {label: "研究对象", value: "通过输入与反馈改变动态系统行为，并检验稳定、性能和不确定性"}
  - {label: "核心区别", value: "负反馈、稳定、跟踪准确和鲁棒不是同一个判断"}
  - {label: "研究连接", value: "声学回路、传感与执行、参数模型、动态调节和实时数字实现"}
  - {label: "重要边界", value: "内部模态、时延、采样、噪声与饱和可能破坏简化模型下的结论"}
references: ["ctrl-feedback", "ctrl-model", "ctrl-response", "ctrl-time", "ctrl-stability", "ctrl-errors", "ctrl-pid", "ctrl-root", "ctrl-nyquist", "ctrl-margins", "ctrl-digital", "ctrl-hold", "ctrl-state", "ctrl-controllability", "ctrl-observer", "ctrl-separation", "ctrl-lqr", "ctrl-windup", "ctrl-lyapunov", "ctrl-are-api", "ctrl-place-api", "ctrl-discrete-api", "ctrl-robust", "ctrl-lqr-conditions"]
order: 1020
---

**控制理论**（control theory）研究怎样选择输入或构造反馈，使动态系统按照希望的方式运行，并判断这种行为是否稳定、对扰动是否敏感、需要多少控制动作。动态系统具有随时间变化的内部状态；控制的对象不仅是某一个瞬间的数值，还包括从现在到未来的演化。[1](#ref-ctrl-feedback)

调节声学装置的输出、抑制振动、维持一个模型的工作点、估计无法直接测量的状态，都可能用到控制思想。扬声器与传声器构成的声学回路也会表现出增益、相位与时延问题；但反馈控制、声学啸叫、前馈降噪和自适应消除各有具体结构，不能只凭“有反馈”就把它们当作同一种算法或机制。

本文与[信号与系统](../signals-and-systems/)、[电路原理](../circuit-theory/)、[最优化方法](../optimization-methods/)配套，并就地解释所需数学。十幅图与全部数值是指定模型的原创教学计算，不是听者、房间或设备实测，不提供真实器件的调参处方。文末有三个短程序，另提供[完整实验脚本](/n3-hearingpedia/code/control-theory/experiments.py)。

初值、解的延续、相图、非线性稳定、极限环与分岔，可配合[微分方程与动力系统](../differential-equations-and-dynamical-systems/)按需阅读；数值轨迹与一般定理、模型有效性应分别核对。

## 阅读准备与独立阅读

**起步知识。** 能理解函数曲线、变化率、正负号和简单方程即可先读反馈例子。向量、矩阵、复数频率响应和特征值会随使用作局部说明；一般稳定性证明、多变量设计和硬件实现还需要进一步训练。

**随用随补。** 状态x是一列描述系统当前情况的数；矩阵Ax表示按行乘积求和。特征值描述线性系统中一些基本模态的增长、衰减或振荡。复数j满足j²=−1，频率响应的模表示放大倍数，角度表示相移。2范数 $\|x\|_2=\sqrt{\sum_i x_i^2}$ 衡量一组数的大小，但不同物理单位的状态应先合理缩放。

**分层阅读。** 第一遍看反馈框图、过大增益、积分饱和和采样反例。第二遍把传递函数、极点、稳定判据与频率裕度连起来。第三遍再读状态反馈、观测器和LQR；需要时按点补读[微积分](../calculus/)、[线性代数](../linear-algebra/)、[复变函数](../complex-analysis/)与[数值分析](../numerical-analysis/)，无需把它们先全部修完。

为统一教学例子的尺度，计算采用归一化时间τ=t/T₀，T₀=1秒，撇号表示对τ求导。状态、输入、输出和增益均按指定尺度无量纲化；归一化角频率ω对应物理频率ω/(2πT₀) Hz，时延θ对应θT₀秒，采样间隔h对应hT₀秒。真实模型仍须保留Pa、V、m等单位及换算关系。

## 反馈怎样改变一个系统

### 参考 控制动作与测量分别负责什么

**被控对象**是希望改变行为的过程，**控制器**根据已有信息计算输入u，**参考**r是希望达到的输出，**传感器**给出测量。开环控制不根据实际输出修正动作；闭环控制把测量送回来，与参考比较，再决定下一步。前馈则可根据参考或可测扰动提前补偿，实际系统常把前馈和反馈结合。

在理想单位测量、没有噪声时，误差e=r−y，比例控制u=Ke，K>0。比较点采用减号称为负反馈结构，但对象的动态相位可能让某些频率上的作用反而强化偏差，因此“负反馈”不能作为稳定证明。[1](#ref-ctrl-feedback)

取一阶对象y′=−y+u+d、初值0、参考1，d是加在对象输入端的扰动。开环u=r的稳态输出在d=0时为1；比例反馈K=4的输出却为0.8，仍有0.2偏差。若τ=3时d从0变为0.3，开环最终为1.3，反馈最终为0.86。反馈减小了这一扰动的影响，却没有同时消除参考跟踪误差。

### 反馈利用信息 也受测量和执行限制

传感器噪声、执行器饱和、计算时延和对象参数偏差都会进入回路。把控制器输出设得更大，不保证实际执行器能做到；把传感器读数当作真实输出，也可能让控制器追着噪声运动。

研究设计首先应画清：测量在哪、扰动加在哪、输入实际作用在哪、哪些内部变量没有测到。声学反馈回路中的传播时延、空间位置与声学通路会改变有效环路；一个模型上的稳定增益范围不能直接移作所有房间、佩戴状态或器件的通用范围。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/feedback-architecture.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/control-theory/feedback-architecture.svg" alt="负反馈框图与一阶对象的开环、比例反馈输出，展示输入扰动作用及非零跟踪误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图1　反馈抗扰与跟踪准确性需要分别评价。左图为无噪声单位反馈，控制器C在正文记为C_c；右图对象y′=−y+u+d，参考1、初值0、比例增益4，τ=3加入0.3的输入扰动。输出最终分别为1.3与0.86，全部信号无量纲。</figcaption></figure>

## 模型如何描述动态和内部状态

### 微分方程与传递函数各保留什么

线性时不变系统的状态空间形式为

$$
x'=Ax+Bu,\qquad y=Cx+Du.
$$

x∈ℝⁿ为状态，u∈ℝᵐ为输入，y∈ℝᵖ为输出；A描述自由演化，B描述输入如何进入，C描述状态如何形成输出，D描述直接通路。状态不是必须能够直接测到的量，也不只允许一种坐标表示。[13](#ref-ctrl-state)

在零初始状态下作Laplace变换，可得 $G(s)=C(sI-A)^{-1}B+D$。这里s是复频率变量，I为单位矩阵；逆矩阵公式用来表达输入输出关系，数值实现通常通过解线性方程求值。非零初态还有C(sI−A)⁻¹x(0)项，不能把传递函数响应直接当作全部状态响应。

单输入单输出时G(s)为标量有理函数。约去公因子后的分母根为输入输出极点，分子根为零点；状态矩阵的全部特征值则包含所有内部模态。两者在最小实现中对应，在不可控或不可观实现中可能不同。极点零点精确消去尤其可能掩盖内部不稳定性，参数稍有误差时也未必维持消去。

### 线性化是围绕工作点的近似

非线性系统x′=f(x,u)在平衡点(x₀,u₀)满足f(x₀,u₀)=0。令δx=x−x₀、δu=u−u₀，局部一阶近似为δx′≈Aδx+Bδu，其中A和B是相应偏导数组成的Jacobian。模型的适用范围取决于偏离程度、遗漏动态和参数变化。[2](#ref-ctrl-model)

线性近似不是把饱和、死区、摩擦或神经非线性证明为不存在。对模型工作点附近的成功控制，不应自动宣称对任意初值、参考和扰动都有同样效果。

## 稳定性与响应质量分别说明什么

### 稳定 不发散与收敛需要区分

对无输入平衡点，Lyapunov稳定表示足够小的初始偏差可使轨迹始终留在任意指定的小邻域；渐近稳定还要求这些轨迹最终回到平衡点。指数稳定进一步用指数包络控制衰减速率。有限时间仿真没有发散，并不构成其中任何一般性证明。

连续时间有限维LTI系统x′=Ax渐近稳定，当且仅当A所有特征值实部严格小于0，常称A为Hurwitz矩阵。虚轴上的特征值不能直接判为渐近稳定；其Jordan结构还影响是否有多项式增长。离散时间对应条件则是特征值模严格小于1。[5](#ref-ctrl-stability)

**有界输入有界输出稳定**（BIBO稳定）只讨论零初态下，任何有界输入是否产生有界输出。对适当的有限维连续时间有理传递函数，它要求约分后的极点在严格左半平面；内部渐近稳定更强。图2的A=diag(−1,+1)、B=(1,0)ᵀ、C=(1,0)、D=0，输入输出传递函数为1/(s+1)，内部第二状态却可能按eᵗ增长。

### 过冲和调节时间描述稳定之后的表现

标准二阶传递函数为G(s)=ωₙ²/(s²+2ζωₙs+ωₙ²)，ωₙ>0为自然频率，ζ为阻尼比。0<ζ<1时极点为−ζωₙ±jωₙ√(1−ζ²)，单位阶跃常出现过冲；ζ>1时为过阻尼，响应形状不同。[3](#ref-ctrl-response)

这个无零点、单位静态增益的标准模型，在0<ζ<1时，相对过冲为exp[−πζ/√(1−ζ²)]，峰值时间为π/(ωₙ√(1−ζ²))。约4/(ζωₙ)的2%调节时间只是常用近似，不能覆盖任意零点、多模态或非线性系统。上升时间、误差带和“进入后不再离开”的规则要明确，否则不同报告的速度指标可能不可比。[4](#ref-ctrl-time)

### Lyapunov函数从轨迹以外提供证据

对原点为平衡点的自治系统，假定向量场局部Lipschitz以保证局部解的唯一性。若在原点邻域找到连续可微V，满足V(0)=0、非零处V>0且沿轨迹V′≤0，可证明局部稳定；若非零处V′<0，可得到局部渐近稳定。要推广到全局，还需相应全局条件，如V径向无界、向量场定义及轨迹延续等。[19](#ref-ctrl-lyapunov)

V不必是真实物理能量；它是用于证明的标量函数。V′≤0本身不保证收敛到原点，可能需要LaSalle不变集分析。例x′=−x³取V=x²/2，V′=−x⁴，原点全局渐近稳定，但不是局部指数稳定；其线性化A=0也不足以给出这一非线性结论。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/response-internal-stability.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/control-theory/response-internal-stability.svg" alt="标准二阶系统不同阻尼比的阶跃响应，以及输出衰减同时隐藏状态增长的反例。" width="1400" height="550" loading="lazy" /></a><figcaption>图2　输出好看不等于内部安全。左图标准二阶模型ωₙ=2、ζ分别0.2、0.7和1.2，零初态单位阶跃；右图换为A=diag(−1,+1)，无输入、初态(1,0.02)，只测第一状态。右图对数纵轴显示隐藏模态增长，两面板是不同模型。</figcaption></figure>

## 增益 根轨迹与稳定范围

### 特征方程决定回路是否具有衰减模态

设对象P(s)、控制器C_c(s)，单位负反馈的环路传递函数L=P C_c；在回路适定时，参考到输出的传递函数为L/(1+L)。适定要求互连能唯一确定内部信号，例如直接通路不能形成不可解的代数环。除去可能消去的因素后，1+L=0给出闭环输入输出极点，仍需另外检查隐藏模态。

根轨迹描述某个参数改变时闭环特征根如何移动，并非真实状态随时间走过的路径。它可以帮助理解提高增益如何改变阻尼、速度和稳定性；增益变化也可能把极点推入右半平面。[8](#ref-ctrl-root)

### 一个可精确判定的负反馈反例

取P(s)=1/[s(s+1)(s+2)]、C_c=K>0。闭环特征多项式为s³+3s²+2s+K。Routh表第一列依次为1、3、(6−K)/3、K，因此严格稳定范围是0<K<6。K=6时多项式分解为(s+3)(s²+2)，有虚轴极点；K>6时出现右半平面极点。[5](#ref-ctrl-stability)

这说明负号与正增益并不保证稳定。K=5虽然仍在稳定范围内，振荡衰减已很慢；K=8则增幅振荡。稳定边界附近的名义结果也容易受未建模时延和参数偏差影响，不应把刚好未越界当作充分设计裕度。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/root-locus-gain.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/control-theory/root-locus-gain.svg" alt="三阶对象的根轨迹随比例增益越过虚轴，阶跃响应从衰减振荡变为增幅振荡。" width="1400" height="550" loading="lazy" /></a><figcaption>图3　增益需要放在动态模型中解释。左图K从0.001到12，标出K=2、6和8的全部极点；右图用K=2、5和8的零初态单位阶跃。τ与极点频率采用归一化尺度，K=6只是临界情况，不属于严格稳定区间。</figcaption></figure>

## 频率响应 裕度与时延

### Bode图和Nyquist图从不同角度看同一环路

在频率ω处，将s=jω代入L；Bode图画幅值20log₁₀|L|及相位随频率变化，Nyquist图画复平面上的L轨迹。二者可用于研究闭环稳定，但“幅值超过1”或“相位到−180°”单独出现都不是一般失稳判据。[9](#ref-ctrl-nyquist)

一种明确约定是：对包围右半平面的Nyquist围线，按对临界点−1的顺时针净环绕数N计，有N=Z−P；P为L的右半平面极点数，Z为1+L的右半平面零点数，均计重数。若L有虚轴极点，需适当绕避，轨迹穿过−1时是临界情况。数圈前必须写清围线、方向和已有不稳定极点，不能只看正频率的一小段曲线。

### 相位裕度是有条件的设计指标

增益交越频率ωc满足|L(jωc)|=1；在常见单交越情形，相位裕度表示该处相位距离−180°还有多少。相位交越处到单位幅值的距离对应增益裕度。多个交越、开环不稳定或多变量系统需要更完整分析，单个正相位裕度不能当作所有系统的稳定证书。[10](#ref-ctrl-margins)

图4使用L₀(s)=4/[(s+1)(s+2)]。交越频率约1.33117，相位裕度约93.2676°。纯时延e⁻θˢ不改变频率幅值，却额外引入−ωθ弧度相位；这一模型的首次临界时延为相位裕度弧度值除以ωc，约1.22286。取θ=1.5已越过临界，名义“幅频曲线没有变”并不能说明稳定性不变。

这里直接计算指数时延频率响应，未用有限阶Padé近似代替真实时延。一般模型不能只根据一个经验采样倍数、一个相位值或有限频率网格就证明稳定；应结合完整环路、交越和适用的判据。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/frequency-delay.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/control-theory/frequency-delay.svg" alt="相同时延前后的环路幅值、展开相位与正负频率Nyquist轨迹，展示时延使临界点环绕改变。" width="1400" height="550" loading="lazy" /></a><figcaption>图4　纯时延保留幅值却改变相位与稳定性。L=L₀ exp(−θs)，θ分别0和1.5；左侧相位展开显示，纵轴仅画−320°至5°，曲线越界不表示相位停止变化。右图同时绘正负频率，轨迹有限截取用于展示，稳定判断另用完整条件与特征方程核对。</figcaption></figure>

## 灵敏度与性能 鲁棒性的取舍

### 写清扰动位置才能解释抑制量

对标量单位反馈定义灵敏度S=1/(1+L)，互补灵敏度T=L/(1+L)，满足S+T=1。若测量为y+n，误差信号e=r−y−n，对象满足y=P(u+d)、控制器u=C_c e，则零初态下

$$
y=T r+P S d-T n.
$$

d在对象输入端，n是测量噪声。因此参考跟踪看T，输入扰动到输出看PS，测量噪声到输出看−T；若扰动加在输出端，对应通路才是S。不能不区分位置就把所有抗扰都称为“降低S”。[6](#ref-ctrl-errors)

S+T=1是复数恒等式，不是幅值相加等于1；但三角不等式给出|S|+|T|≥1，两者不能在同一频率同时任意小。增大低频环路增益可改善某些跟踪和扰动响应，却可能增加噪声作用、控制动作、峰值或时延敏感性。图5的θ=1.0仍在该模型的临界时延以内，但已出现明显峰值。

### 名义稳定和鲁棒稳定是不同目标

名义模型只代表选定的P，实际对象可能包含参数变化、额外模态和传播时延。**鲁棒稳定**要求对明确规定的一组不确定对象都稳定；必须先说明这组对象和误差界，不能把“看起来不敏感”当作证明。

例如采用乘法不确定性P_actual=P(1+WΔ)，并假设名义互连内部稳定、W和Δ为稳定且适当的LTI传递函数、‖Δ‖∞≤1，相关互连适定时，小增益条件‖WT‖∞<1是常用鲁棒稳定充分条件。这里∞范数是对所有频率的幅值上确界，有限网格上的最大值一般不自动给出严格上界。模型误差超过设定范围，证书也不再覆盖。[23](#ref-ctrl-robust)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/sensitivity-tradeoff.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/control-theory/sensitivity-tradeoff.svg" alt="同一环路在无时延与时延1.0下的灵敏度及互补灵敏度幅值，显示接近临界时的峰值。" width="1400" height="550" loading="lazy" /></a><figcaption>图5　仍然稳定也可能有很差的扰动放大特性。沿用图4对象，θ取0和1.0，计算ω从0.01至100的S与T。曲线使用对数坐标，S+T=1按复数逐点成立；这些离散频率图不是未经采样频段的严格鲁棒性包围证书。</figcaption></figure>

## PID 积分作用与执行器饱和

### 比例 积分与微分对应不同信息

理想PID形式为u=Kp e+Ki∫e dτ+Kd e′。比例项响应当前偏差，积分项累积持续偏差，微分项响应变化趋势。各增益作用取决于对象和实现，不能把“增大某项必然使某指标变好”当作一般规律。[7](#ref-ctrl-pid)

在相应闭环稳定、参考和扰动类型适合、执行器未被持续限制等条件下，积分作用可消除某些常值误差。终值定理也要求sE(s)的相关极点位于严格左半平面等条件；若回路不稳定，就不能用形式上的s→0代入声称误差已归零。

理想微分会无限放大高频，实际常用Kd s/(1+s/ωf)等带低通限制的微分环节，ωf>0。对测量量而非参考误差作微分可避免参考阶跃直接引起的某些微分冲击；这改变了控制器结构，应明示公式与滤波，而非只报告三个数字。

### 积分饱和为什么会延迟恢复

令控制器命令u_c=2e+z、积分状态z′=e，实际输入u=clip(u_c,−1,1)。若一阶对象y′=−y+u的参考长期设为2，实际输入最多为1，不可能使输出稳定在2。误差持续为正会让z继续累积；参考随后降低到0.5时，积累的z仍可能让执行器长时间保持上限。[18](#ref-ctrl-windup)

一种反算抗饱和方法是z′=e+k_aw(u−u_c)，k_aw>0，使积分器看到“实际动作与命令之间的差”。图6指定k_aw=2，与无抗饱和对照。它改善本例的恢复，但也有暂时下冲；抗饱和不能让不可实现的参考变得可实现，也不提供所有饱和非线性下的普遍稳定保证。

实际设计还可能采用条件积分、参考治理、限速或显式约束控制。模型必须区分控制命令、实际输入、积分器状态与输出，否则只检查输出短时曲线可能漏掉内部累积。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/integrator-windup.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/control-theory/integrator-windup.svg" alt="参考从不可实现的2降至0.5后，无抗饱和积分器仍把输入维持上限；反算方案更快解除饱和但出现下冲。" width="1400" height="550" loading="lazy" /></a><figcaption>图6　积分状态必须和实际执行能力一起建模。对象y′=−y+u，Kp=2、Ki=1，输入限制[−1,1]；τ=5时参考从2变0.5。反算k_aw=2，所有初态0，RK4步长0.0025并对齐参考切换；实线为命令，右侧虚线为实际输入，未含测量噪声。</figcaption></figure>

## 可控性 可观性与状态反馈

### 能施加输入和能看到状态是不同能力

矩阵的秩是其列向量能够提供的线性独立方向数。连续时间有限维LTI模型的可控矩阵为𝒞=[B,AB,…,Aⁿ⁻¹B]；秩为n，表示在没有输入硬约束的理想模型中，可用适当输入在有限时间内完成任意状态间的转移。可观矩阵为𝒪=[Cᵀ,(CA)ᵀ,…,(CAⁿ⁻¹)ᵀ]ᵀ；秩为n，表示已知输入且无噪声时，可由一段输出唯一辨认初始状态。[14](#ref-ctrl-controllability)

它们属于选定(A,B,C)模型的结构性质：B和C选在哪里很关键。可逆状态坐标变换不改变这些秩。可控也不等于在给定幅值、速度或能量限制内一定能完成任务；可观也不等于面对噪声就一定能准确估计。

较弱的**可稳定性**只要求不可控模态本身稳定；**可检测性**只要求不可观模态稳定。设计稳定反馈或渐近观测器常可使用这些较弱条件，不必把完全可控、完全可观当作任何稳定设计的必要前提。

### 极点配置给出一个明确的动态目标

取归一化振动模型x₁′=x₂、x₂′=−2x₁−0.6x₂+u、y=x₁，即A=[[0,1],[-2,−0.6]]、B=(0,1)ᵀ、C=(1,0)。x₂是归一化时间下的位置变化率，该模型可控且可观，未加入输入限制。

状态反馈u=−Kx使闭环矩阵变为A−BK。取K=(4,4.4)，特征式变为s²+5s+6，极点为−2和−3。这个例子是把初态(1,0)调回0，不是自动完成任意非零参考的跟踪；后者需要合适的参考通道或积分扩展。

可控系统可配置所需的一组共轭对称极点，但极点配置不唯一等于最佳设计，更不等于控制动作足够小。SciPy place_poles采用A−BK的符号约定，返回后仍应核对实际特征值、增益幅度和数值条件。[21](#ref-ctrl-place-api)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/state-feedback.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/control-theory/state-feedback.svg" alt="归一化振动模型的开环与状态反馈自由响应，以及状态反馈产生的控制输入。" width="1400" height="550" loading="lazy" /></a><figcaption>图7　内部极点和输入代价一起看。使用正文二状态模型、初态(1,0)、参考0，K=(4,4.4)；左图比较开环自由响应和闭环位置，右图展示u=−Kx。未施加饱和，因此不能把曲线直接当作受限执行器的可行性能。</figcaption></figure>

## 观测器怎样重建未测状态

### 用模型预测 再以测量残差校正

当只测y=Cx，且输入u已知时，全阶Luenberger观测器为

$$
\hat x'=A\hat x+Bu+L_o(y-C\hat x).
$$

预测来自模型，校正来自测量与预测输出之差；L_o为观测器增益。定义估计误差e_x=x−x̂，无噪声且模型准确时有e_x′=(A−L_oC)e_x。[15](#ref-ctrl-observer)

对图7模型，选L_o=(8.4,12.96)ᵀ可把误差极点设为−4和−5。只要误差系统稳定，初始估计错误会渐近消失；但这不是从一个瞬时输出就直接恢复所有状态，也不意味着有噪声时误差还能精确归零。

### 更快极点与噪声 瞬态之间存在取舍

测量含噪声n时，误差方程多出−L_o n。更大的观测器增益可能加速无噪声误差的后期衰减，却也放大某些频段噪声，并产生较大的初始瞬态。图8将误差极点−4、−5与−12、−15对照，右侧只考察位置测量噪声到速度估计的频率通路，不把它当作任意噪声统计下的均方误差。

如果采用u=−Kx̂，准确LTI模型、无额外时延与饱和条件下，在(x,e_x)坐标中闭环矩阵是分块三角形，其特征值为A−BK和A−L_oC两组极点的并集。这是相应的分离原理，允许分别设计控制器和观测器；未建模动态、噪声性能和鲁棒性仍需联合核查。[16](#ref-ctrl-separation)

Kalman滤波进一步利用指定过程与测量噪声统计构造估计器；它需要明确的随机模型和条件，不能把任意观测器都称为统计最优。可结合[概率论](../probability-theory/)与[数理统计](../mathematical-statistics/)补读。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/observer-noise.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/control-theory/observer-noise.svg" alt="两种观测器的无噪声误差衰减及测量噪声到速度估计的频率幅值，显示更快设计的暂态和噪声代价。" width="1400" height="550" loading="lazy" /></a><figcaption>图8　估计速度不是唯一指标。模型同图7，初始误差(1,0)，左图用矩阵指数精确线性传播；右图画|(jωI−A+L_oC)⁻¹L_o|的第二分量，外部输入u视为已知。右图没有预设白噪声方差或计算一般统计最优性。</figcaption></figure>

## 最优控制怎样把性能写成代价

### LQR的最优性取决于明确问题与假设

对x′=Ax+Bu，无限时域线性二次调节器（LQR）最小化

$$
\begin{aligned}
J&=\int_0^\infty (x^TQx+u^TRu)\,d\tau,\\
Q&=Q^T\succeq0,\qquad R=R^T\succ0.
\end{aligned}
$$

Q和R分别定义状态偏差与输入的代价，权重必须结合单位和尺度解释。Q≽0表示对任意x有xᵀQx≥0，R≻0表示对每个非零u都有uᵀRu>0，因此这些平方代价不会因符号而奖励任意放大输入。标准条件包括(A,B)可稳定、$(Q^{1/2},A)$可检测，其中Q¹ᐟ²为对称半正定平方根；此时存在唯一相应半正定稳定化Riccati解P，最优反馈为u=−Kx，K=R⁻¹BᵀP，且

$$
A^TP+PA-PBR^{-1}B^TP+Q=0.
$$

这里的“稳定化”还要求A−BK为Hurwitz矩阵，不能只验证代数方程残差。[17](#ref-ctrl-lqr)[24](#ref-ctrl-lqr-conditions)[20](#ref-ctrl-are-api)

图9仍用图7模型，Q=I，分别取R=0.1、1和10。R=1时K约(0.23607,0.75356)，与手动配置−2、−3得到的增益不同；它优化指定的全时域平方代价，而非只追求最快极点或最小过冲。不同R下的J采用不同目标，不能把数值大小直接当作同一比赛分数。

### 约束和非线性需要扩展问题本身

基本LQR未加入硬饱和、限速或状态安全边界。如果把最优动作直接裁剪，得到的是另一个非线性闭环，原有最优性与稳定结论不能原封不动继承。非线性模型工作点附近的LQR也通常只是局部设计。

模型预测控制（MPC）在每次更新时求解带模型、有限预测时域和约束的优化问题，执行第一步后再用新状态重算。它便于表达限制，但可行性、终端条件、求解精度和实时计算期限仍决定保证范围。这里提供与[最优化方法](../optimization-methods/)的学习连接，不把一个方法名当作所有约束问题的答案。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/lqr-effort.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/control-theory/lqr-effort.svg" alt="同一二状态模型在三个LQR输入权重下的位置调节与控制动作，展示不同代价产生的性能取舍。" width="1400" height="550" loading="lazy" /></a><figcaption>图9　最优必须相对于指定代价。Q=I，标量R分别0.1、1和10，初态(1,0)，无输入约束；状态由闭环矩阵指数传播。三组控制分别满足其Riccati条件，且以独立Lyapunov代价积分身份核对，不宣称某一组对真实设备普遍最好。</figcaption></figure>

## 数字控制为何要重新检查采样与保持

### 离散模型依赖实际输入如何保持

若每个采样间隔h内输入恒定，即零阶保持（ZOH），连续LTI对象的精确采样模型为xₖ₊₁=A_d xₖ+B_d uₖ，其中

$$
A_d=e^{Ah},\qquad B_d=\int_0^h e^{Av}B\,dv.
$$

即使A奇异，积分仍有定义；不要无条件套用含A⁻¹的表达。输出还需包含C、D及采样约定。[11](#ref-ctrl-digital)[22](#ref-ctrl-discrete-api)

传感采样、计算与传输延迟、执行器保持和模拟抗混叠都影响真实回路。Nyquist采样条件处理频谱混叠，并不单独保证某个数字控制器有足够相位裕度。ZOH在频域也带来幅值和相位影响，高带宽设计尤其需要显式建模。[12](#ref-ctrl-hold)

### 先闭环再采样 与先采样对象再反馈不同

取连续对象x′=−x+u、连续反馈u=−4x，连续闭环为x′=−5x，稳定。若改成只在采样时刻测量并更新uₖ=−4xₖ，然后整段保持，则离散闭环极点为a_cl=e⁻ʰ−4(1−e⁻ʰ)=5e⁻ʰ−4。

稳定要求|a_cl|<1，即0<h<ln(5/3)≈0.51083。h=0.1时极点约0.52419，h=0.4时约−0.64840，h=0.6时约−1.25594，最后一种出现采样点幅值增长。这里使用对象的精确ZOH，不是Euler离散误差造成的假失稳。

e⁻⁵ʰ则只是已经连续闭环的轨迹在采样时刻的变化因子，所有h>0都小于1。把它当作实际“采样测量、保持控制”的闭环极点，就遗漏了两次更新之间没有连续修正输入的事实。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/control-theory/sampled-feedback.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/control-theory/sampled-feedback.svg" alt="三个采样间隔下同一比例反馈的离散状态序列，以及数字闭环极点与连续闭环采样因子的不同。" width="1400" height="550" loading="lazy" /></a><figcaption>图10　数字实现需按互连顺序建模。初值1，无参考及扰动，uₖ=−4xₖ并零阶保持；左图只连接采样点，不表示区间内连续状态是折线。右图比较5exp(−h)−4与exp(−5h)，虚线±1为离散稳定边界，Tₛ=hT₀且T₀=1秒。</figcaption></figure>

## 复算 核验与继续学习

### 练习一 不凭负号判断闭环稳定

下面数值求出三阶反例的全部极点，和Routh结论相互核对。K=6处的极小实部舍入应按临界模态解释，不能靠正负最后一位决定一般稳定性。

```python
import numpy as np
for gain in [2.,5.,6.,8.]:
    poles=np.roots([1.,3.,2.,gain])
    print(gain,poles)
    if gain<6:
        assert np.max(poles.real)<0
    elif gain>6:
        assert np.count_nonzero(poles.real>0)==2
    else:
        assert np.allclose(np.sort(poles.imag),[-np.sqrt(2),0,np.sqrt(2)])
```

### 练习二 核对状态反馈 观测器与分离原理

这段只验证准确、无噪声LTI模型的极点；不因此推断存在测量噪声、饱和和参数偏差时的全部性能。

```python
import numpy as np
from scipy.signal import place_poles
A=np.array([[0.,1.],[-2.,-.6]])
B=np.array([[0.],[1.]])
C=np.array([[1.,0.]])
assert np.linalg.matrix_rank(np.hstack([B,A@B]))==2
assert np.linalg.matrix_rank(np.vstack([C,C@A]))==2
K=place_poles(A,B,[-2.,-3.],method="YT").gain_matrix
Lo=place_poles(A.T,C.T,[-4.,-5.],method="YT").gain_matrix.T
F=np.block([[A-B@K,B@K],[np.zeros((2,2)),A-Lo@C]])
assert np.allclose(np.sort(np.linalg.eigvals(F)),[-5,-4,-3,-2])
print("K",K,"Lo",Lo,"poles",np.linalg.eigvals(F))
```

### 练习三 用精确ZOH核对采样限制

显式指定保持方式，并比较先对对象离散再闭环的结果。实际运行SciPy 1.17.1，在线接口核对版本为1.18.0。

```python
import numpy as np
from scipy.signal import cont2discrete
A=np.array([[-1.]])
B=C=np.array([[1.]])
D=np.array([[0.]])
for h in [.1,.4,.6]:
    Ad,Bd,_,_,_=cont2discrete((A,B,C,D),h,method="zoh")
    pole=float((Ad-4*Bd)[0,0])
    assert np.isclose(pole,5*np.exp(-h)-4)
    print(h,pole,"stable",abs(pole)<1,"continuous",np.exp(-5*h))
```

核验实际控制方案时，应记录模型与单位、传感和执行位置、参考与扰动、初始条件、控制律、保持与延迟、约束、噪声假设以及计算容差。先查适定和内部稳定，再报告跟踪、抗扰、控制动作、估计误差与不确定性范围。有限网格、有限仿真时长和软件返回成功不能代替相应数学证据；数值误差、模型误差及任务效果也应分别评价。

可以继续推问：为什么图1比例控制抗扰却没有零跟踪误差？图2隐藏不稳定状态为何不出现在传递函数里？图4增加纯时延为什么不改幅值却能失稳？图6为何不能仅用提高积分增益解决不可达参考？图8更快极点为何可能有更大瞬态？图10两个采样因子在物理实现上究竟差在哪里？

需要补输入输出表示时读[信号与系统](../signals-and-systems/)，补数字实现时读[数字信号处理](../digital-signal-processing/)，补曲率、约束和代价时读[最优化方法](../optimization-methods/)。[计算神经科学](../computational-neuroscience/)与[生物物理学](../biophysics/)提供动态模型场景，但能拟合或控制一个模型不自动证明其对应的生理机制真实。

本文针对性核对MIT两门课程的18份官方讲义及1份LQR习题课资料、MIT作者Lyapunov在线章节、MIT开放教材的鲁棒性章节及3份SciPy官方接口文档；同一课程的多份资料不视为独立实验研究。图文和程序另作解析、数值及页面核验。仍保留AI辅助编写、draft与待专业审阅状态，不把这些检查替代外部专业评审。
