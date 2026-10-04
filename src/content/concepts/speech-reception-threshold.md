---
title: "语音接收阈"
english: "Speech reception threshold"
slug: "speech-reception-threshold"
summary: "介绍达到规定识别正确率时所需的测量条件、阈值和适应程序。"
categories: ["audiology"]
tags: ["SRT","组内文献"]
aliases: ["SRT","语音接收阈值","speech recognition threshold"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"speech-intelligibility","relation":"prerequisite"},{"slug":"masking","relation":"prerequisite"},{"slug":"zodiac-in-noise","relation":"related"}]
references: ["zhou-zin-2024","kong-atomic-2025","plomp-1979"]
order: 16
---

## 一句话理解

语音接收阈（SRT）是在规定材料和评分规则下，达到目标识别水平所需的刺激条件。许多任务以 50% 正确率为目标，但阈值的调整变量和单位必须随任务说明。

## 它是条件，不是一个固定单位

在噪声中常调整信噪比，报告 dB SNR；在安静中可调整呈现声级；稀疏语音实验还可能调整原子率。仅写“SRT 提高了 2”无法判断是什么意思。

可用以下通用表达理解：

$$
P(\mathrm{correct}\mid x^\ast)=p_{\mathrm{target}}.
$$

$x^\ast$ 是达到目标正确率 $p_{\mathrm{target}}$ 的条件。本式不指定自变量是 SNR、声级或原子率，也不保证所有实验采用相同的心理测量函数。封闭集合任务还需要考虑猜测水平。

## 适应程序怎样寻找阈值

适应程序按受试者反应改变下一次刺激条件，在阈值附近集中取样。步长、升降规则、起点、终止规则及反转点平均方式都会影响估计。不同适应规则对应的目标水平可能不同，不能看到“自适应”就默认收敛于 50%。

材料熟悉程度、关键词或整句计分、掩蔽声类型、训练与列表效应也影响结果。经典句子 SRT 文献是可靠性问题的入口，并非所有语言测试的统一规范。[Plomp 与 Mimpen，1979](#ref-plomp-1979)

## 两篇共同论文如何使用 SRT

生肖噪声测试采用生肖材料，在噪声中用适应程序估计识别阈值，其 SRT 与噪声和测试版本相联系。[Zhou 等，2024](#ref-zhou-zin-2024)

原子语音模型论文则以 **原子率** 为调整变量寻找识别阈值；其单位不是 dB SNR。原子率越低仍能达到目标，表示在该任务中可利用更稀疏的表示。[Kong 等，2025](#ref-kong-atomic-2025)

## 报告与边界

至少报告材料、耳别、掩蔽声、目标正确率、适应规则、变量单位和不确定性。SNR 阈值更低通常表示该测试中表现更好，但不能把不同材料或版本的绝对值直接比较。后续将补充心理测量函数、猜测校正与阈值重测误差。
