---
title: "脉冲式高斯包络音声码器"
english: "Pulsatile Gaussian-enveloped-tone vocoder"
slug: "get-vocoder"
summary: "解释高斯包络音、逐脉冲模拟和时频权衡。"
categories: ["signal-processing","research-methods","cochlear-implants"]
tags: ["GET vocoder"]
aliases: ["GET vocoder","GET","GET声码器","Gabor atom","高斯包络音"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["meng-get-2023","kong-comparable-2023","gabor-1946"]
illustration: {"src":"figures/gaussian-width.svg","alt":"两种高斯时间宽度及对应的频谱宽度","caption":"教学示意：高斯幅度包络及其归一化傅里叶幅度；频轴为相对中心的偏移。时间宽度变小，频谱变宽。幅度标准差定义见正文，图非电刺激或听者实测。"}
order: 25
knowledge_area: "methods"
kind: "model"
key_facts: [{"label":"缩写","value":"GET vocoder"},{"label":"合成单元","value":"脉冲式高斯包络音"},{"label":"关键权衡","value":"时间宽度与频谱宽度"}]
---

**脉冲式高斯包络音声码器**（pulsatile Gaussian-enveloped-tone vocoder，GET vocoder）以局部化高斯包络振荡单元合成声音，将编码事件与声学模拟相联系。单元宽度、载波、幅度与事件时序共同决定输出，模型仍经过正常声学听觉系统。[1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

## 定义与分类

GET 既可指 Gaussian-enveloped tone 单元，也可出现在[声码器](../vocoder/)模型名称中，应依语境区分。它属于[声码器](../vocoder/)的一种，[原子语音模型](../atomic-speech-model/)使用相关局部单元却有不同选择与任务。高斯单元的数学宽度定义不自动给出有效神经通道或电刺激扩散。

### 与传统声码器的区别

传统噪声或正弦声码器常用每带包络调制持续载波。GET 模型强调由刺激事件组织声学脉冲，可纳入谱峰选择、压缩与事件时序，便于研究编码步骤和时频权衡。[1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

改变单元带宽会同时影响跨带重叠与时间特征，因此实验应说明控制了哪些量。不能把一个“通道数”参数当作全部模拟条件。

## 原理与表征

### 高斯宽度与频谱宽度

用便于教学的标准差参数表示单个实值单元：

$$
g(t)=A\exp\left[-\frac{(t-t_0)^2}{2\sigma_t^2}\right]\cos[2\pi f_c(t-t_0)+\phi].
$$

$t_0$ 是中心时间、$f_c$ 是载波频率、$\phi$ 是相位、$\sigma_t$ 以秒表示。对高斯幅度包络，其傅里叶幅度的宽度参数 $\sigma_f=1/(2\pi\sigma_t)$。缩短[时间包络](../temporal-envelope/)会拓宽频谱；这是数学关系，图中的曲线是教学示意，非受试者实测。

对上述高斯包络（不含实值载波的双边总谱），若改用能量加权标准差，则 $\Delta t=\sigma_t/\sqrt2$、$\Delta f=\sigma_f/\sqrt2$，有 $\Delta t\Delta f=1/(4\pi)$。原 GET 论文用另一种幅度下降界限定义有效时长与带宽，并得到相应的乘积关系。比较论文参数时必须先统一宽度定义，不能把这些不同常数当作矛盾。[1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")；[3](#ref-gabor-1946 "Theory of communication. Part 1: The analysis of information")

## 测量与研究方法

### 事件序列怎样承载信息

多个 GET 单元可按事件时刻叠加，幅度表达选中通道的信息，载波和宽度控制局部频谱。事件率、通道选择和事件宽度共同决定输出。高事件率不保证输出仍像互相独立的短脉冲，单元可能重叠；较窄单元也不保证更独立的频谱通道，因为频谱随之拓宽。

### 与噪声和正弦声码器比较

噪声载波带有随机起伏，连续正弦载波有稳定频率，GET 以局部事件形式组织载波。比较三者时，应控制分析滤波、包络、选择规则与响度，同时检查它们保留的实际周期性。载波名称相同或通道数相同，都不足以保证线索一致。

GET 原研究探讨用此类声学单元模拟电刺激时间和频谱特性，并进行声学行为评价。[1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation") 声学[耳蜗](../cochlea/)仍会再次滤波，不能把合成波形等同电场或神经响应。

### 可复现参数表

至少保存分析带边界、单元宽度定义、载波频率、相位规则、事件率、通道选择、压缩与归一化。对双耳实验，还需记录事件是否同步与随机成分是否共享。先用单事件和短序列验证时域及频域，再测试完整语音，可以避免参数命名正确而输出错误。

## 应用与解释边界

### 可比编码与可比感知

相关研究进一步研究声学与电听觉中采用可比编码时的感知模式。这支持以编码结构为线索组织模拟与比较，而不是仅按载波名称判断模型是否合适。[2](#ref-kong-comparable-2023 "Comparable Encoding, Comparable Perceptual Pattern: Acoustic and Electric Hearing")

当前该引用已核对摘要；具体编码参数和跨群体比较应在阅读全文后再扩展，不能把相似趋势说成感知完全等价。

### 模拟的边界

GET 音经过正常耳蜗与正常听觉通路，而[人工耳蜗](../cochlear-implant/)直接电刺激神经。模拟不能自动复制神经存活、真实电流扩散、插入深度和长期适应。

## 分析示例

### 解释示例：缩短事件的双重作用

将高斯时间宽度减半，在相同宽度定义下频谱宽度加倍。事件在时间上更局部，却会覆盖更广频率；如果载波间距不变，谱重叠可能增强。这说明时间清晰度与谱独立性之间存在需要共同检查的关系。

固定事件峰值时，缩短宽度还改变总能量。若要比较宽度效应，应说明是固定峰值、单事件能量还是整句 RMS，三种归一化可能产生不同结果。[1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

教学图只表示理想高斯关系。实际输出叠加、合成过滤和听者的听觉滤波会继续改变谱与包络，因此不能用图中一条宽度曲线直接预测语音或音高成绩。

## 研究沿革

Gabor 的时频局部化理论提供数学背景；2023 年 GET 正式论文提出与刺激事件对应的声学模拟。可比编码研究进一步连接声学与电听觉感知模式。这里的理论、模型与跨人群证据分别承担不同作用，不可把数学局部化关系当作临床收益证明。[3](#ref-gabor-1946 "Theory of communication. Part 1: The analysis of information") [1](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation") [2](#ref-kong-comparable-2023 "Comparable Encoding, Comparable Perceptual Pattern: Acoustic and Electric Hearing")
