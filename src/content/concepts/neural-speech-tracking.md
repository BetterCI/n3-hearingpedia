---
title: "语音神经跟踪"
english: "Neural speech tracking"
slug: "neural-speech-tracking"
summary: "量化神经记录与连续语音特征之间时序关系的分析框架，用于研究编码、注意和交流功能。"
categories: ["neuroscience","research-methods","speech"]
tags: ["neural-speech-tracking"]
aliases: ["cortical speech tracking","speech tracking","cortical tracking","皮层语音跟踪","神经语音跟踪","时域响应函数","TRF"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["lalor-speech-2010","osullivan-aad-2015","guo-tracking-2026","mo-ci-adaptation-2026"]
batch: 3
order: 38
literature_checked_at: "2026-10-04"
knowledge_area: "methods"
kind: "analysis"
key_facts: [{"label":"输入对象","value":"语音特征与神经时间序列"},{"label":"常见模型","value":"前向响应函数或后向重建"},{"label":"主要限制","value":"跟踪相关不等于理解或因果"}]
---

**语音神经跟踪**（neural speech tracking）是量化连续语音特征与神经记录之间时序关系的一类分析框架。研究可以使用[脑电图](../electroencephalography/)、MEG 或其他记录，考察声音包络、频谱或语言特征如何与响应联系。常见皮层语音跟踪属于这一范围；“跟踪”描述统计对应，并不意味着神经信号逐点复制声音或必然代表理解。[1](#ref-lalor-speech-2010 "Neural responses to uninterrupted natural speech can be extracted with precise temporal resolution")[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 定义与分类

### 前向编码

前向模型用声音特征预测神经记录，估计时间延迟相关的响应函数。它有助于描述某种特征与哪些时间尺度的活动相关；预测成功不能单独证明该特征的唯一神经机制，也不说明未纳入的声音特征没有作用。

### 后向重建

后向模型用多通道神经记录重建声音特征，再比较重建结果与候选声音的相似程度。它适合一些[听觉注意](../auditory-attention/)解码任务，但模型权重混合了多个通道和相关结构，不能直接把每个权重当作生理源强度。[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

### 特征与响应指标

[时域包络](../temporal-envelope/)是常用特征，但频谱、声学起点和词语层面变量也可进入模型。相关系数、解释方差和解码准确率回答不同问题。频段、特征定义和时间窗会改变数值，跨研究不能仅凭相关系数大小排序听觉能力。

## 核心原理

单特征线性前向模型可以用教学式表示：

$$
r(t)=\sum_{\tau=\tau_{\min}}^{\tau_{\max}}h(\tau)s(t-\tau)+\varepsilon(t)
$$

$s$ 表示声音特征，$r$ 表示指定神经通道记录，$h$ 是时域响应函数，$\tau$ 为离散延迟，$\varepsilon$ 是未解释项。多特征、多通道模型在相应维度上扩展。模型是对关系的近似，并不宣称整个听觉系统线性。[1](#ref-lalor-speech-2010 "Neural responses to uninterrupted natural speech can be extracted with precise temporal resolution")

连续语音具有强时间相关性，特征间也常高度相关。因此训练时需要正则化和独立验证，并在训练部分选择超参数。若同时纳入包络与起点，某项权重变化可能受共线性影响；“加入特征后预测提升”比单看权重更适合讨论额外解释价值。

## 测量与验证

首先校验语音与神经记录的时间同步，再明确滤波、特征生成、延迟范围和数据剔除。固定偏移或无线延迟会影响估计时窗；[人工耳蜗](../cochlear-implant/)刺激伪迹还可能与包络相关，须通过独立检查确认神经解释。

训练和测试应按实际推广对象划分。对同一人的新段落推广、对新说话者推广和对新受试者推广具有不同难度。应比较打乱、时间错位或适当基线，并考虑相邻窗口相关性，避免把同一录音的重复信息当作独立样本。[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 应用与边界

跟踪可帮助研究选择性注意、[听觉可塑性](../auditory-plasticity/)和感觉恢复，但较强跟踪不自动表示[言语可懂度](../speech-intelligibility/)更好。声音本身更清晰、注意不同、噪声较小或模型条件变化，都可能影响数值。相关也不能单独证明响应变化导致行为改善。

尤其需要区分群体条件标记与个体[语音接收阈](../speech-reception-threshold/)预测。一个模型能够区分安静和噪声条件，并不意味着它能准确估计新个体的阈值。实际预测还应报告误差、基线比较、协议依赖和外部验证，而不仅是统计显著性。[3](#ref-guo-tracking-2026 "Boundary conditions for cortical speech tracking as an objective speech-in-noise marker: a three-dataset MEG/EEG benchmark")

## 分析示例

在两位说话者竞争时，使用同一训练规则对独立试次重建包络，比较其与目标和非目标的相关。若目标相关更高，可支持该任务下的注意选择信息。再若希望估计噪声阈值，需要另有行为阈值作为目标，并在未参与训练的受试者中验证误差；不能把注意分类准确率直接换成 dB。

纵向变化还需控制记录质量、刺激材料和分析流程。如果后期保留了更多试次，跟踪增加可能部分来自估计更稳定，不能只归因于神经适应。

## 研究沿革与近期进展

Lalor 与 Foxe 的连续语音响应提取和 O’Sullivan 等的 EEG 注意解码建立了重要方法入口。2026 年 Guo 等的三个公开数据集基准研究强调，群体条件和注意效应比无条件个体阈值预测更稳健。同期 Mo 等人工耳蜗纵向研究显示跟踪与行为适应相关。两类证据互补：跟踪可用于研究变化，个体评估用途仍需针对协议验证。[1](#ref-lalor-speech-2010 "Neural responses to uninterrupted natural speech can be extracted with precise temporal resolution")[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")[3](#ref-guo-tracking-2026 "Boundary conditions for cortical speech tracking as an objective speech-in-noise marker: a three-dataset MEG/EEG benchmark")[4](#ref-mo-ci-adaptation-2026 "Longitudinal adaptations in neural and behavioral systems following hearing restoration using cochlear implants")
