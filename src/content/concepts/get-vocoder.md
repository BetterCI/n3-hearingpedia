---
title: "脉冲式高斯包络音声码器"
english: "Pulsatile Gaussian-enveloped-tone vocoder"
slug: "get-vocoder"
summary: "解释高斯包络音、逐脉冲模拟和时频权衡。"
categories: ["signal-processing"]
tags: ["GET vocoder","组内文献"]
aliases: ["GET vocoder","GET","GET声码器","Gabor atom","高斯包络音"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"vocoder","relation":"prerequisite"},{"slug":"channel-interaction","relation":"prerequisite"},{"slug":"n-of-m-coding","relation":"prerequisite"},{"slug":"atomic-speech-model","relation":"related"}]
references: ["meng-get-2023","kong-comparable-2023"]
order: 25
---

## 一句话理解

脉冲式高斯包络音声码器（GET vocoder）用短时高斯包络音作为声学单元，构造与编码刺激序列相联系的逐脉冲模拟。GET 是单元，声码器是组织这些单元的模型。

## 一个单元长什么样

采用本词条的教学参数，一枚 GET 可写为：

$$
g(t)=A\exp\left[-\frac{(t-t_0)^2}{2\sigma^2}\right]
\cos[2\pi f_c(t-t_0)+\phi].
$$

$A$ 为幅度，$t_0$ 为中心时刻，$\sigma$ 为时间尺度，单位秒；$f_c$ 单位 Hz，$\phi$ 为相位。把多个单元放到不同时间与频率，并设置幅度，就能得到稀疏或密集的声学表示。

高斯包络越短，频谱通常越宽；越长，频谱越窄。这里的 $\sigma$ 与论文采用的有效时长、带宽指标不是同一符号定义，不能直接套用相同的数值常数。

## 与传统声码器的区别

传统噪声或正弦声码器常用每带包络调制持续载波。GET 模型强调由刺激事件组织声学脉冲，可纳入谱峰选择、压缩与事件时序，便于研究编码步骤和时频权衡。[Meng 等，2023](#ref-meng-get-2023)

改变单元带宽会同时影响跨带重叠与时间特征，因此实验应说明控制了哪些量。不能把一个“通道数”参数当作全部模拟条件。

## 可比编码与可比感知

共同论文进一步研究声学与电听觉中采用可比编码时的感知模式。这支持以编码结构为线索组织模拟与比较，而不是仅按载波名称判断模型是否合适。[Kong 等，2023](#ref-kong-comparable-2023)

当前该引用已核对摘要；具体编码参数和跨群体比较应在阅读全文后再扩展，不能把相似趋势说成感知完全等价。

## 模拟的边界

GET 音经过正常耳蜗与正常听觉通路，而人工耳蜗直接电刺激神经。模拟不能自动复制神经存活、真实电流扩散、插入深度和长期适应。后续补充单元时间与带宽的可视例子及编码驱动的复现记录，所有行为结论分别标注人群。
