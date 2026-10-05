---
title: "音高感知"
english: "Pitch Perception"
slug: "pitch-perception"
summary: "听觉系统从频谱位置、谐波结构、神经时间信息和上下文中形成高低、周期性与旋律相关知觉的过程；音高不是频率或基频本身。"
categories: ["psychoacoustics","neuroscience"]
tags: ["pitch","fundamental-frequency","resolved-harmonics","temporal-coding","place-coding","phase-locking","cochlear-implant"]
aliases: ["pitch","音调感知","音高知觉","F0 pitch","periodicity pitch"]
batch: 2
status: "draft"
last_updated: "2026-10-05"
literature_checked_at: "2026-10-05"
authors: ["AI 辅助重构"]
illustration: {"src":"figures/pitch-coding-hierarchy.svg","alt":"从声学结构、耳蜗滤波、听神经 place 和 phase locking 到听觉皮层与音高知觉的层级示意","caption":"音高并非由单一声学变量或单一神经机制直接读取，而是在多个层级整合 place、timing、harmonic pattern 与上下文后形成。"}
references: ["oxenham-pitch-2023","glasberg-1990","oxenham-2004","hartmann-1990","abrams-pitch-cortex-2025","fung-pitch-development-2025","reiss-ci-pitch-2019","carlyon-ci-temporal-2025","degroote-ci-pitch-2025","berg-ci-music-2025","zeng-2008","zhou-tle-2022","wang-ditone-2022","zhou-f0intfs-2023","li-covarying-2025"]
order: 10
knowledge_area: "perception"
kind: "function"
key_facts:
  - {label: "本质", value: "知觉属性，不等于 frequency 或 F0"}
  - {label: "主要线索", value: "cochlear place、harmonic pattern、phase locking 与 envelope periodicity"}
  - {label: "经典现象", value: "missing fundamental、resolved / unresolved harmonics"}
  - {label: "神经前沿", value: "多线索在皮层形成可泛化表征，并受上下文与预测调节"}
  - {label: "CI 难点", value: "place、rate、AM 和 neural interface 提供不完整且有时相互冲突的音高线索"}
---

**音高感知**（pitch perception）是听觉系统把声音组织为“高—低”、周期性、旋律与声源身份等知觉维度的过程。对周期复合音而言，音高常与[基频](../fundamental-frequency/)（fundamental frequency, $F_0$）密切相关，但 **pitch 是知觉，frequency 和 $F_0$ 是物理描述**，三者不能互换。[1](#ref-oxenham-pitch-2023 "Questions and controversies surrounding the perception and neural coding of pitch")

现代心理声学和神经科学越来越支持一种更谨慎的观点：音高不是由耳蜗位置、神经时间间隔或某一个“pitch center”单独决定，而是由**频谱位置、谐波结构、神经 phase locking、跨通道关系和上下文预测共同约束的多层表征**。[1](#ref-oxenham-pitch-2023 "Questions and controversies surrounding the perception and neural coding of pitch")

![音高编码层级](/n3-hearingpedia/figures/pitch-coding-hierarchy.svg)

## 音高到底是什么

### Pitch height

表示音高在低到高轴上的位置。

### Pitch salience

表示音高是否清晰、稳定、容易判断。两个刺激即使 nominal $F_0$ 相同，也可能具有完全不同的 pitch salience。

### Pitch chroma 与音程

音乐中还涉及 octave equivalence、音级类别和相对音程等更高层结构，不能由一次简单的 frequency discrimination 代表。

### 可辨别不等于“真的听到音高”

两个刺激可以被区分，并不代表听者一定使用 pitch。频谱重心、响度、粗糙度或起止包络也可能支持正确反应。

因此需要区分：

**difference detection → high/low ordering → pitch matching → interval/melody → naturalness**

这些是不同层级的任务。

## 从纯音到复杂音：为什么音高不是“最低频率”

### 纯音

对于单一正弦波，物理 frequency 与 pitch 通常高度相关，因此纯音是 frequency discrimination 的经典刺激。

### 谐波复合音

若成分满足：

$$
f_n=nF_0,qquad n=1,2,3,ldots
$$

听者通常会形成接近 $F_0$ 的整体音高。

### Missing fundamental

即使删除实际 $F_0$ 分量，只保留：

$$
2F_0, 3F_0, 4F_0,ldots
$$

听者仍可感到接近 $F_0$ 的 pitch。

因此：

> **音高不是在频谱中寻找最低实际分量。**

听觉系统可以从多个成分之间的共同结构推断一个共同周期。[1](#ref-oxenham-pitch-2023 "Questions and controversies surrounding the perception and neural coding of pitch")

## Resolved 与 unresolved harmonics

这是现代 pitch psychophysics 最关键的区分之一。

### Resolved harmonics

低阶谐波间隔相对较大，经过[听觉滤波器](../auditory-filter/)后可在耳蜗形成相对独立的响应峰，因此每个谐波保留较清晰的 place 与 timing information。[2](#ref-glasberg-1990 "Derivation of auditory filter shapes from notched-noise data")

通常它们产生更精确的 $F_0$ discrimination 和更强的 pitch salience。

### Unresolved harmonics

当多个高阶谐波落入同一耳蜗滤波器时，单独谐波的 place pattern 变得模糊，但通道输出会产生与 $F_0$ 相关的 **temporal-envelope periodicity**。

因此 unresolved harmonics 并不是“没有 pitch information”，而是依赖不同的线索组合。

2025 年儿童研究在 400 Hz $F_0$ 条件下发现：儿童和成人都表现出 resolved 条件优于 unresolved 条件；8–9 岁儿童整体阈值较高，而 10–11 岁组在所测条件下接近成人。[6](#ref-fung-pitch-development-2025 "Pitch perception in school-aged children: Pure tones, resolved and unresolved harmonics")

这提示 pitch 还具有明显的**发育维度**。

## Place code、temporal code 还是两者结合

### Place / place-pattern coding

[耳蜗](../cochlea/)具有明确的[频位映射关系](../tonotopy/)。不同频率产生不同空间激活模式，因此 place code 是 pitch 的天然候选机制。

对于 resolved harmonics，多个低阶谐波还可形成稳定的 harmonic place pattern。

### Temporal / phase-locking coding

听神经放电在一定频率范围内会随刺激周期出现 phase locking，使 interspike interval 和群体时间结构包含周期信息。

但人类 perceptual pitch 所需要的 phase-locking 上限到底在哪里、哪些 timing information 真正被中枢读取，以及 place 与 timing 各自的必要性，仍没有完全解决。[1](#ref-oxenham-pitch-2023 "Questions and controversies surrounding the perception and neural coding of pitch")

### Place–time / spectrotemporal coding

越来越多模型不再把 place 与 time 当成非此即彼，而认为自然 pitch 很可能使用**跨通道的时空联合结构**。

Oxenham 等的移置刺激研究尤其重要：如果把 temporal pitch information 放到不符合自然 tonotopy 的位置，复杂音高明显受损，说明 timing 不能完全脱离 place 来解释。[3](#ref-oxenham-2004 "Correct tonotopic representation is necessary for complex pitch perception")

因此目前最稳妥的表述是：

> **正常音高依赖 place、timing 与 harmonic relationship 的条件性整合，而不是单一万能代码。**

## 从外周到皮层：音高表征越来越抽象

耳蜗和听神经首先把声音展开成频率相关的群体活动与时间结构，但 pitch percept 最终必须具有一定 **cue invariance**：

- 有实际 $F_0$ 和 missing fundamental 可以产生相似 pitch；
- 不同 timbre 可以具有同样的 pitch；
- 不同声学实现可以落到相同的音高类别。

2025 年 Abrams 等用 MEG 比较纯音、missing-fundamental complex 和 cue-ambiguous stimuli，发现不同刺激类型可以在双侧 low-to-mid auditory cortex 与 sensorimotor cortex 中形成能够**跨 cue type 泛化**的 pitch representation，并表现出右侧优势。[5](#ref-abrams-pitch-cortex-2025 "Dynamics of Pitch Perception in the Auditory Cortex")

更重要的是，可预测上下文会使歧义刺激的 pitch representation 更早出现。[5](#ref-abrams-pitch-cortex-2025 "Dynamics of Pitch Perception in the Auditory Cortex")

这意味着现代 pitch neuroscience 已经不只是“place vs timing”，还要考虑：

**bottom-up evidence + cortical integration + expectation**

共同决定音高何时形成。

## Pitch 与 auditory object formation

音高不仅用于判断高低，还参与复杂声景中的对象形成和跟踪。

不同 $F_0$ 可以帮助：
- 分离同时说话的人；
- 跟踪目标 voice；
- 形成 harmonic auditory object；
- 维持旋律线；
- 识别语调和情绪。

因此 pitch deficit 可能进一步影响[听觉注意](../auditory-attention/)和多声源 scene segregation。

## 轻微失谐为什么重要

如果一个谐波偏离严格整数倍关系，它可能同时改变整体 pitch，并逐渐从原来的 harmonic object 中“跳出”。

Hartmann 等的 mistuned-harmonic 实验说明，pitch judgement 与 auditory grouping 可以被系统操纵。[4](#ref-hartmann-1990 "Hearing a mistuned harmonic in an otherwise periodic complex tone")

## 怎样测量音高

### Frequency / F0 discrimination

可报告：

$$
rac{Delta f}{f}
$$

或：

$$
rac{Delta F_0}{F_0}
$$

但阈值好不保证形成自然 pitch。

### Pitch ranking

要求多个刺激形成稳定高低次序。对人工耳蜗尤其重要，因为有些刺激“可分辨”，却不能稳定排列在单一高低轴上。

### Pitch matching

用于跨耳、跨电极或 acoustic–electric comparison。

### Interval 与 melody

若两个频率为 $f_1$、$f_2$：

$$
Delta s=12log_2left(rac{f_2}{f_1}ight)
$$

$Delta s$ 是物理半音差，不等于主观 pitch distance。

### Pitch salience

越来越值得直接测量“这个 pitch 有多清晰、稳定”，而不只是正确率。

## 怎样排除非音高线索

严谨实验常需要：
- level roving 或 loudness balancing；
- harmonic-number roving；
- random starting phase；
- masking distortion products；
- 控制 spectral centroid；
- 控制 duration 与 onset；
- 使用多种任务交叉验证。

例如 resolved/unresolved harmonic 实验若不 rove lowest harmonic number，受试者可能依赖单独频率成分，而不是 $F_0$ pitch。[6](#ref-fung-pitch-development-2025 "Pitch perception in school-aged children: Pure tones, resolved and unresolved harmonics")

## 听力损失怎样改变音高

[听力损失](../hearing-loss/)可通过多个途径改变 pitch：
- auditory filter 变宽，降低 harmonic resolvability；
- 高低频可听性变化；
- cochlear dead region；
- cochlear nonlinearity 改变；
- neural temporal fidelity 改变；
- 长期 cue reweighting。

所以 pitch deficit 不只是“frequency discrimination 变差”。

## 人工耳蜗中的音高感知

人工耳蜗是检验 pitch mechanism 最有价值的“自然实验”之一，因为它可以在一定程度上独立操纵**刺激位置**与**刺激时间**。[7](#ref-reiss-ci-pitch-2019 "Place and Temporal Cues in Cochlear Implant Pitch and Melody Perception")

![人工耳蜗中的音高线索](/n3-hearingpedia/figures/ci-pitch-cues.svg)

### Place pitch

一般而言，更 basal 的电极往往产生更高 pitch，更 apical 的电极往往产生更低 pitch。

但 electric place pitch 不等于自然 cochlear frequency，因为它同时受到：
- 电极数量有限；
- current spread；
- electrode-to-modiolus distance；
- scalar location；
- neural survival；
- spiral-ganglion map；
- frequency–place mismatch

影响。[11](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

长期使用还可能产生 perceptual adaptation，所以开机初期的 acoustic–electric match 不一定是最终稳定 mapping。

### Temporal / rate pitch

在固定电极上提高 pulse rate，许多 CI 用户在低至中等速率下会报告 pitch 上升。

但最突出的限制是：

> **随着 pulse rate 升高，pitch growth 往往减弱、饱和或变得不稳定。**

2025 年 Carlyon 等的多作者综述指出，这种 temporal pitch deficit 即使在绕过临床处理器、直接电刺激时仍存在，因此不能简单归因于 coding strategy；auditory-nerve adaptation、神经群体同步、中枢 readout 和可塑性都可能参与。[8](#ref-carlyon-ci-temporal-2025 "Limitations on Temporal Processing by Cochlear Implant Users: A Compilation of Viewpoints")

### 为什么 200–300 pps 是重要范围

它不是每个人的硬上限，但很多 CI rate-pitch 实验发现：
- 低至中等 rate 下，pitch 随 rate 增加；
- 到数百 pps 后，增长明显变弱；
- 个体差异很大。

2025 年 de Groote 等在 8 名 MED-EL 用户中同时刺激四个最 apical 电极；当所有电极使用相同速率时，pitch ranking 随 rate 增加到约 **200–300 pps**，把单电极结果推进到了更接近真实策略的 multi-channel 情境。[9](#ref-degroote-ci-pitch-2025 "Temporal Pitch Perception of Multi-Channel Stimuli by Cochlear-Implant Users")

### AM pitch 与 pulse-rate pitch

CI 中 temporal information 至少可以通过两条路径变化：

1. 改变 pulse rate；
2. 在较高 carrier rate 上改变 amplitude-modulation rate。

两者都可能产生 pitch-related percept，但神经同步、幅度波动和 loudness interaction 并不相同，因此不应都笼统称为同一个“temporal pitch”。

### Place 与 temporal cues 并不总能合成一条统一音高轴

如果同时改变 electrode place 与 pulse rate，听者未必能把所有刺激无缝排成一个单一高低次序。

这提示 CI 的 place cue 和 temporal cue 可能只是部分融合。[7](#ref-reiss-ci-pitch-2019 "Place and Temporal Cues in Cochlear Implant Pitch and Melody Perception")

### 电极位置与个体化编程

2025 年 Berg 等研究 50 名成人 CI 用户，发现 electrode placement variables 与 pitch、melody 和 timbre outcome 存在关联；其中 34 人进一步接受 image-guided programming，部分音乐感知指标改善。[10](#ref-berg-ci-music-2025 "Cochlear Implant Electrode Placement and Music Perception")

这支持一个重要方向：

> **未来 pitch fitting 可能需要把 CT electrode position、channel interaction 与 psychophysics 联合起来。**

但现有证据仍不足以证明一种 image-guided map 对所有用户都优于标准 map。

### 新编码策略怎样增强 temporal pitch

研究方向包括：
- rate coding；
- low-frequency synchronized stimulation；
- pulse-rate modulation；
- AM–rate covariation；
- apical/low-frequency emphasis；
- place–time coordinated coding。

TLE 的真实植入者研究显示，特定时域编码可以改变 pitch discrimination 与 ranking，但效果依赖刺激频率和任务。[12](#ref-zhou-tle-2022 "Pitch Perception With the Temporal Limits Encoder for Cochlear Implants")

F0inTFS 通过声学模拟增强 periodicity information，提供算法可行性证据，但不能直接等同于真实 CI 用户获益。[14](#ref-zhou-f0intfs-2023 "F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants")

协变 AM frequency 与 pulse rate 的探索性研究提示，多 temporal dimension 联合变化可能优于单一 rate cue；目前该结果仍属于预印本证据，应等待同行评审和独立重复。[15](#ref-li-covarying-2025 "Covarying Amplitude Modulation and Pulse Rate Enhances Pitch Discrimination in Cochlear Implant Users")

### 声调语言与音乐

普通话 lexical tone 高度利用 $F_0$ contour，但同时可利用 duration、intensity、voice quality 与 lexical context。

DiTone 等研究通过分离 $F_0$ 和 loudness contour 显示，CI 用户可能重新分配线索权重。[13](#ref-wang-ditone-2022 "Cochlear-implant Mandarin tone recognition with a disyllabic word corpus")

因此：

> **tone recognition 正确不等于正常 F0 pitch 已恢复。**

音乐则要求更精细的 interval、stable ordering、melody contour 与 harmonic relation，所以即使安静语音表现很好，CI music pitch 仍可能明显受限。

## 音高感知中的可塑性与上下文

pitch representation 会受到：
- developmental maturation；
- musical experience；
- hearing loss；
- CI map；
- acoustic–electric mismatch；
- long-term device use；
- context and expectation

影响。

2025 年皮层研究进一步显示，predictable context 可改变 ambiguous pitch representation 出现的时间，这提示 pitch generation 包含动态预测加工，而不是完全 feedforward。[5](#ref-abrams-pitch-cortex-2025 "Dynamics of Pitch Perception in the Auditory Cortex")

## 当前前沿研究问题

### 1. Place 与 temporal information 最终在哪里整合？
听神经、脑干、中脑和皮层分别承担什么计算？

### 2. 人类 phase locking 的功能上限在哪里？
动物神经生理、人体 FFR 与行为结果怎样统一？

### 3. 为什么 resolved harmonics 的 pitch 更显著？
是 place pattern 更可靠，还是跨通道 temporal structure 更容易被读取？

### 4. 是否存在真正 cue-invariant 的 cortical pitch representation？
2025 年 MEG 支持跨线索泛化，但其精确解剖位置和因果作用仍待确定。[5](#ref-abrams-pitch-cortex-2025 "Dynamics of Pitch Perception in the Auditory Cortex")

### 5. Context 与 prediction 在 pitch 形成中扮演什么角色？
音高多大程度是“读出”，多大程度是“推断”？

### 6. 听力损失后 cue weighting 怎样改变？
harmonic resolvability、TFS、envelope 与 place 会不会发生系统性重权重？

### 7. CI temporal pitch 的上限由什么决定？
auditory-nerve adaptation、neural survival、current spread、中枢 readout 与经验分别贡献多少？

### 8. Apical stimulation 是否具有 temporal advantage？
更顶端、更低频的电刺激能否扩大可用 rate-pitch range？

### 9. Place–rate coordinated coding 能否建立更自然的单一 pitch axis？
未来策略可能需要让“刺激哪里”和“刺激多快”遵循一致的自然耳蜗规律。

### 10. 个体化影像与神经指标能否真正改善 pitch fitting？
CT、ECAP、pitch match 与长期 adaptation 应怎样联合？

### 11. Speech、tone language 与 music 是否需要不同 pitch optimization？
最适合普通话声调的 map 未必最适合旋律。

## 与其他词条的关系

建议继续阅读：

- [基频](../fundamental-frequency/)：$F_0$ 是物理参数，pitch 是知觉；
- [谐波性](../harmonicity/)：谐波结构怎样支持 pitch 与 auditory object；
- [听觉滤波器](../auditory-filter/)：resolved / unresolved harmonics 的基础；
- [耳蜗](../cochlea/) 与 [频位映射](../tonotopy/)：place code 的外周来源；
- [时域精细结构](../temporal-fine-structure/) 与 [时域包络](../temporal-envelope/)：不同 temporal cues；
- [人工耳蜗](../cochlear-implant/)：electric place 与 temporal coding 的接口；
- [时间限度编码](../temporal-limits-encoder/)：增强 temporal pitch 的策略之一；
- [普通话声调](../mandarin-lexical-tone/)：pitch information 的语言功能；
- [听觉可塑性](../auditory-plasticity/)：长期 map 与 cue weighting；
- [听觉注意](../auditory-attention/)：pitch 如何参与声源选择与分组。

## 研究沿革

Pitch science 已从早期的 frequency/place 与 periodicity/time 之争，逐渐发展为一个**多层、跨线索、动态整合问题**。

今天更准确的问题不是“pitch 到底由 place 还是 time 编码”，而是：

> **在什么刺激条件、神经层级和行为任务下，哪些线索最可靠；大脑又如何把这些不完全相同的线索整合成一个稳定的 pitch percept？**

人工耳蜗进一步把自然耳蜗中紧密耦合的 place、timing 与 harmonic structure 部分拆开，因此 CI pitch 不只是康复难题，也是检验人类音高机制最有价值的实验窗口之一。
