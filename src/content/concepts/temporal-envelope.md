---
title: 时间包络
english: Temporal Envelope
slug: temporal-envelope
summary: 描述频带信号的幅度随时间如何变化，明确它是怎样提取的。
categories: ["signal-processing","acoustics"]
tags: [hilbert, envelope-extraction, modulation]
aliases: [包络, 时域包络, ENV, Hilbert, 希尔伯特变换, amplitude envelope]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["scipy-hilbert","smith-2002","shannon-1995","viemeister-1979"]
illustration: {"src":"figures/envelope-tfs.svg","alt":"正弦调幅声音的波形、上下包络和归一化载波","caption":"教学示意：400 Hz 载波、20 Hz 调制、深度 0.7。橙线表示幅度包络，快速振荡与较慢幅度起伏是同一信号的不同描述。"}
order: 5
literature_checked_at: "2026-10-04"
knowledge_area: "sound"
kind: "representation"
key_facts: [{"label":"含义","value":"幅度随时间的变化"},{"label":"常用表示","value":"解析信号幅度、整流低通、短窗 RMS"},{"label":"依赖条件","value":"频带、滤波与时间尺度"}]
---

**时间包络**（temporal envelope）是信号幅度随时间变化的一种表征。听觉研究通常在指定频带中提取包络，以分析调制、语音线索或构造编码与[声码器](../vocoder/)输出。包络取决于提取方法和频带，宽带信号没有一个适用于全部任务的唯一包络。[1](#ref-scipy-hilbert "scipy.signal.hilbert")

## 定义与分类

包络与[振幅调制](../amplitude-modulation/)分别是表示与信号变化方式；调制谱描述起伏的频率成分。[时间精细结构](../temporal-fine-structure/)描述同带较快相位变化。采用不同提取方法时，应注明平滑尺度及归一化；数字包络采样率还不同于[人工耳蜗](../cochlear-implant/)的脉冲重复率。

### 数学定义

对实信号 $x(t)$，解析信号为：

$$
z(t)=x(t)+j\mathcal{H}\{x(t)\},\qquad e(t)=|z(t)|
$$

- $t$：时间，单位 s。
- $\mathcal{H}$：Hilbert 变换。
- $j$：虚数单位。
- $z(t)$：复解析信号。
- $e(t)$：Hilbert 幅度包络，与原信号具有相同幅度单位。

若 $\phi(t)=\arg z(t)$，则 $x(t)=e(t)\cos\phi(t)$。这是数学分解，不自动等同于听觉系统采用的生理编码。[1](#ref-scipy-hilbert "scipy.signal.hilbert")

## 原理与表征

### 直观解释

把波形的快速振荡想作载体，包络描述这些振荡的幅度轮廓。但“包络就是缓慢变化”不够精确：宽带信号的 Hilbert 包络也可能包含快速起伏。

### 为什么要先说明频带

在语音研究中，常先分频带，再提取各频带包络。滤波带宽和提取后的平滑方式都会影响实际保留的线索。Hilbert 法与整流后低通法应分别报告。[2](#ref-smith-2002 "Chimaeric sounds reveal dichotomies in auditory perception")

Shannon 等的经典研究以频带包络调制噪声，展示了受限频谱条件下的语音识别。这个结果不能直接推广为“所有语音任务只需要包络”。[3](#ref-shannon-1995 "Speech recognition with primarily temporal cues")

### 一个教学信号

$$
x(t)=\left[1+m\cos(2\pi f_m t)\right]\cos(2\pi f_c t)
$$

$f_c$ 是载波频率，$f_m$ 是调制频率，均以 Hz 为单位；$m$ 为无量纲调制深度。令 $0\leq m\leq1$ 且调制频率远低于载波频率，可直观看到幅度轮廓与快速振荡。

### 调制谱与调制度

对平均幅度 $\bar a>0$ 的包络，可构造无量纲相对起伏 $u(t)=[a(t)-\bar a]/\bar a$，再考察其调制频谱。有限语音片段还需注明加窗和频谱归一化。对于理想正弦调幅，深度 $m$ 与调制频率 $f_m$ 共同决定包络；自然语音一般不能用单个 $m$ 概括。

行为上的时间调制传递函数测量听者检测不同 $f_m$ 的能力，其结果依赖载波、呈现时长和声级。这一行为曲线不是对某一个神经元低通截止频率的直接测量。[4](#ref-viemeister-1979 "Temporal modulation transfer functions based upon modulation thresholds")

## 测量与研究方法

### 包络提取不是一个唯一运算

Hilbert 幅度、全波整流后低通以及短窗 RMS 都能生成“幅度随时间”的描述，但不是相同的量。Hilbert 法适合在明确频带内分析；整流低通法的结果依赖低通截止频率和阶数；RMS 法还依赖窗长与重叠。宽带语音的一个总包络不能替代各频带包络。[1](#ref-scipy-hilbert "scipy.signal.hilbert")

直流分量描述平均幅度，较慢调制与音节和停顿有关，较快调制可与周期性和快速音素变化有关。这些是相关的时间尺度，不能把某一调制频率直接指定为某个语言单位的唯一编码。

### 低通与采样率怎样选择

若提取后的包络保留到 $f_e$ Hz，后续采样率应满足带限重建的要求，并在降采样前做抗混叠滤波。仅把原波形隔点抽取，不等于正确获得低速包络。滤波器群延迟和起止瞬态还可能使两耳包络失去原有同步。

低通后包络越平滑，通常会损失较快变化；但保留更多高频调制也可能引入与载波相互作用的侧带。选择截止频率要联系具体任务，不能把某篇声码器研究的参数当作所有语音或音高任务的默认最优值。

### 包络重组实验能说明什么

把声音 A 的各带包络与声音 B 的精细结构合成，可以检验哪些线索在某任务中支配判断。经典听觉嵌合声研究提供了这种思路。[2](#ref-smith-2002 "Chimaeric sounds reveal dichotomies in auditory perception") 但重组信号经后续滤波后可能产生新包络，实验解释需要检查最终输出，而非只检查处理中间变量。

少量频带包络可支持一定语音识别，是声码器研究的重要发现。[3](#ref-shannon-1995 "Speech recognition with primarily temporal cues") 这不意味着包络足以解释音乐、空间听觉、复杂竞争语音或所有声调信息。

### 可复现的最小分析流程

选一段语音，保留原波形和采样率；先分频，再提取各带包络；画出各带平均幅度、时间曲线和调制谱；改变低通参数后重新合成，并检查声级、侧带和延迟。测试材料、滤波器实现及归一化应一并保存。对双耳信号应保留共同时间轴，避免独立处理时人为消除 ITD。

## 分析示例

### 解释示例：100 Hz 起伏从哪里来

单一 1000 Hz 正弦在理想解析表示中具有恒定包络。900 与 1000 Hz 两个分量同落一个分析带时，合成幅度可出现由频差决定的起伏。这种起伏来自分量相互作用，并不要求输入信号单独添加一个 100 Hz 调幅器。

若缩窄分析带使两分量分离，各自的包络又可能接近恒定。因此同一宽带波形可以因分频不同而得到不同包络表示。演示时宜同时画输入谱、每带波形和包络，而非只展示一条红色包络线。

这也解释为什么再生包络重要：经不同滤波后，原来被称为“精细结构”的信号可能产生可供识别的幅度变化。[2](#ref-smith-2002 "Chimaeric sounds reveal dichotomies in auditory perception") 对声码器或人工耳蜗算法，应检查最终输出所保留的调制，不只检查提取阶段。

## 研究沿革

1995 年分带时间线索的声码器研究显示，受控包络信息可支持一定语音识别。2002 年嵌合声研究进一步通过交换包络和精细结构考察不同感知任务。两者是研究信息利用的实验路线，并不建立“包络独立解释全部听觉”的结论。[3](#ref-shannon-1995 "Speech recognition with primarily temporal cues") [2](#ref-smith-2002 "Chimaeric sounds reveal dichotomies in auditory perception")
