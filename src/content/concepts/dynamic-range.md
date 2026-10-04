---
title: "动态范围"
english: "Dynamic range"
slug: "dynamic-range"
summary: "系统、信号或听者可处理水平的上下界之差；声学、听觉与电刺激的定义和单位须分别注明。"
categories: ["acoustics","hearing-aids","cochlear-implants"]
tags: ["dynamic-range"]
aliases: ["auditory dynamic range","electrical dynamic range","听觉动态范围","电动态范围"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["moore-loudness-2014","keidser-nalnl2-2011","zeng-2008","mo-maxima-2023","liu-ci-range-2026"]
batch: 3
order: 32
literature_checked_at: "2026-10-04"
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"定义前提","value":"指定对象、下界与上界"},{"label":"声学常见单位","value":"同一标度的 dB 差值"},{"label":"电刺激要求","value":"设备标度、脉宽、速率与电极"}]
---

**动态范围**（dynamic range）表示一个信号、设备或感知系统可用水平的上下界之差。听觉研究至少需要区分声学设备的动态范围、听者的可听至舒适范围，以及[人工耳蜗](../cochlear-implant/)的电刺激动态范围。它们描述不同对象，边界和单位必须明确，不能互相替换。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

## 定义与分类

### 信号与设备动态范围

设备范围常指噪声底以上能够表示或传输、且低于规定失真或饱和上界的水平跨度。数字信号的峰值相对满刻度可用 dBFS 描述，但其数值并不直接给出耳内声压。若写“动态范围 90 dB”，还需说明测量带宽、噪声定义、加权以及最大值的失真判据。

### 听觉动态范围

声学听觉范围常用可听阈值到不舒适水平或其他指定上界之间的差来描述。这些上下界取决于频率、时长和方法，舒适上界也不是损伤安全上界。阈值、最舒适水平及不舒适水平须采用同一参考标度才能作差；dB HL 与 dB SPL 的原始数值不能直接相减。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

### 电刺激动态范围

电范围通常联系阈值水平与最高舒适或其他临床映射上界，记号可能为 T、C 或 M，具体含义因设备体系而异。电流级有时采用设备专用标度；数值跨度不能脱离脉宽、脉冲速率、刺激电极和配置解释。更大的数值范围也不必然表示更多独立可辨知觉级别。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

## 原理与映射

声学输入变化范围通常比某些受损听者的可用范围更宽。[助听器](../hearing-aid/)可通过压缩改变输入—输出关系；人工耳蜗处理器则把声音特征映射为设备允许的电刺激参数。这些映射需要兼顾可听性、[响度](../loudness/)增长、最大输出及时域结构。[2](#ref-keidser-nalnl2-2011 "The NAL-NL2 Prescription Procedure")[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

在两个声级端点之间，可用教学式描述压缩比：

$$
\mathrm{CR}=\frac{L_{\mathrm{in},2}-L_{\mathrm{in},1}}{L_{\mathrm{out},2}-L_{\mathrm{out},1}}
$$

输入和输出均采用各自一致的声级标度，差值以 dB 表示，压缩比无量纲。若输入增加 20 dB 而输出增加 10 dB，该区段为 2:1。真实装置的拐点、攻击与释放时间、频带及输出限制会改变瞬态响应，不能仅凭这一个斜率重建实际算法。

电映射中的阈值和上界也不是神经活动的完整表征。即使两个电极电范围相近，其[通道相互作用](../channel-interaction/)、神经状态或刺激位置也可能不同，因此范围相同不能证明编码信息相同。

## 测量方法

设备测量应注明输入信号、输出位置及饱和定义；听觉范围测量应说明行为阈值规则和上界判断说明。重复测量还需考虑顺序、适应和听者对“舒适”的理解。不同频率或电极应保留单独数据，再讨论聚合值。

电生理阈值可以提供关于神经响应的辅助信息，但并不是行为阈值和舒适上界的直接替代。[听觉脑干反应](../auditory-brainstem-response/)与电刺激遥测观察不同响应环节，预测映射参数需要独立验证。相关性较高不等于个体误差已足够小，也不保证最终语音表现。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

## 应用与局限

动态范围有助于设计放大、压缩和电映射，但不能单独评价自然度、舒适度或识别能力。[时域包络](../temporal-envelope/)的压缩变化、跨通道的响度合并与输入噪声可能共同影响结果。对[噪声下语音识别](../speech-intelligibility/)的判断应另有行为证据。既有真实人工耳蜗研究将电范围与谱峰数量一起操纵，提示解释参数效果必须保留具体设备和任务条件。[4](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy")

## 分析示例

若程序 A 与 B 的电流级上界相同而阈值级不同，数值范围可能不同；但比较前还需确认两程序是否使用相同脉宽、速率和电流级换算。若这些条件变化，不能只用上界减下界判断知觉范围。再做策略比较时，应记录响度匹配和实际语音输入分布。

在助听器中，两条输入—输出曲线可能中等输入输出相同、低输入增益不同。单一中等声级的验证不能证明弱声可听性相同；需要在多个输入水平检查目标与实际输出。

## 研究沿革与近期进展

动态范围研究跨越电声工程、心理声学和电刺激映射，近期也引入参数预测。Liu 等 2026 年论文题名提出联合神经反应遥测与电诱发脑干反应阈值预测人工耳蜗动态范围参数。本次仅核对到正式书目，日期也只有月份精度，未取得摘要或全文。因此这里只作为研究方向入口，不报告其样本、预测精度、优势或临床有效性。[5](#ref-liu-ci-range-2026 "A dual-data-driven approach for predicting cochlear implant dynamic range parameters using neural response telemetry and electrically evoked auditory brainstem response thresholds")
