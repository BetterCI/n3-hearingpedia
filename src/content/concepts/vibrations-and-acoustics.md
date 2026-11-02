---
title: "振动与声学基础"
english: "Fundamentals of Vibrations and Acoustics"
slug: "vibrations-and-acoustics"
summary: "从质量、弹性与阻尼进入自由振动、受迫共振和多自由度模态，再建立质点运动、线性声波、声压、声强、阻抗与分贝的联系；以行波、驻波、反射、球面近场、管道和Helmholtz共振器说明边界、能流、单位及测量链的适用条件。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "机械振动", "共振", "模态", "线性声学", "声阻抗", "声强", "分贝"]
aliases: ["振动与声学", "声学基础课程", "振动学基础", "Vibrations and Acoustics", "Fundamentals of Acoustics"]
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
  - {label: "课程定位", value: "连接机械振动与空气声学，建立变量、单位、能量、模态和边界的共同框架"}
  - {label: "核心区分", value: "固有频率与响应峰、声压与净声强、局部阻抗与介质特性阻抗分别判断"}
  - {label: "研究连接", value: "声源与换能器、听觉输入、管腔共振、室内声场及响应测量"}
  - {label: "适用边界", value: "主要讨论小振幅、线性、无平均流模型；图与数值不是实际设备或听者测量"}
references: ["va-free", "va-forced", "va-modal", "va-measurement", "va-lumped", "va-tubes", "va-plane", "va-spherical", "va-wave-equation", "va-intensity", "va-compliance", "va-decibels", "va-pipes", "va-helmholtz", "va-ir", "va-eigh", "va-ivp", "va-diffraction"]
order: 1023
---

**振动**是系统状态在某种平衡附近或一定范围内随时间往复变化；**声学**研究机械扰动的产生、传播、相互作用与接收。两者通过介质或结构的惯性、弹性、耗散和边界联系起来，但“物体正在振动”“向外辐射多少声音”和“听起来多响”是不同问题。[1](#ref-va-free)[7](#ref-va-plane)

本篇以小振幅机械振动和静止流体中的线性声学为主，衔接[微分方程与动力系统](../differential-equations-and-dynamical-systems/)、[信号与系统](../signals-and-systems/)与具体声学词条。它提供一条从受力与能量到声波与测量的课程主线；更完整的传播问题可读[声波与传播](../sound-waves-and-propagation/)，声场边值问题可读[波动方程](../wave-equation/)和[亥姆霍兹方程](../helmholtz-equation/)。

十幅图、三个短程序及[完整实验脚本](/n3-hearingpedia/code/vibrations-and-acoustics/experiments.py)均为原创理想模型的复算。采用明确的SI单位或标注归一化量，不是器件、房间或听者实测。文中的声压与声强是物理输入，不能直接换成个体听阈、响度或言语理解结果。

## 阅读准备与独立阅读

**起步知识。** 能区分位移、速度、力与时间，知道正弦表示周期变化，即可先读图和物理解释。导数是局部变化率，积分是累积；后文会重新解释复相量、均方根、矩阵与模态，不要求先完整修完数学或电路课程。

**随用随补。** 频率f的单位为Hz，角频率ω=2πf的单位为rad/s；周期T=1/f。向量是一组数，矩阵把多个量按线性关系连接。复数在本篇用于保存单频幅度与相位，物理可观察量取其规定的实部。

**分层阅读。** 第一遍读振动、波、边界和能量图；第二遍复算共振、阻抗、分贝和管道频率；第三遍再读模态、复声强与测量链。需要更多推导时按点参照[微积分](../calculus/)、[线性代数](../linear-algebra/)、[电路原理](../circuit-theory/)和[数值分析](../numerical-analysis/)。

## 先分清变量 单位和模型范围

| 量 | 本篇符号与单位 | 含义 |
| --- | --- | --- |
| 结构位移、速度 | q：m；v=q̇：m/s | 固体或集总结构的运动 |
| 力、刚度、阻尼 | F：N；kₛ：N/m；b：N·s/m | 恢复力与黏性阻力的模型参数 |
| 声压 | p：Pa | 相对背景静压的扰动，不是绝对气压 |
| 质点速度、位移 | u：m/s；ξ：m | 连续介质小单元的局部运动，不是声速 |
| 体积速度 | Qᵥ：m³/s | 穿过指定截面的声学体积流率 |
| 声强、声功率 | I：W/m²；W：W | 能流密度与穿过表面的总能量速率 |

点号表示对实际时间t求导。机械刚度用kₛ，声学波数另用k=ω/c，避免把两种不同的量混为一谈。空气教学例统一取ρ₀=1.2 kg/m³、c=343 m/s，故ρ₀c=411.6 Pa·s/m；这是指定近似参数，不是所有温湿度、气体组成与频率下的精确常数。[9](#ref-va-wave-equation)[10](#ref-va-intensity)

“线性”主要意味着在选定平衡和小扰动范围内，方程与边界可线性近似；并非真实介质在任意振幅下都服从叠加。本文忽略平均流、冲击波、强非线性以及多数黏热细节，涉及损耗时明确写出简化参数。

## 单自由度振动 质量 弹性与阻尼

### 一个状态坐标怎样承载动力学

单自由度模型用一个独立位移q描述结构；二阶运动方程仍需位移和速度两个初始数据。质量m>0、刚度kₛ>0、黏性阻尼b≥0时

$$
m\ddot q+b\dot q+k_s q=F(t).
$$

惯性项m q̈、阻尼项b q̇和弹性项kₛq都具有力的单位。线性弹簧恢复力与位移相反，阻尼力与速度相反；方程把这两项移到左边后写成正号。实际结构的有效参数依赖模型选取，不能把同一个m、b、kₛ不加说明地跨频段或跨振幅使用。[1](#ref-va-free)

无阻尼、无外力时的自然角频率ωₙ=√(kₛ/m)，自然频率fₙ=ωₙ/(2π)。加上黏性阻尼，定义阻尼比ζ=b/(2√(mkₛ))：0≤ζ<1为欠阻尼，ζ=1为临界阻尼，ζ>1为过阻尼。欠阻尼自由响应的振荡角频率为ω_d=ωₙ√(1−ζ²)，不等于有驱动时某个响应量的峰值频率。

### 用能量看衰减

无外力时，动能与弹性势能之和满足

$$
\begin{aligned}
E&=\tfrac12m\dot q^2+\tfrac12 k_s q^2,\\
\dot E&=-b\dot q^2\leq0.
\end{aligned}
$$

能量不增不意味着位移每时每刻都单调减小；欠阻尼位移可以过零并往复，而总能量衰减。临界与过阻尼通常不呈相同的往复形态，但“临界最快”也应限定为所选初态、输出和评价准则，不能泛称所有任务中的唯一最优阻尼。

图1取m=0.02 kg、kₛ=80 N/m，故fₙ≈10.0658 Hz，初始位移1 mm、初速0；改变ζ时分别重新设置b。它是结构振动例子，不把10 Hz直接解释为一个典型听觉通道。[1](#ref-va-free)[17](#ref-va-ivp)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/free-vibration-energy.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/free-vibration-energy.svg" alt="四种阻尼比的自由位移及相同模型的动能与势能之和" width="1400" height="550" loading="lazy" /></a><figcaption>图1　ζ为0.05、0.3、1和1.5，四条曲线质量、刚度及初态相同；阻尼b随ζ改变。左侧位移可往复，右侧总能量不增。单位分别mm与μJ，不是扬声器振膜或听者测量。</figcaption></figure>

## 受迫振动 共振峰必须说明观察量

### 瞬态 稳态与复相量

对瞬态能够衰减的稳定线性系统，响应可分成初态引起的瞬态与驱动对应的特解。正弦稳态在瞬态充分衰减后才适用；短时开启后的波形不能自动等同稳态幅频公式。[2](#ref-va-forced)

本文统一采用e^(iωt)及**峰值复相量**：F(t)=Re{F̂e^(iωt)}、q(t)=Re{Q̂e^(iωt)}。则

$$
\begin{aligned}
H_q(\omega)&=\frac{\widehat Q}{\widehat F}
=\frac1{k_s-m\omega^2+i\omega b},\\
\widehat V&=i\omega\widehat Q,\qquad
\widehat A=-\omega^2\widehat Q.
\end{aligned}
$$

位移/力传递函数单位为m/N，速度/力为m/(N·s)，二者频率响应不同。若改用RMS相量，后文平均功率公式中的1/2也要相应调整；不能只换名称而保留所有系数不变。

### 位移峰 速度峰与Q

固定驱动力幅度、b>0的黏性阻尼模型下，非零位移幅值峰位于ωₙ√(1−2ζ²)，要求0<ζ<1/√2；阻尼更大时没有这样的非零位移峰。速度幅值与阻尼耗散功率的峰却在ωₙ。一个“共振频率”若不注明输入与输出，可能指不同的数。[2](#ref-va-forced)

对这个模型定义Q=mωₙ/b=1/(2ζ)。固定力幅度时，速度响应的两个半功率角频率精确为

$$
\begin{aligned}
\omega_\pm&=\omega_n\bigl(\sqrt{1+\zeta^2}\pm\zeta\bigr),\\
\Delta\omega&=\omega_+-\omega_-=2\zeta\omega_n.
\end{aligned}
$$

因而ωₙ/Δω=Q。若改用**位移峰附近**的半功率带宽，常见同样形式通常是轻阻尼近似，不能把精确速度结果不加说明地套过去。不同损耗机制、输入方式和多模态叠加也会改变带宽解释。

机械阻抗取力/速度：Zₘ=b+i(ωm−kₛ/ω)，不是力/位移。单频平均输入功率为Re{F̂V̂*}/2，稳态时等于b v_rms²。高Q可使某些稳态响应集中于窄频带，同时伴随较长建立和衰减时间，不能只比较峰值而忽略暂态。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/resonance-response.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/resonance-response.svg" alt="不同阻尼比的位移幅频响应与位移相对驱动力的相位滞后" width="1400" height="550" loading="lazy" /></a><figcaption>图2　输入力峰值固定；位移按静态幅度F₀/kₛ归一，ζ为0.05、0.2和0.8。竖虚线为ω=ωₙ，不是对所有曲线峰位置的标记；速度半功率带宽的定义另在正文给出。</figcaption></figure>

## 多自由度 模态与激励测点

### 广义特征值问题

多个独立位移组成向量q，线性结构可写M q̈+C q̇+Kq=F。对实对称正定质量矩阵M和实对称刚度K，无阻尼模态满足Kφᵣ=ωᵣ²Mφᵣ；这里M与K具有不同单位，不是简单把K的特征值开平方。[3](#ref-va-modal)[16](#ref-va-eigh)

采用质量归一化可令φᵣᵀMφₛ=δᵣₛ，再把q展开为模态形状的组合。模态形状主要描述各位置的相对运动，其整体正负号与缩放约定可变，不能把图中形状幅度当作实际受迫位移。

图3选择

$$
\begin{aligned}
M&=\operatorname{diag}(0.02,0.03)\ \mathrm{kg},\\
K&=\begin{bmatrix}140&-60\\-60&180\end{bmatrix}
\ \mathrm{N/m}.
\end{aligned}
$$

其无阻尼固有频率约10.0658与15.0988 Hz，一阶形状同向，二阶反向。加比例阻尼C=αM+βK，取α=1 s⁻¹、β=0.0005 s，模态阻尼也可同时对角化；一般非比例阻尼下不能照此逐模态完全解耦。

### 模态存在不等于每个测点都看到峰

图3仅在质量1施力，同时观察两个位移。响应既受模态频率与阻尼影响，也受激励投影和测量位置影响；某模态若未被有效激发或测点靠近其节点，峰可能不明显。多个模态相消还可形成反共振，不能把每个峰谷都一一等同一个独立模态。

完整脚本分别用动态刚度矩阵直接求解与质量归一的模态叠加核对。这个相等性依赖选定线性模型及比例阻尼，不是对任意实测多峰频谱的自动分解保证。[3](#ref-va-modal)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/coupled-modes.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/coupled-modes.svg" alt="两质量系统的相对模态形状及驱动质量1时的两个位移响应" width="1400" height="550" loading="lazy" /></a><figcaption>图3　左图各模态按自身最大绝对值归一，未保持图形的质量归一幅度；实际计算使用质量归一模态。右图为位移/力频响，C=αM+βK，α与β含正文所列单位。测点与激励影响峰谷。</figcaption></figure>

## 结构振动怎样连接到声波

结构运动通过与介质的边界交换力和功率，但结构位移或加速度并不唯一决定远处声压。还需几何尺寸、运动分布、频率、辐射负载、指向性和接收位置。局部振动很强不自动等于向外辐射功率很大。[8](#ref-va-spherical)

一个简化端口类比是：均匀速度v的活塞，面积S，法向体积速度Qᵥ=Sv；若作用在该端口的压力差可用均匀p表示，则F=Sp，于是机械负载阻抗Zₘ=F/v=S²Zₐ，其中Zₐ=p/Qᵥ为声学端口阻抗。面积平方不能漏掉；实际表面不均匀时需积分，不能把任意一点压力直接乘总面积。[5](#ref-va-lumped)

平均机械功率与平均声学端口功率在此理想耦合约定下相符：Re{F̂V̂*}/2=Re{P̂Q̂ᵥ*}/2。负载含反应性时还有往复储能，不能把总阻抗模值直接当作消耗功率。可配合[电声换能器](../electroacoustic-transducer/)和[生物物理学](../biophysics/)进一步阅读。

## 线性声波 从压力与质点运动到传播

### 两条一阶关系与波方程

对均匀、静止、无黏无热损的流体，小扰动线性近似给出

$$
\begin{aligned}
\rho_0\frac{\partial\mathbf u}{\partial t}&=-\nabla p,\\
\frac{\partial p}{\partial t}&=-\rho_0c^2\nabla\cdot\mathbf u,\\
\frac{\partial^2p}{\partial t^2}&=c^2\nabla^2p.
\end{aligned}
$$

第一式来自动量守恒，第二式结合连续性与小扰动状态关系，第三式为声压波方程。声速满足c²=Bₛ/ρ₀，Bₛ为相应绝热体积模量。质点速度是局部介质单元的运动速度，c是扰动传播速度；两者单位相同，含义不同。[9](#ref-va-wave-equation)[7](#ref-va-plane)

空气声主要是纵向扰动，固体还可能支持剪切等其他波型；不应把流体声压方程当成任意结构弹性波的完整模型。边界、初值与声源条件也必须给出，单独写波方程并不能唯一决定声场。

### 行波的时间与空间尺度

沿+x传播的单频平面波可写p(x,t)=p̂cos(ωt−kx+φ)，其中k=ω/c、λ=2π/k=c/f。时间曲线里的周期不是空间波长。流体质点主要在平衡附近往复，不会随每个波峰一路前进到接收者。[7](#ref-va-plane)

图4取f=500 Hz、p_rms=1 Pa，则λ=0.686 m、u_rms≈2.42954 mm/s、ξ_rms≈0.77335 μm。图中可见的局部位移与波峰前进0.1715 m是不同尺度；绘图选择μm不表示可以从普通未校准录音直接测得这项位移。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/wave-particle-motion.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/wave-particle-motion.svg" alt="500赫兹行波的空间声压及固定位置介质质点的微米级位移" width="1400" height="550" loading="lazy" /></a><figcaption>图4　左图两时刻相差0.5 ms，波峰前进0.1715 m；右图质点只局部往复。空气参数ρ₀=1.2 kg/m³、c=343 m/s，单向平面波p_rms=1 Pa，所有量由同一模型计算，不夸大位移数值。</figcaption></figure>

## 声压 声强与阻抗 不要省略相位

### RMS与峰值相量

零均值周期声压的均方根p_rms为一个完整周期内p²平均后开平方；有限记录也可在明确的时间窗内定义。单一正弦的p_rms=p̂/√2，而一般复合波或瞬态不具有固定的峰值/RMS比。[4](#ref-va-measurement)

本文单频声压p=Re{P̂e^(iωt)}、沿指定方向的速度u=Re{Ûe^(iωt)}，P̂和Û均为峰值相量。平均有功声强为

$$
\begin{aligned}
\overline I&=\langle pu\rangle
=\tfrac12\operatorname{Re}(\widehat P\widehat U^*),\\
\overline I&=p_{\rm rms}u_{\rm rms}\cos\phi.
\end{aligned}
$$

φ为压力与速度的相位差；三维声强是向量，声功率是声强在给定表面上的法向积分。净通量的方向不能通过对负值随意取绝对值而隐藏。复声强的虚部可表征相位相关的反应性能流，但其单位是W/m²，不等于储能密度J/m³。[10](#ref-va-intensity)

### 三种阻抗的分母不同

| 定义 | 本篇形式 | 单位 |
| --- | --- | --- |
| 机械阻抗 | Zₘ=力相量/速度相量 | N·s/m |
| 比声阻抗 | zₛ=声压相量/法向质点速度相量 | Pa·s/m |
| 声学端口阻抗 | Zₐ=声压相量/体积速度相量 | Pa·s/m³ |

在截面S上速度均匀时Zₐ=zₛ/S；节点处分母为零时，相应比值可能发散或失去定义。局部比声阻抗可随位置、频率和波的叠加而变化；只有在相应单向无损平面行波条件下，zₛ等于实数特性比声阻抗z₀=ρ₀c，并有I=p_rms²/(ρ₀c)。逆向平面波若仍用固定+x速度分量，则压力/速度带相反符号，应保留方向约定。[7](#ref-va-plane)[11](#ref-va-compliance)

线性声学的瞬时能量密度为p²/(2ρ₀c²)+ρ₀|u|²/2；它与能流不是同一物理量。介质可以暂时储能并往返交换，而没有同样大小的平均净传播功率。

## 驻波与反射 有声压不等于有向外的净能流

### 双向平面波怎样叠加

设正向峰值相量幅度为A，反射压力系数为R，则

$$
\begin{aligned}
\widehat P(x)&=A(e^{-ikx}+Re^{ikx}),\\
\widehat U(x)&=\frac A{\rho_0c}(e^{-ikx}-Re^{ikx}).
\end{aligned}
$$

R=1形成理想驻波：压力节点与速度节点错开，压力和速度在时间上正交，平均净声强为0；瞬时能量交换和储能仍可存在。不能把压力腹的高RMS声压直接换成同样大的外向净声强。[7](#ref-va-plane)[10](#ref-va-intensity)

一般反射下，净平均声强为|A|²(1−|R|²)/(2ρ₀c)，而局部声压平方随位置起伏。图5右侧取R=0.6，真实净通量恒定，但把p_rms²/(ρ₀c)硬套为声强会得到随位置变化的错误结果。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/standing-wave-intensity.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/standing-wave-intensity.svg" alt="完全反射时的压力与速度驻波，以及部分反射时净声强和错误声压换算的对比" width="1400" height="550" loading="lazy" /></a><figcaption>图5　左图R=1，ρ₀c乘速度RMS仅用于换成压力等效尺度；净声强为0。右图另取R=0.6，入射p_rms=1 Pa，实际净通量为入射的0.64倍。两面板条件不同，均为无损一维模型。</figcaption></figure>

### 界面压力幅度与能量比例

两侧为实正比声阻抗z₁、z₂的无损流体、平面波法向入射、界面面积相同且无额外能量源时，压力与法向速度连续给出

$$
\begin{aligned}
r_p&=\frac{z_2-z_1}{z_2+z_1},\qquad
t_p=\frac{2z_2}{z_2+z_1},\\
\mathcal R&=|r_p|^2,\\
\mathcal T&=\frac{z_1}{z_2}|t_p|^2,\\
\mathcal R+\mathcal T&=1.
\end{aligned}
$$

rₚ为反射/入射压力幅度比，tₚ为透射/入射压力幅度比。透射压力幅度可以大于1，但透射能流比仍不超过1。z₂=3z₁时rₚ=0.5、tₚ=1.5，而能流反射0.25、透射0.75，能量没有凭空增加。[7](#ref-va-plane)[10](#ref-va-intensity)

理想刚壁极限rₚ→1，理想压力释放边界rₚ→−1；负号代表压力相位反转，不是负能量。若有损耗、斜入射、固体波型转换或可运动边界，则需扩展模型。反射少也不等于吸收多：上例无损阻抗匹配时能量全部透射，真正耗散为0；只有不透射的适当单端口边界才可把1−|rₚ|²直接解释为吸收比例。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/reflection-transmission.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/reflection-transmission.svg" alt="比声阻抗比变化下的压力反射透射系数和能流比例" width="1400" height="550" loading="lazy" /></a><figcaption>图6　两无损流体、法向入射、界面面积一致。左图tₚ可超过1，右图反射与透射能流之和恒为1；图不包含壁内耗散、固体剪切波或斜入射效应。</figcaption></figure>

## 声级与叠加 为什么两个70 dB会有不同结果

### 参考量决定分贝的含义

空气声压级通常写为Lₚ=20log₁₀(p_rms/p_ref)，p_ref=20 μPa；等价地是均方声压比的10log₁₀。它是有参考量的比值表示，0 dB不表示声压为0，也不是每个人在所有频率上的听阈。[12](#ref-va-decibels)

对规定的正声强标量，可用Lᵢ=10log₁₀(I/I_ref)，常见I_ref=10⁻¹² W/m²。指定ρ₀c=411.6时，1 Pa RMS平面行波的Lₚ≈93.9794 dB，而Lᵢ≈93.8552 dB；它们接近但不完全相等。复杂反射声场中，净声强甚至可能为0而声压级有限，更不能普遍认定两种级相同。

参考量、频率计权、时间平均、带宽与测点都应报告。dB SPL不能直接替代声压谱密度、dBFS、听力级或响度；数字满刻度值也不能未经测量链校准就换算为Pa。不同介质或专业约定可能使用不同参考声压，比较前必须核对。[4](#ref-va-measurement)[12](#ref-va-decibels)

### 先加压力 再算均方值

同一点p=p₁+p₂，有⟨p²⟩=⟨p₁²⟩+⟨p₂²⟩+2⟨p₁p₂⟩。最后的相关交叉项不能一律删除。两路同参考、同时间窗、各70 dB的声压若不相关，总级约73.0103 dB；若是等幅同频且同相，总级约76.0206 dB；理想完全反相可在指定点相消。[12](#ref-va-decibels)

等幅同频相差φ时，相对一路的声压级变化为20log₁₀(2|cos(φ/2)|)，φ=π处数学极限为−∞。这不表示整个空间的声能消失；声场的空间干涉和声源实际负载要一起考虑。图7的显示下限也不是实际测量噪声底。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/decibels-correlation.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/decibels-correlation.svg" alt="同频声压相位差决定的声级变化，以及单路、不相关双路和同相双路的声压级" width="1400" height="550" loading="lazy" /></a><figcaption>图7　左图显示下限−40 dB，理想φ=π处应为−∞；右图各路单独70 dB，同一测点和参考。73.010与76.021 dB对应不同相关条件，不是把70直接相加，也不是对所有双声源的固定规则。</figcaption></figure>

## 几何扩散与近远场 先说明声源模型

### 逆距离规律不适用于任意房间

理想各向同性点声源、固定辐射功率、均匀无损自由场中，球面面积为4πr²，平均径向声强按1/r²衰减，声压幅度按1/r衰减。距离翻倍对应声压级约降低6.0206 dB。反射、空气吸收、遮挡、指向性变化与有限声源尺寸都会改变实际测量。[8](#ref-va-spherical)

理想平面行波可无几何扩散，理想柱面扩散又有不同距离关系；不能同时用恒幅平面波模型和球面扩散规律描述同一段传播。绕射也取决于波长与障碍、开口尺寸，不能只凭“高频”或“低频”不带几何尺度就给出遮挡量。[18](#ref-va-diffraction)

### 纯外向球面波的一个重要特例

在本篇e^(iωt)约定下，单极球面对称外向波为

$$
\begin{aligned}
\widehat P(r)&=A e^{-ikr}/r,\\
\widehat U_r(r)&=\frac{\widehat P}{\rho_0c}
\left(1+\frac1{ikr}\right),\\
z_s(r)&=\frac{\rho_0c}{1+1/(ikr)}.
\end{aligned}
$$

kr小的时候压力与速度不再同相，局部比声阻抗具有明显反应性；kr≫1时才接近平面行波的实阻抗。不过，对**这一纯外向球面模型**，把上式代入Re{P̂Ûᵣ*}/2仍精确得到I=p_rms²/(ρ₀c)。因此“任何近场都不能有这个能流关系”同样过度；应按完整场解核对，而不是只贴近场标签。[8](#ref-va-spherical)

这一kr判据属于点式球面模型，不是所有扬声器、孔径或阵列的统一远场距离。大孔径的方向图建立还涉及孔径尺寸与波长，例如D²/λ量级的传播尺度；常数与采用的远场误差准则有关。此处不以一个数替代真实声源几何分析。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/spherical-near-field.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/spherical-near-field.svg" alt="纯外向球面波的逆距离声压级及局部比声阻抗的实虚部" width="1400" height="550" loading="lazy" /></a><figcaption>图8　左图指定1 m处1 Pa RMS，500 Hz，距离翻倍−6.021 dB；右图采用同一e^(iωt)约定，kr小呈反应性。该外向单极模型的净声强仍等于p_rms²/(ρ₀c)，不能推广到任意反射近场。</figcaption></figure>

## 管道与边界 模态频率从哪里来

### 压力节点与速度节点不是同一个条件

理想刚性闭端要求法向速度为0，对一维声压对应空间导数为0；理想开口先近似为压力扰动为0。前者常是压力腹，后者是压力节点。若换成位移或速度图，节点与腹的位置需要相应转换，不能把压力图直接当空气位移图。[6](#ref-va-tubes)[13](#ref-va-pipes)

均匀管长L、平面波、无损理想边界下：开—开管压力形状为sin(nπx/L)，频率fₙ=nc/(2L)；闭—开管若左闭右开，形状为cos((2n−1)πx/(2L))，频率fₙ=(2n−1)c/(4L)，n=1,2,…。L=0.5 m时第一频率分别343和171.5 Hz。

真实开口会向外辐射，压力释放边界只是近似。端修正、黏热损耗、非均匀截面、侧孔与高阶横向模态会改变频率和阻尼；图9的理想谐波序列不能直接当真实乐器或耳道的完整共振谱。[13](#ref-va-pipes)

### 输入阻抗连接行波和集总模型

以管入口朝管内的体积速度为正，截面积S、特性声学阻抗Z₀=ρ₀c/S，理想终端给出

$$
\begin{aligned}
Z_{\rm in,rigid}&=-i Z_0\cot(kL),\\
Z_{\rm in,open}&=i Z_0\tan(kL).
\end{aligned}
$$

低频kL≪1时，刚端管接近容积顺性，开端管接近流体惯抗；这个结论来自上述分布模型的小参数展开。公式要求均匀一维管、所写端点与无损假设，不能把输入阻抗的峰谷忽略激励条件直接叫作任意系统的全部固有模态。[6](#ref-va-tubes)[11](#ref-va-compliance)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/pipe-boundaries.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/pipe-boundaries.svg" alt="半米长理想开开管与闭开管的前三个压力模态形状" width="1400" height="550" loading="lazy" /></a><figcaption>图9　左图两端压力节点，频率343、686、1029 Hz；右图左闭右开，频率171.5、514.5、857.5 Hz。各形状归一化，未画真实位移、端修正、辐射损耗或横向高阶模态。</figcaption></figure>

## Helmholtz共振器 集总惯性与顺性

当波长远大于腔体及颈部的相关尺度，可把腔内压力近似为均匀，把颈部运动近似成一团空气。体积V、颈面积S、有效颈长L_eff给出声学惯抗参数Mₐ=ρ₀L_eff/S和顺性Cₐ=V/(ρ₀c²)。两者单位分别为kg/m⁴、m³/Pa，不是结构质量kg与弹簧顺性m/N。[5](#ref-va-lumped)[14](#ref-va-helmholtz)

以体积速度为端口流变量，简化串联模型为

$$
\begin{aligned}
Z_a(\omega)&=R_a+i\omega M_a+\frac1{i\omega C_a},\\
f_H&=\frac1{2\pi\sqrt{M_aC_a}}\\
&=\frac c{2\pi}\sqrt{\frac S{V L_{\rm eff}}}.
\end{aligned}
$$

这里Rₐ概括指定频段内的损耗，实际可随频率改变；有效颈长包含颈两端附加运动空气的影响，不必等于几何颈长。共振频率公式是简化无损反应项抵消的位置，真实响应峰仍受驱动、损耗与辐射影响。[11](#ref-va-compliance)

取V=1 L、颈半径1 cm、L_eff=4 cm，得到f_H约153.0 Hz。这个计算并未从真实瓶口几何推导端修正，也未预测峰值幅度或吸声率。无损惯性与顺性只储存、交换能量；要让共振器持续耗能并形成具体吸声效果，还需实际损耗和边界匹配。[14](#ref-va-helmholtz)

## 从模型到测量 频谱峰谷可能来自哪里

一次记录混合了声源、传播与接收链。只有在适当近似线性时不变、固定负载及级联条件下，才可把测量传递函数看成这些环节响应的乘积；声源会受声负载反馈时，过分简单的分割也会失效。应先说明输入是力、电压、体积速度还是声压，输出在哪个位置、用什么单位。[4](#ref-va-measurement)

图10选择一个纯数字两路径模型：48 kHz采样，第0点脉冲权重1，第192点权重0.6，对应4 ms延迟。其频响H(f)=1+0.6e^(−i2πf·0.004)，峰谷间距250 Hz，相对直达支路的最大增益约4.0824 dB、最小约−7.9588 dB。这些峰谷仅由两路径干涉产生，不需要结构本身具有同样一串振动模态。

真实路径还会有频率相关反射、吸收与指向性。脉冲响应中的峰值时间也可能受到设备滤波和带宽影响，不能把全部系统延迟都当声传播时间。截短时窗可以减少某些反射，但会改变低频与频率分辨能力；普通DFT频率网格Δf=1/T不意味着所有相距1/T的谱成分都能可靠分离，补零只加密显示网格。[15](#ref-va-ir)

测量至少应把校准、采样率、时间参考、窗长、背景噪声、激励幅度和重复性与结果一起记录；“RMS声压”“平均净声强”“输入阻抗”和“频响幅值”需要不同测量条件。这里的理想公式帮助设计与检查解释，不自动替代实际的传声器、探头或结构模型校准。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/vibrations-and-acoustics/measurement-paths.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/vibrations-and-acoustics/measurement-paths.svg" alt="两抽头数字脉冲响应及其周期性干涉峰谷" width="1400" height="550" loading="lazy" /></a><figcaption>图10　采样率48 kHz、延迟192点、两权重1和0.6。左图是离散脉冲权重，不是连续Dirac函数的有限高度或校准声压；右图只计算指定模型，未运行房间测量或REW。</figcaption></figure>

## 三个可以独立运行的小实验

程序使用Python、NumPy与SciPy，已在Python 3.11、NumPy 1.26.4、SciPy 1.17.1运行。完整脚本还包含自由响应、能量、阻抗、声级与两路径绘图所需模型。数值核对与物理假设分别保留，不把一次求解成功当作模型已经符合真实设备。

### 一 两质量的模态与质量归一化

先解广义特征值问题，再检查残差和M正交；不要只把K送入普通特征值函数后忽略质量。

```python
import numpy as np
from scipy.linalg import eigh
M = np.diag([.02, .03])
K = np.array([[140., -60.], [-60., 180.]])
values, modes = eigh(K, M)
frequencies = np.sqrt(values)/(2*np.pi)
assert np.allclose(K @ modes, (M @ modes) * values)
assert np.allclose(modes.T @ M @ modes, np.eye(2))
assert np.allclose(values, [4000., 9000.])
print('Natural frequencies / Hz:', frequencies)
print('Mass-normalized modes:', modes)
```

### 二 用压力和速度一起计算净声强

保持峰值相量约定，因此平均乘积前有1/2；R=1时有声压与速度分布，净平均声强仍为0。

```python
import numpy as np
rho, c, f = 1.2, 343., 500.
z0 = rho*c
x = np.linspace(0, c/f, 1001)
k = 2*np.pi*f/c
for R in [0., .6, 1.]:
    forward = np.sqrt(2)*np.exp(-1j*k*x)  # incident RMS pressure: 1 Pa
    backward = np.sqrt(2)*R*np.exp(1j*k*x)
    pressure = forward+backward
    velocity = (forward-backward)/z0
    intensity = .5*np.real(pressure*np.conj(velocity))
    expected = (1-R*R)/z0
    assert np.allclose(intensity, expected, atol=1e-14)
    print('R, net mean intensity / W m^-2:', R, intensity.mean())
```

### 三 分贝相加时保留相关交叉项

r₁₂是同一时间窗内两声压的归一化相关系数，不是介质密度。这个程序计算总声压级，未推算响度或全空间辐射功率。

```python
import numpy as np
def total_spl(L1, L2, r12):
    assert -1 <= r12 <= 1
    a, b = 10**(L1/20), 10**(L2/20)
    mean_square_ratio = a*a+b*b+2*r12*a*b
    return 10*np.log10(mean_square_ratio) if mean_square_ratio > 0 else -np.inf
uncorrelated = total_spl(70, 70, 0)
in_phase = total_spl(70, 70, 1)
opposite = total_spl(70, 70, -1)
assert np.isclose(uncorrelated, 73.0102999566)
assert np.isclose(in_phase, 76.0205999133)
assert np.isneginf(opposite)
print('Uncorrelated, in phase, ideal opposite / dB:', uncorrelated, in_phase, opposite)
```

## 常见误解与阅读检查

| 容易混淆的说法 | 应补上的条件 |
| --- | --- |
| 共振峰必等于固有频率 | 指定阻尼、输入和位移/速度/功率等输出 |
| 位移振幅大就一定辐射更多声功率 | 检查运动分布、尺寸、频率与辐射负载 |
| 声压平方总能直接换成净声强 | 保留质点速度、相位与场的结构；逐项核对特例 |
| 压力透射幅度大于1违反能量守恒 | 把两侧阻抗计入透射能流比例 |
| 声压级和声强级严格相同 | 核对参考量、ρ₀c、方向及是否存在反射 |
| 两个70 dB总是73 dB | 检查同一接收点的相关性与平均条件 |
| 距离翻倍总下降6 dB | 检查固定功率、球面自由场、指向性、反射与吸收 |
| 理想开口就是所有频率下的精确零压力 | 检查辐射、端修正、损耗与横向模态 |
| 共振器只靠储能就能持续吸声 | 区分反应性储能、真实耗散和能流匹配 |

读完应能给振动与声学变量配上正确单位，复算模态、共振和声级，解释驻波能量与净通量的区别，并说明边界与测量链怎样限制结论。本文完成定义、来源、解析、数值及页面核查，保留AI辅助草稿和专业审阅待完成标记。
