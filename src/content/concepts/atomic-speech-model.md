---
title: "原子语音模型"
english: "Atomic speech model"
slug: "atomic-speech-model"
summary: "解释基于 Gabor 原子的稀疏语音表示和原子率。"
categories: ["signal-processing"]
tags: ["ASM","组内文献"]
aliases: ["ASM"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"get-vocoder","relation":"prerequisite"},{"slug":"speech-reception-threshold","relation":"prerequisite"},{"slug":"binaural-integration","relation":"prerequisite"}]
references: ["kong-atomic-2025","meng-get-2023"]
order: 26
---

## 一句话理解

原子语音模型（ASM）把语音表示为分散在时间和频率上的短时 Gabor 原子，用可控的稀疏度研究听者需要多少、以及怎样组织信息才能理解语音。

## 原子是信号单元

这里的“原子”不是物理粒子。它是局部化的信号构件，与 GET 的高斯包络振荡单元有形式上的联系。ASM 论文对分频后的信号进行稀疏采样，再以相应原子组织可播放语音；完整算法要按原文核验。[Kong 等，2025](#ref-kong-atomic-2025)；[GET 方法背景](#ref-meng-get-2023)

概念性的合成表示为：

$$
\hat{x}(t)=\sum_{q=1}^{Q}a_q\,g_q(t).
$$

$q$ 是事件索引，$a_q$ 为权重，$g_q$ 指定其时间、频率和形状。本式只表示单元叠加，不规定论文的选择算法或采样规则。

## 原子率怎样报告

若一段长度为 $T$ 秒的信号含 $Q$ 个合成事件，可定义教学上的总事件率 $R=Q/T$，单位原子/秒。论文具体采用的原子率统计口径还需区分总率、每带采样率与选择后事件数，不能只写一个数字。

稀疏程度不仅取决于事件数，也取决于事件分布。把同样数量集中于少数频带，与均匀铺开，不保证包含相同语音信息。

## 阈值与双耳实验

论文通过调整原子率寻找达到规定识别水平的条件；这里的 SRT 是原子率阈值，不是噪声信噪比阈值。它还通过跨耳分配等条件探索双耳整合，结果存在条件和个体差异。[Kong 等，2025](#ref-kong-atomic-2025)

因此把 ASM 结果与噪声下 dB SNR 阈值放在同一个数值轴上没有意义。应分别解释稀疏信息利用和抗掩蔽任务。

## 边界与后续更新

能理解某一种稀疏表示，并不证明自然听觉以同样原子实现编码。后续需核对原子选择、时频分辨率、幅度归一化和事件率定义，再整理单耳、双耳及延迟条件的复现方案。
