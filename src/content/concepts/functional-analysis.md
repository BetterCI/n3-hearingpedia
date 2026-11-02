---
title: "泛函分析"
english: "Functional Analysis"
slug: "functional-analysis"
summary: "从声音信号的距离与收敛出发，理解赋范空间、Banach与Hilbert空间、正交投影、连续线性算子、对偶与Riesz表示，再进入基本定理、弱收敛、紧算子、谱、Sobolev空间和变分问题，以模态、测量与逆滤波例子说明无限维分析的作用和边界。"
categories: ["research-methods", "signal-processing", "acoustics"]
tags: ["基础课程", "泛函分析", "函数空间", "Hilbert空间", "对偶空间", "线性算子", "弱收敛", "谱理论"]
aliases: ["函数分析", "泛函分析基础", "听觉研究中的泛函分析", "Functional Analysis for Hearing Research"]
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
  - {label: "课程主线", value: "空间与拓扑、连续性、对偶、算子及方程的可解性"}
  - {label: "核心区别", value: "有限维与无限维、强与弱收敛、有界与无界算子"}
  - {label: "直观入口", value: "信号误差、正交分解、有限窗测量、平滑与逆问题"}
  - {label: "研究边界", value: "数学适定性、离散精度与实际听觉模型有效性须分别核验"}
references: ["fa-norm", "fa-lp", "fa-hilbert", "fa-riesz", "fa-basis", "fa-fourier", "fa-operator", "fa-adjoint", "fa-hb", "fa-double", "fa-baire", "fa-inverse", "fa-weak", "fa-compact", "fa-spectrum", "fa-selfadj", "fa-spectral", "fa-sobolev", "fa-lm", "fa-dirichlet", "fa-regularization", "fa-fixedpoint"]
order: 1024
---

**泛函分析**（functional analysis）研究带有距离、收敛或拓扑结构的向量空间，以及这些空间之间的算子和取标量值的泛函。它把“向量”从有限个数推广到函数、数列等对象，同时认真处理无限过程：近似是否收敛？极限还在允许的空间里吗？求解器对应的逆映射是否会放大误差？[1](#ref-fa-norm)

听觉与声学研究中的信号、模态、滤波和场方程都能带来这些问题。例如均方误差很小的声音仍可含尖峰；某个平滑过程向前稳定，反演却可能极不稳定；有限矩阵总有的性质，未必能直接延续到连续模型。泛函分析提供组织这些问题的语言与定理，不直接等同一套新的音频处理算法。

本篇从有限向量与误差比较进入抽象定义；微积分、[线性代数](../linear-algebra/)及初步实分析支持进一步推导。复信号与方程应用可分别按需查阅[复变函数](../complex-analysis/)和[数学物理方法](../mathematical-physics-methods/)。本篇围绕入门核心概念展开，并介绍Sobolev与逆问题的用途；不代替测度论、一般拓扑或完整算子理论课程。十幅图与全部计算均为原创指定模型，不是临床、听者或器件实测。

## 阅读准备与独立阅读

**起步知识。** 先熟悉数的加法、数乘、坐标与简单函数图像，即可开始比较向量大小和近似误差。深入定理条件、证明与函数空间例子时，还需逐步熟悉极限、连续、级数、积分和线性映射；这些工具仍需相应练习。

**随用随补。** 在二维中，(3,4)的欧氏长度为5；范数把“大小”的规则推广到其他对象，两个对象的距离可用其差的范数表示。收敛指到一个指定极限的距离趋于0；Cauchy条件只比较序列后部元素彼此的距离。算子先看成把输入向量或函数变成输出的规则。

**分层阅读。** 第一遍从有限向量出发，读范数、完备、投影和基，再用峰值与均方误差的对照理解不同收敛。第二遍核对对偶、基本定理、弱收敛、谱与Sobolev内容。复内积和弱导数在相关段落解释，严格证明可配合线性代数与实分析逐步学习。

## 从距离开始 赋范空间与完备性

### 向量不一定是一列有限数字

在实数域或复数域上，**向量空间**要求向量可相加、可数乘，并满足相应代数规则。有限长波形是 $\mathbb R^N$ 中的向量；整段连续时间函数也可以组成向量空间，但“所有函数”“连续函数”“平方可积函数”是不同集合，不能在推导中无声替换。

**范数** $\|x\|$ 衡量向量大小，要求非负且仅零向量范数为零、绝对齐次 $\|\alpha x\|=|\alpha|\|x\|$、三角不等式 $\|x+y\|\le\|x\|+\|y\|$。它诱导距离 $d(x,y)=\|x-y\|$。满足这些条件的向量空间称**赋范空间**。[1](#ref-fa-norm)

有限向量常用 $\|x\|_1=\sum|x_k|$、$\|x\|_2=(\sum|x_k|^2)^{1/2}$、$\|x\|_\infty=\max|x_k|$。它们回答的误差问题不同：总绝对偏差、平方和大小和最大分量。对记录的声压，平方积分与均方值有关，但要结合时间归一、声阻抗和几何才能解释具体声能，不能把任意范数都叫物理能量。

### Cauchy列为什么还需要极限存在

若对每个ε>0，存在N使m,n>N时 $\|x_n-x_m\|<\varepsilon$，则 $(x_n)$ 是**Cauchy列**：序列后部彼此越来越接近。它不预先给出极限对象。若空间内每个Cauchy列都收敛到空间内的元素，该空间称**完备**；完备赋范空间称**Banach空间**。[1](#ref-fa-norm)

完备性不意味着每个有界序列都收敛，也不意味着算法总会收敛。它确保已经满足Cauchy条件的近似不会“走出空间”。例如[0,1]上的连续函数配最大范数是Banach空间；同一集合若配平方积分范数，却不完备，因为连续函数可以在该范数下逼近不连续的阶跃。其完备化与 $L^2$ 空间相联系，下一节给出具体序列。

### 有限维直觉在哪一步失效

在固定有限维空间上，任意两种范数等价：存在正的c、C使 $c\|x\|_a\le\|x\|_b\le C\|x\|_a$。因此它们给出相同的收敛拓扑，但误差数值和几何仍不同。常数也依赖维数，例如 $\|x\|_\infty\le\|x\|_2\le\sqrt N\|x\|_\infty$。[1](#ref-fa-norm)

当N不断增加，不能默认这些常数保持一致；无限维中不同范数甚至可产生不同的收敛。另一个关键区别是：无限维赋范空间的闭单位球在范数拓扑下不紧。“有界且闭”在有限维欧氏空间成立的紧致结论，不能直接移植。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/norm-geometry.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/functional-analysis/norm-geometry.svg" alt="二维一范数、二范数和无穷范数的单位球分别呈菱形、圆和方形，另一面板展示范数比较常数随维数增长。 " width="1400" height="550" loading="lazy" /></a><figcaption>图1　同一向量可以有不同的大小。右图对全1向量比较二范数与最大范数，比例为维数的平方根；这说明固定维数的范数等价不能直接提供无限维的一致控制。</figcaption></figure>

## Lp空间 几乎处处与收敛方式

### 平方可积不是处处有限误差的保证

对明确测度的域，$1\le p<\infty$ 时定义

$$
\|f\|_p=\left(\int |f|^p\,d\mu\right)^{1/p}.
$$

$L^\infty$ 范数为本质上确界。**$L^p$空间**由这些范数有限的可测函数按“几乎处处相等”识别后组成；在本文的Lebesgue区间上，这些空间都是Banach空间。[2](#ref-fa-lp)

**几乎处处**表示允许在测度为零的集合上例外。因此只在一个时刻取值不同的两条函数，在 $L^2$ 中是同一个元素。没有这个识别，积分只给半范数，非零的逐点函数也可能范数为零。**本质上确界**同样忽略零测集的例外，不等于随意选一组离散采样点中的最大值。

在有限测度区间上，q≥p时有 $\|f\|_p\le\mu(\Omega)^{1/p-1/q}\|f\|_q$；全实线等无限测度域不自动有这种包含关系。p<1时同一表达式通常只有拟范数，三角不等式不再按上述形式成立，本篇不将它称为Banach范数。

### 连续近似可以收敛到不连续对象

令 $f_n(t)=\min\{1,\max[0,n(t-\tfrac12)]\}$，n≥2。它从t=1/2开始，经过宽1/n的连续斜坡升到1；极限可取阶跃 $f(t)=\mathbf1_{(1/2,1]}(t)$。直接分段积分得 $\|f_n-f\|_2^2=1/(3n)$，趋于零，故 $(f_n)$ 在这个范数下也是Cauchy列。

极限在 $L^2$ 中存在，却不能由任何连续函数几乎处处代表，所以“连续函数集合配 $L^2$ 范数”不完备。相同序列不一致收敛到阶跃。**强收敛**在此通常指范数收敛；**逐点收敛**则逐个固定t检查数值，两者不能互相替换。[2](#ref-fa-lp)

### 窄脉冲展示点评价的问题

取连续三角尖峰 $h_n(t)=\max(1-n|t-\tfrac12|,0)$。其峰高始终1，而 $\|h_n\|_2^2=2/(3n)\to0$。因此即使只在连续函数上尝试以 $L^2$ 范数控制点评价 $f\mapsto f(1/2)$，也不连续；在整个 $L^2$ 等价类上，点评价甚至没有代表元无关的定义。

这不说明真实测量“毫无意义”，而是应区分模型。理想点评价、有限窗平均、带宽受限测量与离散采样是不同算子。若要证明峰值或采样值稳定，需要更强的空间条件或特定带限假设，不能仅凭均方误差。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/convergence-and-spikes.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/functional-analysis/convergence-and-spikes.svg" alt="连续斜坡在平方积分中逼近阶跃，三角窄脉冲的二范数减小而峰高保持不变。 " width="1400" height="550" loading="lazy" /></a><figcaption>图2　范数决定“接近”的含义。横坐标为归一化时间，曲线为数学反例；左图的阶跃属于L²，右图说明L²收敛不控制最大幅值，不表示实际音频仪器具有无限带宽。</figcaption></figure>

## Hilbert空间与正交投影

### 内积给出长度和角度

**内积**在复空间上需包含共轭对称、正定和一侧线性。本篇采用**第一变量共轭线性、第二变量线性**的约定：
$$
\langle f,g\rangle=\int f^*(t)g(t)\,dt,\qquad
\|f\|=\sqrt{\langle f,f\rangle}.
$$

它满足Cauchy–Schwarz不等式 $|\langle f,g\rangle|\le\|f\|\|g\|$。不同教材可能反过来规定线性变量，公式中的共轭位置必须一起调整。[3](#ref-fa-hilbert)

由内积范数完备的空间称**Hilbert空间**。$\ell^2$ 与 $L^2$ 是重要例子；一般 $L^p$ 范数在p≠2时不由内积产生。内积范数满足平行四边形恒等式 $\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2$，它体现特殊几何，不是所有Banach空间都有正交投影公式。

### 投影定理为什么强调闭子空间

对Hilbert空间H的**闭线性子空间**M，每个f都有唯一分解 $f=P_Mf+r$，其中 $P_Mf\in M$、r与M正交。$P_Mf$ 是M中使 $\|f-v\|$ 最小的元素，且 $\|P_M\|\le1$；M非零时范数等于1。[4](#ref-fa-riesz)

“闭”不能略去。若M稠密却非闭，而f不在M中，距离下确界可为零，但没有任何v达到它。若集合仅为非空闭凸集，仍存在唯一最近点，但对应投影一般不是线性算子；若集合非凸，最近点又可能不唯一。不能把最小二乘的所有几何都归给同一个公式。

### 用两个音调解释最佳近似

在归一化区间[0,1]取
$$
f(t)=\sin(2\pi t)+0.4\cos(4\pi t)+0.2\sin(6\pi t).
$$

用前两项张成的子空间近似。正交投影为 $p(t)=\sin(2\pi t)+0.4\cos(4\pi t)$，残差为第三项；它与每个允许的修正方向正交。

本例 $\|f\|_2^2=0.6$、$\|p\|_2^2=0.58$、$\|f-p\|_2^2=0.02$，满足勾股关系。这里完整周期、均匀权重保证所选三项正交；更短观察窗、不同权重或非整数周期时要重新计算Gram矩阵，不能把任意两个频率都当成正交坐标。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/orthogonal-projection.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/functional-analysis/orthogonal-projection.svg" alt="一个三音调函数投影到前两项张成的空间，残差与投影正交，右图核对三个平方范数。 " width="1400" height="550" loading="lazy" /></a><figcaption>图3　投影保留子空间能表达的部分。横坐标为归一化时间，纵轴无量纲；平方范数是积分值，不是每个时刻的功率。正交性依赖本例的完整区间和权重。</figcaption></figure>

## 正交基 级数与有限维近似

### 正交还不够 必须覆盖整个空间

集合 $\{e_n\}$ 若满足 $\langle e_m,e_n\rangle=\delta_{mn}$，称**正交归一系**。只有其有限线性组合的闭包等于H时，才是Hilbert意义的**完备正交基**。可分Hilbert空间有可数正交基；这不是要求每个向量只用有限项表示的Hamel基。[5](#ref-fa-basis)

令 $c_n=\langle e_n,f\rangle$。对任意正交归一系，Bessel不等式 $\sum|c_n|^2\le\|f\|^2$ 成立；若系完备，才得到Parseval等式与范数收敛的展开 $f=\sum c_ne_n$。只保留部分模态时，未表示的能量可能位于被遗漏的正交补中。

### Fourier展开首先是哪一种收敛

在[0,1]上，复指数 $e^{j2\pi nt}$，n为全部整数，构成 $L^2$ 的正交基；从而Fourier部分和在 $L^2$ 范数中收敛。这个结论不自动给一致或处处逐点收敛。边界周期化、数据光滑性及采用普通部分和还是Fejér平均，都与更强结论有关。[5](#ref-fa-basis)[6](#ref-fa-fourier)

正弦基可描述零端点边值问题的模态，但“函数展开在 $L^2$ 中成立”不表示任意代表函数的端点值被该范数控制。边界条件应在适当函数空间与迹的意义下表述，而不是只观察级数在端点代入为零。

### 截断误差与离散测量误差不同

对前N个基向量，$P_N f=\sum_{n=1}^Nc_ne_n$ 的平方误差等于完整基中尾部 $\sum_{n>N}|c_n|^2$。但是数值积分、混叠、有限精度和观测噪声会使实际计算的系数偏离真值，这些误差不包含在理想尾和公式里。

例如一个完整正交基下的人工系数 $c_n=1/n$ 属于 $\ell^2$，总平方和π²/6有限，尾部逐渐减小；它不属于 $\ell^1$，不能仅凭平方可和就断言绝对一致收敛。图4只画系数和尾和，不宣称指定时间波形的所有逐点性质。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/basis-and-tails.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/functional-analysis/basis-and-tails.svg" alt="系数1/n平方可和但不绝对可和，右图显示有限项投影的平方尾误差随截断阶数下降。 " width="1400" height="550" loading="lazy" /></a><figcaption>图4　无穷展开的误差由尾部控制。采用人工指定的正交坐标系数；右图尾和由π²/6减去已保留平方和计算，有限项结果不是整个无限维空间的数值证明。</figcaption></figure>

## 连续线性算子 伴随与定义域

### 线性不等于连续

**线性算子**A:X→Y保持加法与数乘。它称**有界**，若存在有限C使 $\|Ax\|_Y\le C\|x\|_X$ 对所有x成立；最小常数为算子范数
$$
\|A\|=\sup_{\|x\|_X\le1}\|Ax\|_Y.
$$

对赋范空间之间、定义在整个X上的线性映射，有界与连续等价。“有界”不是输出对所有任意大输入都不超过一个固定数。[7](#ref-fa-operator)

例如h∈L¹时，卷积满足 $\|h*f\|_2\le\|h\|_1\|f\|_2$；在相应全空间框架下，它给出稳定的能量范数控制。L²有界性与以L∞输入输出定义的BIBO稳定性是不同命题，不能只因都叫“稳定”就互换。

### 微分为什么可能是不连续操作

在[0,1]上取 $e_n(t)=\sqrt2\sin(n\pi t)$，则 $\|e_n\|_2=1$、$\|e_n'\|_2=n\pi$。因此求导D不能作为有界算子从配L²范数的这些函数映到L²；若取 $e_n/n$，输入范数趋零，导数范数仍为π。

更准确地，应写**无界算子** $D:\mathcal D(D)\subset L^2\to L^2$ 并指定定义域，例如H¹。给定义域配包含导数的图范数 $(\|f\|_2^2+\|Df\|_2^2)^{1/2}$ 后，D从这个更强空间到L²可有界。不是同一拓扑下突然改变了连续性，而是改了输入空间。

### 伴随不只是把符号转置

对Hilbert空间之间的有界A:H→K，**伴随算子** $A^*:K\to H$ 由
$$
\langle Ax,y\rangle_K=\langle x,A^*y\rangle_H
$$

定义。其存在性来自Riesz表示，且 $\|A^*\|=\|A\|$、$\ker A^*=(\operatorname{ran}A)^\perp$，并有 $\overline{\operatorname{ran}A}=(\ker A^*)^\perp$。[8](#ref-fa-adjoint)

有限维标准内积下就是共轭转置；若离散内积为 $\langle x,y\rangle_M=x^*My$、$\langle u,v\rangle_W=u^*Wv$，正定权矩阵给出 $A^\dagger=M^{-1}A^*W$。因此带网格权重的数值伴随不一定等于裸矩阵的共轭转置。

对稠密定义的无界算子，伴随还必须确定哪些y使相应泛函连续。**自伴**要求 $A=A^*$ 且定义域相同；分部积分只证明形式对称，不能省去边界和定义域。微分算子的边界项正是在这里进入理论。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/derivative-and-domain.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/functional-analysis/derivative-and-domain.svg" alt="单位二范数正弦函数的频率越高，导数二范数越大，图范数则包含这种变化。 " width="1400" height="550" loading="lazy" /></a><figcaption>图5　算子的大小依赖所用空间。左图各曲线具有相同L²范数；右图比较输入范数、导数范数和H¹型图范数。图示解释求导的无界性，不把有限个模态检验当作无限维证明。</figcaption></figure>

## 泛函 对偶与Riesz表示

### 泛函怎样代表一次稳定测量

**泛函**是取标量值的映射，可以线性也可以非线性，例如能量 $\|f\|_2^2$ 是非线性泛函。**连续对偶空间** $X^*$ 只收集连续线性泛函，范数为 $\|\ell\|=\sup_{\|x\|\le1}|\ell(x)|$；即使X尚未完备，$X^*$ 仍是Banach空间。[7](#ref-fa-operator)

在L²中，已知窗函数g定义 $\ell_g(f)=\langle g,f\rangle$，由Cauchy–Schwarz得 $|\ell_g(f)|\le\|g\|_2\|f\|_2$。若 $g_\varepsilon=\varepsilon^{-1}\mathbf1_I$，I宽ε，则这是窗内平均，泛函范数为 $1/\sqrt\varepsilon$。窗口越窄，允许的L²扰动对该测量的最坏影响界越大；有限窗平均不等同数学点评价。

### Riesz表示把连续读数变成一个向量

**Hilbert空间Riesz表示定理**说，每个连续线性泛函ℓ唯一对应g∈H，使 $\ell(f)=\langle g,f\rangle$，且 $\|\ell\|=\|g\|$。本篇内积第二变量线性，因此g到ℓg的对应在复空间中是共轭线性的；换用另一内积约定时要同步调整。[4](#ref-fa-riesz)

这个结论不表示任意代数线性泛函都连续，也不表示任意Banach空间都能用自身内积代表对偶。它为匹配模板、正交投影、伴随和变分问题提供统一表达；若另讨论“最优噪声检测”，还需要明确噪声协方差和统计判据，单凭Riesz定理不能决定最佳听觉实验。

### Hahn–Banach与双对偶

**Hahn–Banach定理**的一种赋范空间形式保证：子空间上的有界线性泛函可延拓到整个空间，并保持范数。子空间不必先假设闭，但泛函必须有界；延拓通常不唯一。它说明连续线性泛函足以区分不同向量，并给出 $\|x\|=\sup_{\|\ell\|\le1}|\ell(x)|$。[9](#ref-fa-hb)

不唯一可以在二维看清：给 $\mathbb R^2$ 配最大范数，在直线M={(t,t)}上定义ℓ(t,t)=t。对任意0≤a≤1，$F_a(x_1,x_2)=a x_1+(1-a)x_2$ 都是全空间上的延拓，范数均为1。它们在M上相同，却可给出不同的线外读数；保范数没有自动选择唯一测量规则。

**双对偶** $X^{**}$ 是 $X^*$ 的连续对偶。自然映射 $J:X\to X^{**}$ 定义为 $Jx(\ell)=\ell(x)$，它是线性等距嵌入；若它满射，称X**自反**。Hilbert空间、本文有限区间上1<p<∞的Lp是自反的；L¹和L∞一般不能如此处理。不要把“可以嵌入双对偶”误说成“总等于双对偶”。[10](#ref-fa-double)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/window-functionals.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/functional-analysis/window-functionals.svg" alt="积分为1的矩形平均窗随宽度变窄而升高，其作为L²连续泛函的范数按宽度负二分之一次方增加。 " width="1400" height="550" loading="lazy" /></a><figcaption>图6　一次测量也有算子范数。横轴为归一化时间，各窗积分均为1；右图是对L²输入的最坏情况增益界，不是特定仪器的噪声实测，也不直接给出采样定理。</figcaption></figure>

## 三个基本定理 什么时候能控制整族或逆映射

### 一致有界原理中的量词

**一致有界原理**：X是Banach空间，Y是赋范空间，$\{T_i:X\to Y\}$ 是一族有界线性算子；若对每个固定x都有 $\sup_i\|T_ix\|<\infty$，则 $\sup_i\|T_i\|<\infty$。逐个x的界起初可以不同，结论却给出整个单位球上的统一控制。[11](#ref-fa-baire)

关键在“对每个x”，不是测了有限组信号就足够；X的完备性也不能随意删去。其背后的Baire纲定理说，非空完备度量空间不能表示成可数个无处稠密集的并。这里给出结构和用途，不以若干数值样本代替定理证明。

### 开映射与有界逆定理

**开映射定理**：Banach空间之间的满射有界线性算子把开集映到开集。因而若A还单射，其逆 $A^{-1}:Y\to X$ 有界。这使“存在且唯一”在这些完整条件下进一步获得范数稳定性。[12](#ref-fa-inverse)

反例也应准确：紧平滑算子常只有稠密真值域，不是到整个目标Banach空间的满射，其逆在值域上可能无界；这不反驳有界逆定理。把值域换一个更强范数可能恢复稳定，但那已经改变了数据空间和误差意义。

### 闭图定理为什么不排斥无界微分

**闭图定理**：若X、Y为Banach空间、线性A定义在整个X，且图 $\{(x,Ax)\}$ 在X×Y中闭，则A有界。图闭意味着xₙ→x且Axₙ→y时必有Ax=y；不是说算子“把闭集合都映成闭集合”。[12](#ref-fa-inverse)

求导等闭无界算子只定义在L²的真子域上，所以不满足“整个X”的前提。把该域配合图范数构成Banach空间，可重新应用有界算子语言。定理的力量来自条件齐备，不是把“闭”“完备”换成口头上的平滑或有限。

## 弱收敛 弱星收敛与紧致性

### 所有连续读数收敛 不等于范数误差变小

若 $\|x_n-x\|\to0$，称强收敛；若对所有 $\ell\in X^*$ 都有 $\ell(x_n)\to\ell(x)$，称**弱收敛**，写 $x_n\rightharpoonup x$。强收敛推出弱收敛，反向一般不成立。Hilbert中可等价用所有固定g的内积读数检查。[13](#ref-fa-weak)

在ℓ²中，标准基向量eₙ满足 $\|e_n\|=1$；对任意g∈ℓ²，其第n个坐标趋零，所以eₙ弱收敛到0，却不强收敛，彼此距离恒为√2。能量可“移向更高坐标”，而任一固定读数逐渐看不见它。只验有限组g的读数，仍不足以单独证明一般弱收敛。

弱收敛序列有界，范数满足 $\|x\|\le\liminf\|x_n\|$，称弱下半连续。Hilbert中若同时有范数收敛到 $\|x\|$，则可推出强收敛。这常用于先获得弱极限，再用能量等式加强结论。

### 弱星收敛测试的是原空间

对 $X^*$ 中的序列，**弱星收敛** $\ell_n\overset{*}{\rightharpoonup}\ell$ 指对每个x∈X有 $\ell_n(x)\to\ell(x)$。$X^*$ 自身的弱拓扑则由 $X^{**}$ 测试；在非自反情形两者可能不同，不能把“弱”和“弱星”当成随意替换的名称。[13](#ref-fa-weak)

Banach–Alaoglu定理保证对偶闭单位球在弱星拓扑下紧。一般的紧致性不等于任意有界序列都可抽出弱星收敛子列；在X可分等适当条件下，闭单位球的弱星拓扑可度量，才方便用序列来描述。自反Banach空间中的有界序列有弱收敛子列，Hilbert空间是常用情形。

### 弱收敛为什么有用 又不能做什么

连续性和紧致性可帮助证明极小化序列存在极限；但非线性运算不自动保持弱收敛。eₙ弱收敛到0，而 $\|e_n\|^2=1$ 不趋于0，就是最直接例子。把弱极限代入非线性项往往需要额外紧嵌入、强收敛或结构性条件。

在声学反演或学习模型中，有限传感器只提供有限读数，未观测到的方向可有大误差。这与弱拓扑有启发联系，却不表示任何有限测量成功都构成数学弱收敛证明。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/weak-and-strong.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/functional-analysis/weak-and-strong.svg" alt="标准基向量的非零坐标不断向后移动，对固定平方可和向量的读数减小而二范数始终为1。 " width="1400" height="550" loading="lazy" /></a><figcaption>图7　固定观察方向看不见，不等于向量变小。左图展示有限个标准基向量；右图用gₙ=1/n的固定ℓ²向量示意读数。对任意ℓ²向量坐标趋零的解析论证，才支持完整的弱收敛结论。</figcaption></figure>

## 紧算子与谱 不能照搬有限矩阵

### 紧算子把有界序列送到可提取的集合

线性A:X→Y称**紧算子**，若有界集合的像相对紧；等价地，每个有界输入序列的像都有范数收敛子列。紧不表示每个像序列本身收敛，也不表示X或Y是有限维。[14](#ref-fa-compact)

有限秩有界算子是紧的；目标空间为Banach空间时，紧算子的算子范数极限仍紧。在Hilbert空间中紧算子可由有限秩算子按算子范数逼近。无限维H上的恒等算子不是紧的，由eₙ例子即可看出。强算子收敛又不同：正交投影Pₙ对每个f满足Pₙf→f，但 $\|I-P_n\|=1$，所以不是算子范数收敛。

### 谱包括没有特征向量的点

对复Banach空间上的有界A，若 $A-\lambda I$ 在整个空间上有有界逆，则λ在预解集；其余λ构成**谱**σ(A)。**特征值**要求存在非零x使Ax=λx，它只是谱的一部分。[15](#ref-fa-spectrum)

例如L²(0,1)上乘法算子 $(Mf)(t)=t f(t)$ 有谱[0,1]，却没有特征值：非零特征函数只能支撑于单点t=λ，这在L²等价类中为零。对区间内部λ，可把归一化窄窗放在λ附近，使 $\|(M-\lambda I)f_\varepsilon\|=\varepsilon/\sqrt3$，而 $\|f_\varepsilon\|=1$，展示逆映射为何不可能有统一界。区间外，乘以1/(t−λ)给出有界逆。

### 紧自伴谱定理的准确范围

有界自伴算子的谱为实数，但不保证有可数特征向量基，上一乘法算子就是反例。对**紧自伴**K，非零谱点都是实特征值，非零特征空间有限维，若有无限多个非零特征值，只能向0聚集；H由这些正交特征空间及ker K的正交和生成。[16](#ref-fa-selfadj)[17](#ref-fa-spectral)

因此加上ker K的正交基可得到完整展开，但0不必本身是特征值。若Hilbert空间不可分，不能默认完整基一定可数。一般自伴算子有更广的谱测度理论，本篇不把紧自伴的离散级数形式冒充整个谱定理。

### 平滑的Green算子与闭值域

区间[0,1]上零端点负二阶导的逆核为
$G(x,\xi)=\min(x,\xi)[1-\max(x,\xi)]$。
算子 $(Kf)(x)=\int_0^1G(x,\xi)f(\xi)d\xi$ 在L²上紧、自伴、正，特征函数为 $\sqrt2\sin(n\pi x)$，特征值 $1/(n\pi)^2$；它单射而0仍在谱中。[20](#ref-fa-dirichlet)

任意f∈L²有展开，但要成为K的像，系数须满足 $\sum(n\pi)^4|\langle e_n,f\rangle|^2<\infty$。值域稠密却不闭，反演会放大高阶系数。一般有界算子在Hilbert空间中有 $\overline{\operatorname{ran}A}=(\ker A^*)^\perp$；只有值域闭时，才能去掉闭包并获得相应正交分解中的精确可解条件。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/compact-and-spectrum.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/functional-analysis/compact-and-spectrum.svg" alt="Green紧算子特征值按模态序号平方反比趋零，乘法算子上的归一化窄窗形成近似特征向量但没有真正L²特征函数。 " width="1400" height="550" loading="lazy" /></a><figcaption>图8　离散谱与连续谱的两种例子。左图为指定Green核的非零谱；右图围绕λ=0.5构造近似特征向量。窄窗有不连续端点但属于L²；它不是乘法算子的真正特征向量。</figcaption></figure>

## Sobolev空间与变分问题

### 导数也需要弱意义

**弱导数**g由 $\int f\phi'=-\int g\phi$ 对所有光滑紧支撑测试函数φ成立来定义。$H^1(0,1)$ 由f及其一阶弱导数都在L²的元素组成，范数为 $(\|f\|_2^2+\|f'\|_2^2)^{1/2}$；这比仅要求平方可积更强。[18](#ref-fa-sobolev)

在一维单位区间上，每个H¹元素可选绝对连续代表，并有例如

$$
|f(t)|\le\|f\|_2+\|f'\|_2\le\sqrt2\|f\|_{H^1}.
$$

所以点评价可被H¹范数控制。前面的三角尖峰虽L²范数趋零，导数平方范数却为2n，不在有界H¹球内。零端点空间 $H_0^1$ 可定义为光滑紧支撑函数在H¹中的闭包，并与零边界迹对应。更高维的 $H^1$ 不自动连续或允许任意点评价，需要相应嵌入条件。

δ是对测试函数作用的分布，不是L²中的普通单位脉冲；一维点载荷可作为适当Sobolev对偶中的对象。定义域、迹和对偶使边界条件与集中源都有精确位置，不能只用“画得很尖”来取代空间归属。

### Lax–Milgram怎样给出存在 唯一与稳定

先在**实Hilbert空间**V上表述：双线性型a有界，$|a(u,v)|\le C\|u\|_V\|v\|_V$；且**强制性**成立，$a(v,v)\ge\alpha\|v\|_V^2$，α>0。若线性泛函F连续，则存在唯一u∈V使a(u,v)=F(v)对所有v成立，并有 $\|u\|_V\le\|F\|/\alpha$。[19](#ref-fa-lm)

强制性不等同“矩阵的特征值实部为正”这一泛泛说法，更不等同每个频率都能求逆；它是针对指定V范数的统一二次型下界。复空间需要按约定采用半双线性型及实部强制性，不能把实双线性式原样照搬。

对 $-u''=1$、零端点，取V=H₀¹、a(u,v)=∫u'v'、F(v)=∫v。在单位区间上，Poincaré不等式 $\|v\|_2\le\pi^{-1}\|v'\|_2$ 使导数范数与完整H¹范数等价，后者下可取强制常数 $\alpha=\pi^2/(1+\pi^2)$；解为u=x(1−x)/2。纯Neumann问题有常数核，需先限制均值或处理相容性。亥姆霍兹型又可能失去这个直接强制性，不能无条件套用。

### 极小化与近似求解

对上述对称正定问题，u是 $J(v)=\tfrac12a(v,v)-F(v)$ 的唯一极小点；有
$J(v)-J(u)=\tfrac12a(v-u,v-u)$。
极小化的“能量”是该方程对应泛函，不是所有应用中实际声能的同义词。

在闭子空间Vh中求Galerkin解uₕ，有a(u−uₕ,vₕ)=0。在对称情形它是能量内积的投影；一般有界强制型可用Céa估计 $\|u-u_h\|_V\le(C/\alpha)\inf_{v_h\in V_h}\|u-v_h\|_V$，还需精确积分、正确边界和适当离散模型等前提。数值误差小仍不直接说明真实听觉模型正确。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/variational-problem.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/functional-analysis/variational-problem.svg" alt="零端点Poisson问题的抛物线解和分段线性Galerkin近似，右图比较泛函差与能量误差的一半。 " width="1400" height="550" loading="lazy" /></a><figcaption>图9　弱解与最优近似的连接。使用单位区间、单位源和精确积分；分段线性近似属于H₀¹，误差按导数的能量范数比较。此处数学泛函未被等同为真实器件能量。</figcaption></figure>

## 从反演到正则化与迭代

### 唯一可逆为什么仍可能不稳定

若紧算子在正交方向上使系数变成σₙxₙ，σₙ→0，则数据扰动ηₙ反演为ηₙ/σₙ。它可以有唯一原像，却没有在所选数据范数中的稳定逆。逆滤波、去卷积和参数辨识都可能出现类似结构，但实际设备是否符合某个紧模型需要另证。

对Hilbert空间之间的紧、无限秩算子A，在其非零奇异系统上可写 $Av_n=\sigma_nu_n$。精确数据y还须属于 $(\ker A^*)^\perp$ 并满足Picard平方可和条件 $\sum|\langle u_n,y\rangle|^2/\sigma_n^2<\infty$，才能有相应有限范数原像；核方向则引入不唯一性。有限矩阵总有最小二乘解，不会自动消除无限维值域问题。[21](#ref-fa-regularization)

### Tikhonov正则化改变了要解的问题

在Hilbert空间中，给定有界A，$\alpha>0$ 时最小化
$$
\|Ax-y^\delta\|^2+\alpha\|x\|^2
$$

有唯一解

$$
x_\alpha=(A^*A+\alpha I)^{-1}A^*y^\delta.
$$

它平衡数据拟合与解范数；若改用导数或其他惩罚，空间、零空间和适定条件也会改变，不能总用同一公式。

沿奇异方向，滤波增益为 $\sigma_n/(\sigma_n^2+\alpha)$，最大不超过 $1/(2\sqrt\alpha)$；相对真系数还存在偏差。若δ是数据误差范数，$1/(2\sqrt\alpha)$ 给噪声传播界的一部分，不是总重建误差。适当源条件与α(δ)选取才支撑收敛或速率，单幅“更平滑”的图不构成参数选择定理。[21](#ref-fa-regularization)

图10指定60维截断、$\sigma_n=e^{-0.15n}$ 及确定性扰动，演示放大与滤波。所有量无单位，不把σ曲线称为真实声学传递函数，也不从有限维检验宣称证明无限维正则化理论。统计噪声、概率风险与参数选择可结合[数理统计](../mathematical-statistics/)和[机器学习](../machine-learning/)。

### 不动点定理也离不开完备性

Banach不动点定理说：非空完备度量空间上，将空间映到自身且满足 $d(Tx,Ty)\le qd(x,y)$、0≤q<1的压缩映射，有唯一不动点；从任意起点迭代都收敛，并有可计算误差界。它与“Banach空间”同名相关，但不是同一个定义。[22](#ref-fa-fixedpoint)

“迭代误差这几步变小”不能代替全域压缩证明；一般非扩张q=1也不能套用同样结论。若先限制在闭球，应核对迭代确实保留该球。此处作为非线性分析的后续入口，不把所有学习算法说成压缩映射。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/functional-analysis/regularization.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/functional-analysis/regularization.svg" alt="指定对角模型的小奇异值导致直接反演放大扰动，Tikhonov滤波限制增益并在误差与偏差间折中。 " width="1400" height="550" loading="lazy" /></a><figcaption>图10　平滑、逆映射与正则化。使用60个系数的原创确定性模型，α为平方范数惩罚的系数。图形展示这一算例，不表示通用最佳α，也未使用听者或器件数据。</figcaption></figure>

## 可复算的例子与学习自检

### 正交投影和残差

下例以数值积分核对图3。函数使用归一化坐标，两个基函数均归一；读数按本文第一变量共轭线性的约定计算，实函数下共轭不改变结果。

```python
import numpy as np
from scipy.integrate import quad
f = lambda t: np.sin(2*np.pi*t)+.4*np.cos(4*np.pi*t)+.2*np.sin(6*np.pi*t)
e = [lambda t: np.sqrt(2)*np.sin(2*np.pi*t),
     lambda t: np.sqrt(2)*np.cos(4*np.pi*t)]
c = np.array([quad(lambda t: g(t)*f(t), 0, 1)[0] for g in e])
p = lambda t: sum(cc*g(t) for cc, g in zip(c, e))
residual2 = quad(lambda t: (f(t)-p(t))**2, 0, 1)[0]
print(c, residual2)
assert np.allclose(c, [1/np.sqrt(2), .4/np.sqrt(2)])
assert np.isclose(residual2, .02)
for g in e:
    assert abs(quad(lambda t: g(t)*(f(t)-p(t)), 0, 1)[0]) < 1e-10
```

### 加权内积下的伴随

下例使用一个复矩阵和两个正定权矩阵。若把加权伴随误写成A的裸共轭转置，等式一般不成立。

```python
import numpy as np
A = np.array([[1+1j, 2], [-1j, .5]], dtype=complex)
M = np.diag([2., 1.])
W = np.diag([1., 3.])
adj = np.linalg.solve(M, A.conj().T @ W)
x = np.array([1+.2j, -.4j])
y = np.array([.3j, 2-1j])
left = np.vdot(A@x, W@y)
right = np.vdot(x, M@(adj@y))
print(left, right)
assert np.allclose(left, right)
```

### 正则化公式与独立线性求解

本例核对同一个有限对角问题的模态公式和线性方程解，并显示实际系数误差。确定性扰动只为可复现，不代表白噪声或统计置信区间。

```python
import numpy as np
n = np.arange(1, 61)
sigma = np.exp(-.15*n)
truth = 1/n**2
eta = np.cos(1.7*n)
eta *= .001/np.linalg.norm(eta)
y = sigma*truth+eta
alpha = 1e-4
modal = sigma*y/(sigma**2+alpha)
matrix = np.linalg.solve(np.diag(sigma**2)+alpha*np.eye(len(n)), sigma*y)
raw = y/sigma
print(np.linalg.norm(raw-truth), np.linalg.norm(modal-truth))
assert np.allclose(modal, matrix)
assert np.linalg.norm(modal-truth) < np.linalg.norm(raw-truth)
```

[完整实验脚本](/n3-hearingpedia/code/functional-analysis/experiments.py)另含范数、连续近似、弱收敛读数、Green谱与Galerkin能量计算。数值只检验这些指定公式与实现；一般定理的证明仍依赖其全部数学前提。

### 六个问题检查理解

1. 为什么连续函数配最大范数完备，改配L²范数后可能不完备？完备性与紧致性有何区别？
2. 为什么L²中的点评价不成立，而有限窗平均是连续线性泛函？窗宽如何影响其范数？
3. 正交归一系何时才是基？Bessel不等式何时可升级为Parseval等式？
4. 闭图定理为何没有证明“求导从L²到L²有界”？定义域与图范数分别起什么作用？
5. 为什么自伴乘法算子可以没有特征值，而紧自伴算子具有特征展开？0是否一定是特征值？
6. 为什么正向稳定、逆解唯一、离散求解成功、真实模型有效是四件需要分别检查的事？

可先沿“范数—完备性—L²—投影与基—有界算子”学习，再进入对偶、三个基本定理、弱拓扑和紧谱；最后用Sobolev、变分与正则化回到方程和数据。阅读研究模型时，先写清空间、范数、算子定义域、边界、数据误差与要证明的结论，通常比先寻找一个抽象定理更有效。

本篇来源核对日期为2026年11月2日。依据原课程讲义和作者/大学教学资料开展定向定义、定理条件与例题核对；不声称穷尽泛函分析文献。原创图与程序经过数学和数值检查，仍保留待专业审阅状态。
