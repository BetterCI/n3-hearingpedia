---
title: 频位映射关系
english: Tonotopy
slug: tonotopy
summary: 理解频率如何与耳蜗位置及神经系统中的组织关系相连。
categories: [ear-cochlea, neuroscience]
tags: [frequency-place, greenwood, cochlear-map]
aliases: [频位映射, 频率位置关系, frequency-place mapping, Greenwood]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: cochlea, relation: prerequisite }
  - { slug: auditory-filter, relation: related }
  - { slug: vocoder, relation: application }
  - { slug: cochlear-implant, relation: application }
references: [greenwood-1990, sridhar-2006]
order: 2
---

## 一句话理解

频位映射关系描述频率与空间位置之间的有序对应；耳蜗是理解这一关系的起点。

## 直觉

把展开的耳蜗看作一条带有频率坐标的轴。基底侧对应较高频率，顶端侧对应较低频率。位置与频率的关系不是“每毫米增加相同 Hz”的线性标尺。[Greenwood, 1990](#ref-greenwood-1990)

项目统一使用 **“频位映射关系”** 作为 Tonotopy 的中文名称。

## 核心概念与公式

耳蜗频率—位置函数的一种经典表达是：

$$
f(x)=A\left(10^{ax}-k\right)
$$

- $f(x)$：位置 $x$ 所对应的频率，单位 Hz。
- $x$：从顶端向基底增加的归一化位置；采用此约定时，0 为顶端，1 为基底。
- $A$：具有频率单位的尺度参数。
- $a$：决定指数变化速率的无量纲参数。
- $k$：无量纲偏移参数。

常见的人耳参数为 $A=165.4$、$a=2.1$、$k=0.88$。若文献使用毫米或从基底量起的位置，不能直接套用这些坐标与参数。[Sridhar et al., 2006](#ref-sridhar-2006)

## 为什么与实验相关

声码器或人工耳蜗研究经常需要比较“输入频带”与“刺激位置”。作为描述性的比较量，可以写：

$$
\Delta=\log_2\left(\frac{f_{\mathrm{assigned}}}{f_{\mathrm{place}}}\right)
$$

其中 $f_{\mathrm{assigned}}$ 是分配给通道的频率，$f_{\mathrm{place}}$ 是指定映射模型给出的频率。$\Delta$ 的单位是 octave；它表示频率比的对数，不直接预测感知表现。

## 阅读组内论文时

先确认位置针对的是基底膜、柯蒂器、螺旋神经节还是电极接触点。柯蒂器与螺旋神经节的空间关系不能简单视为同一条标尺。[Sridhar et al., 2006](#ref-sridhar-2006)

进一步检查：位置来自影像测量还是模型估计？使用的坐标原点和总长度是什么？研究是否控制了其他处理参数？

## 后续更新关注点

优先补充与组内研究相关的个体解剖、频率分配和映射偏移文献；分开记录模型估计、实际刺激和感知证据。
