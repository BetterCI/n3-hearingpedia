---
title: 听觉滤波器
english: Auditory Filter
slug: auditory-filter
summary: 用频率选择性解释不同频率成分如何进入同一检测通道。
categories: ["psychoacoustics","ear-cochlea"]
tags: [frequency-selectivity, erb, notched-noise]
aliases: [听觉滤波, 频率选择性, ERB, 等效矩形带宽, auditory filtering]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["glasberg-1990","patterson-1976","oxenham-2006"]
illustration: {"src":"figures/auditory-filter.svg","alt":"两种 roex 滤波器及 ERB 随中心频率变化的示意","caption":"教学示意：左为简化对称 roex 功率权重，右为常见 ERB-N 经验式。模型参数用于解释形状，不是受试者拟合结果。"}
order: 3
literature_checked_at: "2026-10-04"
knowledge_area: "perception"
kind: "model"
key_facts: [{"label":"性质","value":"频率选择性的功能模型"},{"label":"常用量","value":"等效矩形带宽 ERB（Hz）"},{"label":"典型测量","value":"凹口噪声掩蔽"}]
---

**听觉滤波器**（auditory filter）是描述听觉频率选择性的功能模型。它用频率权重表示某个检测通道对附近成分的敏感程度，通常通过[掩蔽](../masking/)实验推断形状与带宽。行为估计不应未经说明等同于某个[耳蜗](../cochlea/)位置的机械调谐曲线。[1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

## 定义与分类

听觉滤波器与数字带通滤波器名称相似，证据来源不同。数字滤波器由设计者给定传递函数，听觉滤波器由行为与模型假设推断；耳蜗机械调谐来自局部测量。[掩蔽](../masking/)连接这些层次，[声码器](../vocoder/)的分析频带又是实验操纵。比较“通道数”时必须说明采用哪一层含义。

## 原理与表征

### 直观解释

想象同时开着许多相互重叠的频率窗口。检测一个目标音时，靠近它的噪声更可能进入相关窗口。窗口的“宽”和“形状”需要通过特定实验与模型估计。

### 核心概念

凹口噪声法在目标频率两侧留下频谱空隙，改变空隙宽度并测量目标的检测阈值，再依据模型推断滤波器形状。估计受到离频听取、滤波器非对称性及外中耳传递等假设影响。[1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

因此，行为估计出的滤波器不能未经说明就等同于某条基底膜调谐曲线。

### ERB 衡量的是等效带宽

对功率传递函数 $W(f)$，等效矩形带宽定义为：

$$
\mathrm{ERB}=\frac{\int_0^\infty W(f)\,df}{\max_{f\ge0} W(f)}.
$$

积分频率单位为 Hz，故 ERB 也以 Hz 表示。它把真实滤波器替换为峰值相同、总面积相同的矩形，既不是滤波器的矩形形状假设，也不等同于半功率带宽。常见正常听力经验式 $\mathrm{ERB}_N=24.7(4.37f_c/1000+1)$ 给出中心频率 $f_c$ 对应的近似值；例如 1000 Hz 时约 133 Hz。年龄、损伤、声级与测量范式可能使实际估计偏离经验值。[1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

### 一个可计算的形状模型

教学中可用简化的对称 roex 形式表示归一化功率权重：

$$
W(g)=(1+pg)e^{-pg},\qquad g=\frac{|f-f_c|}{f_c}.
$$

$p$ 控制裙边陡峭程度，越大通常越窄；$g$ 无量纲。用于实际拟合时常需更复杂的形式，以处理不对称和尾部，不能把此简式视作所有条件下的耳蜗传递函数。

### 为什么影响谐波、掩蔽与编码

相邻谐波若落在不同通道中，频谱峰更容易分别表征；若同落在一个较宽通道内，相互作用会产生包络拍频。于是滤波器带宽改变的不只是“能听到几个频率”，还改变可利用的时域线索。语音频谱中的局部峰谷，也可能在更宽的滤波后变得较难区分。

需要区分分析滤波器和合成滤波器。[声码器](../vocoder/)程序中的频带边界是人为参数，听者随后仍通过自己的听觉系统分析输出；[人工耳蜗](../cochlear-implant/)的电极刺激扩散则属于另一种空间相互作用。把程序设为 16 带，不能据此断言听者获得 16 个独立听觉通道。

## 测量与研究方法

### 经典实验入口

Patterson 的噪声刺激研究是这一领域的经典阅读入口；当前仅核验该文书目，具体实验设置应阅读原文。[2](#ref-patterson-1976 "Auditory filter shapes derived with noise stimuli")

同时掩蔽与非同时掩蔽的结果不宜直接混合解释，声级也应明确报告。[3](#ref-oxenham-2006 "Level dependence of auditory filters in nonsimultaneous masking as a function of frequency")

### 凹口噪声法怎样推断滤波器

在目标纯音两侧设置噪声，并逐步改变凹口宽度。凹口很窄时，落入目标相关滤波通道的噪声较多；凹口增宽后，通道内噪声能量下降，检测阈通常下降。把不同条件的阈值与噪声通过候选滤波器后的积分功率相联系，可拟合形状参数。

这一解释依赖若干假设：受试者主要使用目标附近的通道、决策需要的输出信噪比在条件间可近似保持、听觉系统的非线性没有破坏模型近似。非对称凹口有助于检验上下裙边差异；限制离频监听则影响滤波器宽度的估计。[2](#ref-patterson-1976 "Auditory filter shapes derived with noise stimuli")；[1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

### 如何比较研究中的带宽

至少同时报告中心频率、声级、同时或非同时掩蔽、拟合模型和听者特征。非同时掩蔽的声级依赖结果说明，忽略范式就比较 ERB 数值可能误导。[3](#ref-oxenham-2006 "Level dependence of auditory filters in nonsimultaneous masking as a function of frequency") 复现时宜先重现阈值随凹口宽度的趋势，再检查模型参数是否可辨识，而非只追求一个带宽数字。

## 分析示例

### 解释示例：相同 ERB 不保证形状相同

两个滤波器可以具有相同面积与峰值，因此 ERB 相同，却一个裙边陡而尾部较高，另一个主瓣较宽而尾部较低。若掩蔽声紧邻目标，两者可能产生不同阈值；若噪声位于较远频率，差异又可能由尾部决定。一个带宽数值无法代替完整形状。

阅读数据时可以先画出阈值随凹口宽度变化的曲线，再比较多个模型是否都能拟合。若不同参数组合给出近似曲线，参数可能不可唯一确定；增加非对称凹口或更广声级范围，可能比继续提高拟合小数位更有价值。[1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

研究问题还包括：观察到的变宽来自同一声级下的选择性改变，还是比较了不同可听度或不同范式？在行为测量中，先解决这种条件对应关系，再讨论生理解释。

## 研究沿革

Patterson 1976 年噪声刺激研究是经典方法入口；Glasberg 与 Moore 1990 年系统讨论凹口数据与滤波形状推导。2006 年非同时掩蔽研究进一步提示估计的声级依赖。方法沿革说明，滤波器不是一个脱离范式和声级的固定带宽。[2](#ref-patterson-1976 "Auditory filter shapes derived with noise stimuli") [1](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data") [3](#ref-oxenham-2006 "Level dependence of auditory filters in nonsimultaneous masking as a function of frequency")
