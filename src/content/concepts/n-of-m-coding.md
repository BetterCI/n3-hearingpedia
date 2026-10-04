---
title: "n-of-m 编码策略"
english: "n-of-m coding strategy"
slug: "n-of-m-coding"
summary: "解释分析频带、谱峰选择、刺激通道及 ACE 实现。"
categories: ["cochlear-implants","signal-processing"]
tags: ["n-of-m coding strategy"]
aliases: ["谱峰选择","maxima","ACE","电动态范围","EDR"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["mo-maxima-2023","meng-get-2023","zeng-2008","zhou-f0intfs-2023"]
order: 22
knowledge_area: "technology"
kind: "strategy"
key_facts: [{"label":"选择集合","value":"m 个候选分析通道"},{"label":"保留数量","value":"每帧 n 个谱峰"},{"label":"不同参数","value":"选择数量、帧率与脉冲率"}]
---

**n-of-m 编码**（n-of-m coding）是每个分析帧从 $m$ 个候选通道中选择 $n$ 个谱峰的信息选择方式，常见于[人工耳蜗](../cochlear-implant/)声音处理。其具体实现还包括特征提取、选择、压缩、映射与刺激安排，不能只由两个数字定义完整策略。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

## 定义与分类

n-of-m 是选择规则，不是通用的最佳通道数。候选分析带、物理电极和有效信息维度不同；CIS 的顺序脉冲原则又属于刺激安排。[通道相互作用](../channel-interaction/)影响实际信息表达，动态范围与总刺激预算也可能影响改变 n 后的结果。

## 原理与表征

### 分析通道、选择通道和电极

设第 $k$ 帧各通道的选择量为 $E_i[k]$，概念上的选择集合为：

$$
\mathcal{S}[k]=\operatorname{Top}_n\{E_1[k],\ldots,E_m[k]\}.
$$

$\operatorname{Top}_n$ 返回较大的 $n$ 项对应的索引，不是返回一个新的频谱。随后还需要幅度压缩、电极映射和脉冲安排。本式只说明选择原则；滤波、平滑、选择量及刺激顺序由具体实现决定。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

$m$ 个频带不一定对应同样多的独立感知维度；$n$ 也不等于设备安装的电极总数。改变 $n$ 会同时改变保留的谱信息和刺激拥挤程度。

### 电动态范围是什么

电动态范围（EDR）描述与刺激阈水平及上部舒适水平有关的可用电刺激范围。其单位、设备编码量以及从声学输入到电刺激的映射必须说明。它不是声学 dB SPL 动态范围，也不能把一个设备的电流差值直接用于另一个设备。

### 相关研究中的参数研究

Mo 等在实际人工耳蜗条件下研究谱峰数量与电动态范围对噪声中语音表现的影响。结果提示二者都是需要明确报告的实验参数；某个样本和配置下较好的数量，不是全体用户统一的调机推荐。[1](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy")

GET [声码器](../vocoder/)将编码与刺激序列的特征纳入声学模拟，使策略比较尽可能遵循相应编码步骤。但模拟保留了选择规则，也不意味着已经复制真实电听觉。[2](#ref-meng-get-2023 "Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation")

### 谱峰选择的数学描述

设第 $r$ 帧各带包络为 $E_k[r]$，选中集合为 $\mathcal S_r=\operatorname{TopN}\{E_1[r],\ldots,E_m[r]\}$，可概念性地表示选择后输入：

$$
U_k[r]=E_k[r]\,\mathbf 1\{k\in\mathcal S_r\}.
$$

$\mathbf 1$ 为指示函数，$n$ 是每帧保留的通道数，$m$ 是候选通道数。这一表达不规定包络提取、平局处理、刺激顺序或电映射；实现中的预加重和通道增益也可能影响哪一带被选中。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

### 选择数量的收益与代价

$n$ 较小时，输入较稀疏，可能减少同时需要表达的邻近信息，但也可能遗漏弱而重要的语音线索。$n$ 较大时保留更多谱细节，却不保证更多独立感知信息。峰值最大并不等于语言信息最多，尤其当[掩蔽](../masking/)声在部分频带占主导时。

还需区分通道选择与脉冲安排。如果改变 $n$ 的同时改变每通道脉冲率、总脉冲数或输出响度，行为差异包含多个因素。仅保持算法名称相同不保证条件可比。

### 与新策略的关系

F0inTFS 在原有谱峰选择之后增强选中高频带的周期性，因此“是否选中该通道”与“选中后如何调制”属于两个环节。[4](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants") TLE 则改变时间信息的表示。阅读策略比较时，应按分析、选择、时序和映射逐层对照，避免仅把所有参数统称为编码策略。

## 测量与研究方法

### 电动态范围影响比较

电映射把包络转换为可用刺激幅度。电动态范围缩窄可能压缩通道间差异，改变信息表达。Mo 等在所测试的谱峰数量和动态范围条件下比较性能；其中较优区间只适用于该实验，不能用作所有设备和听者的调机规则。[1](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy")

### 如何检查一个实现

保存每帧输入包络、选中索引和最终刺激事件；比较频带选择频率、随时间的切换及输出总能量。静音、极小输入和谱峰平局也应有明确行为。检查分析帧之间是否遗漏或重复事件，比只看一张平均谱更能发现问题。

在实验中，先固定 $m$、频率范围和映射，操纵 $n$；再单独研究动态范围。记录个体基线、训练和条件顺序。将语音、音高或双耳表现分别评价，不能由一个任务推断全部信息利用。

## 分析示例

### 解释示例：谱峰最强未必最有用

某帧的低频噪声能量很强，谱峰选择可能优先保留它，而较弱的目标辅音线索被舍弃。这是基于能量排序与基于任务信息排序的差别。是否真的发生，应检查带内目标与噪声贡献及最终选中索引，而非只从算法名称推断。

若提高 $n$ 后识别变好，可能是更多目标线索被保留；若变差，可能涉及重叠、响度或时序。设置保持其他输出条件可比的对照，有助于区分原因。[1](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy")

研究问题可进一步涉及选择稳定性：相邻帧的快速切换是否引入额外调制？不同选择阈值是否让弱输入不稳定？这些都属于具体实现，需要信号检查与行为实验共同验证。

## 研究沿革

人工耳蜗系统发展形成谱峰选择与不同刺激安排的组合。2023 年谱峰数量研究在所测动态范围条件下比较性能；F0inTFS 则在保留原选择规则的基础上增强周期性。它们分别操纵选择和选后表征，不能把特定实验较优 n 当作通用调机值。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation") [1](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy") [4](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")
