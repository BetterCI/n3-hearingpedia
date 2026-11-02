---
title: "小波分析"
english: "Wavelet Analysis"
slug: "wavelet-analysis"
summary: "从局部变化与多尺度观察进入连续小波、尺度频率换算、多分辨分析、离散小波和完全重建滤波器组，再理解边界、消失矩、双正交、平稳小波、小波包与阈值去噪；以可手算和可运行例子核查声音时频图、能量、相干和显著性的解释边界。"
categories: ["research-methods", "signal-processing", "acoustics"]
tags: ["基础课程", "小波分析", "连续小波变换", "离散小波变换", "多分辨分析", "滤波器组", "小波去噪", "小波包"]
aliases: ["小波", "小波变换", "Wavelets", "Wavelet Transform", "多分辨分析"]
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
  - {label: "课程定位", value: "与信号与系统、数字信号处理配套，深入局部多尺度表示与重建"}
  - {label: "核心区分", value: "连续与离散、尺度与频率、正交与双正交、可重建与去噪有效分别判断"}
  - {label: "声音连接", value: "扫频、短暂振荡、起始变化与多分辨率前端；需检查边界、单位及延迟"}
  - {label: "解释边界", value: "小波亮纹不自动代表真实周期、显著事件、生物通道或因果关系"}
references: ["wa-mallat", "wa-daubechies", "wa-torrence", "wa-coherence", "wa-pitfalls", "wa-scattering", "wa-donoho", "wa-wavelets", "wa-cwt", "wa-dwt", "wa-idwt", "wa-boundary", "wa-swt", "wa-iswt", "wa-packets", "wa-threshold", "wa-coefficients"]
order: 1021
---

**小波分析**（wavelet analysis）用一族具有局部性的分析函数，在不同位置和尺度上描述信号。它关注“某种变化出现在什么时候、持续多宽、在什么尺度上明显”，也研究怎样把这些描述合成为原信号。小波不只是画彩色时频图的方法；正交基、多分辨空间、快速滤波器组和非线性系数处理同样是这门课的核心。[1](#ref-wa-mallat)[2](#ref-wa-daubechies)

本篇与[信号与系统](../signals-and-systems/)、[数字信号处理](../digital-signal-processing/)配套：前两篇建立变换、采样、卷积和数字滤波基础，这里进一步说明多尺度表示为何成立、哪些条件保证重建，以及有限数据怎样影响解释。不需要先通读配套课程；内积、复数、归一化和下采样会在使用处解释。十幅图及数值都是原创指定模型或模拟，不是听者、耳蜗、神经信号或真实语音基准的实测。

声音中的起音、扫频和短暂振荡便于理解局部分析，但小波也用于图像、偏微分方程与数值计算。本文不以“小波比傅里叶先进”作为前提：工具是否适合，取决于信号、任务、精度、延迟和评价方法。文末有三个短程序，另有[完整实验脚本](/n3-hearingpedia/code/wavelet-analysis/experiments.py)。

## 阅读准备与独立阅读

**起步知识。** 知道函数描述输入输出、采样把连续量记录成一串数、平均与差可以突出不同变化，就能开始。第一遍先看母小波、尺度、Haar手算和去噪图；连续积分与空间分解可第二遍读。

**随用随补。** 向量是一组数，内积是对应相乘后求和；连续函数的内积把求和换成积分。平方和衡量有限序列的能量，正交表示不同模板内积为零。复数同时保存两个实数分量，星号表示复共轭；本篇会说明它在相关计算中的位置。

**分层阅读。** 先建立“模板—系数—重建”的主线，再读尺度频率、滤波器组与边界，最后进入统计推断和应用选择。需要扩展时可查[线性代数](../linear-algebra/)、[微积分](../calculus/)、[数学物理方法](../mathematical-physics-methods/)和[泛函分析](../functional-analysis/)；理解噪声模型时按需查[概率论](../probability-theory/)与[数理统计](../mathematical-statistics/)，不把整门课列为入门门槛。

## 从局部变化理解母小波

### 模板与系数

把分析函数看作一个模板：信号在某一位置附近的形状与模板越一致，内积的绝对值可能越大；反向一致则可能得到负值。系数同时受到信号幅度、模板宽度与归一化影响，不能只凭“大系数”断言存在某种物理声源。复系数的模给出大小，辐角给出相对于模板约定的相位。

**母小波**是生成整族分析函数的原型。Haar母小波在0至1/2取1，在1/2至1取−1，其余为0，最直接地比较相邻两段。**Mexican hat**母小波为

$$
\psi(u)=\frac{2}{\sqrt3\,\pi^{1/4}}(1-u^2)e^{-u^2/2}.
$$

它有一个中心瓣和两侧反号瓣，与高斯函数的二阶导数有关；它强调局部曲率式变化，不是只识别一种固定频率的纯正弦。Haar具有紧支撑但不光滑，Mexican hat和Morlet则具有快速衰减的尾部，不能说所有小波都在有限区间外严格为零。[8](#ref-wa-wavelets)

**零均值**指∫ψ(u)du=0：正负部分抵消，使模板不响应无限域上的常数背景。实际有限记录中的端点截断或延拓仍可能产生非零响应。零均值也不能单独替代后面的可容许性条件，尤其不能忽略频域原点附近的收敛性质。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/mother-wavelets.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/wavelet-analysis/mother-wavelets.svg" alt="Haar阶跃、Mexican hat正负瓣和修正Morlet实虚部三种母小波" width="1400" height="550" loading="lazy" /></a><figcaption>图1　横轴为无量纲自变量；三种母小波均按文中定义生成。Haar的不连续、Mexican hat的曲率式形状与Morlet的局部振荡反映不同分析偏好，不表示听觉系统的实测滤波器。</figcaption></figure>

### 尺度与平移怎样改变模板

本文令尺度a>0，位置b为实数，采用L²归一化：

$$
\begin{aligned}
\psi_{a,b}(t)&=\frac1{\sqrt a}\psi\!\left(\frac{t-b}{a}\right),\\
W_x(a,b)&=\int_{-\infty}^{\infty}x(t)\psi_{a,b}^{*}(t)\,dt.
\end{aligned}
$$

**平移**b移动模板中心或参考位置；**尺度**a伸缩模板。a变大，模板在时间上更宽、振荡更慢；a变小则更窄、更快。前面的1/√a使模板的平方积分不随尺度改变：换元u=(t−b)/a便有∫|ψₐ,ᵦ|²dt=∫|ψ|²du。若改用1/a归一化，系数数值及其尺度比较会改变，应明确采用哪一种。

## 连续小波变换 怎样理解可逆与能量

### 连续是参数连续，不是电脑不会采样

上式定义**连续小波变换**（CWT）。数学定义允许a、b连续变化；计算机输出的是在指定尺度和时间网格上的近似采样。把尺度网格加密会增加冗余与运算量，并不会无限创造新的独立信息。有限长度信号还需要规定区间外如何处理。[9](#ref-wa-cwt)

“小波变换”并不只有一条统一公式：实小波和复小波、连续与离散、能量与幅度归一化各有约定。下面的能量及反演公式**限定为实母小波**，避免把正负频率常数与后面的复Morlet计算混用。

### 可容许常数的约定

取傅里叶变换Ψ(ω)=∫ψ(t)e^(−iωt)dt，其中ω是角频率。对非零实母小波，定义正频率可容许常数

$$
0<C_\psi=\int_0^\infty\frac{|\Psi(\omega)|^2}{\omega}\,d\omega<\infty.
$$

当x、ψ满足相应L²条件时，有

$$
\begin{aligned}
&\int_0^\infty\int_{\mathbb R}|W_x(a,b)|^2\,db\,\frac{da}{a^2}\\
&\qquad=C_\psi\int_{\mathbb R}|x(t)|^2\,dt,\\
&F_a(t)=\int_{\mathbb R}W_x(a,b)\psi_{a,b}(t)\,db,\\
&x(t)=\frac1{C_\psi}\int_0^\infty F_a(t)\,\frac{da}{a^2}.
\end{aligned}
$$

Fₐ先合成同一尺度下的平移分量，再沿尺度积分。反演应按L²收敛或适当附加正则条件理解，不能保证任意信号的任意逐点积分都绝对收敛。实小波的正负频率模对称；若另把全频率积分称作可容许常数，其值是这里的两倍，反演前因子也要相应改变。复小波的正负频率贡献未必相等，不能直接照搬这个实小波版本。[1](#ref-wa-mallat)[2](#ref-wa-daubechies)

对上文Mexican hat，Ψ(ω)=A√(2π)ω²e^(−ω²/2)，其中A=2/(√3π^(1/4))，由此Cψ=4√π/3≈2.36327。这个可复算例子同时说明：可容许性检查的是带1/ω权重的频域积分，而不只检查一幅波形有没有正负瓣。

### 单位与图上的颜色

若时间和尺度以秒计、输入x为Pa，则W的单位为Pa·√s，|W|²为Pa²·s。它不是不经进一步约定便得到的功率谱密度，更不是声压级；连续变换的能量积分还包含db·da/a²。图上的10log₁₀(|W|²/P₀)必须交代P₀，以及比较的是单张图最大值、某个参考系数功率，还是其他量。有关谱的区分可参照[频谱与功率谱密度](../spectrum-and-power-spectral-density/)。

## 时间与频率为什么不能同时无限精细

对于同一母小波族，尺度增大时，时间宽度大致随a增大，频率宽度则随1/a缩小。因此高频通常获得较短时间窗，低频通常需要较长观察；这是特定结构的取舍，不是所有信号在所有尺度都能自动得到最佳分辨率。[3](#ref-wa-torrence)

若采用能量归一的时间、角频率二阶矩，并且两个方差有限，不确定性关系写作σₜσ_ω≥1/2。这个式子的条件不能省略：Haar虽有有限时间支撑，其频率二阶矩并不有限，不能把它硬塞进同一有限方差计算。小波图的像素大小也不等于实际时间频率分辨率。

短时傅里叶变换常使用固定窗长，适合需要一致时间窗的任务；小波使用随尺度改变的模板宽度，适合关注跨尺度局部结构的任务。两者都可设计冗余表示、重建方案及不同窗口，不能概括为“傅里叶只有频率、小波才有时间”。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/scale-localization.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/wavelet-analysis/scale-localization.svg" alt="同一Morlet在三个尺度下伸缩，以及多尺度时间宽度的示意格子" width="1400" height="550" loading="lazy" /></a><figcaption>图2　左图保持1/√a归一化，变宽伴随峰值降低；右图只说明时间宽度随尺度变化的结构，不是正交CWT网格，也不是实际滤波器的砖墙通带或听觉带宽测量。</figcaption></figure>

## 尺度怎样换算成频率 声音例子

### 用哪一种Morlet

Morlet常写成高斯窗乘复振荡e^(iω₀u)。单纯相乘的形式一般不严格零均值。本篇用ω₀=6、精确零均值修正和单位L²归一化：

$$
\begin{aligned}
\psi(u)&=\frac{\pi^{-1/4}}N\left(e^{i\omega_0u}-e^{-\omega_0^2/2}\right)e^{-u^2/2},\\
N^2&=1+e^{-\omega_0^2}-2e^{-3\omega_0^2/4}.
\end{aligned}
$$

N在ω₀=6时非常接近1，但仍在代码中保留。不同软件的Morlet参数、带宽和中心频率命名不一定相同；本文的ψ不能仅凭名称就等同于库中的任意`cmorB-C`。[3](#ref-wa-torrence)[9](#ref-wa-cwt)

### 等效频率是一种明确的换算

对ω₀=6，图3使用Torrence–Compo的Morlet尺度—傅里叶周期换算：

$$
P=\frac{4\pi a}{\omega_0+\sqrt{\omega_0^2+2}},\qquad
f_{\rm eq}=\frac{\omega_0+\sqrt{\omega_0^2+2}}{4\pi a}.
$$

它对应未修正Morlet窄带近似下的正弦响应脊线约定；ω₀=6时本文零均值修正的影响很小。母小波频谱峰值除以尺度的换算ω₀/(2πa)与此略有不同，不能隐去差别。实际信号由多个分量、包络和噪声叠加，其系数最大位置也不必正好落在某一个瞬时频率上。[3](#ref-wa-torrence)

**采样尺度**还要换回秒。若库中的scale以采样间隔为单位，物理尺度为a=scale·Δt；PyWavelets的`sampling_period`调整返回频率，不会自动把系数乘上物理积分所需的√Δt。匹配尺度和归一化后，这个因子连接采样单位与物理L²单位；库的积分小波离散化与本文直接卷积求积并非逐点完全相同。[9](#ref-wa-cwt)

### 扫频和短振荡能看到什么

图3设采样率1024 Hz、记录长2 s，叠加20→120 Hz线性扫频和1.3 s附近的100 Hz高斯包络短振荡。短振荡不可能在频率轴上只占一条无限细线，扫频也会受时间窗平均；二者重合时，CWT的线性叠加和功率中的交叉项会改变颜色，不能直接把亮度分配给各个声源。

图中a以秒计，采用Δt加权卷积近似积分，在记录外补零。淡色区按边缘距离小于√2a标记，是选定Morlet影响锥风格的边界约定，**不是误差超过某个阈值的严格证明**。越靠低频，时间支持越宽，短记录的可用内部区可能越少。[3](#ref-wa-torrence)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/sound-cwt.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/wavelet-analysis/sound-cwt.svg" alt="扫频和100赫兹短振荡的波形与修正Morlet小波图，边缘用淡色表示" width="1400" height="750" loading="lazy" /></a><figcaption>图3　128个等效频率从15到160 Hz按几何间隔取样；图示10log₁₀(系数功率/全图最大值)，下限−40 dB。零延拓、L²归一化与所选影响锥均已明确；颜色不是声压级、PSD或统计显著性。</figcaption></figure>

## 多分辨分析 从粗略描述到细节空间

### 近似空间与细节空间

**多分辨分析**（MRA）组织一列嵌套的近似空间。选择“j增大表示分辨率提高”的理论约定，尺度函数平移伸缩为φⱼ,ₖ(t)=2^(j/2)φ(2ʲt−k)，相应空间满足Vⱼ⊂Vⱼ₊₁。正交情形下

$$
V_{j+1}=V_j\oplus W_j.
$$

Vⱼ保存较粗近似，Wⱼ保存从粗到细新增、且与Vⱼ正交的细节；符号⊕表示正交直和。尺度函数负责近似，小波函数负责细节，不是同一个对象。完整MRA还有缩放、平移、稠密性及交空间等要求，仅画嵌套方框不等于证明存在正交小波基。[1](#ref-wa-mallat)

“细节”并不等于噪声。细节空间可能含真正的声学起音、尖峰或变化点；近似空间也可能含低频噪声。是否保留要由任务决定，而不是把高频统一删除。

### 理论下标与软件层号

常见离散分解从有限采样序列出发，做一次低通、高通和二倍降采样；再分解低通近似。软件的分解层数J越大，最终近似越粗，典型时间尺度约增加为2ᴶ个采样间隔。它与上面理论“j越大越精细”的方向相反，是索引约定不同，不能把两个j不加说明地替换。[10](#ref-wa-dwt)

**离散小波变换**（DWT）使用离散尺度与平移构造表示，正交或双正交基需要满足相应结构条件。任意挑选若干CWT尺度和时间点，得到的只是离散采样的CWT，不自动成为正交DWT。有限长度边界处理也会影响系数数目和有限矩阵的性质。

## Haar离散小波 一组可以完全手算的数

### 归一化的平均与差

对相邻输入x₂ₖ、x₂ₖ₊₁，定义

$$
\begin{aligned}
a_k&=\frac{x_{2k}+x_{2k+1}}{\sqrt2},\\
d_k&=\frac{x_{2k}-x_{2k+1}}{\sqrt2},\\
x_{2k}&=\frac{a_k+d_k}{\sqrt2},\\
x_{2k+1}&=\frac{a_k-d_k}{\sqrt2}.
\end{aligned}
$$

aₖ是按√2缩放的成对平均，不是通常除以2的算术平均；dₖ是归一化差。这一对变换保持平方和：aₖ²+dₖ²=x₂ₖ²+x₂ₖ₊₁²。保留a和d便能重建，保留a而丢弃d通常不能。

给定x=[4,6,10,12,8,8,2,2]，第一层A₁=[5√2,11√2,8√2,2√2]，D₁=[−√2,−√2,0,0]；继续只分解A：A₂=[16,10]，D₂=[−6,6]，A₃=[13√2]，D₃=[3√2]。多层完整系数按[A₃,D₃,D₂,D₁]排列。[10](#ref-wa-dwt)[17](#ref-wa-coefficients)

### 有限矩阵与Parseval等式

把这个八点分析写为c=Ux，U的各行是归一正交模板，UᵀU=I，因此x=Uᵀc，且Σxₙ²=Σcₖ²=432。这是有限正交变换的Parseval等式。若要近似连续时间能量，还应考虑采样间隔Δt；有限向量平方和与Pa²·s不是无条件同一个量。

单位也要区分：有限离散正交矩阵是无量纲权重，系数与输入具有相同单位；前文以秒为尺度定义的连续L²系数则含√s。二者都叫“小波系数”，并不表示可以忽略单位直接比较。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/haar-decomposition.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/wavelet-analysis/haar-decomposition.svg" alt="八点Haar正交矩阵与按近似和各级细节排列的系数" width="1400" height="550" loading="lazy" /></a><figcaption>图4　每行是一个分析模板，按A₃、D₃、D₂、D₁排列。输入平方和与系数平方和均为432；系数全部保留可重建。正交性与能量等式针对此处明确构造的有限矩阵。</figcaption></figure>

## 两通道滤波器组 为什么降采样后还能重建

### 分析与合成

分析端分别用低通H₀和高通H₁滤波，再各保留每两个样本中的一个；合成端先插零升采样，再用G₀、G₁滤波并相加。一级两支合起来的样本数可与输入相同，但某一支单独降采样后可能发生混叠。完全重建依靠合成时的混叠抵消，不要求每支独自无混叠。[1](#ref-wa-mallat)[11](#ref-wa-idwt)

在固定的二倍抽取/插零相位约定下，z域输出为

$$
\begin{aligned}
2T(z)&=G_0(z)H_0(z)\\
&\quad+G_1(z)H_1(z),\\
2A(z)&=G_0(z)H_0(-z)\\
&\quad+G_1(z)H_1(-z),\\
Y(z)&=T(z)X(z)+A(z)X(-z).
\end{aligned}
$$

A(z)X(−z)是混叠项。若A(z)=0且T(z)=z^(−d)，则输出是输入延迟d点。其他实现可能还包含增益，必须一并校准。这里是复传递函数相加后抵消，不是把两条幅度响应相加便一定得到常数。

### Haar的一个明确滤波约定

图5使用因果FIR H₀=[1,1]/√2、H₁=[−1,1]/√2，G₀=H₀、G₁=−H₁，滤波后保留偶数索引，循环边界。直接代入可得混叠项为零，总输出恰好延迟1点。前面的成对手算法和库函数可能选择不同对齐及裁切，细节符号也可能不同；这些区别不能被误报为不可重建。

如果分析后改了细节系数，即使仍用正确合成滤波器，重建的也通常是另一个信号。**完全重建滤波器组**描述不改系数时的分析合成性质，**去噪**则是有意改变系数并承担偏差，不能以“滤波器组可重建”证明去噪无损。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/filterbank-reconstruction.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/wavelet-analysis/filterbank-reconstruction.svg" alt="低通和高通合成支路以及它们相加后与一采样延迟输入的对照" width="1400" height="550" loading="lazy" /></a><figcaption>图5　输入为128点中8与48周的两个余弦；采用文中因果Haar滤波器、偶相位抽取和循环边界。单支路不等于独立无混叠原分量；总和与延迟输入的最大差约为浮点舍入量级。</figcaption></figure>

## 消失矩 正交与双正交怎样选择

### 消失矩为何使平滑区系数变小

若小波满足∫tᵏψ(t)dt=0，k=0,…,m−1，并且有关矩存在，称其有m个**消失矩**。它与次数小于m的多项式在合适范围内正交；局部光滑函数可近似成低阶多项式，因此较细尺度内部的某些细节系数会较小。这是局部逼近性质，不表示所有平滑信号的所有细节都严格为零。[2](#ref-wa-daubechies)

有限序列必须避开受延拓影响的边缘；全实线上的非零多项式也不是L²信号，不能把多项式测试不加说明地当成上述L²反演定理的输入。图9比较有限三次多项式的内部一级系数，`db4`的四个消失矩给出接近舍入误差的结果，Haar只有一个消失矩则不会消去一般斜率和曲率。

**命名注意。** PyWavelets的`db4`有4个消失矩、8个滤波器抽头；一些文献里的“D4”按4抽头命名，对应的通常是这里的`db2`。选库时应核对系数表，不能只看名字里的数字。[8](#ref-wa-wavelets)

### 不把几个属性混成一个

**正交**表示同一组分析/合成基之间的内积结构，常带来普通系数平方和的能量保持。**双正交**使用互为对偶的分析与合成函数族，可完全重建，但一般不保持普通系数平方和。部分常用双正交族能提供对称滤波器，适合关心线性相位的任务；不能据此断言所有双正交小波都对称，也不能说正交必然意味着线性相位。

图9指定随机向量的`bior4.4`系数平方和/输入平方和约1.03448，但重建最大差约5.2×10⁻¹²；它展示“不保持普通能量等式”与“不能重建”不同。更长滤波器和更多消失矩可能改善某些逼近，同时扩大支持、增加端点影响与实现延迟，不存在仅凭一个参数决定的全局优胜者。[8](#ref-wa-wavelets)

## 边界与移位 为什么同一瞬态会变样

### 记录之外并没有观测值

zero把区间外设为零，symmetric按规定对称反射，periodization采用有利于最小系数数目的周期化处理。`periodic`与`periodization`在PyWavelets中是不同模式，不能仅凭中文都叫“周期”就互换。分析和合成应使用一致的模式，输出长度与裁切也要记录。[12](#ref-wa-boundary)

图6的斜坡只保留三级近似后重建，不同模式在端点给出不同结果。其差异来自区间外的假设，不能直接当作真实低频变化。对于很短的声音片段，分解过深会使多数系数受到边界影响；库的最大有用分解层数是避免全部落入边缘的一种实现准则，不是“数学上再分一层就绝对禁止”。[10](#ref-wa-dwt)

### 平稳小波以冗余换取移位一致性

降采样DWT对齐不同，系数会变化；经阈值处理再重建，移动输入1点后再移回，结果可能不同。完整DWT不改系数则始终重建输入，本身没有这个去噪差异。**平稳小波变换**（SWT，也称不降采样小波的一类实现）每级保留时间位置，并使滤波器随层数扩展，代价是冗余。[13](#ref-wa-swt)

图6在循环边界、固定逐系数软阈值下比较：SWT处理对整数循环移位等变，DWT处理则出现差异。这里的等变指输入移位，输出也跟着相同移位；不意味着所有边界处理、任意移位、任何自适应阈值都严格一致。PyWavelets的SWT要求长度能被2ᴶ整除，分析与`iswt`合成的`norm`约定也要配对。[14](#ref-wa-iswt)

SWT的能量等式不能无条件照搬正交DWT。在PyWavelets中，正交小波、`norm=True`和`trim_approx=True`同时成立时，所返回的最终近似与各级细节才具有所述能量分配性质；冗余系数的噪声还会相关，不能当作额外获得同样多的独立样本。[13](#ref-wa-swt)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/boundary-shift.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/wavelet-analysis/boundary-shift.svg" alt="不同延拓的斜坡近似，以及DWT与SWT阈值处理的循环移位差" width="1400" height="550" loading="lazy" /></a><figcaption>图6　左图db4三级，只保留A₃；右图Haar三级、固定软阈值0.2，比较原处理与输入循环右移1点处理再移回。SWT使用norm=False并匹配合成；此处的移位结论限定为循环边界与给定处理。</figcaption></figure>

## 阈值去噪 噪声模型和偏差都要说明

### 从稀疏表示到收缩

若有些信号在小波域中主要集中于少量大系数，而噪声分散在很多系数中，可尝试收缩细节。但这是假设，需要结合任务检验；真实高频或弱小事件也可能具有小系数。硬阈值保留超过阈值的系数，软阈值则把保留的系数再向零缩小：[16](#ref-wa-threshold)

$$
\begin{aligned}
T_{\rm hard}(d)&=d\,\mathbf1_{\{|d|>\lambda\}},\\
T_{\rm soft}(d)&=\operatorname{sgn}(d)\max(|d|-\lambda,0).
\end{aligned}
$$

硬阈值在门槛处不连续，软阈值连续但有收缩偏差。在独立同方差高斯噪声和有限正交变换模型下，噪声系数仍为同方差高斯；常见**通用阈值**λ=σ√(2lnN)由高斯噪声最大系数的控制思路得到。它不是任意噪声、任意样本量与任意损失下的最优保证，也不表示所有真实系数都不受损。[7](#ref-wa-donoho)

σ未知时常用最细层细节的稳健估计：σ̂=median(|D₁−median(D₁)|)/0.67448975。分母来自标准正态绝对偏差的中位数。若最细层含大量真实变化、噪声有色或系数相关，这个估计及单一阈值的解释会改变；可按尺度建模、采用其他风险准则或利用独立噪声记录，但必须报告选择方法。

### 一个有明确真值的模拟

图7为1024点分段常数加高斯小凸起，采样率1024 Hz，噪声标准差0.2，随机种子20261102。采用db4四级、periodization、仅修改细节，得到σ̂≈0.20196，λ≈0.75196。相对已知无噪声教学真值的均方误差为：带噪0.040463、软阈值0.005715、硬阈值0.004778。

这个指定例子中硬阈值MSE较低，不证明它对其他信号、噪声或听觉任务更好。真实录音通常没有无噪声真值，不能把重建与带噪输入“越像越好”当作去噪评价；语音可懂度、听感、目标事件保留、失真和延迟需要与任务相符的独立评价。分贝改善也不能未经定义由这一列MSE直接推出。[16](#ref-wa-threshold)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/threshold-denoising.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/wavelet-analysis/threshold-denoising.svg" alt="带噪教学信号与软阈值重建，以及硬阈值和软阈值的系数映射" width="1400" height="550" loading="lazy" /></a><figcaption>图7　仅一个给定种子的模拟，真值用于评价而未用于估计σ或调阈值。软阈值降低此例MSE同时改变跳变和弱信号；右图门槛与偏差揭示修改系数的代价，不是临床或语音基准效果。</figcaption></figure>

## 小波包 不只分解低频支路

标准多层DWT继续分解近似支路，形成不同宽度的名义频带。**小波包**允许把低通和高通两支继续递归分解，形成更丰富的树；同一层的完整正交包基可以有相同名义带宽。选择不同树相当于选择不同表示，应说明选择准则及数据划分。[15](#ref-wa-packets)

节点字符串里的a、d表示沿树经过近似/细节支路，不是频率数值。高通及抽取造成频率折叠，节点的自然字母顺序并不等于频率递增顺序。PyWavelets的`get_level(3, order='freq')`对这里的三级树给出aaa、aad、add、ada、dda、ddd、dad、daa。

图8设fs=1024 Hz，三级的8个名义区间宽64 Hz。160 Hz纯音的最大节点是名义128–192 Hz的add，但能量也出现在其他节点；Haar实际响应宽且重叠，不能当作理想砖墙分带。把“节点能量”命名为某个听觉通道或生物频带，还需要额外的模型与测量依据。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/wavelet-packets.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/wavelet-analysis/wavelet-packets.svg" alt="三级小波包频率顺序的八个名义区间，以及160赫兹纯音的节点能量比例" width="1400" height="550" loading="lazy" /></a><figcaption>图8　Haar、periodization、1024点输入，完整三级正交包树。名义频带只用于组织索引；纯音最大能量在add，但响应泄漏到其他节点，不能把每个节点视为理想互不重叠的带通。</figcaption></figure>

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/moments-biorthogonal.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/wavelet-analysis/moments-biorthogonal.svg" alt="三次多项式的内部一级细节，以及db4与bior4.4系数平方和的比较" width="1400" height="550" loading="lazy" /></a><figcaption>图9　左图使用零延拓但只绘制远离边缘的位置；db4消去三次多项式的内部细节至舍入量级。右图为指定随机向量和周期化三级分解；双正交普通系数平方和不保持输入能量，仍可精确到数值误差地重建。</figcaption></figure>

## 小波相干与显著性 亮纹不是结论

### 交叉小波与相干需要区分

对两个变换Wₓ、Wᵧ，**交叉小波**Wₓᵧ=WₓWᵧ*保留共同系数幅度与相位差，但幅度大可能由一个信号的大功率推动，不自动说明归一化关联强。常见小波平方相干采用时间与尺度的平滑算子S：[4](#ref-wa-coherence)

$$
R^2(a,b)=\frac{|S(a^{-1}W_{xy})|^2}
 {S(a^{-1}|W_x|^2)\,S(a^{-1}|W_y|^2)}.
$$

平滑核、尺度权重和边界处理是定义的一部分；分母为零的地方应作为无效值处理。若根本不平滑，直接计算|WₓWᵧ*|²/(|Wₓ|²|Wᵧ|²)，只要两者非零就恒为1，不能用来测关联。适当正权平滑下的相干反映局部归一化关系，仍受共同输入、处理滤波、时间对齐及噪声影响。

相位箭头的方向取决于复共轭、信号顺序和绘图坐标；在某个频率上的相位差也可能相差整周，不能不加假设地除以2πf便得到唯一传播时延。相干或相位领先本身更不证明因果方向。[5](#ref-wa-pitfalls)

### 噪声背景 端点与多重比较

图10左侧输入只有独立高斯噪声，却仍形成局部亮纹。单张图以最大值归一化，即使绝对信号很弱也会有“最亮处”。要讨论显著性，必须先说明白噪声、红噪声或其他背景模型、参数估计方式、检验统计量以及平滑后的自由度，不能对所有小波和所有预处理统一套一个χ²门槛。[3](#ref-wa-torrence)[5](#ref-wa-pitfalls)

若m次检验相互独立、零假设均为真且单次假阳性率0.05，至少一次假阳性的概率为1−0.95ᵐ；m=100时约0.99408。这个算例只说明重复查看的风险，**不是相关小波像素的有效检验次数公式**。真实时频系数相关，检验范围、校正策略或模拟零分布应匹配实际分析；相邻一片亮区也不是同样数量的独立重复证据。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/wavelet-analysis/noise-inference.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/wavelet-analysis/noise-inference.svg" alt="纯高斯噪声也形成局部小波亮纹，以及独立重复检验的假阳性概率" width="1400" height="550" loading="lazy" /></a><figcaption>图10　左图为种子812的2048点高斯噪声，沿用图3尺度及相对功率显示。右图严格限定为相互独立、全部零假设为真的检验；不据此计算时频像素自由度或实际簇显著性。</figcaption></figure>

## 与声音研究 数值方法和深度学习的联系

**声音与听觉。** 可用CWT探索短暂振荡、起始变化或多尺度调制，用DWT/小波包建立特征和压缩，用SWT减少某些对齐敏感性。小波尺度、[听觉滤波器](../auditory-filter/)带宽与神经时间尺度是不同定义的量；相似的图形只提供比较线索，不能默认存在一一生物对应。对耳蜗或神经数据还应核对刺激、采样、伪迹、跨试次对齐和独立观测单位。

**数值与表示。** 局部支撑和消失矩可支持稀疏逼近、局部细化及某些算子的高效表示；要区分函数逼近误差、离散误差、阈值截断误差与求解器误差。小波使某些问题稀疏，不表示任何矩阵都自动稀疏或条件数必然改善，可与[数值分析](../numerical-analysis/)配合阅读。

**深层表示。** 散射变换用固定小波滤波、模运算和平均逐层构造表示，其稳定性和不变性依赖具体定义及假设；它与所有滤波器都由任务训练的网络并不相同，也不意味着完全不需要学习最终任务映射。将小波输入[机器学习](../machine-learning/)或[深度学习](../deep-learning/)模型时，母小波、层数、特征筛选和阈值都应在训练/验证边界内选择，最终性能由独立数据评估。[6](#ref-wa-scattering)

**实时实现。** 居中CWT往往使用位置b两侧的样本，不能仅凭运行很快就称为零前视实时系统。有限滤波器支持、缓冲、分解层数、降采样相位和合成延迟都要计入。离线截取一小段后补零，与连续流处理中保留真实历史和未来上下文的结果也可能不同。

## 三个可以独立运行的小实验

以下短程序使用NumPy与PyWavelets，完整脚本另使用SciPy。本文以Python 3.11、NumPy 1.26.4、SciPy 1.17.1、PyWavelets 1.8.0运行核查。引用的stable文档是核查日期快照；较新CWT接口中的参数不代表本地1.8.0也支持，三个例子均采用已验证的共同接口。

### 一 八点Haar手算与库函数互相核对

不需要绘图，先看系数、重建和能量。`wavedec`返回[A₃,D₃,D₂,D₁]，此处Haar约定与前面的成对手算一致。

```python
import numpy as np
import pywt
x = np.array([4., 6., 10., 12., 8., 8., 2., 2.])
c = pywt.wavedec(x, 'haar', mode='periodization', level=3)
expected = np.array([13*np.sqrt(2), 3*np.sqrt(2), -6, 6,
                     -np.sqrt(2), -np.sqrt(2), 0, 0])
assert np.allclose(np.concatenate(c), expected)
y = pywt.waverec(c, 'haar', mode='periodization')
assert np.allclose(y, x)
assert np.isclose(sum(v @ v for v in c), x @ x)
print('Haar coefficients:', np.concatenate(c))
print('Input and coefficient energies:', x @ x, sum(v @ v for v in c))
```

### 二 有真值的软硬阈值比较

固定参数先处理，再以教学真值评价；不使用真值挑阈值。读者可以改变噪声种子、增加弱瞬态或有色噪声，观察排序是否改变。

```python
import numpy as np
import pywt
n = 1024
t = np.arange(n) / 1024
clean = ((t >= .2) & (t < .5)).astype(float)
clean -= .5 * ((t >= .5) & (t < .75))
clean += .5 * np.exp(-.5 * ((t - .63) / .015)**2)
noisy = clean + np.random.default_rng(20261102).normal(0, .2, n)
c = pywt.wavedec(noisy, 'db4', mode='periodization', level=4)
sigma = np.median(np.abs(c[-1] - np.median(c[-1]))) / .6744897501960817
threshold = sigma * np.sqrt(2*np.log(n))
print('sigma, threshold:', sigma, threshold)
print('noisy MSE:', np.mean((noisy-clean)**2))
for mode in ['soft', 'hard']:
    modified = [c[0]] + [pywt.threshold(v, threshold, mode=mode) for v in c[1:]]
    y = pywt.waverec(modified, 'db4', mode='periodization')[:n]
    print(mode, 'MSE:', np.mean((y-clean)**2))
```

### 三 小波包的名字 顺序和能量

明确调用频率顺序，并用纯音检查实际能量分布，而不是假设节点就是理想通带。

```python
import numpy as np
import pywt
t = np.arange(1024) / 1024
x = np.cos(2*np.pi*160*t)
wp = pywt.WaveletPacket(x, 'haar', mode='periodization', maxlevel=3)
nodes = wp.get_level(3, order='freq')
energy = np.array([np.sum(node.data**2) for node in nodes])
assert [node.path for node in nodes] == ['aaa', 'aad', 'add', 'ada',
                                        'dda', 'ddd', 'dad', 'daa']
assert np.isclose(energy.sum(), x @ x)
assert nodes[int(energy.argmax())].path == 'add'
for i, node in enumerate(nodes):
    print(node.path, f'nominal {64*i}-{64*(i+1)} Hz', energy[i]/energy.sum())
```

## 常见误解与阅读检查

| 容易混淆的说法 | 应怎样核查 |
| --- | --- |
| 尺度就是频率 | 核对母小波、尺度单位、采样周期与中心频率或脊线换算约定 |
| 小波都紧支撑，零均值就足够 | 区分紧支撑和快速衰减；检查可容许积分及矩条件 |
| 彩图越密，独立信息越多 | 区分显示网格、冗余、物理分辨率与统计自由度 |
| DWT是随便取一些CWT点 | 核对基/对偶结构、抽取格点、边界及重建条件 |
| 所有小波系数平方和都等于信号能量 | 区分正交、双正交、冗余变换、归一化及时间单位 |
| 完全重建所以去噪无损 | 比较改系数之前的PR性质与改系数后的偏差 |
| 高频细节都是噪声 | 检查目标瞬态、弱事件和噪声模型，进行任务评价 |
| 相干高或相位领先就能确定因果 | 核对平滑、背景模型、共同输入和时延的整周歧义 |

读完应能复算Haar的432能量等式，解释CWT中1/√a和尺度频率换算的作用，指出两通道混叠为何可抵消，并说明边界、阈值及多重比较怎样限制结论。这里完成的是定义、原始来源、解析与数值层面的核查；仍保留AI辅助草稿标记，等待专业审阅。
