---
title: "混淆矩阵"
english: "Confusion matrix"
slug: "confusion-matrix"
summary: "用普通话辅音识别解释刺激和反应之间的系统混淆。"
categories: ["speech"]
tags: ["Confusion matrix","组内文献"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"speech-intelligibility","relation":"prerequisite"},{"slug":"mandarin-lexical-tone","relation":"related"}]
references: ["zhou-consonants-2026","zhou-consonants-2023"]
order: 20
---

## 一句话理解

混淆矩阵记录每种刺激被回答成各类别的次数。它让我们看到错误如何分布，而不仅是总体答对了多少。

## 行、列与归一化

本词条约定行是实际刺激、列是受试者反应。若第 $i$ 类刺激被回答为第 $j$ 类的次数为 $C_{ij}$，行归一化为：

$$
P_{ij}=\frac{C_{ij}}{\sum_j C_{ij}}.
$$

$P_{ij}$ 是无量纲比例，某行没有试次时不能直接计算。对角项代表正确识别，非对角项代表具体混淆。若各刺激呈现次数不同，总正确率应按实际试次计算：

$$
\mathrm{Accuracy}=\frac{\sum_i C_{ii}}{\sum_i\sum_j C_{ij}}.
$$

对角比例的简单平均属于类别平均正确率，可能与总正确率不同。论文也可能把反应放在行上，读图前必须确认。

## 一个辅音例子

两组受试者可能具有相同正确率，一组主要混淆送气与不送气，另一组主要混淆发音部位。这两种模式对应不同的后续假设。例子用于说明矩阵价值，并不是共同论文某一张图的原始结果。

比较矩阵时，要固定刺激列表、响应选项、噪声条件和计分单位。合并多位受试者可能掩盖个体差异，最好同时提供个体与汇总结果。

## 共同论文如何扩展分析

2023 年会议论文考察听力损失与放大对普通话辅音识别的影响，混淆模式为理解不同辅音的困难提供入口。[Zhou 等，2023](#ref-zhou-consonants-2023)

2026 年人工耳蜗论文进一步使用聚类、多维尺度分析和特征信息分析描述辅音的感知组织。其结果是特定刺激与任务中的行为结构，不应直接解释为神经表征的维数。[Zhou 等，2026](#ref-zhou-consonants-2026)

## 边界与更新重点

稀少试次可能造成不稳定的非对角比例；猜测与响应偏好也会影响模式。后续将解释 MDS 的距离构建、聚类稳定性与特征信息传递，保留归一化方式、试次数和误差来源，而不只展示一张颜色漂亮的矩阵。
