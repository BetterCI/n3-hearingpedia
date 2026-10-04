---
title: "双耳时间差"
english: "Interaural time difference"
slug: "interaural-time-difference"
summary: "区分波形与包络的双耳时间差，连接空间听觉任务。"
categories: ["binaural"]
tags: ["ITD","组内文献"]
aliases: ["ITD"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"temporal-envelope","relation":"prerequisite"},{"slug":"temporal-fine-structure","relation":"prerequisite"},{"slug":"binaural-integration","relation":"related"},{"slug":"binaural-intelligibility-level-difference","relation":"related"}]
references: ["wan-itd-2020","kan-tle-2021"]
order: 15
---

## 一句话理解

双耳时间差（ITD）是同一声事件到达两耳的时间差，是空间听觉的重要线索。精细结构的时间差与包络的时间差应分别描述。

## 先约定方向

令左右耳到达时间分别为 $t_L,t_R$，本词条约定：

$$
\tau=t_R-t_L.
$$

$\tau$ 单位为秒，通常也用微秒表示；正值表示左耳先到。其他论文可能采用相反符号，比较前要检查定义。对频率为 $f$ 的纯音，相位差与时间差满足 $\Delta\phi=2\pi f\tau$，但相位只有模 $2\pi$ 的信息，不能总能唯一确定时间差。

## 波形与包络不是同一个延迟

窄带声音的内部振荡和较慢包络可以分别设置双耳差异。两耳刺激有相同包络，并不意味着精细结构也相同；反相操作也不等于给宽带信号添加一个恒定时间延迟。

自由声场中的头部、耳廓和反射还会改变声音。耳机中仅操纵 ITD 的侧化任务，回答的是受控刺激的位置感觉，不应直接称为完整的现实声源定位能力。

## 人工耳蜗中的额外约束

两个处理器的时钟、脉冲时序、频带与电极匹配都会影响跨耳时间关系。将声学时间线索编码到电刺激中，并不保证听者能够利用它。TLE 的相关机制文献讨论频带转换及双侧处理对时间信息的影响。[Kan 与 Meng，2021](#ref-kan-tle-2021)

Wan 等的会议论文用声码器模拟比较 TLE 与 CIS 对 ITD 相关任务的表现。它提供策略研究的线索，证据范围限于该模拟与任务，不能写成所有双侧植入者定位改善。[Wan 等，2020](#ref-wan-itd-2020)

## 阅读和更新重点

记录差异施加在声波、包络还是脉冲层面，以及两耳是否同步、刺激是否等响。后续分别建立双耳强度差、侧化、定位和 ITD 辨别阈词条；不要把任务名称或单位相近当作测量等价。
