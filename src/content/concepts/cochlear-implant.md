---
title: 人工耳蜗
english: Cochlear Implant
slug: cochlear-implant
summary: 将声音处理后的信息编码为电刺激，连接系统设计与听觉表现。
categories: ["cochlear-implants","hearing-loss"]
tags: [electric-hearing, speech-processor, electrode-array, cis]
aliases: [CI, cochlear implants, 电听觉, 耳蜗植入, CIS, 人工耳蜗系统]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zeng-2008","wilson-1991","friesen-2001","zhou-tle-2022","zhou-f0intfs-2023"]
order: 8
literature_checked_at: "2026-10-04"
knowledge_area: "technology"
kind: "technology"
key_facts: [{"label":"输入输出","value":"声学输入转为电刺激"},{"label":"主要环节","value":"处理器、植入部分、电极—神经接口"},{"label":"评价任务","value":"语音、音高、空间听觉与使用体验"}]
---

**人工耳蜗**（cochlear implant）是把声学信息转换为电刺激、通过植入电极向听觉神经提供输入的听觉技术。其功能依赖声音处理、刺激映射、电极—神经接口和听者适应。它改变听觉输入方式，不是简单复原自然[耳蜗](../cochlea/)的机械过程。[1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

## 定义与分类

人工耳蜗、声音编码策略与声学模拟属于技术、算法和研究模型三个层次。[n-of-m](../n-of-m-coding/)描述谱峰选择，[TLE](../temporal-limits-encoder/)与[F0inTFS](../f0-in-tfs/)描述特定时间信息处理，[声码器](../vocoder/)则生成可播放的声学模拟。不能把算法的输出规律与真实植入者效果混为同一证据。

### 一个简单的电荷定义

对于矩形脉冲的一相：

$$
Q_{\mathrm{phase}}=I\,\tau
$$

- $I$：这一相的电流幅值，单位 A。
- $\tau$：这一相的持续时间，单位 s。
- $Q_{\mathrm{phase}}$：每相电荷量，单位 C。

这是量的定义，不是刺激设置建议。具体研究需报告波形、各相参数、相间间隔与电极配置；不能只用每相电荷量概括刺激。

## 原理与表征

### 直观解释与系统框图

**麦克风 → 声音处理器 → 传输链路 → 接收／刺激器 → 电极 → 听觉神经系统**

处理器决定提取和编码哪些声音信息；刺激器与电极负责实施电刺激。系统框图是理解论文的起点，不能单独解释最终感知表现。[1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

### 核心研究问题

阅读系统研究时，可以分开考虑声音表征、刺激方式、频率分配与评价任务。把“通道”理解为算法中的频带、电极接触点或功能上可分辨的信息来源时，需要明确具体含义。

### 经典编码入口

Wilson 等的早期研究比较了连续交错采样（CIS）与压缩模拟策略，CIS 使用非重叠顺序呈现的短脉冲。引用这一结果时，应保留早期研究的受试者和策略范围。[2](#ref-wilson-1991 "Better speech recognition with cochlear implants")

### 从声波到电刺激的完整链条

处理器通常经历拾音、增益控制、分频、特征提取、通道选择和电刺激映射，再由植入部分驱动电极。映射把声学幅度转换为适合个体的刺激参数；可听阈、舒适范围与脉冲形状共同决定输出。处理器的数字表示和神经实际接收到的信息之间，还隔着电极—组织接口。[1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

电刺激的频率至少有三种含义：分析频带的声学中心频率、脉冲重复率，以及脉冲幅度调制率。它们都可用 Hz 或每秒脉冲表示，却承担不同功能。“提高频率”必须说清改变的是哪个量。

### 脉冲电荷与时间安排

矩形相的电荷可写为 $Q=I\tau$，其中 $I$ 是电流、$\tau$ 是相宽；例如用安培和秒时，$Q$ 的单位为库仑。双相刺激通常设计为电荷平衡，但仅凭正负相面积相等不足以证明整套输出满足设备要求。相间隔、重复率和电极配置也影响刺激。

这一公式用于理解论文参数，不用于自行制定刺激剂量。比较两种策略时应记录相宽和刺激幅度是否随速率改变，避免把电荷、响度或时间占用的差异误归为算法本身。

### CIS 与 n-of-m 的选择逻辑

CIS 强调不同通道脉冲在时间上顺序安排，以减少同时刺激相关的相互作用；n-of-m 在每个分析帧从 $m$ 个候选通道中选择 $n$ 个谱峰。前者描述刺激安排的重要原则，后者描述信息选择，两者不应当作互斥的同一层参数。[2](#ref-wilson-1991 "Better speech recognition with cochlear implants")；[1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

物理电极数并不等于独立感知通道数。电流扩散、神经状态和谱峰的冗余会限制增加通道的实际收益。不同设备和任务的通道数结果应按条件理解。[3](#ref-friesen-2001 "Speech recognition in noise as a function of the number of spectral channels: Comparison of acoustic hearing and cochlear implants")

### 评价不止是安静语音

| 评价层面 | 可用任务 | 要回答的问题 |
| --- | --- | --- |
| 语音 | 安静和噪声识别、SRT | 语言信息能否被稳定利用 |
| 音高 | 辨别、排序、旋律或声调 | 周期性与位置线索能否支持任务 |
| 双耳 | 侧化、定位、噪声中识别 | 两侧输入能否有效协同 |
| 使用体验 | 音质与聆听努力 | 同样成绩的代价和感受如何 |

若策略在音高排序中改善，不能直接宣布噪声语音或生活交流改善。TLE 的真实植入者研究与 F0inTFS 的声学模拟，属于不同证据层次。[4](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")；[5](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

## 测量与研究方法

### 如何阅读个体差异

平均收益可能包含获益明显、变化很小和表现下降的个体。宜同时查看配对数据、听者经验、原有映射和适应时间。短时实验评估的是即时可用性；长期使用效果需要相应随访证据。良好的工程输出是必要的评价环节，仍需与真实听者的任务表现相结合。

## 应用与解释边界

### 声学模拟的边界

[声码器](../vocoder/)便于操纵声学线索，但没有直接重建实际电极—神经接口。将模拟结果与植入者表现比较时，应分别交代两类实验的输入、听者和研究任务。[1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

## 分析示例

### 解释示例：更规则的刺激是否更好

一种新策略产生更清楚的周期性电图，这是信号层面的可验证改变。接下来要检查总电荷、响度、频位分配和每通道事件数是否可比；然后才评价听者能否辨别或利用该规律。只展示电图不能证明音高、声调和语音都改善。

如果平均正确率提升，但收益主要来自少数人，应查看个体映射、原有表现和训练。较低基线可能留有更多提升空间，也可能伴随较大测量波动。真实植入者研究宜显示配对结果，而非只列两根柱状图。[4](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")

长期研究还需检验适应后的稳定性与不同任务间的代价。算法在某一任务保留更多周期性，同时可能改变幅度对比或刺激安排；策略评价应围绕这些具体变化建立对照。

## 研究沿革

1991 年 CIS 相关研究提出并比较顺序脉冲声音处理，2008 年系统综述连接处理器、植入接口及评价问题。之后的时间信息策略扩展音高和双耳研究。特定年代的设备结果提供发展背景，不应作为当前所有系统的统一性能或参数。[2](#ref-wilson-1991 "Better speech recognition with cochlear implants") [1](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation") [4](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")
