---
title: "语音接收阈"
english: "Speech reception threshold"
slug: "speech-reception-threshold"
summary: "介绍达到规定识别正确率时所需的测量条件、阈值和适应程序。"
categories: ["audiology","speech","research-methods"]
tags: ["SRT"]
aliases: ["SRT","语音接收阈值","speech recognition threshold"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zhou-zin-2024","kong-atomic-2025","plomp-1979","wichmann-2001","levitt-1971","smits-2004"]
illustration: {"src":"figures/psychometric-function.svg","alt":"正确率随 SNR 变化的两条示意曲线及目标水平","caption":"教学示意：目标水平与曲线的交点定义相应阈值；图中参数并非 ZIN、DIN 或临床标准。"}
order: 16
knowledge_area: "measurement"
kind: "metric"
key_facts: [{"label":"缩写","value":"SRT"},{"label":"定义","value":"达到规定识别水平所需的条件"},{"label":"单位","value":"按任务采用 dB SNR、声级或原子率"}]
---

**语音接收阈**（speech reception threshold，SRT）是听者在规定材料和评分规则下达到目标识别水平所需的刺激条件。许多任务采用 50% 正确率，但自变量、单位和猜测水平随测试变化。噪声阈值与稀疏语音的原子率阈值不能数值互换。[3](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences")

## 定义与分类

SRT 属于指标而非一套唯一测试。句子、数字和[生肖噪声测试](../zodiac-in-noise/)可采用不同材料和流程；[语音可懂度](../speech-intelligibility/)是被评价的功能，心理测量函数和适应程序是估计工具。原始百分比与扣除猜测后的水平也需要分别定义。

### 它是条件，不是一个固定单位

在噪声中常调整信噪比，报告 dB SNR；在安静中可调整呈现声级；稀疏语音实验还可能调整原子率。仅写“SRT 提高了 2”无法判断是什么意思。

可用以下通用表达理解：

$$
P(\mathrm{correct}\mid x^\ast)=p_{\mathrm{target}}.
$$

$x^\ast$ 是达到目标正确率 $p_{\mathrm{target}}$ 的条件。本式不指定自变量是 SNR、声级或原子率，也不保证所有实验采用相同的心理测量函数。封闭集合任务还需要考虑猜测水平。

### 可靠性与比较单位

列表等价性、重测误差、练习效应与猜测都会影响阈值。经典句子阈值研究把可靠性作为方法问题处理。[3](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences") 数字噪声测试则需验证自身材料与测试方式。[6](#ref-smits-2004 "Development and validation of an automatic speech-in-noise screening test by telephone")

报告个体重复测试及条件差的不确定性，比只列组平均更有帮助。若同一个体在两种条件中测试，应优先查看配对差，并平衡测试次序；一个差值小于该方法常见波动时，不能仅因方向一致就认定稳定改善。

## 原理与表征

### 升降规则的目标水平

标准等步长且反应近似独立、稳定的条件下，1-up/1-down 的常见规则追踪 50%，2-down/1-up 约追踪 70.7%，3-down/1-up 约追踪 79.4%。这些数值依赖规则含义与假设；改变升降步长、计分或反应处理后，需要重新确定目标。[5](#ref-levitt-1971 "Transformed Up-Down Methods in Psychoacoustics")

对于“越大越容易”的 SNR，正确反应通常使下一次更难，即降低 SNR。若自变量是另一种指标，应先明确难度方向。起始阶段的大步长用于快速接近目标，正式估计阶段的步长与反转规则影响精度；起始点附近的反转不宜未经说明全部混入平均。

### dB 改善依赖曲线斜率

相同的正确率变化，在陡峭函数上可能只对应很小 SNR 差，在平缓函数上则对应更大差。因而“提高 10 个百分点”和“改善 2 dB SRT”不是固定转换。两种条件若曲线斜率不同，只给一个阈值还可能掩盖高正确率区间的差异。

### 噪声阈值与稀疏语音阈值

ZIN 的阈值对应特定噪声、材料和评分程序；ASM 的阈值对应原子率。二者可共同服务语音研究，但量纲和任务不同。跨论文比较应先建立“材料—变量—目标正确率—单位”的对应表，再讨论相对收益，而不是把所有 SRT 排成统一优劣榜。

## 测量与研究方法

### 适应程序怎样寻找阈值

适应程序按受试者反应改变下一次刺激条件，在阈值附近集中取样。步长、升降规则、起点、终止规则及反转点平均方式都会影响估计。不同适应规则对应的目标水平可能不同，不能看到“自适应”就默认收敛于 50%。

材料熟悉程度、关键词或整句计分、[掩蔽](../masking/)声类型、训练与列表效应也影响结果。经典句子 SRT 文献是可靠性问题的入口，并非所有语言测试的统一规范。[3](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences")

### 不同研究如何使用 SRT

[生肖噪声测试](../zodiac-in-noise/)采用生肖材料，在噪声中用适应程序估计识别阈值，其 SRT 与噪声和测试版本相联系。[1](#ref-zhou-zin-2024 "The Chinese Zodiac-in-Noise Test: An Internet-Based Speech-in-Noise Test for Large-Scale Hearing Screening")

[原子语音模型](../atomic-speech-model/)论文则以 **原子率** 为调整变量寻找识别阈值；其单位不是 dB SNR。原子率越低仍能达到目标，表示在该任务中可利用更稀疏的表示。[2](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")

### 从心理测量函数求阈值

用 $P(x)=\gamma+(1-\gamma-\lambda)F(x)$ 描述正确率时，目标 $p_t$ 应位于上下渐近线之间。阈值满足：

$$
x^*=F^{-1}\left(\frac{p_t-\gamma}{1-\gamma-\lambda}\right).
$$

这里 $F^{-1}$ 对应选定的函数及其参数。封闭集合中，50% 原始正确率一般不等于扣除猜测后达到可用范围的中点。猜测水平还取决于逐词还是整串计分，不能只由界面显示的选项数决定。[4](#ref-wichmann-2001 "The psychometric function: I. Fitting, sampling, and goodness of fit")

## 应用与解释边界

### 结果报告与解释边界

至少报告材料、耳别、掩蔽声、目标正确率、适应规则、变量单位和不确定性。SNR 阈值更低通常表示该测试中表现更好，但不能把不同材料或版本的绝对值直接比较。

## 分析示例

### 解释示例：阈值方向和收益

同一材料中条件 A 的 SRT 为 −5 dB SNR，条件 B 为 −8 dB SNR。若定义改善为 A 减 B，则为 3 dB，表示 B 在更不利信噪比下仍达到相同目标。这里的负号并非较差表现；必须按自变量与定义解释。

若另一篇研究阈值为每秒原子数，则“更低更好”只在其固定表示和目标下成立，不能与 −8 dB 比大小。即使两测试均用 dB SNR，材料、掩蔽声和计分不同也可能造成不同绝对阈值。

一个有价值的复现目标是同时恢复阈值和曲线斜率，并检查重测波动。仅在单次阈值上相差很小，不能证明等价；等价判断需要预定界限及相应不确定性。[3](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences")

## 研究沿革

Levitt 1971 年提供变换升降法的经典方法背景，1979 年句子 SRT 研究关注可靠性。数字与生肖噪声测试后来建立各自材料及常模；ASM 则在不同量纲上采用阈值思想。共同名称意味着相似测量框架，不意味着相同绝对标度。[5](#ref-levitt-1971 "Transformed Up-Down Methods in Psychoacoustics") [3](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences") [6](#ref-smits-2004 "Development and validation of an automatic speech-in-noise screening test by telephone") [2](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")
