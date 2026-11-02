---
title: "复变函数"
english: "Complex Analysis"
slug: "complex-analysis"
summary: "用声音学习复变函数：从纯音的相量、干涉与复声阻抗，进入复导数、解析性、对数分支、Cauchy积分、Taylor与Laurent级数及留数，再用收敛域、衰减振荡和滤波器响应连接听觉技术研究。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "数学基础", "复数", "解析函数", "相位", "复积分", "留数", "零极点"]
aliases: ["复分析", "复变函数论", "听觉研究中的复变函数", "Functions of a Complex Variable"]
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
  - {label: "课程定位", value: "从声音的幅值与相位进入复分析及变换方法"}
  - {label: "入门重点", value: "复数、相量、复导数、解析性与对数分支"}
  - {label: "核心方法", value: "复积分、级数、留数、零极点与收敛域"}
  - {label: "研究连接", value: "复声压、声阻抗、滤波器响应与衰减振荡"}
references: ["ca-mit-algebra", "waves-unsw-impedance", "ca-mit-analytic", "pd-smith-2007", "ca-mit-cauchy", "ca-mit-formula", "ca-mit-series", "ca-smith-one-pole", "ca-mit-residue", "ca-mit-laplace", "ca-smith-poles", "ca-mit-integrals", "ca-scipy-freqz", "ca-scipy-lfilter", "mp-smith-filters", "we-demanet-2016"]
order: 1006
---

**复变函数**（functions of a complex variable）是以复数为自变量的函数；研究它们的可导性、解析性、积分、级数与奇点的学科称为**复分析**（complex analysis）。在听觉与声学研究中，复数可以同时记录声音的幅值和相位，而复分析进一步解释：传递函数为什么能展开成脉冲响应？极点为什么与衰减振荡有关？同一个代数表达式，为什么还要说明收敛域才能确定系统？[1](#ref-ca-mit-algebra)

本篇把复数运算作为入口，并实际进入解析函数与复积分，而不是只列傅里叶变换中的复数符号。前半从同频纯音、复声压和相位分支建立直观，后半用一阶低通与二阶数字谐振器展开级数、留数和复频率。所有数值、八张图及三段音频均为原创教学设定，不是听者、器件或房间的实测结果。

本篇先从复数的两坐标表示与代数例子讲起，再逐步引入复导数和复积分；不同深度所用工具见下方提示。矩阵运算可与[线性代数](../linear-algebra/)配套，随机噪声另见[概率论](../probability-theory/)。本篇不代替完整复分析课程的证明与习题，解析延拓、广义函数和完整滤波器设计只提供后续入口。

## 阅读准备与独立阅读

**起步知识。** 从实数运算、平方根、坐标图和周期波形开始。复导数、路径积分与级数部分会逐步用到变化率、累积和极限；完整证明与手算练习仍需要相应微积分知识。

**随用随补。** 令j²=−1，复数a+jb先看成平面中的点(a,b)：模是到原点的距离，辐角是方向角。导数先理解为局部变化率；积分先理解为沿给定路径累加很小的贡献。正文会进一步说明复导数为何要求各个方向相容，而不只是在实轴上求导。

**分层阅读。** 第一遍读复平面、同频声音相加、声阻抗和相位分支，再观察极点对应的衰减图。第二遍核对Cauchy条件、复积分、级数与留数；矩阵和随机噪声的关联阅读可按具体问题补充。

## 一个复数怎样表示一个声音 复平面与相量

### 实部和虚部是同一个数的两个坐标

记 $j^2=-1$，复数写为 $z=x+jy$，其中 $x,y$ 为实数，分别称为**实部**与**虚部**。数学教材常用 $i$，工程中为避免与电流等符号混淆，常用 $j$；两者表示同一个虚数单位。复平面横轴为实部、纵轴为虚部，复数相加就是对应坐标相加。

复数的**模**为 $|z|=\sqrt{x^2+y^2}$。当 $z\ne0$ 时，可选一个角度 $\theta$，使

$$
z=|z|(\cos\theta+j\sin\theta)=|z|e^{j\theta}.
$$

这称为极坐标形式；最后一个等号是**Euler公式** $e^{j\theta}=\cos\theta+j\sin\theta$。角度可相差任意整数倍的 $2\pi$，因此幅角不是天然唯一的实数；零复数的模为0，但幅角未定义。[1](#ref-ca-mit-algebra)

例如 $0.01+j0.01\sqrt3=0.02e^{j\pi/3}$。它距原点0.02，与实轴夹角60°。乘以 $e^{j\phi}$ 使复数旋转 $\phi$，乘以正实数使模按比例伸缩；一般复乘同时完成伸缩与旋转。这比单独跟踪两个三角函数系数更方便。

### 用峰值相量固定幅值与初相位

对单频稳态声压，本篇统一采用

$$
p(t)=A\cos(\Omega t+\phi)
=\operatorname{Re}\{P e^{j\Omega t}\},\qquad P=Ae^{j\phi},\quad \Omega=2\pi f.
$$

$p(t)$ 是实际实值声压，单位Pa；$P$ 是**复声压相量**，保存峰值 $A$ 与初相位 $\phi$；$f$ 用Hz，$\Omega$ 用rad/s。这里的虚部不是另一种实际声压，也不是“耳朵听到的虚声”，而是与余弦相差四分之一周期的正交坐标。若采用正弦作参照，坐标会变化，但实际波形不必变化。

取 $A=0.02$ Pa、$f=1000$ Hz、$\phi=\pi/3$，便得到图1。固定相量 $P$ 先乘随时间旋转的 $e^{j\Omega t}$，再向实轴投影，就是波形。相量只适合给定频率的稳态表示；宽带语音需要多个频率分量，不能把任意整段录音压成一个相量。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/phasor-and-wave.svg" target="_blank" rel="noopener" aria-label="查看相量与波形完整图"><img src="/n3-hearingpedia/figures/complex-analysis/phasor-and-wave.svg" alt="复平面中模为零点零二帕相位六十度的相量，以及对应的一千赫兹实值声压波形" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 1　相量不是额外的声音，而是幅值与相位的坐标。</strong>（a）复声压的实部0.01 Pa、虚部约0.01732 Pa；（b）采用正时间指数，对应峰值0.02 Pa的1000 Hz波形。相量坐标与实际声压的单位都是Pa，但含义不同。图为解析教学计算。</figcaption>
</figure>

对于非零频率纯音，声压RMS为 $A/\sqrt2$，所以本例约0.01414 Pa。本文采用峰值相量；若某篇文献采用RMS相量，后文声强公式的因子会改变。还应先查清时间指数正负号：若别人用 $e^{-j\Omega t}$，同一实波形对应的相量要取共轭，不能只复制相位的数值。

## 两个同频声音怎样相加 复数运算与声阻抗

### 干涉来自相量相加 不是幅值直接相加

在相同频率、同一时刻参考下，设 $p_1(t)=\operatorname{Re}\{P_1e^{j\Omega t}\}$、$p_2(t)=\operatorname{Re}\{P_2e^{j\Omega t}\}$。实部运算的线性性给出 $p_1+p_2=\operatorname{Re}\{(P_1+P_2)e^{j\Omega t}\}$，因此先在复平面相加相量，再取模，才是合成幅值。

令 $P_1=A$、$P_2=Ae^{j\Delta\phi}$，则

$$
|P_1+P_2|^2=2A^2(1+\cos\Delta\phi),\qquad
|P_1+P_2|=2A\left|\cos\frac{\Delta\phi}{2}\right|.
$$

取 $A=0.2$ 的无量纲教学幅值，相位差0°、120°、180°时，合成幅值分别为0.4、0.2、0。相同频率并不意味着总幅值总是两倍；理想反相时完全抵消，也不意味着两个原始分量本身不存在。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/coherent-interference.svg" target="_blank" rel="noopener" aria-label="查看相干叠加完整图"><img src="/n3-hearingpedia/figures/complex-analysis/coherent-interference.svg" alt="两个等幅一千赫兹纯音在零度一百二十度一百八十度相位差下的相量首尾相加和对应波形" width="1400" height="800" loading="lazy" /></a>
  <figcaption><strong>图 2　相位差改变合成幅值。</strong>上排在复平面首尾相加，蓝、绿为两个分量，红为合成；下排在同一幅值尺度比较对应实波形。三列均为1000 Hz、每个分量幅值0.2，区别仅在第二个分量初相位。数字叠加未包含空间传播与设备误差。</figcaption>
</figure>

以下三段音频采样率16 kHz、时长0.7秒，首尾10 ms淡入淡出，统一乘0.6播放增益，未逐段归一化。第三段是理想单通道反相抵消后的静音。声音幅值无量纲、播放未校准；这是波形叠加演示，不是个人听阈测试。

<p>相位差0°，合成幅值0.4：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/complex-analysis/phase-0.wav"></audio>
<p>相位差120°，合成幅值0.2：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/complex-analysis/phase-120.wav"></audio>
<p>相位差180°，理想抵消：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/complex-analysis/phase-180.wav"></audio>

这是同频、相位关系固定的**相干叠加**。两个互不相干声源的长期均方值可在适当条件下相加，是另一种统计关系；不能把这里的幅值公式直接搬过去。实际[房间声学](../room-acoustics/)或主动控制还存在时延、位置、频带与误差，单点单频抵消不能推出整个房间安静；物理幅值也不直接等同[主观响度](../loudness/)。

### 共轭让幅值平方和平均声强写得更清楚

**共轭**定义为 $\bar z=x-jy$，故 $z\bar z=|z|^2$。除法可通过乘共轭化成实分母：$z_1/z_2=z_1\bar z_2/|z_2|^2$，要求 $z_2\ne0$。在声音测量中，复数比值不仅比较幅值，也比较相位。

设同一位置、同一方向的声压峰值相量 $P=0.02$ Pa，质点速度相量 $V=10^{-4}e^{-j\pi/3}$ m/s。**比声阻抗**为

$$
Z_s=\frac{P}{V}=200e^{j\pi/3}
=100+j173.205\ \mathrm{Pa\,s/m}.
$$

它与声压除以**体积速度** $Q$ 的声阻抗 $P/Q$ 不同，后者单位为 $\mathrm{Pa\,s/m^3}$。这两种分母在[电声换能](../electroacoustic-transducer/)与[声导抗测量](../acoustic-immittance-tympanometry/)中都可能出现，不能只看字母名称。[2](#ref-waves-unsw-impedance)

相同频率的实声压与实速度相乘，再对完整周期平均，和频项平均为0，得到沿该方向的**平均声强**

$$
\langle I\rangle=\frac12\operatorname{Re}\{P\bar V\}
=\frac12|P||V|\cos(\phi_P-\phi_V)
=5.0\times10^{-7}\ \mathrm{W/m^2}.
$$

共轭使相位差而不是相位和进入结果。$|P|^2$ 本身的单位为Pa²，不是声强；只有再满足相应行波与介质关系时，才能用阻抗把声压平方转换成能流。本例是局部谐波量的数学设定，不代表空气中单向平面行波的特性阻抗；若用RMS相量，前面的 $1/2$ 应去掉。[2](#ref-waves-unsw-impedance)

## 复函数为什么比二维函数多一层要求 复导数与解析性

### 导数必须不依赖趋近方向

复函数 $F:D\subset\mathbb C\to\mathbb C$ 可以写成 $F(z)=u(x,y)+jv(x,y)$。**复导数**在内点 $z_0$ 定义为

$$
F'(z_0)=\lim_{h\to0,\ h\in\mathbb C}
\frac{F(z_0+h)-F(z_0)}{h}.
$$

$h$ 可以沿任意方向和路径趋于0，极限必须一致。对 $F(z)=z^2$，差商等于 $2z_0+h$，所以从任何路径趋近都得到 $2z_0$；在 $z_0=1+j$，导数为 $2+2j$。检查实轴和虚轴只是必要的方向对照，不是已经检查了所有路径。[3](#ref-ca-mit-analytic)

对 $F(z)=\bar z$，差商为 $\bar h/h$：实方向得到1，纯虚方向得到−1，导数不存在。这里共轭运算完全有用，却不复可导；“用于声学的函数”不必全部解析。例如幅值 $|H|$、平方幅值 $H\bar H$ 往往需要同时用到复变量与其共轭，不能把解析函数的定理直接用于它们。

### Cauchy–Riemann方程怎样从两个方向得到

若复导数存在，分别取 $h$ 为实数与纯虚数，可得

$$
u_x=v_y,\qquad u_y=-v_x.
$$

这组关系称为**Cauchy–Riemann方程**，下标表示偏导数。例如 $F(z)=z^2$ 时 $u=x^2-y^2,v=2xy$，于是 $u_x=2x=v_y$，$u_y=-2y=-v_x$。

一种方便使用的**充分条件**是：$u,v$ 在某邻域具有连续一阶偏导，且在所考察点满足这组关系，则该点复可导。如果在一个开域内处处满足这些条件，就可得到整个开域内的复可导性。仅在一点列出CR等式而没有相应实可微性或连续偏导条件，不能据此保证复导数存在。[3](#ref-ca-mit-analytic)

**全纯函数**（holomorphic）指在开集每一点复可导的函数；**解析函数**（analytic）指每一点附近都可写成收敛幂级数的函数。在一复变量理论中两者等价，但“在孤立一点有复导数”不等于“在该点附近解析”。例如 $F(z)=|z|^2$ 在原点的差商为 $|h|^2/h=\bar h\to0$，所以原点可导；其CR条件只在原点成立，故没有包含原点的解析邻域。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/complex-derivative.svg" target="_blank" rel="noopener" aria-label="查看复导数方向完整图"><img src="/n3-hearingpedia/figures/complex-analysis/complex-derivative.svg" alt="平方函数的实轴虚轴差商趋于同一值，共轭函数差商方向不一致，模平方函数在原点差商趋于零" width="1400" height="600" loading="lazy" /></a>
  <figcaption><strong>图 3　比较方向有助于发现错误，但不能替代全路径论证。</strong>（a）平方函数在1+j附近的两组差商趋于2+2j；（b）共轭函数沿实、虚方向分别为1与−1；（c）模平方在原点的两组差商趋于0，仍不在邻域解析。平方与模平方的全路径极限由正文代数式确定。图为教学计算。</figcaption>
</figure>

### 解析性与声学方程怎样联系

对解析函数，实部、虚部具有更高阶光滑性，结合CR关系可得 $u_{xx}+u_{yy}=0$、$v_{xx}+v_{yy}=0$，称为二维**调和函数**。这里“调和”指满足Laplace方程，不等于声音中“含整数倍频率的谐波”。实际非零频率声压一般满足[Helmholtz方程](../helmholtz-equation/)，不能仅因为采用复声压就认定它在空间坐标上是某个解析函数。[16](#ref-we-demanet-2016)

复导数的局部几何也有意义：$F(z_0+h)\approx F(z_0)+F'(z_0)h$。若 $F'(z_0)\ne0$，小尺度变化相当于同一伸缩与旋转，因而局部保角；导数为0时不能直接使用这一结论。数学映射的保角性质也不会自动成为真实房间声场的相似律，仍需检查物理方程与边界。

## 为什么相位会跳变 复指数 对数与分支

### 复指数很好求逆却不唯一

对 $z=x+jy$，$e^z=e^x(\cos y+j\sin y)$。所以实部控制模，虚部控制角度，且 $e^{z+2k\pi j}=e^z$。求解 $e^w=z\ne0$ 得到全部对数值

$$
\log z=\ln|z|+j(\theta+2k\pi),\qquad k\in\mathbb Z.
$$

选择连续的一组角度值，才形成一个单值**分支**。例如删去非正实轴后，在 $D=\mathbb C\setminus(-\infty,0]$ 上选 $-\pi<\operatorname{Arg}z<\pi$，便得到解析的主支 $\operatorname{Log}z$，其导数为 $1/z$。不能在整个去掉原点的复平面上选出全局单值解析对数，因为绕原点一圈时角度增加 $2\pi$。[1](#ref-ca-mit-algebra)

因此主值对数的乘法规则需要检查分支。取 $z_1=z_2=e^{j3\pi/4}$，两主值对数之和为 $j3\pi/2$；乘积是 $-j$，其主值对数为 $-j\pi/2$，相差 $2\pi j$。两结果的指数相同，却不是同一个主值。用 $z^a=e^{a\operatorname{Log}z}$ 定义复幂时，也必须携带分支约定。

在声传播中，复波数或阻抗可能涉及平方根；应结合时间指数、传播方向与衰减条件选择支，不能把软件给出的某个根直接当作物理解。[16](#ref-we-demanet-2016)

### 主值相位与展开相位怎样区别

取纯延迟 $\tau=3$ ms。在 $e^{j\Omega t}$ 约定下，频率响应为 $H(f)=e^{-j2\pi f\tau}$，幅值恒为1，连续相位可写为 $-2\pi f\tau$。计算机的主值相位通常约束在−π至π之间，所以沿频率增加时会反复跳变；主值区间的端点归属是软件约定，并不保证沿频率连续。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/log-and-phase.svg" target="_blank" rel="noopener" aria-label="查看相位分支完整图"><img src="/n3-hearingpedia/figures/complex-analysis/log-and-phase.svg" alt="三毫秒纯延迟的主值相位反复跳变，展开相位随频率连续下降" width="1400" height="750" loading="lazy" /></a>
  <figcaption><strong>图 4　同一频率响应可以使用不同相位坐标。</strong>0至2000 Hz、步长1 Hz，系统为3 ms纯延迟。（a）主值相位；（b）已知连续相位与稠密采样后的展开结果，纵轴均以π为单位。这里没有幅度零点和测量噪声；一般数据未必能仅靠展开恢复真实延迟。</figcaption>
</figure>

相位展开用相邻变化的约束补上整圈数，但没有凭空增加测量信息。比如在 $f_k=k\Delta f$（$k$ 为整数）的频率网格上采样，延迟相差整数倍 $1/\Delta f$ 可得到同一组复响应；采样太稀或噪声太大时，仅靠自动展开无法判定真实支。响应为0时相位未定义，接近0时估计也很敏感。详见[相位与群延迟](../phase-and-group-delay/)。[4](#ref-pd-smith-2007)

## 沿复平面走一圈怎样积分 路径与Cauchy定理

### 复积分包含路径本身的变化

设一条分段光滑路径由 $z=\gamma(t)$ 参数化，$a\le t\le b$。**复路径积分**定义为

$$
\int_\gamma F(z)\,dz=\int_a^b F(\gamma(t))\gamma'(t)\,dt.
$$

不仅要把路径上的点代入函数，还要乘上路径的复变化量。反向遍历会改变积分符号；符号 $\oint$ 表示闭合路径。这里的路径是复自变量空间中的数学路径，不是麦克风在房间里移动的轨迹。[5](#ref-ca-mit-cauchy)

对逆时针单位圆 $z=e^{jt},0\le t\le2\pi$，$dz=je^{jt}dt$。取 $F(z)=1/z$，相乘后恒为 $j$，因此 $\oint dz/z=2\pi j$。取 $F(z)=z$ 则得到 $\int_0^{2\pi}je^{2jt}dt=0$。两个结果不同，不能笼统认为“绕一圈都抵消”。

### Cauchy积分定理的关键在域内解析

**Cauchy积分定理**的一种常用版本是：若 $F$ 在单连通开域 $D$ 上全纯，则任意位于 $D$ 内的分段光滑闭路径满足 $\oint F(z)dz=0$。单连通直观上表示闭路径能在域内缩成一点，不被洞阻挡；只在路径上有定义远远不够。[5](#ref-ca-mit-cauchy)

$1/z$ 在原点之外全纯，但单位圆围住了缺失的原点，不能找到包含该闭曲线并满足上述条件的单连通域。所以它的积分不为0并不违反定理。应用时必须检查函数在路径及所需内部区域的条件，不能只看函数画出来很平滑。

### Cauchy积分公式让边界决定内部值

若 $F$ 在一条逆时针分段光滑简单闭曲线及其内部的某开邻域全纯，且 $a$ 位于内部，则

$$
F(a)=\frac{1}{2\pi j}\oint\frac{F(z)}{z-a}\,dz,
\qquad
F^{(m)}(a)=\frac{m!}{2\pi j}\oint\frac{F(z)}{(z-a)^{m+1}}\,dz.
$$

第一式用边界积分给出内部函数值，第二式给出高阶导数，$m$ 为非负整数。它们说明全纯性远强于普通连续性；不能把任意复响应在一个圆上测出来，就未经条件检查地按这个公式推算内部。[6](#ref-ca-mit-formula)

例如取 $F(z)=z^2$、单位圆和 $a=1/2$，$F(a)=1/4$，故 $\oint z^2/(z-1/2)\,dz=\pi j/2$。分母带来的极点由公式明确处理，而不是假装积分核也处处全纯。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/contours-and-poles.svg" target="_blank" rel="noopener" aria-label="查看圆周积分完整图"><img src="/n3-hearingpedia/figures/complex-analysis/contours-and-poles.svg" alt="逆时针单位圆内的零点五处极点给出二派虚数积分，圆外一点五处极点则不给出贡献" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 5　路径内部是否有奇点，会改变积分。</strong>两图积分核都是1/(z−a)，路径均为逆时针单位圆；（a）a=0.5，积分2πj；（b）a=1.5，积分0。叉号表示极点，均不在路径上。为数学复平面示意，不表示物理空间中的声源位置。</figcaption>
</figure>

## 同一个公式为什么有两种展开 Taylor与Laurent级数

### 幂级数有自己的收敛范围

在某点 $z_0$ 附近解析的函数可写为**Taylor级数**

$$
F(z)=\sum_{n=0}^{\infty}c_n(z-z_0)^n,
\qquad c_n=\frac{F^{(n)}(z_0)}{n!}.
$$

最大收敛圆盘的边界受复平面中的解析障碍限制，不能只沿实轴找问题。最简单的例子 $1/(1-w)=\sum_{n=0}^\infty w^n$ 仅在 $|w|<1$ 成立；有限和恒等式 $\sum_{n=0}^{M-1}w^n=(1-w^M)/(1-w)$ 则可在 $w\ne1$ 时直接验证。无限级数需要检查余项是否趋于0。[7](#ref-ca-mit-series)

**Laurent级数**允许整数负幂：$F(z)=\sum_{n=-\infty}^{\infty}c_n(z-z_0)^n$，通常在环域 $r<|z-z_0|<R$ 收敛。同一函数在不同环域可以有不同展开；给出系数却不给出区域，信息不完整。

### 把级数解释为一个声音系统的脉冲响应

考虑零初始条件下的离散系统 $y[n]=ay[n-1]+x[n]$，取 $a=0.8$。对单位脉冲输入，因果解为 $h[n]=a^n$（$n\ge0$），负时间为0。它的双边Z变换定义为 $H(z)=\sum_{n=-\infty}^{\infty}h[n]z^{-n}$，所以

$$
H(z)=\sum_{n=0}^{\infty}a^nz^{-n}
=\frac{1}{1-az^{-1}}=\frac{z}{z-a},\qquad |z|>|a|.
$$

每个 $z^{-n}$ 项承载一个时刻的脉冲响应系数；这里是关于 $z^{-1}$ 的幂级数、关于 $z$ 的外部Laurent展开。**收敛域**（region of convergence，ROC）说明这串加和在哪里真正代表该函数。[8](#ref-ca-smith-one-pole)

若改在内部 $|z|<|a|$ 展开同一个有理式，则

$$
\frac{z}{z-a}=-\frac{z/a}{1-z/a}
=-\sum_{k=1}^{\infty}\frac{z^k}{a^k}.
$$

对照Z变换的 $z^{-n}$，这代表 $h[n]=-a^n$（$n\le-1$），非负时间为0，是另一条反因果序列。对 $a=0.8$，其负时间尾部随 $n\to-\infty$ 增长，不绝对可和。因而同一有理式本身并没有唯一指定因果性、稳定性或时域序列。

### 截取更多项之前 先看是否在收敛域内

在 $z=1$ 时，外部级数的精确和为5。截取8项仅得4.1611392，尾项为 $a^8/(1-a)=0.8388608$。这里的误差不是数值程序算错，而是有限项截断。若选 $z=0.6$，$|a/z|>1$，这套外部展开甚至不收敛，增加项数会越来越远；此时应考虑内部的另一套展开。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/series-and-roc.svg" target="_blank" rel="noopener" aria-label="查看级数与收敛域完整图"><img src="/n3-hearingpedia/figures/complex-analysis/series-and-roc.svg" alt="零点八极点以外的因果收敛域包含单位圆，以及三个复平面取值下外部级数截断误差随项数变化" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 6　有理式、展开系数和收敛域要一起阅读。</strong>（a）因果h[n]=0.8ⁿ对应的外部ROC，蓝色为收敛区域，极点与边界不包含在内；（b）在实数z=1、0.9、0.6处比较外部级数截断误差，前两者收敛、后者发散。z为变换变量，不是声压值，图为原创计算。</figcaption>
</figure>

当单位圆位于ROC内时，可取 $z=e^{j\omega}$ 得到相应频率响应。对这里的因果序列，$\sum_n|h[n]|=1/(1-a)=5$，满足离散LTI系统的BIBO稳定条件。对有限阶、因果且已约分的有理传递函数，所有极点严格位于单位圆内可作为该稳定条件的判据；去掉因果与ROC条件后，不能只凭极点位置作同一推论。

## 奇点为什么重要 留数与逆Z变换

### 零点 极点和可去奇点不是同一个概念

若解析函数在 $a$ 附近可写为 $F(z)=(z-a)^mG(z)$，$G(a)\ne0$，则 $a$ 是 $m$ 阶**零点**。若在去心邻域解析，则可由Laurent展开的负幂部分区分孤立奇点：没有负幂为**可去奇点**；负幂只有有限项，最高为 $(z-a)^{-m}$，为 $m$ 阶**极点**；负幂有无限多项则为**本性奇点**。[9](#ref-ca-mit-residue)

例如 $\sin z/z$ 在0处表达式未定义，但补上值1即可解析延拓，是可去奇点。$1/(z-a)$ 在 $a$ 有简单极点，$e^{1/z}$ 在0有本性奇点。复对数的原点是分支点，不属于能用单值Laurent展开包围的上述孤立奇点情形，不能一概当成极点处理。

滤波器有理式的零极点应在约去公共因子后讨论。例如 $(z-a)/(z-a)$ 作为约分后的外部传递函数是常数1，而不是一个实际发散峰；原表达式在 $a$ 的空缺可以补上。但若实现中仍保留相消的内部动态，外部传递函数并不自动保证内部状态稳定。这是代数描述与实现结构的区别。[11](#ref-ca-smith-poles)

### 留数是负一次幂系数 不是峰高

**留数** $\operatorname{Res}(F,a)$ 是Laurent展开中 $(z-a)^{-1}$ 的系数。简单极点可用 $\lim_{z\to a}(z-a)F(z)$ 求得；若 $F=g/q$，$g,q$ 在附近解析，且 $q(a)=0,q'(a)\ne0$，则留数为 $g(a)/q'(a)$。留数可以为复数，不是图上幅度峰值。[9](#ref-ca-mit-residue)

**留数定理**在本篇使用的形式为：若逆时针简单闭曲线内只有有限个孤立奇点，函数在其余内部及曲线上解析，则

$$
\oint F(z)\,dz=2\pi j\sum_{a_k\text{在内部}}\operatorname{Res}(F,a_k).
$$

曲线上不能有未处理的奇点；顺时针方向需改变符号。图5的积分核 $1/(z-a)$ 在简单极点处留数为1，所以极点在内得到 $2\pi j$，在外得到0。

### 从圆周积分取回一个采样点

若Z变换的Laurent级数在某环域收敛，选其中一条逆时针圆周 $C$，则系数公式给出

$$
h[n]=\frac{1}{2\pi j}\oint_C H(z)z^{n-1}\,dz.
$$

对 $H(z)=z/(z-a)$ 的因果外部展开，取半径 $R>|a|$。当 $n\ge0$，被积函数是 $z^n/(z-a)$，在 $a$ 的留数为 $a^n$，因此正好恢复 $1,a,a^2,\ldots$。[7](#ref-ca-mit-series) [9](#ref-ca-mit-residue)

当 $n<0$，不能仍只算 $a$：因子 $z^{n-1}$ 使被积函数在原点也产生极点。原点留数与 $a$ 处贡献相消，因果结果才是0。若把积分圆改到内部ROC，便会提取另一条反因果序列。这解释了为什么逆变换需要函数、积分核和ROC三项信息，不能只背“对传函极点求和”。

## 同样是复频率 为什么s平面和z平面不同

### 连续时间用复指数的增长率与角频率

双边**Laplace变换**写为 $H_c(s)=\int_{-\infty}^{\infty}h_c(t)e^{-st}dt$，$s=\sigma+j\Omega$。这里 $s$ 的实部、虚部均有每秒的量纲：$e^{st}=e^{\sigma t}e^{j\Omega t}$，实部控制增长或衰减，虚部控制振荡。下标 $c$ 用于区别连续时间模型。[10](#ref-ca-mit-laplace)

取因果一阶低通 $h_c(t)=\omega_c e^{-\omega_ct}$（$t\ge0$，负时间为0），$\omega_c=2\pi\times1000\ \mathrm{s}^{-1}$。直接积分得到

$$
H_c(s)=\frac{\omega_c}{s+\omega_c},\qquad
\operatorname{Re}s>-\omega_c.
$$

该ROC包含虚轴，故可取 $s=j\Omega$ 得到频率响应。极点在 $-\omega_c$，脉冲响应衰减时间常数为 $1/\omega_c\approx0.1592$ ms；在1000 Hz处，幅值为 $1/\sqrt2$、相位为 $-\pi/4$，幅度增益约−3.0103 dB。连续时间冲激响应的单位含每秒，与此处无量纲传递函数及离散冲激响应不能混为一谈。

对因果、适当有理且不存在未处理隐藏模态的连续LTI模型，极点在严格左半平面对应指数衰减与外部稳定；离散系统的边界却是单位圆。更一般的双边情形仍需检查ROC是否包含相应频率轴，而不是用一个图上的位置代替全部条件。

### z是无量纲的每采样步乘子

采样间隔为 $T_s$ 时，连续指数在采样点满足 $e^{snT_s}=(e^{sT_s})^n$，因此对应模态乘子为 $z=e^{sT_s}$。若 $\operatorname{Re}s<0$，则 $|z|<1$；虚轴映到单位圆。这是**指数模态的对应**，不表示任意数字滤波器都能把 $s$ 直接换成 $\log z/T_s$ 获得模拟模型。

离散角频率 $\omega=2\pi f/f_s$ 用rad/样本，$\Omega=2\pi f$ 用rad/s；虚部差 $2\pi/T_s$ 的连续指数映到同一个 $z$。这正是采样后频率周期性的一种表示，反向取对数时又会遇到分支。双线性变换则是另一种映射，不能与 $z=e^{sT_s}$ 的模态关系混称同一公式。

## 极点怎样变成衰减振荡 一个数字谐振器的例子

### 共轭极点使实信号保持实值

取实系数二阶模型

$$
H_r(z)=\frac{1}{1-2r\cos\theta_0\,z^{-1}+r^2z^{-2}}
=\frac{1}{(1-re^{j\theta_0}z^{-1})(1-re^{-j\theta_0}z^{-1})}.
$$

对 $0<r<1$ 的因果解释，两个极点为 $re^{\pm j\theta_0}$，ROC为 $|z|>r$。共轭成对使分母系数为实数；展开后对应的实脉冲响应为

$$
h[n]=r^n\frac{\sin((n+1)\theta_0)}{\sin\theta_0},\qquad n\ge0,
\quad 0<\theta_0<\pi.
$$

它可由两个一极点展开相乘、收集同次幂系数得到，也可直接代入差分递推核验。$r^n$ 给出模态衰减，$\theta_0$ 给出正弦因子；时间常数为 $-1/(f_s\ln r)$，不是 $1/(1-r)$ 秒。[11](#ref-ca-smith-poles)

### 极点角度不一定精确等于幅频峰的位置

设 $f_s=16000$ Hz、$\theta_0=2\pi\times1000/f_s=\pi/8$。取 $r=0.95$ 与0.995，衰减时间常数分别约1.218 ms与12.469 ms。保持分子为1时，后者极点离单位圆更近，峰更高、更窄，振铃也更久；若另外调整分子增益，峰高比较就可能改变。

对这个特定两极点、常数分子的模型，内部幅度峰满足

$$
\cos\omega_{\mathrm{peak}}
=\frac{1+r^2}{2r}\cos\theta_0.
$$

该式可由对分母模平方求极值得到；只有右侧在−1至1之间且峰在内部时，才能这样求峰频，否则要检查端点。这里两种 $r$ 的峰分别约991.88 Hz与999.92 Hz。因此极点角度提供振荡频率，也常是窄峰的位置近似，却不能一概当作实际幅度峰的精确位置。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/poles-and-resonance.svg" target="_blank" rel="noopener" aria-label="查看极点与谐振完整图"><img src="/n3-hearingpedia/figures/complex-analysis/poles-and-resonance.svg" alt="同角度不同模长的共轭极点，其频率响应峰高宽度和模态衰减速度不同" width="1400" height="600" loading="lazy" /></a>
  <figcaption><strong>图 7　极点角度、模长与幅度峰相关，但含义不同。</strong>采样率16 kHz、极点角度π/8，对照r=0.95和0.995。（a）局部z平面，横纵采用相同比例，单位圆虚线为稳定边界；（b）分子均为1，未逐条归一化的增益；（c）仅画模态因子rⁿ，不把它当作完整脉冲波形。模型未拟合实际共振腔或听觉滤波器。</figcaption>
</figure>

对一般有理函数 $H(z)=g\prod_k(z-q_k)/\prod_l(z-p_l)$，在没有未处理相消的地方，其模等于 $|g|$ 乘以到各零点距离的乘积、再除以到各极点距离的乘积。还要同时计入增益、所有零极点及可能的幂次；“靠近一个极点”只是局部直观，不能忽略其他因子。[11](#ref-ca-smith-poles)

## 留数怎样帮助计算实积分 低通响应的面积

### 把实轴积分接成一个闭合轮廓

考察 $\int_{-\infty}^{\infty}(1+u^2)^{-1}du$。把实变量延到复变量 $w$，在上半平面用半径 $R>1$ 的半圆闭合，积分核 $1/(1+w^2)$ 内部只有极点 $w=j$，其留数为 $1/(2j)$。因此闭路积分为π。[12](#ref-ca-mit-integrals)

这还不是实轴积分的结论，必须证明大圆弧贡献趋于0。在弧上 $|1+w^2|\ge R^2-1$、弧长πR，故弧积分的模不超过 $\pi R/(R^2-1)\to0$。于是实轴积分确为π。闭合方向、弧估计、路径上无奇点缺一不可，不能只找留数而跳过其余步骤。

### 积分面积与三分贝带宽有什么不同

上节一阶低通的平方幅频响应为 $|H_c(j\Omega)|^2=1/[1+(\Omega/\omega_c)^2]$。令 $u=\Omega/\omega_c$，由上述积分及偶对称性可得

$$
\int_0^{\infty}|H_c(j\Omega)|^2\,d\Omega
=\frac{\pi\omega_c}{2}.
$$

若横轴改为Hz，$d\Omega=2\pi df$，则

$$
B_{\mathrm{eq}}=\int_0^{\infty}|H_c(j2\pi f)|^2\,df
=\frac{\pi f_c}{2}\approx1570.80\ \mathrm{Hz},\qquad f_c=1000\ \mathrm{Hz}.
$$

由于本例直流增益为1，这个单边积分可解释为与单位增益矩形滤波器具有相同平方响应面积的等效带宽。它不同于1000 Hz的三分贝截止频率。若用它预测白噪声输出方差，还需明确输入功率谱密度与单双边约定；这个面积本身不是某段录音的总声能。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/complex-analysis/residue-and-bandwidth.svg" target="_blank" rel="noopener" aria-label="查看实积分与带宽完整图"><img src="/n3-hearingpedia/figures/complex-analysis/residue-and-bandwidth.svg" alt="上半平面半圆围住正虚数单位极点，以及一阶低通平方响应在归一化频率轴上的面积" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 8　复积分可算出响应面积，但物理解释仍需单位与条件。</strong>（a）积分核1/(1+w²)的上半圆示意，极点±j中仅+j在内；实际推导取半径趋于无穷。（b）归一化角频率u上的平方幅度，0至1面积π/4，占0至无穷总面积的一半；曲线只显示到u=5。为教学解析图，非噪声实测。</figcaption>
</figure>

后续可继续学习辐角原理、共形映射，以及反馈系统的Nyquist判据；本篇实际计算集中在上述留数与面积例。讨论反馈稳定裕量还需建立闭环模型，不能把一个相位绕圈数直接当作器件可靠性结论。

## 三个可复现实验 与后续学习

### 从相量还原波形 并计算局部声强

```python
import numpy as np

f = 1000
t = np.arange(16000) / 16000
P = 0.02 * np.exp(1j*np.pi/3)
wave = np.real(P * np.exp(1j*2*np.pi*f*t))
assert np.max(np.abs(wave - 0.02*np.cos(2*np.pi*f*t+np.pi/3))) < 1e-12
V = 1e-4 * np.exp(-1j*np.pi/3)
pressure = 0.02 + 0j
Zs = pressure / V
intensity = 0.5 * np.real(pressure * np.conj(V))
assert abs(intensity - 5e-7) < 1e-18
print("比声阻抗 Pa s/m:", Zs)
print("平均声强 W/m^2:", intensity)
```

第一部分的声压相位为π/3；第二部分重新指定声压相位为0来计算声阻抗，不是把两种设定混在一起。速度相量在这里用m/s，若输入体积速度，必须改变物理量名称与单位。

### 沿两条圆周 提取同一有理式的不同序列

下面直接将逆Z圆周积分参数化，采用周期等距求和。内、外圆都不经过极点；代码比较的是两个不同ROC的解释，未调用“自动判断因果”的接口。

```python
import numpy as np

a = 0.8
theta = 2*np.pi*np.arange(8192) / 8192
def coefficient(n, radius):
    z = radius*np.exp(1j*theta)
    H = z/(z-a)
    return np.mean(H * z**n)

for n in (-2, -1, 0, 1, 2):
    outer = coefficient(n, 1.2)
    inner = coefficient(n, 0.4)
    expected_outer = a**n if n >= 0 else 0.0
    expected_inner = -a**n if n <= -1 else 0.0
    assert abs(outer-expected_outer) < 1e-10
    assert abs(inner-expected_inner) < 1e-10
    print(n, outer.real, inner.real)
```

这里因 $dz=jz\,d\theta$，逆变换的 $z^{n-1}$ 与额外的 $z$ 相乘，代码才使用 `H*z**n`；漏掉这个参数化因子，会把系数索引移错。

### 用递推和频率响应交叉检查谐振器

```python
import numpy as np
from scipy import signal

fs, r, theta0 = 16000, 0.95, np.pi/8
den = [1, -2*r*np.cos(theta0), r*r]
n = np.arange(1000)
delta = np.zeros(len(n)); delta[0] = 1
h = signal.lfilter([1], den, delta)
exact = r**n * np.sin((n+1)*theta0)/np.sin(theta0)
np.testing.assert_allclose(h, exact, atol=1e-12)
f = np.array([600., 1000., 1400.])
_, response = signal.freqz([1], den, worN=f, fs=fs)
z = np.exp(1j*2*np.pi*f/fs)
formula = 1/(1-2*r*np.cos(theta0)/z+r*r/z**2)
np.testing.assert_allclose(response, formula, atol=1e-12)
print("3个频率的增益:", np.abs(response))
```

`freqz` 中显式给出 `fs`，返回频率才与本例Hz坐标一致；`lfilter` 这里采用零初始状态。[13](#ref-ca-scipy-freqz) [14](#ref-ca-scipy-lfilter) 完整[可下载实验脚本](/n3-hearingpedia/code/complex-analysis/experiments.py)另含实积分、对数分支和原始差分递推，需Python、NumPy与SciPy。

### 六个自检问题

1. 两个等幅同频纯音的合成幅值，为什么不能总按两倍计算？
2. 一个函数在原点复可导，是否就能在原点附近使用Taylor级数？
3. 主值相位突然从−π跳到π，是否必然表示设备响应突变？
4. 给出 $H(z)=z/(z-0.8)$，是否已经唯一确定脉冲响应？
5. 用留数求 $h[-1]$ 时，为什么不能只看传函在0.8处的极点？
6. 极点角度对应1000 Hz，是否保证频率响应峰恰在1000 Hz？

<details><summary>展开答案与推理</summary>
<p>1．同频相量还存在相位差，先相加复数再取模。理想反相可抵消；不相干声的统计均方叠加又是另一套条件。</p>
<p>2．不能。必须在一个邻域内解析；模平方函数仅在原点复可导，是直接反例。</p>
<p>3．不必然。可能只是主值分支切换；真实响应零点、采样过稀与噪声还会影响相位解释。</p>
<p>4．没有。外部ROC对应因果序列，内部ROC对应本篇的反因果序列；还需ROC或等价的时域条件。</p>
<p>5．逆Z被积函数还含幂次因子。负时间索引会在原点引入额外极点；外部ROC下各处留数相消才得到0。</p>
<p>6．不保证。本例r=0.95时准确峰约991.88 Hz；整个零极点结构和分子都会影响幅度峰。</p>
</details>

随后可读[频谱与功率谱密度](../spectrum-and-power-spectral-density/)理解复指数分解，读[FIR与IIR滤波器](../fir-and-iir-filters/)连接差分实现，读[最小相位系统](../minimum-phase-system/)理解逆系统的因果与稳定条件。相同幅度响应仍可能有不同相位或延迟，只有满足相应最小相位条件时才可进一步建立特定幅相关系；不能从幅值一个量恢复任意系统的全部信息。[15](#ref-mp-smith-filters)
