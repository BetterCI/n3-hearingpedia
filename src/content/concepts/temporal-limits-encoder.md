---
title: "时间限度编码器"
english: "Temporal Limits Encoder"
slug: "temporal-limits-encoder"
summary: "解释将频带时间信息转换到电听觉时间音高范围的策略。"
categories: ["cochlear-implants","signal-processing"]
tags: ["TLE"]
aliases: ["TLE"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["kan-tle-2021","zhou-tle-2022","wan-itd-2020"]
order: 23
knowledge_area: "technology"
kind: "strategy"
key_facts: [{"label":"缩写","value":"TLE"},{"label":"目标","value":"重编码部分频带时间信息"},{"label":"评价","value":"按语音、音高与双耳任务分开"}]
---

**时间限度编码器**（Temporal Limits Encoder，TLE；中文暂用此译名）是研究将部分频带时间信息转换到电听觉可利用范围的声音编码策略。它涉及频带变换及刺激生成，评价覆盖不同人群和任务，不能概括为在全部听觉功能中均有收益。[1](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants")

## 定义与分类

TLE 属于编码策略，[时间精细结构](../temporal-fine-structure/)属于信号表征，[音高](../pitch-perception/)属于感知功能。降低某些频率的异频变换不等于整体时间拉伸，也不等于直接复制声学相位。与[F0inTFS](../f0-in-tfs/)的区别在于转换目标及处理规则，需要逐层比较。

## 原理与表征

### 为什么需要变换时间信息

声学频带中的快速周期结构，不一定处于电听觉可以有效利用的时间范围。TLE 的思路是把部分高频带时间变化转换到较低范围，而不只是把原波形采样成脉冲。变换参数、频带边界和与原包络的组合共同决定最终刺激。[1](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants")

### 下移操作的一个关键关系

原方法中的调制频率可表达为 $f_{\mathrm{shift}}=f_{\mathrm{low}}-f_{\mathrm{lim}}$，其中 $f_{\mathrm{low}}$ 是所处理带的下边界，$f_{\mathrm{lim}}$ 是目标低频界限。乘以余弦后产生和频与差频分量，经适当滤波选出下移部分，原频率 $f$ 可对应 $f-f_{\mathrm{shift}}$。

这一关系帮助理解异频变换，不是完整 TLE 程序。滤波器、相位、幅度处理与事件生成需按原文实现；变换后保留的是经过重编码的时间线索，而不是原频带声学 TFS 的逐点复制。[1](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants")

### 双耳使用时相位尤其重要

两耳独立使用不同的振荡器相位或处理延迟，可能改变原有跨耳关系。因此需要共同时间基准，并检查最终输出的包络、精细结构和事件时序。单耳语音成绩相近不能证明双耳 ITD 也被正确保留。

Wan 等在正常听力[声码器](../vocoder/)条件下比较 ITD 相关表现，属于声学模拟的空间线索证据。[3](#ref-wan-itd-2020 "Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder") 真实双侧设备的同步、接口与频位匹配还需相应实验。

## 应用与解释边界

### 边界与更新重点

转换后的刺激应检查频谱、包络、响度与两耳时序；两耳保持某种相位关系，不等于所有声学时间差原封不动保留。参数首先是研究设置，不是通用临床配置。

### 已有证据应分任务读取

TLE 的真实植入者研究考察音高辨别和排序，结果受到频率及任务影响。[2](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants") 正常听力声学模拟中的语音结果、真实植入者音高结果和双耳侧化结果，不能合并成“已经全面优于现有策略”的结论。

### 最小复现的证据顺序

先对单频和窄带输入检查目标频移，确认非目标分量的抑制；再对语音检查幅度范围、延迟和频带组合。随后在相同映射和可比响度下进行行为比较，保留个体配对数据及训练量。

重要参数的敏感性应单独研究：改变时间范围上限可能增强某些周期线索，也可能改变语音调制；收益需要放在特定任务中寻找。短时改善是否能稳定用于日常听觉，还需要更长适应与使用评价。

## 分析示例

### 解释示例：下移不等于时间缩放

将一个频带的 1000 和 1200 Hz 分量分别下移同一个 800 Hz，得到 200 和 400 Hz；频率间距保持 200 Hz，但原来的频率比例改变。若把整体时间拉长五倍，则变为 200 和 240 Hz，间距和比例变化不同。两种操作不能混称为降低时间频率。

实际 TLE 的变换还受所用频带、滤波和刺激映射约束。这个算例用于识别异频变换，不代表原论文所有通道的参数。[1](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants")

检验策略时应看是否引入新的包络和跨带关系，并用任务确定听者实际利用了什么。对双耳应用，同步变换只是必要检查之一，还需确认原相位关系经过滤波和事件生成后的结果。

## 研究沿革

2020 年声码器 ITD 研究与 2021 年机制论文建立时间信息转换的研究路线，2022 年真实植入者音高工作进一步评价辨别和排序。年份与任务描述展示证据的发展关系，声学模拟和真实电接口仍需分开记录。[3](#ref-wan-itd-2020 "Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder") [1](#ref-kan-tle-2021 "The Temporal Limits Encoder as a Sound Coding Strategy for Bilateral Cochlear Implants") [2](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")
