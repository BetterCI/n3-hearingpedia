---
title: 耳蜗
english: Cochlea
slug: cochlea
summary: 将声音引起的机械运动连接到频率分析与神经信号。
categories: [ear-cochlea]
tags: [cochlear-mechanics, hair-cells, frequency-analysis]
aliases: [耳蜗力学, 内耳, cochlear mechanics]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: pure-tone-audiometry, relation: related }
  - { slug: tonotopy, relation: mechanism }
  - { slug: auditory-filter, relation: mechanism }
  - { slug: cochlear-implant, relation: application }
references: [robles-2001, zeng-2008]
order: 1
---

## 一句话理解

耳蜗把声音引起的机械运动转化为供神经系统使用的信息，并在这一过程中进行频率分析。

## 直觉

可以先把耳蜗想成一条卷起来的分析通道。不同频率的声音在通道的不同位置产生较强响应；理解时先把它“展开”，比只看螺旋外形更有帮助。

这个比喻只描述位置与响应的关系。耳蜗的响应还随声级和生理状态变化，不能用一组固定线性滤波器概括全部过程。[Robles & Ruggero, 2001](#ref-robles-2001)

## 核心机制

中耳镫骨的运动驱动耳蜗内的机械响应。基底膜上的行波沿基底向顶端传播，不同频率对应不同的响应峰值位置。毛细胞将机械运动与受体电位联系起来，信息随后进入听神经。[Robles & Ruggero, 2001](#ref-robles-2001)

阅读论文时，先分清作者测量的是基底膜运动、毛细胞响应、神经活动，还是行为表现。这些测量层次彼此相关，却不是同一个量。

## 用什么量描述

初步比较输入与位移响应时，可以定义：

$$
G(f,L)=\frac{|X_{\mathrm{BM}}(f,L)|}{|P_{\mathrm{in}}(f,L)|}
$$

- $f$：刺激频率，单位 Hz。
- $L$：输入声级，必须注明使用的标度。
- $X_{\mathrm{BM}}$：指定位置的基底膜位移幅值。
- $P_{\mathrm{in}}$：注明测量位置的输入声压幅值。
- $G$：位移对声压的响应比，单位可写为 m/Pa。

这是帮助读图的量定义，不是完整耳蜗模型。使用时需要固定记录位置和测量条件。

## 阅读组内论文时

1. 测量位置如何报告：物理距离、归一化位置，还是特征频率？
2. 输入声级和测量指标是什么？
3. 结论来自哪种物种、哪种实验状态？
4. 作者如何连接机械测量与感知结果？

## 工程连接与边界

人工耳蜗通过电刺激提供听觉输入，不能把它简单理解为“恢复原来的耳蜗机械过程”。阅读系统论文时，需要分别理解声音处理和电极—神经接口。[Zeng et al., 2008](#ref-zeng-2008)

## 后续更新关注点

优先整理与组内任务相关的机械测量和模型研究，明确物种、位置和声级；由成员审阅后再补充新的机制判断。
