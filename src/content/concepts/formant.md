---
title: "共振峰"
english: "Formant"
slug: "formant"
summary: "声道共振相关的谱特征，是元音等语音分析的重要概念，不能与基频、谐波或任意谱峰混同。"
categories: ["acoustics","speech","signal-processing"]
tags: ["formant"]
aliases: ["formants","F1","F2","F3","formant frequency","共振峰频率"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["yun-formant-2026","zebe-formants-2026","yin-2002"]
batch: 3
order: 43
literature_checked_at: "2026-10-04"
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"主要对象","value":"声道共振相关频率与带宽"},{"label":"常见记号","value":"F1、F2、F3 等"},{"label":"主要区别","value":"基频、谐波与声道共振"}]
---

**共振峰**（formant）是语音声学中与声道共振相关的谱特征，常以 F1、F2、F3 等表示由低到高的共振峰频率，也可描述其带宽和强度。它是研究元音与发音的重要入口。[基频](../fundamental-frequency/)描述声源周期性，谐波描述周期声源的整数倍频率结构，共振峰则主要联系声道滤波作用，三者不能混同。[1](#ref-yun-formant-2026 "Effects of glottal and velopharyngeal port openings on the first formant frequency in natural speech")

## 定义与分类

### 共振与观察到的谱峰

理想共振频率与实际语音幅度谱上看到的峰并不必完全重合。周期声源只在有限谐波处提供采样，声源谱、噪声、声门和鼻腔耦合也会改变谱形。因此某个最高谐波的频率不是自动等于共振峰，自动算法找到的每个峰也不是一个真实声道共振。

### 频率、带宽与轨迹

共振峰频率一般以 Hz 表示，带宽描述峰的频率扩展，连续语音还可以记录随时间变化的轨迹。F1 与 F2 常用于元音空间，但只报告两个中心频率不能完整描述声道、音质或可懂度。发音过渡、时长和频谱能量也会参与感知。

### 与谐波和音高的区别

有声语音中谐波间距通常联系基频，声道响应决定哪些谐波相对增强。改变 F0 会改变谱的采样位置，即使声道形状近似不变，观察到的峰形也可能变化。[谐波性](../harmonicity/)与[音高](../pitch-perception/)因此提供与共振峰不同的信息。

## 声源—滤波原理

最简单教学模型将声源与声道响应分开：

$$
X(f)=G(f)H(f)
$$

$G$ 是声源谱，$H$ 是声道传递函数，$X$ 是输出谱；真实模型还可能包括辐射和相互作用。该近似帮助区分声源周期性与声道共振，并不保证二者完全独立，也不说明所有发声条件都能用同一线性模型解释。

F1 常与舌高或开口相关，F2 常与前后舌位相关，但这些是有条件的经验联系，不能反向唯一恢复姿态。嘴唇、声道长度、声门和腭咽端口等都可能共同影响共振。不同说话者、语境或歌唱状态下的相同元音，也可能出现不同频率。[1](#ref-yun-formant-2026 "Effects of glottal and velopharyngeal port openings on the first formant frequency in natural speech")[2](#ref-zebe-formants-2026 "Acoustic analyses on German vowels in read speech, recited speech, and singing")

鼻腔耦合还可能引入新的共振和反共振，使简单的全极点估计受限。真实发声中的边界变化可能产生与简化模型不同的方向，因此模型结论应由合适的生理与声学测量检验。

## 估计与测量方法

频谱、谱包络和线性预测分析可辅助估计共振峰，但需说明采样率、预加重、窗长、模型阶数和搜索范围。窗太短时频率分辨受限，太长则可能混入明显发音变化；较高 F0 时谐波稀疏，也会增加估计不确定性。

自动轨迹应结合原始声谱图检查，避免跳峰、合并峰或把噪声当峰。基频估计和共振峰估计属于不同任务；YIN 等基频方法不能直接替代声道共振分析。[3](#ref-yin-2002 "YIN, a fundamental frequency estimator for speech and music")

跨说话者比较还需考虑声道长度、语料、语音环境与归一化。归一化可以支持某些比较，但不应消除研究本来关注的生理差异。输出频率和带宽的不确定性应与组间变化幅度一起评价。

## 听觉应用与局限

共振峰信息参与元音区别和语音分析，也是[声码器](../vocoder/)及听觉设备研究的材料线索。处理造成的频谱平滑或位置变化可能影响这些信息，但效果需要在具体语料与听者中测量。保留共振峰形状不自动保证完整[言语可懂度](../speech-intelligibility/)，因为时间、辅音、语言和背景条件也有作用。

## 分析示例

若同一说话者提高 F0 后自动算法输出 F1 上升，先检查是否只是谐波采样和峰选择改变，再判断声道是否实际变化。可在稳定元音区间比较不同估计方法和谱包络，并保留人工核查规则。不能仅凭一个自动值直接写出“舌位下降”。

在跨发声方式研究中，还应匹配元音和语境，并记录声级、鼻腔耦合等条件；朗读与歌唱的差异不必只有一个机制。

## 研究沿革与近期进展

共振峰由静态元音描述逐渐扩展到动态语音和真实发音条件。Yun 等 2026 年 9 月论文在 21 名说话者的德语元音中同步考察声门与腭咽端口，摘要报告 F1 变化涉及边界和耦合，部分方向与模型预测不同。Zebe-Sheng 与 Immerz 10 月论文则比较 16 名专业女歌者在朗读、吟诵和歌唱中的 F1/F2。它们提示保留语境与生理条件，不能直接外推所有语言或说话者。[1](#ref-yun-formant-2026 "Effects of glottal and velopharyngeal port openings on the first formant frequency in natural speech")[2](#ref-zebe-formants-2026 "Acoustic analyses on German vowels in read speech, recited speech, and singing")
