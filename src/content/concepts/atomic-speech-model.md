---
title: "原子语音模型"
english: "Atomic speech model"
slug: "atomic-speech-model"
summary: "解释基于 Gabor 原子的稀疏语音表示和原子率。"
categories: ["signal-processing","research-methods","speech"]
tags: ["ASM"]
aliases: ["ASM"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["kong-atomic-2025","meng-get-2023","mallat-1993"]
order: 26
knowledge_area: "methods"
kind: "model"
key_facts: [{"label":"缩写","value":"ASM"},{"label":"表示","value":"局部化 Gabor 原子的语音叠加"},{"label":"变量","value":"事件率、分布、宽度与跨耳安排"}]
---

**原子语音模型**（atomic speech model，ASM）用局部化 Gabor 原子组织稀疏语音，以可控信息密度研究识别及跨耳、跨时间的信息利用。“原子”是信号单元而非物理粒子；原子率阈值与噪声中的 dB SNR 阈值具有不同量纲。[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")

## 定义与分类

ASM 是研究模型，原子率是其事件密度变量，[SRT](../speech-reception-threshold/)是相应任务的阈值结果。一般字典稀疏分解也使用“原子”，但匹配追踪算法不能自动视为 ASM 实现。[GET](../get-vocoder/)主要连接编码事件与模拟，ASM 则借稀疏材料研究信息利用。

## 原理与表征

### 原子是信号单元

这里的“原子”不是物理粒子。它是局部化的信号构件，与 GET 的高斯包络振荡单元有形式上的联系。ASM 论文对分频后的信号进行稀疏采样，再以相应原子组织可播放语音；完整算法要按原文核验。[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")；[2](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

概念性的合成表示为：

$$
\hat{x}(t)=\sum_{q=1}^{Q}a_q\,g_q(t).
$$

$q$ 是事件索引，$a_q$ 为权重，$g_q$ 指定其时间、频率和形状。本式只表示单元叠加，不规定论文的选择算法或采样规则。

### 与稀疏表示的一般形式有何关系

ASM 用局部化事件研究信息稀疏度；一般时频字典方法也可写成原子的加权叠加，但不能因此把 ASM 等同匹配追踪。匹配追踪是逐步从字典选择解释残差的构件；ASM 论文的分带、采样和替换规则应依据其具体方法。[3](#ref-mallat-1993 "Matching pursuits with time-frequency dictionaries")；[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")

事件多少、出现在哪些带和时刻、具有怎样的幅度，分别决定稀疏表示。均匀删除与优先保留较强事件，即使最后数量相同，也不保证包含相同语音线索。

### 率、占用与信息量不是同一指标

总率 $R=Q/T$ 只描述事件密度。若每个事件平均有效时长为 $D$，$RD$ 可作为时间占用的粗略指标，但单元重叠和多带并行使其不必等于实际占用比例。不同宽度的原子，即使率相同，其时频覆盖仍不同。

每带采样率、谱峰选择后总事件率以及实际保留事件数，应分别统计。不能在尚未核对论文口径时，把某个“原子/秒”数值直接换算为电刺激脉冲率或[声码器](../vocoder/)包络采样率。

## 测量与研究方法

### 原子率怎样报告

若一段长度为 $T$ 秒的信号含 $Q$ 个合成事件，可定义教学上的总事件率 $R=Q/T$，单位原子/秒。论文具体采用的原子率统计口径还需区分总率、每带采样率与选择后事件数，不能只写一个数字。

稀疏程度不仅取决于事件数，也取决于事件分布。把同样数量集中于少数频带，与均匀铺开，不保证包含相同语音信息。

### 阈值与双耳实验

论文通过调整原子率寻找达到规定识别水平的条件；这里的 SRT 是原子率阈值，不是噪声信噪比阈值。它还通过跨耳分配等条件探索[双耳整合](../binaural-integration/)，结果存在条件和个体差异。[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")

因此把 ASM 结果与噪声下 dB SNR 阈值放在同一个数值轴上没有意义。应分别解释稀疏信息利用和抗[掩蔽](../masking/)任务。

### 阈值下降应如何解释

同一表示和任务中，达到目标正确率所需原子率更低，说明听者可利用更稀疏的该类信息。若换了原子宽度、通道范围或选择规则，阈值差还可能反映每个事件承载的信息变化，不一定是整合能力变强。

原论文以稀疏语音、跨耳分配和延迟等条件研究识别，结果有条件和个体差异。[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model") 此类证据适合约束行为模型，但不能直接证明自然神经系统按同样原子编码。

### 一个最小而有说服力的实验

固定频率范围和原子参数，在多个率下测识别并估计阈值；保存每次的事件数和分布，避免随机稀疏化造成未记录差异。然后比较完整信息同耳、左右各自单耳及互补跨耳条件，保持总体事件内容可比。

如果研究延迟，应明确延迟施加在整段耳信号、某些频带还是部分事件，并检查重叠与边缘处理。词或整句评分、猜测水平和训练都应报告。这样才能区分稀疏信息不足、时序错配与双耳整合代价。

## 应用与解释边界

### 解释边界

能理解某一种稀疏表示，并不证明自然听觉以同样原子实现编码。

## 分析示例

### 解释示例：相同原子率的不同分布

两段一秒信号都含 100 个事件，一段均匀分散，另一段集中在开头和少数频带。总率相同，但后一段可能遗漏语音关键片段。比较稀疏化方案时，应同时统计时间空缺、频带覆盖和幅度分布。

若使用随机保留事件，重复生成会带来材料实例差异。宜固定实例用于信号核查，并用多个实例估计行为稳定性；同一实例重复训练后的表现，也应与新实例泛化分开解释。[1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")

研究问题可集中于哪些事件最有价值，以及听者能否跨时间或跨耳补齐缺失。改变事件选择策略之后，低原子率阈值可能反映材料更有效，而非单纯神经整合变强。

## 研究沿革

时频字典与匹配追踪提供稀疏表示的一般背景，2023 年 GET 建立局部声学单元路线，2025 年 ASM 论文研究稀疏语音与跨耳及延迟条件。形式相似不代表相同算法，也不证明自然听觉采用同样单元编码。[3](#ref-mallat-1993 "Matching pursuits with time-frequency dictionaries") [2](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation") [1](#ref-kong-atomic-2025 "Sparse representation of speech using an atomic speech model")
