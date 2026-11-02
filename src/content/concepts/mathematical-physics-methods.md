---
title: "数学物理方法"
english: "Methods of Mathematical Physics"
slug: "mathematical-physics-methods"
summary: "从场、守恒律和定解条件出发，理解偏微分方程分类、分离变量、Sturm–Liouville问题、正交展开、贝塞尔与勒让德函数、傅里叶及拉普拉斯变换、格林函数和变分方法，再用弦、膜、声腔与扩散算例检查解的意义和数值边界。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "数学物理方法", "偏微分方程", "边值问题", "特殊函数", "格林函数", "模态", "变分法"]
aliases: ["数学物理方程", "物理学中的数学方法", "数理方法", "Mathematical Methods in Physics"]
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
  - {label: "课程主线", value: "物理模型、定解条件、算子结构与求解方法"}
  - {label: "核心知识", value: "偏微分方程、正交展开、积分变换、特殊函数与格林函数"}
  - {label: "形象入口", value: "弦的驻波、圆膜节线、扩散平滑与声腔共振"}
  - {label: "研究边界", value: "解析解、稳定算法和真实模型正确性需要分别检验"}
references: ["mm-problem", "mm-classify", "mm-heat", "mm-wave", "mm-sl", "mm-orthogonal", "mm-multi", "mm-coordinates", "mm-bessel", "mm-bessel-zeros", "mm-bessel-integral", "mm-legendre", "mm-harmonics", "mm-fourier", "mm-laplace", "mm-distribution", "mm-green", "mm-energy", "mm-variational", "mm-numerics"]
order: 1009
---

**数学物理方法**（methods of mathematical physics）研究如何把物理规律写成数学问题，利用方程、边界和几何结构求解，再解释解对应的物理行为。它的对象不限于某一种方程：同一组正交模态可以描述弦的振动、热的扩散和静态受力；同一个格林函数思想可以连接点源、边值问题与系统响应。课程的关键能力，是知道一种方法为什么适用，以及所得解究竟满足了哪些条件。[1](#ref-mm-problem)

不同学校的同名课程范围有所区别，常见内容包括复变函数、积分变换、数学物理方程和特殊函数。本篇已有[复变函数](../complex-analysis/)、[线性代数](../linear-algebra/)作为配套，重点展开从连续场到定解问题的这条主线，并补充能量法、弱形式和数值核验。多元微积分、常微分方程、复数与矩阵用于相应推导；下方先给从有限位置点理解连续场的入口，函数空间概念在用到时再解释。

这里的弦、圆膜、热扩散和声腔均为明确指定的理想模型。十幅图及数值是原创教学计算，不是鼓膜、耳蜗或房间的实测；尤其不能把张紧圆膜直接视为具有复杂几何、各向异性和耦合负载的真实鼓膜。

## 阅读准备与独立阅读

**起步知识。** 从函数图像、变化与累积、简单方程和物理单位开始。手工完成分离变量、特殊函数及弱形式推导时，会进一步用到多元微积分、常微分方程和矩阵；这些要求与概念入门分开说明。

**随用随补。** 场先看成“每个位置和时刻各有一个量”，例如不同位置的声压。偏导数表示固定其他变量时的变化率；初始条件规定开始时的状态，边界条件规定空间边缘的约束。把一根弦分成少量位置点，就能先用有限个数理解场、模态与近似。

**分层阅读。** 第一遍从守恒、单位、方程和定解条件入手，对照弦振动与扩散图理解“求什么、受什么约束”。第二遍核对分离变量、Sturm–Liouville、特殊函数、格林函数与弱形式；复数、矩阵和函数空间的定义可按所用方法回查。

## 从物理量与守恒律建立方程

### 标量场 矢量场与算子

**场**是随位置，必要时还随时间变化的物理量。温度 $T(\mathbf x,t)$、声压扰动 $p(\mathbf x,t)$ 是标量场；质点速度 $\mathbf v(\mathbf x,t)$、热流密度 $\mathbf q(\mathbf x,t)$ 是矢量场。这里 $\mathbf x$ 表示空间坐标，不能把声压场 $p$ 和声粒子的位移混为同一未知量。

**梯度** $\nabla u$ 表示标量场增加最快的方向与单位距离的变化率；**散度** $\nabla\cdot\mathbf q$ 描述通量在一点附近的净流出密度；**旋度** $\nabla\times\mathbf v$ 描述局部环流。**拉普拉斯算子** $\Delta u=\nabla\cdot\nabla u$ 在笛卡尔坐标下为各坐标二阶偏导之和。对光滑场，它们是微分运算，不是把“梯度”当成一个任意大小的箭头。

例如热传导本构关系为 $\mathbf q=-k\nabla T$，负号表示热沿温度降低方向流动。结合局部能量守恒 $\rho c_p T_t=-\nabla\cdot\mathbf q+Q$，若参数恒定，便得到 $T_t=D\Delta T+Q/(\rho c_p)$，其中 $D=k/(\rho c_p)$，单位m²/s。若 $k$ 随位置变，应该保留 $\nabla\cdot(k\nabla T)$，不能随意把它写为 $k\Delta T$。[3](#ref-mm-heat)[7](#ref-mm-multi)

### 方程来自守恒和本构两部分

守恒律回答“流入、流出与积累如何平衡”；本构关系回答“这种材料怎样把力、变形或温度梯度联系起来”。同一个守恒框架，配上不同本构关系，会得到不同模型。线性、小扰动、无损、均匀等词都在限定这些关系，不是装饰语。

以静止、均匀、无黏、可压缩介质的小幅声扰动为例，线性动量式 $\rho_0\mathbf v_t=-\nabla p$ 与压力连续性式 $p_t=-\rho_0c^2\nabla\cdot\mathbf v$ 联立，给出 $p_{tt}=c^2\Delta p$。若存在显著流动、密度空间变化、热黏性边界层或非线性，方程就需要相应改变；详见[波动方程](../wave-equation/)。数学方法不能替代模型选择。

### 单位和无量纲化先于求解

**量纲一致**要求一个方程中相加的各项具有相同单位。扩散方程中 $u_t$ 的单位为“u的单位/s”，故D必须是m²/s；波动方程中的c则是m/s。两种方程都含 $\Delta u$，不表示它们拥有相同的时间尺度。

取特征长度L，令 $\xi=x/L$。扩散时间尺度为 $L^2/D$，传播时间尺度为 $L/c$；长度翻倍时，前者变成四倍，后者变成两倍。无量纲化还让误差容限、网格和模态系数更容易比较。本篇标为“归一化”的图会明确其坐标，不把无单位曲线直接当作Pa或毫米。

## 偏微分方程必须和定解条件一起看

### 阶数 线性与三种典型方程

**偏微分方程**（PDE）联系多变量函数及其偏导数，阶数由最高阶导数决定。**线性**表示未知函数及其导数以一次线性组合出现，系数可依赖自变量；$u u_x$、$(u_x)^2$ 一般属于非线性。**齐次**指在写定的线性算子方程 $\mathcal L u=f$ 中 $f=0$，但边界数据也要另行检查，不能只看右端。[2](#ref-mm-classify)

常系数二维二阶主部写为 $A u_{xx}+2B u_{xy}+C u_{yy}$。在该形式和非退化情形下，$B^2-AC<0$、$=0$、$>0$ 分别对应椭圆、抛物、双曲型；更高维以主符号的性质描述，不能只机械套这个二维判别式。[2](#ref-mm-classify)

| 典型问题 | 方程示例 | 主要行为与所需数据 |
| --- | --- | --- |
| 静态势场 | $-\Delta u=f$；f=0为拉普拉斯方程 | 域内各点通过边界与源耦合，通常给边界条件 |
| 扩散 | $u_t=D\Delta u$，D>0 | 平滑与衰减，通常给一组初态及空间边界条件 |
| 波动 | $u_{tt}=c^2\Delta u$，c>0 | 有限速度传播，通常给位形、变化率两组初态及空间边界条件 |

类型描述的是方程结构；具体问题是否适定，还取决于域、系数和数据。譬如把扩散过程倒着恢复初态，虽然方程看似只把t换了方向，却会极度放大高空间频率误差。

### 初始条件和三种边界条件

**初始条件**规定某一时刻的状态；一阶时间扩散式给 $u(\mathbf x,0)$，二阶时间波动式通常还给 $u_t(\mathbf x,0)$。**边界条件**规定空间边界上的关系，常用外法向 $\mathbf n$ 和法向导数 $\partial_n u=\mathbf n\cdot\nabla u$。[1](#ref-mm-problem)

- **Dirichlet条件**：规定函数值 $u=g$，例如理想固定弦端的位移为零。
- **Neumann条件**：规定法向导数 $\partial_n u=g$，热流边界还需结合 $-k\partial_nT$ 的符号和单位。
- **Robin条件**：规定 $\alpha u+\beta\partial_nu=g$，两项单位必须相容；它可描述适当模型下的交换边界。

声学中，理想静止刚壁通常约束法向速度为零，在线性单频压力模型中对应 $\partial_nP=0$；理想压力释放面对应 $P=0$。弦的固定端约束位移，不应把“固定”二字直接翻译成声压也为零。局部阻抗边界还依赖时间约定、法向和阻抗定义，详见[亥姆霍兹方程](../helmholtz-equation/)。

### 适定性 不唯一与相容性

**适定问题**要求解存在、唯一，并在明确的函数空间与范数下连续依赖数据。连续依赖表示小输入误差不会造成不受控制的解误差；不是只凭求解器返回一条曲线就能确认。[1](#ref-mm-problem)

例如在连通有界域内，$-\Delta u=f$ 的纯Neumann问题 $\partial_nu=g$ 必须满足 $\int_\Omega f\,dV=-\int_{\partial\Omega}g\,dS$，这是散度定理的直接结果。满足相容性后，解通常仍差一个任意常数，需要规定均值等附加条件。相反，合适的Dirichlet条件可去掉常数自由度。检查这些约束，常比更换求解软件更有效。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/problem-and-boundaries.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/problem-and-boundaries.svg" alt="一段区间的两端分别规定函数值、导数或Robin组合，右侧展示固定值和零导数对应不同模态。 " width="1400" height="550" loading="lazy" /></a><figcaption>图1　同一个区间、不同边界，产生不同特征函数。曲线为满足相应齐次端点条件的示例，不是任意边界问题的通解；Neumann还包含常数零模态。</figcaption></figure>

## 分离变量与Sturm–Liouville问题

### 把空间结构与时间变化拆开

**分离变量法**尝试乘积形式 $u(x,t)=X(x)T(t)$。对 $u_t=D u_{xx}$ 代入并在非零区域整理，得 $T'/(DT)=X''/X=-\lambda$。左右依赖不同变量，故各自等于同一常数；实际检验可用不除以X、T的方程形式，避免把节点上的零误认成问题。

于是空间式为 $-X''=\lambda X$，时间式为 $T'=-D\lambda T$。对波动式同样得到空间问题，而时间式变为 $T''+c^2\lambda T=0$。边界选出允许的 $\lambda$，初态决定各模态占多少。[3](#ref-mm-heat)[4](#ref-mm-wave)

乘积解只是候选基本解。完整初态一般要用许多乘积解叠加；非齐次边界可先构造满足边界的函数b，再令 $u=b+v$，使v满足齐次边界，但其方程和初态也会改变。复杂几何或系数耦合时，单一坐标分离可能失败，并不代表原问题没有解。

### 特征值为什么由边界选出来

对区间 $0<x<L$ 上的 $-X''=\lambda X$，两端 $X=0$ 的非零解为

$$
X_n(x)=\sin\frac{n\pi x}{L},\qquad
\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad n=1,2,\ldots .
$$

若改成两端 $X'=0$，则为余弦模态，且必须加入 $n=0$ 的常数模态与零特征值。若一端为零值、一端为零导数，则允许半整数空间波数 $(n+\tfrac12)\pi/L$，n从0开始。边界决定了模态谱，不能先认定所有问题都有整数倍频率。[5](#ref-mm-sl)

### 自伴性 权重与正交性

**Sturm–Liouville问题**的常见形式为

$$
-\frac{d}{dx}\!\left[p(x)\frac{dX}{dx}\right]+q(x)X
=\lambda w(x)X .
$$

对有限区间上的正则问题，例如p连续可微、q和w连续，取实系数、p>0、w>0，并配满足边界项消去的自伴边界条件，可得到实特征值以及不同特征值特征函数的加权正交性。这里的p是数学系数，与上文声压p无关；w是权重，也不能与角频率 $\omega$ 混淆。[5](#ref-mm-sl)[6](#ref-mm-orthogonal)

加权内积为 $\langle f,g\rangle_w=\int_a^b f^*(x)g(x)w(x)\,dx$。分部积分后，两组特征式相减，得到 $(\lambda_n-\lambda_m)\langle X_m,X_n\rangle_w=0$。**自伴性**涉及算子及其定义域、边界条件，光看微分表达式相同还不够；简并特征值所在子空间可再选正交基。

在这些正则自伴条件下，可在相应加权平方可积空间中展开足够一般的数据；无穷区间、奇异端点、耗散或非自伴问题需要额外理论。实特征值也不自动表示全为正，q或Robin条件可以改变符号。振动稳定性要再结合能量和特征值检查。

权重也有物理来源。例如线密度μ(x)、张力T(x)随位置变化的理想弦，满足 $\mu u_{tt}=(T u_x)_x$；分离后为 $-(T X')'=\omega^2\mu X$。此时p=T、w=μ、λ=ω²，模态按质量加权正交，不应仍用不带μ的积分。材料参数进入的具体位置，决定了特征值和内积怎样定义。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/eigenfunctions.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/eigenfunctions.svg" alt="单位区间前三个正弦特征函数及数值积分得到的归一化内积矩阵。 " width="1400" height="550" loading="lazy" /></a><figcaption>图2　函数也可以组成正交坐标系。图中使用单位区间、权重1；左图是前三阶归一化正弦模态，右图内积接近单位矩阵。一般权重不为1时须重新计算内积。</figcaption></figure>

## 正交展开如何表示一根被拨动的弦

### 投影系数与收敛的含义

对上述正弦基，$f(x)=\sum_{n\ge1}b_n\sin(n\pi x/L)$ 的系数为

$$
b_n=\frac{2}{L}\int_0^L f(x)\sin\frac{n\pi x}{L}\,dx .
$$

这是函数空间中的投影，与[线性代数](../linear-algebra/)的正交投影相呼应。正交不等于每项峰值都为1，也不等于任取N项就精确表示所有函数。均方收敛控制的是平方误差积分；逐点或一致收敛还需要数据光滑性等条件。[6](#ref-mm-orthogonal)

例如对分段光滑函数，在适当的傅里叶展开意义下，跳跃处趋向左右极限平均，有限项会出现Gibbs现象；增加项数使振铃区域缩小，不保证跳跃附近最大过冲消失。把级数逐项求导也须核对额外条件，不能从函数展开的均方收敛直接推出任意阶导数均收敛。

### 三角初位移的系数能直接算出

取理想均匀柔弦，长度L=1 m、波速c=100 m/s，两端固定；在 $a=0.3L$ 处拨到峰位移A=1 mm，形成两段直线，初速度为零。此时

$$
f(x)=
\begin{cases}
Ax/a,&0\le x\le a,\\
A(L-x)/(L-a),&a<x\le L,
\end{cases}
\quad
b_n=\frac{2AL^2\sin(n\pi a/L)}
{\pi^2n^2a(L-a)} .
$$

系数由分段积分得到，包含拨弦位置的正弦因子和 $n^{-2}$ 衰减。若在中点拨弦，偶数模态的这个因子为零；若在0.3L处拨弦，则并非只剩奇数模态。模态是否出现还取决于激励位置、形状与观测方式，不能仅看频率列表。[4](#ref-mm-wave)

### 空间模态怎样变成振动

本例时间解为

$$
u(x,t)=\sum_{n=1}^{\infty} b_n
\cos(\omega_nt)\sin\frac{n\pi x}{L},\qquad
\omega_n=\frac{n\pi c}{L},\qquad f_n=\frac{nc}{2L}.
$$

基频50 Hz来自指定c与L，不是人耳或乐器的通用数值。若初速度展开系数为 $g_n$，还应加入 $(g_n/\omega_n)\sin(\omega_nt)$；丢掉这部分就只解了某类初态。真实弦的刚度、损耗和端点耦合会改变频率与衰减，整数倍关系不是一切振动物体的定律。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/plucked-string.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/plucked-string.svg" alt="在0.3米处拨起1毫米的三角形弦初位移，展示不同截断阶数的正弦重建和前20个模态系数。 " width="1400" height="550" loading="lazy" /></a><figcaption>图3　初态决定模态权重。左图仅重建t=0的位移，右图保留系数正负；负系数表示相位关系，不表示负能量。有限项在折点附近仍有重建误差。</figcaption></figure>

## 同一空间模态 扩散与波动有何不同

### 扩散使高空间频率更快衰减

在单位长度区间、零值端点下，扩散解为 $u(x,t)=\sum b_n e^{-D\lambda_nt}X_n(x)$。第n阶的时间常数为 $1/(D\lambda_n)$，随n²缩短；尖锐结构包含较多高阶成分，因此扩散会平滑细节。[3](#ref-mm-heat)

取D=0.1 m²/s、L=1 m，初态为 $\sin(\pi x/L)+0.4\sin(3\pi x/L)$，u用任意归一化单位。t=0.2 s时，两模态的衰减因子分别约0.8209和0.1692。第二个系数还应乘原权重0.4，而不是把衰减因子直接当新的完整模态系数。

### 无损波动交换动能与势能

相同初位形放入波速c=1 m/s的理想弦，零初速度下两项分别乘 $\cos(c\sqrt{\lambda_n}t)$，它们可变号并复现，不能像扩散那样直接按指数抹去。这里c与D是两个不同模型的参数，不把它们解释为同一材料的两种量测。

无损弦的总能量可守恒，但位移平方积分不必保持不变：某些时刻位移很小，动能却很大。因此“波形幅度变小”不能单独证明耗散；须分开动能、势能与通过边界的能流。[4](#ref-mm-wave)[18](#ref-mm-energy)

### 传播速度与数学模型的边界

全直线上的一维波动式有达朗贝尔解
$u(x,t)=\tfrac12[f(x-ct)+f(x+ct)]+\tfrac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds$。
它显示观察点只依赖初态中有限区间的数据。边界反射要另行加入；不能把全空间公式直接当有限声管解。

经典扩散方程的高斯核在任意t>0时遍及全空间，表示该近似模型没有严格有限的传播前沿；这不意味着真实物质或能量信号可以无限速传递。模型的微观适用尺度与相对论因果性是另一层限制。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/heat-and-wave.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/heat-and-wave.svg" alt="同一双模态初位形在扩散中衰减，在无损波动中振荡，横坐标均为位置。 " width="1400" height="550" loading="lazy" /></a><figcaption>图4　空间基相同，时间规律不同。左图D=0.1 m²/s，右图c=1 m/s，区间长度1 m；u为归一化场值，不将温度与位移当成相同物理量。</figcaption></figure>

## 亥姆霍兹方程 模态共振与唯一性

### 从时域进入单频问题

采用 $u(\mathbf x,t)=\operatorname{Re}[U(\mathbf x)e^{j\omega t}]$，无源波动式化为 $\Delta U+k^2U=0$，k=ω/c。它描述单一频率下的复幅值，不含任意瞬态；其空间算子属于椭圆型，但这并不保证所有频率、边界下都有唯一解。[7](#ref-mm-multi)

把 $-\Delta X_n=\lambda_n X_n$ 的齐次自伴模态用于源驱动式 $(-\Delta-k^2)U=F$，形式上有 $U_n=F_n/(\lambda_n-k^2)$。若 $k^2$ 恰等于某特征值，源在该模态上的投影非零，则理想无损稳态边值问题无解；若投影为零，则可能存在解却不唯一，因为可叠加该齐次模态。不能把分母为零解释为一个有限的“极大声压”。

### 损耗与激励投影决定响应

时域模态若满足 $q_n''+2\gamma_nq_n'+\omega_n^2q_n=F_n\cos\omega t$，γ>0时的稳态复幅值为 $F_n/(\omega_n^2-\omega^2+j2\gamma_n\omega)$。损耗使峰值有限，驱动投影 $F_n=0$ 时该模态不会被这项源激发。观测点位于模态节点，也可能看不到它。

图5只画一个归一化单模态，令r=ω/ωn、ζ=γ/ωn，幅值为 $|1/(1-r^2+j2\zeta r)|$。其位移幅值峰在 $\sqrt{1-2\zeta^2}$，仅当 $0<\zeta<1/\sqrt2$ 才有正频率峰；自然频率与幅频峰值不应无条件等同。房间或换能器须再叠加各模态、真实损耗与输入输出耦合，见[房间声学](../room-acoustics/)与[电声换能器](../electroacoustic-transducer/)。

### 无界域还要选外向波

在三维全空间中，采用上述时间约定，$G=e^{-jkr}/(4\pi r)$ 是满足 $(\Delta+k^2)G=-\delta$ 的外向自由空间核，r为到点源的距离。其相位 $\omega t-kr$ 向外传播；换成 $e^{-j\omega t}$ 时间约定时，空间指数也要相应改变。

仅写亥姆霍兹微分式并不能区分入射与辐射，需要Sommerfeld等辐射条件。自由空间核还不自动满足房间壁面条件；加入边界或非均匀介质后应构造相应问题的核。[20](#ref-mm-numerics)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/modal-resonance.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/modal-resonance.svg" alt="三个不同阻尼比的单模态稳态幅频曲线，低阻尼有尖峰，高阻尼可能无正频率峰。 " width="1400" height="550" loading="lazy" /></a><figcaption>图5　边值问题的谱与受迫响应。曲线是指定单模态的无量纲位移响应，不是房间实测频响；图示使用非零阻尼，没有把无损共振点画成有限解。</figcaption></figure>

## 特殊函数来自几何与端点要求

### 极坐标为何带来贝塞尔方程

二维极坐标的拉普拉斯算子为 $\Delta u=u_{rr}+r^{-1}u_r+r^{-2}u_{\theta\theta}$。令亥姆霍兹空间解为 $R(r)\Theta(\theta)$，绕一周单值性选出整数m，角向为 $\cos m\theta$、$\sin m\theta$，径向式为

$$
r^2R''+rR'+(\kappa^2r^2-m^2)R=0 .
$$

令z=κr，即标准贝塞尔方程。第一类 $J_m(z)$ 在整数m的原点是正则解；第二类 $Y_m(z)$ 在原点奇异，完整圆盘中要求有限场值时通常排除它。若域是环带，原点不在域中，就不能以同一理由删去 $Y_m$。[8](#ref-mm-coordinates)[9](#ref-mm-bessel)

### 幂级数怎样定义这类函数

在普通点，常可设幂级数并比较同次幂来求系数；在原点这类正则奇点，**Frobenius法**尝试 $R=z^s\sum_{k\ge0}a_kz^k$，先由最低次幂得到指标方程，再递推系数。贝塞尔式的指标为s=±m；根重合或相差整数时，第二个独立解可能涉及对数，不能保证两套普通幂级数足够。

对非负整数m，第一类解的标准归一化可由收敛级数定义：$J_m(z)=\sum_{k=0}^\infty(-1)^k(z/2)^{2k+m}/[k!(k+m)!]$。它给出 $J_0(0)=1$，m>0时近原点为 $(z/2)^m/m!$，而不只是给某条曲线取一个名称。大自变量或大量阶数时，直接截断级数未必是数值上最佳算法，需要稳定递推、渐近式或经过核验的函数库。[9](#ref-mm-bessel)

### 圆膜与圆管不能用同一组零点

半径a、边缘固定的理想均匀张紧圆膜，其位移满足 $R(a)=0$，故 $\kappa_{mn}a=j_{m,n}$，其中 $j_{m,n}$ 是 $J_m$ 的第n个正零点。若膜面内波速为c，$f_{mn}=c j_{m,n}/(2\pi a)$。指定a=0.1 m、c=20 m/s，m=0的前两零点约2.40483、5.52008，对应76.55、175.71 Hz；频率比约2.295，不是整数2。[10](#ref-mm-bessel-zeros)

圆形刚壁声管的横向压力则满足 $R'(a)=0$，使用导数零点；m=0还有κ=0的均匀平面模态。不要把“圆形”当成唯一条件，也不要漏掉零横向波数。轴向波数由 $k_z^2=k^2-\kappa^2$ 决定，高于相应截止频率才有实轴向传播波数；以下为倏逝行为，不能只用横向模态图宣布它一定传播。

径向正交积分带权r：$\int_0^a R_nR_s\,r\,dr$。对固定边界、同m不同正零点，积分为零；对角项为 $\tfrac12a^2[J_{m+1}(j_{m,n})]^2$。权重来自面积元 $r\,dr\,d\theta$，不是可以随手去掉的系数。[11](#ref-mm-bessel-integral)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/circular-modes.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/circular-modes.svg" alt="固定边缘圆膜的四种贝塞尔模态，以有正负的颜色表示瞬时位移，显示节径与节圆。 " width="1400" height="550" loading="lazy" /></a><figcaption>图6　边界与几何共同选择特殊函数。四图均为固定边缘理想圆膜，分别单独归一化；颜色表示相对位移的符号和幅值，白色节线不是材料裂缝，也不表示声压分布。</figcaption></figure>

### 勒让德多项式与球谐函数

球对称几何把角变量带到另一类方程。勒让德方程为 $(1-z^2)y''-2zy'+\ell(\ell+1)y=0$；当ℓ为非负整数时，勒让德多项式 $P_\ell(z)$ 在[-1,1]上有界。前几项为 $P_0=1$、$P_1=z$、$P_2=(3z^2-1)/2$，并满足 $\int_{-1}^1P_\ell P_s\,dz=2\delta_{\ell s}/(2\ell+1)$。[12](#ref-mm-legendre)

在球面上，**球谐函数** $Y_\ell^m(\theta,\varphi)$ 是球面拉普拉斯算子的特征函数，$\Delta_{S^2}Y_\ell^m=-\ell(\ell+1)Y_\ell^m$，$-\ell\le m\le\ell$。标准正交归一约定下 $\int Y_\ell^{m*}Y_{\ell'}^{m'}d\Omega=\delta_{\ell\ell'}\delta_{mm'}$，其中 $d\Omega=\sin\theta\,d\theta\,d\varphi$；不同教材的相位、实基/复基和归一化可能不同，比较系数前要先对齐。[13](#ref-mm-harmonics)

轴对称时m=0，角向正比于 $P_\ell(\cos\theta)$；三维拉普拉斯式的径向因子则为 $r^\ell$ 和 $r^{-\ell-1}$。球内含原点的有限解通常保留前者，球外要求适当远场衰减时选后者；亥姆霍兹径向应换成球贝塞尔函数。角向的球谐函数本身不能代替完整径向解。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/angular-modes.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/angular-modes.svg" alt="勒让德多项式前四阶曲线，以及轴对称Pℓ(cosθ)的极坐标幅值形状，颜色区别正负。 " width="1400" height="550" loading="lazy" /></a><figcaption>图7　角向函数不是物体外形。右侧用半径画绝对值、颜色区分正负，只示意轴对称角向因子；未经完整边值求解，不能当成某麦克风或头部的指向性。</figcaption></figure>

## 积分变换把微分变成代数

### 傅里叶变换与连续谱

有限区间的边界常产生离散模态，全空间的平移对称性则适合傅里叶变换。本篇空间约定为 $\hat u(k)=\int_{\mathbb R}u(x)e^{-jkx}\,dx$，逆变换为 $u(x)=(2\pi)^{-1}\int\hat u(k)e^{jkx}\,dk$。这里k单位rad/m，与时间频率Hz不同。[14](#ref-mm-fourier)

在足够衰减、可分部积分的条件下，$\widehat{u_x}=jk\hat u$、$\widehat{u_{xx}}=-k^2\hat u$；更一般可在分布意义下解释。扩散式变为 $\partial_t\hat u=-Dk^2\hat u$，故 $\hat u(k,t)=e^{-Dk^2t}\hat f(k)$。不是把空间和时间都“消掉”，而是把空间耦合转成每个k的一条时间方程。

### 高斯核体现卷积与尺度

逆变换得到全直线的热核

$$
K(x,t)=\frac{1}{\sqrt{4\pi Dt}}
\exp\!\left(-\frac{x^2}{4Dt}\right),\quad t>0,
\qquad
u(x,t)=\int_{\mathbb R}K(x-\xi,t)f(\xi)\,d\xi .
$$

核的空间积分为1，二阶矩为2Dt，单位为1/m；因此卷积后的u与f单位相同。随t增大，宽度增加、峰值降低。若初态是积分为1的高斯、初始方差σ₀²，则后续方差为σ₀²+2Dt，不是σ₀+2Dt。[14](#ref-mm-fourier)

这个核属于全空间常系数问题。有限区间的零值、绝热或混合边界需要镜像或特征函数等方式修正；直接把测量数据与自由空间核卷积，不会自动实现任意壁面条件。

### 拉普拉斯变换必须保留初值

单边拉普拉斯变换定义为 $U(s)=\int_{0^-}^\infty u(t)e^{-st}dt$，并需说明收敛半平面及初值约定。对本篇常规光滑初态，$\mathcal L[u']=sU-u(0^-)$，$\mathcal L[u'']=s^2U-su(0^-)-u'(0^-)$。初值项消失并不是变换的默认规则；只有相应零初态问题才可省去。[15](#ref-mm-laplace)

对波动模态，$q''+\omega_n^2q=f_n(t)$ 变为
$Q=[F_n+s q(0)+q'(0)]/(s^2+\omega_n^2)$。
变换便于处理阶跃、冲激与强迫项，但反变换和极点仍要与因果性、边界和收敛域相配合。更多复变量细节见[复变函数](../complex-analysis/)，电路初态的同类用法见[电路原理](../circuit-theory/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/heat-kernel.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/heat-kernel.svg" alt="高斯初态随扩散变宽变矮，右图空间傅里叶乘子对高波数衰减更快。 " width="1400" height="550" loading="lazy" /></a><figcaption>图8　同一扩散过程的空间与波数描述。采用全直线、D=0.1 m²/s、初始标准差0.1 m、积分为1的高斯；右侧k为角波数，不是时间频率。图中形状不代表声压随传播距离的通用变化。</figcaption></figure>

## 格林函数把点源响应叠成一般解

### δ是分布 不是普通无限高函数

**Dirac δ分布**由其对光滑紧支撑测试函数的作用定义：$\int\delta(x-\xi)\phi(x)\,dx=\phi(\xi)$。它不是一个普通函数，不能把“某点无限大、别处为零”当作完整数学定义；对量纲明确的一维坐标，δ的单位为1/长度。[16](#ref-mm-distribution)

分布导数通过分部积分定义，$\langle T',\phi\rangle=-\langle T,\phi'\rangle$。因此折线的斜率跃变可以在二阶导数中产生δ，点载荷和冲激就能纳入方程。有限宽高斯或窄脉冲只是δ的近似序列；网格上必须同时控制积分权重，不能把单格值置为1就声称有单位总源强。

### 一维例子可以完整检查

定义区间[0,L]上算子 $\mathcal L=-d^2/dx^2$、两端零值条件的**格林函数**为 $\mathcal L G(x,\xi)=\delta(x-\xi)$，且x=0、L时G=0。其表达式为

$$
G(x,\xi)=\frac{x_<\,(L-x_>)}{L},\quad
x_<=\min(x,\xi),\quad x_>=\max(x,\xi).
$$

它在x=ξ处连续，而导数满足 $G_x(\xi^+,\xi)-G_x(\xi^-,\xi)=-1$，负号来自算子定义。对 $-u''=f$、齐次边界，$u(x)=\int_0^L G(x,\xi)f(\xi)d\xi$。例如f=f₀为常数，得到 $u=f_0x(L-x)/2$，可直接二次求导验证。[17](#ref-mm-green)

L=1 m、ξ=0.3 m时，G在源点为0.21 m，单位不是无量纲；若u为位移，f的单位应为位移/长度²。图中用单位长度归一化，避免把数学源f误当成尚未除以张力的机械力。

### 格林函数依赖算子和全部条件

上例有 $G(x,\xi)=G(\xi,x)$，反映相应实自伴问题的互易结构；非自伴、带偏置流或特殊边界时不能照搬。对时间演化，因果格林函数还要求响应不先于激励，并需包含初态的贡献。

格林函数法与模态法可相遇：在合适可逆自伴问题中，核可用 $X_n(x)X_n^*(\xi)/\lambda_n$ 的归一化谱和表示；若有零模态，逆算子并不存在于整个空间，要先处理相容性与投影。非齐次边界还会出现边界项，不是仅积分体源就结束。[17](#ref-mm-green)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/green-function.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/green-function.svg" alt="零端点负二阶导算子的三条点源格林函数，以及均匀源积分产生的抛物线解。 " width="1400" height="550" loading="lazy" /></a><figcaption>图9　点源响应受边界约束。左图折点处函数连续、斜率跳变；右图比较格林积分与解析解。坐标按L归一化，不能把自由空间核与此有限区间核互换。</figcaption></figure>

## 能量法 弱形式与变分法

### 不求出显式解也能检查唯一性

对两端固定的理想弦，线密度μ、张力T恒正，能量为
$E=\tfrac12\int_0^L[\mu u_t^2+T u_x^2]dx$。
由 $\mu u_{tt}=T u_{xx}$ 分部积分得 $dE/dt=[T u_tu_x]_0^L$。固定端随时间保持位移零，故端点速度也为零、边界功率为零；若端点运动，边界项可能输入能量。[18](#ref-mm-energy)

把两解作差，若方程、初态、边界相同，差解初始能量为零且一直为零；在上述正定条件和固定边界下可推出差解为零，得到唯一性。扩散也可用 $\tfrac12d\|u\|_2^2/dt=-D\|u_x\|_2^2$ 检查零边界齐次解的衰减。能量等式的符号和边界项是审查推导的有效工具。

### 弱形式把高阶导数要求降低

对 $-u''=f$、零值端点，乘测试函数v、积分并分部积分，得到 $\int_0^L u'v'\,dx=\int_0^L fv\,dx$。测试函数端点也为零；更一般需用适当Sobolev空间，导数在弱意义下存在。[16](#ref-mm-distribution)

这里 $H^1(0,L)$ 表示函数与一阶弱导数都平方可积的Sobolev空间，$H_0^1(0,L)$ 再要求零边界迹；在本例中求u和选v都使用后者。**弱解**满足这类积分关系，不要求处处存在经典二阶导数。它不是“比较不准确的解”，而是换了满足方程的意义；若解有足够光滑性且边界适当，弱形式与经典形式可对应。数值网格上的近似解，又是弱问题的有限维近似，不能把这三层混在一起。

### 变分极值与Rayleigh商

对本例，泛函 $J[u]=\tfrac12\int(u')^2dx-\int fu\,dx$ 在零端点试探空间中的驻点给出同一弱式；因二次型正定，它还是唯一极小点。若泛函不凸或约束改变，“驻点”不必是最小值。[19](#ref-mm-variational)

对零值或适当零通量边界，特征问题的Rayleigh商为 $\mathcal R[X]=\int[p|X'|^2+q|X|^2]dx/\int w|X|^2dx$，须在满足本质边界约束的非零试探函数中使用；一般Robin条件还会贡献边界二次项，不能直接省去。对 $-X''$ 的零值端点，取 $X=x(L-x)$ 得 $\mathcal R=10/L^2$，高于精确第一特征值 $\pi^2/L^2$。这是第一特征值的变分上界，不意味着任何离散频率都必定偏高。

有限元法将弱式投到有限试探空间，形成刚度矩阵K与质量矩阵M，特征问题为 $K\mathbf a=\lambda M\mathbf a$。矩阵维度、边界处理和积分精度都要检查；“用了有限元”本身不能保证模型、网格或结果正确。

## 数值解需要稳定性与收敛性核验

### 差分把空间算子变成矩阵

均匀网格上，中心差分 $(u_{j+1}-2u_j+u_{j-1})/\Delta x^2$ 近似 $u_{xx}$，对足够光滑函数局部空间误差为 $O(\Delta x^2)$。零值边界的负二阶导矩阵为三对角形式，其低阶特征值趋近连续值；高阶接近网格尺度时可能有明显误差。[20](#ref-mm-numerics)

对区间L、M个等长网格单元，内部矩阵特征值为 $\lambda_n^h=4\sin^2(n\pi/(2M))/\Delta x^2$。M=20时第一特征值约9.8493/L²，小于π²/L²；M翻倍后误差约缩小四倍。它与上一节Rayleigh试探函数的上界不矛盾，因为离散方式不同。

### 稳定不等于准确

对一维常系数热方程的前向Euler加中心空间差分，令r=DΔt/Δx²，标准无限/周期网格傅里叶稳定分析给出 $0\le r\le1/2$；常规零值边界下它也是常用充分限制。r太大，高频误差会被放大。隐式方法可能解除这一稳定限制，却仍需时间步足够小才能准确。

对一维二阶波动式的显式时间、空间中心差分，标准条件为ν=cΔt/Δx≤1；多维与非均匀问题条件会改变。离散平面波满足 $\sin^2(\omega_h\Delta t/2)=\nu^2\sin^2(k\Delta x/2)$，说明满足CFL仍可能存在数值色散。只有特定一维常系数设置中ν=1的特殊性质，不能推广成任意网格无色散。[20](#ref-mm-numerics)

### 怎样证明结果值得信任

至少区分三层：离散方程是否解对、离散是否逼近目标PDE、目标PDE是否适合真实对象。小残差主要支持第一层；网格加密、时间步缩小、解析特例与独立方法比较支持第二层；第三层还需要材料、几何、边界和实验数据。

复杂声学还要核对外域截断反射、边界损耗、源与传感器位置、点源正则化和频率覆盖。把网格画得很细并不弥补错误的边界条件。若要从含噪声结果反推源或材料，稳定的正向问题也不保证反问题稳定，正则化等内容可与[线性代数](../linear-algebra/)配套阅读。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/mathematical-physics-methods/numerical-checks.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/mathematical-physics-methods/numerical-checks.svg" alt="中心差分第一特征值误差随网格数按二阶缩小，以及不同Courant数的波动相速度误差。 " width="1400" height="550" loading="lazy" /></a><figcaption>图10　数值方法也有可检验的结构。左图为零端点区间问题的空间离散误差；右图来自一维常系数中心格式的离散色散式，两图不是同一个时域仿真实验。</figcaption></figure>

## 可复算的例子与学习路线

### 检查拨弦系数而非只看动画

下例用独立数值积分核对分段解析系数。只需NumPy和SciPy；米为长度单位，系数也为米。

```python
import numpy as np
from scipy.integrate import quad
L, a, A = 1., .3, .001
def f(x):
    return A*x/a if x <= a else A*(L-x)/(L-a)
n = np.arange(1, 11)
formula = 2*A*L**2*np.sin(n*np.pi*a/L)/(np.pi**2*n*n*a*(L-a))
numeric = np.array([2/L*quad(
    lambda x: f(x)*np.sin(i*np.pi*x/L), 0, L,
    points=[a], epsabs=1e-13)[0] for i in n])
print(formula[:3])
assert np.allclose(formula, numeric, atol=1e-12, rtol=1e-9)
```

第10项接近零来自 $\sin(3\pi)$，只是本例拨弦位置造成的选择；浮点输出接近零时应按容限判断，不以是否精确等于0作为物理结论。

### 检查格林核的边界和源积分

下例把均匀源通过核积分，和解析抛物线比较。L=1，坐标及场量取归一化单位。

```python
import numpy as np
from scipy.integrate import quad
def G(x, xi):
    return min(x, xi)*(1-max(x, xi))
x = np.linspace(0, 1, 21)
u = np.array([quad(lambda xi: G(xx, xi), 0, 1,
                  points=[xx], epsabs=1e-12)[0] for xx in x])
exact = x*(1-x)/2
print(np.max(np.abs(u-exact)))
assert np.max(np.abs(u-exact)) < 1e-10
assert G(0, .3) == 0 and G(1, .3) == 0
```

零端点和积分正确还不能替代源点的导数跳跃检查；完整实验脚本同时检查此跳跃，以及与独立三对角差分解的比较。

### 以网格加密核对特征值

下例直接构造矩阵并求最低特征值，再比较解析值π²。输出误差比接近4，指这组规则网格和光滑第一模态进入二阶收敛区域。

```python
import numpy as np
errors = []
for M in [20, 40, 80]:
    h = 1/M
    K = (2*np.eye(M-1)-np.eye(M-1, k=1)-np.eye(M-1, k=-1))/h**2
    first = np.linalg.eigvalsh(K)[0]
    errors.append(abs(first-np.pi**2))
print(errors, np.array(errors[:-1])/errors[1:])
assert 3.9 < errors[0]/errors[1] < 4.1
assert 3.9 < errors[1]/errors[2] < 4.1
```

[完整实验脚本](/n3-hearingpedia/code/mathematical-physics-methods/experiments.py)另含扩散/波动模态、圆膜零点、格林核与高斯尺度计算。均为指定理想问题的复算，没有把软件调用当作真实耳部结构或器件的实验验证。

### 六个问题检查理解

1. 为什么只写波动方程还不足以确定解？分别说明初位形、初速度与边界的作用。
2. 两端零值与两端零导数的特征谱有何不同？常数零模态会怎样影响可逆性与唯一性？
3. 同一初态为何在扩散中平滑、在无损弦上振荡？位移平方积分是否等于总能量？
4. 为什么固定圆膜用贝塞尔函数零点、刚壁圆管用导数零点？径向内积为什么含r？
5. 改写算子从 $-u''$ 为 $u''$ 时，格林函数的导数跳跃符号应怎样改变？
6. 为什么小残差、满足CFL和网格加密，都还不足以单独证明真实声学模型正确？

入门可先沿“定解条件—正弦模态—扩散与波动—数值特例”学习；再补特殊函数、积分变换和格林函数，最后进入能量法、弱形式与复杂模型。阅读听觉或声学论文时，依次确认未知量、单位、介质与几何、边界、激励、初态、解法和验证，能避免把漂亮的场图误当成完整证据。

本篇来源核对日期为2026年11月2日。依据原作者课程资料、在线教材和NIST数学函数手册开展定向核对；未开展穷尽的数学文献综述。推导、原创图和数值实现经过检查，内容仍保留待专业审阅状态。
