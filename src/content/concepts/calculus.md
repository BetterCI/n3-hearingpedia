---
title: "微积分"
english: "Calculus"
slug: "calculus"
summary: "从变化率与累积理解极限、连续、导数和积分，再进入微积分基本定理、Taylor近似、反常积分、级数、多元微分、重积分和初值问题；用波形与数值反例学习条件、单位和误差。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "微积分", "极限", "导数", "积分", "Taylor展开", "微分方程"]
aliases: ["Calculus", "微分与积分", "微积分基础"]
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
  - {label: "研究对象", value: "连续变量上的局部变化、整体累积及二者的联系"}
  - {label: "核心桥梁", value: "在适当条件下，微分与积分通过微积分基本定理相联系"}
  - {label: "研究连接", value: "波形斜率、均方与RMS、模型灵敏度、连续动力学与数值计算"}
  - {label: "重要边界", value: "连续不保证可导，偏导存在不保证可微，数值近似不等于极限证明"}
references: ["calc-functions", "calc-limit", "calc-continuity", "calc-derivative", "calc-rules", "calc-mvt", "calc-taylor", "calc-integral", "calc-ftc", "calc-substitution", "calc-techniques", "calc-improper", "calc-series", "calc-partial", "calc-differentiable", "calc-gradient", "calc-multiple", "calc-polar", "calc-ode", "calc-numerical", "calc-trapezoid-api", "calc-ivp-api"]
order: 1002
---

**微积分**（calculus）是研究函数的局部变化、整体累积及其联系的数学分支。微分侧重某一点附近怎样变化，积分侧重许多小贡献怎样相加；极限为这两种操作提供严格定义。它既是一套计算方法，也要求说明对象、条件和误差，不能只理解为“求导公式加积分公式”。[1](#ref-calc-functions)[2](#ref-calc-limit)

在听觉与声学研究中，波形斜率、声压均方、变化包络、连续滤波模型、膜电位动力学和参数灵敏度都可能使用微积分。本篇从函数图像和小数组建立概念，与[信号与系统](../signals-and-systems/)、[数字信号处理](../digital-signal-processing/)、[概率论](../probability-theory/)、[数学物理方法](../mathematical-physics-methods/)及[计算神经科学](../computational-neuroscience/)相互配合。

十幅图和全部数值均由独立指定的教学函数产生，未测量听者、神经元或实际器件。声学例子帮助解释数学关系，不据此声称算法改善了感知。文末提供三个可单独运行的短例子，另有[完整实验脚本](/n3-hearingpedia/code/calculus/experiments.py)。

实际计算中的舍入、条件数、算法稳定性和离散误差，可配合[数值分析](../numerical-analysis/)按具体问题学习，并用独立计算核对。

## 阅读准备与独立阅读

**起步知识。** 会读横纵坐标、使用比例、解简单方程即可开始。函数、绝对值、指数、三角函数和求和在首次使用处作解释，不要求先学完另一门大学数学课程。先修的高中代数与函数知识有帮助，可随文补充。

**随用随补。** f(x)表示把输入x对应到输出的规则；|x|表示x到0的距离。Σ表示把指定项相加；n!=1×2×…×n，且0!=1。exp(u)=eᵘ是自然指数，ln是它在正数上的反函数；三角函数角度用弧度，完整一周为2π。指数、对数和三角函数的自变量应无量纲，例如时间t除以时间常数τ。

**分层阅读。** 第一遍看图理解极限、切线、矩形求和和初始条件，再读单位与数值误差。第二遍核对ε—δ、余项、收敛和多元可微的定义。完整实分析、测度积分和微分方程理论需要进一步训练；本文保留必要条件和反例，让主要解释尽量不依赖外部课程。

## 极限描述附近的行为 连续还要核对点值

### 函数先有定义域 再谈变化

**定义域**是允许的输入集合，**值域**是实际输出集合。f(x)=1/x在x=0没有定义；ln x在实数范围内只接受x>0。讨论某点极限、导数或积分之前，要先确定在哪个区间、允许从哪一侧靠近，以及变量是否具有物理单位。[1](#ref-calc-functions)

以下有限区间[a,b]默认a<b，避免把零长度区间代入平均斜率等含分母的公式。

函数图像不必是一条光滑曲线，也不一定能由一条简单公式写出。离散录音x[n]只给出整数索引上的样值，连续函数p(t)则定义在连续时间上；有限样本本身不能唯一决定样点间的所有变化。若用插值曲线求导，应把插值假设列为模型的一部分。

### ε—δ定义把“任意接近”说清楚

先讨论f在包含a的某个开区间内有定义、但a本身可以除外的情形。推广到一般定义域时，还需a是它的聚点，即任意小邻域内都有不同于a的定义域点；不能在孤立输入点附近用空条件给任意L都指定一个极限。

说 $\lim_{x\to a}f(x)=L$，指对每个ε>0，都能选出δ>0，使定义域内所有满足0<|x−a|<δ的x都满足|f(x)−L|<ε。ε控制输出误差，δ控制输入邻域；δ可以依赖ε，但必须对这个邻域内所有合格的x同时有效。这里排除x=a，所以极限不由f(a)单独决定。[2](#ref-calc-limit)

例如无量纲f(x)=x²，在a=1处，若|x−1|<1，则|x+1|<3。因此选δ=min(1,ε/3)，便有|x²−1|=|x−1||x+1|<ε。这个不等式证明对任意ε成立；仅列几个越来越接近1的数值，仍不能代替证明。

左极限与右极限分别限制x从a左侧或右侧靠近；内点的双侧极限存在，要求两侧极限存在且相等。某一特定路径上的接近不代表所有接近方式都成立，多变量时尤其如此。

### 连续 可导和有界分别回答不同问题

**在a连续**要求f(a)已定义、极限存在，且该极限等于f(a)。如果x≠1时f(x)=x²，却另设f(1)=1.6，极限仍为1，但函数在1处不连续。跳变、发散和持续振荡是其他不同的极限失败方式，不能都看成一个“缺失点”。[3](#ref-calc-continuity)

闭区间[a,b]上的实连续函数能取得最大值与最小值，并具有介值性质；开区间上的连续函数不一定取得端点附近的上确界。连续也不保证可导，例如|x|在0处左右斜率不同；有界更不保证连续。这些条件各自有作用，不宜混用。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/limit-continuity.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/calculus/limit-continuity.svg" alt="用输入邻域和输出误差带说明平方函数的极限，再比较修改一个点值后的不连续。" width="1400" height="550" loading="lazy" /></a><figcaption>图1　极限与连续多核对了一件事。（a）x²在1附近，ε=0.3、δ=0.1，邻域内输出落入误差带；（b）只把f(1)改为1.6，空心点表示原曲线此点未取值，实心点表示实际点值。坐标均无量纲，非测量数据。</figcaption></figure>

## 导数是局部变化率 不是两个零相除

### 从割线斜率到导数定义

当h≠0时，平均变化率为[f(a+h)−f(a)]/h；若它在h→0时趋于同一个有限数，称f在a可导，导数记作f′(a)或df/dx在a处的值。导数的定义是差商的极限，没有把h直接设成0再计算0/0。[4](#ref-calc-derivative)

**切线**由这个局部斜率确定；与曲线相交一次或多次都不是切线的定义。若f在a可导，则
$f(a+h)=f(a)+f'(a)h+o(h)$，
其中o(h)/h在h→0时趋于0。这表示线性部分之外的误差相对h更小。可导必连续，反向不成立；竖直切线对应无穷斜率，不能按这里的有限导数称为可导。

导数的单位是“输出单位/输入单位”。位移对时间求导是速度，声压对时间求导是Pa/s。图上横轴由s改为ms时，数字斜率差1000倍；物理变化率并没有改变。

### 用一个脉冲把定义算出来

设连续声压模型p(t)=A exp[−t²/(2τ²)]，A=1 Pa、τ=2 ms。按链式法则，
$p'(t)=-(t/\tau^2)p(t)$。
在t=2 ms处，p约0.6065 Pa，导数约−303.27 Pa/s。负号表示该点向前走时声压在下降，不表示波形此时声压为负。

取h=2、1、0.2、0.02 ms的右侧割线，斜率依次约−235.60、−281.88、−302.28、−303.26 Pa/s。它们不是四种相互矛盾的“瞬时斜率”，而是不同时间跨度的平均变化率；模型光滑时才趋近同一导数。图2显示这种关系，但严格结论仍由解析定义支持。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/derivative-pulse.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/calculus/derivative-pulse.svg" alt="高斯声压脉冲在两毫秒处的割线趋向切线，并显示解析导数的正负变化。" width="1400" height="550" loading="lazy" /></a><figcaption>图2　局部斜率需要说明时间尺度。A=1 Pa、τ=2 ms，高斯模型从负时间到正时间均有定义；左图切点为2 ms，右图导数以Pa/s计，过峰值时变号。波形是教学函数，不是实际声源录音。</figcaption></figure>

## 求导规则怎样连接模型与极值

### 每条规则都以相应可导性为前提

在所讨论点满足可导及必要非零分母条件时，和、乘积与商分别遵循
$(f+g)'=f'+g'$、
$(fg)'=f'g+fg'$、
$(f/g)'=(f'g-fg')/g^2$。
复合函数遵循**链式法则**：(f∘g)′(x)=f′(g(x))g′(x)，即外层变化率与内层变化率相乘。[5](#ref-calc-rules)

基本导数包括(xⁿ)′=nxⁿ⁻¹、(eˣ)′=eˣ、(ln x)′=1/x（x>0）、(sin x)′=cos x、(cos x)′=−sin x。实数幂的定义域随指数而变；三角函数的这些形式使用弧度。如果输入角度以度计，要补上π/180的转换因子。

例如p(t)=A(t)cosφ(t)，若指定的A与φ都可导，则p′=A′cosφ−Aφ′sinφ。第二项不能漏掉φ′；恒定幅度的1 kHz余弦，其导数幅度是原幅度乘2π×1000 s⁻¹。对已指定的相位模型可定义f(t)=φ′(t)/(2π)，但仅有一条实波形并不能在无附加条件下唯一拆出任意“包络”和“瞬时频率”。

### 平均值定理约束整体变化

若f在[a,b]连续、在(a,b)可导，则存在c∈(a,b)，使
$f'(c)=[f(b)-f(a)]/(b-a)$。
这就是平均值定理：至少有一个局部斜率等于整段平均斜率；不保证c唯一，也不保证它恰在区间中点。[6](#ref-calc-mvt)

由此可得，若整个区间内|f′|≤K，则|f(b)−f(a)|≤K|b−a|。这把导数界变成输出误差界，可用于灵敏度估计；只知道某一个点导数很小，不能保证远处也变化很小。

### 导数为零只是候选点

内点的可导局部极值必须满足f′=0；但x³在0处导数为0却没有局部极值。求闭区间最值还要检查端点及不可导点；|x|的最小值就在不可导的0。若f′在某点由负变正可判断局部极小；在有适当二阶光滑性时，f′=0且f″>0也是局部极小的充分条件，f″=0则不能单凭这一检验下结论。

二阶导数f″是导数的变化率，常用于曲率、加速度及局部近似。它的符号说明曲线如何弯曲，不等于函数本身的正负。把这些判断带到[机器学习](../machine-learning/)损失函数时，也要区分局部极小、全局极小及多变量的鞍点。

## Taylor近似必须同时说明余项

### 微分是线性近似 不是有限增量的精确值

在一点附近取dx作为输入小增量，**微分**df=f′(a)dx是线性预测；实际增量Δf=f(a+dx)−f(a)一般还包括余项。dx可以选成有限的小数，但df=Δf并非普遍精确等式。模型线性化围绕某工作点建立，允许范围应由误差要求决定。

若f在连接a与x的区间上具有连续的n+1阶导数，一个常用充分条件保证
$f(x)=\sum_{k=0}^{n}f^{(k)}(a)(x-a)^k/k!+R_n(x)$，
且 $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$，
这里M是该区间内|f⁽ⁿ⁺¹⁾|的上界。余项中的范围、阶数和上界都不能省略。[7](#ref-calc-taylor)

对无量纲u≥0，e⁻ᵘ在0附近用1−u近似；0≤u≤0.2时二阶导数e⁻ᵘ≤1，因此绝对误差≤u²/2。在u=0.2处真实值约0.81873，线性近似0.8，实际误差约0.01873，小于上界0.02。这里说的是绝对误差，不能直接称为2%的相对误差。

### 无限多项还要问是否收敛到原函数

有限Taylor多项式有有限余项；无限Taylor级数则要求余项随阶数增加趋于0，才能代表原函数。即使函数有任意阶导数，也不自动等于它在某点的Taylor级数。[7](#ref-calc-taylor)

例如g(u)=exp(−1/u²)（u≠0），g(0)=0，在0处各阶导数都为0，但其他点g(u)>0，因此在0展开的全零级数不能代表它附近的函数。这个例子强调“光滑”与“解析”不同；[复变函数](../complex-analysis/)会进一步解释复解析性为什么有更强的局部约束。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/taylor-remainder.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/calculus/taylor-remainder.svg" alt="指数衰减的不同阶Taylor多项式及其绝对误差，与一阶余项上界对照。" width="1400" height="550" loading="lazy" /></a><figcaption>图3　近似式应带上适用范围和误差。（a）e⁻ᵘ与0处一、二、四阶多项式；（b）同一无量纲区间的绝对误差，一阶界为u²/2。误差面板用对数纵轴，显示下限10⁻¹⁵只为绘图，不把低于该值的差异声称为精确测量。</figcaption></figure>

## 定积分是有条件的累积极限

### Riemann和的区间宽度不能漏掉

把[a,b]划分为小区间，第i段宽Δxi，选段内一点ξi，构成Σf(ξi)Δxi。若当最大区间宽度趋于0时，这些和对任意合格划分及取点都趋于同一有限值，便定义Riemann定积分∫aᵇ f(x)dx。不是只让某一段变窄，也不是只观察某一种取点恰好收敛。[8](#ref-calc-integral)

连续函数在有限闭区间上可积；有限个有界跳变也不必破坏可积性。但并非所有有界函数都Riemann可积，例如有理点取1、无理点取0的函数，在任意小区间内仍能分别取到0与1。更一般的Lebesgue积分另有定义，见[泛函分析](../functional-analysis/)，本文不把不同积分体系混在一起。

对f(x)=x²、区间[0,1]，N个等宽小区间取中点时，和为1/3−1/(12N²)。N=4得0.328125，N=16得0.3330078125，极限为1/3。有限矩形是近似，极限才是定积分；图4展示的两种网格只是这个已解析验证关系的例子。

### “面积”要保留正负与单位

若f≥0，积分可解释为曲线与横轴间的几何面积；f有正有负时，定积分给出带符号净累积，几何面积要积分|f|。反向积分∫bᵃ f=−∫aᵇ f，且相邻区间可以相加。积分的单位是“函数单位×自变量单位”，例如Pa·s，不因画成面积就一定是m²。

定积分是一个数；不定积分∫f(x)dx表示原函数族F(x)+C，要求F′=f。积分常数不能丢失，它记录由求导无法恢复的整体偏移。原函数存在也不保证能用有限个熟悉的初等函数写出，计算时可采用特定函数或数值方法。[8](#ref-calc-integral)[9](#ref-calc-ftc)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/riemann-sums.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/calculus/riemann-sums.svg" alt="平方函数在零到一上用四个与十六个中点矩形近似积分。" width="1400" height="550" loading="lazy" /></a><figcaption>图4　累积要把高度乘以区间宽度。左右分别用4与16个等宽中点矩形逼近x²在[0,1]的积分1/3，使用相同坐标尺度；变量无量纲，图中的矩形有限近似不代替可积性的定义或证明。</figcaption></figure>

## 微积分基本定理连接变化与累积

### 两个方向分别看清条件

若f在[a,b]连续，定义F(x)=∫aˣ f(t)dt，则F在内点可导且F′(x)=f(x)。理由是F(x+h)−F(x)等于短区间上的累积，除以h后由连续性趋于f(x)。这说明累积函数的局部增长率由当前被积函数给出。[9](#ref-calc-ftc)

反向地，在同样的连续条件下，若G′=f，则
$\int_a^b f(x)\,dx=G(b)-G(a)$。
这让我们用端点处原函数之差计算整体累积。连续条件是这里方便且充分的版本，并非所有推广中都必要；若存在跳变，累积函数不一定在跳点可导，不能原样套用处处等式。

积分变量t是占位符，与上限x的角色不同。若F(x)=∫aᵍ⁽ˣ⁾ f(t)dt，在相应连续与可导条件下F′=f(g(x))g′(x)，上限的链式因子不能漏掉。被积函数本身也随参数变动时，还会出现对参数的偏导项；交换导数与积分需要额外的连续性或支配条件，不能只凭符号相邻就交换。

### 换元与分部积分来自求导规则

**换元积分**对应链式法则。一个充分的有限区间版本是φ在[α,β]连续可导、f在其像所在区间连续，则
$\int_\alpha^\beta f(\phi(u))\phi'(u)\,du=\int_{\phi(\alpha)}^{\phi(\beta)}f(x)\,dx$。
上下限与方向随变换一起改变；例如t=τu时dt=τdu，时间因子τ不能遗漏。[10](#ref-calc-substitution)

**分部积分**对应乘积法则：当u、v在[a,b]连续可导时，∫aᵇ uv′=[uv]aᵇ−∫aᵇ u′v。边界项有具体数值，不能因为常把它写在方括号里就删去。例如∫0¹ xeˣdx=1，可由u=x、v=eˣ求出。[11](#ref-calc-techniques) 反常积分中使用这些公式还须另外检查边界极限。

### 正弦净累积为零 仍可有非零均方

设p(t)=A sin(2πt/T)，A=1 Pa、T=10 ms。完整一周期上∫pdt=0，正负部分抵消；但∫|p|dt=2AT/π≈0.006366 Pa·s，∫p²dt=A²T/2=0.005 Pa²·s。三种累积是不同的量。

均方是T⁻¹∫p²dt，单位Pa²；均方根RMS再取平方根，本例为A/√2≈0.7071 Pa。A/√2适用于这个零均值正弦在完整周期等相应平均条件下，不是任意短窗、任意波形的通用换算。声压平方积分也不直接等于焦耳，真实声能还需传播、阻抗和空间条件，详见[声波与传播](../sound-waves-and-propagation/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/cumulative-cycle.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/calculus/cumulative-cycle.svg" alt="一个周期正弦声压的正负面积，以及随时间先增加再减少的净累积函数。" width="1400" height="550" loading="lazy" /></a><figcaption>图5　零净累积不等于没有波动。A=1 Pa、T=10 ms，左图正负声压区分别着色；右图F(t)=∫从0至t的p(s)ds，以Pa·s计，在半周期最大、完整一周期回到0。均方与RMS在正文另按平方积分定义。</figcaption></figure>

## 反常积分和级数都要检查收敛

### 无穷区间与无界端点另取极限

反常积分∫1∞ f(x)dx定义为limR→∞∫1ᴿ f(x)dx；只有极限有限才称收敛。端点无界时也须先避开奇点，再取单侧极限。多个奇点或无穷端要分别收敛，不能用某种对称抵消掩盖各自发散。[12](#ref-calc-improper)

例如∫1ᴿ x⁻¹dx=ln R，随R增长而发散；∫1ᴿ x⁻²dx=1−1/R，收敛到1。一般∫1∞ x⁻ᵖdx在p>1时收敛，而∫0¹ x⁻ᵖdx在p<1时收敛；同一个幂函数在远端与零附近有不同条件。

在[−1,1]上积分1/x，左右反常积分分别发散，通常意义的积分不存在；若强制用对称删去区间得到0，那是Cauchy主值，不能把主值0当作原反常积分收敛。[12](#ref-calc-improper)

### 级数由部分和定义 不是由单项趋零定义

数列是按n排列的一串数；**级数**Σan的和指部分和SN=Σ从1到N的an在N→∞时的极限。an→0是收敛的必要条件，不是充分条件：调和级数Σ1/n发散，而Σ1/n²收敛；图6将这与相应积分对照。[13](#ref-calc-series)

几何级数Σ从0开始的rⁿ在|r|<1时和为1/(1−r)。对一般幂级数Σcn(x−a)ⁿ，需说明收敛半径，边界点另查；不能将圆内或区间内结论直接沿用到端点。绝对收敛指Σ|an|有限，比条件收敛更强；任意重排、交换无限和与积分或逐项求导都需对应条件。

傅里叶展开、滤波器冲激响应和概率期望都可能涉及无穷过程，但使用的收敛概念与信号空间不总相同。有限图上看起来“很接近”不等于已证明逐点、一致或均方收敛，后续可读[泛函分析](../functional-analysis/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/convergence.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/calculus/convergence.svg" alt="比较倒数和倒数平方的截断积分及级数部分和，展示单项趋零与整体收敛的区别。" width="1400" height="550" loading="lazy" /></a><figcaption>图6　尾部越来越小，累积仍可能无界。左图分别为ln R与1−1/R，右图为Σ1/n与Σ1/n²的前N项，横轴采用对数尺度，所有量均无量纲。有限绘图区只能展示趋势，收敛结论由解析判据支持。</figcaption></figure>

## 多元微分区分单方向变化与整体近似

### 偏导数固定其他变量

对f(x,y)，偏导fx(a,b)是h→0时[f(a+h,b)−f(a,b)]/h的极限，即只改变x、固定y；fy类似。实际测量中若两个量同时变动，观测到的变化率一般不能直接等同其中一个偏导。[14](#ref-calc-partial)

**多元可微**比两个偏导存在更强。令增量向量h=(h1,h2)，其长度‖h‖=√(h1²+h2²)；要求
$f(\mathbf a+\mathbf h)=f(\mathbf a)+f_x(\mathbf a)h_1+f_y(\mathbf a)h_2+o(\|\mathbf h\|)$。
也就是同一线性近似对所有方向的充分小增量都有效。在邻域内偏导存在且连续是可微的一个充分条件，并非必要条件。[15](#ref-calc-differentiable)

反例F(x,y)=xy/(x²+y²)（非原点），F(0,0)=0。沿坐标轴F恒为0，原点两个偏导都为0；沿y=x且x≠0却恒为1/2，所以原点不连续，更不可微。只验证两个轴或有限几条路径不足以证明多元极限存在。

### 梯度需要指定坐标与尺度

梯度∇f=(fx,fy)把偏导排成向量；若f可微，沿单位向量v的方向导数为∇f·v。这个点积是对应分量乘积之和，给出沿该方向每单位位移的变化率。欧氏度量下，非零梯度方向使这一变化率最大。[16](#ref-calc-gradient)

图7取无量纲L(a,b)=(a−1)²+4(b+0.5)²，在(2,0.25)梯度为(2,6)，最小值在(1,−0.5)。若把一个参数的单位或尺度改掉，“单位长度”与最陡方向也会变化；不同物理单位的分量不能不加尺度处理就作直观长度比较。

对多元复合关系，链式法则表现为各条变化路径的贡献相加。例如x=x(t)、y=y(t)时，df/dt=fx dx/dt+fy dy/dt，前提是f及路径具有相应可微性。二阶偏导排成Hessian矩阵可描述局部二次形状；混合偏导在邻域连续等充分条件下才可交换次序。

### 灵敏度不自动等于随机误差传播

小扰动下Δf≈∇f·Δx是确定性的一阶近似。若Δx又是小的随机扰动，其协方差矩阵Σ记录各分量的方差和共同变动，则线性化方差约为∇fᵀΣ∇f；忽略相关性只对相应协方差为0的情形成立。模型非线性或扰动较大时，余项可能不可忽略；这连接[数理统计](../mathematical-statistics/)，不能把局部导数本身叫作置信区间。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/multivariable.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/calculus/multivariable.svg" alt="二元二次函数的等高线和梯度方向，以及原点偏导存在却不连续的路径反例。" width="1400" height="550" loading="lazy" /></a><figcaption>图7　偏导与可微承担不同要求。左图L=(a−1)²+4(b+0.5)²，箭头沿(2,0.25)处梯度方向缩短显示，不把箭头长度当作原向量模；右图F沿轴为0、沿y=x为1/2，但原点定义为0。全部坐标无量纲。</figcaption></figure>

## 重积分把局部密度与空间范围一起累积

### 面积权重与积分次序

二重积分∬D q(x,y)dA由小面积上的贡献qΔA相加取极限建立。如果q是面密度，积分得到总量；若q是一般场，则结果单位为q的单位乘面积。平均值还须除以区域面积，不是把积分符号改个名称。[17](#ref-calc-multiple)

在闭矩形上连续时，可按两个变量先后作迭代积分，两个次序结果相同。对更一般或无界问题，绝对可积等条件可保证相应交换；不能在存在发散或条件抵消时随意换次序。积分区域若非矩形，内层上下限通常依赖外层变量，画清区域比机械抄限更可靠。

### 换坐标要带上Jacobian

极坐标x=r cosθ、y=r sinθ，把小面积变为r dr dθ；半径越大，相同角宽与径向宽度围出的面积越大。这个r来自坐标变换的Jacobian绝对值，即局部面积缩放因子，不是可省略的装饰。[18](#ref-calc-polar)

例如无量纲径向函数q=exp[−(x²+y²)/2]在半径R=3圆盘上的积分为
$\int_0^{2\pi}\int_0^3 e^{-r^2/2}r\,dr\,d\theta=2\pi(1-e^{-9/2})\approx6.21339$。
整个平面上的积分则为2π。未除以2π时q不是归一化概率密度；这有助于理解[概率论](../probability-theory/)里的密度为何必须与积分测度一起读。

线积分和曲面积分进一步沿曲线或曲面累积，涉及弧长、方向与法向；散度、旋度及Green、Gauss、Stokes定理还要求明确场的光滑性和区域边界。这里不把它们简化成“把二重积分多加一个积分号”，连续声场的后续学习可接[数学物理方法](../mathematical-physics-methods/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/polar-integral.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/calculus/polar-integral.svg" alt="圆盘上的径向高斯函数与带面积权重的径向积分，说明极坐标中的半径因子。" width="1400" height="550" loading="lazy" /></a><figcaption>图8　局部函数值相同不代表面积贡献相同。左图q=exp(−r²/2)及等宽圆环，右图比较q(r)与圆环累积密度2πrq(r)；圆心q最高，但圆心附近圆环面积很小。R=3，全部变量无量纲，非空间声场或神经组织测量。</figcaption></figure>

## 微分方程把变化规律与初值放在一起

### 方程规定导数 初值选择具体轨迹

常微分方程把未知函数与其导数联系起来；**初值问题**还规定起始时刻的函数值。例如τy′+y=x(t)，τ>0以s计，x和y具有相同单位。它描述变化率由当前输入与状态之差决定，是一阶线性模型。[19](#ref-calc-ode)

把方程乘以积分因子exp(t/τ)，由乘积法则并积分可得
$y(t)=e^{-t/\tau}y(0)+\tau^{-1}\int_0^t e^{-(t-s)/\tau}x(s)\,ds$。
当x连续时，这个式子给出满足方程与初值的唯一解；输入分段连续时可在相应区间与连接条件下理解。第一项来自初始状态，第二项来自输入，不能默认第一项永远为0。

若t≥0时x=1，解为y(t)=1+[y(0)−1]exp(−t/τ)。取τ=5 ms、y(0)=0，经过一个时间常数后达到1−e⁻¹≈0.6321；若初值为0.4，同一时刻达到约0.7793。它不是所有膜、电路或听觉响应的普遍曲线，只是明确一阶模型的结果；相关物理条件可读[生物物理学](../biophysics/)与[电路原理](../circuit-theory/)。

### 存在 唯一 稳定与求解精度分别检查

一般非线性问题不能仅凭右端连续就认定初值解唯一。例如y′=√|y|、y(0)=0，在t≥0既有零解，也有y=t²/4等解。解析代入可以逐一核对；程序返回一条曲线不能排除其他解。

模型自身的稳定性还不同于数值格式的稳定性。对上面τ>0的一阶模型，两条解之差按exp(−t/τ)衰减；显式Euler近似却满足y[n+1]=y[n]+h(1−y[n])/τ，误差递推因子为1−h/τ。要使这个因子模小于1，需0<h<2τ；越过边界即可能出现人工增长。

在这个简单模型中，h=1 ms平滑趋近，h=8 ms交替但衰减，h=12 ms交替增长。数值稳定也不保证误差已足够小；大步长即便没有发散，也可能漏掉重要的时间细节。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/ode-initial-state.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/calculus/ode-initial-state.svg" alt="一阶初值问题在不同初值下的解析响应，以及Euler不同步长导致的衰减或人工增长。" width="1400" height="550" loading="lazy" /></a><figcaption>图9　初值改变轨迹，数值格式还会带来自己的问题。模型τy′+y=1、τ=5 ms；左图初值0与0.4，右图初值0、Euler步长1、8、12 ms，与解析解比较。输入输出无量纲，时间用ms，未模拟具体器件。</figcaption></figure>

## 从连续公式到数值结果要保留误差

### 差分步长存在取舍

前向差分[f(x+h)−f(x)]/h在足够光滑时截断误差通常为O(h)，中心差分[f(x+h)−f(x−h)]/(2h)通常为O(h²)；O表示h趋小时误差可被某个常数乘该幂控制。所需的导数存在且有界等条件必须成立，尖点和跳变不能照搬这些阶数。

浮点计算相近数相减会丢失有效数字，除以极小h后还会放大误差。若两次测量误差独立、方差均为σ²，中心差分中的噪声方差是σ²/(2h²)；更密的时间差不自动给出更可靠的斜率。有关方差公式来自线性组合与协方差展开，而非对所有录音噪声的独立性保证。

图10一边画float64对eˣ在x=1处求导的误差，一边画指定独立噪声模型下的放大。最合适的h随函数尺度、精度、噪声与方法而变，不存在所有问题统一使用的极小数。

### 求积与初值求解也有假设

复合梯形法将相邻样值用线段连接后积分。等距且函数有足够有界二阶导数时，全区间误差为O(h²)；复合Simpson法在等距、偶数个小区间和足够四阶光滑性下可达到O(h⁴)。提高形式阶数不补回未采集的高频信息，也不使不连续输入自动光滑。[20](#ref-calc-numerical)

例如∫0¹ x⁴dx=0.2，8个小区间时梯形结果0.2052002、Simpson结果0.2000326；16个小区间时误差约分别降为原来的1/4和1/16。这里端点与函数已知且无噪声，不能将它当作真实录音积分的通用误差表。

软件接口还要核对间隔、次序和轴。trapezoid若不给x或dx，默认间隔为1；以时间样本积分却漏乘Ts，会改变数值与单位。传入x时该接口按给定顺序积分，不自动排序；真实时间戳也要检查单调性与丢样。[21](#ref-calc-trapezoid-api)

自适应初值求解器会估计局部误差并调整内部步长。solve_ivp的rtol与atol参与误差控制，但不直接保证全局真实误差小于同一个数；t_eval指定输出时刻，不等于强制内部按这些点等步长走。还需检查成功标志、方法、步长限制和适合问题尺度的容差。[22](#ref-calc-ivp-api)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/calculus/numerical-differentiation.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/calculus/numerical-differentiation.svg" alt="数值求导误差随步长先减小后受舍入影响，以及独立噪声在小步长中心差分中的放大。" width="1400" height="550" loading="lazy" /></a><figcaption>图10　更小的步长并不总更准确。左图float64对eˣ在1处求导，误差绘图下限10⁻¹⁶；右图两样值独立加性噪声σ=10⁻⁶，中心差分噪声标准差理论为σ/(√2h)，以种子20261102的100000对噪声复算。变量均无量纲，非测量噪声估计。</figcaption></figure>

### 三个可独立运行的例子

以下在NumPy 1.26.4、SciPy 1.17.1运行；本轮查看的SciPy在线文档为1.18.0。公式核对与接口版本分开记录，未声称在未运行的版本上测试。

例1把高斯脉冲的解析导数与中心差分比较。时间使用秒，输出为Pa/s；这只是一个指定步长的局部核对，不证明任意h都准确。

```python
import numpy as np
A, tau, a, h = 1.0, 0.002, 0.002, 1e-5
def p(t):
    return A*np.exp(-t*t/(2*tau*tau))
analytic = -a*p(a)/(tau*tau)
central = (p(a+h)-p(a-h))/(2*h)
assert np.isclose(central, analytic, rtol=1e-4)
print(analytic, central)  # Pa/s
```

例2分别计算净累积与均方根，显式传入时间坐标，避免把Pa·s、Pa²·s与Pa混在一起。这个网格包括两个端点，共480个时间间隔。[21](#ref-calc-trapezoid-api)

```python
import numpy as np
from scipy.integrate import trapezoid
T = 0.01
t = np.linspace(0, T, 481)
p = np.sin(2*np.pi*t/T)  # Pa，幅度1
net = trapezoid(p, x=t)  # Pa*s
square = trapezoid(p*p, x=t)  # Pa**2*s
rms = np.sqrt(square/T)  # Pa
assert abs(net) < 1e-14
assert np.isclose(square, 0.005)
assert np.isclose(rms, 1/np.sqrt(2))
print(net, square, rms)
```

例3在同一初值下比较数值轨迹与解析解。这里的误差是已知教学模型上的实际差值，与求解器局部误差控制参数不是同一概念。[22](#ref-calc-ivp-api)

```python
import numpy as np
from scipy.integrate import solve_ivp
tau = 0.005
t = np.linspace(0, 0.03, 301)
sol = solve_ivp(lambda t, y: (1-y)/tau, (0, 0.03), [0.4],
                method="RK45", t_eval=t, max_step=0.001,
                rtol=1e-9, atol=1e-12)
assert sol.success
exact = 1-0.6*np.exp(-t/tau)
error = np.max(np.abs(sol.y[0]-exact))
assert error < 1e-8
print(error)
```

### 用问题检查定义与解释

1. 修改一个点值为何可能破坏连续，却不改变该点极限？数值表格和ε—δ证明提供的保证有何不同？
2. 高斯脉冲在峰顶导数为0，是否说明它在附近没有变化？横轴由s改为ms时，斜率的数字怎样变化？
3. 1−u近似e⁻ᵘ时，0.02的绝对误差上界为何不等于2%的相对误差？有限Taylor多项式与无限级数还差哪个收敛问题？
4. 完整正弦周期的净累积为0，为什么RMS仍非零？声压平方积分还缺什么条件才能解释为物理能量？
5. 两个偏导存在为什么不能保证可微？更换参数尺度为什么会改变“最陡方向”的解释？
6. 极坐标中漏掉r会如何改变结果？反常积分左右各自发散，能否用对称抵消称为收敛？
7. 连续模型稳定时，Euler为何仍可能增长？求导步长、积分步长和求解器容差分别控制什么？

来源主要为OpenStax官方微积分教材的对应章节及SciPy官方接口说明。同一教材的多个章节用于明确命题位置，不当作多项独立实验；图形、参数和数值均为独立教学计算。本轮完成定义、条件、单位、来源与计算核对，仍保留待专业审阅状态。
