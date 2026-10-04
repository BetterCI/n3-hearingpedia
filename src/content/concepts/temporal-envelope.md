---
title: 时间包络
english: Temporal Envelope
slug: temporal-envelope
summary: 描述频带信号的幅度随时间如何变化，明确它是怎样提取的。
categories: [signal-processing]
tags: [hilbert, envelope-extraction, modulation]
aliases: [包络, 时域包络, ENV, Hilbert, 希尔伯特变换, amplitude envelope]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: temporal-fine-structure, relation: related }
  - { slug: amplitude-modulation, relation: related }
  - { slug: auditory-filter, relation: prerequisite }
  - { slug: vocoder, relation: application }
  - { slug: speech-intelligibility, relation: application }
  - { slug: cochlear-implant, relation: application }
references: [scipy-hilbert, smith-2002, shannon-1995]
order: 5
---

## 一句话理解

时间包络描述信号幅度随时间的变化；在研究中，它的含义取决于分频带方式和提取方法。

## 直觉

把波形的快速振荡想作载体，包络描述这些振荡的幅度轮廓。但“包络就是缓慢变化”不够精确：宽带信号的 Hilbert 包络也可能包含快速起伏。

## 数学定义

对实信号 $x(t)$，解析信号为：

$$
z(t)=x(t)+j\mathcal{H}\{x(t)\},\qquad e(t)=|z(t)|
$$

- $t$：时间，单位 s。
- $\mathcal{H}$：Hilbert 变换。
- $j$：虚数单位。
- $z(t)$：复解析信号。
- $e(t)$：Hilbert 幅度包络，与原信号具有相同幅度单位。

若 $\phi(t)=\arg z(t)$，则 $x(t)=e(t)\cos\phi(t)$。这是数学分解，不自动等同于听觉系统采用的生理编码。[SciPy 方法文档](#ref-scipy-hilbert)

## 为什么要先说明频带

在语音研究中，常先分频带，再提取各频带包络。滤波带宽和提取后的平滑方式都会影响实际保留的线索。Hilbert 法与整流后低通法应分别报告。[Smith et al., 2002](#ref-smith-2002)

Shannon 等的经典研究以频带包络调制噪声，展示了受限频谱条件下的语音识别。这个结果不能直接推广为“所有语音任务只需要包络”。[Shannon et al., 1995](#ref-shannon-1995)

## 一个教学信号

$$
x(t)=\left[1+m\cos(2\pi f_m t)\right]\cos(2\pi f_c t)
$$

$f_c$ 是载波频率，$f_m$ 是调制频率，均以 Hz 为单位；$m$ 为无量纲调制深度。令 $0\leq m\leq1$ 且调制频率远低于载波频率，可直观看到幅度轮廓与快速振荡。

## 阅读组内论文时

检查分析频带、包络提取方法、低通截止频率、滤波器阶数、边界处理和幅度归一化方式。只报告“提取包络”不足以复现刺激。

## 后续更新关注点

先补齐各论文对包络的操作性定义，再比较结论；将算法实现证据与行为或生理证据分开记录。
