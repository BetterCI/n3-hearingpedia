---
title: "助听器"
english: "Hearing Aid"
slug: "hearing-aid"
summary: "通过声学输入、个体化实时信号处理与耳道输出改善可听性和交流；其效果取决于残余听觉、处方与验证、空间处理、使用场景和长期适应。"
categories: ["hearing-aids","audiology","signal-processing"]
tags: ["hearing-aid","WDRC","real-ear-measurement","directional-microphone","self-fitting","personalization"]
aliases: ["hearing aids","声学助听器","数字助听器","HA"]
status: reviewed
last_updated: "2026-10-05"
authors: ["AI 辅助重构"]
reviewer: null
reviewed_at: null
literature_checked_at: "2026-10-05"
illustration:
  src: "figures/hearing-aid-signal-chain.svg"
  alt: "助听器从麦克风输入、场景分析、多频带处理到受话器输出以及处方和验证闭环的示意图"
  caption: "助听器是受听力状态、环境和个体目标约束的实时声学处理系统；处方、输出验证与长期使用反馈构成完整验配闭环。"
knowledge_area: "technology"
kind: "technology"
key_facts:
  - {label: "核心目标", value: "改善可听性、语音交流和真实生活参与"}
  - {label: "基本链路", value: "麦克风 → 实时数字处理 → 受话器 → 耳道"}
  - {label: "验配核心", value: "处方只是起点，需要 REM、行为评价和长期反馈"}
  - {label: "主要边界", value: "不能恢复正常耳蜗的频率选择性、神经编码和全部复杂声场能力"}
  - {label: "当前前沿", value: "双耳空间处理、self-fitting、AI 个体化与真实世界闭环"}
references: ["nidcd-hearing-aids","keidser-nalnl2-2011","asha-hearing-aids-adults","fda-otc-hearing-aids","de-sousa-self-fitting-2023","knoetze-self-fitting-2024","tasnim-ml-hearingaid-2024","kuk-irrt-2026"]
batch: 3
order: 30
---

**助听器**（hearing aid, HA）是把环境声音采集后进行实时声学处理，再通过受话器把处理后的声音送入耳道的听觉辅助设备。它最主要的作用不是“把所有声音整体放大”，而是依据听力损失、输入声级、频率、方向和使用环境，对声音进行**频率相关、声级相关和场景相关的重映射**，以提高可听性、交流效率和日常参与。NIDCD 将其基本组成概括为麦克风、放大/处理电路和扬声器，并明确指出助听器可以改善听觉与言语理解，但不能把听觉恢复为正常。[1](#ref-nidcd-hearing-aids "Hearing Aids")

## 一句话理解

> **助听器不是“声音放大器”，而是一套“声学输入 + 个体化实时处理 + 耳道输出 + 临床验证 + 长期适应”的闭环系统。**

它能把更多声音送入残余可听范围，却仍依赖使用者原有的[耳蜗](../cochlea/)、听神经和中枢听觉系统完成后续编码。因此，“输出更大”不等于“有用信息更多”。

## 装置形式与基本组成

常见装置形式包括耳背式（BTE）、受话器外置式（RIC/RITE）、耳内式（ITE）、耳道式（ITC）和完全耳道式（CIC）等。装置形态会影响麦克风位置、可用功率、耳道开放程度、反馈风险、无线功能和佩戴舒适度，但**形态、价格或功能数量本身都不能直接推出最终听觉效果**。[1](#ref-nidcd-hearing-aids "Hearing Aids")

NIDCD 官方资料提供了典型 BTE、mini-BTE、ITE、ITC 和 CIC 外形图，并标注图源为 NIH/NIDCD：

![NIDCD 助听器形态图](https://www.nidcd.nih.gov/sites/default/files/Content%20Images/NIDCD-Hearing-Loss-And-Older-Adults-Figure.jpg)

*图源：NIH/NIDCD，Hearing Aids 官方页面。*

现代数字助听器的实际处理链远比“麦克风—放大器—扬声器”复杂：

![助听器信号链](/n3-hearingpedia/figures/hearing-aid-signal-chain.svg)

## 助听器真正补偿的是什么

听力损失后，最直接的问题之一是部分语音频谱成分低于听阈。频率相关增益可以把这些成分重新送入可听范围。但感音神经性听力损失常同时伴随[动态范围](../dynamic-range/)缩窄、响度增长异常、频率选择性变差以及阈上神经编码变化，因此单纯线性放大会很快遇到两个问题：弱声仍可能听不到，而强声又可能过响。

这就是现代助听器广泛采用**宽动态范围压缩（wide dynamic range compression, WDRC）**的重要原因。某一频带内，压缩比可写为：

$$
CR=rac{\Delta L_{\mathrm{in}}}{\Delta L_{\mathrm{out}}}
$$

- $\Delta L_{\mathrm{in}}$：输入声级变化；
- $\Delta L_{\mathrm{out}}$：输出声级变化；
- $CR>1$：输入范围被映射到较窄的输出范围。

但真正的压缩行为还取决于 compression threshold、attack/release time、频带划分和最大输出限制（MPO）。**助听器压缩并不等于恢复正常耳蜗的主动压缩机制。**

## 现代助听器不只有增益

### 多频带增益与压缩

不同频率和不同输入声级采用不同增益，使弱语音更可听，同时限制高声级输出。NAL-NL2 等处方体系会在语音可听性、响度与长期可接受性之间建立群体层面的目标。[2](#ref-keidser-nalnl2-2011 "The NAL-NL2 Prescription Procedure")

### 方向性与波束形成

多麦克风系统可以利用空间差异提高目标方向上的信噪比。它对固定目标/固定噪声配置尤其有效，但真实环境中的移动说话人、多噪声源和混响会显著增加难度。

### 数字降噪

数字降噪根据时频统计特征估计哪些成分更可能属于噪声并进行抑制。改善舒适度并不一定同步改善[语音可懂度](../speech-intelligibility/)；强处理还可能产生失真。

### 反馈管理

声学反馈来自受话器输出重新进入麦克风形成闭环。现代反馈抑制可以提高可用增益，但也可能在某些输入条件下产生处理伪影。

### Frequency lowering

当高频可听性难以通过常规增益恢复时，可将高频信息压缩或搬移到更低频区域。它改变的是信息位置，因此需要单独验证学习、语音收益和音质代价。

## 处方、编程、验证和有效性是四件事

### 1. 处方（prescription）

NAL-NL2、DSL 等体系根据听力图、输入声级、年龄和其他变量给出目标增益或输出。**处方是有证据支持的起点，不是每个人的最终答案。**[2](#ref-keidser-nalnl2-2011 "The NAL-NL2 Prescription Procedure")

### 2. 编程（programming）

把处方目标转换成具体设备参数，包括频带增益、压缩、MPO、方向性、降噪和程序设置。厂商“first fit”与处方目标并不必然一致。

### 3. 输出验证（verification）

真耳测量（real-ear measurement, REM）用探管麦克风测量实际佩戴后耳道中的输出，能够考虑真实耳道大小、形状和共振。ASHA 成人助听器实践资料把 REM 视为处方目标客观验证的核心方法，并强调 first fit 之后仍需验证与微调。[3](#ref-asha-hearing-aids-adults "Hearing Aids For Adults")

### 4. 有效性评价（validation）

真正的结果还应包括：
- 安静与噪声语音；
- 声音质量与舒适度；
- [聆听努力](../listening-effort/)；
- 空间听觉；
- 真实生活中的使用时长和参与；
- 长期满意度。

因此，**REM 达标 ≠ 语音一定改善 ≠ 日常交流一定最优**。这三个层级必须分别评价。

## 耳道耦合为什么重要

开放式、耳塞式和定制耳模会改变低频泄漏、反馈裕度、耳道共振和自身声音体验。open fit 往往可以减轻 occlusion effect，却同时降低低频可控增益；更密闭耦合提高低频输出能力，却可能带来堵塞感和自声不自然。

研究论文只写“aided condition”是不够的，至少应说明：
- 单耳还是双耳；
- open/closed fitting；
- 耳塞或耳模；
- 处方公式与实际 target match；
- 是否完成 REM；
- 程序、方向性与降噪状态；
- 使用经验与适应时间。

## 双耳助听并不只是“两只独立设备”

双耳听觉依赖 ITD、ILD 和耳廓谱形。方向性、独立压缩、自动增益和无线同步都可能改变这些线索，因此双耳设备有两种可能同时存在的效果：

1. **提高目标信噪比**；
2. **改变天然空间关系**。

未来的双耳助听器更像一个联合空间处理系统，而不是左右各自优化的两台设备。评价时应把 speech-in-noise 与[空间听觉](../spatial-hearing/)分开测量。

## Self-fitting、OTC 与远程服务

FDA 的 OTC hearing aid 类别面向 **18 岁及以上、自觉轻至中度听力损失**成人，并允许设备通过软件、应用或自测工具进行自定义；儿童以及重度至极重度听损不属于这一类别的目标人群。[4](#ref-fda-otc-hearing-aids "OTC Hearing Aids: What You Should Know")

2023 年随机临床试验比较特定 OTC self-fitting hearing aid 与 audiologist-fitted hearing aid，在所研究成人和随访范围内观察到具有临床意义的自验配效果；这说明“专业人员介入程度”可以有新的服务模式，但不能推广成“所有人都适合 self-fitting”。[5](#ref-de-sousa-self-fitting-2023 "Effectiveness of an Over-the-Counter Self-fitting Hearing Aid Compared With an Audiologist-Fitted Hearing Aid")

2024 年交叉临床试验进一步比较 self-adjustment 与 in-situ audiometry 两种 OTC self-fitting 路径，总体 APHAB、IOI-HA、噪声语音和 REM 结果相近，但部分满意度和日常使用维度存在差异。[6](#ref-knoetze-self-fitting-2024 "Comparing Self-Fitting Strategies for Over-the-Counter Hearing Aids")

这些结果更适合支持一种新的分层模式：

**自动初配 → 自主微调 → 远程支持 → 专业验证 → 复杂病例管理**

而不是把 self-fitting 与专业服务理解为非此即彼。

## AI 与个体化助听

机器学习已被用于偏好学习、个体化放大、主动学习、强化学习和基于真实环境反馈的参数优化。2024 年综述指出，这一方向的核心目标是突破固定处方对个体偏好和场景差异刻画不足的问题。[7](#ref-tasnim-ml-hearingaid-2024 "A Review of Machine Learning Approaches for the Personalization of Amplification in Hearing Aids")

未来可能形成这样的闭环：

**听力图 + REM + 语音表现 + 场景分类 + 使用日志 + EMA/用户偏好 → 参数更新**

但信号指标提高并不等同于植入真实设备后生活收益提高。任何 AI fitting 还必须满足：
- 低延迟；
- 低功耗；
- 输出安全；
- 稳定性；
- 可解释的参数边界；
- 不破坏重要空间和时间线索。

## 为什么“听懂”仍不足以描述助听器效果

同样的语音正确率可能需要不同程度的认知资源。2026 年 Kuk 等研究比较正常听力者和佩戴助听器的听损者，在匹配可懂度条件下仍观察到语境、记忆和努力指标提供额外信息。这类结果提醒我们：**正确率只是结果的一部分，聆听代价也应成为设备评价对象。**[8](#ref-kuk-irrt-2026 "The Intelligibility-Based Repeat-Recall Test: II. Performance of Listeners With Normal Hearing and Hearing Impairment (Aided)")

## 助听器的根本边界

助听器仍依赖残余耳蜗和听神经功能。NIDCD 明确指出，若内耳损伤过重，即使输入振动更大，也可能无法转化为有效神经信号。[1](#ref-nidcd-hearing-aids "Hearing Aids")

因此助听器并不能保证恢复：
- 正常频率选择性；
- 正常耳蜗压缩；
- 正常时域精细结构利用；
- 正常双耳同步；
- 正常 auditory object formation；
- 正常噪声下交流。

更准确的理解是：

> **助听器是在残余听觉的约束下重新分配和增强可利用信息，而不是把受损耳蜗变回正常耳蜗。**

## 当前前沿研究问题

### 1. 处方能否真正个体化？
听力图之外，是否应该加入响度、频率选择性、噪声语音、空间听觉、认知、语言和长期声景？

### 2. REM 能否预测真实世界收益？
输出匹配与日常交流之间还缺哪些中间变量？

### 3. AI 降噪如何避免“增强目标却破坏声音世界”？
SNR、语音、空间线索、音质和延迟应该如何联合优化？

### 4. 双耳助听器如何真正联合工作？
能否共享场景、目标方向和时间信息，而不是两耳独立 AGC？

### 5. Fitting 能否成为长期闭环？
是否可以用 EMA、设备日志、远程测听和真实生活结果持续调整参数？

### 6. 如何评价“听懂但很累”？
speech score、listening effort 和 participation 是否应成为同等重要终点？

### 7. Self-fitting 与专业服务如何形成分层体系？
哪些用户适合自主验配，哪些用户需要 REM、复杂诊断和长期专业管理？

### 8. 助听器能否从“补偿听力图”走向“补偿 auditory phenotype”？
未来处方是否应该直接针对个体在时间、空间、频率和认知维度上的真实缺陷？

## 与其他词条的关系

建议继续阅读：

- [听力损失](../hearing-loss/)：助听器究竟在补偿什么；
- [耳蜗](../cochlea/)：为什么单纯增加声压不能恢复所有信息；
- [动态范围](../dynamic-range/) 与 [响度](../loudness/)：压缩的感知基础；
- [语音可懂度](../speech-intelligibility/) 与 [聆听努力](../listening-effort/)：设备效果的不同层次；
- [空间听觉](../spatial-hearing/)：方向性和双耳处理的收益与代价；
- [人工耳蜗](../cochlear-implant/)：当声学放大不足时的另一种听觉接口。

## 研究沿革

助听器已经从简单线性放大器发展为多麦克风、多频带压缩、反馈管理、无线互联和场景自适应的嵌入式听觉系统。与此同时，研究重点也正在从“**有没有增益**”转向“**输出是否经过客观验证、听者能否利用、是否降低真实交流代价，以及系统能否长期个体化**”。

下一阶段最值得关注的变化，可能不是某个单独降噪算法，而是助听器从一次性验配设备逐渐演变为一个持续学习的**个人听觉接口**。
