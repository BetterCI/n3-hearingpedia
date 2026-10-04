---
title: 声码器
english: Vocoder
slug: vocoder
summary: 拆分、提取并重新合成声音，用于研究被保留线索的作用。
categories: [signal-processing, cochlear-implants]
tags: [noise-vocoder, sine-vocoder, acoustic-simulation]
aliases: [噪声声码器, 正弦声码器, noise vocoder, sine vocoder, vocoding]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: temporal-envelope, relation: prerequisite }
  - { slug: tonotopy, relation: prerequisite }
  - { slug: speech-intelligibility, relation: method }
  - { slug: cochlear-implant, relation: application }
references: [shannon-1995, dorman-1997]
order: 6
---

## 一句话理解

听觉研究中的声码器通过分析与重合成控制声学线索，帮助回答“哪些信息支持某项感知任务”。

## 直觉

先把语音分成几条频带，各自提取幅度变化，再用这些变化控制新的载波，最后合成输出。得到的声音与原声不同，但仍可保留一部分任务相关信息。

## 核心处理链

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

公式只表示共同流程；具体实现必须另列滤波、缩放和载波生成参数。频带包络调制噪声是经典研究采用的一种构建方式。[Shannon et al., 1995](#ref-shannon-1995)

## 一张复现参数清单

| 模块 | 必须说明的内容 |
|---|---|
| 分析 | 频率范围、通道边界、滤波类型与阶数 |
| 包络 | Hilbert 或整流法、平滑及截止频率 |
| 载波 | 噪声或正弦、随机种子、载频或频带 |
| 合成 | 滤波、各通道增益、整体归一化 |
| 评价 | 材料、听者、训练、声级、任务与评分 |

## 与人工耳蜗的连接

改变分析频带与合成载波的对应关系，可以研究频率—位置偏移的声学模拟。Dorman 等的研究提供了这一实验方向的经典入口。[Dorman et al., 1997](#ref-dorman-1997)

声学模拟的结果不应直接当作实际电刺激结果；两者的受试者、输入方式和研究范围必须分别说明。

## 阅读组内论文时

先画出处理链，再列出被操纵与被固定的参数。比较通道数时，检查其他处理参数是否同时变化。

## 后续更新关注点

建立声码器参数表和方法关联，之后再加入课题组特色声码器词条；每种方法保留其定义、实现和适用任务。
