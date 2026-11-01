---
title: "概率论"
english: "Probability Theory"
slug: "probability-theory"
summary: "用听觉检测、含噪录音和重复测量学习概率论：从一次反应与随机变量开始，逐步理解分布、条件概率、贝叶斯、期望与方差、独立性、平均降噪、大数定律和中心极限定理，再连接检测模型、心理测量函数与统计推断。"
categories: ["research-methods", "signal-processing", "ai-hearing"]
tags: ["基础课程", "数学基础", "随机变量", "条件概率", "噪声", "贝叶斯", "统计推断"]
aliases: ["概率", "听觉研究中的概率论", "Probability for auditory research"]
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
  - {label: "课程定位", value: "从听觉检测、噪声和重复测量理解概率论"}
  - {label: "入门重点", value: "随机变量、分布、条件概率、期望、方差与独立性"}
  - {label: "研究连接", value: "平均降噪、检测判据、心理测量函数与不确定性"}
  - {label: "能力目标", value: "能写清随机模型，并区分模型概率、样本结果与统计推断"}
references: ["prob-mit-models", "prob-mit-discrete", "prob-scipy-binom", "prob-scipy-poisson", "prob-mit-continuous", "sdt-scipy-norm", "prob-mit-bayes", "prob-mit-independence", "prob-mit-conditional-moments", "prob-mit-covariance", "prob-mit-lln", "prob-mit-clt", "prob-heeger-sdt", "speech-reception-threshold-wichmann", "psychoacoustics-nist-wilson", "prob-scipy-beta", "prob-mit-process"]
order: 1001
---

**概率论**（probability theory）是用概率空间、随机变量及其分布研究不确定性的数学学科。一段固定的数字录音可以当作确定的向量，但下一次录音中的噪声、听者下一次是否答对、检测器下一次是否虚报，都可能需要随机模型。概率论帮助我们从“这一次发生了什么”，走向“在什么条件下，各种结果有多大可能”。[1](#ref-prob-mit-models)

本文用听觉与声学问题学习数学：同一个微弱纯音，为什么重复呈现会得到不同反应？平均十六次录音，噪声会减小多少？检测器报告“有声音”，是否就有很高把握真的存在声音？这些问题逐步引出概率、分布、条件化、期望、独立性与极限定理，再连接统计推断。数值、八张图和三段音频均来自明确设定的原创教学模型，不是听者或设备的实测结果。

前置知识为基本代数、函数与求和；涉及密度时解释积分的面积意义，证明可在学过微积分后重读。多通道协方差可与[线性代数](../linear-algebra/)配套。本文覆盖听觉研究常用的初等概率与入门推断，测度论证明、随机微分方程和完整统计检验体系另需专门课程。先读前六节即可建立主要概念，再进入随机过程、检测模型与推断。

## 同一个声音重复播放 怎样描述一次不确定的结果

### 先写清实验 再写概率

设一个“有／无”检测实验：每次可能呈现目标纯音，也可能只呈现背景；听者必须报告“有声”或“无声”。这里“有声”专指目标是否存在，背景噪声在两类试次中都可以存在。用第一坐标的1或0表示目标存在或不存在，第二坐标的1或0表示报告有声或无声，一试次的简化**样本空间**为

$$
\Omega=\{(1,1),(1,0),(0,1),(0,0)\}.
$$

样本空间是模型中所有可能基本结果的集合。**事件**是我们为其赋予概率的结果集合：设 $S=\{(1,1),(1,0)\}$ 为“目标存在”，$R=\{(1,1),(0,1)\}$ 为“报告目标存在”。$S\cap R=\{(1,1)\}$ 只包含“有目标且报有声”；$\cap$ 表示同时发生，$\cup$ 表示至少一个发生，上标 $c$ 表示补集。四个结果不一定等可能；把结果数一数就除以四，只有在等可能假设成立时才有依据。

完整的**概率空间**写作 $(\Omega,\mathcal F,P)$：$\mathcal F$ 是允许讨论的事件族，须包含样本空间，并对补集、可数并封闭，称为 $\sigma$ 代数；$P$ 把这些事件映为概率，满足非负、$P(\Omega)=1$，以及可数个互不相交事件的概率可相加。有限的四格模型可取所有子集作为 $\mathcal F$。由此可得

$$
P(A^c)=1-P(A),\qquad
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$

后一式减去交集，是因为两次相加时把交集算了两遍。互斥事件的交集为空，因而可直接相加；更一般地，只要 $P(A\cap B)=0$ 就能直接相加，即使交集含有零概率的结果。[1](#ref-prob-mit-models)

若允许漏答、设备失败或提前按键，四格就不再穷尽原始记录，应增加结果类型，或明确分析是在有效试次条件下进行。记录哪些试次被排除，会影响概率的分母。与[心理声学](../psychoacoustics/)实验一样，刺激、任务和计分规则要先固定，概率才有清楚的对象。

### 一次反应不是一个概率

**随机变量**是把基本结果映为数值的可测函数 $X:\Omega\to\mathbb R$；可测意味着诸如“$X\le x$”的集合是可赋概率的事件。一次完成的观察值写作小写 $x$。现在换成两间隔强迫选择任务，每试次仅一个间隔含目标，样本空间相应改由“目标在哪个间隔、选择哪个间隔”的组合构成。把答对记为 $X=1$、答错记为 $X=0$，便有 $P(X=1)=p$。参数 $p$ 描述固定条件下的模型正确概率，单次观察只能是 0 或 1。[2](#ref-prob-mit-discrete)

重复 $n$ 次，观察到 $k$ 次正确，**相对频率**为 $k/n$。它是样本统计量，不是模型参数本身。若假定 $p=0.75$，既不保证每四次恰好答对三次，也不保证前十次的比例比前五次更接近 0.75。反过来，观察到 30/40 并不意味着已无误差地知道 $p=0.75$。后文将分别讨论“已知 $p$，结果怎样变化”和“看到结果，怎样估计 $p$”。

## 从一次答对到四十次总数 离散分布与计数

### 伯努利分布和二项分布怎样接起来

离散随机变量的**概率质量函数**为 $p_X(x)=P(X=x)$，各质量非负且总和为 1。只有 0、1 两个取值、正确概率为 $p$ 的变量称为**伯努利变量**：$P(X=1)=p$，$P(X=0)=1-p$。它描述一次结果，并没有自动规定多个试次之间的关系。

若伯努利变量 $X_1,\ldots,X_n$ **相互独立，且具有同一正确概率** $p$，总正确数 $K=\sum_iX_i$ 就服从**二项分布**：

$$
P(K=k)=\binom nkp^k(1-p)^{n-k},\qquad k=0,1,\ldots,n.
$$

为什么有组合数？某一个指定的结果序列，例如“前三次正确、后两次错误”，概率为 $p^3(1-p)^2$；但五次中三次正确可出现在 $\binom53=10$ 组位置。一般地，$\binom nk=n!/[k!(n-k)!]$ 计算从 $n$ 个位置选择 $k$ 个正确位置的方法数。因此二项公式把同一总数对应的所有互斥序列相加，而不是只算一种排列。[2](#ref-prob-mit-discrete) [3](#ref-prob-scipy-binom) 独立同概率是这个推导的充分条件，不能反过来仅凭总数分布看似二项，就认定原始试次独立。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/trials-and-binomial.svg" target="_blank" rel="noopener" aria-label="查看反应与二项分布完整图"><img src="/n3-hearingpedia/figures/probability-theory/trials-and-binomial.svg" alt="上图显示四十次模拟的零一反应，下图显示假定正确概率零点七五时整套实验正确总数的二项分布" width="1400" height="800" loading="lazy" /></a>
  <figcaption><strong>图 1　单次反应与总数分布属于不同层次。</strong>（a）固定种子生成的一组40次独立伯努利反应，此次恰好32次正确；（b）在相同参数下，总数的精确二项概率，均值为30。上面的一个序列不要求落在均值上，也不是后文指定30/40的推断例数据。图为教学计算。</figcaption>
</figure>

二项分布的均值为 $np$、方差为 $np(1-p)$。取 $n=40,p=0.75$，平均总数为30，方差为7.5，标准差约2.739次。图上某根柱的高度才是“恰好得到该总数”的概率；均值的位置不表示该总数必然发生。

### 哪些计数不能直接套二项分布

若越来越疲劳使第 $i$ 次正确概率变为 $p_i$，独立条件下的总数通常也不是单一 $p$ 的二项分布；若连续试次存在依赖，连“把所有试次当作独立”这一步也需要改变。**独立同分布**（independent and identically distributed，i.i.d.）同时要求独立与分布相同，两者不能互相替代。

另一种声学问题是统计固定时长内的短促事件。若假定事件服从速率为 $r$ 次/秒的**齐次泊松过程**，不相交时间段的计数独立，长度 $T$ 秒内的计数 $K$ 满足

$$
P(K=k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad
\lambda=rT,\quad k=0,1,\ldots.
$$

$\lambda$ 是这段时间的期望事件数，无量纲；它同时是计数方差。假设 $r=20$ 次/秒，$T=0.1$ 秒，则 $\lambda=2$，零次事件的概率 $e^{-2}\approx0.1353$。[4](#ref-prob-scipy-poisson) 这是一个计数模型：若声事件成簇、受周期驱动或存在不应期，泊松假设可能不适合。真实听神经放电不能仅因“能数脉冲”就一律归为齐次泊松过程。

二项模型先固定机会次数，每次至多贡献一次成功；泊松模型在固定时间窗中允许任意非负整数个事件。二项在 $n$ 很大、$p$ 很小而 $np$ 固定时可逼近泊松，但40次正确率为0.75的例子没有这个稀有事件条件。

## 噪声声压取连续数值 概率密度与分布函数

### 曲线下面积才是概率

现在把注意力转向麦克风。选定一个采样时刻，重复录制背景，把该时刻的噪声声压记为 $X$。若它具有**概率密度函数** $f_X(x)$，则

$$
P(a<X\le b)=\int_a^b f_X(x)\,dx,\qquad
f_X(x)\ge0,\quad\int_{-\infty}^{\infty}f_X(x)\,dx=1.
$$

密度不是单点概率。对于具有密度的连续变量，$P(X=x)=0$，但它会落在某个区间，区间概率由面积给出。这里 $X$ 用 Pa 表示，密度单位是 $\mathrm{Pa}^{-1}$，才能在对 Pa 积分后得到无量纲概率。密度高度超过1并不违反概率上限。[5](#ref-prob-mit-continuous)

**累积分布函数**（cumulative distribution function，CDF）定义为 $F_X(x)=P(X\le x)$，对离散、连续或混合分布都适用。它单调不减、右连续，从0趋向1；有密度时 $F_X(x)=\int_{-\infty}^xf_X(u)\,du$。求区间概率可以用 $F_X(b)-F_X(a)$。本文的连续公式假定存在密度，并非声称一切分布都可用普通密度表示。

### 正态分布是幅值模型 白噪声是相关结构

**正态分布** $X\sim\mathcal N(\mu,\sigma^2)$ 的密度为

$$
f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\!\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],\qquad\sigma>0.
$$

$\mu$ 是均值，与 $X$ 同单位；$\sigma$ 是标准差，$\sigma^2$ 是方差。把 $Z=(X-\mu)/\sigma$ **标准化**后，$Z\sim\mathcal N(0,1)$。令其CDF为 $\Phi$，则 $P(X>b)=1-\Phi((b-\mu)/\sigma)$。[6](#ref-sdt-scipy-norm)

例如 $\mu=0,\sigma=0.02$ Pa，$f_X(0)\approx19.95\ \mathrm{Pa}^{-1}$，而 $P(-0.01<X\le0.01)=\Phi(0.5)-\Phi(-0.5)\approx0.3829$。前者是峰高，后者才是38.29%的概率。真实模数转换记录经过量化，严格地说是离散数值；在量化足够细时，用连续密度描述幅值变化是一种近似。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/density-and-dependence.svg" target="_blank" rel="noopener" aria-label="查看密度与时间相关完整图"><img src="/n3-hearingpedia/figures/probability-theory/density-and-dependence.svg" alt="正态声压密度的区间面积，以及单点正态分布相同但自协方差不同的独立序列与AR序列" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 2　分布形状与时间结构要分别描述。</strong>（a）标准差0.02 Pa的零均值正态密度，阴影面积约0.3829；（b）两种单位方差高斯序列的理论归一化自协方差，一种仅零间隔非零，另一种为 0.9<sup>|k|</sup>。两面板的幅值尺度不同；右图比较理论相关结构，不是从一段音频估出的相关。图为解析教学计算。</figcaption>
</figure>

“高斯”描述分布，“白”描述频谱或相关结构；两者是不同属性。对联合高斯的输入作固定线性平滑滤波，输出仍是高斯过程，却可产生时间相关和有色频谱；非线性处理一般没有这个保证。只看直方图，无法判定相邻样本是否独立；只听起来像“沙沙声”，也无法断定它满足某种精确概率模型。随机过程一节会把这个区别写成公式。

## 听到报告有声之后 条件概率与贝叶斯更新

### 条件概率是在更小的集合里重新计数

对 $P(B)>0$ 的事件 $B$，**条件概率**定义为

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

竖线后面的 $B$ 表示已知的条件，相当于把 $B$ 当作新的讨论范围。它不是“$B$ 造成 $A$”的符号，也不能把前后顺序随意交换。[7](#ref-prob-mit-bayes)

回到有／无检测。设 $P(S)=0.2$，命中率 $P(R\mid S)=0.8$，虚报率 $P(R\mid S^c)=0.1$。假想重复1000次：期望有200次含目标，其中160次报告有声；800次无目标，其中80次也报告有声。注意这是按模型计算的**期望计数**，不是承诺任何一套1000次实验恰好得到这些整数。

| 真实条件 | 报告有声 $R$ | 报告无声 $R^c$ | 合计 |
| --- | ---: | ---: | ---: |
| 有目标 $S$ | 160 命中 | 40 漏报 | 200 |
| 无目标 $S^c$ | 80 虚报 | 720 正确拒绝 | 800 |

命中率的分母是200次含目标试次；“报告有声后确实有目标”的分母却是240次报有声试次。后者为 $160/(160+80)=2/3$，并不是0.8。

### 全概率是分开再相加 贝叶斯是把方向倒过来

若事件 $B_1,\ldots,B_m$ 互斥且穷尽样本空间，$P(B_i)>0$，则**全概率公式**为 $P(A)=\sum_iP(A\mid B_i)P(B_i)$。因此 $P(R)=0.8\times0.2+0.1\times0.8=0.24$。再把条件概率定义用于另一方向，得到**贝叶斯公式**：

$$
P(S\mid R)=\frac{P(R\mid S)P(S)}
{P(R\mid S)P(S)+P(R\mid S^c)P(S^c)}.
$$

$P(S)$ 是看到报告前的**先验概率**，$P(S\mid R)$ 是看到报告后的**后验概率**。分子计算“有目标且报有声”的联合概率，分母把所有能够产生“报有声”的路径都算进去，所以后验会同时取决于命中、虚报和先验。[7](#ref-prob-mit-bayes)

若只把先验改为0.02，而保持两种条件反应率不变，后验降为 $0.016/(0.016+0.098)\approx0.1404$。这不是说检测器变坏，而是大量无目标试次提供了更多虚报来源。真实听者可能随呈现概率改变反应判据，所以“条件反应率不变”是本对照的设定，不能未经检验用于真实实验。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/bayes-and-base-rate.svg" target="_blank" rel="noopener" aria-label="查看先验与后验完整图"><img src="/n3-hearingpedia/figures/probability-theory/bayes-and-base-rate.svg" alt="四格期望计数和保持命中虚报率不变时后验概率随先验变化的曲线" width="1400" height="680" loading="lazy" /></a>
  <figcaption><strong>图 3　把分母找对，才知道报告意味着什么。</strong>（a）表中四类结果的期望计数；（b）命中率固定0.8、虚报率固定0.1时，报有声后真实有声的概率。红点对应先验0.02和0.2。曲线为上述公式的原创计算，未拟合听者，也不表示听者必然保持判据不变。</figcaption>
</figure>

### 独立不等于互斥 条件独立不等于总体独立

两个事件**独立**是指 $P(A\cap B)=P(A)P(B)$；若 $P(B)>0$，等价于 $P(A\mid B)=P(A)$。两个正概率的互斥事件交集概率为0，反而不独立。多个事件相互独立还要求任意子组的交集概率都等于各自概率的乘积；只验证两两独立还不够。[8](#ref-prob-mit-independence)

随机变量 $X,Y$ 独立，要求对任意可测取值集合 $A,B$，有 $P(X\in A,Y\in B)=P(X\in A)P(Y\in B)$；离散时可检验联合质量是否分解为边缘质量的乘积。两支麦克风录到同一个背景源，或同一听者连续完成任务，都不能仅因为“有两列数据”就假定独立。

**条件独立**是给定条件后才成立的乘积分解。例如给定某位听者固定正确概率 $p$，可以假定其各次反应独立；但若把正确概率不同的听者混在一起，不知道本次抽到了哪位听者，同一听者的多次结果在总体模型中可以相关。条件化可能建立、破坏或改变独立性，分组与合并必须说明随机抽样的层次。[8](#ref-prob-mit-independence)

## 均值和方差 怎样描述声压与反应的变化

### 期望是按概率加权 不是最常见结果

在 $\mathbb E|X|<\infty$ 时，**期望**定义为离散情形的 $\mathbb E[X]=\sum_xxP(X=x)$，或有密度情形的 $\mathbb E[X]=\int xf_X(x)\,dx$。例如伯努利变量 $\mathbb E[X]=0\times(1-p)+1\times p=p$。若 $p=0.75$，期望为0.75，但一次反应永远不会是0.75；期望也不一定等于密度峰的位置。[2](#ref-prob-mit-discrete)

**期望的线性性**是 $\mathbb E[aX+bY]=a\mathbb E[X]+b\mathbb E[Y]$，只要所需期望存在，**不要求独立**。所以即使试次相关，期望总数仍可由各次正确概率相加；相关性主要会改变总数的不确定性和分布，不能据此继续套二项方差。

一般函数则须先变换、再加权：相应期望存在时，$\mathbb E[g(X)]=\sum_xg(x)P(X=x)$，或相应积分。通常 $\mathbb E[g(X)]\ne g(\mathbb E[X])$。例如同样长的两段零均值录音，RMS分别为0.01和0.03 Pa。拼接后的均方值为 $(0.01^2+0.03^2)/2=0.0005\ \mathrm{Pa}^2$，RMS约0.02236 Pa，不是把两个RMS直接平均得到的0.02 Pa。计算[声级](../audiometric-calibration/)还要先说明平均的是线性均方声压还是对数声级，两种平均回答不同问题。

### 方差是偏离均值的平方的期望

若二阶矩有限，**方差**与**标准差**为

$$
\operatorname{Var}(X)=\mathbb E[(X-\mu)^2]
=\mathbb E[X^2]-\mu^2,\qquad
\operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)},\quad\mu=\mathbb E[X].
$$

方差单位是原单位的平方；标准差回到原单位。$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$，加上固定偏置不改变方差。零均值噪声的均方值等于方差；有直流偏置时，均方值为方差加均值平方，不能把两者混用。

伯努利变量因 $X^2=X$，方差为 $p-p^2=p(1-p)$。样本平均 $\bar x$ 与样本方差（$n\ge2$）$s^2=\sum_i(x_i-\bar x)^2/(n-1)$ 则是从数据计算的统计量；在独立同分布、有限方差条件下，$s^2$ 是总体方差的无偏估计。这里的 $n-1$ 用于估计总体方差，有限录音本身的均方值通常按 $1/n$ 计算，不能只凭一个叫“平均”就互换分母。

### 条件期望与全方差 把听者差异放回模型

本节以离散类别变量 $G$ 说明：对 $P(G=g)>0$ 的类别，给定 $G=g$ 后对条件分布求期望，得到 $\mathbb E[X\mid G=g]$；把 $g$ 看成变化的条件，$\mathbb E[X\mid G]$ 本身也是随机变量。满足相应矩条件时，**全期望公式**与**全方差公式**为

$$
\mathbb E[X]=\mathbb E\{\mathbb E[X\mid G]\},
$$

$$
\operatorname{Var}(X)=\mathbb E\{\operatorname{Var}(X\mid G)\}
+\operatorname{Var}\{\mathbb E[X\mid G]\}.
$$

后一式可从 $X-\mathbb E[X]=(X-\mathbb E[X\mid G])+(\mathbb E[X\mid G]-\mathbb E[X])$ 平方后取期望得到：第一项的条件均值为0，使交叉项消失。它把总变异分为“各类条件方差的平均”和“条件均值的变异”。[9](#ref-prob-mit-conditional-moments)

举例，等概率抽到两类模型听者，其正确概率分别0.6和0.9。一次反应的总体均值为0.75；两类条件方差的平均为 $(0.6\times0.4+0.9\times0.1)/2=0.165$；条件均值的方差为 $[(0.6-0.75)^2+(0.9-0.75)^2]/2=0.0225$。总方差为0.1875，恰好等于 $0.75\times0.25$。

关键在于：若先抽一位听者，再由其完成整套试次，潜在正确概率在这套试次内共享；总正确数是两个二项分布的混合，不是 $\operatorname{Binomial}(n,0.75)$。大量重复试次不能替代抽到更多独立听者，个体内不确定性与人群差异要分开估计。

## 平均十六次录音 噪声为什么可能降不下去

### 联合分布与协方差描述共同变化

**联合分布**描述多个随机变量同时取值的概率；离散变量由 $p_{X,Y}(x,y)$ 给出，把另一个变量所有取值加起来，就得到**边缘分布** $p_X(x)=\sum_yp_{X,Y}(x,y)$。只知道两个边缘分布，还不足以确定二者如何共同变化。

对有限二阶矩变量，**协方差**定义为

$$
\operatorname{Cov}(X,Y)=\mathbb E[(X-\mu_X)(Y-\mu_Y)]
=\mathbb E[XY]-\mu_X\mu_Y.
$$

若两者标准差均非零，**相关系数** $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ 在−1至1之间。正值表示线性共同起伏，负值表示相反起伏；它既不证明因果，也没有覆盖全部非线性依赖。独立可推出零协方差，反向一般不成立。[10](#ref-prob-mit-covariance)

例如让 $X$ 等可能取−1、0、1，令 $Y=X^2$。则 $\mathbb E[X]=\mathbb E[XY]=0$，所以协方差为0；但知道 $X=0$ 就能确定 $Y=0$，二者显然不独立。这也提醒我们：声压与由它算出的平方幅值，即使线性相关为零，也不能因此说没有依赖。若 $X,Y$ **联合高斯**，零协方差就足以推出独立；这是一个充分条件，不是独立变量必须满足的分布要求。仅仅各自直方图呈高斯形状，还没有建立联合高斯条件。

### 从方差展开式推导平均降噪

设第 $m$ 次对齐录音在某个固定时刻为 $Y_m=s+N_m$，其中 $s$ 是每次相同的确定信号，噪声均值为0、方差为 $\sigma^2$。平均 $M$ 次得到 $\bar Y=s+\bar N$。从平方展开可得

$$
\operatorname{Var}(\bar N)=\frac{1}{M^2}
\left[\sum_{m=1}^M\operatorname{Var}(N_m)
+2\sum_{i<j}\operatorname{Cov}(N_i,N_j)\right].
$$

若各次噪声互不相关，协方差项为0，平均噪声方差为 $\sigma^2/M$、标准差为 $\sigma/\sqrt M$。独立是足够条件；仅推导这个方差结果时，零协方差已足够。[10](#ref-prob-mit-covariance)

对整段录音，在相同时间窗内设确定目标的均方值为 $P_s>0$，用噪声均方值的期望 $P_n=\mathbb E[N^2]$ 定义理论[信噪比](../speech-reception-threshold/) $P_s/P_n$。若上述同方差、跨次不相关条件在各采样点均成立，且目标保留，平均后的 $P_n$ 降为原来的 $1/M$，理论信噪比增加 $M$ 倍，即 $10\log_{10}M$ dB。这里是期望均方值之比；它不是有限录音所得随机比值的期望，也不保证每一段实际音频恰好改善这些分贝。

若任意不同记录的噪声相关系数均为同一个 $0\le\rho\le1$，则有 $M(M-1)/2$ 个协方差对，于是

$$
\operatorname{Var}(\bar N)=\sigma^2\left[\rho+\frac{1-\rho}{M}\right].
$$

这个设定可由 $N_m=C+U_m$ 实现：共享噪声 $C$ 方差为 $\rho\sigma^2$，各次私有噪声 $U_m$ 相互独立、与 $C$ 独立，方差为 $(1-\rho)\sigma^2$。平均只减小私有成分，共享成分保留。这里相关系数比较的是**同一时刻的不同记录**，不是一段记录中相邻时间点。

取 $\sigma=0.2,M=16$：不相关时标准差降至0.05，理论功率信噪比增加12.04 dB；若 $\rho=0.5$，标准差仍约0.1458，只增加2.75 dB；即使无限次平均，标准差也不会低于 $0.2\sqrt{0.5}\approx0.1414$。这来自共享噪声假设，不是一般设备的性能下限。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/averaging-and-covariance.svg" target="_blank" rel="noopener" aria-label="查看重复平均完整图"><img src="/n3-hearingpedia/figures/probability-theory/averaging-and-covariance.svg" alt="单次含噪纯音与十六次平均波形，以及独立噪声和共享噪声条件下理论标准差随平均次数的变化" width="1400" height="800" loading="lazy" /></a>
  <figcaption><strong>图 4　平均降噪的关键在协方差。</strong>（a）1000 Hz、幅值0.15的纯音与标准差0.2的独立高斯噪声相加，展示前6 ms的单次记录与16次平均；（b）同方差下比较记录间 ρ=0 与0.5的理论结果。图中幅值无量纲，时间已严格对齐，未模拟听者或真实声学通路。</figcaption>
</figure>

### 试听平均前后 并检查信号有没有一起被平均掉

三段教学音频都包含同一个1000 Hz、幅值0.15的目标，采样率16 kHz、时长0.8秒；首尾10 ms淡入淡出，统一乘0.65播放增益，**没有逐段归一化**。播放幅值未做声学校准。正文标准差指淡入淡出前的随机模型参数，有限音频的实际RMS会略有变化。

<p>一次含噪记录：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/probability-theory/one-trial.wav"></audio>
<p>16次独立噪声记录平均：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/probability-theory/average-16.wav"></audio>
<p>16次含共享噪声的记录平均，记录间相关系数0.5：</p>
<audio controls preload="none" src="/n3-hearingpedia/audio/probability-theory/shared-average-16.wav"></audio>

音频帮助观察模型的声学差异，不能据此估计个人听阈。平均还要求想保留的信号跨次一致且对齐：若目标相位每次随机，直接平均可能把纯音也抵消；若响应有时延抖动，[诱发响应](../auditory-evoked-potential/)的峰可能被抹宽。减少随机方差也不会自动消除固定校准偏差。

## 做更多试次会怎样 大数定律与中心极限定理

### 大数定律不保证每一步都更接近真值

设 $X_1,\ldots,X_n$ 独立同分布，均值 $\mu$、有限方差 $\sigma^2$。样本平均 $\bar X_n=n^{-1}\sum_iX_i$ 满足 $\mathbb E[\bar X_n]=\mu$、$\operatorname{Var}(\bar X_n)=\sigma^2/n$。对任意 $\varepsilon>0$，Chebyshev不等式给出

$$
P(|\bar X_n-\mu|\ge\varepsilon)
\le\frac{\sigma^2}{n\varepsilon^2}\longrightarrow0.
$$

这就是本条件下的**弱大数定律**：样本平均依概率趋于均值。“依概率”表示偏离超过任意固定容差的概率趋于0，不要求一条样本路径单调靠近，也不规定第几次之后永不偏离。[11](#ref-prob-mit-lln)

若听者状态稳定、试次独立，累计正确率可以估计固定的 $p$；若同时改变信噪比、反馈或训练水平，就未必还在估计同一个参数。增加试次主要减小这个模型下的抽样波动，不能靠数量修复系统偏差、材料不代表目标场景或把少数听者当作整个人群的问题。

### 中心极限定理描述标准化后的波动形状

同样假设独立同分布，且 $0<\sigma^2<\infty$，**中心极限定理**为

$$
Z_n=\frac{\sqrt n(\bar X_n-\mu)}{\sigma}
\ \xrightarrow{\ d\ }\ \mathcal N(0,1).
$$

箭头表示依分布收敛：标准化变量的CDF趋于标准正态CDF。大数定律说明均值附近的集中，中心极限定理将均值偏差乘以 $\sqrt n/\sigma$，描述标准化后的分布形状。它没有说原始听者反应或原始噪声必然正态，也没有说离散变量的单点概率会直接变成连续密度。[12](#ref-prob-mit-clt)

对独立伯努利反应，$\operatorname{SD}(\bar X_n)=\sqrt{p(1-p)/n}$。$p=0.75,n=40$ 时约0.06847，即6.85个百分点；把试次数增至160才减半。有限样本的正态近似是否充分还取决于偏斜、边界和尾部；“超过30个数据就一定可用”没有这样的普遍保证。参数接近0或1、事件很稀少时，应直接考虑离散分布或合适的区间方法。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/law-and-limit.svg" target="_blank" rel="noopener" aria-label="查看极限定理完整图"><img src="/n3-hearingpedia/figures/probability-theory/law-and-limit.svg" alt="四条累计正确率模拟路径和不同试次数下标准化二项分布与标准正态形状的对比" width="1400" height="680" loading="lazy" /></a>
  <figcaption><strong>图 5　靠近均值与趋近正态是不同结论。</strong>均设 p=0.75。（a）四条独立模拟的累计正确率；（b）n=10,40,160 的精确二项概率质量除以标准化网格间距，与标准正态密度比较。右图连线仅辅助读图，离散变量并未因此具有连续密度；定理陈述的是CDF收敛。原创教学计算。</figcaption>
</figure>

## 把一串噪声看成随机过程 时间相关与白噪声

### 一次录音是过程的一条实现

离散时间**随机过程** $\{N[n]\}$ 是按样本时刻 $n$ 索引的一族随机变量。固定 $n$、跨重复录音看变化，得到单时刻分布；固定一次录音、沿 $n$ 看变化，得到一条实现 $n[n]$。这两个观察方向不是自动等价的。

有限二阶矩的实过程称为**宽平稳**（wide-sense stationary，WSS），是指均值不随时间改变，且自协方差只依赖时间间隔 $k$：

$$
C[k]=\mathbb E[(N[n]-\mu)(N[n+k]-\mu)].
$$

自相关 $R[k]=\mathbb E[N[n]N[n+k]]=C[k]+\mu^2$。自相关与自协方差只有零均值时才相同。宽平稳只约束前两阶矩；严格平稳要求所有有限维联合分布在时间平移下不变。在有限二阶矩条件下，严格平稳可推出宽平稳；没有该矩条件的严格平稳过程，可能连这里的协方差都不存在。[17](#ref-prob-mit-process)

本文的离散**白噪声**采用零均值约定：$C[k]=\sigma^2\delta[k]$，其中 $\delta[0]=1$，其余为0。它在不同时刻不相关；若还满足联合高斯，则可推出不同样本独立。非高斯白噪声仅凭这个二阶定义不能推出独立。对应的[功率谱密度](../spectrum-and-power-spectral-density/)是平坦的，实际采样率与单双边约定决定频率坐标和归一化。

### 滤波会把白噪声变成有色噪声

例如 $N[n]=\phi N[n-1]+\epsilon[n]$，$|\phi|<1$，$\epsilon[n]$ 是均值0、方差 $\sigma^2(1-\phi^2)$ 的高斯创新，各时刻创新相互独立并与初始值独立。采用零均值平稳高斯初始分布后，$N[n]$ 的边缘分布仍为 $\mathcal N(0,\sigma^2)$，但 $C[k]=\sigma^2\phi^{|k|}$。其方差来自递推 $\sigma^2=\phi^2\sigma^2+\operatorname{Var}(\epsilon)$，相关结构来自创新与过去独立的条件。

取 $\phi=0.9$，相邻样本相关很强；它与独立高斯白噪声可以具有相同的单点密度，却有不同频谱。把滤波后的一万点当作一万个独立观测，通常会低估均值估计的不确定性。图2右侧正是这两种理论结构。上述递推相当于一种一阶[IIR滤波](../fir-and-iir-filters/)，没有模拟特定录音设备。

从一条长记录估计总体均值或自协方差，还需相应遍历性或一致性条件；宽平稳本身不够。[17](#ref-prob-mit-process) 例如令整段噪声记录 $N[n]=C$，其中 $C$ 是有限方差、非退化的随机常数，则均值不变、各间隔的自协方差都等于 $\operatorname{Var}(C)$，所以宽平稳；但单条记录的时间平均始终等于抽到的 $C$，与总体均值之差不会随记录变长而减小，因而不能保证收敛到总体均值。因此“时间点更多”与“独立重复更多”不能一概等同。

## 从噪声分布到听到声音 检测判据与心理测量函数

### 用尾部面积计算命中与虚报

在一个简化的等方差高斯检测模型中，内部证据 $Z$ 满足：无目标时 $Z\mid S^c\sim\mathcal N(0,1)$，有目标时 $Z\mid S\sim\mathcal N(1.5,1)$。若 $Z>c$ 就报告有声，取 $c=1$，则

$$
F=P(R\mid S^c)=1-\Phi(1)\approx0.1587,
\qquad H=P(R\mid S)=1-\Phi(1-1.5)\approx0.6915.
$$

这里 $Z$ 是模型证据，不是以Pa表示的声压，也没有直接等同某个神经元放电率。两分布的均值差除以共同标准差给出 $d'=1.5$；对 $0<H,F<1$，也有 $d'=\Phi^{-1}(H)-\Phi^{-1}(F)$。一般不等方差模型不能直接沿用共同标准差的这套解释。[13](#ref-prob-heeger-sdt)

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/detection-and-roc.svg" target="_blank" rel="noopener" aria-label="查看高斯检测与ROC完整图"><img src="/n3-hearingpedia/figures/probability-theory/detection-and-roc.svg" alt="无声和有声的内部证据正态分布及判据右侧的面积，旁边显示移动判据得到的ROC曲线" width="1400" height="680" loading="lazy" /></a>
  <figcaption><strong>图 6　同一敏感度可以对应不同报告倾向。</strong>（a）两个单位方差、均值相隔1.5的正态密度，竖线 c=1 右侧面积给出虚报与命中；（b）保持分布不变、移动判据得到ROC，红点为 c=1。这是等方差模型解析计算，内部证据单位任意，不是听者实测分布。</figcaption>
</figure>

降低判据会同时提高命中与虚报。因而“报告有声的次数更多”可能来自判据变化，未必是敏感度提高；需要同时比较有目标与无目标试次。ROC以虚报率为横轴、命中率为纵轴，把这一权衡画出来。更详细的响应设计与极端比例处理见[信号检测论](../signal-detection-theory/)。

若改为两个间隔、一个有目标一个无目标，假设两间隔证据相互独立，且听者选较大的证据，则差值 $D=Z_S-Z_N\sim\mathcal N(d',2)$，所以 $P(\text{正确})=\Phi(d'/\sqrt2)$。$d'=1.5$ 对应约0.8556。这个转换依赖独立、等方差、选大规则和无失误等条件，不能把任意任务的正确率都照此换成 $d'$。

### 正确率随信噪比变化 阈值要先定义

把刺激信噪比记为 $x$，每个条件下指定反应的概率记为 $\psi(x)$，便得到**心理测量函数**。反应可以是“答对”，也可以是有／无任务中的“报有声”，必须先说明计分对象。下面的 $\psi(x)$ 专指两间隔任务的正确概率，一种带渐近线的形式是

$$
\psi(x)=\gamma+(1-\gamma-\lambda)
L\!\left(\frac{x-\alpha}{\beta}\right),\qquad
L(u)=\frac{1}{1+e^{-u}},\quad\beta>0.
$$

$\gamma$ 为下渐近线，$1-\lambda$ 为上渐近线，要求 $0\le\gamma<1-\lambda\le1$；$\alpha$ 为位置参数，$\beta$ 控制变化尺度，与 $x$ 同单位。等机会的两选一无信息条件通常取 $\gamma=0.5$。若有／无任务拟合的是“报有声”概率，低端渐近线与虚报倾向相关；若讨论总正确率，则还取决于目标呈现比例，不能把虚报率与总正确率混为一谈。[14](#ref-speech-reception-threshold-wichmann)

这里 $\lambda$ 是上限离1的差。若另一种生成解释把 $\ell$ 定义为“走神后随机作答”的概率，则二选一时上限为 $1-\ell/2$，对应 $\lambda=\ell/2$，两种参数不能直接当成同一个数。

取 $\gamma=0.5,\lambda=0.02,\alpha=0$ dB、$\beta=3$ dB，则 $\psi(\alpha)=0.5+0.48/2=0.74$，所以位置参数0 dB并不是75%正确阈值。对指定 $q\in(\gamma,1-\lambda)$，先令 $u=(q-\gamma)/(1-\gamma-\lambda)$，反解得

$$
x_q=\alpha+\beta\log\frac{u}{1-u}.
$$

这里 $\log$ 为自然对数；$q=0.75$ 时，$x_q\approx0.2501$ dB。阈值必须连同任务、正确率目标、渐近线和模型一起报告，详见[言语接收阈](../speech-reception-threshold/)。这个logistic函数是一个概率曲线模型，没有从上面的固定 $d'=1.5$ 例子推导出其参数。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/psychometric-and-likelihood.svg" target="_blank" rel="noopener" aria-label="查看心理测量函数与似然完整图"><img src="/n3-hearingpedia/figures/probability-theory/psychometric-and-likelihood.svg" alt="下限零点五上限零点九八的logistic正确率函数，以及四十次全错、对三十次、全对对应的相对似然曲线" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 7　位置参数、指定阈值与未知正确概率各有含义。</strong>（a）本文logistic设定，x=0 对应0.74，75%阈值约0.250 dB；（b）固定 n=40，三种假设观察结果对应的二项似然，各曲线除以自身峰值以比较形状。右图纵轴是相对似然，不是概率密度；没有把三个结果当成真实听者数据。</figcaption>
</figure>

## 四十次对三十次 如何估计未知概率

### 似然把结果固定 把参数当作待比较对象

此前假定参数已知，再求结果概率。现在指定一个独立同概率的40试次教学数据，观察到30次正确、10次错误。**似然函数**把数据固定，考察不同候选 $p$ 对这份数据的支持：

$$
\mathcal L(p;k,n)=\binom nkp^k(1-p)^{n-k},\qquad 0\le p\le1.
$$

它与二项PMF有相同表达式，却沿不同对象变化：PMF固定 $p$、对 $k$ 求概率；似然固定 $k,n$、比较 $p$。似然不要求对参数积分为1，也不能直接读作“参数为 $p$ 的概率”。[3](#ref-prob-scipy-binom)

取自然对数并对 $p$ 求导，忽略不随 $p$ 变的组合项，有 $k/p-(n-k)/(1-p)=0$。内点解为**最大似然估计** $\hat p=k/n=0.75$。若全对，估计落在边界1；这只是当前数据下似然最大的参数，不证明下次必对。对于多个信噪比水平，可把各水平的二项似然相乘、用 $\psi(x)$ 替换 $p$ 来估计曲线参数；独立性、采样位置和拟合优度仍要检查。[14](#ref-speech-reception-threshold-wichmann)

### 置信区间描述重复抽样方法的覆盖性质

一个双侧95% **Wilson置信区间**可写为

$$
\frac{\hat p+z^2/(2n)\ \pm\ z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}
{1+z^2/n},\qquad z=\Phi^{-1}(0.975)\approx1.960.
$$

代入30/40，得到约 $[0.5981,0.8581]$。[15](#ref-psychoacoustics-nist-wilson) 95%指方法的名义覆盖率：在固定真实参数、反复按同一规则独立抽样并计算区间的框架下，区间覆盖该参数的比例应接近目标；离散有限样本下Wilson覆盖率依赖 $p,n$，不保证恰为95%。

在这个频率学解释中，真实 $p$ 固定、区间随数据变化，不能把已算出的区间直接解释为“$p$ 有95%概率在里面”。区间也不是个体差异范围，不是40次中95%的反应范围，更不是同一听者两次测试差值的临界范围。若试次相关或正确概率持续变化，直接套独立二项区间就可能过窄。

### 贝叶斯后验需要把先验写出来

若对未知 $p$ 指定 **Beta先验**，密度为

$$
\pi(p)=\frac{p^{a-1}(1-p)^{b-1}}{B(a,b)},\quad 0<p<1,\quad a,b>0,
\qquad B(a,b)=\int_0^1u^{a-1}(1-u)^{b-1}\,du.
$$

它是在参数空间上表达不确定性的分布。贝叶斯更新给出 $\pi(p\mid k,n)\propto\mathcal L(p;k,n)\pi(p)$；把幂次相加，就得到

$$
p\mid k,n\sim\operatorname{Beta}(a+k,b+n-k).
$$

选择均匀先验 $\operatorname{Beta}(1,1)$，30/40后变为 $\operatorname{Beta}(31,11)$，后验均值 $31/42\approx0.7381$。从后验CDF取2.5%与97.5%分位数，得到95%等尾**可信区间**约 $[0.5970,0.8578]$。[16](#ref-prob-scipy-beta) 在所指定的先验与似然模型下，可以说后验把95%概率质量分配给这个区间。它与Wilson区间数值接近，不意味着两种解释相同。

<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/probability-theory/estimation-and-uncertainty.svg" target="_blank" rel="noopener" aria-label="查看概率估计与区间完整图"><img src="/n3-hearingpedia/figures/probability-theory/estimation-and-uncertainty.svg" alt="三十除以四十对应的Wilson置信区间与Beta后验可信区间，以及均匀先验到Beta三十一十一后验的变化" width="1400" height="650" loading="lazy" /></a>
  <figcaption><strong>图 8　同一份数据可以得到两种含义不同的区间。</strong>设40次独立同概率试次中30次正确。（a）上方为95% Wilson置信区间，点为0.75；下方为均匀先验下95%等尾后验可信区间，点为后验均值约0.7381；（b）先验与后验密度。横轴都是未知正确概率，区间相似不代表解释可互换。原创教学计算。</figcaption>
</figure>

均匀先验是在 $p$ 坐标上的具体选择，不是唯一“没有信息”的先验，也不是声称二选一听者的正确率在0至1间确实均匀。若有科学理由把参数限制为 $p\ge0.5$，应显式截断并重新归一化，不能照搬完整Beta后验的数值。跨听者分析则可能需要分层模型，不能把每个人都当作共享同一个固定 $p$。

### 显著性也要分清条件方向

若事先规定检验“正确率是否高于机会水平0.5”，在独立二项零假设 $p=0.5$ 下，观察到至少30次正确的**单侧p值**为

$$
P_{p=0.5}(K\ge30)=\sum_{j=30}^{40}\binom{40}{j}2^{-40}
\approx0.0011107.
$$

它是零假设成立时，得到当前或更极端统计量的概率；不是“零假设为真的概率”，也不是“该听者有99.89%概率真正会听”。方向、统计量和停止规则应在看结果前确定；换成双侧问题、反复尝试多个条件或看显著就停止，会改变需要计算的概率。这个例子只展示概率推断的条件方向，不能替代完整实验设计与多重比较处理。

## 用三个小实验复现 并把结论解释回声音

### 从组合计数核对概率

下面用Python标准库直接求二项尾概率，并用正态CDF计算指定声压区间的概率；它不依赖随机模拟来“凑出”公式结果。

```python
from math import comb, erf, sqrt

tail = sum(comb(40, k) for k in range(30, 41)) / 2**40
Phi = lambda z: (1 + erf(z / sqrt(2))) / 2
area = Phi(0.5) - Phi(-0.5)
assert abs(tail - 0.0011107168866146822) < 1e-14
assert abs(area - 0.38292492254802624) < 1e-14
print("机会水平下至少30/40:", tail)
print("声压落在±0.01 Pa内:", area)
```

第一项描述指定零假设下整套实验的尾概率，第二项描述指定连续模型下单时刻声压的区间概率。它们虽然都在0至1之间，却没有相同的测量对象。

### 独立与共享噪声的平均

以下在一个固定时刻模拟许多套重复记录，以估计跨套实验的标准差。数组的行是一套16次平均实验，列才是该套中的各次记录；不是把一条时间波形的相邻点直接当作独立录音。

```python
import numpy as np

rng = np.random.default_rng(20261105)
sets, M, sigma, rho = 50000, 16, 0.2, 0.5
ind = rng.normal(0, sigma, (sets, M))
common = rng.normal(0, sigma * np.sqrt(rho), (sets, 1))
private = rng.normal(0, sigma * np.sqrt(1-rho), (sets, M))
sd_ind = ind.mean(axis=1).std(ddof=1)
sd_shared = (common + private).mean(axis=1).std(ddof=1)
theory = sigma * np.sqrt(rho + (1-rho)/M)
assert abs(sd_ind - sigma/np.sqrt(M)) < 0.002
assert abs(sd_shared - theory) < 0.003
print("独立与共享噪声平均后的模拟标准差:", sd_ind, sd_shared)
print("相应理论值:", sigma/np.sqrt(M), theory)
```

模拟估计允许有限抽样误差；公式给的是模型总体标准差。若把 `rho` 改为0，第二种构造也回到独立噪声情况；改为1则所有列共享同一个噪声，平均次数增加不再降低它的标准差。

### 同时计算置信区间与后验区间

```python
from math import sqrt
from statistics import NormalDist
from scipy.stats import beta

k, n = 30, 40
p = k/n
z = NormalDist().inv_cdf(0.975)
den = 1 + z*z/n
center = (p + z*z/(2*n))/den
half = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/den
wilson = (center-half, center+half)
posterior = beta(1+k, 1+n-k)
credible = posterior.ppf([0.025, 0.975])
print("样本正确率与Wilson区间:", p, wilson)
print("均匀先验下的后验均值与可信区间:", posterior.mean(), credible)
assert abs(wilson[0] - 0.5980603857923197) < 1e-12
assert abs(posterior.mean() - 31/42) < 1e-12
```

完整的[可下载实验脚本](/n3-hearingpedia/code/probability-theory/experiments.py)汇总上述计算，并增加听者混合导致的协方差、检测模型和阈值反解；需要Python、NumPy和SciPy。绘图与音频采用不同固定种子，种子只固定示例，不改变模型定理。

### 六个自检问题

1. 命中率0.8、虚报率0.1，是否足够知道“报有声后确实有声”的概率？
2. 40次中30次正确，下一次答对概率是否已被证明等于0.75？
3. 两种噪声的幅值直方图相同，能否认为它们的时间相关也相同？
4. 平均16次没有得到12 dB信噪比改善，应优先检查哪些模型条件？
5. 把试次数从40增加到160，独立同概率条件下正确率的标准误差怎样变化？
6. 给定某听者后试次独立，是否意味着随机抽一位听者完成整套试次时，所有试次在总体上仍独立？

<details><summary>展开答案与推理</summary>

<p>1．还需要有目标的先验概率；用全概率算出所有报有声的路径，再用贝叶斯公式更新。</p>
<p>2．0.75是这个独立同概率模型的最大似然估计；有限数据仍有参数不确定性，条件变化时也不能直接外推。</p>
<p>3．不能。边缘分布不决定联合分布；例如图2中的独立高斯与相关高斯具有相同单点分布。</p>
<p>4．检查跨次是否共享噪声、噪声方差是否一致、目标是否对齐且保留、增益或归一化是否改变，以及信噪比是否按同一均方值定义计算。</p>
<p>5．标准误差与试次数平方根成反比，因此减半；不是减少到四分之一。</p>
<p>6．不一定。两类听者正确概率0.6与0.9的例子中，共享的潜在听者类别带来0.0225的跨试次协方差。给定类别后独立，并不使混合后独立。</p>

</details>

学完后，可用[混淆矩阵](../confusion-matrix/)组织多类别刺激—反应的联合频率，用[信号检测论](../signal-detection-theory/)区分敏感度与判据，用[频谱与功率谱密度](../spectrum-and-power-spectral-density/)继续理解随机过程的频域描述。阅读实验结果时，先找随机对象与条件，再找独立性、抽样单位和不确定性，比先代入某一个公式更有帮助。
