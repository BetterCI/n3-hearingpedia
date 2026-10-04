---
title: 语音可懂度
english: Speech Intelligibility
slug: speech-intelligibility
summary: 在明确材料、听者和任务的条件下，测量语音被正确理解的程度。
categories: [speech, audiology]
tags: [word-recognition, srt, speech-in-noise]
aliases: [语音清晰度, 语音识别率, SRT, speech reception threshold, 语音接收阈值, 正确率]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
related:
  - { slug: masking, relation: prerequisite }
  - { slug: temporal-envelope, relation: mechanism }
  - { slug: vocoder, relation: method }
  - { slug: cochlear-implant, relation: application }
references: [plomp-1979, shannon-1995, smith-2002]
order: 7
---

## 一句话理解

语音可懂度是任务中的测量结果：一定条件下，听者能正确识别多少语音内容。

## 直觉

同一段声音，回答“有没有声音”“是什么词”“复述整句话”会得到不同指标。报告“可懂度提高”时，先追问：谁听、听什么、怎样评分？

可懂度与声音自然程度、主观偏好和聆听努力应分别测量，不能用一个百分比替代所有体验。

## 正确率的定义

$$
P_{\mathrm{correct}}=\frac{N_{\mathrm{correct}}}{N_{\mathrm{scored}}}\times100\%
$$

- $N_{\mathrm{correct}}$：正确评分单元的数量。
- $N_{\mathrm{scored}}$：全部评分单元的数量。
- $P_{\mathrm{correct}}$：正确率，单位 %。

评分单元可以是词、关键词或句子，但必须声明。开放式回答与固定选项选择的机会水平也不同。

## 从固定条件到阈值

固定信噪比下可以测正确率；适应性程序则可估计达到规定正确率所需的信噪比。在噪声中报告 SRT 时，应说明目标正确率、调整规则和材料。

Plomp 与 Mimpen 的句子 SRT 研究强调测试可靠性，提供了经典方法入口；不能把该材料的结果当作所有语言测试的统一标准。[Plomp & Mimpen, 1979](#ref-plomp-1979)

## 经典研究怎样读

Shannon 等的包络研究提供了观察受限线索下语音识别的入口。[Shannon et al., 1995](#ref-shannon-1995)

阅读听觉嵌合声音实验时，可以比较包络与精细结构来自不同声音时的识别任务，同时留意分频带数量和材料范围。[Smith et al., 2002](#ref-smith-2002)

这些实验展示了特定条件下的线索作用；不能只摘取一个识别率，省略刺激和听者条件。

## 阅读组内论文时

整理材料语言、说话人、噪声类型、呈现声级、听者特征、训练、列表分配和评分单元。跨研究比较时，优先比较实验条件，再比较数值。

## 后续更新关注点

为新论文建立“处理方法—材料—听者—任务—指标”记录，避免把模型指标、主观评价和行为正确率混为同一证据。
