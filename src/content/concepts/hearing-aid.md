---
title: "助听器"
english: "Hearing Aid"
slug: "hearing-aid"
summary: "通过个体化声学处理改善可听性与交流，系统介绍分频压缩、方向性与降噪、耳道耦合、验配处方、真耳验证、使用获益及公开计算模型。"
categories: ["hearing-aids","audiology","signal-processing"]
tags: ["助听器","宽动态范围压缩","真耳测量","方向性麦克风","自助验配","个体化"]
aliases: ["hearing aids","声学助听器","数字助听器","HA","WDRC"]
status: draft
depth: in-depth
last_updated: "2026-10-06"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
literature_checked_at: "2026-10-06"
knowledge_area: "technology"
kind: "technology"
key_facts:
  - {label: "核心目标", value: "改善可听性、言语交流与日常活动参与"}
  - {label: "补偿机制", value: "按频率、声级与使用场景调节声学处理"}
  - {label: "验配依据", value: "处方计算、真耳验证与实际获益评价相互补充"}
  - {label: "关键区分", value: "听得见、听得懂、听得轻松分别评价"}
  - {label: "计算模型", value: "openMHA、Clarity、MSBG、HASPI／HASQI"}
references: ["nidcd-hearing-aids","keidser-nalnl2-2011","kayser-openmha-2022","winkler-open-fitting-2016","asha-hearing-aids-adults","moore-compression-speed-2008","brons-noise-reduction-2014","kuk-irrt-2026","kates-haspi-hasqi-2022","wu-hearing-aid-features-2019","clarity-toolkit","simpson-frequency-lowering-2018","scollie-dsl5-2005","almufarrij-real-ear-2021","boystown-recd","fda-otc-hearing-aids","knoetze-self-fitting-2024","de-sousa-self-fitting-2023","humes-self-fit-2025","wu-hearing-aid-service-2025","tasnim-ml-hearingaid-2024"]
batch: 3
order: 30
---

**助听器**（hearing aid）是为听力损失者提供声学补偿的听觉辅助装置。常见的气导助听器通过麦克风采集声音，经频率相关、声级相关的处理后，由受话器把声音送入耳道，使更多有用的声音进入使用者的残余可听范围。现代助听器还可利用多个麦克风、双耳通信和场景分析改善噪声中的聆听条件；其最终价值体现在言语交流、聆听舒适度和日常活动参与，而不只是输出声级的增加。[1](#ref-nidcd-hearing-aids)

助听器依赖使用者原有的[耳蜗](../cochlea/)和听觉通路完成声音编码。放大可以改善可听性，却不能完整恢复受损耳蜗的频率选择性和阈上信息处理能力。因此，同样听得见一句话，佩戴者仍可能在辨认辅音、分离多个说话人或理解嘈杂环境中的内容时感到困难。理解助听器，需要把声学装置、个体听觉状态、验配方法和真实使用环境放在一起考察。[2](#ref-keidser-nalnl2-2011)

## 工作原理与装置形式

气导助听器的基本链路包括声电转换、数字信号处理和电声转换。麦克风把耳旁的声压变化转换为电信号，模数转换后进入数字处理器；经处理的信号再驱动受话器。这里的“受话器”是小型电声换能器，相当于微型扬声器，并不是接收无线信号的部件。电源、无线连接和控制软件支持整套系统运行，但最终送到鼓膜附近的仍然是声波。[1](#ref-nidcd-hearing-aids)

数字处理通常按频率划分为若干频带，在各频带内独立或联动调整增益。这样可以对高频听阈较差、低频残余听力较好的情况提供不同补偿，也能让小声和大声采用不同的放大量。方向性处理、降噪、反馈抵消和输出限制会与分频压缩共同工作；具体顺序、分析频带数和可供验配调节的通道数因设计而异，不能仅根据“通道数”判断整机优劣。公开研究平台展示了这些模块的组合方式，但不代表所有商业产品采用同一条处理链。[3](#ref-kayser-openmha-2022)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/hearing-aid/01-signal-and-acoustic-paths.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/hearing-aid/01-signal-and-acoustic-paths.svg" alt="气导助听器的电子处理链、直达声路径和声学反馈路径" width="656" height="283" loading="lazy" /></a>
<figcaption><p>图 1　气导助听器的信号与声学路径。处理声经过受话器进入耳道；开放耳塞或通气孔还允许部分环境声直接到达鼓膜，两路声音在耳道内叠加。受话器输出若重新到达麦克风，便形成声学反馈路径。图中数字处理框概括功能，不规定算法顺序；声反馈虚线也不表示反馈必然发生啸叫。依据装置原理与开放式验配文献绘制。<a href="#ref-nidcd-hearing-aids">1</a><a href="#ref-winkler-open-fitting-2016">4</a><a href="#ref-kayser-openmha-2022">3</a></p></figcaption>
</figure>

外形主要决定部件放置和声学耦合方式。耳背式把主体置于耳后，通过声管连接耳模或耳塞；受话器外置式把受话器放入耳道，通过细导线连接耳后主体；耳内式和耳道式则把较多部件整合在耳甲腔或耳道中。小型化可能改善外观，却也影响电池空间、操作便利性、麦克风布置和可用输出。开放式、封闭式描述的是耳道耦合程度，不能与某一种外形简单画等号。[1](#ref-nidcd-hearing-aids)[4](#ref-winkler-open-fitting-2016)

本文主要讨论这类气导声学助听器。骨导听觉装置通过机械振动把声音传至内耳；[人工耳蜗](../cochlear-implant/)则把声音转换为电刺激，绕过部分受损的感受器功能。三者的适用听觉条件、输入输出单位和验证方式不同。对侧信号传输系统（CROS）把较差耳一侧的声信号送至另一侧，主要改善该侧声音的可达性，也不等于重建两耳各自独立的听觉输入。[5](#ref-asha-hearing-aids-adults)

## 从听力损失到补偿目标

助听器最直接处理的问题是听阈升高：原本可听的弱声成分落到听阈以下，通过适当增益可使其重新可听。然而，[听力损失](../hearing-loss/)通常不能只用“声级整体下降”表示。耳蜗性损失可能伴随响度增长加快、频率分辨能力下降，以及在噪声中利用微弱线索的困难。相同听力图的两个人，对同一处理方案的言语识别和声音偏好仍可能不同。[2](#ref-keidser-nalnl2-2011)[6](#ref-moore-compression-speed-2008)

助听器的补偿目标因而包含多个层次：弱声应尽可能可听，普通交谈声应清晰而舒适，强声输出应受到合理约束，同时尽量保留有助于区分音素、说话人和声源位置的信息。例如，提高高频增益可能使某些辅音线索显现，也可能暴露原本听不到的背景噪声或增加反馈风险；减少增益可能让声音更柔和，却同时降低了信息的可达性。这些目标有时相互促进，有时需要权衡。[2](#ref-keidser-nalnl2-2011)[4](#ref-winkler-open-fitting-2016)

**听得见、听得懂和听得轻松是不同结果。** 可听性关注声音是否超过听阈；[言语可懂度](../speech-intelligibility/)关注能否正确理解内容；聆听费力还涉及为完成任务所投入的认知资源。满意度则进一步受音质、佩戴感受、操作和环境需求影响。任何单项测量都难以代替其余维度，这也是助听器研究常同时报告声学、行为和自评结果的原因。[7](#ref-brons-noise-reduction-2014)[8](#ref-kuk-irrt-2026)

## 频率增益与宽动态范围压缩

### 为什么需要随声级改变增益

在某些耳蜗性听力损失中，听阈明显升高，而响度不适水平的变化相对较小，残余[动态范围](../dynamic-range/)因而缩窄。如果始终施加足够大的固定增益，弱声可能变得可听，但原本较响的声音也可能变得过响。**宽动态范围压缩**通过对弱声提供较大增益、对强声提供较小增益，把较宽的输入声级范围映射到较窄的输出范围。它处理的是声级关系，并不是把声波在时间轴上压短。[6](#ref-moore-compression-speed-2008)

用单个频带的简化稳态关系表示，输入声级为 $L_{\mathrm{in}}$，输出声级为 $L_{\mathrm{out}}$，增益为 $G=L_{\mathrm{out}}-L_{\mathrm{in}}$。若压缩起点为 $K$、起点以下的增益为 $G_0$，可以写成：

$$
L_{\mathrm{out}}=
\begin{cases}
L_{\mathrm{in}}+G_0, & L_{\mathrm{in}}\le K,\\
K+G_0+\dfrac{L_{\mathrm{in}}-K}{\mathrm{CR}}, & L_{\mathrm{in}}>K.
\end{cases}
$$

这里的压缩比为 $\mathrm{CR}=\Delta L_{\mathrm{in}}/\Delta L_{\mathrm{out}}$。例如 2∶1 表示在压缩区内输入增加 10 dB，稳态输出增加 5 dB。输出仍随输入增大，只是增长较慢；它不是“输入越大，输出越小”。真实装置还可能包含低声级扩展、多个压缩拐点、跨频带联动和输出限制，上式只用于说明基本关系。[6](#ref-moore-compression-speed-2008)[3](#ref-kayser-openmha-2022)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/hearing-aid/02-compression-level-and-time.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/hearing-aid/02-compression-level-and-time.svg" alt="宽动态范围压缩的稳态输入输出曲线与快慢增益调整示例" width="819" height="315" loading="lazy" /></a>
<figcaption><p>图 2　声级压缩与增益调整速度。A：示意模型在输入 50 dB SPL 以下提供 30 dB 固定增益，以上采用 2∶1 压缩，并在 105 dB SPL 设置稳态输出上限；数值仅为解释关系而选，不代表处方、舒适阈或任何产品规格。B：输入从 60 升至 80 dB SPL 后再降回 60 dB SPL，两组增益都趋向相同稳态值，但调整过程不同。图例为模型的启动／恢复指数时间常数，不等同于按具体测试标准测得的启动时间或恢复时间；本图未模拟完整输出限幅器的瞬态。</p></figcaption>
</figure>

### 压缩速度与时域信息

压缩器需要估计声级并改变增益，这一过程不是瞬间完成的。输入突然增强时，减小增益所需的过程通常用启动时间描述；输入减弱后，增益恢复的过程用恢复时间描述。较快的调整可能提升相邻强音之间弱音的可听性，但也会改变音节之间的声级反差和[时域包络](../temporal-envelope/)；较慢的调整更容易保留短时声级变化，却可能使强声之后的弱声暂时得不到足够放大。[6](#ref-moore-compression-speed-2008)

压缩速度与压缩比应分开理解。相同 2∶1 的稳态压缩器可以有很不相同的动态反应，两个装置在稳定测试音下的输出接近，也可能对连续言语产生不同包络。多频带压缩还会改变频谱峰谷之间的相对幅度。这里改变的是声信号的可用线索，并不意味着已经补回耳蜗受损造成的频率选择性下降。[6](#ref-moore-compression-speed-2008)[9](#ref-kates-haspi-hasqi-2022)

现有证据不支持对所有使用者统一采用“越快越好”或“越慢越好”的原则。听力程度、背景噪声起伏、言语材料及个体利用声学线索的能力都会影响结果。有关[时域精细结构](../temporal-fine-structure/)敏感性与压缩偏好的研究提出了可能的解释，但这不等于已经存在可以仅凭一项精细结构测验决定最佳参数的通用临床规则。[6](#ref-moore-compression-speed-2008)

## 方向性、降噪与双耳处理

### 方向性如何改变信噪比

方向性麦克风系统利用多个麦克风之间的声级或相位关系，对不同方向施加不同响应。若目标说话人在较高灵敏度方向，噪声主要来自其他方向，处理后目标相对噪声的比例可以提高。自适应系统还能随声场改变抑制方向；双耳波束形成则可使用两侧装置的麦克风信号，形成更大的空间采样范围。[3](#ref-kayser-openmha-2022)[10](#ref-wu-hearing-aid-features-2019)

这种空间优势取决于声源几何关系。当言语和噪声来自同一方向，单纯方向性无法依据方位把两者区分开；混响会使目标和噪声从多个方向到达，也会削弱理想指向图的预测作用。多人轮流交谈、说话人在身侧或使用者转头时，强调正前方的处理未必符合当时的聆听目标。因此，方向性模式的价值必须结合场景与目标选择来理解。[10](#ref-wu-hearing-aid-features-2019)[4](#ref-winkler-open-fitting-2016)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/hearing-aid/03-directional-principle.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/hearing-aid/03-directional-principle.svg" alt="理想全向和心形方向性响应及其随噪声方位变化的信噪比改善" width="610" height="329" loading="lazy" /></a>
<figcaption><p>图 3　方向性获益依赖目标与噪声的空间分离。A：理想全向响应与心形幅度响应 <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>D</mi><mo stretchy="false">(</mo><mi>θ</mi><mo stretchy="false">)</mo><mo>=</mo><mo stretchy="false">(</mo><mn>1</mn><mo>+</mo><mi>cos</mi><mo>⁡</mo><mi>θ</mi><mo stretchy="false">)</mo><mi mathvariant="normal">/</mi><mn>2</mn></mrow><annotation encoding="application/x-tex">D(\theta)=(1+\cos\theta)/2</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.0278em;">D</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0278em;">θ</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord">1</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mop">cos</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal" style="margin-right:0.0278em;">θ</span><span class="mclose">)</span><span class="mord">/2</span></span></span></span>，正前方为 0°，半径是归一化线性幅度。B：目标固定在正前方、单一噪声改变方位时，相对全向系统的理论信噪比改善为 <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>−</mo><mn>20</mn><msub><mrow><mi>log</mi><mo>⁡</mo></mrow><mn>10</mn></msub><mi mathvariant="normal">∣</mi><mi>D</mi><mo stretchy="false">(</mo><mi>θ</mi><mo stretchy="false">)</mo><mi mathvariant="normal">∣</mi></mrow><annotation encoding="application/x-tex">-20\log_{10}|D(\theta)|</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">−</span><span class="mord">20</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop"><span class="mop">lo<span style="margin-right:0.0139em;">g</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.207em;"><span style="top:-2.4559em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2441em;"><span></span></span></span></span></span></span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mord">∣</span><span class="mord mathnormal" style="margin-right:0.0278em;">D</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.0278em;">θ</span><span class="mclose">)</span><span class="mord">∣</span></span></span></span>。这是无混响、无泄漏和无设备噪声的理想模型，不是助听器实测性能；未绘制具有理想零点的 180°，该零点不能解释为真实设备可无限抑制噪声。</p></figcaption>
</figure>

### 降噪的作用不只在正确率

传统单麦克风降噪通常估计某个时频单元中噪声所占比例，并降低噪声占优区域的增益。由于言语与噪声会重叠，降低增益也可能削弱目标言语。噪声变小、声音更舒适，与识别分数提高并不是同一件事。Brons 等在 20 名中度感音神经性听力损失者中比较三种商业降噪处理，观察到噪声烦扰降低，但未观察到言语可懂度提高；某些条件中舒适度与可懂度之间还存在权衡。这个结果描述所测试的算法和条件，不能外推为所有现代降噪都无法改善理解。[7](#ref-brons-noise-reduction-2014)

基于深度学习的处理可以利用更复杂的语音模式估计目标声，与传统噪声估计方法不同。不过，评价它仍需同时检查目标信息保留、延迟、功耗、对未见说话人和噪声的适应，以及真实听损者的表现。离线语音增强的客观分数提高，并不能单独证明在耳旁实时设备中也具有同等获益。Clarity 等公开任务提供了可重复比较的材料和基线，但竞赛条件与临床使用条件仍需明确区分。[11](#ref-clarity-toolkit)[9](#ref-kates-haspi-hasqi-2022)

### 双耳可懂度与空间感的权衡

双耳助听不仅是两侧分别增大声音。[空间听觉](../spatial-hearing/)依赖耳间时间差、耳间声级差和耳廓频谱等线索；麦克风位置、两侧增益差异及联合处理都可能改变这些线索。独立压缩可能使耳间声级关系随时间变化，强空间滤波则可能把声场集中到特定方向。设计时既要考虑目标增强，也要考虑定位、环境感知及处理造成的空间线索变化。[4](#ref-winkler-open-fitting-2016)[3](#ref-kayser-openmha-2022)

Wu 等的交叉研究让 54 名轻至中度听损老年人在四种条件下分别使用双耳助听器。高级方向性和降噪功能在受控实验室条件下显示优势，但日常自评没有同样强的证据支持高级装置优于基础装置；功能开启相对关闭的价值则更一致。这提示实验室应测出算法能做什么，真实生活随访则要回答使用者是否经常遇到能够发挥这些优势的场景。结果不能直接推广到所有年龄、职业、产品和声场。[10](#ref-wu-hearing-aid-features-2019)

## 反馈、耳道耦合与处理延迟

### 声学反馈与堵耳效应

受话器发出的声若经耳塞周围或通气孔返回麦克风，会再次被放大。当闭环在某些频率满足足够的增益和相位条件时，就可能出现持续啸叫。手靠近耳旁、耳塞移位或佩戴帽子都可能改变反馈路径。反馈抵消通常通过估计返回麦克风的成分并予以抵消来提高稳定性；它不能无条件消除所有反馈，也不能代替合适的耳模、耳塞和增益设置。[4](#ref-winkler-open-fitting-2016)[3](#ref-kayser-openmha-2022)

封闭耳道有利于保留低频输出并减少泄漏，但可能使自己的声音听起来低沉、空洞或“堵在耳内”。堵耳效应的一项重要机制，是发声时由骨和组织振动传入耳道的低频声，在出口被堵塞后不易向外释放。扩大通气孔或使用开放耳塞常能减轻这种感受，但也会改变低频放大、最大稳定增益和信号处理效果。受话器外置式可以采用开放或较封闭耦合，不能仅凭细导线外观认定其没有堵耳效应。[4](#ref-winkler-open-fitting-2016)

### 直达声与处理声为何会互相影响

开放式验配中，耳道内既有未经助听器处理的直达声，也有经过电子处理后延迟到达的声音。两者相对强度随频率变化；在直达声占主导的频段，助听器即使对电子路径进行了强降噪，也无法同等程度地降低直接进入耳道的噪声。开放式佩戴的主观自然感和信号处理控制能力之间，因此存在具体的声学权衡。[4](#ref-winkler-open-fitting-2016)

当两路信号具有足够相关性且幅度接近时，延迟还会引起随频率交替出现的相长和相消，形成梳状频谱。简化地设直达路径幅度为 1、处理路径幅度为 $a$、相对延迟为 $\tau$，则：

$$
H(f)=1+a\,e^{-j2\pi f\tau}.
$$

在这一模型中，相邻梳齿间隔为 $1/\tau$。这只是解释延迟与频谱起伏的数学例子；实际耳道传递函数、两路频响、非线性增益和输入信号相关性都会改变结果。听者是否察觉以及是否不喜欢这种变化，也不能仅由一个延迟数值决定。[4](#ref-winkler-open-fitting-2016)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/hearing-aid/04-open-fitting-delay.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/hearing-aid/04-open-fitting-delay.svg" alt="开放耳道内直达声与延迟处理声叠加产生的梳状频谱" width="711" height="394" loading="lazy" /></a>
<figcaption><p>图 4　两路相干声叠加的理想频率响应。两路幅度比固定为 1∶0.8，相对幅度按 <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>20</mn><msub><mrow><mi>log</mi><mo>⁡</mo></mrow><mn>10</mn></msub><mo stretchy="false">(</mo><mi mathvariant="normal">∣</mi><mi>H</mi><mo stretchy="false">(</mo><mi>f</mi><mo stretchy="false">)</mo><mi mathvariant="normal">∣</mi><mi mathvariant="normal">/</mi><mn>1.8</mn><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">20\log_{10}(|H(f)|/1.8)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">20</span><span class="mspace" style="margin-right:0.1667em;"></span><span class="mop"><span class="mop">lo<span style="margin-right:0.0139em;">g</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.207em;"><span style="top:-2.4559em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">10</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.2441em;"><span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord">∣</span><span class="mord mathnormal" style="margin-right:0.0813em;">H</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.1076em;">f</span><span class="mclose">)</span><span class="mord">∣/1.8</span><span class="mclose">)</span></span></span></span> 归一化；分别采用 2 ms 和 6 ms 延迟，梳齿间隔约为 500 Hz 和 167 Hz。图中没有加入耳道共振、频率相关增益或真实泄漏，不能据此判断某个延迟必然可接受或必然产生可闻失真。</p></figcaption>
</figure>

## 频率降低与远程传声

**频率降低**把部分较高频率的信息移到较低、残余听觉更可利用的频率区域，包括频率移位和非线性频率压缩等方法。它与声级压缩处理不同：前者改变频谱位置或频率间距，后者主要改变输入输出声级关系。高频信息在原位置难以有效利用时，频率降低可能帮助察觉或辨认某些辅音；但过强的处理也可能改变频谱对比、音质以及不同音素间的区分线索。[12](#ref-simpson-frequency-lowering-2018)

一项纳入 20 篇研究的系统综述发现，成人使用频率降低后，安静中辅音识别的合并结果显示有限获益，其他言语指标未显示一致优势。因此，“高频听阈差”不应直接等同于“必然需要更强的频率降低”。评价时应说明降低的起始频率、映射关系、比较条件和适应时间，并直接测试需要改善的言语线索。[12](#ref-simpson-frequency-lowering-2018)

远程麦克风采用另一种路径：把拾音位置移到目标说话人附近，再把信号传到助听器，从输入端减少距离和部分环境噪声的影响。它与耳旁麦克风阵列的方向性原理不同，在课堂、讲座或距离较远的交流中有明确的功能定位；但多人自由交谈时，谁佩戴麦克风、如何切换目标、保留多少环境声同样重要。无线串流、远程麦克风和本机拾音的混合比例，会改变使用者实际收到的声场。[5](#ref-asha-hearing-aids-adults)

## 验配处方：从听力图到初始目标

助听器处方把听阈、输入声级和相关个体信息转化为频率增益或输出目标。它提供的是有研究依据的起点，随后仍需验证耳内输出并评价使用效果。处方不是某一品牌的功能名称，也不是把听力图逐点倒转：听阈以 dB HL 表示，设备输入和耳道输出通常以 dB SPL 表示，二者涉及换能器、频率和个体耳道的校准关系，不能直接相减就得到完整验配方案。[2](#ref-keidser-nalnl2-2011)[13](#ref-scollie-dsl5-2005)

**NAL-NL2**综合言语可懂度模型和响度模型，在保证响度合理的约束下优化言语信息的可利用程度，并根据经验数据修正目标。它也考虑年龄、助听经验、语言等因素。声调语言版本在低频信息权重上有所调整，但这不意味着只增加低频增益就能完整解决[普通话汉语声调](../mandarin-lexical-tone/)识别问题；基频、包络、频谱线索和个体残余听觉仍共同影响表现。[2](#ref-keidser-nalnl2-2011)

**DSL v5**即“期望感觉级”方法的第五版，围绕可听性、舒适度和不同输入声级的输出安排形成多阶段输入输出目标，并考虑儿童与成人需求的差别。它在儿童验配中具有重要应用，但并非只用于儿童；同样，NAL 也不能被简单归为只适合成人。讨论处方差异时，应比较相同耳、相同输入和相同目标定义下的曲线，而不是只看软件屏幕上显示的名称。[13](#ref-scollie-dsl5-2005)

| 环节 | 主要回答的问题 | 结果的适用边界 |
| --- | --- | --- |
| 听力学评估 | 听阈、耳间差异及言语能力如何 | 听力图不能覆盖所有阈上困难 |
| 处方计算 | 初始增益和输出目标设为多少 | 模型目标不能保证耳内实际输出 |
| 电声检测与真耳验证 | 装置是否正常，鼓膜附近是否达到目标 | 声学达标不能代替行为获益 |
| 效果评价与随访 | 交流是否改善，是否愿意持续使用 | 单一场景、单次自评不代表全部生活需求 |

## 真耳测量与输出验证

**真耳测量**通过置于耳道内的细探管测量鼓膜附近声压，观察某个使用者实际佩戴助听器时获得了怎样的频率响应。常见的真耳助听响应直接以 dB SPL 表示佩戴状态下的耳道输出；真耳插入增益则比较助听与未助听状态的响应差。测试箱和耦合腔可以检查装置电声性能，但其声学负载不等同于每个人的耳道。[5](#ref-asha-hearing-aids-adults)

验证不宜只检查一个中等声级。较弱、普通交谈和较强言语输入可以揭示压缩在不同工作点的表现，输出上限也需要单独核查。非线性助听器对稳态纯音、噪声和具有言语起伏的刺激可能产生不同反应，因此必须注明测试信号、输入声级和处理模式。低频泄漏、高频输出不足或反馈限制，可能使软件中显示的目标与耳内测量明显不同。[5](#ref-asha-hearing-aids-adults)[14](#ref-almufarrij-real-ear-2021)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/hearing-aid/05-real-ear-verification.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/hearing-aid/05-real-ear-verification.svg" alt="真耳助听响应在调整前后与目标的比较及其频率相关偏差" width="819" height="301" loading="lazy" /></a>
<figcaption><p>图 5　真耳验证如何发现“软件已设定、耳内却未达到”的情况。A：以输入总声级 65 dB SPL 的测试言语为条件，示意某次调整前的高频输出不足，以及调整后更接近目标的响应。B：同一数据减去目标后得到频率相关偏差。全部数据为教学构造，不是受试者记录，也不是 NAL-NL2 或 DSL 计算结果；横轴频率处的耳道频谱输出不能与输入信号的总声级直接逐点相减作为插入增益。本图只展示一个输入声级，不能代替完整多声级验证。</p></figcaption>
</figure>

对婴幼儿或无法完成常规真耳流程的个体，可结合真耳—耦合腔差值等方法，把耦合腔测量转换为更接近个体耳内的输出估计。儿童耳道体积和生长变化尤其重要：同一装置在不同声学负载中的输出可能不同，成人设置不能按比例直接套用。处方、耦合方式和测量转换必须保持一致。[15](#ref-boystown-recd)[13](#ref-scollie-dsl5-2005)

2021 年的系统综述纳入六项实验研究，其中五项进入荟萃分析。相对厂家初始设置，探管验证后调整在安静中言语表现、使用偏好等结果上有统计学收益；噪声中表现和自评能力的合并收益较小。作者同时指出样本和研究数量有限，部分结局的证据质量较低，临床最小重要差异也未充分建立。因此，真耳验证有其明确的声学与证据依据，但不能被描述为保证每位佩戴者都获得相同幅度的交流改善。[14](#ref-almufarrij-real-ear-2021)

## 获益评价、适应与长期使用

实验室评价通常结合安静与噪声中的言语任务。可以在固定信噪比下比较正确率，也可以测定达到某一正确率所需的言语接收阈值；后者常以 dB 信噪比表示，与纯音听阈不是同一个量。比较助听前后或两个算法时，应控制材料、声场、输入声级、耳塞耦合、处方匹配程度以及处理适应状态。否则观察到的差异可能来自可听性不等，而非所研究算法本身。[10](#ref-wu-hearing-aid-features-2019)[9](#ref-kates-haspi-hasqi-2022)

舒适度、音质和聆听费力需要各自的测量。一个人可能准确重复句子，却难以同时记住内容或长时间参与讨论；也可能更偏好噪声较小的设置，却没有更高的正确率。2026 年的基于可懂度的重复—回忆测试研究表明，即使通过调整信噪比匹配部分识别表现，语境和噪声配置仍会影响回忆、费力评分及愿意留在噪声中的时间。该研究包含正常听力者和助听状态听损者，现阶段属于研究工具，不能视为已经通用的临床验配终点。[7](#ref-brons-noise-reduction-2014)[8](#ref-kuk-irrt-2026)

日常评价可结合助听器获益问卷、具体交流目标、佩戴时长和即时情境报告。手机上的即时报告能在事件发生后较短时间记录环境与体验，减少只凭事后总体印象的局限；但记录频率、填写负担和使用者生活方式也影响样本代表性。安静生活占比较高的人与经常参加多人会议的人，即使听力图类似，也可能重视不同功能。[10](#ref-wu-hearing-aid-features-2019)

初戴者可能需要逐步熟悉重新可听的声音、自己的声音变化和装置操作。适应并不是固定天数后必然发生的“自动改善”，也不应作为忽略持续不适、配戴问题或输出不足的理由。随访应区分声学设置、佩戴与维护、沟通策略和期望管理所涉及的问题。当经过合适验配后仍难以获得足够言语理解时，需要进一步评估其他听觉辅助或康复途径，而非简单继续增加音量。[1](#ref-nidcd-hearing-aids)[5](#ref-asha-hearing-aids-adults)

## 自助验配、非处方助听器与服务模式

非处方助听器（OTC）是美国监管体系中的特定类别，面向 18 岁及以上、自觉轻至中度听力损失的成人；不宜把这一适用范围直接当作其他国家的法规。非处方产品可以采用预设程序，也可以具备自助验配功能，因此“非处方”和“自助验配”不是同义词。自助验配可能基于应用程序内的原位测听，也可能让使用者调整增益和频谱平衡，或通过偏好比较逐步寻找设置。[16](#ref-fda-otc-hearing-aids)[17](#ref-knoetze-self-fitting-2024)

有关自助验配的证据应落实到具体装置、流程和支持条件。De Sousa 等的随机试验比较同一型号助听器的自助验配与专业最佳实践验配，64 人进入分析；在六周时，两组主要结果相近，但自助组在规定阶段可以获得远程支持。Knoetze 等在 28 人交叉试验中比较自我调整与原位测听两种自助方式，主要获益和言语结果相近，部分满意度与使用行为指标有所差别。这些研究支持特定流程的可行性，不等于任意设备、任意听力状况下均可获得同样结果。[18](#ref-de-sousa-self-fitting-2023)[17](#ref-knoetze-self-fitting-2024)

进一步的研究也显示，**自助流程不能作为单一干预笼统比较**。2025 年 Humes 等的多中心试验随机分配 584 名参与者，在规定纳入条件和所用设备下，两种自助方法在六周、六个月的主要和次要问卷结局达到不劣于专业验配的结论。另一项由 Wu 等完成的试验则发现，245 名完成者中，专业最佳实践服务在即时日常获益评分上优于两种模拟非处方服务模式，尽管后者总体也有积极结果。[19](#ref-humes-self-fit-2025)[20](#ref-wu-hearing-aid-service-2025)

| 研究 | 比较方式与观察时间 | 可以支持的结论及主要限制 |
| --- | --- | --- |
| De Sousa 等，2023 | 同一型号，自助含远程支持与专业验配；六周 | 本试验主要结果相近；不能去掉支持条件后直接外推 |
| Humes 等，2025 | 相同设备，专业验配与两种自助方法；六周及六个月 | 特定问卷结局达到不劣效；有明确人群筛选及随访流失 |
| Wu 等，2025 | 专业、有限支持和独立使用三种模式；第七周日常评价 | 专业服务评分更好；非处方模式由处方设备模拟，未代表全部市售自助产品 |

这些结果之间的差异提示，应同时考虑纳入人群、硬件、调节权限、操作引导、支持服务和结局指标。没有显著差异也不自动等于证明不劣效，只有按预定界值和相应分析设计实施的试验才能支持后者。设备功能等级与服务质量同样应分开：某项研究没有发现高端设备的额外收益，不意味着所有高级处理在任何困难场景都无用。[19](#ref-humes-self-fit-2025)[20](#ref-wu-hearing-aid-service-2025)

## 计算模型与公开实现

### 放大与实时处理模型

**openMHA** 是面向听觉研究的开放式主助听器平台，可以配置校准、滤波器组、多频带压缩、方向性、降噪及反馈处理，并支持离线文件处理与实时运行。它适合把算法放到共同处理链中比较，也能检验模块顺序、缓冲区和参数如何影响结果。[官方代码仓库](https://github.com/HoerTech-gGmbH/openMHA)、[项目网站](https://www.openmha.org/)和[技术文档](https://doxygendev.openmha.org/index.html)提供不同层次的入口。公开平台的某个配置不应被称为某品牌临床助听器的完整仿真。[3](#ref-kayser-openmha-2022)

**Clarity 工具包**提供听觉场景、助听处理基线、听损模拟和可懂度评价工具，便于建立可复现的端到端比较。其公开实现包括 NAL-R、CAMFIT 等放大基线以及 HASPI；其中 **NAL-R 是线性处方，不能写成 NAL-NL2 的开源实现**，CAMFIT 也具有自己的处方来源。使用前应查清具体任务版本和基线配置。[代码仓库](https://github.com/claritychallenge/clarity)及[工具说明](https://claritychallenge.org/clarity/introduction.html)列出了这些模块。[11](#ref-clarity-toolkit)

### 听损、可懂度与音质模型

听损模拟尝试以阈值、频率选择性或其他外周处理变化，表示听力损失对声信号的影响。它可以帮助构建研究假设，却无法把一个正常听力者变成具有完整听损经历、认知和适应状态的临床受试者。Clarity 中的剑桥 MSBG 模拟及其可微分近似提供了相关实现；模型参数、输入声级校准和所模拟的机制应随结果一起报告。[11](#ref-clarity-toolkit)

**助听器言语感知指数**（HASPI）与**助听器言语质量指数**（HASQI）分别面向可懂度和音质预测。两者使用可按听力损失调整的听觉外周模型，再比较处理声与参考声在听觉表征上的关系。二者不能互相替代，也不能当作满意度、长期佩戴率或聆听费力的直接测量。其预测能力受到训练和验证材料、失真类型以及测试人群范围约束。[9](#ref-kates-haspi-hasqi-2022)

| 平台或模型 | 可用于什么 | 公开入口与使用注意 |
| --- | --- | --- |
| openMHA | 构造实时或离线助听器处理链，比较模块和参数 | [官方仓库](https://github.com/HoerTech-gGmbH/openMHA)；需明确校准、设备与配置 |
| Clarity / pyClarity | 场景、放大基线、听损模拟与预测评估 | [官方仓库](https://github.com/claritychallenge/clarity)；不同挑战的基线并不相同 |
| MSBG 听损模拟 | 检验部分外周听觉损失机制对信号的影响 | [Clarity 工具文档](https://claritychallenge.org/clarity/introduction.html)；不代替真实听损者实验 |
| HASPI / HASQI | 预测言语可懂度与音质，检查放大和失真的权衡 | [HASPI 实现](https://github.com/claritychallenge/clarity/tree/main/clarity/evaluator/haspi)、[HASQI 实现](https://github.com/claritychallenge/clarity/tree/main/clarity/evaluator/hasqi)；均为 Clarity 的 Python 实现，须注明版本 |
| 本词条图示模型 | 复现压缩、方向性、延迟叠加与验证示例 | [绘图源码](/n3-hearingpedia/code/hearing-aid/generate-figures.py)；教学模型不作为验配软件 |

对同一处理链开展可重复研究，至少需要保存输入输出校准、听力图、滤波频带、增益与压缩设置、延迟、双耳策略和软件版本。若先做听损模拟、再交给已经包含听损外周模型的指标，还需要检查是否重复施加了同一种损失。研究应先验证声学实现与假设一致，再讨论预测值，最后以适当的听者实验评价实际获益。[3](#ref-kayser-openmha-2022)[9](#ref-kates-haspi-hasqi-2022)

## 个体化研究与尚待解决的问题

个体化研究正在把听力图以外的信息纳入设置：使用者对声音的偏好、常见环境、语言需求、即时反馈，以及对不同处理的反应都可能参与优化。机器学习可以减少逐项人工搜索参数的负担，但“最喜欢”“最清楚”和“最省力”仍是不同优化目标。偏好学习若只追求即时舒适，可能把增益推向更低的设置；优化声学指标若忽略佩戴体验，也可能得不到长期使用。[21](#ref-tasnim-ml-hearingaid-2024)

研究前沿还包括低延迟目标言语分离、动态多说话人追踪、保留空间线索的双耳增强，以及把实验室模型与真实生活反馈联系起来。需要解决的并非只有预测准确率，还包括实时计算资源、耳道声学、目标选择错误和跨场景稳定性。对中文使用者，普通话汉语声调、多人交谈和语言材料特征也应进入验证，而不能仅依据外语句子测试推断全部日常获益。[11](#ref-clarity-toolkit)[21](#ref-tasnim-ml-hearingaid-2024)[2](#ref-keidser-nalnl2-2011)

助听器相关概念可沿两条路径继续阅读：从[听力损失](../hearing-loss/)、[响度](../loudness/)和[动态范围](../dynamic-range/)理解补偿依据；从[听觉滤波器](../auditory-filter/)、[时域包络](../temporal-envelope/)、[空间听觉](../spatial-hearing/)与[言语可懂度](../speech-intelligibility/)理解处理改变了哪些线索、又应如何评价这些变化。
