---
title: "纯音测听"
english: "Pure-tone audiometry"
slug: "pure-tone-audiometry"
summary: "介绍听阈、频率、气导测听与自动测听流程。"
categories: ["audiology"]
tags: ["PTA","组内文献"]
aliases: ["PTA"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"cochlea","relation":"prerequisite"},{"slug":"audiometric-calibration","relation":"related"},{"slug":"zodiac-in-noise","relation":"related"}]
references: ["guo-audiometry-2021","zhou-anc-audiometry-2024","asha-audiometry-2005"]
order: 17
---

## 一句话理解

纯音测听是在规定频率、耳别和测量条件下，寻找受试者能检测到纯音的最低呈现级。它描述听阈随频率的分布，不等同于语音理解能力。

## 图上的坐标意味着什么

听力图通常以频率为横轴、听力级 dB HL 为纵轴。dB HL 使用与频率、换能器和参考条件有关的零点；它不是声压级 dB SPL，也不是“零声压”。气导经耳机或插入式耳机呈现，骨导使用不同的换能器和参考框架。

测量还取决于指令、反应可靠性、呈现节奏、阈值搜索规则以及环境噪声。2005 年 ASHA 指南提供手动测听的测量与记录框架；实际使用应核对适用的现行规范。[ASHA 指南](#ref-asha-audiometry-2005)

## PTA 的两个常见含义

本词条中的 PTA 指 pure-tone audiometry。另一些论文用 PTA 指 pure-tone average，即若干频率听阈的平均值：

$$
\mathrm{PTA}_{\mathrm{avg}}=\frac{1}{K}\sum_{i=1}^{K}H(f_i).
$$

$H(f_i)$ 是指定频率的听阈，单位 dB HL。平均值必须同时写出包含的频率和耳别，不同频率组合不能仅凭缩写视为同一指标。

## 真无线耳机自动测听的线索

Guo 等研究将真无线耳机用于自动纯音测听，包含声学与行为校准以及与参考测量的比较。因此“手机能播放纯音”只是系统的一环，不能直接推出能够准确测量听阈。[Guo 等，2021](#ref-guo-audiometry-2021)

后续 ANC 耳机研究进一步检查降噪、输出和自动测量条件。主动降噪可能改善部分条件下的背景噪声，但不能替代耳机输出校准、佩戴控制或测量验证。[Zhou 等，在线发表于 2024](#ref-zhou-anc-audiometry-2024)

## 边界与更新重点

纯音听阈不能单独说明所有听力困难，也不能代替噪声下语音测量。后续将分别解释气骨导、掩蔽和听力图记录；自动测量研究应报告设备型号、算法、环境与个体结果，而不只报告组平均误差。
