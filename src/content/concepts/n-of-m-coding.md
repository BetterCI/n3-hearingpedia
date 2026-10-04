---
title: "n-of-m 编码策略"
english: "n-of-m coding strategy"
slug: "n-of-m-coding"
summary: "解释分析频带、谱峰选择、刺激通道及 ACE 实现。"
categories: ["cochlear-implants"]
tags: ["n-of-m coding strategy","组内文献"]
aliases: ["谱峰选择","maxima","ACE","电动态范围","EDR"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"cochlear-implant","relation":"prerequisite"},{"slug":"temporal-envelope","relation":"prerequisite"},{"slug":"channel-interaction","relation":"related"},{"slug":"temporal-limits-encoder","relation":"related"},{"slug":"f0-in-tfs","relation":"related"}]
references: ["mo-maxima-2023","meng-get-2023","zeng-2008"]
order: 22
---

## 一句话理解

n-of-m 编码策略先在 $m$ 个分析通道中提取信息，再在每个选择时刻挑出 $n$ 个较强通道安排刺激。ACE 是相关的一种具体实现，不能作为所有 n-of-m 策略的同义词。

## 分析通道、选择通道和电极

设第 $k$ 帧各通道的选择量为 $E_i[k]$，概念上的选择集合为：

$$
\mathcal{S}[k]=\operatorname{Top}_n\{E_1[k],\ldots,E_m[k]\}.
$$

$\operatorname{Top}_n$ 返回较大的 $n$ 项对应的索引，不是返回一个新的频谱。随后还需要幅度压缩、电极映射和脉冲安排。本式只说明选择原则；滤波、平滑、选择量及刺激顺序由具体实现决定。[Zeng 等，2008](#ref-zeng-2008)

$m$ 个频带不一定对应同样多的独立感知维度；$n$ 也不等于设备安装的电极总数。改变 $n$ 会同时改变保留的谱信息和刺激拥挤程度。

## 电动态范围是什么

电动态范围（EDR）描述与刺激阈水平及上部舒适水平有关的可用电刺激范围。其单位、设备编码量以及从声学输入到电刺激的映射必须说明。它不是声学 dB SPL 动态范围，也不能把一个设备的电流差值直接用于另一个设备。

## 共同论文中的参数研究

Mo 等在实际人工耳蜗条件下研究谱峰数量与电动态范围对噪声中语音表现的影响。结果提示二者都是需要明确报告的实验参数；某个样本和配置下较好的数量，不是全体用户统一的调机推荐。[Mo 等，2023](#ref-mo-maxima-2023)

GET 声码器将编码与刺激序列的特征纳入声学模拟，使策略比较尽可能遵循相应编码步骤。但模拟保留了选择规则，也不意味着已经复制真实电听觉。[Meng 等，2023](#ref-meng-get-2023)

## 阅读与后续更新

记录 $m,n$、频带边界、每通道脉冲率、压缩规则、刺激顺序和个体映射。比较策略时说明哪些步骤相同、哪些改变。后续补充 ACE 与其他策略的实现差异，参数研究继续按设备、任务和样本限定结论。
