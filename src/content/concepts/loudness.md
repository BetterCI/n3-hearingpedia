---
title: "响度"
english: "Loudness"
slug: "loudness"
summary: "声音被感知为强弱的知觉属性，受声级、频谱、时域结构、双耳输入及听觉状态共同影响。"
categories: ["psychoacoustics","acoustics"]
tags: ["loudness"]
aliases: ["loudness perception","响度感知","响度重振"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["moore-loudness-2014","robles-2001","guerit-focusing-2026"]
batch: 3
order: 31
literature_checked_at: "2026-10-04"
knowledge_area: "perception"
kind: "function"
key_facts: [{"label":"概念层次","value":"强弱的知觉属性"},{"label":"常见标度","value":"响度 sone；响度级 phon"},{"label":"主要区别","value":"不等同于声压级或音高"}]
---

**响度**（loudness）是声音在知觉上被感受为强或弱的属性。声压级是输入声音的物理描述，而响度描述听者的体验。二者通常相关，却不是同一量；相同声压级的不同频率、不同带宽或不同时长声音，可以具有不同响度。响度也不同于[音高](../pitch-perception/)，后者主要描述声音在知觉上的高低。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

## 定义与标度

### 响度与响度级

响度常以 sone 表示，作为知觉强度比例标度；响度级以 phon 表示，依据与参考频率声音的等响关系定义。按经典约定，1 sone 对应参考条件下 40 phon 的响度。参考音、呈现方式和测量程序构成定义的一部分，不能把任意声音的 dB SPL 数值直接改写为 phon 或 sone。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

### 等响与响度增长

等响比较询问两种声音是否同样响；响度增长询问同一种声音随输入水平变化时感受如何变化。前者常控制参考音并调节比较音，后者可以采用类别判断或数值估计。不同方法的响应偏差和标度不同，不能不经转换混用。

### 部分响度

目标声音与背景共同呈现时，目标的部分响度描述其在混合物中的知觉强度。它不同于混合声音的总响度，也不同于目标是否可检测。背景声能量增大时，总响度可能增加而目标更难辨认，因此响度不能直接代表[语音可懂度](../speech-intelligibility/)。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

## 原理与模型

耳蜗中的频率分析和声级相关非线性参与响度形成。常见模型先表示外中耳传递与[听觉滤波器](../auditory-filter/)输出，再把频率相关兴奋转换为特定响度，最后进行谱域求和。特定响度类似知觉强度的密度；Zwicker 与 Cambridge 系列采用不同频率标度和转换细节，参数不能随意拼接。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")[2](#ref-robles-2001 "Mechanics of the Mammalian Cochlea")

以连续频率位置标度 $z$ 表示，可以用教学式概括总响度：

$$
N=\int N'(z)\,\mathrm{d}z
$$

$N'$ 是特定响度，单位需与 $z$ 的标度匹配；$N$ 以 sone 表示。若 $z$ 采用 ERB-number，密度相对于该标度定义。这只说明求和结构，不是可直接运行的完整模型，也没有给出双耳合并及时间积分规则。

谱分布、声音持续时间和双耳呈现均会影响结果。对时间变化声音，瞬时、短时和较长时程响度可能不同。高层语境和声源距离知觉也可能影响判断，经典外周模型不能包含所有影响。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

## 测量方法

类别响度判断要求听者按规定类别评估，响度匹配则调节一个声音以匹配另一个。实验应报告刺激频谱、时长、耳别、呈现设备和判断规则。调节式任务还应控制先后顺序及锚定影响；将群体平均曲线用于个人之前需要验证个体差异。

在[听力损失](../hearing-loss/)中，一些耳蜗性损伤会表现为较高听阈与较快的阈上响度增长，即响度重振。它不等同于所有听觉过敏现象，也不能由阈值升高单独确定。测量增长曲线有助于解释[动态范围](../dynamic-range/)和放大需求，但不能唯一定位细胞病变。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

## 技术应用与边界

[助听器](../hearing-aid/)需要在可听性、响度与舒适度之间平衡；[人工耳蜗](../cochlear-implant/)的电流、脉宽、脉冲速率和通道配置共同影响响度。两个电刺激程序即使峰值电流相同，也可能不等响。比较编码策略时往往需要先控制响度，再讨论辨别或识别差异。

等响并不等于等兴奋分布，更不等于等信息量。若一种处理的声音更响，识别差异可能混有可听性因素；若完成等响匹配，仍需检查频谱、时间和空间信息是否发生变化。

## 分析示例

比较窄带与宽带噪声时，先固定总体声压级。宽带声可能跨更多听觉频带产生兴奋，从而有不同响度；若改为逐频带声级相同，总能量也会改变。研究必须明确是控制总体级还是频带级，否则无法辨明响度差异来自谱分布还是总能量。

同理，在电流聚焦比较中，减少空间扩散后可能需要调整电流或其他参数达到等响。比较时应记录这些补偿，而不能只将电极配置差异归为“空间分辨率提升”。

## 研究沿革与近期进展

从等响测量到频带求和和时变模型，响度研究逐渐同时处理正常与受损听觉。2026 年 10 月 Guérit 与 Carlyon 的正式论文结合 16 名人工耳蜗使用者与计算模型，讨论电流聚焦、兴奋图形锐度和响度的权衡。摘要强调需要在多通道、复杂刺激下评价；这支持把响度作为控制因素，不能据此宣称某种聚焦策略已经改善临床语音识别。[3](#ref-guerit-focusing-2026 "On Balancing Sharpness of Excitation Patterns, Loudness, and Potential Effects on Speech Perception with Cochlear-Implant Current-Focussing Strategies")
