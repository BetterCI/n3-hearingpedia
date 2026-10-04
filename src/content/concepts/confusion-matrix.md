---
title: "混淆矩阵"
english: "Confusion matrix"
slug: "confusion-matrix"
summary: "用普通话辅音识别解释刺激和反应之间的系统混淆。"
categories: ["research-methods","speech"]
tags: ["Confusion matrix"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zhou-consonants-2026","zhou-consonants-2023","shannon-1948","miller-1955"]
order: 20
knowledge_area: "methods"
kind: "analysis"
key_facts: [{"label":"本文方向","value":"行＝刺激类别，列＝反应类别"},{"label":"数据形式","value":"计数、条件比例或联合概率"},{"label":"用途","value":"分析正确识别、错误分布与偏置"}]
---

**混淆矩阵**（confusion matrix）是按真实类别与反应类别组织计数或比例的数据表。听觉实验中可用它描述声调、辅音等识别的错误模式；机器学习中也用于分类评价。矩阵方向、归一化和类别比例必须注明。[4](#ref-miller-1955 "An Analysis of Perceptual Confusions Among Some English Consonants")

## 定义与分类

混淆矩阵是数据组织方式，正确率和互信息是由数据计算的指标，聚类或多维尺度则是分析方法。行归一化适于查看给定刺激的反应，联合概率保留输入比例。不同结果不能因来自同一张表就自动具有同样解释；低维图更不能直接当作神经编码维度。

## 原理与表征

### 行、列与归一化

本词条约定行是实际刺激、列是受试者反应。若第 $i$ 类刺激被回答为第 $j$ 类的次数为 $C_{ij}$，行归一化为：

$$
P_{ij}=\frac{C_{ij}}{\sum_j C_{ij}}.
$$

$P_{ij}$ 是无量纲比例，某行没有试次时不能直接计算。对角项代表正确识别，非对角项代表具体混淆。若各刺激呈现次数不同，总正确率应按实际试次计算：

$$
\mathrm{Accuracy}=\frac{\sum_i C_{ii}}{\sum_i\sum_j C_{ij}}.
$$

对角比例的简单平均属于类别平均正确率，可能与总正确率不同。论文也可能把反应放在行上，读图前必须确认。

### 一个辅音例子

两组受试者可能具有相同正确率，一组主要混淆送气与不送气，另一组主要混淆发音部位。这两种模式对应不同的后续假设。例子用于说明矩阵价值，并不是所引论文某一张图的原始结果。

比较矩阵时，要固定刺激列表、响应选项、噪声条件和计分单位。合并多位受试者可能掩盖个体差异，最好同时提供个体与汇总结果。

### 行归一化与总体概率不能混用

令 $C_{ij}$ 为真实类别 $i$ 被答成 $j$ 的次数。行归一化 $P(j\mid i)=C_{ij}/\sum_jC_{ij}$ 回答某刺激被如何识别；总体联合概率 $p_{ij}=C_{ij}/N$ 则保留类别出现比例。输入类别不平衡时，两个量不同。

总正确率为 $\sum_iC_{ii}/N$；先算每类正确率再平均，得到的是类别等权指标。报告矩阵时必须注明行列方向、计数还是比例，以及是否包含漏答，不能仅凭色深解释差异。

### 信息量是一种补充描述

在刺激与反应类别定义明确时，互信息可写为：

$$
I(S;R)=\sum_{i,j}p_{ij}\log_2\frac{p_{ij}}{p_i p_j}.
$$

$p_i=\sum_jp_{ij}$、$p_j=\sum_ip_{ij}$，零概率项按极限记为零，单位为 bit。若 $K$ 类输入等概率，输入熵为 $\log_2K$；输入不均匀时应计算实际熵。此式属于信息论描述，不表示大脑实际用多少 bit 编码。[3](#ref-shannon-1948 "A Mathematical Theory of Communication")

有限样本会造成估计偏差，尤其在类别很多、每格次数很少时。不同类别数或先验比例下的原始互信息也不能直接比较。重复测量与个体差异应通过适当统计框架处理，不宜把所有听者合并后忽略来源。

### 从类别错误到语音特征

辅音研究可进一步按发音部位、方式或清浊等特征整理混淆，但具体特征体系须与材料对应。经典语音混淆研究提供历史入口；本词条不从仅核对的书目中复现原始矩阵数值。[4](#ref-miller-1955 "An Analysis of Perceptual Confusions Among Some English Consonants")

[人工耳蜗](../cochlear-implant/)辅音研究结合聚类和多维尺度分析描述混淆结构。[1](#ref-zhou-consonants-2026 "Perceptual organization of Mandarin consonants in cochlear implant users") 低维图表示的是行为差异的近似结构，不是对神经编码维度的直接发现；旋转方向和距离尺度也需按模型解释。

## 测量与研究方法

### 相关研究如何扩展分析

2023 年会议论文考察听力损失与放大对普通话辅音识别的影响，混淆模式为理解不同辅音的困难提供入口。[2](#ref-zhou-consonants-2023 "Effects of hearing loss and amplification on Mandarin consonant perception")

2026 年人工耳蜗论文进一步使用聚类、多维尺度分析和特征信息分析描述辅音的感知组织。其结果是特定刺激与任务中的行为结构，不应直接解释为神经表征的维数。[1](#ref-zhou-consonants-2026 "Perceptual organization of Mandarin consonants in cochlear implant users")

### 一个有意义的比较流程

先展示计数与各类试次数，再给归一化矩阵；检查哪些错误在个体中重复出现，并比较相应声学线索。若某类反应偏多，可能是反应偏置而非仅有刺激不可分辨。对于前后或两种策略比较，应保留配对信息，避免把总正确率相同误当作混淆机制相同。

矩阵是描述工具。要解释某个特征缺失造成错误，仍应通过控制刺激、独立辨别任务或针对性处理验证，不能由一张热图直接推出因果机制。

## 应用与解释边界

### 边界与更新重点

稀少试次可能造成不稳定的非对角比例；猜测与响应偏好也会影响模式。

## 分析示例

### 解释示例：反应偏置与可分辨性

若每类刺激次数相等，但听者几乎总选类别 A，矩阵将出现整列较高。A 类的正确率可能很好，其他类别很差；总正确率无法说明这一反应偏置。只看归一化后的对角线，也可能漏掉错误聚集在哪一列。

两种条件比较时可分别看列总量、逐类命中和特定类别对的互相混淆。若某对仅单向混淆，解释可能涉及决策规则和先验，不宜立即认为两个声学表示完全重合。

图形排序也应保持一致。若每张热图按自身聚类重新排列，视觉上的变化可能来自顺序而非数据；用于解释时应标明聚类方法，保留原类别标识和计数。[1](#ref-zhou-consonants-2026 "Perceptual organization of Mandarin consonants in cochlear implant users")

## 研究沿革

1955 年语音混淆论文提供经典研究入口，信息论又提供概率与互信息描述。较新辅音研究结合矩阵、聚类和多维尺度比较感知模式。引用仅核对书目的经典论文时，本词条不复现未读取的原始数值。[4](#ref-miller-1955 "An Analysis of Perceptual Confusions Among Some English Consonants") [3](#ref-shannon-1948 "A Mathematical Theory of Communication") [1](#ref-zhou-consonants-2026 "Perceptual organization of Mandarin consonants in cochlear implant users")
