---
title: 语音可懂度
english: Speech Intelligibility
slug: speech-intelligibility
summary: 在明确材料、听者和任务的条件下，测量语音被正确理解的程度。
categories: ["speech","psychoacoustics"]
tags: [word-recognition, srt, speech-in-noise]
aliases: [语音清晰度, 语音识别率, 正确率]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["plomp-1979","shannon-1995","smith-2002","wichmann-2001","steeneken-1980"]
illustration: {"src":"figures/psychometric-function.svg","alt":"不同斜率的理想语音心理测量函数与 50% 目标水平","caption":"教学示意：假定猜测下限 0.1、失误率 0.02，使用两种 logistic 尺度。曲线用于解释斜率与阈值，不是任何测试常模。"}
order: 7
literature_checked_at: "2026-10-04"
knowledge_area: "perception"
kind: "function"
key_facts: [{"label":"含义","value":"语音内容被正确理解的程度"},{"label":"常用结果","value":"正确率、心理测量函数、SRT"},{"label":"评分单位","value":"音素、词、关键词或整句"}]
---

**语音可懂度**（speech intelligibility）是听者正确理解语音内容的程度，常通过规定材料与评分规则下的识别表现测量。它受声学信息、[掩蔽](../masking/)、语言背景、听力状态和任务影响。可懂度应与音质、自然度和聆听努力分别评价。[1](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences")

## 定义与分类

固定条件的正确率与[语音接收阈](../speech-reception-threshold/)是两种结果形式：前者固定刺激条件，后者固定目标识别水平。物理预测指标与行为测量也应分开；[混淆矩阵](../confusion-matrix/)进一步描述错误分布。测试分类还可按开放或封闭集合、安静或噪声、评分单位和自适应程序区分。

### 正确率的定义

$$
P_{\mathrm{correct}}=\frac{N_{\mathrm{correct}}}{N_{\mathrm{scored}}}\times100\%
$$

- $N_{\mathrm{correct}}$：正确评分单元的数量。
- $N_{\mathrm{scored}}$：全部评分单元的数量。
- $P_{\mathrm{correct}}$：正确率，单位 %。

评分单元可以是词、关键词或句子，但必须声明。开放式回答与固定选项选择的机会水平也不同。

### 正确率必须先说明评分单位

词、关键词、音节、辅音和整句正确率回答的问题不同。三词串若按单词计分，一个错误扣掉一个单词；若按整串计分，同一次反应可能使整串判错。封闭集合提供备选答案，开放集合要求自行报告；相同百分比不能直接比较难度。

设正确次数为 $r$、有效试次数为 $N$，点估计为 $\hat p=r/N$。若试次近似独立且条件相同，可用二项分布框架评估不确定性。重复呈现同一材料、同一句多个关键词和同一听者多次作答可能相关，不能把它们全部当作独立样本以人为缩小区间。

## 原理与表征

### 直观解释

同一段声音，回答“有没有声音”“是什么词”“复述整句话”会得到不同指标。报告“可懂度提高”时，先追问：谁听、听什么、怎样评分？

可懂度与声音自然程度、主观偏好和聆听努力应分别测量，不能用一个百分比替代所有体验。

### 从固定条件到阈值

[语音接收阈（SRT）](../speech-reception-threshold/)现在有独立词条，解释不同阈值任务的变量、单位与适应程序。

固定信噪比下可以测正确率；适应性程序则可估计达到规定正确率所需的信噪比。在噪声中报告 SRT 时，应说明目标正确率、调整规则和材料。

Plomp 与 Mimpen 的句子 SRT 研究强调测试可靠性，提供了经典方法入口；不能把该材料的结果当作所有语言测试的统一标准。[1](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences")

### 客观指标与行为成绩的关系

物理或计算指标依据传输失真、调制保留或特征差异预测语音可懂度。STI 的经典研究属于用传输特性预测行为的路线。[5](#ref-steeneken-1980 "A physical method for measuring speech-transmission quality") 预测关系需要在相应材料、噪声和听者范围内验证；一个指标变好，不等于[人工耳蜗](../cochlear-implant/)听者的成绩必然改善。

可懂度还应与音质、自然度和聆听努力分别测量。语音可以被正确识别却听起来不自然，或需要很大努力才能达到较高正确率；这些结果对应用有不同意义。

## 测量与研究方法

### 经典研究怎样读

Shannon 等的包络研究提供了观察受限线索下语音识别的入口。[2](#ref-shannon-1995 "Speech recognition with primarily temporal cues")

阅读听觉嵌合声音实验时，可以比较包络与精细结构来自不同声音时的识别任务，同时留意分频带数量和材料范围。[3](#ref-smith-2002 "Chimaeric sounds reveal dichotomies in auditory perception")

这些实验展示了特定条件下的线索作用；不能只摘取一个识别率，省略刺激和听者条件。

### 心理测量函数比一个百分点更完整

用刺激条件 $x$ 表示 SNR 或声级，一个通用模型为：

$$
P(\mathrm{correct}\mid x)=\gamma+(1-\gamma-\lambda)F(x;\alpha,\beta).
$$

$F$ 是从 0 到 1 的递增函数，$\gamma$ 为猜测下限，$\lambda$ 为失误造成的上限损失，$\alpha,\beta$ 控制位置与斜率。$\alpha$ 的具体阈值含义依赖所选函数；不能一律当作 50% 正确率。对参数、失误率及拟合优度的处理会影响结论。[4](#ref-wichmann-2001 "The psychometric function: I. Fitting, sampling, and goodness of fit")

两种处理条件可能在低 SNR 附近差别很大，高 SNR 时却共同接近上限。只报告最容易条件中的正确率，会漏掉这一差异；只报告最困难条件，也可能遭遇地板效应。

### 怎样设计一次可靠比较

明确目标听者与评分规则，预先选择有区分力的难度范围；使用相当的列表并平衡顺序；报告安静与指定噪声条件；对同一听者的条件差使用配对分析。材料长度、语言熟练程度和训练量应纳入解释。

少量时域线索支持语音识别的经典[声码器](../vocoder/)结果，是研究信息必要性的起点。[2](#ref-shannon-1995 "Speech recognition with primarily temporal cues") 将任务扩展到噪声、声调、竞争说话人或真实植入者时，需要重新验证，不能仅凭前一个任务的高分判断整套听觉功能已经恢复。

## 分析示例

### 解释示例：80% 正确率并不唯一

一名听者正确识别八个完整句子中的全部内容，另一名在每句中都漏掉少量关键词；按关键词汇总可能得到相近分数，实际错误分布却不同。报告应让读者知道评分单位及错误是否集中在某类音素、说话人或难度。

两种条件在高 SNR 下均达 95%，并不说明没有差异：可能都接近任务上限。增加较困难但仍可测量的条件，有助于观察心理测量函数的位置或斜率。相反，长时间停留在猜测下限附近，也难以区分处理效果。[4](#ref-wichmann-2001 "The psychometric function: I. Fitting, sampling, and goodness of fit")

值得进一步研究的是，同样可懂度的两种输出是否带来不同聆听努力，以及个体改善是否跨材料保持。它们需要独立指标和适当的重复设计，不能从正确率自动推算。

## 研究沿革

经典句子 SRT 研究关注测试可靠性，1980 年 STI 研究提供物理传输特性预测的路线。声码器研究则检验经过信息削减后仍可识别多少内容。各方法回答不同问题，后续模型和新策略的评价仍需与目标听者及材料对应。[1](#ref-plomp-1979 "Improving the reliability of testing the speech reception threshold for sentences") [5](#ref-steeneken-1980 "A physical method for measuring speech-transmission quality") [2](#ref-shannon-1995 "Speech recognition with primarily temporal cues")
