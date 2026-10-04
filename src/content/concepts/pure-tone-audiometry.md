---
title: "纯音测听"
english: "Pure-tone audiometry"
slug: "pure-tone-audiometry"
summary: "介绍听阈、频率、气导测听与自动测听流程。"
categories: ["audiology","hearing-loss"]
tags: ["PTA"]
aliases: ["PTA"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["guo-audiometry-2021","zhou-anc-audiometry-2024","asha-audiometry-2005","iso-389-1-2017","iso-8253-1-2010","swanepoel-2014"]
order: 17
knowledge_area: "measurement"
kind: "test"
key_facts: [{"label":"测量对象","value":"各频率的检测敏感度"},{"label":"主要方式","value":"气导与骨导"},{"label":"常用标度","value":"dB HL；参照条件需匹配"}]
---

**纯音测听**（pure-tone audiometry）是通过规定流程测量不同频率纯音检测阈的方法，通常以听力图报告耳别、频率和呈现方式。气导与骨导提供不同传入路径的信息。纯音阈值不能单独代表全部语音或双耳功能。[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry")

## 定义与分类

PTA 可以指 pure-tone audiometry，也可以指 pure-tone average，后者需要注明平均频率。测量方法、平均指标和听力损失分类不应混用。[校准](../audiometric-calibration/)建立输出标度，[语音接收阈](../speech-reception-threshold/)评价另一种任务；听力图是结果组织方式，而非病因本身。

### PTA 的两个常见含义

本词条中的 PTA 指 pure-tone audiometry。另一些论文用 PTA 指 pure-tone average，即若干频率听阈的平均值：

$$
\mathrm{PTA}_{\mathrm{avg}}=\frac{1}{K}\sum_{i=1}^{K}H(f_i).
$$

$H(f_i)$ 是指定频率的听阈，单位 dB HL。平均值必须同时写出包含的频率和耳别，不同频率组合不能仅凭缩写视为同一指标。

### dB HL 的参考含义

听力级以相应频率、换能器及标准耦合条件的参考阈为零点。教学上可写为：

$$
L_{\mathrm{HL}}(f)=L_{\mathrm{SPL,coupler}}(f)-\mathrm{RETSPL}(f).
$$

两项均以 dB 表示，RETSPL 是参考等效阈声压级。0 dB HL 不等于没有声压，也不表示每个个体必然在此检测到声音；不同换能器的参考零点不能任意交换。[4](#ref-iso-389-1-2017 "Acoustics — Reference zero for the calibration of audiometric equipment — Part 1: Reference equivalent threshold sound pressure levels for pure tones and supra-aural earphones")

## 原理与表征

### 图上的坐标意味着什么

听力图通常以频率为横轴、听力级 dB HL 为纵轴。dB HL 使用与频率、换能器和参考条件有关的零点；它不是声压级 dB SPL，也不是“零声压”。气导经耳机或插入式耳机呈现，骨导使用不同的换能器和参考框架。

测量还取决于指令、反应可靠性、呈现节奏、阈值搜索规则以及环境噪声。2005 年 ASHA 指南提供手动测听的测量与记录框架；实际使用应核对适用的现行规范。[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry")

### 真无线耳机自动测听的线索

Guo 等研究将真无线耳机用于自动纯音测听，包含声学与行为校准以及与参考测量的比较。因此“手机能播放纯音”只是系统的一环，不能直接推出能够准确测量听阈。[1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry")

后续 ANC 耳机研究进一步检查降噪、输出和自动测量条件。主动降噪可能改善部分条件下的背景噪声，但不能替代耳机输出校准、佩戴控制或测量验证。[2](#ref-zhou-anc-audiometry-2024 "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control")

### 气导与骨导回答不同问题

气导经外耳和中耳传入，骨导以振动激励听觉系统；二者的差异可为传导环节问题提供信息，但解释还依赖[掩蔽](../masking/)、耦合和有效阈值。骨导并不天然只作用于测试耳，气导也可能跨耳被听见。是否需要对非测试耳掩蔽，应按规范与具体情况判断。

ISO 8253-1 的公开适用范围涵盖气导与骨导纯音测听。本词条引用其范围与版本，未依据目录声称满足全部标准条款；具体规范应使用完整标准及专业流程。[5](#ref-iso-8253-1-2010 "Acoustics — Audiometric test methods — Part 1: Pure-tone air and bone conduction audiometry")；[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry")

### 便携系统需要验证什么

手机或 TWS 测听需要设备输出校准、换能器稳定性、环境噪声管理和与参考系统的比较。受试者听得到某段音，并不能证明该设备的 dB HL 标度有效。TWS 校准研究和集成质量控制的手机筛查研究，均针对具体系统与使用条件。[1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry")；[6](#ref-swanepoel-2014 "Smartphone hearing screening with integrated quality control and data management")

## 测量与研究方法

### 阈值搜索与反应可靠性

阈值是规定测量流程下的检测结果，受到反应判据和重复性影响。指导语、熟悉步骤、呈现持续时间、间隔变化及真假反应检查都有意义。单次按键不等于稳定阈值；受试者猜测、迟反应或对节律的预测可能改变结果。

听力图宜保留各频率、耳别和测试方式。PTA 在文献中可能表示 pure-tone audiometry，也可能表示 pure-tone average；后一种必须明确平均了哪些频率。一个平均数可能掩盖低频或高频局部损失，不能替代整张图。

### 与语音实验怎样结合

纯音阈值刻画各频率的检测敏感度；噪声语音、声调或双耳任务刻画不同的信息利用。比较实验组时，可用听力图说明可听度基础，同时保留语音任务的独立结论。筛查结果、临床听力测量与病因诊断属于不同层次，单项测试不能承担全部任务。

## 应用与解释边界

### 边界与更新重点

纯音听阈不能单独说明所有听力困难，也不能代替噪声下语音测量。

## 分析示例

### 解释示例：相同平均听阈的不同听力图

两个听者在选定频率的平均阈值相同，一个各频率较均匀，另一个低频较好、高频较差。它们对语音谱信息的可听度可能不同。只用平均值匹配实验组，可能仍留下重要频率差异，因此宜同时展示听力图。

对于左右耳不对称，双耳语音测试可能主要由较好耳支持；这不能证明较差耳敏感度正常。研究筛查时应明确参照的是较好耳、较差耳还是双耳平均，并按该目标验证。

测试前后轻微阈值变化可能来自佩戴、环境或反应波动。宜查看重复测量和各频率模式，而非仅以单个点的方向解释。规范测量条件是判断变化的基础。[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry")

## 研究沿革

纯音测听以标准化换能器、参考零点和阈值流程建立可比测量。ASHA 2005 年指南及 ISO 目录提供方法与范围入口，较新便携和 TWS 研究验证特定系统。标准全文的具体规范与公开目录不同，本词条不据目录声称满足全部条款。[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry") [5](#ref-iso-8253-1-2010 "Acoustics — Audiometric test methods — Part 1: Pure-tone air and bone conduction audiometry") [1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry")
