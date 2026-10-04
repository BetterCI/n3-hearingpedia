---
title: "音高感知"
english: "Pitch perception"
slug: "pitch-perception"
summary: "连接时间音高、位置音高和音高辨别任务。"
categories: ["psychoacoustics"]
tags: ["Pitch perception","组内文献"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"fundamental-frequency","relation":"prerequisite"},{"slug":"tonotopy","relation":"prerequisite"},{"slug":"temporal-fine-structure","relation":"prerequisite"},{"slug":"mandarin-lexical-tone","relation":"related"}]
references: ["zhou-tle-2022","wang-ditone-2022","zeng-2008"]
order: 10
---

## 一句话理解

音高感知是听者把声音判断为“高”或“低”的知觉属性；基频是物理量。音高通常与周期性有关，但不能用一个频率数值替代全部感知结果。

## 时间线索与位置线索

周期性声刺激提供重复间隔，听觉系统也能利用不同频率激活耳蜗位置的差别。前者常称时间音高线索，后者联系频位映射关系。人工耳蜗中，刺激电极的位置、脉冲的时间安排以及它们的相互作用都会影响音高判断。[Zeng 等，2008](#ref-zeng-2008)

一个谐波复合音即使没有基频分量，也可能产生接近其共同周期对应频率的音高。这个例子说明，音高并不总由频谱中最低的实际分量决定。

## 三类任务分别回答什么

音高辨别问“两声是否不同”或“哪一个更高”；音高排序要求把多个刺激排出次序；音高匹配寻找与参考刺激相似的音高。声调识别还涉及语言类别和其他声学线索，不能与这些任务互换。

若参考频率为 $f$，可辨别的频率变化为 $\Delta f$，研究常报告相对差别 $\Delta f/f$。音程也可写成：

$$
d=12\log_2\left(\frac{f_2}{f_1}\right).
$$

$d$ 的单位为半音，$f_1,f_2$ 为正频率，单位相同。这是刺激差异的尺度，不是听者必然能分辨的阈值。

## 共同论文提供的线索

TLE 论文用音高辨别与排序考察时间信息转换，并显示效果依赖刺激频率与任务；不能把某个实验的优势推广到全部音高或音乐感知。[Zhou 等，2022](#ref-zhou-tle-2022)

DiTone 研究分别操纵基频与响度轮廓，提示普通话声调识别中需要检查线索依赖。识别出正确声调，并不足以证明植入者获得了准确的基频音高。[Wang 等，2022](#ref-wang-ditone-2022)

## 实验记录与边界

记录刺激类型、响度匹配、频率或电极变化、呈现顺序和任务规则。若更高的频率同时更响，反应可能部分来自响度线索。后续将补充时间音高上限、位置音高匹配及音乐任务；这些上限随个体和范式变化，不作为统一的设备调节数值。
