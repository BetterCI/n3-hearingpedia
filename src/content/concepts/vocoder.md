---
title: 声码器
english: Vocoder
slug: vocoder
summary: 拆分、提取并重新合成声音，用于研究被保留线索的作用。
categories: ["signal-processing","research-methods","cochlear-implants"]
tags: [noise-vocoder, sine-vocoder, acoustic-simulation]
aliases: [噪声声码器, 正弦声码器, noise vocoder, sine vocoder, vocoding]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["shannon-1995","dorman-1997","meng-get-2023","friesen-2001","swaminathan-2014"]
order: 6
literature_checked_at: "2026-10-04"
knowledge_area: "methods"
kind: "model"
key_facts: [{"label":"研究用途","value":"受控改变声音信息"},{"label":"常见载波","value":"噪声、正弦、脉冲式声学单元"},{"label":"关键参数","value":"分频、包络、载波、合成与归一化"}]
---

**声码器**（vocoder）在听觉实验中通常指将声音分解后，用选定特征控制合成载波的模型。它可有针对性地改变频谱、时间或跨耳信息，用于研究语音感知及[人工耳蜗](../cochlear-implant/)相关信息限制。本文范围是听觉实验声码器，其他通信和语音合成语境需按具体系统区分。[1](#ref-shannon-1995 "Speech recognition with primarily temporal cues")

## 定义与分类

噪声声码器、正弦声码器和[GET 声码器](../get-vocoder/)是不同合成方式。载波类型是分类轴，分析带数、包络带宽和映射又是其他轴；不能仅由一种载波名称推断完整处理。声码器属于实验模型，[人工耳蜗](../cochlear-implant/)属于实际听觉技术，二者的接口与听者经验不同。

## 原理与表征

### 直观解释

先把语音分成几条频带，各自提取幅度变化，再用这些变化控制新的载波，最后合成输出。得到的声音与原声不同，但仍可保留一部分任务相关信息。

### 核心处理链

**输入 → 分析滤波器组 → 包络提取 → 载波调制 → 合成／滤波 → 输出**

一个概念性表达是：

$$
y(t)=\sum_{k=1}^{N}\mathcal{S}_k\{e_k(t)c_k(t)\}
$$

- $N$：通道数，无量纲整数。
- $e_k(t)$：第 $k$ 个分析频带提取出的包络。
- $c_k(t)$：指定幅度约定的噪声或正弦载波。
- $\mathcal{S}_k$：该通道使用的合成处理。
- $y(t)$：输出波形，单位由信号缩放约定决定。

公式只表示共同流程；具体实现必须另列滤波、缩放和载波生成参数。频带包络调制噪声是经典研究采用的一种构建方式。[1](#ref-shannon-1995 "Speech recognition with primarily temporal cues")

### 与人工耳蜗的连接

改变分析频带与合成载波的对应关系，可以研究频率—位置偏移的声学模拟。Dorman 等的研究提供了这一实验方向的经典入口。[2](#ref-dorman-1997 "Simulating the effect of cochlear-implant electrode insertion depth on speech understanding")

声学模拟的结果不应直接当作实际电刺激结果；两者的受试者、输入方式和研究范围必须分别说明。

### 分析与合成各负责什么

一个包络声码器可概念性地表示为：

$$
y(t)=\sum_{k=1}^{K}h_k^{(s)}*\left[a_k(t)c_k(t)\right].
$$

$a_k$ 来自分析滤波及包络处理，$c_k$ 是载波，$h_k^{(s)}$ 是可选的合成滤波器，$*$ 表示卷积。该式帮助区分处理环节，不规定所有声码器都使用相同合成结构。通道数、分析边界、载波频率和合成边界应分别记录。

噪声载波通常产生随机快速振荡；正弦载波具有稳定频率，却可能引入不属于原声的音高与拍频。脉冲式 GET 单元另以事件时间和高斯宽度控制结构。不同载波即使带数相同，也不一定保留相同的周期性或空间线索。[1](#ref-shannon-1995 "Speech recognition with primarily temporal cues")；[3](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

### 为什么模拟结果不能直接代表植入者

正常听力受试者通过完整声学[耳蜗](../cochlea/)聆听合成音；人工耳蜗通过电极刺激神经，存在电流扩散、神经存活差异、电动态范围和个体适应。声学频带重叠可以模拟某些信息损失，却不能自动复现电极—神经接口。

Friesen 等比较通道数与语音任务时发现，正常听力声码器听者与植入者对增加通道的收益不同。应把这理解为研究条件下的信息利用差异，而不是“所有人工耳蜗最多只能利用八个通道”。研究年代、设备与听者经验都限制外推。[4](#ref-friesen-2001 "Speech recognition in noise as a function of the number of spectral channels: Comparison of acoustic hearing and cochlear implants")

## 测量与研究方法

### 一张复现参数清单

| 模块 | 必须说明的内容 |
|---|---|
| 分析 | 频率范围、通道边界、滤波类型与阶数 |
| 包络 | Hilbert 或整流法、平滑及截止频率 |
| 载波 | 噪声或正弦、随机种子、载频或频带 |
| 合成 | 滤波、各通道增益、整体归一化 |
| 评价 | 材料、听者、训练、声级、任务与评分 |

### 怎样建立有解释力的对照

若研究位置偏移，可保持分析频带不变，仅改变合成频带，报告偏移量及边缘处理；若研究包络低通，则应保持载波、带数及输出声级。一次改变多项参数，会使结果难以归因。[2](#ref-dorman-1997 "Simulating the effect of cochlear-implant electrode insertion depth on speech understanding")

| 研究问题 | 主要操纵 | 必须额外检查 |
| --- | --- | --- |
| 频谱分辨率 | 通道数、带宽 | 总频率范围与载波类型 |
| 时域线索 | 包络低通、事件时序 | 调制谱、侧带与输出延迟 |
| 位置不匹配 | 合成频率映射 | 偏移方向和边缘频带 |
| 双耳线索 | 跨耳同步或分配 | 共同采样时钟与两耳声级 |

### 实现和报告的常见陷阱

滤波器在首尾的瞬态、随机噪声种子、归一化是在每句还是整套材料上进行，都会影响可复现性。比较策略时应先检查输出长时频谱、RMS、峰值、包络谱与必要的两耳相关性，再开展行为任务。

学习效应也不可忽略。陌生合成语音的短时成绩同时反映线索和适应。宜记录训练量、条件顺序和重复测量，区分初次接触表现与经过训练后可利用的信息。[5](#ref-swaminathan-2014 "Consonant identification using temporal fine structure and recovered envelope cues")

## 分析示例

### 解释示例：八带方案是否真的等价

两种声码器都称八带，却可能一个按等 Hz 划分，另一个按对数或 ERB 尺度划分；一个用噪声载波，另一个用正弦；包络截止频率还可能不同。它们对低频谐波、调制侧带与频谱细节的表达并不等价。

合理比较可先统一频率范围和带边界，再逐项替换载波或包络参数。将输出音频、实现版本和参数表保存，比只写“八通道声码器”更有复现价值。若涉及随机载波，固定种子用于输出核查，并用多个实例检验结果是否依赖某一随机片段。

研究问题可以是：某策略的音高收益来自事件时序，还是载波产生的新侧带？设计消除或保留侧带的对照，并评估语音任务，能比单独展示更规则的波形提供更强证据。[3](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

## 研究沿革

听觉科学中的包络声码器由经典时域线索研究形成重要实验路线，随后用于通道数和频率—位置不匹配等问题。2023 年 GET 方法将合成单元与编码事件更直接联系。新模型扩展了可操纵因素，仍需要相应信号检查和行为验证。[1](#ref-shannon-1995 "Speech recognition with primarily temporal cues") [2](#ref-dorman-1997 "Simulating the effect of cochlear-implant electrode insertion depth on speech understanding") [3](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")
