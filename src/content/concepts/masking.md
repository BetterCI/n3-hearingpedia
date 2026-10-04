---
title: 掩蔽
english: Masking
slug: masking
summary: 用目标检测条件的变化研究声音之间的相互影响。
categories: [psychoacoustics]
tags: [detection, threshold, simultaneous-masking, forward-masking]
aliases: [听觉掩蔽, masking threshold, 同时掩蔽, 前向掩蔽, 非同时掩蔽]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: speech-reception-threshold, relation: related }
  - { slug: binaural-intelligibility-level-difference, relation: related }
  - { slug: auditory-filter, relation: mechanism }
  - { slug: speech-intelligibility, relation: application }
  - { slug: temporal-envelope, relation: related }
references: [glasberg-1990, oxenham-2006]
order: 4
---

## 一句话理解

掩蔽描述其他声音的存在如何改变目标声音的可检测性；实验必须明确目标、掩蔽声和判定任务。

## 直觉

判断背景声中有没有一个微弱目标，比听孤立目标需要更多信息。实验通过固定目标和背景的条件，测量达到规定表现水平所需的目标强度。

“听不见”“听见但认不出”与“听错内容”对应不同问题，不应把所有表现下降都解释为同一种机制。

## 核心概念

同时掩蔽中，目标与掩蔽声在时间上重叠；非同时掩蔽中，两者不重叠。掩蔽声先于目标的情况通常称为前向掩蔽。比较实验时要报告持续时间、间隔和声级。[Oxenham & Simonson, 2006](#ref-oxenham-2006)

凹口噪声实验利用掩蔽阈值随噪声频谱变化的关系估计听觉滤波器，但这种估计依赖模型假设。[Glasberg & Moore, 1990](#ref-glasberg-1990)

## 一个清楚的测量定义

可以用阈值差描述某个规定条件下的掩蔽量：

$$
M=L_{\mathrm{threshold,masker}}-L_{\mathrm{threshold,quiet}}
$$

- $M$：阈值升高量，单位 dB。
- $L_{\mathrm{threshold,masker}}$：存在掩蔽声时的目标阈值。
- $L_{\mathrm{threshold,quiet}}$：安静条件下的目标阈值。

两项必须使用相同标度、刺激和阈值判定标准。这个差值描述实验结果，不单独说明产生结果的机制。

## 实验设计入口

一个便于讨论的设计是：固定目标纯音频率，逐步改变噪声凹口宽度，比较检测阈值。实施前还需确定适应程序、试次数、耳机校准和统计方案。

## 阅读组内论文时

1. 目标与背景的时间关系是什么？
2. 改变的是目标声级、背景声级，还是信噪比？
3. 任务要求检测还是识别？阈值对应多大正确率？
4. 不同条件是否具有一致的校准与基线？

## 后续更新关注点

把新论文的任务、刺激和声级整理为可比较的条件表。语音在竞争声中的识别结果，应另外记录材料和评分方式。
