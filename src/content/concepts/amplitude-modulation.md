---
title: "振幅调制"
english: "Amplitude modulation"
slug: "amplitude-modulation"
summary: "解释调制频率、调制深度以及电刺激包络调制。"
categories: ["signal-processing"]
tags: ["AM","组内文献"]
aliases: ["AM"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"temporal-envelope","relation":"prerequisite"},{"slug":"pitch-perception","relation":"related"},{"slug":"mandarin-lexical-tone","relation":"related"}]
references: ["zhou-tle-2022","li-covarying-2025"]
order: 13
---

## 一句话理解

振幅调制（AM）是让信号的幅度随时间按一定规律变化。调制频率描述起伏有多快，调制深度描述起伏有多大。

## 从声学模型开始

对正弦载波，一个常见教学模型为：

$$
x(t)=A[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct).
$$

$A$ 为幅度，$m$ 为无量纲调制深度，通常取 $0\leq m\leq1$；$f_m$ 为调制频率、$f_c$ 为载波频率，单位均为 Hz。$m=0$ 时没有振幅起伏，$m=1$ 时理想包络最小值到零。频谱中可出现 $f_c-f_m$ 与 $f_c+f_m$ 的边带。

上述模型只描述一种规则信号。语音包络同时含有多个变化速率，不能简单概括为一个 $f_m$。

## 电刺激中要区分两种速率

在固定脉冲率的刺激序列中，各脉冲幅度仍可缓慢起伏。脉冲率以每秒脉冲数表示，调制频率以每秒包络周期数表示。提高其中一个不必提高另一个；二者协变也不代表知觉音高一定按相同比例改变。

声学调制深度的定义不能未经说明就搬到电流、响度或设备编码值上。比较电刺激时还要记录电流范围、脉冲宽度、电极及响度控制。

## 共同论文中的两条线索

TLE 关注把频带时间信息转换为可利用的刺激变化，其效果需要通过具体音高任务检验。[Zhou 等，2022](#ref-zhou-tle-2022)

2025 年协变振幅调制与脉冲率的研究探索组合时间线索对音高辨别的影响。本词条引用的是 **medRxiv 预印本，尚未同行评审**；结果依刺激范围和受试者条件而定，不能视为已确立的通用编码方案。后续同组版本应按同一研究线索追踪，不能重复计算为独立证据。[Li 等，2025](#ref-li-covarying-2025)

## 研究记录与后续更新

至少分别写出载波或脉冲率、调制频率、调制深度、响度匹配及辨别规则。后续补充调制检测与调制频率辨别，核对预印本正式发表后的方法与结论变化。
