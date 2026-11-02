---
title: "数字信号处理"
english: "Digital Signal Processing"
slug: "digital-signal-processing"
summary: "配套《信号与系统》，从样值、采样率和处理规格进入DFT与谱估计、FIR/IIR设计、分块卷积、STFT重建、多速率、有限精度及自适应滤波，学习怎样实现并验证数字处理链。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "数字信号处理", "FFT", "数字滤波", "谱估计", "多速率", "自适应滤波"]
aliases: ["DSP", "数字信号处理基础", "Digital Signal Processing"]
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
  - {label: "研究对象", value: "有限精度样值上的分析、变换、滤波与算法实现"}
  - {label: "配套课程", value: "信号与系统解释关系，本篇落实规格、计算、状态和验证"}
  - {label: "核心区别", value: "幅度与PSD、线性与循环卷积、离线与实时分别判断"}
  - {label: "重要边界", value: "理论频响不等于完整设备响应，数值改善不等于感知获益"}
references: ["dsp-structures", "dsp-dft", "dsp-spectral", "dsp-periodogram", "dsp-periodogram-api", "dsp-welch-api", "dsp-fir", "dsp-firwin-api", "dsp-phase", "dsp-iir", "dsp-butter-api", "dsp-filtfilt-api", "dsp-sos-api", "dsp-block", "dsp-stft", "dsp-stft-api", "dsp-rates", "dsp-polyphase", "dsp-upfirdn-api", "dsp-resample-api", "dsp-quant", "dsp-adaptive"]
order: 1013
---

**数字信号处理**（digital signal processing，DSP）研究怎样对数字表示的信号进行分析和运算，并在给定精度、存储、运算量与时间限制下实现这些运算。对象既包括录音，也包括图像、振动和神经记录；这里主要用一维声音序列建立概念。[1](#ref-dsp-structures)

本篇与[信号与系统](../signals-and-systems/)配套：在那里理解卷积、频率响应和采样的关系，在这里进一步确定规格、设计系数、选择算法、维护分块状态并核验输出。[FIR与IIR滤波器](../fir-and-iir-filters/)提供滤波器专题的更细讨论。课程之间可以按问题往返查阅，无需先完整学完一门才开始另一门。

十幅图和全部数值均来自独立指定的教学模型，不是耳机、助听器、听者或实际房间的测量。示例以Python、NumPy和SciPy复算，配有[完整实验脚本](/n3-hearingpedia/code/digital-signal-processing/experiments.py)；文末还给出三个可单独运行的短例子。

## 阅读准备与独立阅读

**起步知识。** 会读函数图像、使用比例和简单方程就可以开始。序列、复数、求和、卷积和分贝在首次使用处说明；暂时不熟悉积分、矩阵或概率分布，也能先读处理流程和图例。

**随用随补。** x[n]表示第n个样值，n为整数；Σ表示相加。j²=−1，复数a+jb可用平面上的点(a,b)表示，模为√(a²+b²)，相位为相应方向角。复指数exp(jθ)=cosθ+j sinθ让幅度和相位一起参与计算。向量只是把多个样值排在一起；[线性代数](../linear-algebra/)和[概率论](../probability-theory/)可按投影、期望等具体问题补读。

**分层阅读。** 第一遍关注单位、滤波、分块、重采样和验证；第二遍核对DFT归一化、窗函数、STFT重建及有限精度。完整推导收敛性、随机谱估计误差和自适应算法理论，还需要相应数学训练；正文给出定义、适用条件及可运行的小例子，帮助读者独立理解主要结论。

极限、变化率、累积与连续初值问题，可配合[微积分](../calculus/)按需补读；这里的数字实现仍从有限样值和明确计算规则开始。

## 从处理任务写出可检查的规格

### 样本索引与秒之间靠采样率连接

均匀采样时，采样率fs以Hz或sample/s计，采样间隔Ts=1/fs，以s计，x[n]=xc(nTs)。16 kHz录音的160个样本对应10 ms；同样160个样本若标成8 kHz，播放时长就变为20 ms。数组本身没有自动携带秒的含义，文件元数据必须与算法实际使用的采样率一致。

物理频率f以Hz计，离散角频率Ω=2πf/fs以rad/sample计。16 kHz下的2 kHz对应Ω=π/4；不能把2000直接传给一个只接受0到π的接口。软件中“归一化频率”还可能指f/fs或f/(fs/2)，必须读清约定。

离散复指数在Ω与Ω+2π处相同，采样后相差整数倍fs的连续频率可能无法区分，这就是混叠的来源。对实信号，正负频率互为共轭，通常画0到fs/2；fs/2称Nyquist频率。理想均匀采样要无混叠地表示带限于|f|≤B的任意信号，通常要求fs>2B，并在采样前抑制带外分量；恰在等号边界的某些相位会丢失信息。实际滤波有过渡带，不能把全部可用频带一直用到边界。

### 先写通带 阻带 误差和时间预算

假设要保留0—2.5 kHz、抑制3.5—8 kHz，并允许2.5—3.5 kHz为过渡带。**通带**是希望按指定增益传输的范围，**阻带**是希望衰减的范围；有限长度或有限阶数通常不能实现理想砖墙响应。规格还需写明通带误差、阻带衰减、相位要求、采样率、可用延迟及处理对象。

幅度增益A的分贝为20log10|A|，功率比则用10log10；二者只有在功率正比于幅度平方且比较条件相同时才对应。音频数组的无单位幅度不自动等于Pa，也不直接给出dB SPL。若使用dBFS，应声明满刻度及峰值/RMS约定；设备输出仍需[测听校准](../audiometric-calibration/)。

“去噪”“增强”也必须变成具体任务：保留哪些信号、误差相对哪个目标、允许多少延迟、用什么独立资料评价。把曲线画得平滑不是充分规格。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/processing-chain.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/digital-signal-processing/processing-chain.svg" alt="从采样率和单位进入分块状态、算法计算和输出核验的四阶段流程。" width="1400" height="550" loading="lazy" /></a><figcaption>图1　先定义任务，再计算和验证。模拟抗混叠、ADC、数字算法、DAC与模拟输出链各有作用；图中的16 kHz和64样本块只是教学设定，不能代替完整硬件延迟测量。</figcaption></figure>

## 用差分方程和冲激响应定义数字滤波

### FIR是有限加权和 IIR使用递推

**滤波器**根据输入序列生成输出，可选择性改变频率分量，也可能改变时间波形。M点因果FIR可写成
$y[n]=\sum_{k=0}^{M-1}b_kx[n-k]$。
系数bk称抽头权重，冲激响应h[k]=bk在这M个索引之外为0；阶数通常为M−1，前提是末项系数非零。比如h=[1,0,0.5]会把输入与延迟两个样本的半幅副本相加。[1](#ref-dsp-structures)

若有限输入x=[1,2]从n=0开始、记录外为零，则完整输出为[1,2,0.5,1]：输出长度2+3−1=4，而不是只保留两个输入索引。这也是后面检查分块尾部的最小例子。

一般常系数递推写为
$a_0y[n]=\sum_{k=0}^{K}b_kx[n-k]-\sum_{\ell=1}^{P}a_\ell y[n-\ell]$，
要求a0≠0；软件常先除以a0使其为1。反馈项的负号来自这个约定，不能把另一教材的正反馈系数不加转换地抄入。IIR指冲激响应一般无限持续；存在递推的表达也可能因抵消退化为FIR，必须看实际输入输出关系。

### 卷积和稳定性都有条件

单位样本δ[n]在n=0为1，其余为0。零初始状态的线性时不变系统对它的输出称冲激响应h；满足相应收敛条件时，
$y[n]=(h*x)[n]=\sum_k h[k]x[n-k]$。
有限FIR的求和没有无限尾部问题；IIR还需说明初始状态与收敛。实时流处理中，每一块的开头通常不是整个系统的零初始时刻。

离散LTI系统的BIBO稳定性要求有界输入产生有界输出，等价于冲激响应绝对可和。对因果、适当有理传递函数，约去公共因子后的外部稳定条件为全部极点严格位于单位圆内；代数抵消不能证明实现内部所有状态稳定。极点是分母的根，单位圆是复平面|z|=1。读者可先用一阶h[n]=aⁿ、n≥0检查：|a|<1时绝对和有限，a=1时不再有限。

为解释后面的频响，先定义 $H(e^{j\Omega})=\sum_n h[n]e^{-j\Omega n}$；绝对可和时此和存在。它表示复指数输入在稳态下被乘上的复增益，|H|给出幅度比，arg H给出相位变化。差分方程在零初始条件下还可写成有理传递函数 $H(z)=(\sum_k b_kz^{-k})/(\sum_\ell a_\ell z^{-\ell})$，z⁻¹对应一拍延迟；若单位圆属于收敛域，在z=eʲΩ处即得到频率响应。零点是分子根，极点是分母根，讨论抵消后关系仍须留意内部实现。更完整的Z变换与收敛域见配套课程。

## DFT和FFT怎样变成可解释的谱

### FFT是计算DFT的方法 不是另一种物理变换

对N点数组，约定
$X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}$，
逆变换为
$x[n]=N^{-1}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}$。
k对应f=kfs/N；大于fs/2的部分可按周期性解释为负频率。FFT用分治等结构减少计算量，常用算法把典型规模从N²降至NlogN量级，但计算的是同一个DFT，误差仍受浮点精度影响。[2](#ref-dsp-dft)

有限记录相当于给无限序列加窗；DFT又在离散频率点上取样。补零到更长NFFT会让图上的频率间隔fs/NFFT更小，却没有增加观测时长，也没有把本来混在同一主瓣中的两个分量自动分开。[3](#ref-dsp-spectral)

### 窗函数同时改变泄漏 主瓣和幅度

窗w[n]把记录乘成w[n]x[n]。矩形窗就是记录内权重全为1；本篇周期Hann窗为w[n]=0.5−0.5cos(2πn/N)，0≤n<N。它与端点对称的Hann定义不同，必须说明使用哪一种。低旁瓣有助于减小强分量向远处的泄漏，代价通常是主瓣变宽；选窗要看相邻分量和动态范围，而不是只看曲线好看。[3](#ref-dsp-spectral)

相干增益CG=(Σw)/N。对恰落在DFT栅格、远离DC和Nyquist且正负谱瓣不相互污染的实余弦，幅度可按2|Xw[k0]|/|Σw|估计；因子2合并正负频率贡献。DC与偶数长度的Nyquist分量不应乘2。偏离栅格时还会出现栅栏效应和幅度偏差，不能仅除以CG就声称任意频率都已精确校正。

图2取N=256、fs=16 kHz，观测长16 ms，原始栅格间隔62.5 Hz。2050 Hz余弦没有恰落栅格；8192点FFT只用于细画同一有限窗谱，不是把分辨能力提高到1.953 Hz。

### 幅度谱 频谱功率与PSD不能混用

**周期图**是一种有限记录谱估计。双边密度按
$\widehat S_{xx}[k]=|X_w[k]|^2/(f_s\sum_n w[n]^2)$
归一化，单位为输入单位平方/Hz；对实信号转为单边PSD时，将内部正频率的功率乘2，保留DC及偶数FFT长度的Nyquist项不变。这里加倍的是功率，不是先把幅度乘2再平方。[4](#ref-dsp-periodogram)[5](#ref-dsp-periodogram-api)

频谱功率形式可用|Xw|²/|Σw|²；它与密度的比值是**等效噪声带宽**
$B_{\mathrm{ENBW}}=f_s\sum w[n]^2/|\sum w[n]|^2$，
不是随意丢掉一个Hz。该量要求Σw非零；本例矩形窗为62.5 Hz，周期Hann为93.75 Hz，即1和1.5个原始频点间隔。[5](#ref-dsp-periodogram-api)

完整单边周期图的ΣPSD·Δf精确对应Σ|wx|²/Σw²，而非任意有限记录未加窗的均方值Σ|x|²/N。二者在某些统计条件下期望相同，却不能对每一段录音直接画等号。对于随机过程，谱估计还涉及平稳性、窗导致的偏差与估计方差；一条密集FFT曲线不等于精确获知真实随机谱。

**Welch法**把记录分段、加窗，计算各段周期图后平均，常以降低方差为目标；在固定总记录长度下，较短分段通常牺牲频率分辨。重叠段并非彼此独立，置信区间的自由度不能直接按段数翻倍。要记录段长、重叠、窗、去趋势和平均方式；本篇例子显式关闭去趋势，避免软件默认去均值改变被验证的等式。[6](#ref-dsp-welch-api) 更详单位见[频谱与功率谱密度](../spectrum-and-power-spectral-density/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/spectral-window.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/digital-signal-processing/spectral-window.svg" alt="矩形与周期Hann窗的时域权重及同一偏离频点余弦的加窗频谱比较。" width="1400" height="550" loading="lazy" /></a><figcaption>图2　窗改变泄漏、主瓣和增益。输入为幅度0.8、2050 Hz余弦，256点、16 kHz；8192点FFT用于细画。右图使用2|FFT|/Σw的幅度标度，取20log10，参考幅度1，限于正频率内部，未标成PSD或声压级。</figcaption></figure>

## 从规格设计FIR 并计算延迟

### 窗函数法把理想响应截成有限系数

理想低通在|f|<fc时幅度为1，其他频率为0；其无限长冲激响应可写成
$h_d[n]=(2f_c/f_s)\operatorname{sinc}[(2f_c/f_s)(n-\alpha)]$，
这里sinc(u)=sin(πu)/(πu)，sinc(0)=1，α=(M−1)/2。乘有限窗再按所需频率归一化，得到可实现FIR。截断会产生过渡带与波纹，fc、窗和长度共同决定响应，不能只设置一个“截止频率”就视为满足所有规格。[7](#ref-dsp-fir)

本例fs=16 kHz、fc=3 kHz，比较65点Hann、129点Hann和129点Kaiser窗β=8.6。Kaiser的β控制窗形，长度与β都影响主瓣、旁瓣及过渡带。**SciPy的firwin在这里把cutoff定义为半幅度点，约−6.02 dB，而不是半功率−3.01 dB。** 实际有限窗结果在该点接近0.5。[8](#ref-dsp-firwin-api)

按0—2.5 kHz测最大绝对幅度误差，按3.5—8 kHz测最差阻带增益，65536点频率网格上三种方案的阻带衰减约44、62、89 dB。这些是指定频带和网格上的计算，不是所有设计的保证；最终工程验收还需更细搜索极值、量化系数并检查实际实现。

### 对称系数给出线性相位 仍需要等待

实对称系数h[n]=h[M−1−n]使响应可写成实函数乘exp(−jΩα)；在响应不为零且相位连续的频段，群延迟为α个样本。群延迟定义为−d相位/dΩ，用样本计；除以fs后换成秒。65点与129点在本例分别为32和64样本，即2与4 ms。[9](#ref-dsp-phase)

这说明不同频率可有共同时间平移，不表示没有延迟。零点处相位未定义，符号改变可能带来π跳变；不能跨零点直接差分相位再解释为正常群延迟。奇长度对称FIR属Type I，偶长度对称FIR属Type II并在Nyquist处必有零点，某些高通规格因此不能使用偶数抽头。[8](#ref-dsp-firwin-api) 详见[相位与群延迟](../phase-and-group-delay/)及[最小相位系统](../minimum-phase-system/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/fir-design.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/digital-signal-processing/fir-design.svg" alt="三个指定FIR低通的幅频响应与阻带衰减和群延迟比较。" width="1400" height="550" loading="lazy" /></a><figcaption>图3　长度、窗形和延迟一起比较。fs=16 kHz，firwin的fc=3 kHz；阴影标明0—2.5 kHz通带与3.5—8 kHz阻带。右图衰减以指定网格上最差阻带增益计算，不是连续全频域的严格极值证明。</figcaption></figure>

## IIR设计与离线双向处理

### 模拟原型 双线性变换与二阶节

IIR常从Butterworth等模拟原型设计。Butterworth低通的特点是通带幅度最大平坦，阶数提高使过渡更陡，但相位一般非线性。双线性变换用
$s=2f_s(1-z^{-1})/(1+z^{-1})$
把模拟s平面映射到数字z平面；频率关系为ωa=2fs tan(Ω/2)，因而是非线性频率压缩。要使某个数字截止频率准确对应，需预畸变ωa=2fs tan(πfc/fs)。[10](#ref-dsp-iir)

本例用butter生成六阶、3 kHz、16 kHz采样的低通，并指定输出为SOS，即**二阶节**级联。每节有三项分子和三项分母系数；六阶系统为三节。把高阶多项式拆节通常改善数值条件，但节的排序、缩放、信号幅度和字长仍影响误差，不能宣布SOS在所有有限精度下都绝对稳定。[11](#ref-dsp-butter-api)[13](#ref-dsp-sos-api)

### filtfilt改变幅度 也改变时间可用性

对实系数滤波器，在无限序列或远离适当处理过的边界时，前向再反向滤波的等效频响为H(eʲΩ)H(e⁻ʲΩ)=|H(eʲΩ)|²，因而相位为零、幅度平方、有效阶数加倍。单次Butterworth截止处幅度1/√2，双向后为1/2；用分贝看就是约−3.01 dB变成−6.02 dB。[12](#ref-dsp-filtfilt-api)

双向处理需要未来样本，不能直接拿来作零延迟实时算法。有限录音还涉及补边、初始状态与端点暂态，短记录尤其应检查；“零相位”不保证边界无伪影，更不保证波形所有细节保持原样。若目标是最终双向响应的某一截止规格，要针对平方后的响应重新设计，不能照搬单次参数。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/iir-offline.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/digital-signal-processing/iir-offline.svg" alt="六阶Butterworth的单次与双向幅频响应，以及因果实现的单位圆内极点。" width="1400" height="550" loading="lazy" /></a><figcaption>图4　相同系数不等于相同最终滤波器。左图以理想内部区间的|H|与|H|²比较，未模拟有限文件端点；右图仅画单次因果滤波器极点，不能把它当作双向非因果实现的实时稳定性图。</figcaption></figure>

## 分块处理必须保留记忆和完整卷积

### 状态应从上一块传到下一块

流式处理每次收到B个新样本，滤波器还需要过去输入和输出。FIR可保留M−1个输入样本，IIR常保留某种实现对应的内部状态；具体状态不必等于直观上的过去输出。sosfilt采用二阶节的状态表示，一维输入下形状为“节数×2”，处理后将返回状态传给下一块。[13](#ref-dsp-sos-api)

只在真正的记录起点初始化为零，逐块延续状态后，应与同样初始条件的整段计算一致。每一块都清零会反复制造启动暂态。断流、采样率变化和滤波参数切换则需要单独定义状态策略，不能把任意旧状态直接解释成新滤波器的物理记忆。

### FFT乘法默认对应循环卷积

B点输入块与M点FIR的完整线性卷积长B+M−1。用FFT实现时，必须令NFFT≥B+M−1，或采用等价的有效区间处理，否则后部会绕回前部，得到循环卷积污染。[14](#ref-dsp-block)

**重叠相加**（OLA）把输入分成不重叠块，各块补零做完整卷积，再把输出中重叠的尾部相加。**重叠保留**（OLS）则让输入块重叠M−1点；NFFT点循环卷积的前M−1点受污染而丢弃，每块保留B=NFFT−M+1个有效输出。开始补零与结束冲洗尾部都要计入，不能只在中段比较正确就省掉最后响应。

图5故意令M=129大于B=64，选择NFFT=256，检查跨多个块的尾部累积。FFT法对长卷积可更高效，但变换、缓存与内存访问也有成本；短滤波器不保证更快。算法的群延迟、凑齐一个输入块的等待、声卡缓冲与AD/DA延迟是不同来源，应分别计算并测量整条链。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/block-convolution.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/digital-signal-processing/block-convolution.svg" alt="按64样本划分输入，将129抽头FIR的重叠相加结果与完整直接卷积比较。" width="1400" height="550" loading="lazy" /></a><figcaption>图5　分块不是把系统切成互不相干的短记录。输入257点，FIR长129，完整输出385点；B=64、NFFT=256，最后一块不足64点仍保留其全部有效尾部。下方面板显示两种算法的浮点差值。</figcaption></figure>

## STFT分析还要回答怎样重建

### 窗长 步长和FFT长度分别控制什么

短时傅里叶变换**STFT**对局部加窗片段计算谱。本篇使用局部索引约定：
$X[m,k]=\sum_{n=0}^{N-1}x[mR+n]w[n]e^{-j2\pi kn/N_{\mathrm{FFT}}}$，
R为步长，N为窗长，NFFT≥N。改变时间原点约定可能改变相位因子，比较两个程序时须先对齐约定。[15](#ref-dsp-stft)

窗长256、fs=16 kHz表示16 ms观察范围；R=64表示每4 ms更新一帧；NFFT=512表示31.25 Hz频率栅格。更新间隔不是独立时间分辨率，31.25 Hz也不是任意两个正弦可分辨的保证。窗长与窗形决定主要时频平滑；重叠增加冗余，补零增加显示取样。详见[声谱图](../spectrogram/)。

### 同窗分析合成时要除以重叠权重

对未修改的STFT逐帧逆FFT、截回N点，再乘同一个合成窗并重叠相加，会得到原信号乘上Σm w[n−mR]²。逐样本除以这个和即可恢复原值，前提是所需位置的分母非零；这就是此处**非零重叠相加条件NOLA**的作用。[16](#ref-dsp-stft-api)

常数重叠相加COLA在特定窗对和合成结构下提供方便的常数归一化；它与这里的“分母非零”不同，不能把COLA作为所有重建方案唯一必要条件。必须同时说明分析窗、合成窗、边界扩展、步长和FFT缩放。图6在两端补256个零，周期Hann、R=64，原记录范围内平方窗重叠和约为1.5，重建误差在浮点舍入量级。

修改谱后，逆变换得到的信号未必再分析成完全相同的修改谱；任意逐帧增益也可能产生调制和边界伪影。“原样STFT能重建”不能当作任意时频去噪都无失真的证明。软件资料中的旧stft接口已标为legacy，本文以定义展示原理，新项目可结合ShortTimeFFT等现行接口评估需求。[16](#ref-dsp-stft-api)

滤波器组则把信号分到多个频带，可能同时降采样。分析与合成滤波器、抽取率和混叠抵消条件共同决定是否可重建；任意摆放几只带通并相加不自动完美重建。数字频带数也不等于独立听觉通道数。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/stft-reconstruction.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/digital-signal-processing/stft-reconstruction.svg" alt="一千赫兹切换三千赫兹的合成信号STFT，与同窗重叠归一化后的重建误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图6　显示与重建使用同一组明确参数。4096点信号，前半1 kHz、后半3 kHz，幅度均为1；16 ms周期Hann窗、4 ms步长、512点FFT，两端补零。颜色为相对全图最大值的谱幅度分贝，非校准PSD；重建面板检查原记录范围。</figcaption></figure>

## 多速率处理改变样本间隔

### 抽取前滤波 插值后去镜像

整数M倍降采样可写成y[n]=v[Mn]，但v应先经过抗混叠低通；否则原高频分量折入新的可表示范围。图7从32 kHz降至16 kHz，原13 kHz余弦直接抽取后成为3 kHz，无法靠降采样之后的处理再与真实3 kHz成分区分。[17](#ref-dsp-rates)

整数L倍升采样先在样本间插L−1个零，频谱产生镜像，再用插值低通去掉不需要的复制。理想重建原样值尺度时，该高采样率低通通带增益应为L；只插零再用单位DC增益低通会改变幅度。升采样增加样本数，不恢复原采样时已经丢失的信息。

一般L/M重采样先约去公因数，再按升L、滤波、降M解释；滤波器在升采样后的采样率上设计，同时限制插值镜像和降采样混叠。输出采样率为fsL/M，正确处理应大致保留物理时长；把文件的采样率标签直接改为fsL/M却不重算样本，会改变播放速度和音高。

### 多相分解省掉不必要的运算

**多相分解**把系数按索引余数分组，如h[r+qL]形成第r相。它重排升采样、滤波和抽取的运算顺序，避免大量与插入零相乘或最终会被丢弃的计算；在精确算术、相同边界与对齐下，与直接结构等价。[18](#ref-dsp-polyphase)[19](#ref-dsp-upfirdn-api)

upfirdn返回按所给系数实现的升采样—FIR—降采样结果，包括其因果延迟与尾部；resample_poly则提供居中、裁切等便捷约定，不能不对齐就逐点比较两者。给resample_poly传入系数数组时，还要按约分后的升采样率设计；记录补边方式，检查有限录音开头和结尾。[20](#ref-dsp-resample-api)

图7使用129点Kaiser窗β=8.6、7 kHz低通，再降2。取远离边界的2048个输出样本估计幅度，1 kHz由0.8保持在约0.8，折叠至3 kHz的分量从0.5降到约2.8×10⁻⁶；有限FIR只提供有限抑制，不是数学上完全消除。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/multirate-alias.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/digital-signal-processing/multirate-alias.svg" alt="三十二千赫兹降采样至十六千赫兹时，比较直接抽取和先低通的输出频谱。" width="1400" height="550" loading="lazy" /></a><figcaption>图7　重采样滤波必须发生在混叠产生之前。输入8192点，为0.8倍1 kHz与0.5倍13 kHz余弦之和；右图取输出中央2048点，单边幅度用2|FFT|/2048归一化。仅画内部正频率，幅度参考1，未使用声压级。</figcaption></figure>

## 有限精度会改变算法行为

### 量化误差不普遍等于独立白噪声

均匀量化把幅度映射到间隔Δ的离散级。在没有过载且采用最近级舍入的范围内，误差e=Q(x)−x满足|e|≤Δ/2；饱和限幅后的过载误差不受这个界限制。若另假定误差在[−Δ/2,Δ/2]均匀分布，才得到方差Δ²/12；时间独立、与信号独立又是额外假设。[21](#ref-dsp-quant)

低幅周期输入可产生周期误差，其谱具有结构。图8用幅度0.1、周期32样本的余弦和Δ=0.25的八级中升型量化器，零附近没有输出级0，因此输出在±0.125间变化，误差明显与输入相关。抖动可在特定分布、幅度及加减方式下改变误差统计，却引入噪声或其他代价，不能笼统宣称任意抖动都使误差完全独立且无代价。

字长、定点小数位、舍入、饱和和溢出规则分别需要说明。回绕溢出与饱和限幅产生不同输出；浮点也有有效位、下溢及非结合性。位数高通常减少某些误差，不代替动态范围和数值条件分析。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/quantization-error.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/digital-signal-processing/quantization-error.svg" alt="低幅周期余弦的八级中升型量化结果，以及误差呈现周期结构的自相关。" width="1400" height="550" loading="lazy" /></a><figcaption>图8　误差的结构由输入和量化规则共同决定。512点输入为0.1cos(2πn/32+0.2)，八个输出级从−0.875至0.875，间隔0.25；右图为有限记录的有偏自相关，除以零延迟值，不是总体相关函数的无误差估计。</figcaption></figure>

### 系数量化与输出量化是两类问题

令y[n]=a y[n−1]+x[n]、a=0.9997。若只将系数舍入到2⁻¹⁰的网格，并允许整数部分表示1，则a变为1。原冲激响应随n衰减，量化后的响应保持1；单位阶跃输入下，后者输出n+1，无界增长，BIBO稳定性因此改变。

图9只量化这一个系数，其余运算用双精度，未模拟完整定点设备。若某种格式根本不能表示1，结果会不同，所以不能把这里的网格不加说明地称为某个固定Q格式。真实IIR还可能有状态舍入导致的极限环、溢出和节间缩放问题；SOS有助于控制数值误差，但不能免除逐实现验证。[1](#ref-dsp-structures)[21](#ref-dsp-quant)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/coefficient-rounding.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/digital-signal-processing/coefficient-rounding.svg" alt="一阶递推系数从0.9997舍入到1后，冲激不衰减且阶跃响应持续增长。" width="1400" height="550" loading="lazy" /></a><figcaption>图9　系数很小的改变也可能跨过稳定边界。零初始状态，n=0—9999；原a=0.9997，按10位小数精度的网格舍入为1且允许表示该值。仅系数量化，其余双精度，非完整定点仿真。</figcaption></figure>

## 自适应滤波怎样利用误差更新系数

### 先区分输入 期望目标和误差

固定滤波器设计一次系数，自适应滤波器则根据数据持续更新。以实值FIR系统辨识为例，输入向量u[n]=[x[n],x[n−1],…]ᵀ，权重向量w[n]在计算当前输出前已确定，预测ŷ[n]=w[n]ᵀu[n]，期望目标d[n]由另一路观测提供，误差e[n]=d[n]−ŷ[n]。目标未必是无噪声真值，不能把d误称为算法已知的纯净语音。[22](#ref-dsp-adaptive)

**归一化最小均方算法NLMS**的一种实值约定为
$\mathbf w[n+1]=\mathbf w[n]+\mu e[n]\mathbf u[n]/(\epsilon+\mathbf u[n]^\mathsf T\mathbf u[n])$。
它对当前半平方误差沿负梯度更新，并按输入能量归一化；μ为无量纲步长，ε>0用于避免除零，在此应与输入平方有同一单位。不同文献的误差符号和梯度常数约定可能不同。

过大步长会引起不稳定或过强失调，过小则适应慢；激励不足时某些系数无法可靠辨认，相关输入、噪声、路径变化与有限精度都会影响收敛。简单理想假设下的步长界不能当作任意实际闭环系统的保证。复值数据还需要共轭约定，本式只用于实值例子。[22](#ref-dsp-adaptive)

### 冻结参数后 用另一段数据检验

图10用16抽头模型辨认三个非零通路系数：h[0]=0.8、h[3]=0.35、h[8]=−0.2。训练输入4000点，独立高斯输入标准差0.2，观测噪声标准差0.02；μ=0.2、ε=10⁻⁶，初始权重为零。训练结束后冻结系数，在另生成的1000点输入上评价，与训练误差分开。

固定随机种子20261102时，系数RMSE约0.0064；独立验证中，相对无噪声系统输出的RMSE约0.0052，相对带噪观测约0.0217。RMSE为误差平方平均的平方根。两个目标回答不同问题，不能只报较小者，也不能推广为所有声音和路径的效果。

更新权重期间系统不是一个固定LTI滤波器，不能用单条永久不变H解释所有输入。这个辨识例子也不是完整声学回声消除器：真实应用还涉及参考信号同步、双讲、非线性、长路径、漂移和闭环稳定。助听器反馈与录音回声更有不同的路径和信号相关性，应依具体任务验证。[22](#ref-dsp-adaptive)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/digital-signal-processing/adaptive-validation.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/digital-signal-processing/adaptive-validation.svg" alt="NLMS训练后的系数与指定真值比较，并用冻结系数预测独立验证数据。" width="1400" height="550" loading="lazy" /></a><figcaption>图10　训练拟合与独立验证分别报告。左图16个系数；右图仅画1000点验证记录的前80点，完整RMSE使用全部1000点。随机种子20261102，输入和噪声独立生成；无噪声目标只因教学模型已知而可用，不是实际录音中自动可得。</figcaption></figure>

## 把数值正确性落实到完整处理链

### 从等式 小信号和边界开始

先用单位样本、常数、单频、短数组和随机输入检查实现，再进入复杂录音。脉冲可核对h与延迟；常数可检查DC增益；正弦可核对幅度和相位；随机输入可比较整段与任意分块；短文件可暴露补边、尾部和维度错误。算法允许复数还是只允许实数、多声道沿哪个轴处理、输入是否可原地修改，也应写清。

报告误差使用合适的绝对与相对容差；浮点算法间微小差异不必要求逐位相同。相对误差在真值接近0时会放大，不能只看一个百分比。FFT、直接卷积和递推若在同一条件下相符，支持这些实现的数值一致性，不是对任意输入、硬件或参数的普遍证明。

### 系统评价需要声学任务和独立数据

对[助听器](../hearing-aid/)等设备，完整链还包括模拟抗混叠、换能器、压缩、缓存、重建滤波及实际声学负载。算法本身的幅频响应不能替代实耳测量。对[听觉计算模型](../auditory-computational-models/)，数字滤波只是模型操作之一，参数拟合良好也不自动确认生理机制。

训练与测试要按任务隔离听者、语料、路径或设备，避免数据泄漏。客观误差、频谱失真、可懂度模型与真实听者表现是不同结果；若研究声称感知获益，还需对应实验与统计证据。来源在本文用于数学和算法定义，未被解释成听觉干预有效性证据。

### 三个可运行的核对例子

以下使用NumPy与SciPy；本篇运行环境为NumPy 1.26.4、SciPy 1.17.1，所查官方在线接口文档为1.18.0。窗、去趋势、采样率及缩放均显式指定，避免依赖可能变化的默认值。其余十幅图模型见文首完整脚本。

例1在2000 Hz恰落频点时检查实余弦幅度，并验证周期图积分对应加窗均方。最后一个等式不应擅自改成未加窗均方。[5](#ref-dsp-periodogram-api)

```python
import numpy as np
from scipy import signal
fs, N = 16000, 256
n = np.arange(N)
x = 0.8 * np.cos(2*np.pi*2000*n/fs)
w = signal.windows.hann(N, sym=False)
X = np.fft.rfft(w*x)
amplitude = 2*abs(X[32])/w.sum()  # 内部正频率，不适用于DC/Nyquist
f, psd = signal.periodogram(x, fs=fs, window=w, detrend=False,
                            return_onesided=True, scaling="density")
integral = psd.sum()*(f[1]-f[0])
weighted_ms = np.sum((w*x)**2)/np.sum(w*w)
assert np.isclose(amplitude, 0.8)
assert np.isclose(integral, weighted_ms)
print(amplitude, fs*np.sum(w*w)/w.sum()**2, integral)
```

例2核对三节SOS的跨块状态；最后一块不足127点仍参与计算。若把循环中的zi每次设为零，一般不会再与整段一致。[13](#ref-dsp-sos-api)

```python
import numpy as np
from scipy import signal
sos = signal.butter(6, 3000, fs=16000, output="sos")
x = np.random.default_rng(1003).normal(size=2048)
whole = signal.sosfilt(sos, x)
zi = np.zeros((len(sos), 2))
blocks = []
for start in range(0, len(x), 127):
    y, zi = signal.sosfilt(sos, x[start:start+127], zi=zi)
    blocks.append(y)
stream = np.concatenate(blocks)
assert np.allclose(stream, whole, atol=1e-12, rtol=1e-12)
print(np.max(np.abs(stream-whole)))
```

例3用“显式插零—完整卷积—取每M点”核对多相实现。这里保留因果延迟和尾部，没有进行resample_poly式居中裁切；L倍通带增益通过L*h给出。[19](#ref-dsp-upfirdn-api)

```python
import numpy as np
from scipy import signal
L, M = 3, 2
x = np.array([1., -0.5, 0.25, 0., 0.8])
h = signal.firwin(31, 1/max(L, M), fs=2, window=("kaiser", 5.0))
z = np.zeros((len(x)-1)*L+1)
z[::L] = x
reference = np.convolve(z, L*h)[::M]
polyphase = signal.upfirdn(L*h, x, up=L, down=M)
assert reference.shape == polyphase.shape
assert np.allclose(reference, polyphase, atol=1e-14, rtol=1e-14)
print(len(polyphase), np.max(np.abs(reference-polyphase)))
```

### 用问题检查自己是否真正理解

1. 为什么8192点FFT可以把256点记录画得更细，却不等于观察了8192个新样本？窗的相干增益与ENBW各校正什么？
2. 为什么firwin的3 kHz与butter的3 kHz在本例不是同一幅度判据？双向滤波后又发生什么变化？
3. 129抽头FIR、64点输入块，为什么不能直接用64点FFT相乘？最后一个输入块处理完为何还可能有输出？
4. STFT的步长4 ms、窗长16 ms、FFT频点间隔31.25 Hz，分别表示什么？原样重建与任意修改谱的重建是否同一问题？
5. 为什么降采样前的13 kHz分量会变成3 kHz？只改文件采样率标签与真正重采样有何不同？
6. 为什么Δ²/12不是每个量化误差序列的必然方差？怎样让接近单位圆的极点在系数量化后跨越稳定边界？
7. NLMS的期望目标从何而来？为什么冻结系数后还要另用验证输入，并分别报告相对无噪声目标和带噪观测的误差？

来源以MIT官方课程笔记、大学自适应滤波讲义和SciPy官方接口说明为主。课程笔记支持原理，接口说明支持具体缩放与参数约定，本文图形、规格及数值另行复算；仍按“待专业审阅”标记，不把自动核验称为外部专家评审。
