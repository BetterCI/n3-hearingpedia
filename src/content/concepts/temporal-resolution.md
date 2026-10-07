---
title: "时域分辨率"
english: "Auditory temporal resolution"
slug: "temporal-resolution"
summary: "系统介绍间隙检测、调制检测和顺序辨别，解释带宽、声级、可听度及听觉状态的影响，并提供计算模型与公开代码。"
categories: ["psychoacoustics", "neuroscience", "speech"]
tags: ["时域分辨率"]
aliases: ["听觉时间分辨率", "时域分辨能力", "temporal resolution"]
status: "draft"
depth: "in-depth"
last_updated: "2026-10-07"
literature_checked_at: "2026-10-07"
authors: ["AI 辅助编写"]
knowledge_area: "perception"
kind: "function"
key_facts: [{"label": "常见指标", "value": "间隙检测阈与调制检测阈"}, {"label": "主要条件", "value": "带宽、声级、标记声及任务判据"}, {"label": "关键区分", "value": "信号时域特征与行为检测能力"}]
references: ["temporal-resolution-moore", "temporal-resolution-efficient", "temporal-resolution-dau-i", "temporal-resolution-shailer", "temporal-resolution-neural", "temporal-resolution-speech", "temporal-resolution-forrest", "temporal-resolution-viemeister", "temporal-resolution-musicians2025", "temporal-resolution-integration", "temporal-resolution-phase", "temporal-resolution-gin", "temporal-resolution-unilateral", "temporal-resolution-dau-ii", "temporal-resolution-ewert", "temporal-resolution-review", "temporal-resolution-age", "temporal-resolution-position2026", "temporal-resolution-levitt", "temporal-resolution-shannon", "temporal-resolution-regev-jasa", "temporal-resolution-regev2025", "temporal-resolution-amt-dau", "temporal-resolution-amt-ewert", "temporal-resolution-amt-source", "temporal-resolution-tinnitus2025", "temporal-resolution-ginage"]
batch: 3
order: 50
---

**时域分辨率**是听觉系统辨别声音中短暂中断、快速幅度变化及其他短时结构的能力。听者能否发现持续噪声中的短暂停顿，能否察觉声音的强弱起伏，都是研究这种能力的常见切入点。但这些任务并不共享一个可以直接互换的“最短时间”：声音的频谱、声级、持续时间，以及要求听者检测变化还是判断顺序，都会改变测量结果。[1](#ref-temporal-resolution-moore)[2](#ref-temporal-resolution-efficient)

时域分辨率与[时域包络](../temporal-envelope/)和[时域精细结构](../temporal-fine-structure/)密切相关，但概念层次不同。包络与精细结构描述声音及其内部表征的变化形式；时域分辨率描述听者在特定任务中利用这些变化的能力。一个信号可以保留快速起伏，却因强度不足、掩蔽或加工环节的限制而难以被辨别；检测到包络变化，也不等于能准确理解言语或判断声源位置。[1](#ref-temporal-resolution-moore)[3](#ref-temporal-resolution-dau-i)

研究时域分辨率有助于理解言语中的闭塞与释放、连续声音的分段、背景噪声起伏以及听觉辅助设备的动态处理。它也是连接[听觉滤波器](../auditory-filter/)、[掩蔽](../masking/)、[听力损失](../hearing-loss/)与[听觉场景分析](../auditory-scene-analysis/)的重要概念。解释这些联系时，需要区分刺激中的时间信息、神经反应中的时间信息和行为测得的检测能力。[4](#ref-temporal-resolution-shailer)[5](#ref-temporal-resolution-neural)[6](#ref-temporal-resolution-speech)

## 概念范围与主要指标

### 时间分辨是一组能力

最常见的测量是间隙检测：在一段声音中插入短暂的静默，寻找听者能够可靠发现的最短间隙。另一类测量是振幅调制检测：在载波上加入周期性强弱起伏，测量不同起伏速率下所需的最小调制深度。两种任务分别强调较突然的中断和持续的幅度变化，刺激统计特性和可用线索也不同。[7](#ref-temporal-resolution-forrest)[8](#ref-temporal-resolution-viemeister)

时长辨别、起始时间差辨别和先后顺序判断也属于更广泛的听觉时域加工研究。它们可以为时域分辨提供补充信息，但不能未经论证就与间隙检测合并为单一指标。尤其是“感觉两个声音不同”与“说出哪个声音先出现”有不同的信息需求，后者还涉及声音的识别、记忆和分组。[1](#ref-temporal-resolution-moore)

| 测量任务 | 主要操纵 | 常见结果 | 解释时应保留的条件 |
| --- | --- | --- | --- |
| 间隙检测 | 静默或幅度下降的时长 | 毫秒表示的检测阈 | 标记声频谱、声级、边沿、间隙位置、判据 |
| 振幅调制检测 | 调制深度与调制频率 | 最小调制深度或其分贝值 | 载波种类、带宽、内部起伏、频谱线索 |
| 时长辨别 | 两段声音的时长差 | 最小可辨时长差或相对差 | 基准时长、起止线索、响度及记忆负荷 |
| 顺序辨别 | 两类声音的先后间隔 | 达到指定正确率的时间间隔 | 任务是差异检测还是顺序命名、知觉分组 |
| 双耳相关变化检测 | 两耳信号关系改变的持续时间 | 关系变化的检测阈 | 每耳可能始终有声，不能当作单耳静默间隙 |

表中的指标具有不同量纲和实验含义。数值较小的间隙检测阈表示该条件下更容易发现短间隙；较小的调制检测深度表示该条件下对弱起伏更敏感。两者不能仅凭大小排序，也不能从毫秒阈值推算一个人的全部调制检测能力。[2](#ref-temporal-resolution-efficient)[9](#ref-temporal-resolution-musicians2025)

### 与时域整合、精细结构和双耳时间差的区别

时域整合通常考察较长时间内的信息如何累积，例如延长声音后检测阈下降。时域分辨则关心短时变化是否保留、能否被区分。两种现象可以同时存在：听觉系统既可利用短时片段形成证据，也可在更长时间内汇总多个片段。因此，较长的有效整合时间不能直接解释成只能分辨同样长的间隙。多次观察模型正是为解释这种区别而提出的框架之一。[10](#ref-temporal-resolution-integration)

精细结构敏感性涉及利用波形的快速振荡或相位关系；间隙检测通常更直接依赖幅度中断及其起止反应，但纯音间隙也可能受恢复相位和外围滤波影响。不能根据间隙阈值正常，就断言精细结构利用能力正常。对于[双耳听觉](../binaural-hearing/)，很小的两耳时间差是在比较两路输入的相对时序，也不能与单路声音的静默间隙阈逐一比较。[11](#ref-temporal-resolution-phase)[1](#ref-temporal-resolution-moore)

## 间隙检测：在连续声音中发现中断

### 标记声与间隙的定义

间隙前后的声音称为标记声，分别提供声音结束和重新出现的线索。实验常用宽带噪声、带限噪声或纯音。听者需要在多个呈现中找出含有间隙的一次，或者报告长噪声片段中是否出现中断。检测阈是按规定程序和判据估计的结果，并不是一个固定的生理不应期。[4](#ref-temporal-resolution-shailer)[12](#ref-temporal-resolution-gin)

间隙的物理定义需要明确。若声音先逐渐衰减到零，再完全静默，随后逐渐恢复，那么“完全为零的时长”“两个边沿之间的总时长”和“幅度低于某一比例的时长”并不相同。文献和程序若采用不同定义，直接比较标称毫秒数会产生偏差。图 1 将完全静默段与边沿单独标出，以说明报告刺激参数时需要提供什么信息。[11](#ref-temporal-resolution-phase)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/temporal-resolution/01-gap-markers.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/temporal-resolution/01-gap-markers.svg" alt="同频带与不同频带间隙标记声及边沿定义" loading="lazy" /></a>
<figcaption><p>图 1. 间隙刺激的结构示意。A 的前后标记声均为 1 kHz；B 的后标记声改为 2.3 kHz，用来说明频谱改变。两者都采用 2 ms 余弦边沿，完全静默段为 46–54 ms，即 8 ms；幅度开始下降到完全恢复的区间为 44–56 ms，即 12 ms。C 展示门控函数，纵轴不是听觉神经活动。波形相对幅度在 ±1 以内；这些参数是教学示例，不是常模或正式测试处方。</p></figcaption>
</figure>

### 同通道与跨通道检测

当间隙前后的声音主要激活相同或高度重叠的听觉频率通道时，常称为同通道间隙检测。听者可以利用同一表征中的短时下降及恢复。若标记声位于分离的频率区域，任务还需要比较不同表征的结束与起始时间，通常称为跨通道间隙检测。这里的“通道”主要指频率选择性或知觉加工通道，不能直接等同于左右耳、处理器通道数或人工耳蜗电极数。[1](#ref-temporal-resolution-moore)[13](#ref-temporal-resolution-unilateral)

这种划分也不是“只有一个听觉滤波器”与“只有两个听觉滤波器”的字面区别。宽带噪声同时激活许多滤波器，但若前后噪声频谱相同，实验仍可归入同通道条件。反过来，不同频谱是否形成分离的知觉通道，还取决于频带重叠、标记声类型与任务设计。因此，实际研究应说明前后标记声的频谱，而不只使用一个类别标签。[1](#ref-temporal-resolution-moore)[4](#ref-temporal-resolution-shailer)

一项对长期单侧重度至极重度听力损失者的研究，测量了其临床正常耳的间隙检测。研究发现，同通道结果与年龄匹配正常听力组没有显著差异，而跨通道阈值更高。这表明任务设计可以揭示不同方面的表现，不能用同通道正常或跨通道异常概括所有时域加工能力，也不能把该样本结论扩大到全部单侧听力损失者。[13](#ref-temporal-resolution-unilateral)

### 为什么“几毫秒”需要附带条件

正常听力者在某些具有足够可听度的宽带噪声条件下，能够检测几毫秒量级的间隙。经典研究中的宽带条件得到约 2.3 ms，而带限刺激在低中心频率条件下得到更长阈值；提高频率、带宽或声级会影响结果。这个例子说明常被引用的“2–3 ms”具有明确的实验来源，却不是整个听觉系统唯一的时间分辨极限。[4](#ref-temporal-resolution-shailer)

噪声自身也有幅度起伏。窄带噪声可能出现较长的自然低谷，人工加入的间隙需要从这些随机低谷中被识别出来；宽带刺激则可提供多个频率区域的同步中断线索。纯音更稳定，但短时门控会产生频谱扩展，间隙后的恢复相位也可能改变滤波输出。因此，换用另一种载波不仅改变刺激形式，也可能改变可用的判断线索。[3](#ref-temporal-resolution-dau-i)[11](#ref-temporal-resolution-phase)

这些差别说明，间隙检测是对一套刺激、听觉表征和决策过程的联合测量。实验设计可以努力限制额外线索，例如采用平滑边沿、控制恢复相位或设置适当掩蔽声，但没有一种简单门控方式能自动保证测到纯粹、独立于频谱的“时间能力”。[11](#ref-temporal-resolution-phase)[7](#ref-temporal-resolution-forrest)

## 振幅调制检测与时域调制传递函数

### 调制深度与调制速率

[振幅调制](../amplitude-modulation/)是在载波上施加幅度起伏。对正弦调制，一个常用表达式为

$$
x(t)=A\,[1+m\cos(2\pi f_m t)]\,c(t),\qquad 0\leq m\leq1,
$$

其中 $c(t)$ 为载波，$f_m$ 为调制频率，$m$ 为调制深度。对这种理想形式，$m=0$ 表示没有外加调制，$m=1$ 表示调制包络的谷值达到零；对于未过调制的正弦包络，调制深度也可由最大与最小包络值之差除以其和得到。若载波为随机噪声，这个参数定义的是外加门控，而不是瞬时随机波形的峰谷比。[8](#ref-temporal-resolution-viemeister)[3](#ref-temporal-resolution-dau-i)

调制深度描述起伏有多强，调制频率描述起伏有多快。两者改变的是不同维度：较深的调制可能很慢，较浅的调制也可能很快。将两者分开，有助于理解为什么“能听见快变化”不等于“对微弱变化敏感”。当调制深度用分贝表示时，常采用 $20\log_{10}m$；此时更负的检测阈表示所需深度更小，而不是表现更差。[8](#ref-temporal-resolution-viemeister)[2](#ref-temporal-resolution-efficient)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/temporal-resolution/03-modulation.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/temporal-resolution/03-modulation.svg" alt="不同调制深度和频率的波形与包络" loading="lazy" /></a>
<figcaption><p>图 2. 调制深度与速率的独立变化。载波均为 700 Hz，上、中两行保持 10 Hz 调制并改变深度，下两行保持深度 0.8 并改变速率。橙线是规定的外加包络及其负值，蓝线为调制波形。为了让相对幅度保持在 ±1 内，各行以 <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>+</mo><mi>m</mi></mrow><annotation encoding="application/x-tex">1+m</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:0.7278em;vertical-align:-0.0833em;"></span><span class="mord">1</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="katex-base"><span class="katex-strut" style="height:0.4306em;"></span><span class="mord mathnormal">m</span></span></span></span> 除归一化；该展示归一化不表示各行均方根声级相同，也不能直接用作等声级调制检测实验。</p></figcaption>
</figure>

### 调制传递函数测量什么

时域调制传递函数通常以调制频率为横轴、最小可检测调制深度为纵轴，表示听者对不同速率起伏的敏感性。在宽带噪声等条件下，阈值往往在较快调制处升高，表现出一定的低通特征；但低速端、刺激时长和声级也会影响曲线。名称中的“传递函数”并不意味着直接测量了耳蜗的线性输入输出增益，而是一组行为检测阈。[8](#ref-temporal-resolution-viemeister)

载波条件改变时，曲线不一定保持同一种形状。纯音振幅调制会产生载波两侧的频谱成分，在这些成分可被分辨时，听者可能利用频谱差异而不仅是幅度起伏；噪声载波则有自身的起伏，可能掩蔽外加调制。调制检测阈因而受到声学滤波、内部起伏、调制频率选择性及判断方式的共同影响。[3](#ref-temporal-resolution-dau-i)[14](#ref-temporal-resolution-dau-ii)[15](#ref-temporal-resolution-ewert)

### 为什么不能用间隙阈代替调制传递函数

一些经典模型可以用相同的时间平滑框架解释间隙检测与调制检测的部分数据，这提供了两类任务可能共享加工环节的理论依据。但是，模型中共享环节不意味着每位听者的两个指标必然高度对应。Shen 与 Richards 的研究发现，间隙检测阈与调制传递函数的敏感度参数相关，而与其截止速率的关系并不支持简单的“间隙越短，处理越快”推论。[7](#ref-temporal-resolution-forrest)[2](#ref-temporal-resolution-efficient)

因此，若研究目标是刻画完整的调制敏感性，应尽量测量多个调制频率或使用经过验证的参数估计方法；若只完成一个间隙任务，结论应限定为该间隙条件的表现。这一点也影响模型拟合：单一阈值通常不足以区分时间常数、内部噪声和决策效率等不同解释。[2](#ref-temporal-resolution-efficient)[14](#ref-temporal-resolution-dau-ii)

## 听觉系统如何保留和限制短时变化

### 外围滤波与时间展宽

声音通过耳蜗的频率选择性滤波后，其内部时间结构可能改变。滤波器的冲激响应持续一段时间，输入中断后输出不一定立即降到零；恢复声也可能与残留响应叠加。滤波带宽与响应时程的联系，可以帮助解释一些低频或窄带刺激的间隙检测结果，但并不能把所有行为阈值都归因于一个滤波器的“振铃”。[4](#ref-temporal-resolution-shailer)[11](#ref-temporal-resolution-phase)

听力损失常使听觉滤波器变宽，却不能据此直接推出时域分辨率一定改善。可听频谱的缩减、外围压缩的改变、声音强度及神经加工可能同时变化。较宽滤波器对输入的短时展宽可能较少，但行为任务仍可能受其他环节限制；频率选择性与时域分辨既有物理联系，也有各自的测量边界。[16](#ref-temporal-resolution-review)[3](#ref-temporal-resolution-dau-i)

### 适应、时间平滑与重新起始反应

神经系统对持续声音会产生适应，声音重新出现时又可能产生起始反应。间隙能否被检测，不仅取决于静默段的持续时间，也可能取决于前段声音持续多久、末段声音能否产生足够明显的重新起始反应，以及这些反应如何与背景活动区分。人体听觉诱发磁场研究发现，间隙后的反应与前标记声时长和间隙时长均有关。[5](#ref-temporal-resolution-neural)

为了直观展示时间平滑，可以将幅度门控输入一个一阶低通系统。时间常数较长时，短间隙产生的输出下降较浅，高速调制的输出也衰减更多。这是一种模型机制示意，不是实测听者曲线；听觉系统还包括外围非线性、适应、调制选择性和决策等环节，不能从示意图指定某人的时间常数。[7](#ref-temporal-resolution-forrest)[3](#ref-temporal-resolution-dau-i)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/temporal-resolution/02-temporal-smoothing.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/temporal-resolution/02-temporal-smoothing.svg" alt="时间平滑对间隙门控和调制增益的影响" loading="lazy" /></a>
<figcaption><p>图 3. 一阶因果平滑器的教学模拟。A 输入一个 8 ms 的完全中断，比较 2 ms 与 8 ms 时间常数下的门控响应；系统在间隙前已经处于稳定状态。B 为同一系统的幅度传递增益 <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>20</mn><msub><mrow><mi>log</mi><mo>⁡</mo></mrow><mn>10</mn></msub><mo stretchy="false">[</mo><mn>1</mn><mi mathvariant="normal">/</mi><msqrt><mrow><mn>1</mn><mo>+</mo><mo stretchy="false">(</mo><mn>2</mn><mi>π</mi><mi>f</mi><mi>τ</mi><msup><mo stretchy="false">)</mo><mn>2</mn></msup></mrow></msqrt><mo stretchy="false">]</mo></mrow><annotation encoding="application/x-tex">20\log_{10}[1/\sqrt{1+(2\pi f\tau)^2}]</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="katex-base"><span class="katex-strut" style="height:1.24em;vertical-align:-0.305em;"></span><span class="mord">20</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop"><span class="mop">lo<span style="margin-right:0.0139em;">g</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.207em;"><span style="top:-2.4559em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2441em;"><span></span></span></span></span></span></span><span class="mopen">[</span><span class="mord">1/</span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.935em;"><span class="svg-align" style="top:-3.2em;"><span class="pstrut" style="height:3.2em;"></span><span class="mord" style="padding-left:1em;"><span class="mord">1</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mopen">(</span><span class="mord">2</span><span class="mord mathnormal" style="margin-right:0.0359em;">π</span><span class="mord mathnormal" style="margin-right:0.1076em;">f</span><span class="mord mathnormal" style="margin-right:0.1132em;">τ</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7401em;"><span style="top:-2.989em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="katex-sizing reset-size6 size3 mtight"><span class="mord mtight">2</span></span></span></span></span></span></span></span></span></span><span style="top:-2.895em;"><span class="pstrut" style="height:3.2em;"></span><span class="hide-tail" style="min-width:1.02em;height:1.28em;"><svg xmlns="http://www.w3.org/2000/svg" width="400em" height="1.28em" viewBox="0 0 400000 1296" preserveAspectRatio="xMinYMin slice"><path d="M263,681c0.7,0,18,39.7,52,119
c34,79.3,68.167,158.7,102.5,238c34.3,79.3,51.8,119.3,52.5,120
c340,-704.7,510.7,-1060.3,512,-1067
l0 -0
c4.7,-7.3,11,-11,19,-11
H40000v40H1012.3
s-271.3,567,-271.3,567c-38.7,80.7,-84,175,-136,283c-52,108,-89.167,185.3,-111.5,232
c-22.3,46.7,-33.8,70.3,-34.5,71c-4.7,4.7,-12.3,7,-23,7s-12,-1,-12,-1
s-109,-253,-109,-253c-72.7,-168,-109.3,-252,-110,-252c-10.7,8,-22,16.7,-34,26
c-22,17.3,-33.3,26,-34,26s-26,-26,-26,-26s76,-59,76,-59s76,-60,76,-60z
M1001 80h400000v40h-400000z"/></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.305em;"><span></span></span></span></span></span><span class="mclose">]</span></span></span></span>，不是调制检测阈或临床常模。两图解释同一平滑机制在时域和频域的表现，不包含耳蜗滤波、神经适应或判断噪声。</p></figcaption>
</figure>

### 从神经反应到行为判断

神经记录可研究短时变化在哪里、何时被编码，但神经反应阈与行为检测阈并不天然等价。脑电或磁场结果依赖所记录的成分、统计检测标准、重复次数和刺激序列；行为结果还依赖注意、练习、记忆和反应规则。即使两者在特定实验中接近，也不能在另一种人群或另一种刺激中直接代换。[5](#ref-temporal-resolution-neural)[17](#ref-temporal-resolution-age)

此外，较大的神经反应不总意味着更好的检测。响应幅度可能反映同步性、适应状态或抑制机制的改变，而行为检测还需要将有间隙与无间隙的内部表征可靠地区分。对于[听觉诱发电位](../auditory-evoked-potential/)等词条，应把“对变化的响应”“响应与行为的关联”和“能够替代行为的临床指标”分层介绍。[18](#ref-temporal-resolution-position2026)[17](#ref-temporal-resolution-age)

## 实验测量与结果报告

### 固定刺激与自适应程序

固定刺激法在多个间隙时长或调制深度下收集正确率，再拟合心理测量函数，能够观察猜测水平、斜率、上限和判据对应的阈值。自适应程序则根据上一轮或若干轮反应调整刺激，将试次集中在目标正确率附近。不同程序减少或增加某些测量信息，选择应与研究问题相配。[19](#ref-temporal-resolution-levitt)[2](#ref-temporal-resolution-efficient)

对二选一任务，随机猜测正确率为 50%，所以“达到 50% 正确”不能定义为有效检测阈。三选一、是否判断和按键报告也有不同的机会水平与偏差来源。阈值必须附带任务格式、目标正确率、阶梯规则及计算方式；未经换算不能把不同判据的阈值混为同一常模。[19](#ref-temporal-resolution-levitt)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/temporal-resolution/04-psychometric.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/temporal-resolution/04-psychometric.svg" alt="二选一间隙检测的合成心理测量函数" loading="lazy" /></a>
<figcaption><p>图 4. 二选一任务的心理测量函数示意。两条曲线均为合成数据，猜测水平 50%，上限 98%；本图把阈值定义在 75% 正确率，对应约 4.5 ms 和 8.1 ms。它们仅展示统一判据下的读取方式，不代表两个听觉状态。若判据、机会水平或注意失误率改变，阈值的含义也会改变。</p></figcaption>
</figure>

### 声级、带宽和任务条件

声级报告至少要区分声压级与感觉级。相同声压级表示物理强度相同，却不保证相同可听度；相同感觉级表示相对各自阈值的距离相同，却可能对应不同物理声级和响度。对于宽带声音，仅凭单一纯音阈值也不足以概括每个频率区域的可听度。研究通常需要根据刺激频谱检查相关频段，并说明选择哪一种匹配方法。[16](#ref-temporal-resolution-review)[20](#ref-temporal-resolution-shannon)

间隙在声音中的位置、前后标记声时长、是否连续播放背景噪声，以及噪声片段是否重复，都会改变适应、预期和可用线索。重复一段固定噪声可能让听者学习特定起伏；每次独立生成噪声则会引入不同随机变化。两种做法都有用途，但需要记录生成方法与随机种子，避免把刺激重复性误认为听者差异。[7](#ref-temporal-resolution-forrest)[3](#ref-temporal-resolution-dau-i)[5](#ref-temporal-resolution-neural)

结果报告还应保留练习与重复测量的信息。一次阶梯的阈值可能受起始点、步长和偶然反应影响；多个重复估计、适当置信区间和预先规定的排除标准有助于判断差异是否稳定。若某人未达到程序要求的上限正确率，应报告这一现象，而不是强行拟合出一个看似精确的阈值。[19](#ref-temporal-resolution-levitt)[2](#ref-temporal-resolution-efficient)

### 临床间隙测试

噪声中间隙测试（GIN）把短间隙嵌入较长的噪声片段，以报告检测到的中断为主要任务。Musiek 等人的原始研究采用每段 6 s 白噪声、每段零至三个间隙以及规定的列表与评分方式，在正常听力组和已证实中枢听觉神经系统受累组之间发现差异。这为其临床应用提供了依据，但原研究的均值不能直接当作所有年龄、语言或测试系统的异常界限。[12](#ref-temporal-resolution-gin)

GIN 的近似阈值与实验室强迫选择法的阈值并非同一程序产物。持续监测任务可能受漏报、误报、注意维持和反应策略影响，强迫选择任务也有自身限制。临床解释应依据所使用版本的规范、适用人群和综合评估，不能用网页示例声音或一张图诊断听觉加工障碍。[12](#ref-temporal-resolution-gin)[16](#ref-temporal-resolution-review)

## 听力损失、年龄与人工耳蜗

### 可听度与阈上加工的区分

听力损失者在相同声压级下测得较长间隙阈，可能部分来自较低感觉级或较小有效可听带宽。研究需要进一步判断，在控制这些因素之后是否仍存在差异。Reed 等人的评估指出，不同任务的证据并不一致；对部分间隙检测和短声检测结果，给正常听力者施加掩蔽以模拟可听度下降，可以再现听损者的表现，而其他时域任务不能被同样解释。[16](#ref-temporal-resolution-review)

这不表示听力损失只影响可听度，也不表示所有“阈上缺陷”都已被证实。较严谨的做法是分开报告物理刺激、各频段可听性和控制后的剩余差异，并保留人群范围与测量不确定性。若年龄与听力损失同时改变，仅比较两组平均值难以辨认每个因素的贡献。[16](#ref-temporal-resolution-review)[21](#ref-temporal-resolution-regev-jasa)

### 年龄效应需要具体到指标

年龄相关变化可能涉及外围听觉、神经适应、认知加工及任务经验。正常听力阈值相近并不保证全部加工过程相同，但年龄较大也不能自动推出所有时域指标下降。采用不同载波、调制频率和测量方法，可能得到不同程度的年龄差异。[17](#ref-temporal-resolution-age)[22](#ref-temporal-resolution-regev2025)

例如，一项在 20 名语后聋人工耳蜗使用者中比较年轻与老年组的研究，采用绕过处理器的单电极刺激，并结合行为间隙检测、皮层反应、神经恢复和认知测量。显著年龄效应主要出现在脉冲串掩蔽后的听神经复合动作电位恢复；所测其他时域指标和言语表现没有呈现一致的年龄效应。小样本与电刺激条件限制了推广范围，但该结果提醒我们保留指标之间的不一致。[17](#ref-temporal-resolution-age)

### 电刺激与日常处理器输出

[人工耳蜗](../cochlear-implant/)可以通过停止一段脉冲串形成间隙，也可以改变脉冲幅度表达包络变化。直接电刺激研究发现，检测阈对刺激水平有明显依赖；在部分高水平条件下可以得到几毫秒量级的间隙阈，而低水平条件下更长。因此，“人工耳蜗缺少声学精细结构”不能直接推出其所有间隙检测都差。[20](#ref-temporal-resolution-shannon)

直接刺激与日常使用设备需要区分。前者可以控制电极、脉冲速率、脉冲幅度及静默间隔，后者还经过麦克风、滤波、压缩、通道选择和编码。处理器输入端 8 ms 的声学间隙，不保证每个电极上都产生相同长度的完全无刺激区间。输出记录和用户行为应分别测量，不能把程序中的标称间隙当作已验证的听觉效果。[20](#ref-temporal-resolution-shannon)[17](#ref-temporal-resolution-age)

## 与言语、音乐和听觉场景的联系

### 短时线索与言语理解

言语包含短暂停顿、闭塞、释放与持续的幅度起伏，时域信息因此参与音素识别和言语分段。经典声码器研究表明，在保留若干频带包络的条件下，严重减少频谱细节后仍可维持较高的部分言语识别表现。这证明包络承载了重要信息，却没有证明某个间隙阈值就能预测句子理解，也没有证明频谱和精细结构在所有情境中都不重要。[6](#ref-temporal-resolution-speech)

噪声中的言语识别还涉及利用背景低谷、区分目标与干扰、跨片段汇总信息和语言知识。[言语可懂度](../speech-intelligibility/)与[言语接收阈](../speech-reception-threshold/)因而是综合表现，不能由单一非言语时域指标替代。若发现相关，需要检查年龄、可听度和其他共变因素；相关也不自动说明训练某项检测能力就会改善日常沟通。[21](#ref-temporal-resolution-regev-jasa)[22](#ref-temporal-resolution-regev2025)

### 调制敏感性与调制掩蔽

检测孤立的弱起伏与在其他起伏中辨认目标起伏不同。后者还涉及调制频率选择性与调制掩蔽：背景强弱变化可能干扰目标言语的包络，即使背景的声学频谱没有发生相同变化。调制滤波器和包络功率谱模型为研究这种干扰提供了框架。[3](#ref-temporal-resolution-dau-i)[15](#ref-temporal-resolution-ewert)

2025 年的一项研究在不同年龄和听力状态的听者中，发现调制调谐指标在特定干扰条件下，对言语接收阈的个体差异具有超出年龄和可听度的解释贡献。另一项主要使用声码器包络信息的研究，却未得到老年组在各种调制干扰下都稳定更差的结果。这些发现支持继续研究联系，同时反对把一种实验的关联写成普遍规律。[21](#ref-temporal-resolution-regev-jasa)[22](#ref-temporal-resolution-regev2025)

### 顺序、节奏与双耳关系变化

音乐和言语中的先后关系不只由间隙大小决定。声音若被组织成不同知觉流，听者可能难以判断跨流音符的精确先后，却能清楚辨认各流内部的节奏。这把时域加工与[听觉场景分析](../auditory-scene-analysis/)联系起来：知觉分组既受到时间结构影响，也会反过来影响时间结构的判断。[1](#ref-temporal-resolution-moore)

双耳实验中的“间隙”还可能指两耳关系的短暂改变，而非声能中断。2025 年一项研究把不相关的两耳噪声片段嵌入原本相同的两耳噪声，比较不同音乐训练经历听者的检测表现。其结果涉及双耳相关变化敏感性与训练经历的关联，不能当作单耳静默间隙检测的证据，也不能由分组关联推断音乐训练必然产生因果改善。[9](#ref-temporal-resolution-musicians2025)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/temporal-resolution/05-task-boundaries.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/temporal-resolution/05-task-boundaries.svg" alt="间隙检测、顺序判断和双耳相关变化的任务区别" loading="lazy" /></a>
<figcaption><p>图 5. 三类时域任务的边界示意。A 为同一标记声中 10 ms 的无声区间；B 要求判断高、低音的先后，其时间关系不等于 A 的间隙阈；C 左右耳都持续有声，只在中央 20 ms 区间改变相关性。条块表示事件安排而非声压波形，C 的颜色也不是能量下降。所有时长均为说明任务结构的合成参数。</p></figcaption>
</figure>

## 计算模型与公开实现

### 时间窗口和漏泄积分模型

一种经典框架先进行声学滤波与非线性变换，再用短时间窗口平滑内部响应，最后根据谷值、峰谷差或其他统计量判断是否有变化。漏泄积分器是这种思想的简化形式；它可以解释某些间隙和调制检测数据，但时间常数只是模型参数，不能脱离外围处理和决策规则被当作人的唯一“时间分辨率”。[7](#ref-temporal-resolution-forrest)[8](#ref-temporal-resolution-viemeister)

图 3 的离散实现为 $y[n]=(1-a)u[n]+ay[n-1]$，其中 $a=\exp[-1/(f_s\tau)]$，$f_s$ 为采样率，$\tau$ 为时间常数。输入 $u[n]$ 是归一化幅度门控；这段代码用于展示平滑，并未实现上述经典论文的全部听觉前端。复现正式模型时，应使用论文规定的信号变换、参数和判断机制，而不是只替换一个时间常数。[7](#ref-temporal-resolution-forrest)

### 调制滤波器组与包络功率谱模型

Dau 等人的模型在外围处理、整流与适应之后，加入对不同调制频率敏感的滤波器。模型中的两类频率轴需要区分：声学频率描述载波或耳蜗通道，调制频率描述包络的强弱变化速率。多通道扩展进一步汇总不同声学频带与不同时段的信息，用于解释调制检测和调制掩蔽。[3](#ref-temporal-resolution-dau-i)[14](#ref-temporal-resolution-dau-ii)

Ewert 与 Dau 的包络功率谱模型则根据调制滤波器通带内的目标与背景包络能量进行预测，更直接地刻画调制选择性和掩蔽。两种框架的输入、内部表征和决策方式不同，不能只因都使用“调制滤波器”就把实现和适用范围视为相同。模型是否能解释一种间隙测试，也需要该刺激与行为程序下的单独验证。[15](#ref-temporal-resolution-ewert)

听觉建模工具箱（AMT）提供可查看的模型文档与源代码。下面的入口对应正式模型说明，工具箱的官方代码托管在 SourceForge；本次整理核查了公开文档和入口，未宣称运行过完整第三方模型。[23](#ref-temporal-resolution-amt-dau)[24](#ref-temporal-resolution-amt-ewert)[25](#ref-temporal-resolution-amt-source)

公开实现还可能包含后续修订。AMT 的 Dau 1997 函数默认调制滤波设置包含后续版本选项，源码提供原模型设置的线索；Ewert 2000 函数文档则明确说明，其频带中心和附加低通处理与原论文配置存在差别。因此，下载同名函数不等于已经精确复现原论文，正式比较需要核对参数、实现版本及配套实验程序。[23](#ref-temporal-resolution-amt-dau)[24](#ref-temporal-resolution-amt-ewert)

| 模型或资源 | 适合了解的问题 | 文档与代码入口 | 使用边界 |
| --- | --- | --- | --- |
| Dau 1997 调制滤波器组 | 调制检测、适应与多通道处理 | [模型说明](https://amtoolbox.org/amt-1.6.0/doc/models/dau1997.php)；[源代码页面](https://amtoolbox.org/amt-1.6.0/doc/models/dau1997_code.php) | 内部表征需配合相应决策过程，不能直接读作受试者阈值 |
| Ewert 2000 包络功率谱模型 | 调制频率选择性、调制掩蔽 | [模型说明](https://amtoolbox.org/amt-1.6.0/doc/models/ewert2000.php)；[源代码页面](https://amtoolbox.org/amt-1.6.0/doc/models/ewert2000_code.php) | 原始验证的任务和刺激条件应保留 |
| AMT 官方代码 | 模型下载、示例与复现基础 | [开发说明](https://amtoolbox.org/development.php)；[官方仓库](https://sourceforge.net/p/amtoolbox/code/ci/develop/tree/) | 检查版本、依赖、采样率及输入声级约定 |
| 本词条绘图脚本 | 门控、时间平滑和测量判据的教学演示 | [配图 Python 脚本](/n3-hearingpedia/figures/temporal-resolution/generate-figures.py) | 合成示意，未拟合受试者，也不是听力诊断程序 |

### 模型预测如何与行为对应

模型输出通常是一组滤波后的响应、包络能量或特征，而行为阈值来自一套完整任务。要从模型得到可比较的阈值，还需要定义有无变化条件、内部噪声、参考模板、决策统计量和目标正确率。若这些环节缺失，即使输出曲线显示清楚的间隙，也不能据此说听者一定能检测。[14](#ref-temporal-resolution-dau-ii)[2](#ref-temporal-resolution-efficient)

参数辨识同样重要。一个较长间隙阈可以由较强内部噪声、较弱可听度、不同载波起伏或时间平滑产生；单一测量点难以决定哪一种机制起主要作用。比较不同声级、带宽和调制频率的结果，并用独立数据验证预测，通常比对一条曲线做高精度拟合更能检验机制。[2](#ref-temporal-resolution-efficient)[16](#ref-temporal-resolution-review)

## 近期研究与待解决问题

### 用电生理减少反应要求

电生理方法可用于无需逐次按键的变化检测范式，但仍受刺激序列、神经适应和统计分析影响。2026 年 Omidvar 等人对 17 名年轻成人使用含多个偏差刺激的序列，比较 500 ms 噪声中不同位置的 10 ms 与 30 ms 间隙。偏差相关负波受到间隙时长和位置影响，较晚间隙的反应减弱，支持研究时间位置与整合过程的重要性。这里的数百毫秒反应变化不能写成最短间隙检测阈，也不能直接成为临床判界。[18](#ref-temporal-resolution-position2026)

### 不同研究结果并存

耳鸣与时域加工的关系也需要保留任务差异。2025 年一项采用宽带和窄带刺激并结合行为与电生理的研究，报告耳鸣组在部分条件下较差，尤其接近耳鸣音高区域；2014 年另一项使用 GIN 的研究却没有发现耳鸣耳、非耳鸣耳和正常对照之间的平均间隙阈显著差异。刺激、样本和方法不同，不能把任一结果归纳为“耳鸣必然降低时域分辨率”，更不能解释成耳鸣声音必然填满静默间隙。[26](#ref-temporal-resolution-tinnitus2025)[27](#ref-temporal-resolution-ginage)

未来较有价值的研究方向包括：让不同方法使用可比较的刺激条件；区分可听度、年龄与加工机制；在短时检测之外加入跨频带与自然言语任务；检验模型在独立人群和设备条件中的预测。对于临床与设备应用，关键并不是得到尽可能短的毫秒数，而是弄清指标测量什么、能否重复，以及它与实际沟通困难之间有多稳定的联系。[2](#ref-temporal-resolution-efficient)[21](#ref-temporal-resolution-regev-jasa)[17](#ref-temporal-resolution-age)

## 与相关词条的关系

阅读本词条时，可先结合[听觉滤波器](../auditory-filter/)理解频谱分析如何影响短时表征，再通过[时域包络](../temporal-envelope/)与[振幅调制](../amplitude-modulation/)区分信号特征和测量任务。[时域精细结构](../temporal-fine-structure/)提供另一类时间线索，其敏感性不能由间隙测试单独推断。

[掩蔽](../masking/)解释目标短时变化如何被其他声音干扰；[听觉场景分析](../auditory-scene-analysis/)讨论时间结构与声源分组的相互影响；[空间听觉](../spatial-hearing/)和[双耳听觉](../binaural-hearing/)关注两耳关系及定位线索。对于沟通与设备问题，可继续阅读[言语可懂度](../speech-intelligibility/)、[言语接收阈](../speech-reception-threshold/)、[听力损失](../hearing-loss/)和[人工耳蜗](../cochlear-implant/)，把单项时域指标放回完整听觉过程之中。
