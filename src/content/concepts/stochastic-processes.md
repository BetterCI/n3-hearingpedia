---
title: "随机过程"
english: "Stochastic Processes"
slug: "stochastic-processes"
summary: "配合《信号与系统》《数字信号处理》，从过程与实现、联合统计和平稳性进入相关函数、遍历性、白噪声与高斯过程，再建立功率谱、LTI滤波、采样混叠和Wiener估计的联系；用AR、随机相位、Poisson、Brownian和Markov例子核查有限记录的解释边界。"
categories: ["research-methods", "signal-processing", "neuroscience"]
tags: ["基础课程", "随机过程", "平稳性", "相关函数", "功率谱", "遍历性", "随机信号处理", "Wiener滤波"]
aliases: ["随机信号", "随机过程基础", "随机信号分析", "Random Processes", "Stochastic Signals"]
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
  - {label: "课程定位", value: "衔接概率论与信号系统，研究随机信号的时间依赖、谱和系统变换"}
  - {label: "核心区分", value: "过程与单条记录、平稳与遍历、白与独立、总体谱与有限估计分别判断"}
  - {label: "声音连接", value: "相关噪声、平均降噪、滤波输出、谱估计、采样与事件计数"}
  - {label: "证据边界", value: "平滑曲线或单段PSD不能独自证明平稳、独立、遍历、生理机制或因果"}
references: ["sp-processes", "sp-psd", "sp-wiener", "sp-mmse", "sp-wss", "sp-filtering", "sp-spectral", "sp-wkt", "sp-poisson", "sp-markov", "sp-basic", "sp-stationary", "sp-brownian", "sp-welch", "sp-periodogram", "sp-csd", "sp-coherence", "sp-lfilter"]
order: 1024
---

**随机过程**（stochastic process）是一族定义在同一概率空间上、通常由时间或空间索引的随机变量。它把“一次不确定的数值”扩展为“不同时间的数值怎样共同变化”。对声音研究，噪声在某一采样点的分布只是起点；相邻样本的依赖、通过滤波器后的变化以及有限录音怎样估计总体，都是随机过程的问题。[11](#ref-sp-basic)[1](#ref-sp-processes)

本篇与[信号与系统](../signals-and-systems/)、[数字信号处理](../digital-signal-processing/)配套。前两篇主要建立变换、卷积、采样、数字滤波与计算框架，这里进一步说明输入具有随机性时，均值、相关与谱怎样演化。[概率论](../probability-theory/)提供分布、期望和条件化的基础；本文在使用处重新解释需要的概念，不要求先完整通读配套课程。

十幅图及所有数值为原创指定概率模型或模拟，不是录音、神经或听者实测。将部分模拟幅值标成Pa，是明确物理量纲的教学约定，不代表已经完成传声器校准。文末有三个独立短程序，另提供[完整实验脚本](/n3-hearingpedia/code/stochastic-processes/experiments.py)。

## 阅读准备与独立阅读

**起步知识。** 理解加权平均、方差和采样序列即可先看实现、相关与滤波图。期望是按概率加权的总体平均；方差是偏离均值的平方平均，不是某次记录的一个固定幅度。

**随用随补。** 联合分布描述多个变量一起取值的概率；独立意味着联合概率按相应边缘概率相乘。相关描述二阶线性联系，不能覆盖全部依赖。傅里叶变换把随滞后变化的相关函数连接到频率表示，公式约定和单位将在正文明确。

**分层阅读。** 第一遍读过程与实现、平稳和反例，再看AR噪声与LTI输出；第二遍复算相关、谱、采样与有限估计；第三遍进入Wiener、事件过程和Markov链。需要推导时按点查[线性代数](../linear-algebra/)、[微积分](../calculus/)和[数理统计](../mathematical-statistics/)，不把完整先修课程作为入口门槛。

## 过程 实现与有限维分布

### 固定时间与固定实验结果是两种切法

设概率空间为(Ω,𝓕,P)，离散时间过程写X[n,ξ]，ξ∈Ω代表一次实验结果。固定n得到随机变量，固定ξ并让n变化得到一条**实现**或样本路径。录音文件中的一串数通常是一条有限实现；同一随机机制可以产生许多不同实现。[11](#ref-sp-basic)

**总体平均**是在固定时刻跨可能结果取期望；**时间平均**是沿一条实现跨时间计算。图1把这两种观察放在一起。把一次长录音切成很多片段，不会自动得到同样多的独立重复实验；能否替代总体还需要平稳、遍历或其他适用条件。

### 时间类型与取值类型分别分类

离散时间X[n]不必离散取值，采样声压可近似为连续值；连续时间N(t)也可只取整数，例如累计事件数。**有限维分布**是任取若干时刻时，(X[n₁],…,X[nᵣ])的联合分布。单个时刻的直方图通常不能确定这些联合分布，均值与方差也不能唯一确定一般过程。[1](#ref-sp-processes)

本文主线采用实值过程与有限二阶矩；频域中出现复数是为了保存相位。若扩展到复值随机过程，需要明确相关定义中的共轭以及相应统计条件，不能只把实变量换个符号。连续时间的路径连续性、可微性等也需额外说明，不能由“一族随机变量”几个字自动保证。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/ensemble-realizations.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/stochastic-processes/ensemble-realizations.svg" alt="同一AR模型的四条时间实现以及固定采样点的总体切片直方图" width="1400" height="550" loading="lazy" /></a><figcaption>图1　AR系数0.8、创新方差0.36 Pa²、初值按平稳N(0,1)抽取，采样率1000 Hz。右图取4000条实现的n=100，与已知总体密度比较；并非沿左图一条路径取直方图，也不以模拟直方图证明正态性。</figcaption></figure>

## 均值 相关与协方差 怎样描述时间依赖

均值m[n]=E[X[n]]，自相关R(n,m)=E[X[n]X[m]]，协方差C(n,m)=E[(X[n]−m[n])(X[m]−m[m])]。所以R=C+m[n]m[m]；非零均值会进入自相关，不能把自相关和协方差不加区分地使用。[1](#ref-sp-processes)

对有限时刻组成的向量，协方差矩阵必须半正定：任意实系数c对应的线性组合，其方差cᵀCc≥0。矩阵可以奇异，例如某些时刻间存在确定线性关系。不能任意画一条“像相关”的曲线就保证它能来自某个过程。

当方差非零时，归一化相关系数可由协方差除以相应标准差得到；它不是联合概率。相关为0通常只排除某种二阶线性联系，独立则对整个联合分布作更强约束。后面的白噪声反例会直接用到这一区别。

## 严格平稳与宽平稳 假设究竟限制什么

### 严格平稳看全部有限维分布

**严格平稳**要求任意有限组时刻同时平移后，联合分布不变；离散时间平移整数步，连续时间按允许的实数平移。它不是“每条实现画出来都平直”，也不要求每条波形重复。若严格平稳且二阶矩有限，则均值恒定，相关只依赖时差。[12](#ref-sp-stationary)

### 宽平稳只约束到二阶

**宽平稳**（WSS）要求有限二阶矩、均值m不随n改变，且R(n+k,n)只依赖滞后k。本文记

$$
\begin{aligned}
R[k]&=E[X[n+k]X[n]],\\
C[k]&=R[k]-m^2,\\
C[0]&=\operatorname{Var}(X[n]).
\end{aligned}
$$

实WSS过程有C[−k]=C[k]，且|C[k]|≤C[0]。WSS不自动严格平稳：令各时刻彼此独立，偶数点为N(0,1)、奇数点为等概率±1，则均值均为0、协方差均为单位脉冲，但一阶分布随奇偶改变。这个例子只满足二阶的时移要求。[5](#ref-sp-wss)

**高斯过程**则要求任意有限组变量联合高斯，而不只是每个时刻单独正态。对实高斯过程，均值与协方差决定全部有限维分布，因此WSS可进一步推出严格平稳。一般非高斯过程没有这个简化；严格平稳若缺乏有限二阶矩，也不能直接按上述WSS定义讨论。

## 遍历性 一段长记录能代表什么总体

### 先说明要替代哪一种平均

离散样本均值为X̄_N=N⁻¹Σₙ₌₀^(N−1)X[n]。若对WSS过程有E[|X̄_N−m|²]→0，称这里的均值在**均方意义下遍历**。功率、相关等其他时间平均能否替代总体，是另外的问题；不能证明样本均值收敛后，就默认所有统计量都已遍历。[1](#ref-sp-processes)

这一定义说明的是一种特定二阶收敛；严格的概率动力系统遍历性还有更完整的含义。本篇涉及实际估计时，会说明均值或均方值，而不把“遍历”当成一条记录可以代表所有性质的通行证。

### 一个平稳且白 却仍有共同隐变量的过程

令A以相同概率取1或2，在一次实现中保持不变；W[n]为独立同分布N(0,1)，并与A独立。取X[n]=A W[n]，则过程严格平稳、均值0，C[k]=2.5δ[k]，是二阶意义的白过程。但不同时间的平方相关：n≠m时Cov(X[n]²,X[m]²)=2.25，故样本不独立。

样本均值可以趋向0；沿一条路径的样本均方值却趋向本次A²，即1或4，而非总体E[A²]=2.5。它的功率平均不具有相应遍历性。单看平坦二阶谱，看不出这个共享尺度和高阶依赖。[1](#ref-sp-processes)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/white-not-independent.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/stochastic-processes/white-not-independent.svg" alt="共享随机幅度模型中时间均值与时间均方值的不同极限" width="1400" height="550" loading="lazy" /></a><figcaption>图2　X[n]=A W[n]，A在一次实现中固定。图中对A=1和2各展示三条条件模拟路径；均方值趋向对应的1或4，总体值为2.5。均值收敛不证明功率遍历，白也不等于无任何依赖。</figcaption></figure>

## 相关怎样改变平均降噪 AR例子

### 均值方差的精确有限样本式

对实WSS过程，样本均值的方差为

$$
\begin{aligned}
\operatorname{Var}(\overline X_N)&=\frac{C[0]}N\\
&\quad+\frac2{N^2}\sum_{k=1}^{N-1}(N-k)C[k].
\end{aligned}
$$

独立同方差时，非零滞后协方差消失，才得到C[0]/N。正相关往往减少平均带来的方差下降，负相关也可能改善某些平均；结论应从具体C[k]计算。把总体方差除以这个均值方差，可定义**针对均值精度**的等效独立样本数，但它不是所有检验或频谱估计的通用自由度。[1](#ref-sp-processes)

### 因果平稳AR(1)模型

令X[n]=aX[n−1]+E[n]，E为独立零均值创新、方差q，并独立于过去；选择因果稳定构造|a|<1，得到

$$
\begin{aligned}
\sigma_X^2&=\frac q{1-a^2},\\
C[k]&=\sigma_X^2 a^{|k|}.
\end{aligned}
$$

本文取a=0.8、q=0.36 Pa²，故方差1 Pa²；创新高斯时过程联合高斯。创新彼此独立不表示X的相邻样本独立。模拟初值按平稳分布抽取；若从零状态开始，早期方差会随时间建立，不能立刻称作同一平稳记录。[6](#ref-sp-filtering)[18](#ref-sp-lfilter)

N=64时，均值方差约0.130859 Pa²，独立假设却给0.015625 Pa²；对应均值精度的等效独立样本数约7.642。大N时方差渐近为9/N Pa²，标准差约为独立公式的3倍。这些数值只属于指定相关模型，不是所有噪声的固定修正倍数。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/correlation-averaging.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/stochastic-processes/correlation-averaging.svg" alt="AR相关函数以及时间平均方差的精确值、独立近似和大样本渐近值" width="1400" height="550" loading="lazy" /></a><figcaption>图3　a=0.8、方差1 Pa²；右图比较同一过程的精确有限N式与1/N、9/N。等效样本数只针对均值方差，不替代其他统计量的自由度或实际听觉效果。</figcaption></figure>

## 从相关到功率谱 先固定约定与单位

### 每Hz双侧谱与反变换

对采样率fₛ的实WSS序列，若R[k]绝对可和，就满足普通谱密度存在的一种方便的充分条件，可写每Hz双侧密度：

$$
\begin{aligned}
S_X(f)&=\frac1{f_s}\sum_{k=-\infty}^{\infty}
R[k]e^{-i2\pi fk/f_s},\\
R[k]&=\int_{-f_s/2}^{f_s/2}
S_X(f)e^{i2\pi fk/f_s}\,df.
\end{aligned}
$$

这是一种Wiener–Khinchin关系的约定。S_X随f以fₛ为周期，通常只画一个Nyquist区间；对实过程，普通谱为实、偶且非负。积分给R[0]=E[X²]，不是自动以瓦特计的电功率或声功率；声压输入时单位为Pa²/Hz。[2](#ref-sp-psd)[7](#ref-sp-spectral)

数字角频率ω按rad/sample计时，常写S_ω(ω)=ΣR[k]e^(−iωk)，有S_X(f)=S_ω(2πf/fₛ)/fₛ。这个1/fₛ不能在把横轴改成Hz时随意遗漏。单侧谱对实过程在内部正频率通常合并为双侧的2倍，DC与Nyquist的DFT端点不按相同规则重复加倍。[15](#ref-sp-periodogram)

### 不要把所有平稳过程强行画成普通密度

绝对可和是上式直接作为普通函数使用的充分条件，不是每个WSS过程都满足。更一般的平稳二阶谱需要**谱测度**，可以含离散谱线。非零均值还给自相关谱增加m²δ(f)形式的DC质量；中心化协方差谱与原始自相关谱因此不同。随机常量等结构也可能产生DC谱质量，DC线不只来自非零总体均值。[8](#ref-sp-wkt)

令X[n]=A cos(2πf₀n/fₛ+Φ)，Φ在[0,2π)均匀，A固定；它是严格平稳随机相位过程。选0<f₀<fₛ/2，R[k]=(A²/2)cos(2πf₀k/fₛ)，双侧在±f₀各有A²/4的谱质量。Dirac是积分意义的对象，没有可当作普通有限高度读取的“峰高”。

图4取A=√2 Pa、f₀=125 Hz、fₛ=1000 Hz。256点和1024点恰好含整数周期时，单侧矩形周期图峰高分别0.256和1.024 Pa²/Hz，积分均方值却都为1 Pa²。更高的有限记录峰不表示信号功率增大。[2](#ref-sp-psd)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/spectral-lines.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/stochastic-processes/spectral-lines.svg" alt="随机相位正弦的离散谱质量和两种记录长度的有限周期图峰" width="1400" height="550" loading="lazy" /></a><figcaption>图4　左图纵轴是每条线的质量Pa²，不是Dirac的有限高度；右图为一条指定相位实现，矩形窗、无去均值，频率均对齐DFT频点。峰高与频率网格一起变化，积分均为1 Pa²。</figcaption></figure>

## 白噪声 高斯与连续时间理想化

离散零均值白过程可定义为C[k]=σ²δ[k]，其中δ[k]在0为1、其他为0；每Hz双侧谱恒为σ²/fₛ。白描述二阶相关或谱的形状；独立描述联合分布，高斯描述有限维联合分布，三者不应互相替代。[2](#ref-sp-psd)

若过程联合高斯且不同时刻协方差为0，则相应样本独立；仅逐点边缘正态不够。前面的A W[n]反例是高斯尺度混合，给定A时为高斯白序列，未经条件化的过程并不是高斯过程。

连续时间理想白噪声常形式化写为R(τ)=(N₀/2)δ(τ)、双侧谱N₀/2。它不具有可按普通点值读取的有限方差，通常作为广义过程或积分驱动使用；物理噪声和采集系统总有限带宽。带限到±B的平坦谱，方差才是N₀B。[8](#ref-sp-wkt)

改变采样率时，固定离散σ²会使每Hz白谱按σ²/fₛ变化。若目标是覆盖整个Nyquist带的相同连续谱密度，离散方差需随带宽相应改变；不能同时固定所有这些量，还声称模拟的是完全相同的物理噪声。

## 随机输入通过LTI系统后的统计

### 均值与输出谱

令Y[n]=Σₗh[l]X[n−l]，输入WSS、二阶矩有限，h绝对可和是保证相应均方构造良好的方便充分条件。全历史稳态输出仍WSS，均值为m_Y=m_XΣh[l]。输出自相关由两份滤波权重与输入相关组合，频域简化为

$$
\begin{aligned}
H(f)&=\sum_l h[l]e^{-i2\pi fl/f_s},\\
S_Y(f)&=|H(f)|^2 S_X(f).
\end{aligned}
$$

相应公式也可按谱测度理解；带谱线时不能假装原谱已变成普通光滑密度。H无量纲时不改变PSD的物理单位；积分输出谱得到输出均方值。[5](#ref-sp-wss)[6](#ref-sp-filtering)

有限程序的零初态输出可能含建立过程。AR从零开始的早期样本、FIR缺少最前面的历史，不能仅凭系统稳定就把所有输出点当作已经处于稳态。本文AR用平稳初值；三抽头因果估计图避开最初两点。

图5把平稳AR输入通过8点等权平均，输出方差约0.604858 Pa²；若输入是方差1的白序列才是1/8 Pa²。滤波可以改变相关和频带，却不自动使输出样本独立，也不保证某种听觉任务的信噪比或可懂度提高。[18](#ref-sp-lfilter)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/lti-colored-spectra.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/stochastic-processes/lti-colored-spectra.svg" alt="白创新经AR整形得到的有色谱，以及AR输入经过八点平均的总体输出谱" width="1400" height="550" loading="lazy" /></a><figcaption>图5　双侧每Hz密度，fₛ=1000 Hz。右图按已知总体|H|²S_X计算，输出方差0.604858 Pa²；对数显示下限10⁻¹⁰，实际滤波零点可为0。曲线不是单条录音FFT，也不是实测降噪性能。</figcaption></figure>

### 互谱的方向与平方相干

对联合WSS的实过程，本文取R_YX[k]=E[Y[n+k]X[n]]，其每Hz傅里叶变换记S_YX。上述无噪声LTI关系给S_YX=H S_XX；延迟d点时H=e^(−i2πfd/fₛ)，相位的符号因此确定。交换X、Y顺序会共轭反向，软件命名必须核对。[6](#ref-sp-filtering)

SciPy的`csd(x,y)`采用conj(FFT(x))·FFT(y)，其结果方向对应本文的S_YX，而不能只按变量名Pxy猜测。实际频谱相位还受时间参考和滤波链影响。[16](#ref-sp-csd)

在普通联合谱密度及非零分母处，平方相干为|S_YX|²/(S_XX S_YY)，范围在0到1。它衡量频率相关的归一化二阶联系，不独自证明因果或直接耦合。单个未经平均的谱点若直接用|YX*|²/(|X|²|Y|²)，非零时恒为1；估计相干需要相应分段或平滑及有效样本解释。[17](#ref-sp-coherence)

## 采样与随机谱混叠

若连续时间过程具有合适的有限方差谱密度S_c(f)，采样率fₛ，且数字谱也按每Hz定义，则基带内

$$
S_d(f)=\sum_{r\in\mathbb Z} S_c(f+r f_s).
$$

这是按当前物理频率约定写的混叠和，不额外再乘1/fₛ。若换成数字角频率谱，归一化又会改变。理想连续白噪声由于无限带宽，不可直接当成每个采样点有限方差的普通过程。[2](#ref-sp-psd)

图6取连续双侧谱0.001 Pa²/Hz、带宽±750 Hz，方差1.5 Pa²。按1000 Hz直接采样，|f|<250 Hz的基带谱为0.001，250<|f|<500 Hz为0.002；折叠后总方差仍为1.5 Pa²，但频率归属已改变。先理想低通到±450 Hz则方差为0.9 Pa²，带外量被删除，不能说只是换了画法而总量必不变。

抗混叠必须发生在相应降采样之前；折叠后的同频贡献一般不能仅靠后续数字低通重新分开。更完整的实现、过渡带与有限滤波器问题见数字信号处理，本文只核查随机谱和单位。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/sampling-aliasing.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/stochastic-processes/sampling-aliasing.svg" alt="带限白谱采样前后的混叠，以及先低通的不同结果" width="1400" height="550" loading="lazy" /></a><figcaption>图6　左图连续双侧谱限于±750 Hz；右图在1000 Hz基带按谱复制相加，未添加错误的额外采样率因子。绿色为另一个先理想限到±450 Hz的系统，其方差0.9而非1.5 Pa²；不是实际采集设备的实测频响。</figcaption></figure>

## Wiener估计 最优性需要指定信息范围

### MMSE与线性投影

给定观测Z，平方误差意义的最优一般估计为条件期望E[S|Z]；限制为线性或仿射形式，则得到LMMSE。二者一般不同，联合高斯是条件均值可化为相应线性/仿射形式的重要情形。均值非零时通常先中心化，再加回相应均值。[4](#ref-sp-mmse)

令Z[n]=S[n]+V[n]，S为上述方差1的平稳高斯AR，V为独立零均值白高斯噪声、方差0.5。若只使用Z[n]、Z[n−1]、Z[n−2]，线性估计Ŝ[n]=Σᵢ₌₀²wᵢZ[n−i]的正规方程为

$$
\begin{aligned}
R_{ij}&=0.8^{|i-j|}+0.5\delta_{ij},\\
r_i&=0.8^i,\qquad Rw=r,\\
\operatorname{MSE}_{\rm causal,3}&=1-r^\mathsf T w.
\end{aligned}
$$

最优误差与可用观测正交，给出权重约(0.515002,0.207254,0.096397)，总体MSE约0.257501 Pa²。它是使用三个当前/过去观测的因果解，不是假设能看到未来。[3](#ref-sp-wiener)

### 非因果谱解使用不同信息

若允许整个时间轴的观测，理想非因果Wiener谱解为H_nc=S_S/(S_S+S_V)，对应MSE为对S_S S_V/(S_S+S_V)的频率积分。本例约0.207514 Pa²，直接使用带噪观测的总体MSE为0.5 Pa²。

这些是已知模型下的总体风险，不是用图中真值调参后报告的一段样本分数。非因果解使用不同的信息范围，不能只比较MSE就声称它可在同样实时限制下替代三抽头因果滤波器。实际信号与噪声相关、统计未知或任务损失不同，解和评价都需改变。[3](#ref-sp-wiener)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/wiener-estimation.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/stochastic-processes/wiener-estimation.svg" alt="指定高斯AR加噪模型的因果估计片段与不同信息范围的总体MSE" width="1400" height="550" loading="lazy" /></a><figcaption>图7　模型参数预先给定，图中真值只用于显示，不用于估计参数或选择权重。右图MSE由正规方程或谱积分计算；理想全时域非因果解并非同样延迟约束下的算法，也未绘制其未来观测实现。</figcaption></figure>

## Poisson与Brownian 平稳增量不是状态平稳

### 事件计数与等待时间

齐次Poisson过程N(t)满足N(0)=0、不相交区间增量独立，长度Δt内的增量服从Poisson(λΔt)。因此E[N(t)]=Var(N(t))=λt，Cov(N(s),N(t))=λmin(s,t)。它有平稳增量，但计数状态本身不WSS；事件间隔为独立指数分布，平均1/λ。[9](#ref-sp-poisson)

图8的λ=20 s⁻¹只是教学事件率。把神经放电或声学事件建模成Poisson，需要检验刺激依赖、事件检测、不应期和历史影响；有不应期的模型通常不再具有相同的指数间隔结构。短时事件少，也不能随意以连续高斯噪声替代计数分布。

### Brownian的状态和增量

标准Brownian运动B(t)取B(0)=0、几乎必然连续的样本路径，具有独立平稳高斯增量，B(t+Δt)−B(t)服从N(0,Δt)。其均值为0，Cov(B(s),B(t))=min(s,t)，方差随t增长，故状态不WSS。[13](#ref-sp-brownian)

连续不意味着可按普通导数处理，标准Brownian样本路径几乎必然不可微；把理想白噪声称作它的导数，需要广义过程或随机积分意义。图中的网格高斯增量可复现有限时刻分布，但连线不是证明网格之间的真实路径可微，也未引入完整Itô微积分。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/poisson-brownian.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/stochastic-processes/poisson-brownian.svg" alt="Poisson事件计数路径与Brownian网格模拟路径" width="1400" height="550" loading="lazy" /></a><figcaption>图8　左图用独立指数等待时间生成事件，λ=20 s⁻¹，虚线是总体λt；右图步长0.001，以方差Δt的独立高斯增量生成并连线。二者都有平稳增量，计数或累积状态却不平稳，不是实测神经事件或粒子轨迹。</figcaption></figure>

## Markov性质与平稳初分布

Markov性质是“给定当前状态后，下一步的条件分布不再依赖更早历史”，并不是未来与过去无条件独立。状态可以离散也可以连续；一阶AR在所写独立创新条件下就是连续取值的Markov例子。[10](#ref-sp-markov)

对二状态、时间齐次链，本文按行定义Pᵢⱼ=Pr(S[n+1]=j|S[n]=i)，取

$$
\begin{aligned}
P&=\begin{bmatrix}0.95&0.05\\0.10&0.90\end{bmatrix},\\
\pi&=(2/3,1/3),\qquad\pi P=\pi.
\end{aligned}
$$

只有初态按π抽取等相应条件满足时，才从一开始处于平稳分布。固定从状态0开始，早期Pr(S[n]=1)会改变，虽然转移矩阵从未改变。该链有限、不可约且非周期，分布趋向唯一π；一般存在多个闭类或周期性时，不能照搬同样收敛结论。

把状态1记为指示变量，平稳均值为1/3，协方差为(2/9)·0.85^|k|。这再次表明Markov不等于相邻样本独立。若内部状态被噪声观测，观测序列本身还未必保持相同的Markov性；观测建模可与[计算神经科学](../computational-neuroscience/)及[机器学习](../machine-learning/)配合阅读。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/markov-stationarity.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/stochastic-processes/markov-stationarity.svg" alt="平稳初分布下的一条二状态链，以及两种固定初态的状态概率演化" width="1400" height="550" loading="lazy" /></a><figcaption>图9　转移矩阵按行定义，π=(2/3,1/3)。左图初态按π抽取；右图另固定初态0或1，用矩阵幂计算概率。相同时间齐次P并不意味着任意初态过程已平稳。</figcaption></figure>

## 有限记录 相关估计与谱估计

### 总体相关不等于有限求和

已知总体均值为0、记录x[0],…,x[N−1]时，k≥0的常见估计为

$$
\begin{aligned}
T[k]&=\sum_{n=0}^{N-k-1}x[n+k]x[n],\\
\widehat R_b[k]&=T[k]/N,\\
\widehat R_u[k]&=T[k]/(N-k).
\end{aligned}
$$

后者在这些已知零均值与WSS条件下逐滞后无偏，但大滞后可用项少。若先减去同一段记录估得的均值，无偏结论已改变。前者带有限长度权重，其镜像并在区间外置零的傅里叶级数等于有限序列DTFT平方模除以N，在DFT频点即非负的|DFT|²/N；逐滞后无偏却不自动保证同样零延拓后得到非负谱。[2](#ref-sp-psd)[15](#ref-sp-periodogram)

图10右图取x=[1,−1,1]，两种非负滞后估计分别[1,−2/3,1/3]和[1,−1,1]。镜像后区间外置零，后者的傅里叶级数在cosω=1/4处为−1.25。它说明的是有限估计和截断的性质，不是总体合法PSD可以为负。

### 周期图与Welch的取舍

每Hz密度形式的窗周期图分母为fₛΣw²；对矩形窗、关闭去均值的DFT，频率格点求和再乘Δf可由Parseval核对样本均方值。一般加窗或Welch积分对应的是相应加权与分段平均，不能无条件要求恰等于整段未加权方差。[15](#ref-sp-periodogram)

普通周期图增加总时长，并不普遍消除固定频率处的相对随机波动；Welch通过分段、加窗和平均降低某些波动，同时较短段长会改变谱平滑和分辨力。重叠段不独立，实际自由度不是简单把段数翻倍；一次估计更平滑也不等于总体模型已经正确。[14](#ref-sp-welch)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/stochastic-processes/finite-estimation.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/stochastic-processes/finite-estimation.svg" alt="同一AR实现的周期图与Welch谱，以及无偏相关估计零延拓后的负谱反例" width="1400" height="550" loading="lazy" /></a><figcaption>图10　左图N=8192，Welch用512点Hann、256点重叠，均关闭去均值；总体单侧曲线只在内部正频率画双侧的2倍。右图已知零均值、未减样本均值，对估计镜像并在未观测滞后置零，不把负值当作真实PSD。</figcaption></figure>

## 非平稳 循环平稳与实际研究

有限录音看起来“差不多”，不证明其联合统计时移不变。令X[n]=a[n]W[n]，W为独立零均值白噪声，若确定包络的平方a[n]²随时间改变，方差σ²a[n]²也会改变；若这个方差周期变化，可在相应条件下讨论二阶**循环平稳**，而非普通WSS。[1](#ref-sp-processes)

循环平稳是均值、相关等统计按周期重复，不等于每条波形完全重复。刺激锁定的重复试次、起音包络、设备漂移和状态转换都可能改变适合的模型；选择短窗“局部近似平稳”是一项需验证的分析选择，不是截窗便自动成立的定理。

单段PSD不能唯一恢复波形、全部依赖或机制；平坦谱也不证明独立，两个信号高相干也不证明直接因果。实际研究还需说明记录单位、时间对齐、独立重复单位、预处理、采样和参数估计的范围。可配合[频谱与功率谱密度](../spectrum-and-power-spectral-density/)进一步学习估计与声级细节。

## 三个可以独立运行的小实验

程序使用Python、NumPy与SciPy，已在Python 3.11、NumPy 1.26.4、SciPy 1.17.1运行。模拟中的总体分布和参数预先给定；数值检查不是实测拟合或外部专业评审。

### 一 相关样本的均值方差

直接从协方差矩阵与滞后求和分别计算，核对分母与非对角项。

```python
import numpy as np
from scipy.linalg import toeplitz
a, N = .8, 64
k = np.arange(1, N)
formula = (N+2*np.sum((N-k)*a**k))/N**2
covariance = toeplitz(a**np.arange(N))
matrix_result = np.ones(N) @ covariance @ np.ones(N) / N**2
assert np.isclose(formula, matrix_result)
print('AR variance of mean, iid value, mean-specific effective N:',
      formula, 1/N, 1/formula)
```

### 二 每Hz归一化与谱线积分

已知随机相位正弦模型，这里只固定一条实现来计算有限周期图；频点恰好对齐，关闭去均值。单侧峰高和频率间隔要一起解释。

```python
import numpy as np
from scipy.signal import periodogram
fs, f0 = 1000., 125.
for N in [256, 1024]:
    x = np.sqrt(2)*np.cos(2*np.pi*f0*np.arange(N)/fs+.7)
    f, S = periodogram(x, fs=fs, window='boxcar',
                       detrend=False, scaling='density')
    df = fs/N
    integral = S.sum()*df
    assert np.isclose(integral, np.mean(x*x))
    assert np.isclose(integral, 1.)
    assert np.isclose(S.max(), N/fs)
    print('N, peak Pa^2/Hz, integrated Pa^2:', N, S.max(), integral)
```

### 三 已知模型的三抽头因果Wiener解

只允许当前与过去两个观测，以总体协方差解权重；检查误差正交，不使用一段模拟真值调参。

```python
import numpy as np
from scipy.linalg import toeplitz
a, noise_variance, L = .8, .5, 3
r = a**np.arange(L)
R = toeplitz(r)+noise_variance*np.eye(L)
w = np.linalg.solve(R, r)
mse = 1-r @ w
assert np.allclose(R @ w-r, 0.)
assert np.isclose(mse, .2575009037233401)
assert mse < noise_variance
print('Causal coefficients, population MSE:', w, mse)
```

## 常见误解与阅读检查

| 容易混淆的说法 | 应核对的区别 |
| --- | --- |
| 一条录音就是整个随机过程 | 区分过程律、实现、固定时刻分布与有限记录 |
| 平稳意味着波形不变，也自动遍历 | 区分统计时移不变与指定时间平均的收敛 |
| 白噪声必独立，高斯只要边缘正态 | 白是二阶性质，高斯过程要求全部有限维联合高斯 |
| 所有WSS过程都有光滑PSD | 允许离散谱质量，说明普通密度存在条件 |
| 总平均N点总能按1/N降方差 | 把非零滞后协方差计入，明确等效样本数用途 |
| 稳定滤波器从第一个输出就平稳 | 核对全历史、随机初态与有限程序瞬态 |
| 时间齐次Markov链就是平稳链 | 同时核对初始分布、闭类与周期性 |
| 无偏相关估计总是更好的合法谱 | 检查有限截断、方差、半正定与非负谱要求 |
| 相干为1或非因果MSE更小就可直接部署 | 核对平均、可用信息、未来样本与任务评价 |

读完应能写清随机过程的联合假设，区分平稳与指定意义的遍历，复算相关平均、LTI输出谱和因果Wiener解，并说明采样、单位与有限估计的限制。本文完成定义、来源、解析、数值及页面核查，保留AI辅助草稿与专业审阅待完成标记。
