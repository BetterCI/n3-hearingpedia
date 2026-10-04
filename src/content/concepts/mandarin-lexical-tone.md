---
title: "普通话词汇声调"
english: "Mandarin lexical tone"
slug: "mandarin-lexical-tone"
summary: "解释基频轮廓、时长和幅度等声调识别线索。"
categories: ["speech"]
tags: ["Mandarin lexical tone","组内文献"]
aliases: ["普通话声调","词汇声调","DiTone"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"fundamental-frequency","relation":"prerequisite"},{"slug":"pitch-perception","relation":"prerequisite"},{"slug":"amplitude-modulation","relation":"prerequisite"},{"slug":"confusion-matrix","relation":"related"}]
references: ["wang-ditone-2022","zhou-f0intfs-2023"]
order: 19
---

## 一句话理解

普通话词汇声调是音节中能够区别词义的声调类别。基频轮廓是重要声学线索，时长、幅度和发声特征也可能参与识别。

## 声调类别与轮廓的区别

教材常以高平、上升、低或降升、下降描述四个基本声调。实际轮廓受语境、相邻声调、说话人和语速影响，第三声尤其不能机械理解为每次都完整“先降后升”。声调类别属于语言层面，测出的 $F_0(t)$ 曲线属于刺激层面。

相对基频变化可用教学尺度表示：

$$
q(t)=12\log_2\left(\frac{F_0(t)}{F_{\mathrm{ref}}}\right).
$$

$q(t)$ 单位为半音，$F_{\mathrm{ref}}$ 是明确指定的正参考频率。只有可靠的有声帧才适合计算；参考频率不同会改变纵轴零点。

## 为什么不能只看正确率

如果某些声调的基频、幅度和时长一起变化，听者可能利用多个线索。实验中“答对了声调”并不自动说明其基频编码良好。把线索分别操纵，可以进一步检验听者依赖什么信息。

## DiTone 提供的方法入口

Wang 等使用双音节词语料，并独立操纵基频与响度轮廓，研究人工耳蜗用户的普通话声调识别。DiTone 的相关材料以第一、第二和第四声为目标；不能把该任务写成完整覆盖四声的统一测试。[Wang 等，2022](#ref-wang-ditone-2022)

F0inTFS 论文也利用这一类声调任务评价周期性增强。2023 年行为验证属于正常听力声码器模拟，应与真实植入者的 DiTone 结果分开报告。[Zhou 等，2023](#ref-zhou-f0intfs-2023)

## 如何设计清晰的比较

说明音节位置、语料、说话人、词汇熟悉度、基频与响度操纵，以及受试者群体。除总正确率外，检查声调之间的混淆模式；若不同条件的响度或时长不一致，应讨论这些替代线索。

## 边界与后续更新

声调识别、音高辨别和连续基频跟踪是不同任务。后续增加四声语境变化与线索权重研究，按材料与人群区分结论，避免把有限语料的优势直接推广到自然对话。
