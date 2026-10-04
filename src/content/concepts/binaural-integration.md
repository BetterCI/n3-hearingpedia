---
title: "双耳整合"
english: "Binaural integration"
slug: "binaural-integration"
summary: "解释两耳互补的频谱时间信息能否合并支持识别。"
categories: ["binaural"]
tags: ["Binaural integration","组内文献"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"interaural-time-difference","relation":"prerequisite"},{"slug":"speech-intelligibility","relation":"prerequisite"},{"slug":"atomic-speech-model","relation":"related"},{"slug":"binaural-intelligibility-level-difference","relation":"related"}]
references: ["kong-atomic-2025","shi-dbd-2024"]
order: 21
---

## 一句话理解

双耳整合是听觉系统把两耳提供的信息结合起来支持感知的过程。两耳同时接收声音，并不保证结合后一定表现更好。

## 从互补信息看问题

可以把不同频带或不同时刻的语音信息分配给两耳，再比较单耳、双耳和完整信息条件。若双耳优于任一单耳，说明跨耳信息具有利用价值；但这种优势仍可能包含选择较好耳等因素，需要适当对照才能支持具体机制。

教学中可写出一个描述性指标：

$$
G=A_{\mathrm{both}}-\max(A_L,A_R).
$$

$A$ 为同一任务的正确率，若以百分数记录，$G$ 的单位是百分点。$G>0$ 仅描述双耳成绩超过较好单耳；它不是整合机制的充分证明，也不适合直接与 SRT 差值混用。

## 与双耳去掩蔽的关系

双耳去掩蔽关注两耳相位或时间关系怎样帮助目标在掩蔽声中被检测或理解。互补频带合并关注分散的信息能否形成有效语音表示。两者都涉及双耳，却不应由同一个实验成绩互相替代。

## 原子语音模型的线索

ASM 将稀疏语音单元分配到两耳，考察跨耳组合是否支持识别。论文报告跨耳分配的表现具有条件和个体差异，并非所有双耳条件都优于单耳呈现。[Kong 等，2025](#ref-kong-atomic-2025)

因此应同时检查每耳的信息量、两耳的互补程度、时间对齐及总能量。否则“两耳更差”可能混入刺激变化，不能仅凭组平均值断言某一整合机制不存在。

## DBD-CI 的工程问题

DBD-CI 把更密集的分析频带交错分配到两耳，探索每耳承担较少拥挤信息、两耳共同提供较密频谱的可能性。2024 年结果来自初步声码器模拟；真实双侧植入还存在电极、听力及处理器匹配问题。[Shi 等，2024](#ref-shi-dbd-2024)

## 边界与后续更新

把两耳同步、耳间匹配、学习效应和个体差异分别记录。后续将补充双耳冗余、互补信息、较好耳效应与双耳去掩蔽的对照设计，避免仅用“双耳获益”概括不同机制。
