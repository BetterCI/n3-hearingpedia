---
title: 频位映射关系
english: Tonotopy
slug: tonotopy
summary: 理解频率如何与耳蜗位置及神经系统中的组织关系相连。
categories: ["ear-cochlea","neuroscience"]
tags: [frequency-place, greenwood, cochlear-map]
aliases: [频位映射, 频率位置关系, frequency-place mapping, Greenwood]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["greenwood-1990","sridhar-2006","stakhovskaya-2007","oxenham-2004","kan-2013"]
illustration: {"src":"figures/frequency-place.svg","alt":"Greenwood 函数随顶端到基底归一化位置递增的对数频率曲线","caption":"教学示意：按正文坐标与参数绘制 Greenwood 函数。位置采用从顶端到基底的归一化柯蒂器坐标；曲线不是个体耳蜗测量。"}
order: 2
literature_checked_at: "2026-10-04"
knowledge_area: "biology"
kind: "organization"
key_facts: [{"label":"中文名称","value":"频位映射关系"},{"label":"对应变量","value":"频率与空间位置"},{"label":"典型模型","value":"Greenwood 耳蜗频率—位置函数"}]
---

**频位映射关系**（tonotopy）是听觉系统中频率与空间位置的有序对应。在[耳蜗](../cochlea/)中，较高频率主要对应基底侧，较低频率主要对应顶端侧；听觉通路的其他层级也有频率有序组织。具体函数与坐标必须针对所测结构定义。[1](#ref-greenwood-1990 "A cochlear frequency-position function for several species—29 years later")

## 定义与分类

频位映射关系不等于[音高感知](../pitch-perception/)，也不等于滤波带宽。前者描述空间组织，音高属于知觉属性，带宽描述频率选择性。声学分配频率、模型预测位置频率与实际感知匹配应分开记录。中央听觉的有序组织需要自身测量，不能直接套用耳蜗长度函数。

### 坐标选择决定映射含义

Greenwood 函数常写为：

$$
f(x)=A(10^{ax}-k),\qquad
x(f)=\frac{1}{a}\log_{10}\left(\frac{f}{A}+k\right).
$$

$x$ 为从顶端向基底计的归一化柯蒂器位置，$f$ 的单位为 Hz。常见人耳参数 $A=165.4$ Hz、$a=2.1$、$k=0.88$ 对应这一坐标约定；若改成距基底的距离，必须先转换坐标。本式是经验关系，不是每个人耳蜗的直接测量。[1](#ref-greenwood-1990 "A cochlear frequency-position function for several species—29 years later")；[2](#ref-sridhar-2006 "A Frequency-Position Function for the Human Cochlear Spiral Ganglion")

若柯蒂器总长度为 $L$，归一化位置可换算为距离 $d=xL$。同一个 $x$ 在不同 $L$ 的耳蜗中对应不同毫米位置；同一个插入深度也不保证对应同一自然特征频率。图像中的电极角度、沿耳蜗管距离和螺旋神经节坐标更不能混用。

## 原理与表征

### 直观解释

把展开的耳蜗看作一条带有频率坐标的轴。基底侧对应较高频率，顶端侧对应较低频率。位置与频率的关系不是“每毫米增加相同 Hz”的线性标尺。[1](#ref-greenwood-1990 "A cochlear frequency-position function for several species—29 years later")

Tonotopy 的中文名称在此采用 **“频位映射关系”**。

### 柯蒂器与螺旋神经节为何不同

毛细胞位置通过神经纤维投射到螺旋神经节，二者的长度和几何走向不同。人体解剖研究测量了这种对应关系，提示[人工耳蜗](../cochlear-implant/)刺激位置的频率估计需要考虑目标神经结构。只把电极毫米位置直接代入柯蒂器公式，可能忽略投射关系及个体差异。[3](#ref-stakhovskaya-2007 "Frequency Map for the Human Cochlear Spiral Ganglion: Implications for Cochlear Implants")

“分配频率”是处理器把哪个声学频带送往哪个电极；“位置频率”是解剖或生理模型预测该区域原本对应什么频率；“感知音高”则必须通过行为任务测量。三者可相近，也可明显不同。

### 用什么量描述不匹配

一个便于跨频率比较的教学指标是：

$$
\Delta_{\mathrm{oct}}=\log_2\frac{f_{\mathrm{assigned}}}{f_{\mathrm{place}}}.
$$

其单位为倍频程，正值表示分配频率高于所用模型的对应位置频率；乘以 12 可用半音报告。例如分配 1000 Hz、模型位置 2000 Hz 时，$\Delta_{\mathrm{oct}}=-1$。这个差值依赖位置频率的估计方法，不是直接测得的听觉误差，也不提供个人调机建议。

参数 $A$ 决定频率尺度，$a$ 控制指数变化速度，$k$ 调整低频偏移；三者为经验参数，不应脱离物种与坐标使用。

## 测量与研究方法

### 频位关系怎样参与音高与双耳任务

正常听力的移置刺激研究显示，在特定复合音任务中，仅把低频时间变化移到高频位置，并不能保证保留原来的复杂[音高感知](../pitch-perception/)。这支持位置与时间线索需要共同考虑；它不意味着所有音高都只由位置决定。[4](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception")

双侧人工耳蜗还涉及两耳之间的匹配。两边电极编号相同并不保证激活自然特征频率相同的区域。研究设计可将影像位置、跨耳音高匹配与侧化表现结合，分别报告各测量的不确定性。[5](#ref-kan-2013 "Effect of mismatched place-of-stimulation on binaural fusion and lateralization in bilateral cochlear-implant users")

## 分析示例

### 映射示例：先统一原点再比较

某报告给出“从基底沿耳蜗管量起 15 mm”，另一报告给出“从顶端归一化位置 0.5”。二者不能直接判断相同。需知道总长度与路径定义，先把基底距离转换为顶端距离，再除以对应总长度；如果一个沿外壁、另一个沿柯蒂器，还需要路径转换。未知信息应保留为不确定性。

即使公式得到相近频率，电极激活区域仍可能宽于一个点。比较位置模型与感知音高时，应同时报告估计误差和测量重复性，避免小于定位误差的差别被解释成精确的机制改变。[3](#ref-stakhovskaya-2007 "Frequency Map for the Human Cochlear Spiral Ganglion: Implications for Cochlear Implants")

耳蜗以外的听觉通路也存在频率有序组织，但中央响应受整合与可塑性影响。耳蜗位置函数不能直接拿来预测皮层毫米位置；不同层级的频位映射关系需要各自的测量。

## 研究沿革

Greenwood 1990 年论文重新整理了跨物种的耳蜗频率—位置函数。2006—2007 年人体螺旋神经节研究将柯蒂器坐标与神经结构联系起来，为人工耳蜗映射提供更具体的解剖背景。其后策略研究仍需区分个体解剖、处理器分配和行为适应。[1](#ref-greenwood-1990 "A cochlear frequency-position function for several species—29 years later") [2](#ref-sridhar-2006 "A Frequency-Position Function for the Human Cochlear Spiral Ganglion") [3](#ref-stakhovskaya-2007 "Frequency Map for the Human Cochlear Spiral Ganglion: Implications for Cochlear Implants")
