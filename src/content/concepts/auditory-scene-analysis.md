---
title: "听觉场景分析"
english: "Auditory scene analysis"
slug: "auditory-scene-analysis"
summary: "系统介绍听觉对象和声流、同时与序列分组、时域相干性、连续性错觉、注意及听力损失，并比较实验范式和计算模型。"
categories: ["psychoacoustics", "neuroscience", "speech"]
tags: ["听觉对象", "声流分离", "鸡尾酒会", "时域相干性"]
aliases: ["ASA", "听觉声流分离", "auditory streaming", "声流分离"]
status: draft
depth: in-depth
last_updated: "2026-10-07"
literature_checked_at: "2026-10-07"
authors: ["AI 辅助编写"]
knowledge_area: "perception"
kind: "function"
key_facts: [{label: "核心过程", value: "分组、分离与声源身份维持"}, {label: "主要层面", value: "同时分组与序列分组"}, {label: "关键区分", value: "知觉组织、注意选择与言语识别"}]
references: ["auditory-scene-analysis-bregman", "auditory-scene-analysis-darwin", "auditory-scene-analysis-objects", "auditory-scene-analysis-texture", "auditory-scene-analysis-mesgarani", "auditory-scene-analysis-cusimano", "auditory-scene-analysis-coherence", "auditory-scene-analysis-bizley", "auditory-scene-analysis-attention", "auditory-scene-analysis-onset", "auditory-scene-analysis-streamproperties", "auditory-scene-analysis-prediction", "auditory-scene-analysis-oxenham", "auditory-scene-analysis-broadband", "auditory-scene-analysis-shamma", "auditory-scene-analysis-precedence", "auditory-scene-analysis-automatic", "auditory-scene-analysis-initial", "auditory-scene-analysis-bistable", "auditory-scene-analysis-models", "auditory-scene-analysis-teki", "auditory-scene-analysis-continuity", "auditory-scene-analysis-global", "auditory-scene-analysis-mcwalter", "auditory-scene-analysis-chatterjee", "auditory-scene-analysis-figurebrain", "auditory-scene-analysis-ding", "auditory-scene-analysis-crossmodal", "auditory-scene-analysis-neural2026", "auditory-scene-analysis-amt", "auditory-scene-analysis-bass", "auditory-scene-analysis-sts", "auditory-scene-analysis-asteroid"]
batch: 3
order: 48
---

**听觉场景分析**（auditory scene analysis，ASA）是听觉系统将到达耳朵的混合声音组织为相对连贯的听觉对象和声流的过程。在餐厅交谈时，耳朵接收到的是谈话、餐具碰撞、背景音乐和房间反射声的叠加；听者却可以把某些声学成分归为朋友的声音，把另一些归为邻桌交谈，并在朋友停顿后继续跟随其话语。这个过程涉及声音成分的分组、不同对象的分离以及声源身份在时间上的维持，是理解复杂环境中聆听能力的重要基础。[1](#ref-auditory-scene-analysis-bregman)[2](#ref-auditory-scene-analysis-darwin)

场景分析不仅适用于言语。把一串音符听成连续旋律、从车流中听出警报、把雨滴声听成整体的雨声背景，都涉及声学信息的组织。听觉系统形成的对象也不必与物理声源一一对应：多个乐器可能共同形成一条旋律，一件乐器的不同声部也可能被听成分开的声流。因此，“听到几个对象”与“实际有几个发声物体”是两个不同的问题。[3](#ref-auditory-scene-analysis-objects)[4](#ref-auditory-scene-analysis-texture)

本词条采用“听觉对象”表示知觉上被归为一个整体的声音单位，采用“声流”表示在时间上被连接起来的一系列声音事件。“听觉流分离”“听觉声流分离”在相关文献中常用于描述声流被分开的现象。场景分析回答声音如何被组织；[听觉注意](../auditory-attention/)回答当前选择和维持哪个目标；[言语可懂度](../speech-intelligibility/)回答目标内容能被正确辨认到什么程度。三者相互作用，不能用同一个指标替代。[2](#ref-auditory-scene-analysis-darwin)[5](#ref-auditory-scene-analysis-mesgarani)

## 声音混合与知觉组织

### 耳朵接收混合信号

在近似线性的声音传播条件下，一只耳朵处的信号可以表示为不同声源经过传播后的叠加：

$$
x_e(t)=\sum_{k=1}^{K}(h_{e,k}*s_k)(t)+n_e(t).
$$

其中，$s_k(t)$ 为第 $k$ 个声源发出的信号，$h_{e,k}$ 为该声源到耳朵 $e$ 的传播响应，星号表示卷积，$n_e(t)$ 表示模型中未单独描述的背景项。传播响应可以包含距离、头部与耳廓滤波以及房间反射。这个表达式描述声学输入，不意味着听觉系统必须先恢复每个声源的完整波形，才能形成有效知觉。[1](#ref-auditory-scene-analysis-bregman)[6](#ref-auditory-scene-analysis-cusimano)

单个声源本身也往往包含许多频率成分。说话者的一个元音可能包含大量谐波，餐具敲击可能激发多个共振频率。与此同时，不同声源的能量又会在相同时间和相邻频率范围内重叠。因此，[听觉滤波器](../auditory-filter/)提供的频率分析是场景组织的基础之一，却不能把每个滤波通道简单认作一个声源：同一声源跨越多个通道，一个通道也可能包含多个声源的信息。[2](#ref-auditory-scene-analysis-darwin)[7](#ref-auditory-scene-analysis-coherence)

### 从声学事件到听觉对象

听觉对象具有知觉层面的连贯性。例如，说话者改变音高、发出不同元音、短暂停顿或移动位置时，其声音仍可能被归为同一对象。这里的“相同”并不要求波形完全一致，而是指变化可以被解释为一个持续声源的活动。对对象的形成、身份识别及意义理解应分别讨论：听者可以分辨两位说话者，却未必认出他们是谁，也未必理解其语言。[3](#ref-auditory-scene-analysis-objects)[8](#ref-auditory-scene-analysis-bizley)

对象组织还具有尺度依赖性。听者可以把整个乐队视为背景，也可以主动跟随其中一件乐器；可以把人群谈话听成整体喧声，也可以在其中寻找某位说话者。任务目标改变时，听觉组织和注意分配可能共同变化。因此，实验报告中的“对象数”“声流数”必须结合刺激、任务及报告方式解释。[1](#ref-auditory-scene-analysis-bregman)[9](#ref-auditory-scene-analysis-attention)

## 同时分组与序列分组

### 同时分组：哪些成分属于同一事件

同时分组关注在相近时间出现的频率成分是否应被归为同一个声音。例如，一个元音的多个谐波可以共同形成一个具有特定音高和音色的对象，而不会被逐一听成许多独立纯音。共同起始、谐波关系及协同变化都可以提供线索；当其中一个成分的起始时间或变化方式与其余成分不同，它参与整体知觉的程度可能下降。[2](#ref-auditory-scene-analysis-darwin)[10](#ref-auditory-scene-analysis-onset)

“同时”不是要求所有成分在物理上完全同步。真实言语中的辅音与元音具有不同起始和持续方式，乐器的各个共振成分也可能衰减不同。听觉系统利用的是多种线索及其上下文，而不是仅根据一个精确的时间界限决定归属。将共同起始视为有利于分组的证据，比把起始不同写成必然分离更符合研究结果。[10](#ref-auditory-scene-analysis-onset)[2](#ref-auditory-scene-analysis-darwin)

### 序列分组：哪些事件来自持续的声源

序列分组关注先后出现的声音能否被连接成同一声流。声音的频率范围、音色、[基频](../fundamental-frequency/)、[时域包络](../temporal-envelope/)、方位以及时间接近性都可能影响这种连接。连续的声音事件越容易被解释为同一来源，越有可能形成连贯声流；但频率接近既不是唯一依据，也不是充分条件。[11](#ref-auditory-scene-analysis-streamproperties)

同时分组和序列分组相互关联。先把一个复杂音中的成分组织为一个事件，有助于随后将它与同一声源的其他事件连接；先前已经建立的声流又可以影响新出现成分的归属。以两位说话者交替和重叠交谈为例，听者不仅需要在重叠时区分声音，也需要在停顿后重新接续对应的说话者。[1](#ref-auditory-scene-analysis-bregman)[12](#ref-auditory-scene-analysis-prediction)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-scene-analysis/01-simultaneous-sequential-grouping.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-scene-analysis/01-simultaneous-sequential-grouping.svg" alt="同时分组与序列分组的时频事件示意" loading="lazy" /></a>
<figcaption><p>图 1　同时分组与序列分组。两面板使用相同的合成时频事件，蓝色成分位于 200、400 和 600 Hz，红色成分位于 300、600 和 900 Hz。A 的方框强调一个事件内的共同起始；B 的虚线强调跨事件的连接。颜色标记候选归属，既不是听者实测结果，也不代表听觉系统能够直接读取声源标签；图中线段不是实际记录的语谱图。</p></figcaption>
</figure>

## 支持分组与分离的声学线索

### 共同起始与共同结束

许多物理事件会同时激发多个频率成分，所以共同起始有助于判断共同来源。元音实验表明，一个谐波若提前出现并在其余成分结束后继续存在，对元音音质的贡献可以减弱；进一步改变提前部分的分组关系，又能改变该谐波对元音的贡献。这类结果说明，成分归属不能全部解释为提前刺激造成的外周适应。[10](#ref-auditory-scene-analysis-onset)

共同结束也可能提供信息，但起始与结束的作用并不要求对称。声音起始的陡峭程度、持续时间、相邻事件和背景噪声都会影响线索的可用性。研究中需要明确改动的是哪个成分、提前或延后多少，以及是否同时改变了总能量与可听性，避免把声级差异误认为分组效应。[10](#ref-auditory-scene-analysis-onset)[2](#ref-auditory-scene-analysis-darwin)

### 谐波性、基频与音色

周期性声源常产生与同一基频相关的一组谐波。[谐波性](../harmonicity/)因而有助于把分布在不同频率的成分组织起来。两组复杂音若具有不同基频，听者有时能更容易分辨它们；这种收益取决于谐波是否可分辨、频谱重叠及刺激任务，不能把某个基频差值当作所有声音都适用的分离阈。[2](#ref-auditory-scene-analysis-darwin)[13](#ref-auditory-scene-analysis-oxenham)

音色和频谱形状也能支持声流身份的维持。相同基频的不同乐器仍可能被区分，同一说话者改变基频时也不一定形成新声流。另一方面，非谐波声音同样能够形成连贯对象，因此谐波性是重要线索，而不是听觉场景分析成立的必要条件。[11](#ref-auditory-scene-analysis-streamproperties)[14](#ref-auditory-scene-analysis-broadband)

### 时域包络与协同变化

同一声源的不同频率成分经常呈现相关的起伏或共同的调制模式，这些关系可用于判断归属。[振幅调制](../amplitude-modulation/)和包络差异既可能帮助分离，也可能在适当条件下支持分组。需要区分声学包络、听觉滤波后的通道包络与神经响应中的起伏，因为它们不必具有相同的相关结构。[7](#ref-auditory-scene-analysis-coherence)[15](#ref-auditory-scene-analysis-shamma)

协同变化不等于每个频率成分具有完全相同的包络。言语包含不同发音方式，房间反射会改变起伏，多个乐器也可能同步演奏。真实场景中应综合包络关系、频谱结构、时序和任务需求，而不能只计算一个相关系数就认定声源数。[7](#ref-auditory-scene-analysis-coherence)[6](#ref-auditory-scene-analysis-cusimano)

### 空间线索

[双耳时间差](../interaural-time-difference/)、双耳声级差以及耳廓提供的频谱线索，可以支持声源定位与连续跟随。声源空间分离还可能通过头影效应和双耳处理改善目标的可用信息，但定位、去掩蔽和知觉分组是不同结果。两个声音来自同一方向仍可分开，来自不同方向也不保证每个重叠成分都被正确归属。[2](#ref-auditory-scene-analysis-darwin)

[空间听觉](../spatial-hearing/)中的优先效应使许多直达声与反射声不被听成重复出现的独立声源，这与稳定场景知觉有关。讨论空间收益时，应说明声源方位、声级、房间条件及单耳和双耳输入，以区分输入信噪比的改变与进一步的知觉组织。空间分离条件的言语成绩不能单独证明某一种分组机制。[16](#ref-auditory-scene-analysis-precedence)[2](#ref-auditory-scene-analysis-darwin)

## 交替音序列与声流形成

### 经典的 A–B–A— 范式

重复呈现 A–B–A— 音组时，A 与 B 表示两种声音，破折号表示静默间隔。在某些条件下，听者会将它们听成一条具有整体节奏的声流；在另一些条件下，A 音和 B 音分别形成两条声流，各自呈现不同节奏。改变频率间隔、重复速率和序列持续时间，可以研究声流组织的变化。[11](#ref-auditory-scene-analysis-streamproperties)[17](#ref-auditory-scene-analysis-automatic)

对简单纯音序列而言，较大的频率间隔和较快的呈现速率往往有利于声流分离。不过结果取决于声音参数和听者，不存在可直接推广到所有复杂声音的统一分界线。频率间隔还应说明以 Hz、半音还是听觉频率尺度表示，音持续时间与起始间隔也应分别报告。[11](#ref-auditory-scene-analysis-streamproperties)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-scene-analysis/02-aba-streaming.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-scene-analysis/02-aba-streaming.svg" alt="同一个交替音序列的一条与两条声流解释" loading="lazy" /></a>
<figcaption><p>图 2　相同 A–B–A— 序列的两种组织方式。A 显示物理刺激；B 的灰线表示整体连接的一条声流解释；C 的同色虚线表示分别连接 A 音与 B 音的两条声流解释。示例 A 为 600 Hz、B 为 900 Hz，音持续 85 ms，相邻音起始间隔 120 ms，每组周期 480 ms。连接线只表示知觉组织，不表示实际扫频或声源运动；参数仅用于绘图，不保证每位听者产生同样知觉。</p></figcaption>
</figure>

### 建立过程与知觉切换

声流组织可以随聆听时间变化。在许多交替音实验中，序列起始较容易被听成整体，随后出现两条声流的比例增加，称为声流分离的建立过程。但是这不是从零开始、最后必然完成的固定阶段；声音参数突然改变、插入间隔或注意切换，都可能改变其发展。[18](#ref-auditory-scene-analysis-initial)[17](#ref-auditory-scene-analysis-automatic)

在具有歧义的条件下，即使声音保持不变，听者也可能在一条与两条声流之间自发切换。Pressnitzer 与 Hupé 比较听觉和视觉双稳态知觉，发现两者的切换具有相似的动态特征，同时个体偏好并非在两种感觉中简单对应。由此可以研究知觉解释之间的竞争，但不能仅凭双稳态现象定位某个特定脑区。[19](#ref-auditory-scene-analysis-bistable)

### 分离并非在所有任务中都有利

当任务是跟随 A 音组成的序列时，分离可能减少 B 音的干扰；当任务是判断 A 与 B 之间的时间关系时，分离反而可能使比较更困难。因此，“更容易分离”不应无条件解释为“听觉更好”。判断场景分析的适应性，需要考虑听者是否形成了与当前任务相适合的组织。[17](#ref-auditory-scene-analysis-automatic)

## 时域相干性及其解释范围

### 从频率分离到跨特征的时间关系

时域相干性强调不同特征响应随时间变化的关联。Elhilali 等将人类知觉实验与雪貂初级听觉皮层记录结合，发现频率相距较远的音在同步呈现时可以被组织为一个整体，而同步与交替条件都可以产生沿频位轴分开的神经响应。这说明，仅有神经群体在频位上的分离，不能充分说明声流知觉是否分离。[7](#ref-auditory-scene-analysis-coherence)

该框架将频率、音高、音色及其他特征的动态关系作为分组依据，试图解释为什么相隔较远但共同变化的成分仍能形成一个对象。不过，它是一类理论与模型，而不是对所有场景都已验证的唯一机制。适应、抑制、预测与注意等过程可能共同参与，模型之间也存在可互补的解释。[15](#ref-auditory-scene-analysis-shamma)[20](#ref-auditory-scene-analysis-models)

### 相关系数是教学例子，不是完整模型

对两条已经选定的特征轨迹 $a_i(t)$ 与 $a_j(t)$，可用归一化相关系数描述其线性协同变化：

$$
r_{ij}=\frac{\left\langle(a_i-\bar a_i)(a_j-\bar a_j)\right\rangle}
{\sqrt{\left\langle(a_i-\bar a_i)^2\right\rangle\left\langle(a_j-\bar a_j)^2\right\rangle}}.
$$

这里的尖括号表示选定时间窗内的平均，前提是两条轨迹都具有非零方差。这个表达式可帮助理解“共同变化”，但只是一种简化量化方法。听觉时域相干模型可以包含多尺度特征表示、滤波、时间整合与不同的相干性运算，不能把上述相关系数视为论文中完整模型的等价实现。[7](#ref-auditory-scene-analysis-coherence)[21](#ref-auditory-scene-analysis-teki)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-scene-analysis/03-temporal-coherence.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-scene-analysis/03-temporal-coherence.svg" alt="同步与不同步包络的相关关系" loading="lazy" /></a>
<figcaption><p>图 3　跨通道时域关系的教学示例。A 中两条归一化包络相同，相关系数为 1；B 使用不同调制频率，所示时间窗内的相关系数接近 0。曲线是人工构造的特征轨迹，没有加入听觉滤波、神经噪声或真实声源传播；图中相关性不直接预测听者会听到几个对象，也不表示完整的时域相干计算模型。</p></figcaption>
</figure>

窗口选择会影响结果。过短的窗口可能只有一个偶然共同起伏，过长的窗口可能掩盖声源切换；滤波及共同背景也可能使互不相关的声源产生相关响应。相反，一个声源的不同成分可能因发声结构或传播而不同步。计算时应报告特征提取、窗口长度及控制条件，并将相关关系与因果上的共同来源区分。[21](#ref-auditory-scene-analysis-teki)[6](#ref-auditory-scene-analysis-cusimano)

## 连续性、预测与背景组织

### 连续性错觉

若一个声音被短暂中断，而中断期间出现足以掩盖潜在目标的噪声，听者有时会听到目标仿佛在噪声下继续存在。这称为听觉连续性错觉。它体现了知觉可以推断被遮挡部分，而不是逐点复制物理输入。噪声并未实际恢复目标的波形，图示中的知觉延续也不能当作目标在间断中真实存在的证据。[22](#ref-auditory-scene-analysis-continuity)

连续知觉受噪声特征及上下文影响。Riecke 等的实验显示，前面听到的场景能够改变随后声音的连续性判断；另一些研究发现，掩蔽声的整体特征也会影响连续性错觉，局部频谱能量并不能解释全部结果。因此，不能把某一示例的噪声级或间断长度写成普遍产生错觉的充分条件。[22](#ref-auditory-scene-analysis-continuity)[23](#ref-auditory-scene-analysis-global)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-scene-analysis/04-continuity-illusion.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-scene-analysis/04-continuity-illusion.svg" alt="物理间断与可能的连续知觉" loading="lazy" /></a>
<figcaption><p>图 4　连续性错觉的条件示意。A 的目标在 0.45–0.75 s 确实停止；B 的噪声在该期间存在；C 的绿色虚线表示在适当掩蔽和上下文条件下可能产生的知觉延续。纵轴 0 与 1 仅表示不存在与存在，不是声压、响度或神经反应幅度。此图没有给出声级和频谱，因此不构成能够保证错觉出现的刺激配方，也不是实测知觉轨迹。</p></figcaption>
</figure>

### 规律、预期与经验

声源在时间上重复、按一定节奏出现或遵循熟悉的模式，可以为后续事件的归属提供线索。预测性既可能存在于目标中，也可能存在于背景中：较稳定的背景有助于解释哪些变化属于新事件。相关研究同时使用主观报告和行为任务，因此需要将规律本身的作用与注意策略、学习和声学差异区分。[12](#ref-auditory-scene-analysis-prediction)

熟悉的说话者、旋律或环境声可以提供先验信息，但经验不能补回所有缺失细节。需要区分“知道可能是什么”与“当前确实辨认出内容”：听者可能根据语境正确猜到词语，也可能形成错误的声源归属。设计实验时应控制材料重复、熟悉程度和语言背景，避免把学习收益全部归为低层声学分组。[1](#ref-auditory-scene-analysis-bregman)[6](#ref-auditory-scene-analysis-cusimano)

### 声音纹理

雨声、火焰声及密集虫鸣不一定被逐个分析为独立事件，而可以被组织为具有稳定统计特征的声音纹理。McDermott 与 Simoncelli 通过声音合成研究发现，匹配听觉表示中的若干统计量，特别是通道之间的关联，能够生成可辨认的纹理。这提供了另一种场景组织视角：有些背景可能通过统计概括形成知觉，而不需要追踪每个微小事件。[4](#ref-auditory-scene-analysis-texture)

声音纹理与声流的边界并非固定。连续的多人交谈可形成背景喧声，其中显著的声音又可能成为前景对象。描述复杂环境时，除了声源数量，还可以考虑背景的稳定性、变化速率及是否存在可跟随的结构；不同层次的组织未必对应同一时间尺度。[4](#ref-auditory-scene-analysis-texture)[24](#ref-auditory-scene-analysis-mcwalter)

## 实验范式与测量解释

### 主观声流报告

常见方法是要求听者报告听到一条或两条声流，也可以连续记录知觉切换。报告应配合清晰示例，并说明是否允许“无法判断”或其他组织方式。主观报告直接反映听者的经验，但会受到理解、判断准则和任务指令影响；尤其在听力损失或设备使用者中，需要排除仅凭声音差异回答“不同”的情况。[17](#ref-auditory-scene-analysis-automatic)[25](#ref-auditory-scene-analysis-chatterjee)

### 间接行为测量

某些节奏偏差或跨声流时间比较，在整体组织下更容易完成；其他目标检测任务则可能从分离中获益。这些范式可以提供与主观报告互补的证据，但不应笼统称为完全不受认知影响的“客观场景分析能力”。任务本身仍需要检测、记忆、决策和反应，应验证它与所关注的组织方式是否有预期关系。[17](#ref-auditory-scene-analysis-automatic)

在比较两个实验条件时，应检查简单的频率或电极差异辨别、目标可听性和基线任务难度。若某个条件中的 A 与 B 根本不能被分辨，缺少分离报告可能首先来自线索不可用；反过来，能分辨 A 与 B，也不足以证明它们已经形成独立声流。[25](#ref-auditory-scene-analysis-chatterjee)[14](#ref-auditory-scene-analysis-broadband)

### 随机图形—背景范式

随机图形—背景刺激由连续变化的短时音组组成；某些频率成分在连续时间帧中重复，形成可以从背景中听出的“图形”。它避免只依靠两个固定纯音研究分离，要求听者跨时间和频率整合结构。Teki 等的研究发现，人类能够检测这类重复图形，行为结果支持时域关系参与复杂场景组织。[21](#ref-auditory-scene-analysis-teki)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-scene-analysis/05-stochastic-figure-ground.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-scene-analysis/05-stochastic-figure-ground.svg" alt="随机背景中连续重复成分的示意" loading="lazy" /></a>
<figcaption><p>图 5　随机图形—背景的原创教学示意。每个 50 ms 时间帧从 24 个候选成分中选择 8 个；A 始终随机选择，B 在 1 s 后固定重复索引 5、11、17 的三个成分，并随机选择另外五个。两条件的每帧成分总数相同，图形没有依赖总成分数突然增加。纵轴为成分索引而不是 Hz，黑块表示成分存在，不是实测声能；示例未合成音频，也未复现某篇论文的全部刺激参数。</p></figcaption>
</figure>

图形检测应同时记录命中与虚报，避免只用命中率评价敏感性。重复成分数、图形持续时间、随机背景密度及声级匹配都应说明。改变其中一个参数时，还可能改变整体能量或线索显著性，需要相应控制。图形检测表现也不能直接换算成[言语接收阈](../speech-reception-threshold/)或日常交流水平。[21](#ref-auditory-scene-analysis-teki)[26](#ref-auditory-scene-analysis-figurebrain)

### 神经测量

脑电、脑磁、功能磁共振及颅内记录可以研究场景组织的神经表征，不同方法提供的空间、时间信息和取样范围不同。Teki 等的图形—背景实验在无需主动检测图形的任务中观察到与分离相关的脑活动，说明某些组织能够在没有主动目标报告时发生；这并不等于所有形式的场景分析完全不需要注意。[26](#ref-auditory-scene-analysis-figurebrain)

连续言语研究则可以比较目标与竞争说话者的神经表征。Mesgarani 与 Chang 的皮层表面记录以及 Ding 与 Simon 的脑磁研究，分别提供了目标选择与听觉对象表征的证据。神经响应对目标具有选择性，不能单独证明听者理解了每句话，也不能把不同测量方式得到的指标视为同一尺度。[5](#ref-auditory-scene-analysis-mesgarani)[27](#ref-auditory-scene-analysis-ding)

## 注意与场景分析的相互作用

### 自动组织与主动选择

声学结构能够在没有明确分组指令时影响知觉，但注意也会改变声流建立和目标选择。Carlyon 等发现，执行竞争任务可以减少随后报告的声流分离；Billig 与 Carlyon 结合主观及行为测量，又发现注意转回序列后的分离增长不同于全新序列起始，支持某些组织在未被主动关注时仍可发生。两类证据不宜被压缩为“全部自动”或“全部由注意产生”。[9](#ref-auditory-scene-analysis-attention)[17](#ref-auditory-scene-analysis-automatic)

实际交流中，听者通常需要既维持目标，又监测重要变化。突然的警报可能引发注意转移，原目标随后还需要重新接续；视觉口型、情境知识和说话者身份也可能协助选择。解释这些收益时，要区分增加了目标信息、提供了选择线索，还是降低了记忆与判断负担。[28](#ref-auditory-scene-analysis-crossmodal)[5](#ref-auditory-scene-analysis-mesgarani)

### 鸡尾酒会聆听

鸡尾酒会问题包含多个层面：目标成分能否被听到、能否与竞争对象区分、能否持续跟随，以及最终能否辨认内容。[掩蔽](../masking/)中的能量掩蔽与信息掩蔽可以从不同角度解释困难，但场景分析并不只等同于其中某一类掩蔽。更清楚的声源组织可能减轻竞争，也可能仍受到目标本身可听性的限制。[2](#ref-auditory-scene-analysis-darwin)[5](#ref-auditory-scene-analysis-mesgarani)

一个实验可以同时报告声流组织、目标正确率和[听觉努力](../listening-effort/)，但应保留它们各自的意义。正确率相近时，听者投入可能不同；两声流报告增多时，理解成绩也可能没有改善。多维评价有助于避免把某个实验指标当成整个复杂环境聆听能力的替代物。[17](#ref-auditory-scene-analysis-automatic)[29](#ref-auditory-scene-analysis-neural2026)

## 听力损失与听觉设备

### 听力损失的影响具有任务依赖性

[听力损失](../hearing-loss/)可能使频谱、周期性或时域线索的利用发生变化。例如，频率选择性下降可以影响低次谐波的分辨及音高相关分离。但这不意味着所有听力损失者在所有场景分析任务中均表现较差：Valentine 与 Lentz 的宽带非谐波刺激研究未发现组间显著的分离能力差异。这类结果强调，应说明受损的线索和任务，而不是赋予一个笼统的能力标签。[13](#ref-auditory-scene-analysis-oxenham)[14](#ref-auditory-scene-analysis-broadband)

年龄、注意、记忆及材料经验还可能共同影响表现。纯音听阈提供可听性信息，不能完整描述场景组织；场景分析困难也不能单独诊断外周或中枢疾病。研究中应结合听力、刺激可听性及任务要求解释个体差异。[12](#ref-auditory-scene-analysis-prediction)[14](#ref-auditory-scene-analysis-broadband)

### 助听器与人工耳蜗

[助听器](../hearing-aid/)通过增益和其他处理改善输入，但放大所有声音并不自动解决声源归属。方向性、降噪和远程传声可以改变目标与背景的关系；评价时既要测量言语获益，也应关注是否保留了空间、音色与时域线索，以及处理延迟或伪迹是否干扰连续跟随。[29](#ref-auditory-scene-analysis-neural2026)

[人工耳蜗](../cochlear-implant/)将声音映射为电刺激，可用的频谱及周期性信息与正常声学听觉不同。[通道相互作用](../channel-interaction/)和有效频谱分辨率可能影响对象线索，但电极数量不能直接等同于可独立分离的声源数量。早期直接电刺激研究发现，一些使用者能够依据电极位置或时域包络差异产生分离报告，同时个体差异明显。[25](#ref-auditory-scene-analysis-chatterjee)[13](#ref-auditory-scene-analysis-oxenham)

[声码器](../vocoder/)可以在正常听力者中研究部分线索降质的作用，但声码器表现不能直接预测某位人工耳蜗使用者的场景分析能力。真实使用者还存在电极—神经接口、经验与适应差异。设备评价应结合具体任务和实际使用者数据，并区分声音差异辨别与声流形成。[25](#ref-auditory-scene-analysis-chatterjee)[13](#ref-auditory-scene-analysis-oxenham)

## 计算模型与公开实现

### 模型需要解释什么

计算场景分析可以研究分组机制，也可以服务于工程声音分离。前者关注模型是否预测人类的融合、分离、建立过程、错觉及个体行为；后者往往关注输出波形与目标的接近程度。两者有交集，但较高的工程分离性能不能单独证明模型模拟了人脑组织方式。用人类行为和神经数据检验模型时，应说明比较的是哪个层次。[20](#ref-auditory-scene-analysis-models)[6](#ref-auditory-scene-analysis-cusimano)

| 模型方向 | 主要思想 | 常见解释对象 | 使用时的边界 |
| --- | --- | --- | --- |
| 频率通道、适应与竞争 | 不同声音激活不同通道，响应随历史及竞争变化 | 交替音、速率效应与部分建立过程 | 不能仅凭频位分离解释所有同步复杂声音 |
| 时域相干性 | 根据多个特征随时间变化的关系进行绑定 | 同步分组、图形—背景及复杂声流 | 特征表示与整合尺度影响预测 |
| 预测与生成模型 | 推断哪些声源及事件能够生成当前输入 | 连续性、歧义刺激和自然声音混合 | 依赖声源先验、合成器及推断方法 |
| 神经网络声音分离 | 从训练数据学习估计目标声音 | 多说话者分离与设备处理 | 波形还原成功不等于人类知觉组织一致 |

### 时域相干模型

Elhilali 等及 Teki 等的论文给出了模型思想、方法和刺激信息，可用于研究跨频率动态关系如何支持组织。本词条配图的相关运算只是教学实现；若复现论文，应根据原方法确定听觉表示、时间尺度、相干性矩阵及决策方式，并与论文使用的任务一致。不能把简单包络相关的阈值人为设成“一个声源”判据后，声称已经复现完整模型。[7](#ref-auditory-scene-analysis-coherence)[21](#ref-auditory-scene-analysis-teki)

模型论文入口：[Elhilali 等，2009](https://doi.org/10.1016/j.neuron.2008.12.005)、[Teki 等，2013，开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3721234/)。听觉前端可以参考[听觉建模工具箱的官方文档](https://amtoolbox.org/doc.php)，其中的滤波和听觉模型模块可为实现提供基础；前端工具箱本身不等于通用的场景分析模型。[30](#ref-auditory-scene-analysis-amt)

### 贝叶斯听觉场景合成

生成模型先描述可能的声源、事件及其参数，再通过声音合成与输入比较来推断场景。概念上，可将这一关系表示为：

$$
p(S\mid x)\propto p(x\mid S)\,p(S).
$$

其中 $S$ 为候选场景，$p(S)$ 为场景先验，$p(x\mid S)$ 为该场景生成当前输入的可能性。该式表达推断原则，并不说明人脑以精确概率表实现运算。具体模型还需要规定声源结构、噪声假设、参数及近似推断过程。[6](#ref-auditory-scene-analysis-cusimano)

Cusimano、Hewitt 与 McDermott 的 2024 年研究将这一思想用于经典错觉及日常声音混合，同时通过人类与模型的差异检验生成假设。公开入口包括[项目演示](https://mcdermottlab.mit.edu/mcusi/bass/)和[代码仓库](https://github.com/mcusi/bass)。仓库明确说明代码主要用于展示论文与实验逻辑，并非完整可直接执行的软件包；复现时需要核对推断流程、计算环境和实验数据。[6](#ref-auditory-scene-analysis-cusimano)[31](#ref-auditory-scene-analysis-bass)

### 声音纹理的统计合成

声音纹理模型通过分析听觉通道及调制表示中的统计量，再合成具有类似统计特征的新声音，检验哪些信息足以支持纹理识别。[STSstep 代码仓库](https://github.com/rmcwalter/STSstep)提供相关合成与纹理变化的 MATLAB 实现，基于 McDermott 与 Simoncelli 的方法扩展；作者说明还需要 minFunc 优化工具及 LTFAT 工具箱。它用于研究纹理统计及其变化，不是从多说话者混合中逐个提取声源的通用算法。[4](#ref-auditory-scene-analysis-texture)[24](#ref-auditory-scene-analysis-mcwalter)[32](#ref-auditory-scene-analysis-sts)

### 工程声音分离与工具

[Asteroid](https://github.com/asteroid-team/asteroid) 提供基于 PyTorch 的声音分离模型、训练流程和数据集配方，可以作为比较算法的入口。运行时需要匹配具体配方所需的数据与依赖；已有模型在某一数据集上的表现不保证能推广到不同语言、房间或设备。若研究目标是人类场景分析，还应另行测量声流判断、错觉或目标行为，建立算法与知觉之间的联系。[33](#ref-auditory-scene-analysis-asteroid)

本词条的[配图生成脚本](/n3-hearingpedia/figures/auditory-scene-analysis/generate-figures.py)可复现五张合成示意图，使用 NumPy 与 Matplotlib，所有随机图形由固定种子产生。脚本不包含论文模型的完整实现，也未测量听者。它适合检查绘图参数及教学逻辑，不应作为临床评估或声音分离性能测试工具。

## 研究沿革与当前问题

### 从知觉分组到自然场景

Bregman 在 1990 年的专著中系统组织了同时分组、序列分组及经验相关组织的研究，形成听觉场景分析的理论框架。随后，实验逐渐从简单纯音扩展到复杂音、言语、随机图形—背景和环境声音，神经研究也从响应特征延伸到对象及注意的表征。发展过程表明，简单刺激提供可控机制线索，自然场景提供功能相关性，二者需要相互约束。[1](#ref-auditory-scene-analysis-bregman)[21](#ref-auditory-scene-analysis-teki)[27](#ref-auditory-scene-analysis-ding)

### 近期模型与选择性聆听

2024 年的生成模型研究提供了可从声音计算出候选解释的框架，使经典错觉与真实混合声音能够放在同一模型中检验。模型的价值不只在于符合已有现象，也在于暴露哪些声源假设仍不足以解释人类知觉。由模型得到的声源结构应与人类报告比较，而不能只依赖模型内部的自洽性。[6](#ref-auditory-scene-analysis-cusimano)

2026 年的脑控选择性聆听研究使用四名因临床需要接受颅内记录、听力自报正常的参与者，实时解码注意并调节竞争言语的相对声级；还让另一个听力损失群体评价由这些解码结果产生的声音。研究报告了知觉收益，但后一个群体并未用自己的脑信号实时控制系统。这一设计区分对于理解证据至关重要：它支持目标选择与增强结合的研究方向，尚不能被表述为普通用户已经可以通过无创设备获得同等效果。[29](#ref-auditory-scene-analysis-neural2026)

### 尚未统一解决的问题

目前仍需解释不同线索如何在自然声音中被联合使用、场景组织如何随目标及经验变化，以及实验室声流指标能在多大程度上预测真实交流困难。模型比较应包括对不同条件的推广和失败案例；设备研究应考虑移动声源、混响、注意切换与长期使用，而不只采用固定的双说话者任务。[20](#ref-auditory-scene-analysis-models)[6](#ref-auditory-scene-analysis-cusimano)[29](#ref-auditory-scene-analysis-neural2026)

## 相关词条与阅读路径

理解声学线索可先阅读[听觉滤波器](../auditory-filter/)、[基频](../fundamental-frequency/)、[谐波性](../harmonicity/)和[时域包络](../temporal-envelope/)；理解复杂环境中的行为可结合[掩蔽](../masking/)、[空间听觉](../spatial-hearing/)、[听觉注意](../auditory-attention/)及[言语可懂度](../speech-intelligibility/)；理解听觉设备中的应用可进一步阅读[听力损失](../hearing-loss/)、[助听器](../hearing-aid/)、[人工耳蜗](../cochlear-implant/)和[声码器](../vocoder/)。这些词条分别介绍输入表征、组织与选择、行为结果和设备处理，合在一起构成复杂场景聆听的知识链。
