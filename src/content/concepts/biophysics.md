---
title: "生物物理学"
english: "Biophysics"
slug: "biophysics"
summary: "作为《计算神经科学》的配套篇，从热运动、自由能、扩散和反应进入电化学势、膜电容、离子通道、电缆与细胞力学，再以毛细胞的机械电转导、耳蜗电势和带状突触连接听觉，明确模型参数、能量来源、随机性及实验边界。"
categories: ["neuroscience", "research-methods", "ear-cochlea"]
tags: ["基础课程", "生物物理学", "自由能", "扩散", "电化学势", "膜电位", "离子通道", "机械电转导"]
aliases: ["生物物理", "神经生物物理基础", "Biophysical Foundations of Neuroscience"]
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
  - {label: "课程定位", value: "用物理定律约束生命系统的结构、运动、能量与测量"}
  - {label: "配套主线", value: "为计算神经科学中的电容、电导、反转电位、时间常数和噪声提供来源"}
  - {label: "听觉连接", value: "毛束机械电转导、耳蜗电势、外毛细胞电动性与带状突触"}
  - {label: "模型边界", value: "平衡、稳态、小信号、局部近似与真实细胞需分别检验"}
references: ["bp-overview", "bp-boltzmann", "bp-brownian", "bp-fick", "bp-peclet", "bp-binding", "bp-osmosis", "bp-migration", "bp-electrochem", "bp-nernst", "bp-goldman", "bp-electric", "bp-passive", "bp-hh", "bp-cable", "bp-viscosity", "bp-stokes", "bp-met-original", "bp-endocochlear", "bp-hair-text", "bp-prestin", "bp-prestin-knockout", "bp-synapse", "bp-ribbon"]
order: 1011
---

**生物物理学**（biophysics）用物理定律、定量实验和数学模型研究生命系统。它既研究分子结构与相互作用，也研究膜、细胞和组织怎样输运物质、转换能量、产生力与信号。生命系统通常处于持续交换物质和能量的非平衡状态，因此不能把“像电路”“像弹簧”当成完整解释，必须说明相应近似、尺度和能量来源。[1](#ref-bp-overview)

本篇与[计算神经科学](../computational-neuroscience/)配套：后者侧重怎样把神经系统假设变成模型、编码和可检验输出；本篇侧重模型中的电容、电导、反转电位、扩散常数、力和随机性从哪里来。它也连接[电路原理](../circuit-theory/)、[概率论](../probability-theory/)和[数学物理方法](../mathematical-physics-methods/)。已有的神经网络、脉冲统计与学习规则不在这里重复展开。

生物物理学的范围很广，本篇聚焦与神经和听觉研究紧密相关的统计、膜、输运及力学基础，不覆盖结构解析、全部分子模拟或所有成像方法。所需准备为基础力学、电学、微积分与简单化学；十幅图、参数和代码均为原创教学设定，不是患者、听者、细胞或器件实测，也不把一个理想膜模型当成真实鼓膜或耳蜗的完整模型。

## 先看尺度 单位与模型对象

### 从单分子到细胞 不同量不能直接相加

膜厚常处于纳米尺度，细胞几何常以微米描述，浓度可用mol/L，单通道电流可小到pA。计算时必须先对齐单位。例如1 mM=1 mol/m³，1 pA=10⁻¹² A；看上去“都是小数”的量并不自动在同一数量级。

电导g的单位是S，通透率P通常为m/s，扩散系数D为m²/s，膜比电容为F/m²。它们描述不同关系：电导连接电流与电压，通透率连接跨膜输运与浓度/电场，扩散系数连接浓度梯度与通量。不能在没有推导的情况下把P当成g代入。

### 约定好方向 才能解释符号

本文定义膜电位 $V=\phi_{\rm in}-\phi_{\rm out}$，常规离子电流以**正电荷向外**为正，注入细胞的电流 $I_{\rm inj}$ 以向内为正。离子粒子运动方向与常规电流方向并不总相同：负离子向内运动产生向外的常规电流。

温度用绝对温度K。本文统一使用SI常数 $k_B=1.380649\times10^{-23}$ J/K、$e=1.602176634\times10^{-19}$ C、$N_A=6.02214076\times10^{23}$ mol⁻¹，并由R=NₐkB、F=Nₐe计算气体与Faraday常数。所有标为“归一化”的图另行说明，不将无单位输出直接标成生理电压或听觉获益。

## 热运动 自由能与非平衡生命系统

### kBT是分子尺度的能量参照

**热运动**是有限温度下微观自由度的持续涨落。T=310 K时，kBT约为4.28×10⁻²¹ J，即4.28 pN·nm；RT约2.58 kJ/mol。前者是每个粒子的能量尺度，后者是每摩尔，二者不能少乘或多乘一个Avogadro常数。

在适当热平衡条件下，微观状态s的概率满足Boltzmann权重 $p_s\propto e^{-E_s/(k_BT)}$。若把许多微观状态合成“开”“闭”等宏观状态，其简并度与环境贡献应计入有效自由能，不能只比较某一个构象的势能。[2](#ref-bp-boltzmann)

### 二状态概率的形状来自能量差

令 $\Delta G=G_{\rm open}-G_{\rm closed}$ 为已包含所需统计与环境效应的自由能差。在适合的平衡或局部准平衡二状态模型中，

$$
\frac{P_{\rm open}}{P_{\rm closed}}=e^{-\Delta G/(k_BT)},\qquad
P_{\rm open}=\frac{1}{1+e^{\Delta G/(k_BT)}}.
$$

ΔG=0时开概率为1/2；ΔG=+2kBT时约0.119，−2kBT时约0.881。电压、配体或力可以改变ΔG，但各自的耦合项和控制条件要写明。一个S形拟合曲线并不能独自证明系统真的只有两个构象，也不能识别某种蛋白。[2](#ref-bp-boltzmann)

### 平衡 稳态与耗能不能混同

热力学平衡没有持续的净驱动通量；**稳态**只表示宏观状态不再随时间变化，仍可有持续离子流和代谢耗能。固定温度压力下常用Gibbs自由能，固定温度体积下可用Helmholtz自由能；讨论机械控制或交换粒子的系统时，还须使用相应的有效势。

离子泵、分子马达和维持细胞组成需要自由能输入，ATP水解的实际自由能取决于反应物浓度与环境，并非一个在所有细胞中固定的数字。细胞局部有序也不违反热力学第二定律，因为它是开放系统，总熵产生要把环境一起计入。后文的通道和机械元件可暂时借用局部平衡模型，却不代表整个细胞已处于平衡。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/energy-and-states.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/biophysics/energy-and-states.svg" alt="二状态模型的开概率随开态与闭态自由能差变化，另一面板比较指定分子力学功与kBT尺度。 " width="1400" height="550" loading="lazy" /></a><figcaption>图1　能量差决定概率偏向，不把热涨落简单等同于误差。T=310 K；机械功示例为指定的力乘位移，仅用于数量级比较，不是某个马达的ATP计量或效率测量。</figcaption></figure>

## 扩散 反应与渗透

### 随机运动怎样形成确定的输运规律

对均匀、各向同性、无漂移的正常扩散，每一坐标的均方位移为2Dt，d维总均方位移为2dDt。**均方位移**是位移平方的统计平均，不是每个分子一定走过的距离；一维、二维膜面和三维体积的系数要分开。[3](#ref-bp-brownian)

一维点初态的归一化扩散核为

$$
p(x,t)=\frac{1}{\sqrt{4\pi Dt}}
\exp\!\left(-\frac{x^2}{4Dt}\right),\qquad t>0.
$$

它描述概率密度；要变成具体物质浓度，还需源强、空间维数、几何与边界。若取D=100 µm²/s，均方位移达到L²的一维时间尺度 $L^2/(2D)$，L=10 µm时为0.5 s，100 µm时为50 s。此处不是首次到达时间，也不直接预测递质清除时间。

### Fick定律与流动的竞争

理想稀溶液常用Fick通量 $\mathbf J=-D\nabla c$，J若以物质的量计为mol/(m²·s)。结合质量守恒与恒定D得到 $c_t=D\Delta c$；有反应、流动或变系数时应保留相应项和边界。[4](#ref-bp-fick)

球形粒子在连续牛顿流体、低Reynolds数、稀释和平衡等条件下，Stokes–Einstein关系为 $D=k_BT/(6\pi\eta r)$。指定T=310 K、黏度η=1 mPa·s、半径r=5 nm，D约45.4 µm²/s。细胞质拥挤、结合、主动运输和膜内运动可能偏离该模型，不应把水中估计当作所有分子的实测D。[3](#ref-bp-brownian)

若存在速度U和长度L，Péclet数Pe=UL/D比较对流与扩散；反应还会引入新的时间尺度。膜两侧的一个浓度值不能代替完整的扩散—反应—流动场。[5](#ref-bp-peclet)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/diffusion-scales.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/biophysics/diffusion-scales.svg" alt="一维高斯扩散核随时间展宽，均方距离达到给定尺度所需时间随长度平方增加。 " width="1400" height="550" loading="lazy" /></a><figcaption>图2　扩散没有一条固定速度轨迹。使用D=100 µm²/s、全直线与点初态；左图为概率密度，右图为一维均方位移时间尺度，不是首次到达或实际突触几何的仿真。</figcaption></figure>

### 配体结合同时有平衡常数和速率

对单个位点的简单结合 $L+R\rightleftharpoons LR$，令游离配体浓度c由大储库近似保持，结合占比θ满足

$$
\dot\theta=k_{\rm on}c(1-\theta)-k_{\rm off}\theta,\quad
K_d=\frac{k_{\rm off}}{k_{\rm on}},\quad
\theta_\infty=\frac{c}{K_d+c}.
$$

k_on若以M⁻¹s⁻¹计，c就必须用mol/L；k_off为s⁻¹，Kd为浓度。松弛时间 $\tau=1/(k_{\rm on}c+k_{\rm off})$。相同Kd可由快或慢的不同速率组合产生，所以相同稳态剂量曲线不保证相同动态响应。[6](#ref-bp-binding)

例如k_on=10⁶ M⁻¹s⁻¹、k_off=1 s⁻¹、c=2 µM，平衡占比2/3，时间常数1/3 s。若c会被消耗、受扩散限制或存在多个状态，就要一起求解。Hill曲线中的指数可以反映合作性或其他综合效应，但不能仅凭拟合指数宣布真实结合位点数。

### 渗透压连接水与溶质

理想稀溶液的渗透压近似为 $\Pi=RTc_{\rm osm}$，c_osm按渗透活性粒子的总摩尔浓度计。310 K下，1 mM的理想粒子浓度差对应约2.58 kPa，而不是1 mM就等于一个固定水流速度。能否跨膜、反射系数、压力差与水通透性会影响实际体积变化。

等渗透浓度与对细胞长期体积影响相同并不总是一回事，因为溶质可能透膜。固定电荷还可引出Donnan分配：理想一价盐的平衡中，膜内外阳、阴离子浓度乘积相等，同时各侧近似电中性，但浓度可以不相等。活细胞含泵和多种不透物，不能把被动Donnan平衡直接当作它的一般稳态。[7](#ref-bp-osmosis)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/binding-kinetics.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/biophysics/binding-kinetics.svg" alt="三种具有相同解离常数的结合模型有相同平衡曲线，却有不同的浓度阶跃响应速度。 " width="1400" height="550" loading="lazy" /></a><figcaption>图3　平衡相同不等于动力学相同。各模型同时缩放结合、解离速率，Kd均为1 µM；右图游离配体固定在2 µM、初始占比为0，没有模拟有限配体池或空间扩散。</figcaption></figure>

## 电化学势与膜电位

### 离子同时感受浓度和电场

对同一种离子，在相应理想化条件下可写摩尔电化学势

$$
\widetilde\mu=\mu^0+RT\ln a+zF\phi.
$$

a为无量纲活度，z为价数，φ为电势。理想稀溶液常用浓度比近似活度比；高离子强度、结合与局部场可能需要修正。浓度差不是唯一驱动力，电势差也不是唯一驱动力。[8](#ref-bp-migration)[9](#ref-bp-electrochem)

忽略对流、取恒温理想溶液时，Nernst–Planck式可写 $\mathbf J=-D[\nabla c+(zF/RT)c\nabla\phi]$。第一项扩散，第二项电迁移。它是带假设的连续输运模型，不自动包含每个离子通道内的选择性结构和离散占据。

### Nernst电位怎样从平衡推出来

同一种离子在膜内外电化学势相等时，令 $V=\phi_{\rm in}-\phi_{\rm out}$，得到

$$
E_i=\frac{RT}{z_iF}\ln\frac{a_{\rm out}}{a_{\rm in}}.
$$

这叫该离子的**平衡电位**。310 K时，一价阳离子每十倍活度比约对应61.5 mV；负离子的z改变符号。指定教学浓度K⁺内140、外5 mM，Na⁺内12、外145 mM，Cl⁻内10、外120 mM，理想近似下各电位约−89.0、+66.6、−66.4 mV。它们不构成某个真实细胞的完整参数表。[10](#ref-bp-nernst)

单一选择性离子通路的反转电位在适当条件下等于相应Nernst电位；混合离子通道的反转电位则不一定等于任意一种离子的E。必须区分“这个离子的平衡电位”“通道总电流为零的电位”和“细胞静息电位”。

### 静息通常是稳态 不是所有离子都平衡

在恒场、独立通透、单价离子及相应稳态等近似下，常用的GHK电压式为

$$
V_{\rm GHK}=\frac{RT}{F}\ln
\frac{P_K[K]_{\rm out}+P_{\rm Na}[Na]_{\rm out}+P_{\rm Cl}[Cl]_{\rm in}}
{P_K[K]_{\rm in}+P_{\rm Na}[Na]_{\rm in}+P_{\rm Cl}[Cl]_{\rm out}}.
$$

Cl的内外位置与阳离子相反。这里P是通透率，不是电导；不能把Ca²⁺直接塞进同一个单价式，也不能把它说成普遍精确的细胞定律。Goldman原始工作提供相关膜输运背景，本文公式按明确约定独立计算。[11](#ref-bp-goldman)

零净电流允许不同离子各有非零电流，浓度梯度需要主动过程维持；电生性泵还可直接贡献电流。因此把浓度设为固定参数，是适当时间尺度上的储库近似，不是声称离子梯度不会消耗。[10](#ref-bp-nernst)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/electrochemical-potentials.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/biophysics/electrochemical-potentials.svg" alt="三种指定离子的Nernst电位及GHK电位随钾离子外浓度改变的计算，明确温度和通透率比例。 " width="1400" height="550" loading="lazy" /></a><figcaption>图4　一个静息电位不等于每种离子都处于平衡。T=310 K，浓度均为指定理想活度近似；GHK取相对通透率PK:PNa:PCl=1:0.04:0.45，曲线不是人体或毛细胞记录。</figcaption></figure>

## 膜电容与被动电响应

### 脂双层怎样成为电容

细胞膜把导电液体隔开，薄介电层及界面电荷可在一定范围内用电容表示。平板近似 $C=\epsilon A/d$ 中ε为介电常数、A为面积、d为厚度；真实膜的组成、表面与电压依赖会影响测量。常用模型比电容1 µF/cm²等于0.01 F/m²，不是1 F/m²。[12](#ref-bp-electric)[14](#ref-bp-hh)

指定面积1000 µm²，则总C=10 pF；在70 mV电压差下，电容两侧分离电荷的量级 $|Q|=C|V|$，约对应4.37×10⁶个单位电荷。若另指定体积1 pL、K⁺浓度140 mM，总K⁺数约8.43×10¹⁰，前者仅约5.2×10⁻⁵倍。这个数量级说明形成膜电压不要求整个胞质大幅失去电中性；它不是每次动作电位实际交换离子总数的计算。

### 电流守恒与时间常数

沿用向外离子电流、向内注入电流约定，被动膜满足

$$
C\dot V=-g_L(V-E_L)+I_{\rm inj},\qquad
\tau_m=\frac{C}{g_L},\qquad
V_\infty=E_L+\frac{I_{\rm inj}}{g_L}.
$$

恒定参数和阶跃输入下，
$V(t)=V_\infty+[V(0)-V_\infty]e^{-t/\tau_m}$。
若C=10 pF、gL=1 nS、EL=−70 mV，注入20 pA，则τ=10 ms，终值−50 mV，10 ms时约−57.36 mV。这只是被动响应，不包含动作电位、阈值或复位。[13](#ref-bp-passive)

### 电容储能与离子梯度不是同一个能量库

理想电容能量为CV²/2，电流改变电容电荷；离子跨膜的电化学自由能由电势与浓度共同决定。电导支路画成“电池加电阻”时，电池是对梯度驱动力的等效，不表示细胞内部真的存在一枚可无限供能的电池。

面积归一的Cm、gm、Im与整细胞C、g、I不能混用，须同时乘面积。电压钳中还可能量到通道门控电荷和非线性电容，不能把全部电容变化都归于几何面积。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/passive-membrane.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/biophysics/passive-membrane.svg" alt="指定被动膜在电流阶跃后按10毫秒时间常数接近新平衡，另一面板比较电容和漏电支路电流。 " width="1400" height="550" loading="lazy" /></a><figcaption>图5　膜电容使电压连续变化。C=10 pF、gL=1 nS、EL=−70 mV、注入20 pA，初态为EL；支路图采用本文电流方向，未加入电压门控或生成脉冲。</figcaption></figure>

## 离子通道的动力学与随机性

### 开概率不等于瞬间电流

对简化通道，$\dot p=\alpha(V)(1-p)-\beta(V)p$。在固定电压下，$p_\infty=\alpha/(\alpha+\beta)$、$\tau=1/(\alpha+\beta)$；若电压或配体变化，速率也可随之变。二状态概率的稳态与热平衡Boltzmann表达要有相容的速率比，不能随意拼接。[14](#ref-bp-hh)

N个相同、独立通道，单通道电导γ，可在欧姆近似下写平均电流 $\langle I\rangle=N\gamma p(V-E)$。打开更多通道只改变电导；电流还取决于驱动力V−E。即使通道开放，V=E时平均净电流也可为零；真实电流—电压关系还可能整流或饱和。

### 有限通道数产生涨落

固定p、独立同分布条件下，开放数n服从二项分布，$\langle n\rangle=Np$、$\operatorname{Var}(n)=Np(1-p)$。若每个开放通道电流固定为i，平均电流Np i，方差Np(1−p)i²。通道之间的相关性、多状态、环境波动会改变这些关系。

指定i=−1 pA、p=0.2，N=100时均值−20 pA、标准差4 pA；N=10000时均值−2000 pA、标准差40 pA。绝对涨落增大而相对涨落减小，不能只看“噪声更大”而忽略平均尺度。稳态分布也不决定时间相关性，后者需要开闭速率。

### 从通道机制回到神经元模型

Hodgkin–Huxley类模型把不同电流的驱动力与门控变量耦合到电容方程；m³h、n⁴是特定模型的门控描述，不等于“恰好有三枚钠通道和四枚钾通道”。钠电流再生反馈、钾电流与失活的恢复过程需要结合动态分析，详见[计算神经科学](../computational-neuroscience/)。[14](#ref-bp-hh)

温度会影响速率、反转电位和材料性质。Q10是描述一定温区速率比的经验量，不能把某个Q10当作所有通道、所有温度和所有物种通用的定律。确定性平均门控也不自动保留有限通道涨落。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/channel-kinetics.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/biophysics/channel-kinetics.svg" alt="固定开闭速率下的开概率松弛，以及两种通道数量下开放比例的二项分布，展示相对涨落差异。 " width="1400" height="550" loading="lazy" /></a><figcaption>图6　平均动力学与分布是不同描述。左图α=100 s⁻¹、β=50 s⁻¹、p初值0.2；右图另取固定p=0.2的独立通道分布，不把左图终值与右图分布混用，也未冒充膜片记录。</figcaption></figure>

## 细胞有空间 电缆近似与几何

### 同一个膜 不能总压成一个电压

长树突或轴突内不同位置可以有不同电位，轴向电流与跨膜电流相互耦合。对半径a的均匀圆柱，轴浆电阻率ρi、单位面积膜电阻RM与比电容CM给出单位长度参数：
$c_m=2\pi aC_M$、$r_i=\rho_i/(\pi a^2)$、$r_m=R_M/(2\pi a)$。

c_m是单位长度电容，单位F/m；r_i是轴向单位长度电阻，单位Ω/m。r_m的单位为Ω·m，长度Δx的一段膜，其跨膜电阻为r_m/Δx，不能把r_m也标成Ω/m。

相应被动电缆模型可写
$\tau_m v_t=\lambda^2v_{xx}-v+r_m i_{\rm inj}$，
其中v=V−EL，v_t与v_xx分别是时间一阶和空间二阶偏导，i_inj为每单位长度注入电流，单位A/m；$\tau_m=R_MC_M$，
$\lambda=\sqrt{aR_M/(2\rho_i)}$。
每项量纲都要一致，不能把整细胞电阻直接当单位长度电阻。[15](#ref-bp-cable)

### 长度常数与时间常数控制不同事情

半无限被动电缆若端点持续钳定v(0)=v0、远处趋零，稳态为 $v(x)=v_0e^{-x/\lambda}$。λ是空间衰减尺度，τ是膜局部响应时间，不应互称“传导速度”。角频率为ω=2πf的边界信号还按 $\exp[-x\sqrt{1+j\omega\tau_m}/\lambda]$ 衰减并移相，这里采用随时间变化为exp(jωt)的复振幅约定，j²=−1。

指定a=1 µm、RM=1 Ω·m²、ρi=1 Ω·m、CM=0.01 F/m²，λ约0.707 mm、τ=10 ms。分支、直径变化、主动通道和髓鞘会改变模型；这些被动结果不等同再生动作电位的传播，也不直接给真实听神经速度。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/cable-filtering.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/biophysics/cable-filtering.svg" alt="半无限被动电缆对稳态和不同频率边界信号的幅度衰减与相位变化，显示长度常数和膜时间常数的不同作用。 " width="1400" height="550" loading="lazy" /></a><figcaption>图7　几何把局部膜变成空间滤波器。使用均匀半无限圆柱、端点电压驱动、λ=0.707 mm与τ=10 ms；不含分支、髓鞘或主动传播机制。</figcaption></figure>

## 细胞力学 黏性与热涨落

### 小尺度运动常受黏性支配

Reynolds数Re=ρUL/η比较惯性和黏性。微小、缓慢的流体运动常处于低Re区，但不能仅凭对象“是细胞”就忽略惯性或弹性。应先看长度、速度、流体和驱动频率。[16](#ref-bp-viscosity)[17](#ref-bp-stokes)

线性弹簧F=kx表示可恢复形变，黏性阻力F=ζẋ依赖速度；Kelvin–Voigt模型把两者并联，$F=kx+\zeta\dot x$。对正弦驱动，复刚度为k+jωζ，幅值与相位随频率改变。真实细胞具有多时间尺度、非线性及主动重塑，单弹簧或单黏壶只在限定范围内有意义。

### 平衡涨落也能测出力学参数

对恒温、被动、谐性一维束缚，Boltzmann分布给出
$\langle x^2\rangle=k_BT/k$，即每个二次自由度的平均储能为kBT/2。该x是相对平衡位置的涨落，不是任意细胞运动轨迹都满足这一关系。[2](#ref-bp-boltzmann)

过阻尼Langevin近似可写
$\zeta\dot x=-kx+F_{\rm ext}+\xi(t)$，
平衡白噪声理想化取 $\langle\xi(t)\xi(t')\rangle=2k_BT\zeta\,\delta(t-t')$。这是相关强度约定，不是说真实瞬时力的方差是一个有限常数；高频惯性、非白噪声与主动过程需另行处理。

### 灵敏度与噪声要一起量化

指定水样流体η=1 mPa·s、被束缚球半径0.5 µm、k=10⁻⁵ N/m、T=310 K，Stokes阻力系数约9.42×10⁻⁹ N·s/m，松弛时间ζ/k约0.942 ms，平衡位置标准差约20.7 nm。恒力0.2 pN的平均位移为20 nm，与涨落尺度相近；这不是听觉阈值的计算。

时间平均可降低某些噪声，但速度、相关时间与测量带宽也会限制信息。活细胞可能远离热平衡，不能从所有自发运动直接反推出k或温度；必须先检验被动平衡假设。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/mechanics-and-noise.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/biophysics/mechanics-and-noise.svg" alt="过阻尼弹性束缚对恒力的平均阶跃响应，及相应热平衡位置分布，比较20纳米位移与涨落尺度。 " width="1400" height="550" loading="lazy" /></a><figcaption>图8　均值响应不是每条微观轨迹。指定被动球、线性弹性与热平衡；左图只画确定性均值，右图为涨落概率密度，未生成某种细胞的实际噪声记录。</figcaption></figure>

## 听觉连接 毛束 势差与外毛细胞

### 毛束位移怎样改变通道开放

毛细胞的毛束机械刺激可以改变转导通道的开放及电导。经典原始实验研究了机械刺激方向、敏感性与电导变化，不能把某一物种或器官的全部参数直接移植到哺乳动物耳蜗。[18](#ref-bp-met-original)

一个现象学教学模型取 $\Delta G(x)=z_g(x_0-x)$，则 $P_o(x)=1/[1+\exp(z_g(x_0-x)/(k_BT))]$。这里zg是有效力，不是离子价数，x0是半开放位移；它把机械功与热能连接起来。指定zg=0.3 pN，310 K下概率转变的位移尺度kBT/zg约14.3 nm。模型不由此识别具体通道蛋白、连接结构或适应机制。

### 为什么毛细胞顶端的钾电流可向内

哺乳动物耳蜗毛细胞顶端面向高K⁺的内淋巴，基底侧则面向不同组成的细胞外环境。内淋巴相对于外淋巴的正电势由血管纹及相关离子输运系统维持，涉及电扩散势与电屏障，不能视为无须代谢的免费电源。[19](#ref-bp-endocochlear)

以外淋巴为0，**教学上指定**内淋巴+80 mV、细胞内−60 mV，则顶端跨膜电压为−140 mV，基底侧为−60 mV。MET通路以阳离子为主，若把其反转相对于内淋巴近似为0，则用外淋巴作统一参考时，有效反转约+80 mV。于是I_MET=g_MET(V−80 mV)为负，表示向内常规电流；这里不能代入普通神经元低外钾的EK来判断方向。[20](#ref-bp-hair-text)

这是不同隔室和电压参考的演示，不是每个物种、部位或年龄毛细胞的通用电压表。真实MET反转还涉及离子选择性、活度与混合通透；也不能因钾流入，就误说耳蜗内外所有细胞的钾都沿同一方向流动。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/hair-cell-references.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/biophysics/hair-cell-references.svg" alt="以外淋巴为零的隔室图显示内淋巴正80毫伏与胞内负60毫伏，顶端和基底侧跨膜电压不同，阳离子电流方向须各自判断。 " width="1400" height="550" loading="lazy" /></a><figcaption>图9　跨膜电位必须先说“跨哪一面”。为参考电位示意，不按真实细胞比例绘制；有效MET反转近似与基底侧钾通路分别标注，箭头不代表无耗能的完整钾循环。</figcaption></figure>

### 受体电位 电动性与能量反馈

指定基底侧gK=20 nS、EK=−80 mV，顶端gMET最大10 nS，暂忽略其他电流，则稳态
$V_\infty=(g_KE_K+g_{\rm MET}E_{\rm MET})/(g_K+g_{\rm MET})$。
图10展示开放概率经电导和驱动力变成渐变受体电位。非线性可来自多个环节，S形位移关系不等于输出电压也是同样的S形。[20](#ref-bp-hair-text)

[内毛细胞](../inner-hair-cell/)的受体电位可影响基底侧Ca²⁺通道与递质释放；成熟听神经动作电位主要由相连神经元形成，不能把受体电位直接叫一次听神经脉冲。[外毛细胞](../outer-hair-cell/)还通过电压依赖的prestin电动性参与机械反馈。原始鉴定与敲除研究支持其关键作用，但具体频率、负载和物种条件不能从一个静态二状态图直接推断。[21](#ref-bp-prestin)[22](#ref-bp-prestin-knockout)

Prestin不是每次伸缩都直接水解一个ATP的通用马达；能量讨论要包括膜电压、电化学梯度、持续代谢与机械负载。耳蜗放大也不是把声波能量凭空变大，详见[基底膜](../basilar-membrane/)与[耳声发射](../otoacoustic-emissions/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/biophysics/transduction-chain.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/biophysics/transduction-chain.svg" alt="指定二状态机械门控的开概率，以及该概率进入两电导膜模型后产生的稳态受体电位，比较两种指定顶端有效反转。 " width="1400" height="550" loading="lazy" /></a><figcaption>图10　机械门控、离子驱动力和受体电位分步计算。T=310 K、有效力0.3 pN、半开放位移10 nm；右图仅改变设定的顶端有效反转0或+80 mV，其余参数人为固定，不是损伤实验或完整耳蜗放大仿真。</figcaption></figure>

## 突触把电信号接到化学与随机释放

### Ca²⁺电流 局部浓度和释放不是同一个量

突触前电压可改变Ca²⁺通道开放，离子进入又经扩散、缓冲、结合和排出塑造局部浓度，释放装置再响应这些局部变化。电流是电荷每时间的通量，浓度是单位体积的物质含量，释放概率是无量纲统计量，三者不能只用一条固定增益互换。[23](#ref-bp-synapse)

一价与二价离子的电荷换算不同；按本文向外电流为正的约定，向内Ca电流 $I_{\rm Ca}<0$ 对应进入速率 $-I_{\rm Ca}/(2F)$，再对时间积分才得到物质的量，并需结合有效体积和反应才能估计浓度变化。这里的换算直接来自电荷守恒。所谓Ca微域或纳米域强调空间与时间的局部性，不由一个整体平均Ca值自动确定全部释放位点行为。

### 带状突触为何需要观测模型

毛细胞带状突触可以连续调节释放，原始电生理工作从与内毛细胞接触的传入末梢记录突触后电流，说明测量对象与细胞内Ca电流不同；其分布和时序需要相应释放模型解释。[24](#ref-bp-ribbon)

膜电容变化可帮助研究膜面积相关过程，但它不是每个囊泡内容物或释放位点的直接计数器；突触后电流还受受体、驱动力和记录滤波影响。预测一个平均电流，并不等于已经解释囊泡随机性、听神经脉冲或言语行为。

### 与计算神经科学怎样配合阅读

学习电容与通道后，可回到《计算神经科学》的被动膜、Hodgkin–Huxley、突触和隔室部分，再进入脉冲统计与编码。本篇提供机制约束，配套篇提供状态方程、统计模型和验证方法。物理上可行只是第一层；神经编码是否成立，还需要数据与区分竞争模型的实验。

## 怎样测量与检验生物物理模型

### 电压钳和电流钳控制不同变量

理想电压钳控制膜电位、观察所需电流；电流钳控制注入电流、观察电压。真实记录有串联电阻、寄生电容、液接电位和带宽限制。例如按指定电流方向估计的电压误差量级为|I|Rs，不能只因软件给出指令电压就认定细胞膜瞬时处处达到它。

模型还应说明测的是整细胞、单位面积、单通道还是细胞外信号。电流除以膜面积得到密度，但面积估计本身有误差；不同温度、离子溶液或细胞状态下的参数也不能不经转换混用。[14](#ref-bp-hh)

### 验证先检查守恒 单位与可识别性

可先用单位、质量/电荷守恒、极限情况和独立解法检查实现。例如V=E时相应欧姆支路净电流应为零，p必须在[0,1]，扩散核总概率应为1，热平衡弹性方差应与kBT/k相符。数值步长过大可以让概率越界或改变时间常数。

同一宏观曲线也可能由不同机制产生：只量稳态占比难以分别识别k_on与k_off；只量电压时间常数难以单独确定C和g；多种通道组合可能给出接近的总电流。需要多种刺激、独立测量和干预，而不是仅提高曲线拟合的精度。

### 从机制参数到听觉表现还有层次

模型可以在一个层次上正确而在另一个层次上不充分。膜参数正确不代表完整细胞几何正确，细胞响应相似不代表群体编码相同，神经响应改善也不自动等于听者表现改善。对分子结构、力学、细胞、神经和行为，分别说明输入、状态、输出与证据，是两篇配套课程共同的核验原则。

## 可复算的例子与学习自检

### 用化学势核对Nernst符号

下例按本文温度和浓度计算，活度比以理想浓度比近似。只需NumPy；公式中电压单位为V。

```python
import numpy as np
kB, NA, e = 1.380649e-23, 6.02214076e23, 1.602176634e-19
R, F, T = NA*kB, NA*e, 310.
for name, z, cin, cout in [("K", 1, 140., 5.),
                           ("Na", 1, 12., 145.),
                           ("Cl", -1, 10., 120.)]:
    E = R*T/(z*F)*np.log(cout/cin)
    residual = R*T*np.log(cin/cout)+z*F*E
    print(name, E*1000, "mV", residual, "J/mol")
    assert abs(residual) < 1e-8
```

负价数必须参与计算；不要先把Cl当阳离子算，再凭印象补符号。这个检查核对电化学势相等，并不证明所列浓度是某个细胞的实测值。

### 同一结合常数 不同动力学

下例让k_on与k_off同时按比例缩放，以独立ODE积分核对解析时间过程；浓度使用mol/L，时间使用s。

```python
import numpy as np
from scipy.integrate import solve_ivp
c, t = 2e-6, np.linspace(0, 2, 301)
for scale in [.2, 1., 5.]:
    kon, koff = scale*1e6, scale*1.
    eq, tau = kon*c/(kon*c+koff), 1/(kon*c+koff)
    sol = solve_ivp(lambda tt, y: [kon*c*(1-y[0])-koff*y[0]],
                    [0, t[-1]], [0.], t_eval=t, rtol=1e-9, atol=1e-11)
    exact = eq*(1-np.exp(-t/tau))
    print(koff/kon, tau)
    assert sol.success and np.max(abs(sol.y[0]-exact)) < 1e-7
```

### 电流守恒与被动膜

此例把漏电、电容和注入电流对照。电压、电导、电容、电流分别用V、S、F、A，不额外加入阈值和复位。

```python
import numpy as np
from scipy.integrate import solve_ivp
C, g, EL, I = 10e-12, 1e-9, -.070, 20e-12
tau, final = C/g, EL+I/g
t = np.linspace(0, .05, 501)
sol = solve_ivp(lambda tt, v: [(-g*(v[0]-EL)+I)/C],
                [0, t[-1]], [EL], t_eval=t, rtol=1e-10, atol=1e-12)
exact = final+(EL-final)*np.exp(-t/tau)
leak = g*(exact-EL)
capacitive = I*np.exp(-t/tau)
print(tau, final, np.max(abs(sol.y[0]-exact)))
assert sol.success and np.max(abs(sol.y[0]-exact)) < 1e-8
assert np.allclose(leak+capacitive, I, atol=1e-22, rtol=1e-10)
```

[完整实验脚本](/n3-hearingpedia/code/biophysics/experiments.py)另含扩散尺度、GHK、门控、通道分布、电缆与力学计算。它验证指定模型的实现，不能代替生理实验或一般机制证明。

### 六个问题检查理解

1. 为什么kBT与RT不能直接比较数值？二状态Boltzmann式使用能量还是有效自由能取决于哪些假设？
2. 为什么扩散的L²/D时间尺度不是一条确定的运动速度，也不自动等于首次到达时间？
3. Nernst电位、混合通道反转、GHK零电流电位和细胞静息电位分别回答什么问题？
4. 为什么形成膜电压只需少量电荷分离，却仍需要持续代谢维持长期离子梯度？
5. 相同Kd或相同时间常数，为何不足以唯一识别结合速率或膜参数？
6. 为什么毛细胞顶端与普通神经元可有不同的钾驱动力方向？电压参考和外部溶液各起什么作用？

建议先读热能、扩散和电化学，再读膜、通道与电缆；随后把力学和毛细胞实例与《计算神经科学》的膜与突触模型对照。阅读研究论文时，依次确认量、单位、参考、储库、几何、状态、耗能与观测，能把“看起来像机制”的曲线转成可检查的物理关系。

本篇来源核对日期为2026年11月2日。教材、作者课程与原始论文分别标记核验范围，原始摘要不冒充全文；未开展穷尽式生物物理文献综述。数学、图示和代码经过检查，仍保留待专业审阅状态。
