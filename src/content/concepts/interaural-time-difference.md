---
title: "双耳时间差"
english: "Interaural time difference"
slug: "interaural-time-difference"
summary: "区分波形与包络的双耳时间差，连接空间听觉任务。"
categories: ["binaural","acoustics"]
tags: ["ITD"]
aliases: ["ITD"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["wan-itd-2020","kan-tle-2021","mcalpine-2001","goupell-2013","kan-2013"]
order: 15
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"缩写","value":"ITD"},{"label":"单位","value":"秒、毫秒或微秒"},{"label":"本文符号","value":"τ=tR−tL，正值表示左耳先到"}]
---

**双耳时间差**（interaural time difference，ITD）是声音在两耳之间的到达或对应时间差，是空间听觉的重要线索。研究中需区分声波、精细结构、包络或脉冲时序的时间关系，以及耳机侧化与声场定位任务。[3](#ref-mcalpine-2001 "A neural code for low-frequency sound localization in mammals")

## 定义与分类

ITD 是物理时间关系，侧化和定位是行为任务。对于单频信号，时间差与取模相位差有关；宽带延迟则不能等同所有频率反相。[双耳可懂度级差](../binaural-intelligibility-level-difference/)是识别阈值差，不是 ITD 的另一个单位；双耳时域线索与声级线索也应分别控制。

## 原理与表征

### 先约定方向

令左右耳到达时间分别为 $t_L,t_R$，本词条约定：

$$
\tau=t_R-t_L.
$$

$\tau$ 单位为秒，通常也用微秒表示；正值表示左耳先到。其他论文可能采用相反符号，比较前要检查定义。对频率为 $f$ 的纯音，相位差与时间差满足 $\Delta\phi=2\pi f\tau$，但相位只有模 $2\pi$ 的信息，不能总能唯一确定时间差。

### 波形与包络不是同一个延迟

窄带声音的内部振荡和较慢包络可以分别设置双耳差异。两耳刺激有相同包络，并不意味着精细结构也相同；反相操作也不等于给宽带信号添加一个恒定时间延迟。

自由声场中的头部、耳廓和反射还会改变声音。耳机中仅操纵 ITD 的侧化任务，回答的是受控刺激的位置感觉，不应直接称为完整的现实声源定位能力。

### 人工耳蜗中的额外约束

两个处理器的时钟、脉冲时序、频带与电极匹配都会影响跨耳时间关系。将声学时域线索编码到电刺激中，并不保证听者能够利用它。TLE 的相关机制文献讨论频带转换及双侧处理对时域信息的影响。[2](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants")

Wan 等的会议论文用[声码器](../vocoder/)模拟比较 TLE 与 CIS 对 ITD 相关任务的表现。它提供策略研究的线索，证据范围限于该模拟与任务，不能写成所有双侧植入者定位改善。[1](#ref-wan-itd-2020 "Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder")

### 时间差、相位差与歧义

规定 $\tau=t_R-t_L$：正值表示声音先到左耳。对于单一频率 $f$，若用左相位减右相位定义相位差，则 $\Delta\phi=2\pi f\tau$，但实际观察到的相位按 $2\pi$ 取模。于是不同时间差可能对应相同的纯音相位关系；频率升高并不只是“时间差线索更多”，还涉及周期歧义和神经时域表征限制。

包络 ITD 描述幅度起伏的跨耳延迟，精细结构 ITD 描述快速振荡的跨耳关系。研究脉冲式或调幅声音时，两者可能被独立操纵，也可能随处理一起改变。报告一个 ITD 数字之前，应说明延迟施加在哪个信号层面。

### 相关性分析能说明什么

可用归一化互相关检查两耳信号：

$$
\rho(\tau)=\frac{\sum_n x_L(n)x_R(n+\tau)}{\sqrt{\sum_n x_L^2(n)\sum_n x_R^2(n+\tau)}}.
$$

延迟单位在此为样本，应除以采样率换成秒；计算需处理边界并说明窗。相关峰值反映信号关系，不直接等于神经机制或受试者定位。多频率和噪声条件可能有宽峰或多个峰。

动物神经研究提供了低频空间信息由群体活动编码的证据，提醒我们不能把单一理想延迟线模型视为全部物种和频段的唯一实现。[3](#ref-mcalpine-2001 "A neural code for low-frequency sound localization in mammals")

### 侧化与定位为何要分开

耳机下判断声像偏左或偏右，通常称为侧化；自由声场判断声源方向，属于定位，还包含头相关频谱、声级差及头部运动线索。耳机实验中的侧化改善不必然等于真实环境定位改善。

双耳[人工耳蜗](../cochlear-implant/)需要考虑共同时间基准、处理延迟、刺激同步与两耳频位匹配。正常听力模拟研究和真实双侧植入者研究均提示，跨耳位置不匹配会影响融合或侧化，但两种证据的接口不同。[4](#ref-goupell-2013 "Effect of mismatched place-of-stimulation on the salience of binaural cues in conditions that simulate bilateral cochlear-implant listening")；[5](#ref-kan-2013 "Effect of mismatched place-of-stimulation on binaural fusion and lateralization in bilateral cochlear-implant users")

## 测量与研究方法

### 阅读和更新重点

记录差异施加在声波、包络还是脉冲层面，以及两耳是否同步、刺激是否等响。后续分别建立双耳强度差、侧化、定位和 ITD 辨别阈词条；不要把任务名称或单位相近当作测量等价。

### 一个复现检查框架

先验证最终播放的左右信号确有目标延迟，同时检查 ILD、包络和频谱；再使用多个延迟与无延迟条件，平衡左右顺序并评估个体变化。TLE 的 ITD 声码器研究应明确为正常听力模拟，不能直接写成双侧植入者的空间听觉恢复。[1](#ref-wan-itd-2020 "Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder")

## 分析示例

### 解释示例：同一延迟在不同频率下

1000 Hz 纯音的周期为 1 ms。0.5 ms 时间差对应半周期相位关系；再加一个完整周期，纯音的稳态相位关系可能重复。宽带信号包含多个频率，各分量不能同时按相同周期重复，因此宽带延迟与某频率的反相不可互换。

实现整数样本延迟时，最小步长为 $1/f_s$ 秒；所需延迟若不为整数样本，可采用合适的分数延迟方法，并检查其幅频和相位误差。左右分别处理产生的固定延迟，也应计入最终 ITD。

研究双耳策略时，频位匹配、ILD 与同步应同时验证。如果一个条件更偏向一耳，应先检查输入不对称，再讨论时域编码。[5](#ref-kan-2013 "Effect of mismatched place-of-stimulation on binaural fusion and lateralization in bilateral cochlear-implant users")

## 研究沿革

动物神经研究提出低频空间信息的群体编码证据。2013 年正常听力模拟及真实双侧植入者研究考察跨耳位置失配与侧化；2020 年 TLE 声码器研究进一步测试时域编码。物种、接口和任务的差别构成各结论的适用边界。[3](#ref-mcalpine-2001 "A neural code for low-frequency sound localization in mammals") [4](#ref-goupell-2013 "Effect of mismatched place-of-stimulation on the salience of binaural cues in conditions that simulate bilateral cochlear-implant listening") [5](#ref-kan-2013 "Effect of mismatched place-of-stimulation on binaural fusion and lateralization in bilateral cochlear-implant users") [1](#ref-wan-itd-2020 "Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder")
