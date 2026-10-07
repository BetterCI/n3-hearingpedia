---
title: "听觉注意"
english: "Auditory attention"
slug: "auditory-attention"
summary: "系统介绍目标选择、持续维持与注意切换，区分声源分组、理解和聆听努力，并比较神经机制、注意解码模型及验证方法。"
categories: ["neuroscience","speech","psychoacoustics"]
tags: ["auditory-attention"]
aliases: ["选择性听觉注意", "selective auditory attention", "auditory attention"]
status: draft
depth: in-depth
last_updated: "2026-10-07"
authors: ["AI 辅助编写"]
references: ["auditory-attention-object", "auditory-attention-golumbic", "auditory-attention-continuity", "auditory-attention-hearing", "auditory-attention-fuel", "auditory-attention-escera", "auditory-attention-switch", "auditory-attention-sustained", "auditory-attention-mesgarani", "auditory-attention-osullivan", "auditory-attention-noattention", "auditory-attention-ownname", "auditory-attention-hillyard", "auditory-attention-kerlin", "auditory-attention-methods", "auditory-attention-ding", "auditory-attention-alpha", "auditory-attention-wostmann", "auditory-attention-binding2025", "auditory-attention-matrix2025", "auditory-attention-gaze2024", "auditory-attention-dataset-kul", "auditory-attention-mtrf", "auditory-attention-unsup", "auditory-attention-code-mtrf", "auditory-attention-code-python", "auditory-attention-code-unsup", "auditory-attention-dataset-gaze", "mo-ci-adaptation-2026", "auditory-attention-classroom2025", "auditory-attention-virtual2025"]
batch: 3
order: 37
literature_checked_at: "2026-10-07"
knowledge_area: "perception"
kind: "function"
key_facts: [{"label": "功能维度", "value": "选择、维持、切换与干扰抵抗"}, {"label": "主要测量", "value": "行为任务、神经响应及注意解码"}, {"label": "关键区分", "value": "注意选择、理解成绩与资源投入"}]
---

**听觉注意**是根据当前目标、任务和声音环境，对听觉信息进行选择、维持、切换与优先处理的功能。在餐厅里跟随同伴的谈话、课堂上关注教师、合奏中追踪某件乐器，都需要在同时存在的声音中保持与任务有关的信息。注意改变声音的加工与利用，却不意味着耳朵只接收被关注的声源，也不意味着其他声音完全不进入神经系统。[1](#ref-auditory-attention-object)[2](#ref-auditory-attention-golumbic)

听觉注意与[听觉场景分析](../auditory-scene-analysis/)相互影响。场景分析关心混合声音如何被组织成可区分的声源或知觉流；注意关心哪些对象被优先选择、哪些信息需要持续加工。稳定的声源表征可帮助注意选择，注意又可能强化目标的表征。因此，两者具有联系，但不能用“能分开两个人的声音”替代“能持续听懂其中一个人”。[1](#ref-auditory-attention-object)[3](#ref-auditory-attention-continuity)

听觉注意也是理解[言语可懂度](../speech-intelligibility/)、[听觉努力](../listening-effort/)、[听力损失](../hearing-loss/)和听觉辅助设备的重要环节。听者可能正确选择了目标，却因信号不清楚而无法理解；也可能投入较大努力维持目标，最终取得与较容易条件相近的成绩。注意对象、资源投入和任务成绩应分别测量。[4](#ref-auditory-attention-hearing)[5](#ref-auditory-attention-fuel)

## 概念范围与主要维度

### 目标驱动与刺激驱动

目标驱动注意来自听者当前的意图，例如提前知道要关注左侧说话者，或者从多件乐器中寻找小提琴。位置、说话者身份、音高、音色、节奏和内容都可以作为选择线索。不同线索可能联合使用，听者也可以在一位说话者移动时继续跟随其声音，说明关注对象不必固定在一个空间方位。[1](#ref-auditory-attention-object)[3](#ref-auditory-attention-continuity)

刺激驱动的注意转移则可由突然出现、显著改变或具有特殊意义的声音诱发，例如任务之外的异常声。它可能打断当前加工，但不是任何声学变化都会产生同等干扰。Escera 等人的研究将声音偏差、事件相关电位和另一任务中的行为干扰结合起来，表明不同类型的声音变化可以有不同的神经与行为表现。检测到变化与注意真正被转移，也需要区别。[6](#ref-auditory-attention-escera)

目标驱动与刺激驱动不是互不相干的两套开关。同一个提示声在某项任务中可能是需要主动寻找的目标，在另一项任务中则是无关干扰；听者的预期、经验和当前负荷都会影响它的作用。解释实验结果时，需要说明声音的物理属性，也需要说明指令与目标规则，不能仅根据“声音很响”判断注意的方向。[1](#ref-auditory-attention-object)[6](#ref-auditory-attention-escera)

### 选择、维持与切换

选择回答“此刻关注谁”，维持回答“能否继续跟随同一对象”，切换回答“目标改变后如何转向新的对象”。三者可在一次交流中连续发生：先确定同伴声音，持续跟随一句话，再转向另一位发言者。某项任务中选择目标准确，并不保证长时间维持和快速切换同样良好。[3](#ref-auditory-attention-continuity)[7](#ref-auditory-attention-switch)

维持并不意味着加工状态恒定不变。连续任务中的表现可能波动，疲劳、无关思绪或声音结构也会影响注意。2024 年一项持续听觉注意研究观察到神经言语跟随与 α 节律之间的动态关系及其与目标检测的关联。研究中的特定波动频率并非所有人、所有任务共有的“注意周期”，其内部／外部加工解释也需要与直接可观测的信号区分。[8](#ref-auditory-attention-sustained)

切换则有不同层面的含义：换一个声源、换一个方位、换一条选择规则，或者换一种反应方式。实验如果同时改变视觉提示和目标声音，测得的时间差可能包含提示识别、规则更新和反应选择，而不只是声音注意的重新分配。Koch 等人的研究通过改变提示设置，展示了这些因素需要分别控制。[7](#ref-auditory-attention-switch)

| 维度 | 示例问题 | 常见测量 | 需要避免的混淆 |
| --- | --- | --- | --- |
| 目标选择 | 应复述哪位说话者？ | 目标识别、干扰侵入、神经选择性 | 目标更响或更熟悉造成的优势 |
| 持续维持 | 能否跟随一段较长谈话？ | 随时间变化的漏报、正确率、反应时间 | 听不清、疲劳和任务未理解 |
| 注意切换 | 提示后能否转向另一声源？ | 切换相对重复试次的成绩变化 | 提示变化、规则更新和反应切换 |
| 干扰抵抗 | 无关声音是否打断当前任务？ | 误报、侵入错误、反应延迟 | 声学掩蔽与注意竞争混为一谈 |
| 分配注意 | 能否同时监测多路信息？ | 多目标检测与双任务代价 | 双任务结果不是固定“资源容量” |

## 与声源分组、可听度和理解的关系

### 混合输入相同，关注对象可以不同

在经典多说话者任务中，可以让听者对完全相同的声音混合物执行不同指令。若改变注意目标后，行为报告或神经响应也随之改变，就能更清楚地研究目标选择的影响。关键是控制输入，而不是始终把目标放得更响或只用某一位说话者作为目标。[9](#ref-auditory-attention-mesgarani)[10](#ref-auditory-attention-osullivan)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-attention/01-mixture-selection.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-attention/01-mixture-selection.svg" alt="合成声源与相同混合输入" loading="lazy" /></a>
<figcaption><p>图 1. 相同物理输入可以对应不同注意目标。A、B 是具有不同包络的合成载波，C 为两者相加后除以 2 的混合波形；在 C 保持不变时，指令可以要求关注 A 或 B。图中没有模拟注意后的神经响应，也不代表真实言语分离效果。声压波形的相对幅度均在 ±1 内；不同颜色只区分声源和混合物。</p></figcaption>
</figure>

### 声源形成与目标选择相互作用

在嘈杂环境中，目标并不是一条已经分离好的信号。听觉系统需要根据时间连续性、声音特征和空间线索，将属于同一对象的信息组织起来；当目标与干扰的声音特征接近，或者场景快速变化时，形成稳定对象可能更困难。注意选择依赖这种组织，但不能简单理解为先完全分离、再启动注意的严格串行流程。[1](#ref-auditory-attention-object)[4](#ref-auditory-attention-hearing)

Best 等人的目标数字序列研究发现，目标位置连续时识别表现更好，声音身份连续还能进一步促进选择的建立。这个结果说明，关注同一对象的优势可以随时间发展，而不只是在每个瞬间选择一个方位。它也解释了为什么日常交流中的快速轮流发言，可能比持续跟随同一人更费力。[3](#ref-auditory-attention-continuity)

另一方面，部分场景结构的加工可以在没有主动追踪每个声源时发生。Sohoglu 与 Chait 的研究在主动和被动聆听中都观察到对声音规律性的响应差异。这支持把自动组织与主动选择分别讨论；它既不证明全部场景分析无需注意，也不证明所有被动反应都代表已经形成完整的声源理解。[11](#ref-auditory-attention-noattention)

### 可听度、注意和理解是不同问题

声音可听意味着某些声学信息能够被检测，注意选择意味着这些信息或对象被优先处理，理解则涉及从中提取有意义的内容。听者可以注意一门不熟悉的语言而无法理解，也可以理解一句容易的目标话语，却漏掉同时出现的另一个任务事件。测量注意时不能只记录是否“听见”，测量理解时也不能只记录是否“关注”。[10](#ref-auditory-attention-osullivan)[5](#ref-auditory-attention-fuel)

因此，在噪声中复述成绩下降时，可能同时存在能量掩蔽、声源混淆、注意切换和记忆负荷等因素。明确目标、优化空间线索或提高目标声级，可能通过不同环节改善表现。实验应尽量识别具体机制，不能把所有困难都归为“注意力不集中”。[4](#ref-auditory-attention-hearing)[1](#ref-auditory-attention-object)

### 注意与听觉努力、工作记忆

注意与听觉努力都涉及任务控制，但侧重点不同。注意强调选择与优先加工，听觉努力强调为了克服障碍而有目的地投入心理资源。困难增加时，听者可能投入更多努力维持目标，也可能因任务过难或动机不足而减少投入。FUEL 框架将任务需求、可用容量和动机放在一起讨论，提醒我们不要把困难程度直接换算成努力。[5](#ref-auditory-attention-fuel)

工作记忆涉及暂时保留与使用信息，可帮助维持目标规则、整合句子或恢复漏掉的片段，但不是听觉注意的同义词。Conway 等人的姓名干扰研究发现，工作记忆指标与发现非目标通道中自己姓名的概率相关。这种关联来自特定任务，不能由一次姓名检测判断一个人的一般注意能力或工作记忆水平。[12](#ref-auditory-attention-ownname)

## 注意如何影响声音加工

### 从短声诱发反应到连续言语

经典短声研究发现，相同或可比较的声音在被关注与被忽略条件下，诱发电位成分可以不同。Hillyard 等人的双耳分听研究观察到被关注短声的早期负向成分增强，后期成分又与稀有目标识别有关。这里的不同潜伏期反映特定任务与成分，不能把某个时间点当作听觉注意唯一启动时刻。[13](#ref-auditory-attention-hillyard)

连续言语研究则关注神经活动如何随正在进行的声音变化。在[言语神经跟踪](../neural-speech-tracking/)研究中，常用[时域包络](../temporal-envelope/)等特征与神经信号建立统计关系，比较目标与非目标声音的对应程度。神经跟踪是研究表征的方法，不等于神经系统只处理包络，也不等于每个跟踪峰都对应一个独立认知步骤。[14](#ref-auditory-attention-kerlin)[15](#ref-auditory-attention-methods)

### 皮层表征具有任务选择性

Mesgarani 与 Chang 使用人类皮层表面记录，发现双说话者条件下的响应包含对被关注说话者的选择性，从神经信号重建的频谱具有目标声音的关键特征。这直接支持皮层表征受到当前任务目标影响。但该证据来自特定手术患者与记录位置，其空间分辨率、信噪比和覆盖范围都不同于头皮脑电。[9](#ref-auditory-attention-mesgarani)

Zion Golumbic 等人的记录进一步表明，不同区域中目标与非目标声音的表征并不一样：某些较低层级区域仍可记录到被忽略声音的跟踪，而较高区域表现出更强的选择性。这里的“未检测到”需要保留记录与分析灵敏度的边界，不能解释为脑内所有无关信息都彻底消失。[2](#ref-auditory-attention-golumbic)

Ding 与 Simon 的脑磁研究则提供了对象层面加工的证据：当目标和背景声级分别变化时，目标表征的变化更依赖目标声自身，而非整个混合物的总强度。不同记录方法相互补充，但不能根据它们都观察到选择性，就将一个方法的具体潜伏期直接套用到另一个方法。[16](#ref-auditory-attention-ding)

### 目标增强与干扰抑制

更好地处理目标与更少地处理干扰，是注意选择的两种可能贡献。若实验只比较“关注左”与“关注右”，两种贡献往往一起改变，很难独立判断。Wöstmann 等人的空间任务通过固定目标或固定干扰，发现与目标选择和干扰抑制有关的 α 侧化可以表现出不同方向及关系，支持将二者分别研究。[17](#ref-auditory-attention-alpha)

但 α 节律的变化不是通用的“注意量表”。它可能随位置、任务阶段和声音时序变化，空间侧化也依赖设计。Wöstmann 等人的数字流研究发现，α 侧化随言语速率动态起伏；这说明平均功率可能掩盖时间结构，也提醒我们不要把某个频段活动变强简单翻译为注意增加或理解更好。[18](#ref-auditory-attention-wostmann)[14](#ref-auditory-attention-kerlin)

## 持续注意、切换与干扰

### 稳定跟随与重复目标

保持同一目标能够利用声音身份和位置的连续性，但真实交流往往包含停顿、重叠和轮换。目标暂时不发声时，听者仍可能保持对其身份或位置的预期；另一位说话者插入时，则需要决定继续维持还是转向新对象。行为研究可以分别操纵目标连续性和指令切换，以了解两者的作用。[3](#ref-auditory-attention-continuity)[7](#ref-auditory-attention-switch)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-attention/02-maintain-switch.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-attention/02-maintain-switch.svg" alt="维持与切换目标的试次安排" loading="lazy" /></a>
<figcaption><p>图 2. 维持与切换目标的实验结构示意。A、B 两行提供相同的声源片段和提示时刻，差别在于提示要求持续关注 A，还是从 A 转向 B。彩色条块表示事件安排，粗线表示指令指定的目标，不是实测注意强度。时间仅为教学示例；要分离声音切换与视觉提示变化，还需在正式实验中加入提示控制。</p></figcaption>
</figure>

### 切换成本与准备效应

切换成本常指切换试次相对重复试次的反应时间增加或正确率下降，但具体数值依赖任务。更长的准备时间可能帮助调整目标，也可能主要改变提示处理或声音特征的绑定。因此，反应变快、目标特征选择更独立、无关特征干扰更小，不必同时发生。[7](#ref-auditory-attention-switch)[19](#ref-auditory-attention-binding2025)

2025 年 Strivens 等人的双耳分听研究分别以声音性别和位置为目标维度，发现准备时间增加时切换成本减少，但性别与位置的绑定效应反而增强。这种分离说明，更多准备不能一概解释为把所有无关维度都过滤得更彻底；它可能改变对象建立和先前特征关系的利用。[19](#ref-auditory-attention-binding2025)

在更自然的句子任务中，切换效应也可能与短词分类任务不同。Breuer 与 Fels 的 2025 年虚拟环境研究采用不可预测的德语矩阵句，没有发现强而统一的重新定向主效应，同时观察到与目标词位置等有关的交互。自然度提高后的阴性或不一致结果，本身就是认识任务边界的证据。[20](#ref-auditory-attention-matrix2025)

### 无关声音为什么仍会被加工

忽略一条信息不代表所有特征都完全停止加工。竞争声音可能引起干扰侵入错误，也可能因与目标相关的特征、意义或突发变化而影响反应。双耳分听中的姓名现象表明，有些听者会报告在非目标通道中听到自己的姓名，但并非每个人都会发生；结果还受到具体呈现与报告方法影响。[12](#ref-auditory-attention-ownname)[7](#ref-auditory-attention-switch)

这类现象可以用于讨论选择性加工，却不宜把注意描述成绝对的早期门控或无条件的完整语义加工。不同刺激、任务和神经层级可能呈现不同选择程度；经典“过滤”和“衰减”的思想提供历史问题框架，现代证据则更强调加工阶段、对象与任务条件。[1](#ref-auditory-attention-object)[2](#ref-auditory-attention-golumbic)

## 行为与神经测量

### 行为任务测量什么

行为任务可以要求复述目标、分类目标词、发现稀有事件或回答理解问题。除总正确率外，还可区分把干扰当目标的侵入错误、漏报与误报，并记录反应时间和随时间变化的表现。这些指标揭示不同问题：侵入错误更直接反映目标混淆，而全部错误还可能包括没听清、忘记内容或不熟悉反应规则。[7](#ref-auditory-attention-switch)[3](#ref-auditory-attention-continuity)

双耳分听把不同声音呈现给两耳，有利于严格控制信息，但“关注左耳”并不等同真实环境里关注左侧声源。空间化多说话者任务则引入[双耳听觉](../binaural-hearing/)及[空间听觉](../spatial-hearing/)线索，也可能同时改变声学掩蔽。两种范式各有用途，其结果应结合刺激和任务解释。[4](#ref-auditory-attention-hearing)[18](#ref-auditory-attention-wostmann)

持续注意任务还要区分平均成绩与时间内波动。一段任务的平均正确率相近，并不表示漏报发生在相同时间或以相同模式聚集。记录目标出现时刻、背景变化和任务阶段，才能研究维持失误；仅凭一次短测验不宜评价全部日常注意功能。[8](#ref-auditory-attention-sustained)

### 事件相关电位、节律与连续跟踪

事件相关电位适合研究短声目标、偏差和切换提示的响应，节律分析适合描述功率或相位的动态变化，连续跟踪则建立言语特征与神经信号之间的关系。三者可结合，但不是同一指标的不同名称。某个偏差波存在，不自动说明听者已理解目标；目标跟踪增强，也不直接指出投入了多少努力。[13](#ref-auditory-attention-hillyard)[6](#ref-auditory-attention-escera)[15](#ref-auditory-attention-methods)

[脑电图](../electroencephalography/)具有较好的时间分辨能力，却不保证每个头皮电极只对应一个脑区。皮层表面记录、脑磁与头皮脑电的信号来源、采样和分析约定也不同。对于注意相关潜伏期和侧化，报告需要保留记录方法与模型设置，而不把不同来源的数值混成统一时间表。[9](#ref-auditory-attention-mesgarani)[16](#ref-auditory-attention-ding)[10](#ref-auditory-attention-osullivan)

### 实验控制与标签

为了验证选择性注意，应尽量交换目标与干扰角色，平衡位置、身份、声级及提示，并加入行为检查。若目标总是左侧、更响或某个固定声音，模型可能识别位置、强度或身份，而没有验证对新场景中注意对象的推断。对准备与切换任务，还应控制视觉提示本身的重复效应。[21](#ref-auditory-attention-gaze2024)[7](#ref-auditory-attention-switch)

标签也需要说明来源。指令指定的目标是实验者希望听者关注谁，按键报告是听者报告的状态，行为正确率提供是否完成任务的线索；它们都不是对每个瞬间内在注意的完全观测。尤其在自发切换中，指令、实际转向和按键之间可能有不同延迟，应避免把三者强制设为同一个切换时刻。[15](#ref-auditory-attention-methods)[10](#ref-auditory-attention-osullivan)

## 听觉注意解码

### 解码目标与常见方法

听觉注意解码是根据脑电、脑磁或其他神经记录，估计听者正在关注的候选声源、位置或声音特征。它首先是一个经过定义的统计推断任务，不是直接读取内在想法。候选说话者识别、左／右方位判断和目标言语提取有不同的输出，不能只因都称为解码就比较同一个准确率。[10](#ref-auditory-attention-osullivan)[21](#ref-auditory-attention-gaze2024)

一种常见方法从多通道脑电重建声音包络，再分别计算与各候选包络的相似性，选择更匹配的候选。O’Sullivan 等人的研究证明，这种方法可以在特定连续言语任务中利用单试次脑电判断注意对象。该经典结果使用约 60 s 的分析片段，不能据此宣称设备能无延迟识别目标。[10](#ref-auditory-attention-osullivan)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-attention/03-envelope-decision.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-attention/03-envelope-decision.svg" alt="包络重建与候选比较的合成示意" loading="lazy" /></a>
<figcaption><p>图 3. 包络匹配决策的合成演示。A 展示两个随机生成并低通处理的候选特征，以及人为加入较多 A 成分、少量 B 成分和噪声的“重建特征”；B 根据完整 20 s 序列计算与 A、B 的皮尔逊相关。左图只显示前 4 s，右图使用完整序列。曲线为均值零、标准差一的特征值，不是声压波形或真实脑电；没有训练或验证受试者模型，较大相关也不是注意强度的百分比。</p></figcaption>
</figure>

### 判断窗口与切换延迟

更长窗口可以提供更多数据，有时改善相关估计或分类稳定性，但会混合切换前后的状态。较短窗口更新更快，却可能有较大估计方差。更新一次决策的频率、窗口中包含的历史长度、神经响应时延和设备处理耗时是不同量，不能只报告“每 0.1 s 更新”就声称总延迟只有 0.1 s。[15](#ref-auditory-attention-methods)[10](#ref-auditory-attention-osullivan)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-attention/04-window-delay.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-attention/04-window-delay.svg" alt="过去窗口对理想切换标签的平滑影响" loading="lazy" /></a>
<figcaption><p>图 4. 历史窗口如何混合切换前后信息。假定理想标签在 10 s 从 A 变为 B，分别计算过去 2 s 与 8 s 内属于 A 的样本比例；两条曲线在切换后 1 s 与 4 s 到达 0.5。这只是矩形窗作用于理想标签的数学演示，不是实际注意恢复、神经潜伏期或某算法实测延迟。真实系统还需考虑神经信号、特征估计、决策规则与设备处理。</p></figcaption>
</figure>

### 验证中的捷径与独立性

脑电具有时间相关和试次特征。把同一试次中不重叠的小片段随机分到训练与测试，仍可能让模型识别这个试次，再利用该试次固定的目标标签取得高正确率。这种结果不能直接证明它能对新的试次进行注意解码。不重叠只是没有重复样本，并不等于研究问题所要求的独立性。[21](#ref-auditory-attention-gaze2024)[22](#ref-auditory-attention-dataset-kul)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/auditory-attention/05-validation.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/auditory-attention/05-validation.svg" alt="片段划分与完整试次划分的区别" loading="lazy" /></a>
<figcaption><p>图 5. 验证单位的示意。A 将每个试次中的不同片段分到训练与测试，存在利用试次特征的风险；B 留出完整试次 4，示范对新试次的验证。每个条块只是一个数据片段，图中不提供实测准确率。若目标是推广到新人、新会话或新说话者，还需按对应单位划分，完整试次划分本身也不保证已经满足所有推广目标。</p></figcaption>
</figure>

眼动是另一项重要混杂。听者关注左侧说话者时，可能同时看向左侧；眼电或眼位相关变化可以进入脑电。2024 年 Rotaru 等人的研究让视觉与听觉注意方向一致或不一致，发现直接空间分类方法容易受到眼位和试次特征影响。这提醒研究者控制注视与分析方法，但不能扩大成全部包络重建或所有注意解码都只依赖眼动。[21](#ref-auditory-attention-gaze2024)

因此，应根据实际应用选择验证单位：对同一个人的新试次、对新会话、对新受试者和对新说话者分别是不同问题。滤波、特征标准化、参数选择也应与训练／验证／测试划分协调；若目标是实时系统，应进一步检查是否使用了未来数据，而不是把离线滤波结果当作已完成因果在线处理。[15](#ref-auditory-attention-methods)[22](#ref-auditory-attention-dataset-kul)

## 计算模型与公开代码

### 前向时域响应函数

前向模型用声音特征预测神经信号。对一个简化的线性形式，可写为

$$
\hat r_c(t)=\sum_j\sum_{\tau\in\mathcal T}h_{cj}(\tau)s_j(t-\tau),
$$

其中 $s_j$ 是包络或其他刺激特征，$r_c$ 是第 $c$ 个神经通道，$h_{cj}$ 为时域响应函数，$\mathcal T$ 为模型考虑的时间滞后。比较目标与非目标特征对独立数据的预测，可以研究选择性表征；但线性模型是对统计映射的近似，不是对真实神经电路的完整描述。[23](#ref-auditory-attention-mtrf)[15](#ref-auditory-attention-methods)

模型权重依赖特征之间的相关、正则化和预处理。一个滞后位置的较大权重，不必唯一对应某个神经加工阶段；预测准确也不能直接证明该特征是因果机制。解释潜伏期时，还需注意滤波对波形时序的影响，并区分模型选择的滞后范围与测得的神经响应。[15](#ref-auditory-attention-methods)

### 后向重建与候选匹配

后向模型从多个神经通道与时间滞后重建刺激特征，可概括为

$$
\hat s(t)=\sum_c\sum_{\tau\in\mathcal T}g_c(\tau)r_c(t+\tau).
$$

这里采用神经信号相对刺激具有延迟的记号，$\tau$ 的正负约定应与实现核对。后向模型可利用分布在不同通道中的信息，但其权重包含通道之间的相关和噪声结构，不能直接当作头皮脑区激活图；从后向权重解释生理来源需要额外方法。[23](#ref-auditory-attention-mtrf)[15](#ref-auditory-attention-methods)

对候选包络 $s_k$，可在预先规定窗口内计算 $\rho_k=\operatorname{corr}(\hat s,s_k)$，再取相关最大的候选。这个规则适合解释基本决策，但实际系统还要考虑候选音频如何获得、包络如何提取、窗口内是否有足够变化，以及连续决策是否稳定。相似声源、目标停顿和短窗口都可能增加不确定性。[10](#ref-auditory-attention-osullivan)[15](#ref-auditory-attention-methods)

### 自适应和非线性模型

监督学习需要已知目标的校准数据，跨受试者模型试图减少个人校准，自适应方法则可随新数据更新。Geirnaert 等人的无监督方法使用预测标签迭代调整重建模型，提供了减少已知标签依赖的研究路径。它的性能与收敛仍依赖所研究条件，不能理解为已经对所有新人和所有环境免校准可靠工作。[24](#ref-auditory-attention-unsup)

深度网络可以联合脑电与声音特征，或者从脑电直接分类空间方向，但更灵活的模型也可能更容易利用非目标线索。网络结构中的“注意机制”是计算术语，不等同于人的听觉注意机制；有高分类分数，也需要独立验证、混杂控制与相应应用证据。本文优先提供可核查的基础工具和原作者方法入口，而不按单一公开数据集的最高分推荐模型。[21](#ref-auditory-attention-gaze2024)[15](#ref-auditory-attention-methods)

| 模型或资源 | 主要用途 | 官方或原作者入口 | 解释边界 |
| --- | --- | --- | --- |
| 多变量时域响应函数工具箱 | 前向预测、后向重建、交叉验证与注意评价 | [mTRF-Toolbox](https://github.com/mickcrosse/mTRF-Toolbox) | 工具实现不保证任务控制正确；权重不直接等于神经来源 |
| Python 时域响应函数工具 | Python 环境中的模型训练、预测与交叉验证 | [mTRFpy](https://github.com/powerfulbean/mTRFpy)；[文档](https://mtrfpy.readthedocs.io/en/stable/) | Python 实现与 MATLAB 工具参数应分别核对 |
| 无监督自适应重建解码 | 使用预测标签更新注意解码模型 | [原作者仓库](https://github.com/AlexanderBertrandLab/unsupervised-AAD-stimulus-reconstruction) | 需保留初始化、迭代和验证条件；不是已验证临床控制器 |
| KU Leuven 注意数据 | 基础包络重建与比较研究 | [数据及发布者说明](https://zenodo.org/records/4004271) | 发布者提醒试次特征与注视混杂，勿将全部片段随机划分 |
| 视听注视控制数据 | 分离注视方向与听觉注意方向 | [AV-GC-AAD 数据](https://zenodo.org/records/11058711) | 数据条件决定适合检验的推广问题 |

以上代码和数据入口已核查维护者说明，未在本次词条撰写中运行完整第三方模型。正文配图使用独立的[配图脚本](/n3-hearingpedia/figures/auditory-attention/generate-figures.py)，只演示输入、时间窗口和验证结构，不作为任何工具箱的性能复现。[25](#ref-auditory-attention-code-mtrf)[26](#ref-auditory-attention-code-python)[27](#ref-auditory-attention-code-unsup)[22](#ref-auditory-attention-dataset-kul)[28](#ref-auditory-attention-dataset-gaze)

## 听力损失、年龄与听觉设备

### 感觉输入与注意困难

听力损失可以削弱用于区分声源的音高、音色和空间线索，使稳定对象的形成与跟随更困难。因而噪声中的目标选择问题可能部分来自外围输入退化，而不是独立的注意控制障碍。正常纯音阈值也不保证所有复杂聆听任务都相同；解释时需要同时考虑刺激可听性、声源区分与认知需求。[4](#ref-auditory-attention-hearing)

组间比较应尽可能控制年龄、各频段可听度、材料熟悉度和任务难度。若一组更难听清目标，其神经跟踪、反应时间和主观努力也可能同时改变；这些变化不能未经控制就归因于“注意资源不足”。神经模型信噪比和记录条件的差别，同样可能影响组间比较。[5](#ref-auditory-attention-fuel)[15](#ref-auditory-attention-methods)

### 年龄与持续、切换表现

随着年龄和经验变化，声音表征、目标保持、反应选择和资源分配都可能变化，但这些因素不一定沿同一个方向改变。听者可能通过经验或准备维持较好成绩，也可能在快速轮换或复杂干扰中出现更大困难。年龄相关结论应具体到任务和控制条件，而不是用“老年人注意力差”概括。[4](#ref-auditory-attention-hearing)[5](#ref-auditory-attention-fuel)

如果希望研究年龄影响，应分别评价持续与切换，并检查准备时间、目标可听度和反应需求。更长反应时间可能来自选择、记忆或运动反应等多个环节；即使两组正确率相近，也不能仅据此断言全部注意过程相同。与神经指标结合可增加解释线索，但仍需保留每项测量的范围。[7](#ref-auditory-attention-switch)[15](#ref-auditory-attention-methods)

### 人工耳蜗后的选择性加工

[人工耳蜗](../cochlear-implant/)提供新的听觉输入，用户需要逐渐适应其频谱与时域线索。关于注意的研究可以结合目标言语跟踪、空间聆听和行为测量，观察适应过程，但不能只根据目标跟踪更强就认为理解已经恢复正常，或只根据一次低分认定注意没有恢复。[29](#ref-mo-ci-adaptation-2026)

Mo、Alain 与 Dimitrijevic 的 2026 年纵向研究在开机及其后 3、6、12 个月追踪 19 名新植入成人，结合连续竞争言语、脑电和行为测量。目标言语的跟踪比非目标更强且更早，较强目标跟踪与较好的识别、空间聆听和生活质量相关；部分组平均改善主要集中在较早阶段。这些发现支持联合测量的价值，却不制定每位用户的注意恢复期限，也不证明神经跟踪变化单独造成全部行为改善。[29](#ref-mo-ci-adaptation-2026)

### 神经引导听觉设备

注意解码可以为[助听器](../hearing-aid/)或人工耳蜗提供目标估计，再与声源分离、定向拾音或增益控制结合。这样的系统需要串联多个环节：声音候选获取、可靠神经记录、目标判断、输出处理和用户适应。解码准确率只是其中一个指标，最终还应评估言语理解、努力、错误切换与稳定性。[24](#ref-auditory-attention-unsup)[15](#ref-auditory-attention-methods)

尤其在目标切换后，设备若仍增强旧目标，可能造成新的干扰；增益变化也可能改变用户的注意与神经输入。因此，静态离线分类成功不能自动证明闭环系统有净收益。较合适的评价应包括动态会话、不同环境和实际使用者，并区分工程验证与临床效果。[24](#ref-auditory-attention-unsup)[21](#ref-auditory-attention-gaze2024)

## 近期研究与开放问题

### 更接近日常的声音环境

2025 年 Breuer 等人的虚拟课堂研究在成人验证样本中比较复杂课堂噪声、白噪声和安静条件，发现具有可懂言语的真实感干扰尤其影响目标选择，复杂噪声也增加主观需求与努力。该范式虽然为儿童适用任务而设计，正文中的实验结论仍来自成人，不能直接写成已证实儿童效果。[30](#ref-auditory-attention-classroom2025)

同年的视听课堂研究还表明，视觉信息并不总能单向改善听觉任务：其内容是否一致、出现时刻与听觉刺激的关系，会影响反应时间和错误。真实场景中的面孔、文字与动作可能提供线索，也可能带来竞争；应区分跨模态提示、语义启动与多感觉整合。[31](#ref-auditory-attention-virtual2025)

### 更严格的解码与机制验证

注视控制数据和完整试次验证把研究问题从“模型能否在熟悉数据中分类”推进到“它究竟利用了什么”。这既有助于评估非线性模型，也有助于认识简单线性分类器的局限；不能仅靠模型简单就排除混杂。与此同时，持续注意的动态研究提醒我们，固定窗口标签不能完全描述真实会话中的注意变化。[21](#ref-auditory-attention-gaze2024)[8](#ref-auditory-attention-sustained)

仍需解决的问题包括：如何区分目标增强与干扰抑制；如何把声源形成和目标切换在自然会话中分别测量；如何获得可靠的动态标签；以及神经指标能否在独立人群与设备条件中稳定预测实际收益。回答这些问题需要行为、神经和工程结果相互验证，而不只是增加分类分数。[17](#ref-auditory-attention-alpha)[19](#ref-auditory-attention-binding2025)[15](#ref-auditory-attention-methods)[29](#ref-mo-ci-adaptation-2026)

## 与相关词条的关系

[听觉场景分析](../auditory-scene-analysis/)解释声音如何成为可选择的对象，[掩蔽](../masking/)解释竞争声音带来的声学与知觉干扰，[空间听觉](../spatial-hearing/)与[双耳听觉](../binaural-hearing/)介绍可用于目标区分的空间线索。[时域分辨率](../temporal-resolution/)讨论短时变化的辨别能力，它既可为选择提供线索，也可能受任务要求影响，不能把检测成绩当作注意的直接量表。

[听觉努力](../listening-effort/)讨论为完成任务投入的资源，[言语可懂度](../speech-intelligibility/)和[言语接收阈](../speech-reception-threshold/)讨论言语任务表现。[脑电图](../electroencephalography/)与[言语神经跟踪](../neural-speech-tracking/)介绍测量方法；听觉注意解码则是把这些测量与预先定义的目标推断任务结合起来。将这些概念分别说明，有助于避免用一个神经指标概括全部听觉体验。
