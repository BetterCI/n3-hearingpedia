---
title: "谐波性"
english: "Harmonicity"
slug: "harmonicity"
summary: "解释谐波关系及其在安静与竞争语音中的作用。"
categories: ["speech"]
tags: ["Harmonicity","组内文献"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"fundamental-frequency","relation":"prerequisite"},{"slug":"speech-intelligibility","relation":"prerequisite"},{"slug":"pitch-perception","relation":"related"},{"slug":"mandarin-lexical-tone","relation":"related"}]
references: ["shi-harmonicity-2025"]
order: 12
---

## 一句话理解

谐波性描述声音中的频率分量是否接近同一基频的整数倍。它连接声源的周期性、感知组织及语音处理，但不是语音可懂度的同义词。

## 一个可以操作的概念

理想谐波复合音可写成：

$$
x(t)=\sum_{n=1}^{N}A_n\cos(2\pi nF_0t+\phi_n).
$$

$A_n$ 为幅度，$\phi_n$ 为相位，$F_0$ 单位为 Hz。若将频率改为 $f_n=nF_0+\delta_n$，不相同的偏移 $\delta_n$ 可破坏整数倍关系。这里仅展示一种教学操纵；具体论文如何构建非谐波语音，需要按其方法核对。

所有分量整体移动、改变谐波相位、改变幅度谱和扰动谐波间距，是不同操作。不能仅凭“非谐波化”这个名称就认为实验只改变了一个线索。

## 研究为什么关注它

共同频率关系可能有助于把分量组织为同一个声音，也可能改变周期性和音高线索。要判断识别改善来自哪种机制，需要控制时频包络、响度、目标与干扰的关系，并选择合适的感知任务。

## 共同论文的证据

Shi 等分别研究正常听力、模拟人工耳蜗和真实人工耳蜗条件下的普通话感知，考察安静和竞争语音情境中的谐波性作用。摘要报告的效果随听者条件和情境变化，不能把三个群体合并成一个“人工耳蜗实验”。[Shi 等，2025](#ref-shi-harmonicity-2025)

该研究为谐波性与普通话语音感知的联系提供线索；它并不单独证明所有优势都来自声流分离，也不意味着增强谐波性必然提高每位用户的成绩。本词条目前据摘要与可见引言整理，刺激构建和统计细节仍待全文审阅。

## 读论文与设计实验

先列出哪些量改变、哪些量保持：分量频率、平均能量、局部包络、基频轮廓和竞争声是否一致。再分别报告安静正确率与噪声条件的阈值，避免在不同指标之间直接比较效应大小。后续将补充谐波可分辨性、非谐波化实现及对照刺激示例。
