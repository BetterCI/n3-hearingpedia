---
title: "普通话词汇声调"
english: "Mandarin lexical tone"
slug: "mandarin-lexical-tone"
summary: "解释基频轮廓、时长和幅度等声调识别线索。"
categories: ["speech","psychoacoustics"]
tags: ["Mandarin lexical tone"]
aliases: ["普通话声调","词汇声调","DiTone"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["wang-ditone-2022","zhou-f0intfs-2023","kong-tones-2006"]
order: 19
knowledge_area: "perception"
kind: "linguistic"
key_facts: [{"label":"语言功能","value":"参与词汇意义区分"},{"label":"主要线索","value":"F₀ 高度、轮廓与时序"},{"label":"辅助线索","value":"时长、强度与发声方式"}]
---

**普通话词汇声调**（Mandarin lexical tone）是参与词汇意义区分的声调系统，其感知涉及[基频](../fundamental-frequency/)高度、变化轮廓和时间组织，也可利用时长、强度及发声方式。孤立音节和连续语流的轨迹不同，变调与协同发音需要按语境理解。[3](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition")

## 定义与分类

声调是语言类别，[基频](../fundamental-frequency/)是声学量，[音高](../pitch-perception/)是知觉属性。普通话通常区分四个主要词汇声调，轻声的实现又与语境相关；受控测试可以只取其中部分类别。DiTone 原研究的 1、2、4 类别设计不能称作覆盖全部四声的通用测试。

### 声调类别与轮廓的区别

教材常以高平、上升、低或降升、下降描述四个基本声调。实际轮廓受语境、相邻声调、说话人和语速影响，第三声尤其不能机械理解为每次都完整“先降后升”。声调类别属于语言层面，测出的 $F_0(t)$ 曲线属于刺激层面。

相对基频变化可用教学尺度表示：

$$
q(t)=12\log_2\left(\frac{F_0(t)}{F_{\mathrm{ref}}}\right).
$$

$q(t)$ 单位为半音，$F_{\mathrm{ref}}$ 是明确指定的正参考频率。只有可靠的有声帧才适合计算；参考频率不同会改变纵轴零点。

## 原理与表征

### 为什么不能只看正确率

如果某些声调的基频、幅度和时长一起变化，听者可能利用多个线索。实验中“答对了声调”并不自动说明其基频编码良好。把线索分别操纵，可以进一步检验听者依赖什么信息。

### 声调轨迹与语境

普通话声调的感知涉及基频高度、变化方向、范围与时间位置。持续时间、强度和发声方式也可提供线索。连续语流中存在协同发音与变调，孤立音节的标准示意不能直接替代所有语境中的实际轨迹。

对音节内时间 $t$，可用归一化时间 $u=t/T$ 比较轨迹形状，并用半音尺度表示相对高度。这样有助于区分“轮廓不同”和“时长不同”，但时间归一化会移除原有时长信息，不能据此宣布时长对感知无关。

### 调制与频谱分别保留什么

低阶谐波的位置可提示基频；较宽频带中的谐波相互作用可提供包络周期性；时长和能量分布也可能提示类别。Kong 与 Zeng 比较不同形式的时间和频谱信息，说明声调线索应依据具体信号处理理解。[3](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition")

噪声[声码器](../vocoder/)可能削弱精细频谱与部分周期性，但结果还依赖通道数、包络低通和载波。不能把声码器声调识别简单当作真实[人工耳蜗](../cochlear-implant/)表现，或把一次低分解释为“没有任何基频信息”。

### 混淆矩阵比总正确率更有信息

两组听者可能有相同正确率，却混淆不同类别。逐类矩阵可以显示平调与升调、不同高度或轮廓类别的混淆；解释时应保证试次数、说话人和评分规则一致。对某种混淆的声学解释，应回到刺激实际的基频、时长和能量，而不是仅凭类别名称推断。

## 测量与研究方法

### DiTone 提供的方法入口

Wang 等使用双音节词语料，并独立操纵基频与响度轮廓，研究人工耳蜗用户的普通话声调识别。DiTone 的相关材料以第一、第二和第四声为目标；不能把该任务写成完整覆盖四声的统一测试。[1](#ref-wang-ditone-2022 "Cochlear-implant Mandarin tone recognition with a disyllabic word corpus")

F0inTFS 论文也利用这一类声调任务评价周期性增强。2023 年行为验证属于正常听力声码器模拟，应与真实植入者的 DiTone 结果分开报告。[2](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

### 如何设计清晰的比较

说明音节位置、语料、说话人、词汇熟悉度、基频与响度操纵，以及受试者群体。除总正确率外，检查声调之间的混淆模式；若不同条件的响度或时长不一致，应讨论这些替代线索。

## 应用与解释边界

### 解释边界

声调识别、音高辨别和连续基频跟踪是不同任务。后续增加四声语境变化与线索权重研究，按材料与人群区分结论，避免把有限语料的优势直接推广到自然对话。

### DiTone 的实验用途与限制

DiTone 通过控制基频轮廓与响度，研究听者如何使用声调相关线索。原研究的目标类别包括声调 1、2、4，不能写成覆盖四个普通话声调的完整通用测试。其设计适合检验线索变化，不等于完整日常语言能力测量。[1](#ref-wang-ditone-2022 "Cochlear-implant Mandarin tone recognition with a disyllabic word corpus")

如果只改变合成轨迹而未平衡响度或时长，听者可能使用辅助线索。反过来，过度消除所有自然相关线索也可能使任务偏离真实语音。研究应说明自己在检验受控机制还是实际交流表现。

### 后续研究的证据链

先验证合成刺激的轨迹和辅助线索，再测试受控辨别或识别，最后扩展到多说话人、噪声和连续语流。F0inTFS 的声码器声调实验是周期性增强的机制线索，真实植入者验证、训练与更广材料仍是不同阶段。[2](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

## 分析示例

### 解释示例：声调正确不等于仅靠 F0

一组刺激中某类别同时具有较长时长、较强能量和特定基频轨迹，听者识别正确可能利用其中任一或多个线索。将基频变平后仍保留部分成绩，并不证明基频无关；它说明剩余线索还可支持任务。

可分别操纵基频、时长和响度，观察类别反应怎样改变，再与自然材料比较。完全受控刺激有助于机制识别，自然材料有助于外推，两者回答不同问题。[3](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition")

对于人工耳蜗策略，宜按类别报告混淆并检查不同说话人的泛化。只在训练过的单个说话人上改善，可能包含材料学习；若扩展到多说话人或噪声仍保持，才形成更广的使用证据。

## 研究沿革

2006 年时间与频谱线索研究探讨受控信号中声调识别。2022 年 DiTone 工作通过基频和响度轮廓操纵研究线索利用，2023 年 F0inTFS 在声学模拟中评价增强周期性。各路线从材料控制到技术评价，需分别说明真实植入者或模拟听者。[3](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition") [1](#ref-wang-ditone-2022 "Cochlear-implant Mandarin tone recognition with a disyllabic word corpus") [2](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")
