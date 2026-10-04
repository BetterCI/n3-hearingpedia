---
title: "音高感知"
english: "Pitch perception"
slug: "pitch-perception"
summary: "连接时间音高、位置音高和音高辨别任务。"
categories: ["psychoacoustics","neuroscience"]
tags: ["Pitch perception"]
aliases: []
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zhou-tle-2022","wang-ditone-2022","zeng-2008","glasberg-1990","oxenham-2004","hartmann-1990","zhou-f0intfs-2023"]
order: 10
knowledge_area: "perception"
kind: "function"
key_facts: [{"label":"性质","value":"知觉属性"},{"label":"相关线索","value":"谐波位置、时间周期性与跨带信息"},{"label":"任务","value":"辨别、排序、匹配、音程与旋律"}]
---

**音高感知**（pitch perception）是听者把声音组织在较高或较低等维度上的知觉过程。对于周期复合音，音高常与[基频](../fundamental-frequency/)相关，却不要求声音包含实际基频分量。频谱位置、谐波可分辨性和时间信息共同约束不同任务。[5](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception")

## 定义与分类

音高是知觉属性，[基频](../fundamental-frequency/)是物理量，响度与音色则是另外的感知维度。纯音、谐波复合音和调幅音可提供不同线索；辨别、排序和旋律任务又测量不同能力。用一个刺激频率差替代感知音高差，会忽略匹配与判断的实际结果。

## 原理与表征

### 时间线索与位置线索

周期性声刺激提供重复间隔，听觉系统也能利用不同频率激活[耳蜗](../cochlea/)位置的差别。前者常称时间音高线索，后者联系[频位映射关系](../tonotopy/)。[人工耳蜗](../cochlear-implant/)中，刺激电极的位置、脉冲的时间安排以及它们的相互作用都会影响音高判断。[3](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

一个谐波复合音即使没有基频分量，也可能产生接近其共同周期对应频率的音高。这个例子说明，音高并不总由频谱中最低的实际分量决定。

### 三类任务分别回答什么

音高辨别问“两声是否不同”或“哪一个更高”；音高排序要求把多个刺激排出次序；音高匹配寻找与参考刺激相似的音高。声调识别还涉及语言类别和其他声学线索，不能与这些任务互换。

若参考频率为 $f$，可辨别的频率变化为 $\Delta f$，研究常报告相对差别 $\Delta f/f$。音程也可写成：

$$
d=12\log_2\left(\frac{f_2}{f_1}\right).
$$

$d$ 的单位为半音，$f_1,f_2$ 为正频率，单位相同。这是刺激差异的尺度，不是听者必然能分辨的阈值。

### 相关研究提供的线索

TLE 论文用音高辨别与排序考察时间信息转换，并显示效果依赖刺激频率与任务；不能把某个实验的优势推广到全部音高或音乐感知。[1](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")

DiTone 研究分别操纵基频与响度轮廓，提示普通话声调识别中需要检查线索依赖。识别出正确声调，并不足以证明植入者获得了准确的基频音高。[2](#ref-wang-ditone-2022 "Cochlear-implant Mandarin tone recognition with a disyllabic word corpus")

### 可分辨与不可分辨谐波

复合音中的谐波间距为 $F_0$。当[听觉滤波器](../auditory-filter/)足够窄时，较低阶谐波可分别形成响应峰；当多个谐波落入同一通道，其相互作用会产生以 $F_0$ 为周期的包络。前者提供较明确的频谱结构，后者提供通道内的时间周期性。二者的相对作用随频率、带宽和声级变化。[4](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

“缺失基频”复合音没有实际 $F_0$ 分量，却仍可能引发对应音高。它说明感知可从多个分量推断共同周期，并不要求听觉系统在低频处找到一个真实谱峰。它也不能单独证明唯一的空间模型或时间模型。

### 人工耳蜗结果的层次

TLE 的真实植入者研究按频率和任务评价音高，不应把某个任务的收益扩展为全部音乐能力恢复。[1](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants") F0inTFS 以声学模拟检验周期性增强，不能视为同样强度的临床证据。[7](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants") 有区分力的后续研究应同时报告个体配对变化、任务间一致性和适应时间。

## 测量与研究方法

### 测量音高时究竟测什么

辨别任务回答两个声音是否不同；排序回答哪个更高；匹配要求调整比较声；旋律识别还依赖记忆、音程关系和任务经验。正确率高不一定意味着音高自然或稳定，排序正常也不保证精细音程准确。

频率差可报告为相对变化 $\Delta f/f$，或半音差：

$$
\Delta s=12\log_2\frac{f_2}{f_1}.
$$

该量描述刺激频率关系。若要讨论感知音高差，需有相应行为测量。两个音相差一倍频程时 $\Delta s=12$；这不意味着每位人工耳蜗听者都将它感为准确的十二半音。

### 如何排除非音高线索

音高实验应考虑响度平衡或小幅声级随机化、频谱范围、刺激时长和起止包络。若比较复合音，只改变 $F_0$ 可能同时改变最外侧谐波、谐波数量和谱重心，听者可能使用这些线索判断。控制措施也会改变可用信息，因此需要报告具体设计。

位置不匹配的移置刺激研究支持时间与位置相协调的重要性。[5](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception") 谐波轻微失谐的研究则提供了观察音高与声音分组如何共同变化的实验入口。[6](#ref-hartmann-1990 "Hearing a mistuned harmonic in an otherwise periodic complex tone")

## 应用与解释边界

### 实验记录与边界

记录刺激类型、响度匹配、频率或电极变化、呈现顺序和任务规则。若更高的频率同时更响，反应可能部分来自响度线索。

## 分析示例

### 解释示例：没有基频分量的音高

考虑 400、600、800 Hz 三个等间隔分量，它们是 200 Hz 的第 2、3、4 谐波。声谱中没有 200 Hz 峰，听者仍可能感到相应周期的音高。是否得到稳定判断，还受相位、带宽、可分辨性和任务影响；教学示例不等于对所有人的测量结果。

若把三个分量统一上移 50 Hz，得到的关系不再是原来 200 Hz 的严格整数倍。音高是否及如何变化可用于研究谱结构与时间规律，但不能简单宣布增加的 50 Hz 就是感知音高变化。

对于人工耳蜗，应分别考察频谱位置和脉冲时间线索。两声音可被辨别但无法稳定排序时，说明存在可察觉差异，尚不证明形成了可靠的高低音高维度。[5](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception")

## 研究沿革

复杂音高研究通过缺失基频、移置时间线索与失谐谐波等刺激约束候选机制。2004 年位置相关研究支持时间与位置共同考虑；人工耳蜗研究进一步检验特定编码在辨别和排序任务中的作用。这里的发展线索不意味着已经确立单一、普适的音高模型。[5](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception") [6](#ref-hartmann-1990 "Hearing a mistuned harmonic in an otherwise periodic complex tone") [1](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")
