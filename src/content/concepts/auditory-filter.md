---
title: 听觉滤波器
english: Auditory Filter
slug: auditory-filter
summary: 用频率选择性解释不同频率成分如何进入同一检测通道。
categories: [psychoacoustics]
tags: [frequency-selectivity, erb, notched-noise]
aliases: [听觉滤波, 频率选择性, ERB, 等效矩形带宽, auditory filtering]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: cochlea, relation: prerequisite }
  - { slug: tonotopy, relation: related }
  - { slug: masking, relation: method }
  - { slug: vocoder, relation: application }
references: [glasberg-1990, patterson-1976, oxenham-2006]
order: 3
---

## 一句话理解

听觉滤波器是描述听觉频率选择性的功能模型：一个检测通道对附近频率的成分有不同的敏感程度。

## 直觉

想象同时开着许多相互重叠的频率窗口。检测一个目标音时，靠近它的噪声更可能进入相关窗口。窗口的“宽”和“形状”需要通过特定实验与模型估计。

## 核心概念

凹口噪声法在目标频率两侧留下频谱空隙，改变空隙宽度并测量目标的检测阈值，再依据模型推断滤波器形状。估计受到离频听取、滤波器非对称性及外中耳传递等假设影响。[Glasberg & Moore, 1990](#ref-glasberg-1990)

因此，行为估计出的滤波器不能未经说明就等同于某条基底膜调谐曲线。

## 等效矩形带宽

ERB 把滤波器替换为峰值相同、面积相同的矩形，便于比较带宽。常用经验式为：

$$
\mathrm{ERB}(f)=24.7\left(4.37\frac{f}{1000}+1\right)
$$

- $f$：中心频率，单位 Hz。
- $\mathrm{ERB}(f)$：等效矩形带宽，单位 Hz。
- 24.7 与 4.37：经验拟合常数，不能当作普遍的生理常量。

例如 $f=1000$ Hz 时，该式给出约 133 Hz。这只是经验估计，不等于任意个体、声级或实验条件下的实测带宽。公式的原始使用条件需结合全文审阅。[Glasberg & Moore, 1990](#ref-glasberg-1990)

## 经典实验入口

Patterson 的噪声刺激研究是这一领域的经典阅读入口；当前仅核验该文书目，具体实验设置应阅读原文。[Patterson, 1976](#ref-patterson-1976)

同时掩蔽与非同时掩蔽的结果不宜直接混合解释，声级也应明确报告。[Oxenham & Simonson, 2006](#ref-oxenham-2006)

## 阅读组内论文时

- 实验测的是检测阈值，还是识别正确率？
- 目标频率、噪声谱密度和呈现声级是什么？
- 凹口对称吗？允许离频听取吗？
- 报告的是 ERB、某个衰减点的带宽，还是完整滤波形状？

## 后续更新关注点

按实验范式、声级和受试者分组整理新证据，避免只保留一个脱离条件的带宽数值。
