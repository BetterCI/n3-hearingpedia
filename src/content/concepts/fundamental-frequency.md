---
title: "基频"
english: "Fundamental frequency"
slug: "fundamental-frequency"
summary: "解释基频、周期、谐波及在语音中的变化。"
categories: ["acoustics","speech"]
tags: ["F0"]
aliases: ["F0"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zhou-f0intfs-2023","shi-harmonicity-2025","yin-2002","kong-tones-2006"]
order: 11
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"符号","value":"F₀"},{"label":"单位","value":"Hz"},{"label":"定义","value":"严格周期信号最小正周期的倒数"}]
---

**基频**（fundamental frequency，$F_0$）是严格周期信号最小正周期的倒数。在语音中通常以局部近似周期的轨迹表示，清音或不规则发声段可能没有可靠的单一估计。基频与音高相关，但不是[音高感知](../pitch-perception/)本身。[3](#ref-yin-2002 "YIN, a fundamental frequency estimator for speech and music")

## 定义与分类

基频、谐波频率和共振峰分别描述重复周期、整数倍分量和声道响应峰。频谱中最强或最低可见峰不一定等于基频；[音高](../pitch-perception/)也不要求存在实际基频谱线。估计器是测量方法，轨迹是估计结果，真实周期变化与倍频错误需要通过信号核查区分。

### 周期、频谱和单位

若信号的基本周期为 $T_0$ 秒，则：

$$
F_0=\frac{1}{T_0},\qquad f_n=nF_0.
$$

$F_0$ 与谐波频率 $f_n$ 的单位为 Hz，$n$ 是正整数。例如 $T_0=0.005$ 秒对应 $F_0=200$ Hz，理想谐波位于 200、400、600 Hz 等位置。这个例子是教学信号，不是任何受试者或语料的测量结果。

“基频”也不保证频谱中实际存在对应分量：某些谐波复合音缺少第一谐波，仍有共同的重复周期。自然语音只有近似、局部的周期性，无声辅音段通常不宜强行赋予稳定的 $F_0$。

### 周期定义与语音中的变化

严格周期信号满足 $x(t+T_0)=x(t)$，最小正周期为 $T_0$ 时，$F_0=1/T_0$。语音声带振动通常只是局部近似周期，$F_0(t)$ 是随时间变化的轨迹；清音段、停顿或不规则发声不一定存在可可靠估计的单一基频。给每一帧强制输出数字会制造虚假的连续轨迹。

频谱中第 $n$ 个谐波理想位置为 $nF_0$，但共振峰是声道响应的峰，两者不同。提高 $F_0$ 会使谐波取样更稀疏，不等于把所有共振峰也按比例提高。调音高、改变说话人音色和时间拉伸是不同操作。

## 原理与表征

### 在研究中的位置

F0inTFS 的设计利用低频带中的周期性信息，而不是简单把一条独立估计的基频轨迹直接替代全部语音。读算法时要区分“显式估计 $F_0$”和“让处理后的刺激含有与 $F_0$ 相关的重复结构”。[1](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

[谐波性](../harmonicity/)研究进一步关心分量之间是否保持整数倍关系。两种声音的估计基频相近，并不代表它们具有相同谐波性或可懂度。[2](#ref-shi-harmonicity-2025 "Effects of harmonicity on Mandarin speech perception in cochlear implant users")

## 测量与研究方法

### 为什么估计方法会改变结果

时间域估计寻找重复间隔，频域估计寻找谐波间距；实际分析还需要窗长、帧移、有声判断及范围约束。把周期误判为两倍会产生半频错误，把半周期当成完整周期会产生倍频错误。噪声、气声和不规则发声会增加困难。

绘制 $F_0(t)$ 轮廓时，应说明未检测到基频的帧如何处理。插值曲线可能便于展示，却不应让读者误以为每个时刻都有可靠测量。

### 一个基频估计器如何工作

YIN 的方法路线利用延迟差分寻找重复周期。其基本差分量可示意为：

$$
d(\tau)=\sum_{n\in\mathcal W}[x(n)-x(n+\tau)]^2.
$$

$\tau$ 为样本延迟、$\mathcal W$ 为分析窗；候选周期对应较小差分。完整算法还包含归一化、候选选择与插值，不能仅以最小 $d$ 代替原方法。[3](#ref-yin-2002 "YIN, a fundamental frequency estimator for speech and music")

搜索范围、窗长和有声判决决定结果。低基频需要足够长的时间窗来观察多个周期，但长窗可能抹平快速变化；高噪声、倍周期和次谐波可造成倍频或半频错误。应在原波形、频谱与估计轨迹之间交叉检查，而非只观察一条平滑曲线。

### 轨迹比较为何常用对数尺度

以参考频率 $F_{\mathrm{ref}}$ 定义 $s(t)=12\log_2[F_0(t)/F_{\mathrm{ref}}]$，可把比例变化转成半音尺度。参考应明确是固定值、说话人基线还是试次内均值；不同归一化会保留或消除绝对高度差。对无声段不应直接取对数，可标为缺失并说明插值规则。

### 基频信息如何进入不同表示

低阶谐波可在频谱中提供间隔结构；不可分辨谐波可产生 $F_0$ 包络起伏；低频带精细结构也可能包含相关周期性。这些不是同一种实现。F0inTFS 利用低频带信号增强高频带包络，不需要先得到一条显式 $F_0$ 估计轨迹。[1](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

普通话声调任务需同时关注轨迹方向、范围和时序，并控制响度和时长等辅助线索。一个估计器在干净朗读中准确，不保证其在[声码器](../vocoder/)输出、噪声或儿童声音中具有同样性能。[4](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition")

## 应用与解释边界

### 解释边界

基频属于刺激描述，音高属于知觉，普通话声调属于语言类别。

## 分析示例

### 解释示例：倍频错误如何被发现

某估计轨迹在相邻帧突然从 120 Hz 跳到 240 Hz，可能是说话人的真实变化，也可能是算法误选半周期。可查看原波形重复间隔、谐波间距和相邻帧有声状态，不能只用平滑器将跳变消掉。平滑可能掩盖错误，也可能抹掉真实快速变化。

报告估计性能时，宜分开有声判定错误、粗大周期错误和正确周期下的小偏差，并说明参考轨迹怎样获得。噪声条件中的基频性能需要相应验证，不能从安静语音准确率推导。[3](#ref-yin-2002 "YIN, a fundamental frequency estimator for speech and music")

在周期性增强策略中，即便没有显式估计器，也要检验低频输入是否可靠，以及无声段会生成什么输出。没有输出一个 F0 数字，并不意味着完全摆脱了基频范围与输入质量的限制。

## 研究沿革

语音研究使用周期差分等方法从有限片段估计基频，2002 年 YIN 论文系统描述了相关算法路线。普通话声调研究将轨迹与频谱、包络及辅助线索联系；F0inTFS 则采用低频时间信息增强周期性，不需要先得到显式基频轨迹。[3](#ref-yin-2002 "YIN, a fundamental frequency estimator for speech and music") [4](#ref-kong-tones-2006 "Temporal and spectral cues in Mandarin tone recognition") [1](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")
