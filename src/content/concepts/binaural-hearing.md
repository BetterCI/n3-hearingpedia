---
title: "双耳听觉"
english: "Binaural hearing"
slug: "binaural-hearing"
summary: "系统介绍双耳输入与交互、融合与解掩蔽、收益比较基线、设备线索变化、实验评价与计算模型，并区分双耳听觉和空间听觉。"
categories: ["psychoacoustics", "neuroscience", "speech"]
tags: ["双耳听觉"]
aliases: ["binaural hearing", "双耳聆听"]
status: "draft"
depth: "in-depth"
last_updated: "2026-10-07"
literature_checked_at: "2026-10-07"
authors: ["AI 辅助编写"]
knowledge_area: "perception"
kind: "function"
key_facts: [{"label": "输入条件", "value": "左右两耳的声学或电刺激输入"}, {"label": "主要现象", "value": "融合、响度总和、解掩蔽与空间线索利用"}, {"label": "关键区分", "value": "双耳输入、声像融合与实际收益分别评价"}]
references: ["binaural-hearing-grothe", "binaural-hearing-hawley", "binaural-hearing-loudness2014", "binaural-hearing-training", "binaural-hearing-loudness2016", "binaural-hearing-kan", "binaural-hearing-jelfs", "binaural-hearing-weighting", "binaural-hearing-bronkhorst", "binaural-hearing-durlach", "binaural-hearing-lindemann", "binaural-hearing-fusion", "binaural-hearing-dietz", "binaural-hearing-jeffress", "binaural-hearing-lavandier", "binaural-hearing-correlation", "binaural-hearing-aids", "binaural-hearing-asymmetry2026", "binaural-hearing-unilateral", "binaural-hearing-haspi2026", "binaural-hearing-adultci", "binaural-hearing-simulation", "binaural-hearing-cros", "binaural-hearing-amt-lindemann", "binaural-hearing-amt-dietz", "binaural-hearing-leclere", "binaural-hearing-amt-jelfs", "binaural-hearing-amt-code", "binaural-hearing-ild2025"]
batch: 3
order: 49
---

**双耳听觉**（binaural hearing）是听觉系统利用左右两耳输入来感知声音的功能。它既包括比较两耳声音的到达时间、声级和相关结构，也包括利用两耳相似或互补的信息完成检测、识别和知觉组织。日常生活中，人们借助这些信息判断声音来自左侧还是右侧，在多人交谈中跟随目标说话人，并形成声音的响度与空间印象。双耳听觉不是把两个单耳结果简单相加；其作用取决于输入信息、听觉状态和任务。[1](#ref-binaural-hearing-grothe)[2](#ref-binaural-hearing-hawley)[3](#ref-binaural-hearing-loudness2014)

双耳听觉与[空间听觉](../spatial-hearing/)高度重叠，但不是同义词。前者以“两耳的信息如何共同被利用”为主线，后者以“声音在哪里、空间关系怎样被感知”为主线。空间听觉还利用耳廓频谱、头部运动和经验，涉及方向、距离及声音位于头外的体验；双耳听觉则还包括无需报告位置的响度总和、同相与反相条件下的解掩蔽，以及跨耳互补信息组合。两者是交叉关系，而不是简单的包含关系。[1](#ref-binaural-hearing-grothe)[4](#ref-binaural-hearing-training)[5](#ref-binaural-hearing-loudness2016)

本词条介绍双耳输入、比较机制、主要知觉现象、评价方法和计算模型。[双耳整合](../binaural-integration/)进一步讨论两耳互补信息的组合，[双耳时间差](../interaural-time-difference/)讨论特定声学线索，[双耳可懂度级差](../binaural-intelligibility-level-difference/)讨论规定测试条件间的识别阈值差。拥有两只可工作的耳朵、佩戴两个设备、听成一个声音，以及噪声中言语成绩提高，分别属于不同层面的描述，不能相互替代。[6](#ref-binaural-hearing-kan)[7](#ref-binaural-hearing-jelfs)

## 双耳听觉的范围与基本概念

### 两耳输入与跨耳比较

一个声源的声音到达两耳时，会受到头部、躯干和外耳的不同影响。同一时刻，两耳的波形通常既有共同成分，也有不同的时间、幅度和频谱结构。听觉系统需要从这些输入中提取有用关系，而不是直接“看见”声源方向；[耳蜗](../cochlea/)首先按频率分析声音，左右声源位置并不是耳蜗上的左右位置。[1](#ref-binaural-hearing-grothe)[8](#ref-binaural-hearing-weighting)

在宽义上，双耳聆听也包含选择当前信息较好的耳朵。狭义的双耳交互则强调两耳关系的比较：一个单耳中不存在的时间差，只有把左右信号联系起来才有意义。因此，“两耳参与任务”与“利用跨耳差异”需要分开。某种双耳优势可以主要来自较好耳的声学条件，不能仅凭双耳成绩较高就确定发生了哪一种中枢比较。[9](#ref-binaural-hearing-bronkhorst)[2](#ref-binaural-hearing-hawley)

### 同耳式、异耳式与单耳呈现

实验中，**单耳呈现**只把刺激送到一耳；**双耳同信号呈现**把相同信号送到两耳，英文常称 diotic；**双耳异信号呈现**使左右信号有所不同，英文常称 dichotic。后者可以只改变目标的相位，也可以让两耳听到不同音节或不同频带，因而不能把所有异耳刺激都理解为自然空间声音。[10](#ref-binaural-hearing-durlach)[11](#ref-binaural-hearing-lindemann)

双耳同信号在耳机中可能形成居中的声像，但“居中”不一定等于“头外正前方”。自然声音带有方向相关的声学过滤、房间反射及头动线索；耳机中复制相同波形只规定了左右输入一致。讨论外化、定位或融合时，应该另外说明呈现方式和感知任务。[8](#ref-binaural-hearing-weighting)[6](#ref-binaural-hearing-kan)

### 与相邻词条的分工

| 概念 | 主要问题 | 典型评价 |
| --- | --- | --- |
| 双耳听觉 | 两耳输入如何共同参与感知 | 单耳与双耳比较、跨耳线索敏感性 |
| 空间听觉 | 声音位于哪里，空间关系如何形成 | 定位、距离、前后判断和外化 |
| 双耳整合 | 分配到两耳的信息怎样被组合 | 互补信息、融合及完整信息对照 |
| 双耳可懂度级差 | 规定双耳条件改变了多少识别阈值 | 材料和评分一致的配对阈值差 |

这张表用于说明内容侧重点，不代表四个概念互相独立。例如，两耳融合异常可能改变声像，也可能影响言语信息组合；空间分离带来的识别改善又可能同时包含较好耳和跨耳比较。关系应该通过刺激和对照条件说明，而不能只按词条名称划界。[12](#ref-binaural-hearing-fusion)[2](#ref-binaural-hearing-hawley)

## 两耳之间有哪些声学线索

### 双耳时间差

声源位于一侧时，声音到达近侧耳通常早于远侧耳。两耳到达时间的差称为双耳时间差，常用微秒或毫秒表示。本文约定 $\Delta t=t_L-t_R$，因此正值表示右耳先到达；研究中也常采用相反约定，比较数据前应检查定义。时间差由传播和信号处理共同决定，不能不说明符号就把正负值直接解释为左右。[9](#ref-binaural-hearing-bronkhorst)[13](#ref-binaural-hearing-dietz)

对较低频率的声音，波形周期内的时间关系可提供精细的双耳线索。对较高频率的调制声，缓慢变化的[时域包络](../temporal-envelope/)也可以携带时间差，但包络时间差的敏感性及使用方式不应直接等同于低频[时域精细结构](../temporal-fine-structure/)时间差。宽带自然声音还包含起始、多个频率成分和随时间变化的线索。[8](#ref-binaural-hearing-weighting)[13](#ref-binaural-hearing-dietz)

### 双耳声级差

声源相对于头部的位置会使两耳声压级不同，这一差值称为双耳声级差，常缩写为 ILD。本文约定右耳减左耳，对于相同阻抗参考下的 RMS 声压，可写为：

$$
\mathrm{ILD}=20\log_{10}\frac{p_{R,\mathrm{rms}}}{p_{L,\mathrm{rms}}}.
$$

正值表示右耳声级较高。对数字信号，这一表达式也可用于相对 RMS 幅度，但只有结合换能器与声学校准，才能把数字数值解释为耳旁声压级。电刺激电流的差值则另有量纲与参考，不能直接套用声学分贝的含义。[9](#ref-binaural-hearing-bronkhorst)[6](#ref-binaural-hearing-kan)

**头影效应**指头部造成的方向相关衰减。它在较高频率通常更明显，但真实双耳声级差还与声源距离、耳廓、房间反射和频率有关。头影不意味着一侧耳朵完全听不到声音，也不意味着全频带都具有同一个固定的差值。[8](#ref-binaural-hearing-weighting)[9](#ref-binaural-hearing-bronkhorst)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/binaural-hearing/01-two-ear-cues.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/binaural-hearing/01-two-ear-cues.svg" alt="声源传播关系与两耳时间、幅度的教学示例" loading="lazy" /></a>
<figcaption><p>图 1　两耳输入的时间和声级差。A 为右前方声源与两耳的概念几何，箭头不表示真实绕射路径；B 使用理想 500 Hz 稳态正弦，设定右耳领先 0.30 ms，右、左幅度分别为 0.8 和 0.4；C 根据稳态 RMS 幅度比计算右耳减左耳为 +6.02 dB。波形相对幅度在 ±1 内。B、C 的参数是独立设定的教学例子，不是由 A 的头部几何计算的传递函数，也不是人的固定时间差或声级差。</p></figcaption>
</figure>

### 双耳相位差与周期歧义

对频率为 $f$ 的单一正弦，以右耳相位减左耳相位定义两耳相位差时，在本文时间差约定下可写为 $\Delta\phi=2\pi f\Delta t$，但相位通常只记录一个周期内的值。因此，同一个相位关系可以对应相差整数个周期的延迟；频率越高，一个周期越短。仅从单一纯音的相位，不能无限精确、唯一地恢复声源方向。[14](#ref-binaural-hearing-jeffress)[11](#ref-binaural-hearing-lindemann)

“反相”指一耳信号相对另一耳乘以 −1。对于单一正弦，这等价于半周期相位变化；对于包含许多频率的言语或噪声，它不是给整个波形施加同一个固定时间延迟。研究反相信号时，应说明究竟反转目标、噪声还是两者，不能把所有操作写成“增加了某个双耳时间差”。[10](#ref-binaural-hearing-durlach)

### 耳间相关结构

两耳信号的相似程度也提供信息。互相关可以描述一个信号相对于另一个平移后有多相似；本文采用 $C_{LR}(\tau)=E[x_L(t)x_R(t-\tau)]$ 的约定，对右耳先到达的延迟副本，峰值位于正延迟。归一化可减少总体幅度的影响，但估计仍受分析时窗、频率范围及混响影响。[11](#ref-binaural-hearing-lindemann)[13](#ref-binaural-hearing-dietz)

零延迟相关、允许搜索延迟后的最大互相关，以及频域的相干函数不是完全相同的量。两耳信号只是错开一点时间时，零延迟相关可以下降，补偿延迟后的相关仍可能很高；完全反相的信号则可以具有很强的负相关。使用“耳间相干性”时应给出具体计算定义，不能只报告一个脱离频带和时窗的数字。[15](#ref-binaural-hearing-lavandier)[16](#ref-binaural-hearing-correlation)

## 两耳信息如何进入听觉通路

### 从单耳编码到双耳敏感性

左右耳各自把声学输入转换为听神经活动，随后在脑干及更高层级发生双耳信息交互。经典框架强调上橄榄复合体参与早期双耳处理，内侧上橄榄核与低频时间线索、外侧上橄榄核与声级线索密切相关。这里的分工是概括：神经元反应依赖兴奋与抑制、频率、刺激历史和物种，不能把全部人类双耳能力一一归给某个核团。[1](#ref-binaural-hearing-grothe)

两耳声学波形相同，也不保证神经表示完全相同。两侧听阈、频率选择性、同步编码和响度增长可以不同，设备还会加入增益或延迟。因此，研究双耳关系既要记录输入，也要考虑各耳如何编码输入；耳间“匹配”不只是在电脑上把两个数字文件设成一样。[1](#ref-binaural-hearing-grothe)[17](#ref-binaural-hearing-aids)[18](#ref-binaural-hearing-asymmetry2026)

### 符合检测与群体编码

Jeffress 的经典位置编码模型用内部延迟与符合检测解释时间差：左右活动在某一内部延迟下同时到达时，相关检测单元响应更强。这一模型是理解“比较时间关系”的重要入口，但它不是所有哺乳动物、全部频率与任务的统一解剖图。[14](#ref-binaural-hearing-jeffress)

哺乳动物研究还强调抑制时序、响应曲线及神经群体活动的比较。Grothe 等的综述指出，新的证据挑战了简单的教科书式定位模型。对于百科阅读，更合理的认识是：双耳时间差需要被神经计算，而具体实现可以有多个层级和机制；一个行为阈值不能唯一确定使用了哪一种神经电路。[1](#ref-binaural-hearing-grothe)

### 融合、侧化与识别可以分离

**双耳融合**描述两耳输入是否被听成一个整体声音；**侧化**描述耳机中声像偏向哪一侧。听成一个声音不等于侧化准确，能够侧化也不必说明两耳在音质或频率上理想匹配。Kan 等在双侧人工耳蜗使用者中控制电极刺激位置不匹配，发现即使出现偏离中心或多个声像，某些条件下仍可进行侧化。[6](#ref-binaural-hearing-kan)

融合范围也可能过宽。Reiss 等对双模态使用者的研究发现异常宽的跨耳音高融合和音高平均，提示“能够融成一个”未必总是有利于保持两耳频谱差异。这类发现提出可能的机制联系，但不能仅凭融合范围就预测某人的言语成绩；融合、线索辨别和识别仍需分别测量。[12](#ref-binaural-hearing-fusion)

## 双耳聆听带来的不同收益

### 头影与较好耳选择

目标与干扰位于不同方向时，头影可能使某一耳的目标—噪声比更好。利用这一耳，可以改善检测或识别，而无需证明听者进行了复杂的跨耳相位比较。应当区分“身体产生了较好耳输入”与“听者有效利用了它”；如果听力较差的一耳恰好获得声学优势，实际表现仍可能受可听性限制。[9](#ref-binaural-hearing-bronkhorst)[19](#ref-binaural-hearing-unilateral)

较好耳还可能随时间和频率改变。一个干扰声在左侧、另一个在右侧时，整个句子未必存在始终占优的同一耳；局部时频区间的优势与全句平均信噪比不同。模型中的“每个区间选择最佳耳”是一种有用假设，但它不自动意味着人能无代价地、即时地完成相同选择。[2](#ref-binaural-hearing-hawley)[20](#ref-binaural-hearing-haspi2026)

### 双耳冗余与响度总和

当两耳得到相似目标信息时，双耳条件有时比单耳更容易检测或识别，这常被称为冗余收益或双耳总和效应。相似信息增加了可利用的输入，但效应大小会受到声级、噪声条件、单耳基线和听觉不对称影响。两耳都有输入，并不保证所有听者、所有任务都获得同样的改善。[21](#ref-binaural-hearing-adultci)[3](#ref-binaural-hearing-loudness2014)

响度总和属于另一种评价维度：两耳同信号可能比单耳同声级更响，但不是“两耳声压在一只耳朵上相加”，也不能把主观响度比、等响声级差与识别阈值差混用。Moore 等分别测量等响条件并建立包含双耳抑制的响度模型，说明两耳组合具有非线性和条件依赖性。[3](#ref-binaural-hearing-loudness2014)[5](#ref-binaural-hearing-loudness2016)

### 双耳解掩蔽

双耳解掩蔽指利用目标与干扰不同的跨耳关系，提高目标检测或识别。一个经典耳机操作保持噪声在两耳同相，只把目标在一耳反相。虽然目标与噪声的单耳功率比保持相同，双耳关系发生了变化，因而可以检验超出单耳能量改善的收益。[10](#ref-binaural-hearing-durlach)[16](#ref-binaural-hearing-correlation)

传统纯音噪声检测常用双耳掩蔽级差，缩写 BMLD；言语任务则可以使用双耳可懂度级差等阈值比较。它们具有不同刺激、评分和条件，不能把纯音检测的级差直接作为日常对话的改善量。电刺激下的实验也必须保留载波速率、包络和同步条件，不能直接套用声学听者的数值。[16](#ref-binaural-hearing-correlation)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/binaural-hearing/02-phase-and-cancellation.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/binaural-hearing/02-phase-and-cancellation.svg" alt="两耳同相和目标反相条件的理想相减模型" loading="lazy" /></a>
<figcaption><p>图 2　反相目标如何提供超出单耳功率比的信息。A 为 N0S0：两耳噪声和目标均相同；B 为 N0Sπ：噪声不变，右耳目标反相。C、D 使用理想“左耳减右耳”：A 的目标与噪声同时消失，B 的共同噪声消失、目标成为两倍幅度。两条件的目标分量与噪声分量在每耳各自具有相同 RMS；不要求有限时窗中混合波形的 RMS 恰好相同。所有波形相对幅度在 ±1 内。图中没有加入等化误差、内部噪声或生理限制，因此只展示计算原理，不是人的实际输出或临床效果。</p></figcaption>
</figure>

### 双耳降噪收益与空间释放

双侧设备研究常把在固定空间配置中“加入声学信噪比较差的一耳后，超过较好单耳的收益”称为双耳降噪收益，英文称 binaural squelch。它是通过特定对照条件定义的功能收益，不能理解为一定存在某个字面上的神经降噪开关；不同文献对收益的名称和计算基线也可能不同。[9](#ref-binaural-hearing-bronkhorst)[21](#ref-binaural-hearing-adultci)

**掩蔽的空间释放**描述目标与干扰从同位变为分离后，检测或识别改善多少。它可能包含头影、跨耳解掩蔽和声源选择等作用，不能全部归为狭义双耳交互。Hawley 等通过改变干扰的数量和类型表明，空间分离和双耳收益具有任务依赖性；使用一种稳态噪声得到的结果，不能穷尽多人言语竞争的困难。[2](#ref-binaural-hearing-hawley)[19](#ref-binaural-hearing-unilateral)

### 互补整合与双耳干扰

如果把目标的不同频带或片段分别送到两耳，双耳输入可能提供比任一单耳更多的有效信息，这属于互补组合的问题。应同时设置左单耳、右单耳、跨耳组合和完整信息同耳呈现，控制总频谱覆盖、能量与时间关系。超出单耳的改善支持信息被利用，但完整信息同耳条件有助于判断跨耳组合是否仍有代价。[22](#ref-binaural-hearing-simulation)[12](#ref-binaural-hearing-fusion)

双耳干扰则指加入另一耳输入后任务表现变差。它可能涉及线索冲突、频谱平均、不对称、注意或设备处理，不能由一个组平均值确定单一原因，也不能把某类双耳干扰概括为“第二只耳朵总是有害”。跨频率竞争中的线索干扰，与某位设备使用者的双耳言语干扰还属于不同实验问题。[12](#ref-binaural-hearing-fusion)[17](#ref-binaural-hearing-aids)

## 如何量化双耳收益

### 先定义任务、单位与基线

对于识别正确率，可以定义双耳相对于较好单耳的差为 $A_B-\max(A_L,A_R)$；若 $A$ 用百分数表示，差值单位是**百分点**。对越低越好的[言语接收阈](../speech-reception-threshold/)，同一刺激配置下可以定义：

$$
G_{\mathrm{better}}=\min(\mathrm{SRT}_L,\mathrm{SRT}_R)-\mathrm{SRT}_B.
$$

按此约定，正值表示双耳阈值低于较好单耳，单位为 dB。相减方向、材料、目标正确率和呈现单位必须一致。左耳与右耳的识别得分相差多少，并不直接给出它们的声学信噪比差；成绩较好的耳与物理信噪比较好的耳也不保证始终相同。[2](#ref-binaural-hearing-hawley)[7](#ref-binaural-hearing-jelfs)

在左右耳很不对称时，只与较差单耳比较容易放大“收益”。选择较好耳的基线也要注意测量误差：如果只用一次噪声较大的测量决定哪一耳最好，随后计算的差值可能受到选择偏差影响。应保留两耳原始结果、重复测量和配对不确定性，而不只呈现一个收益柱形。这里的统计提醒来自差值和选择操作本身，不构成某一种双耳模型的神经结论。

### 同位与分离条件下的阈值差

若同位与分离条件都使用双耳，可定义：

$$
\mathrm{SRM}=\mathrm{SRT}_{B,\mathrm{co}}-\mathrm{SRT}_{B,\mathrm{sep}}.
$$

这一空间释放指标与上式的双耳超出较好单耳收益不同：前者改变声源配置，后者固定配置、改变聆听耳数。二者可能共同受到头影和跨耳关系影响，但不能不经过完整对照就相互替代，更不能把不同基线的差值直接相加。[9](#ref-binaural-hearing-bronkhorst)[2](#ref-binaural-hearing-hawley)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/binaural-hearing/03-benefit-baselines.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/binaural-hearing/03-benefit-baselines.svg" alt="人工阈值示例中不同双耳收益基线的比较" loading="lazy" /></a>
<figcaption><p>图 3　收益的数值取决于比较基线。人工设定同位双耳 SRT 为 0 dB SNR；同一个分离配置下，左单耳为 −4、右单耳为 +2、双耳为 −6 dB SNR。左右单耳差为 6 dB，双耳超出较好单耳为 2 dB，双耳从同位到分离的空间释放为 6 dB。前两项相加得到 8 dB，并不等于后一项，因为参考条件不同。数值只用于演示差值逻辑，没有误差条，也不是正常听力或人工耳蜗人群的实测结果。</p></figcaption>
</figure>

### 为什么单一测验不够

定位、相位差检测、言语识别、响度判断和融合报告测量不同能力。Rothpletz 等的单侧听力损失研究中，定位表现存在明显个体差异，而特定信息性掩蔽任务中的空间选择收益不能直接由定位能力解释。这个结果提醒人们：某项空间任务表现较好，不保证另一项双耳任务同样正常。[19](#ref-binaural-hearing-unilateral)

评价至少需要说明目标与干扰的方位、干扰数量和类型、测试耳、声级或信噪比、材料、评分，以及是否允许转头。左右耳听阈、响度平衡和设备配置也应记录。测试应按问题选择：研究跨耳比较时尽量控制单耳功率线索；研究真实交流时则需要保留真实线索，并另行讨论哪些机制可能共同贡献。[2](#ref-binaural-hearing-hawley)[6](#ref-binaural-hearing-kan)

## 实验方法与声学控制

### 声场与耳机

声场中可以使用多个扬声器呈现目标和干扰，让头部及耳廓自然形成双耳线索；但房间反射、扬声器传递和头动都可能改变输入。耳机可以精确操纵两耳时间、声级或相位，也可以用头相关传递函数模拟方向；但非个体化传递函数、耳机校准和头动反馈会影响空间印象。[9](#ref-binaural-hearing-bronkhorst)[8](#ref-binaural-hearing-weighting)

控制左、右通道不是只检查播放软件的标签。采样率、通道延迟、串扰、输出声级和音频接口同步都与结果相关。数字采样间隔限制直接整数采样移位的步长，必要时应使用经过验证的分数延迟方法；耳机的物理佩戴和耳道耦合则可能产生额外频谱差异。后者不能通过把左右数字 RMS 设成一样就完全解决。

### 固定延迟与互相关估计

对同一个宽带信号的延迟副本，互相关通常可以显示接近设定延迟的峰；但单一正弦会产生重复的峰，混合多个声源也会出现多种延迟关系。一个全频、全句互相关峰可能由最强干扰主导，并不一定对应目标说话人的方向。模型因此往往先作频率分析，再考察局部可靠性和多个区间。[11](#ref-binaural-hearing-lindemann)[13](#ref-binaural-hearing-dietz)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/binaural-hearing/04-correlation-and-ambiguity.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/binaural-hearing/04-correlation-and-ambiguity.svg" alt="宽带信号与单一正弦的互相关延迟歧义" loading="lazy" /></a>
<figcaption><p>图 4　互相关估计的适用条件。A 为同一 150–5000 Hz 带通信号的左右副本，采样率 48 kHz，左耳延后 14 个采样，即约 0.292 ms；按正文的互相关定义，峰值位于正延迟。B 为同样时差的理想无限长 500 Hz 正弦，其互相关每 2 ms 重复，展示周期歧义。B 的多个峰是解析模型结果，不是人体能够使用任意大时间差的证据；两面板均不是实测头相关传递函数。</p></figcaption>
</figure>

### 相位、包络与频位匹配

研究包络双耳关系时，应确认是否同时引入载波时间差、载波相关变化或可听的单耳调制差。两耳同源载波与独立载波可能产生不同跨耳结构；“包络相同”不足以说明两个完整波形相同。Goupell 与 Litovsky 的同步电刺激实验还说明，包络相关辨别受参考相关、包络带宽和载波速率等条件影响。[16](#ref-binaural-hearing-correlation)

双耳频率或电极位置匹配同样需要明确定义。同一频率分配表不必刺激相同的耳蜗位置；音高相等、影像中的位置接近和双耳线索敏感性最好，也不必是完全相同的匹配标准。实验应该说明使用了何种依据，以及它针对的任务，避免把一个匹配步骤称为消除了所有不对称。[6](#ref-binaural-hearing-kan)[22](#ref-binaural-hearing-simulation)

## 听力损失与两耳不对称

### 听阈之外的双耳功能

[纯音测听](../pure-tone-audiometry/)描述每耳在各频率上的检测敏感度，但没有直接测量两耳时间差敏感性、噪声中跨耳信息利用或融合。因此，两耳听力图接近，并不保证全部双耳能力相同；听力图存在差异，也不能单凭差值推定某一机制完全失效。测试需要把可听性与阈上信息利用区分。[19](#ref-binaural-hearing-unilateral)[16](#ref-binaural-hearing-correlation)

单侧听力损失可能减少可用的自然双耳比较，特别影响某些定位和竞争声任务，但不意味着所有场景都无法理解言语。人可以利用保留耳的可听性、频谱与经验补偿部分困难。评价时要区分头影造成的输入不利、缺少跨耳线索，以及对特定线索的学习与重加权。[19](#ref-binaural-hearing-unilateral)[4](#ref-binaural-hearing-training)

### 儿童、听觉经历与适应

两耳信息的长期平衡是发育和适应的重要背景。儿童的双侧损失、先后植入时间、不同设备及语言经验可能共同影响后续表现。不能把成人正常听力耳机实验直接作为儿童双侧设备收益的常模，也不能从横断面的组差异单独确定某一个发育原因。[18](#ref-binaural-hearing-asymmetry2026)[21](#ref-binaural-hearing-adultci)

成人也可以重新学习改变后的线索。Hofman 等通过改变外耳形状，观察到仰角定位逐渐适应新频谱线索；这项证据主要涉及单耳频谱与空间校准，不是双耳时间差训练恢复的直接证明。在双耳听觉中引用适应研究，应保留它实际改变的线索与测量任务。[4](#ref-binaural-hearing-training)

### 双耳响度与对称性

两耳增益或电流在数值上对称，不一定使响度对称；各耳的阈值、动态范围与响度增长不同，都可能改变居中声像和主观舒适度。声像居中又不等于频位理想匹配，调整声级能够缓解某个位置偏移，也可能同时改变声级线索。应把响度平衡、融合与线索敏感性分别验证。[3](#ref-binaural-hearing-loudness2014)[6](#ref-binaural-hearing-kan)

## 助听器、人工耳蜗与双耳线索

### 双侧助听器

双侧[助听器](../hearing-aid/)可以改善两耳可听性，但独立的[动态范围](../dynamic-range/)压缩、降噪、方向性和频率降低会改变声级及时间关系。Brown 等用真实数字助听器和人工头记录输入输出，考察了非线性频率压缩等处理引入的双耳线索变化。设备具有两个通道，不能据此认定输出保留了自然双耳线索。[17](#ref-binaural-hearing-aids)

设备评价应同时关注目标可懂度与空间信息。某种处理提高目标信噪比时，可能改变残余噪声的声像或目标—干扰的空间关系；效果取决于场景与实现，不是所有线索变化都产生相同损害。记录两耳输出、分析时间和声级关系，再用行为任务检验，比只比较一个总体降噪量更有解释力。[17](#ref-binaural-hearing-aids)[20](#ref-binaural-hearing-haspi2026)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/binaural-hearing/05-device-cue-changes.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/binaural-hearing/05-device-cue-changes.svg" alt="示意增益与延迟对双耳声学线索的改变" loading="lazy" /></a>
<figcaption><p>图 5　设备处理的耳间差异。A 固定右耳减左耳输入声级差为 6 dB，加入两耳不同且随左耳输入级变化的示意增益后，输出差值随输入级改变；图中增益函数是人为指定的，不是验配处方或商业压缩器。B 固定左耳减右耳输入时差为 +0.3 ms：若左、右设备分别附加 2、5 ms 延迟，输出变为 −2.7 ms；两耳同加 2 ms 时差仍为 +0.3 ms。此处只计算固定延迟的差值，不模拟群时延、时钟漂移或人的声像。</p></figcaption>
</figure>

### 双侧人工耳蜗

双侧[人工耳蜗](../cochlear-implant/)使两耳都能接收电刺激，提供了较好耳利用和双耳交互的机会，但自然低频精细结构时间差不一定被常规处理器以可利用方式传递。独立处理、频位不匹配、耳间动态范围和听觉经历等还会影响收益，不能把“植入两侧”写成“恢复了全部正常双耳听觉”。[21](#ref-binaural-hearing-adultci)[6](#ref-binaural-hearing-kan)[16](#ref-binaural-hearing-correlation)

同步研究接口可以帮助控制电刺激时间关系。Goupell 与 Litovsky 在同步处理器、单对匹配电极和特定载波条件下测量包络相关与解掩蔽，显示部分使用者能够利用这些线索；这不等于日常处理器、多电极连续言语条件已经产生相同收益。研究结论应带着接口、刺激与对照条件一起阅读。[16](#ref-binaural-hearing-correlation)

### 双模态与单侧失聪的声音转送

一侧人工耳蜗、另一侧助听器构成双模态聆听，两耳分别获得电听觉与声听觉信息。残余低频线索可以补充言语信息，但接口、音高、响度和处理延迟的差异也会影响融合。Reiss 等提出异常跨耳频谱整合可能参与部分使用者的收益差异；该发现支持开展个体测量，不能据此默认所有双模态聆听都会受干扰。[12](#ref-binaural-hearing-fusion)

把较差侧的声音转送到较好耳，可以改善该侧声音的可达性，却没有在两耳各自建立正常的独立输入。CINGLE 研究比较单侧失聪的人工耳蜗、骨导装置和对侧信号传输助听器，结果随言语与噪声方位改变；短期测试中，部分转送配置还会把不利干扰引入较好耳。装置用途应与“双耳功能恢复”分开表述，不在本词条中据此作个体治疗选择。[23](#ref-binaural-hearing-cros)

## 计算模型与公开实现

### 互相关、符合检测与方向估计

互相关模型先建立两耳的频率或神经活动表示，再比较不同内部延迟下的共同变化。Lindemann 模型加入对侧抑制与单耳检测机制，用来描述单纯互相关不能完整解释的侧化现象。公开的[听觉建模工具箱](https://www.amtoolbox.org/)提供 [lindemann1986 模型文档](https://www.amtoolbox.org/amt-1.6.0/doc/models/lindemann1986.php)和源码入口；输出是模型双耳活动，不是脑干电位的直接测量。[11](#ref-binaural-hearing-lindemann)[24](#ref-binaural-hearing-amt-lindemann)

Dietz 等的方向估计模型分析时域精细结构、包络、声级差与耳间相干性，用可靠性线索辅助处理同时存在的声源。[dietz2011 文档](https://www.amtoolbox.org/amt-1.6.0/doc/models/dietz2011.php)说明输出参数和处理环节。方向估计正确，不意味着模型已经预测完整言语理解、外化或听力损失；模型的适用任务与验证条件仍需单独核对。[13](#ref-binaural-hearing-dietz)[25](#ref-binaural-hearing-amt-dietz)

### 等化—抵消模型

Durlach 的等化—抵消理论先通过增益和延迟使两耳掩蔽成分尽量一致，再相减以减弱掩蔽。一个教学表达式为：

$$
y(t)=x_L(t)-\alpha x_R(t-\delta),
$$

其中 $\alpha$ 与 $\delta$ 是为匹配掩蔽而设置的相对增益和延迟。若目标与掩蔽具有不同跨耳关系，抵消可能保留目标；若二者关系相同，目标也会被削弱。实际理论加入处理误差，因而不预测理想图示那样无限精确的噪声消除。[10](#ref-binaural-hearing-durlach)

这一表达式是功能模型，不宣称神经系统逐样本执行电脑上的减法。对多个干扰、混响或非平稳声音，单一增益与延迟可能不能匹配所有成分；模型扩展通常需要分频、时变处理和内部限制。使用完整论文参数复现理论，与展示一个无误差相减示例，是不同程度的实现。[10](#ref-binaural-hearing-durlach)[15](#ref-binaural-hearing-lavandier)[26](#ref-binaural-hearing-leclere)

### 双耳言语可懂度模型

Lavandier 与 Culling 的模型结合单耳条件、双耳解掩蔽和频率权重，解释指定噪声与房间条件下的阈值。Jelfs 等进一步修订并验证计算方式。[jelfs2011 官方文档](https://www.amtoolbox.org/amt-1.6.0/doc/models/jelfs2011.php)给出总体收益、较好耳分量与双耳解掩蔽分量，还强调多个干扰的输入组织方式。数值分解属于模型假设下的预测，不等于实验已经独立测量每一机制。[15](#ref-binaural-hearing-lavandier)[7](#ref-binaural-hearing-jelfs)[27](#ref-binaural-hearing-amt-jelfs)

混响既可能降低耳间相关，也可能使目标时域结构模糊。Leclère 等扩展模型以考虑这些作用，但其研究表明某些参数不能无条件跨房间推广。因此，不能仅输入一个房间混响时间，就宣称已精确预测任意听者的双耳言语成绩。[26](#ref-binaural-hearing-leclere)

### 双耳响度模型与模型选择

包含双耳抑制的响度模型分别估计两耳内部响度表示及其交互，再形成总体响度。这类模型适于响度及等响比较，与通过相减提高目标检测的模型具有不同目标。选择模型应先确定要预测的是侧化、融合、响度、检测阈值还是言语识别，并确认所需输入能否取得。[5](#ref-binaural-hearing-loudness2016)

AMT 的官方[开发与源码说明](https://www.amtoolbox.org/development.php)指向 [SourceForge 项目](https://sourceforge.net/projects/amtoolbox/)及其代码仓库。部分模型提供网页源码与示例，可以核查输入和计算步骤；本稿未运行这些第三方完整模型。本词条的[配图生成代码](/n3-hearingpedia/figures/binaural-hearing/generate-figures.py)仅实现合成波形、理想抵消、阈值差及互相关演示，不能代替完整 AMT 模型或临床测试。[28](#ref-binaural-hearing-amt-code)

## 研究沿革与近期进展

### 从方向线索到复杂场景

经典时间差理论与互相关模型提供了理解双耳比较的框架；等化—抵消理论则把重点移到噪声中的目标检测。此后，研究逐渐将两耳线索与多人言语竞争、房间混响、响度、不对称和设备处理联系起来。其共同变化是从“存在某种双耳线索”，进一步追问“在这个听者和场景中能否有效利用”。[14](#ref-binaural-hearing-jeffress)[10](#ref-binaural-hearing-durlach)[2](#ref-binaural-hearing-hawley)

### 线索增强不等于单耳信噪比提高

Richardson 等 2025 年研究用瞬时双耳时间差估计产生增强的声级差，并在对称干扰配置中考察言语识别。该配置减少自然长期较好耳优势，研究包括正常听力声码器模拟与实际双侧植入使用者，结果支持线索增强在所测条件中的作用。它是受控研究，不能直接写成全部临床处理器已有的标准策略。[29](#ref-binaural-hearing-ild2025)

该方法对每个时频区间的两耳混合信号施加相对衰减，不分别修改区间中的目标与噪声。因此，区间内目标—掩蔽比不因同一增益而改变；不同区间的加权仍可能影响汇总指标。解释收益时应保留局部与总体量的区别，不把“没有单区间信噪比改善”自动扩大成所有全句能量比例都不变。[29](#ref-binaural-hearing-ild2025)

### 两耳编程与听觉经历

Sabourin 等 2026 年回顾性研究分析 542 名双侧植入儿童的编程参数与外周神经反应，发现编程不对称与植入顺序的联系比与某些电极阵列类型差异的联系更突出。它提示双耳匹配不仅是硬件问题，也涉及既往听觉经历；回顾性关联不单独证明唯一中枢原因，更不能把编程差值直接换算成定位误差。[18](#ref-binaural-hearing-asymmetry2026)

### 为单耳预测模型增加双耳前端

Lavandier、Kates 与 Arehart 2026 年提出双耳前端，将两耳的含噪输入和干净参考转换为增强的单耳信号，再使用言语感知指标 HASPI 预测。所测正常听力、耳机、无混响数据中，静态前端对空间分离稳态噪声较有效，对弥散噪声仍有低估；时变前端在低信噪比下出现高估。该研究尚未验证听力损失或混响条件，体现了模型的进展，也提供了清楚的适用边界。[20](#ref-binaural-hearing-haspi2026)

这些研究没有形成一个可以替代所有双耳测验的指标。今后的核心问题包括：模型是否保留真实单耳与跨耳线索，是否适用于不同听觉状态，能否解释个体差异，以及实验室的收益是否转化为实际交流和空间感知。检验应依赖多种任务和独立数据，而不只依赖某一条平均收益曲线。

## 相关词条

本词条与[空间听觉](../spatial-hearing/)、[双耳时间差](../interaural-time-difference/)、[双耳整合](../binaural-integration/)及[双耳可懂度级差](../binaural-intelligibility-level-difference/)组成相互衔接的专题。理解噪声中收益还可以结合[掩蔽](../masking/)、[听觉场景分析](../auditory-scene-analysis/)、[言语可懂度](../speech-intelligibility/)和[言语接收阈](../speech-reception-threshold/)；设备应用则与[听力损失](../hearing-loss/)、[助听器](../hearing-aid/)、[人工耳蜗](../cochlear-implant/)及[频位映射关系](../tonotopy/)交叉阅读。
