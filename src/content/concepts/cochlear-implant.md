---
title: 人工耳蜗
english: Cochlear Implant
slug: cochlear-implant
summary: 将声音处理后的信息编码为电刺激，连接系统设计与听觉表现。
categories: [cochlear-implants]
tags: [electric-hearing, speech-processor, electrode-array, cis]
aliases: [CI, cochlear implants, 电听觉, 耳蜗植入, CIS, 人工耳蜗系统]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: n-of-m-coding, relation: related }
  - { slug: temporal-limits-encoder, relation: related }
  - { slug: cochlea, relation: prerequisite }
  - { slug: tonotopy, relation: prerequisite }
  - { slug: temporal-envelope, relation: mechanism }
  - { slug: vocoder, relation: method }
  - { slug: speech-intelligibility, relation: method }
references: [zeng-2008, wilson-1991]
order: 8
---

## 一句话理解

人工耳蜗系统将声音中的信息转为电刺激，通过电极与听觉神经系统连接，为听者提供听觉输入。

## 直觉与系统框图

**麦克风 → 声音处理器 → 传输链路 → 接收／刺激器 → 电极 → 听觉神经系统**

处理器决定提取和编码哪些声音信息；刺激器与电极负责实施电刺激。系统框图是理解论文的起点，不能单独解释最终感知表现。[Zeng et al., 2008](#ref-zeng-2008)

## 核心研究问题

阅读系统研究时，可以分开考虑声音表征、刺激方式、频率分配与评价任务。把“通道”理解为算法中的频带、电极接触点或功能上可分辨的信息来源时，需要明确具体含义。

## 一个简单的电荷定义

对于矩形脉冲的一相：

$$
Q_{\mathrm{phase}}=I\,\tau
$$

- $I$：这一相的电流幅值，单位 A。
- $\tau$：这一相的持续时间，单位 s。
- $Q_{\mathrm{phase}}$：每相电荷量，单位 C。

这是量的定义，不是刺激设置建议。具体研究需报告波形、各相参数、相间间隔与电极配置；不能只用每相电荷量概括刺激。

## 经典编码入口

Wilson 等的早期研究比较了连续交错采样（CIS）与压缩模拟策略，CIS 使用非重叠顺序呈现的短脉冲。引用这一结果时，应保留早期研究的受试者和策略范围。[Wilson et al., 1991](#ref-wilson-1991)

## 声学模拟的边界

声码器便于操纵声学线索，但没有直接重建实际电极—神经接口。将模拟结果与植入者表现比较时，应分别交代两类实验的输入、听者和研究任务。[Zeng et al., 2008](#ref-zeng-2008)

## 阅读组内论文时

1. 研究改变的是处理算法还是刺激参数？
2. 分析通道数、有效电极数与刺激率怎样定义？
3. 频率分配和刺激位置怎样报告？
4. 评价使用何种语音材料与任务？是否考虑训练？

## 后续更新关注点

逐步增加电刺激、ACE 和通道相互作用等独立词条。涉及特定设备的新结论，应由成员结合对应文献审阅后发布。
