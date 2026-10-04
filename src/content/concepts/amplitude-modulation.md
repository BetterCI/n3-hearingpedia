---
title: "振幅调制"
english: "Amplitude modulation"
slug: "amplitude-modulation"
summary: "解释调制频率、调制深度以及电刺激包络调制。"
categories: ["acoustics","signal-processing"]
tags: ["AM"]
aliases: ["AM"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zhou-tle-2022","li-covarying-2025","viemeister-1979","dau-1997"]
illustration: {"src":"figures/envelope-tfs.svg","alt":"调制频率 20 Hz、载波频率 400 Hz 的理想 AM 波形","caption":"教学示意：调制频率与载波频率不同。参数仅用于展示正弦调幅，不是实验或临床默认设置。"}
order: 13
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"缩写","value":"AM"},{"label":"频率","value":"调制频率与载波频率分别报告"},{"label":"深度","value":"无量纲 m，或 20 log₁₀m dB"}]
---

**振幅调制**（amplitude modulation，AM）是信号幅度按一定规律随时间变化的方式。其描述包括载波、调制频率、深度和波形；听觉研究用它考察时间起伏检测、时间音高及编码。电刺激中的幅度调制与脉冲率必须分别说明。[3](#ref-viemeister-1979 "Temporal modulation transfer functions based upon modulation thresholds")

## 定义与分类

规则正弦调幅、随机包络起伏和自然语音调制具有不同谱结构。调制检测主要询问是否察觉起伏，调制速率辨别询问起伏快慢，利用调制识别语言又是不同任务。[时间包络](../temporal-envelope/)是幅度变化的表示；调制深度的 dB 标度不是声压级。

### 电刺激中要区分两种速率

在固定脉冲率的刺激序列中，各脉冲幅度仍可缓慢起伏。脉冲率以每秒脉冲数表示，调制频率以每秒包络周期数表示。提高其中一个不必提高另一个；二者协变也不代表知觉音高一定按相同比例改变。

声学调制深度的定义不能未经说明就搬到电流、响度或设备编码值上。比较电刺激时还要记录电流范围、脉冲宽度、电极及响度控制。

## 原理与表征

### 从声学模型开始

对正弦载波，一个常见教学模型为：

$$
x(t)=A[1+m\cos(2\pi f_mt)]\cos(2\pi f_ct).
$$

$A$ 为幅度，$m$ 为无量纲调制深度，通常取 $0\leq m\leq1$；$f_m$ 为调制频率、$f_c$ 为载波频率，单位均为 Hz。$m=0$ 时没有振幅起伏，$m=1$ 时理想包络最小值到零。频谱中可出现 $f_c-f_m$ 与 $f_c+f_m$ 的边带。

上述模型只描述一种规则信号。语音包络同时含有多个变化速率，不能简单概括为一个 $f_m$。

### 相关研究中的两条线索

TLE 关注把频带时间信息转换为可利用的刺激变化，其效果需要通过具体音高任务检验。[1](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")

2025 年协变振幅调制与脉冲率的研究探索组合时间线索对音高辨别的影响。本词条引用的是 **medRxiv 预印本，尚未同行评审**；结果依刺激范围和受试者条件而定，不能视为已确立的通用编码方案。后续同组版本应按同一研究线索追踪，不能重复计算为独立证据。[2](#ref-li-covarying-2025 "Covarying Amplitude Modulation and Pulse Rate Enhances Pitch Discrimination in Cochlear Implant Users")

### 侧带说明调制会改变频谱

对正弦载波的正弦调幅：

$$
x(t)=A\cos(2\pi f_ct)+\frac{Am}{2}\{\cos[2\pi(f_c+f_m)t]+\cos[2\pi(f_c-f_m)t]\}.
$$

$f_c$ 是载波频率，$f_m$ 是调制频率，$m$ 是无量纲调制度。当 $0\le m\le1$ 时原调幅包络不跨过零。该展开说明出现两个侧带；改变调制度也改变侧带幅度，故调制检测可能受听者能否分辨侧带影响。

调制度常以 $20\log_{10}m$ dB 报告，例如 $m=0.1$ 为 −20 dB。它不是声压级，也不是信噪比。对于足够长且满足周期平均条件的载波，调幅后的平均功率含 $1+m^2/2$ 因子；若需比较等能量刺激，应处理这种变化，而不是默认相同载波幅度就代表相同 RMS。

### 电刺激中的三种速率

脉冲率规定每秒发送多少脉冲；调制率规定脉冲幅度变化多少次；帧率规定多久重新计算参数。三者不能混写。若脉冲幅度以 $f_m$ 变化，脉冲序列必须有足够时间采样，同时受到刺激安排和总速率约束。

共变调幅与脉冲频率的预印本只提供其任务和样本下的初步证据，不能作为已建立的通用编码收益。[2](#ref-li-covarying-2025 "Covarying Amplitude Modulation and Pulse Rate Enhances Pitch Discrimination in Cochlear Implant Users")

## 测量与研究方法

### 时间调制传递函数怎样测量

在不同 $f_m$ 下寻找刚能区分调幅与未调幅声音的深度。采用噪声载波可以减少特定纯音侧带线索，但噪声本身有随机起伏，载波带宽、时长和声级仍会改变阈值。Viemeister 的经典研究说明这些因素必须进入解释。[3](#ref-viemeister-1979 "Temporal modulation transfer functions based upon modulation thresholds")

行为上的低通趋势可以用时间处理限制解释，但不是对单一神经截止频率的直接定位。调制滤波器组模型还考虑不同调制频率间的检测与[掩蔽](../masking/)关系，是功能模型的一条路线。[4](#ref-dau-1997 "Modeling auditory processing of amplitude modulation. I. Detection and masking with narrow-band carriers")

### 一次可解释的实验比较

比较调制检测时，固定或明确控制载波、时长、声级及起止包络；比较调制音高时，还需控制响度与频谱位置。记录阈值对应正确率、训练和重复测量。检测到起伏、分辨起伏快慢以及利用起伏识别语音，是不同任务，应分别报告结果。

## 分析示例

### 解释示例：检测到起伏不等于辨别速率

听者可以判断一个声音具有幅度起伏，却无法稳定区分起伏快慢。前者的自变量通常是深度，后者可能是调制频率差；两种阈值单位与实验目标不同。若将它们合成一个“时间分辨率”数字，就会丢失可解释性。

比较 20 与 40 Hz 调制时，应检查两声音平均能量、载波和时长是否一致，以及是否出现可利用的侧带或起止差异。较短声音可能只包含少数调制周期，难度变化也可能来自可观察周期数。[3](#ref-viemeister-1979 "Temporal modulation transfer functions based upon modulation thresholds")

对电刺激而言，若降低脉冲率却保留较高调制率，输出可能不能充分表达目标包络。应先验证刺激序列，再评估听者成绩；输入公式中的调制不一定等于最终可用调制。

## 研究沿革

Viemeister 1979 年时间调制传递函数研究考察不同条件下的调制检测。Dau 等 1997 年提出调制处理的功能建模路线。电刺激组合时间线索的较新工作应按发表状态与样本限定，未同行评审的共变研究不能视为已经确立的策略收益。[3](#ref-viemeister-1979 "Temporal modulation transfer functions based upon modulation thresholds") [4](#ref-dau-1997 "Modeling auditory processing of amplitude modulation. I. Detection and masking with narrow-band carriers") [2](#ref-li-covarying-2025 "Covarying Amplitude Modulation and Pulse Rate Enhances Pitch Discrimination in Cochlear Implant Users")
