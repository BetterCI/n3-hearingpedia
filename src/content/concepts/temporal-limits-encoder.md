---
title: "时间限度编码器"
english: "Temporal Limits Encoder"
slug: "temporal-limits-encoder"
summary: "解释将频带时间信息转换到电听觉时间音高范围的策略。"
categories: ["cochlear-implants"]
tags: ["TLE","组内文献"]
aliases: ["TLE"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"temporal-fine-structure","relation":"prerequisite"},{"slug":"pitch-perception","relation":"prerequisite"},{"slug":"n-of-m-coding","relation":"prerequisite"},{"slug":"interaural-time-difference","relation":"related"},{"slug":"amplitude-modulation","relation":"related"}]
references: ["kan-tle-2021","zhou-tle-2022","wan-itd-2020"]
order: 23
---

## 一句话理解

时间限度编码器（TLE，中文暂用此译名）尝试把频带中的时间信息转换到电听觉可利用的时间变化范围，以探索音高及双耳时间线索的编码。

## 为什么需要转换

在较高频带中，快速振荡未必能够被电刺激及听者充分利用。只提取慢包络，又可能丢失部分周期性结构。TLE 的思路是对频带输出进行频率转换，使部分时间变化降低，同时保留相关信息；它并非把所有频率都直接换成同一个基频。

## 一个机制入口

相关机制论文用频带下边界 $f_{\mathrm{low}}$ 与目标下限 $f_{\mathrm{lim}}$ 决定转换频率：

$$
f_m=f_{\mathrm{low}}-f_{\mathrm{lim}}.
$$

频带信号与 $\cos(2\pi f_mt)$ 相乘会产生和、差频分量；配合滤波可选择较低的分量。所有频率单位为 Hz。本式说明混频的核心关系，完整策略还涉及带限、后续变换及刺激映射，不能把这一行公式当作完整实现。[Kan 与 Meng，2021](#ref-kan-tle-2021)

这里的机制文献是相关背景论文，并非 Zhou 与 Meng 的共同署名论文；共同论文用于进一步连接感知验证。

## 不同任务的证据

2022 年共同论文用真实人工耳蜗受试者的音高辨别与排序考察 TLE。效果与参考频率及任务有关，参数变化不能解释为在所有情境中均有一致收益。[Zhou 等，2022](#ref-zhou-tle-2022)

2020 年双耳时间差论文使用声码器模拟。它与真实植入者的音高研究对象及指标不同，应分别记录。[Wan 等，2020](#ref-wan-itd-2020)

## 边界与更新重点

转换后的刺激应检查频谱、包络、响度与两耳时序；两耳保持某种相位关系，不等于所有声学时间差原封不动保留。后续核验不同版本的频带、目标下限、刺激安排及代码。参数首先是研究设置，不是通用临床配置。
