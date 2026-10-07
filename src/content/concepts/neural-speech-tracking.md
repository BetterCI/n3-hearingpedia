---
title: "言语神经跟踪"
english: "Neural speech tracking"
slug: "neural-speech-tracking"
summary: "系统介绍连续言语的神经跟踪、声学与语言特征、前后向模型、听觉注意解码、验证设计与开源工具。"
categories: ["neuroscience","research-methods","speech"]
tags: ["neural-speech-tracking"]
aliases: ["语音神经跟踪", "神经言语追踪", "neural speech tracking", "speech tracking", "皮层语音跟踪"]
status: draft
depth: in-depth
last_updated: "2026-10-07"
authors: ["AI 辅助编写"]
references: ["neural-speech-tracking-continuous", "neural-speech-tracking-obleser", "lalor-speech-2010", "neural-speech-tracking-mesgarani", "neural-speech-tracking-golumbic", "neural-speech-tracking-task", "guo-tracking-2026", "neural-speech-tracking-chinese", "neural-speech-tracking-chinese-team", "neural-speech-tracking-haufe", "neural-speech-tracking-speechrate", "neural-speech-tracking-gillis", "neural-speech-tracking-mtrf", "osullivan-aad-2015", "neural-speech-tracking-methods", "neural-speech-tracking-acoustic", "neural-speech-tracking-brodbeck", "neural-speech-tracking-semantic", "neural-speech-tracking-phoneme", "neural-speech-tracking-ding", "neural-speech-tracking-eelbrain", "neural-speech-tracking-code-python", "neural-speech-tracking-code-matlab", "neural-speech-tracking-gaze", "neural-speech-tracking-code-unsup", "neural-speech-tracking-dataset-kul", "neural-speech-tracking-code-mne", "neural-speech-tracking-hierarchyage", "neural-speech-tracking-karuna", "neural-speech-tracking-sle2018", "neural-speech-tracking-ciartifact", "neural-speech-tracking-gaze2024", "neural-speech-tracking-comparison2025", "neural-speech-tracking-code-eelbrain", "neural-speech-tracking-cca", "mo-ci-adaptation-2026", "neural-speech-tracking-vanthornhout", "neural-speech-tracking-lesenfants", "neural-speech-tracking-ci2025"]
batch: 3
order: 38
literature_checked_at: "2026-10-07"
knowledge_area: "methods"
kind: "analysis"
key_facts: [{"label":"输入对象","value":"语音特征与神经时间序列"},{"label":"常见模型","value":"前向响应函数或后向重建"},{"label":"主要限制","value":"跟踪相关不等于理解或因果"}]
---

**言语神经跟踪**是指神经活动与连续言语中的声学或语言特征之间，可测量的时间对应关系，以及用于量化这种关系的研究范式。听者持续听故事、课堂讲解或多人谈话时，研究者可以同步记录声音与神经信号，考察语音包络、频谱变化、音素、词汇和句子结构等特征如何与神经响应联系。这里的“跟踪”描述统计关系，不是大脑逐点复制声音，也不是研究者沿着解剖位置追踪某条神经。[1](#ref-neural-speech-tracking-continuous)[2](#ref-neural-speech-tracking-obleser)

这一范式将分析从反复呈现短声后平均响应，扩展到较长的自然言语。它能够在持续变化的输入中估计响应的时间特性，比较被关注与被忽略的声源，并研究声学信息向语言表征的转换。常见记录包括[脑电图](../electroencephalography/)、脑磁图和皮层表面电记录；这些记录的空间范围、信号来源和适用人群各不相同。[3](#ref-lalor-speech-2010)[4](#ref-neural-speech-tracking-mesgarani)[5](#ref-neural-speech-tracking-golumbic)

言语神经跟踪与[听觉注意](../auditory-attention/)、[言语可懂度](../speech-intelligibility/)、[听觉努力](../listening-effort/)和[听觉可塑性](../auditory-plasticity/)有关，但不等同于其中任何一个概念。能识别噪声条件、能判断注意对象和能预测个体[言语接收阈](../speech-reception-threshold/)，是不同的验证目标。跟踪增强也不能单凭方向解释成理解更好、努力更多或康复更快。[6](#ref-neural-speech-tracking-task)[7](#ref-guo-tracking-2026)

中文文献与研究介绍中存在“言语追随”“神经跟踪”等表述。本词条采用“言语”覆盖声音到语言理解的不同层级；讲述波形、包络和频谱时仍使用“语音”。“跟踪”与“追踪”在此属于译名选择，不能据此划分不同机制，也不声称某一种译法已经成为统一标准。[8](#ref-neural-speech-tracking-chinese)[9](#ref-neural-speech-tracking-chinese-team)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/neural-speech-tracking/01-signal-feature-response.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/neural-speech-tracking/01-signal-feature-response.svg" alt="合成声学波形、包络特征和带延迟噪声的模拟神经记录" loading="lazy" /></a>
<figcaption><p>图 1　声音、分析特征与记录信号是不同对象。上图为有已知包络的合成载波，相对幅度限制在 ±1；中图为非负包络；下图为经过延迟并加入噪声的模拟记录，以任意单位表示。全部为说明性合成数据，不是自然言语或被试脑电。模拟记录与包络有关系，却不复制声学载波；图中 120 ms 延迟是生成参数，不是人类言语处理的固定潜伏期。</p></figcaption>
</figure>

## 概念范围与相邻术语

### 跟踪、皮层跟踪与包络跟踪

“言语神经跟踪”是较宽的名称，可涉及不同记录层级和不同特征；“言语皮层跟踪”强调皮层活动。头皮脑电常用来研究皮层相关响应，但电极处的记录并非单一脑区的直接读数。若要讨论具体脑区，需要结合记录方法、源定位及模型条件，而不能只凭某个电极权重给出解剖结论。[1](#ref-neural-speech-tracking-continuous)[10](#ref-neural-speech-tracking-haufe)

“包络跟踪”则限定特征。[时域包络](../temporal-envelope/)描述信号振幅随时间的变化，常用于连续言语研究；包络的变化与声学起点、音节节奏及其他语言事件相关，却不与它们完全等同。因此，研究只使用包络时，应说明测得的是包络相关活动，不宜将结果改称为完整的语义理解或所有言语信息的跟踪。[11](#ref-neural-speech-tracking-speechrate)[12](#ref-neural-speech-tracking-gillis)

### 跟踪与神经夹带

神经夹带通常涉及神经振荡与外部节律的同步关系。较宽用法有时与刺激跟踪重叠，较严格的机制解释则涉及内源振荡如何被外部输入调整。神经记录与声音有相位关系或可预测性，既可能包含振荡同步，也可能包含连续声学事件引起的响应；仅凭相关或同频峰值，不足以确定唯一机制。[2](#ref-neural-speech-tracking-obleser)

因此，本词条以“跟踪”描述可观察的对应，用“夹带”讨论明确提出的振荡机制。证明某项言语特征可被神经信号预测，与证明它通过振荡夹带影响行为，是不同层级的证据。研究报告应把测量结果、机制假设和因果推断分开。[1](#ref-neural-speech-tracking-continuous)[2](#ref-neural-speech-tracking-obleser)

### 跟踪、编码与解码

前向编码用言语特征预测神经记录，后向解码用神经记录估计言语特征或任务状态。两者都可量化跟踪，却有不同目的。前向模型适合讨论指定特征与响应的延迟关系；后向模型常用于重建包络或分类注意对象。模型名字不能代替验证：一个能重建包络的模型并不必然能识别词语内容。[13](#ref-neural-speech-tracking-mtrf)[14](#ref-osullivan-aad-2015)

| 名称 | 限定范围 | 典型问题 | 不能直接推出的结论 |
| --- | --- | --- | --- |
| 言语神经跟踪 | 言语特征与神经活动的时间关系 | 是否存在可重复的对应？ | 一定听懂或存在唯一机制 |
| 言语皮层跟踪 | 皮层相关活动 | 皮层如何响应指定特征？ | 每个头皮电极代表独立脑区 |
| 语音包络的神经跟踪 | 振幅变化特征 | 包络能否预测或被重建？ | 已测到所有语言层级 |
| 神经夹带 | 振荡与外部节律关系 | 节律是否调整神经振荡？ | 任何刺激相关都证明夹带 |
| 时域响应函数 | 延迟回归建模 | 特征与响应在何种延迟相关？ | 响应峰值等于独立处理阶段 |
| 听觉注意解码 | 从记录估计注意对象或状态 | 此时在关注谁？ | 已预测个体理解能力 |

## 言语特征与神经记录

### 包络、频谱与声学起点

包络是常用的低维输入，但提取方式会改变其内容。对整个信号求振幅变化、在多个频带内提取后组合，或保留分频带包络，得到的特征并不相同。实验应说明频带、变换、压缩及降采样规则；不能只写“提取了包络”，便假定各研究的输入一致。[13](#ref-neural-speech-tracking-mtrf)[15](#ref-neural-speech-tracking-methods)

频谱图保留频率与时间上的能量结构，可以用于构建频谱—时域响应模型。声学起点或边缘特征则强调振幅与频谱的上升变化。包络、频谱与边缘往往相关，却各自强调不同信息；只用较简单声学控制，可能让模型把未解释的声学变化归到其他变量。[16](#ref-neural-speech-tracking-acoustic)[12](#ref-neural-speech-tracking-gillis)

声音的[基频](../fundamental-frequency/)、[共振峰](../formant/)及[时域精细结构](../temporal-fine-structure/)也属于可讨论的信号属性，但不意味着所有记录和分析频段都能以相同方式跟踪这些属性。需要区分声学特征的原始频率、特征的变化速度与神经信号的分析频段。研究低频包络对应关系，并不是直接记录声学载波的每一个周期。[1](#ref-neural-speech-tracking-continuous)[11](#ref-neural-speech-tracking-speechrate)

### 音素、词汇与语义特征

较高层级的模型常利用转录和时间对齐，为音素或词语起始位置生成事件序列，也可在事件处赋予词频、意外程度或语义差异等数值。这里“意外程度”描述材料在指定语言模型下的低概率程度，不等于听者主观感到惊讶。词汇模型和听者的经验不同，其输出需要作为假设特征解释。[17](#ref-neural-speech-tracking-brodbeck)[18](#ref-neural-speech-tracking-semantic)[12](#ref-neural-speech-tracking-gillis)

早期音素特征研究表明，结合声学与音素标签可以改善对神经信号的描述；后续工作指出，较充分的声学边缘表示也可解释某些原先归为音素的效果。这不是否定全部语言加工，而是说明一个语言命名的变量，未必具有独立于声学的解释价值。[19](#ref-neural-speech-tracking-phoneme)[16](#ref-neural-speech-tracking-acoustic)

因此，语言特征的检验通常需要一个足够合理的声学基线，再比较加入语言变量后是否改善独立数据预测。Gillis 等人的研究在控制声学性质后，发现部分音素和词汇变量仍贡献独特信息，并检验了跨故事推广。这样的证据比只看到某个语言变量与脑电相关，更能支持对应层级的解释。[12](#ref-neural-speech-tracking-gillis)

### 词、短语和句子的层级结构

自然言语包含多个时间尺度；有些研究使用规则呈现的音节或词，将词、短语、句子对应到不同频率，观察神经记录中是否存在相应成分。这类频率标记设计便于分离层级，也能针对声学和可预测性设置对照，但它具有特定材料结构，并非自然会话的所有节奏。[20](#ref-neural-speech-tracking-ding)

看到高层级频率成分，需要检查它是否可由声学变化、词汇统计或重复结构解释；缺少该成分，也不能立即推断听者完全没有理解。频率标记与自然故事回归是互补方法，前者强调受控结构，后者更接近持续言语，但更依赖特征定义和相关性的处理。[20](#ref-neural-speech-tracking-ding)[21](#ref-neural-speech-tracking-eelbrain)

### 脑电、脑磁与皮层表面记录

脑电和脑磁提供较高时间分辨率，适合较长记录；皮层表面电记录能够考察局部活动及高频响应，但通常来自临床需要植入电极的患者，覆盖范围有限。不同方法的数值和空间图不宜直接互换，特定患者中的选择性结果也不能当作所有健康人头皮脑电的预期值。[4](#ref-neural-speech-tracking-mesgarani)[5](#ref-neural-speech-tracking-golumbic)

连续言语响应与[听觉诱发电位](../auditory-evoked-potential/)有联系：二者都研究声音相关的神经活动，但连续模型同时处理多个时间上重叠的事件。回归权重可能呈现类似早期或晚期电位的形状；仍需考虑滤波、输入特征和事件重叠，不能仅凭峰形就赋予与短声诱发电位完全相同的生成机制。[3](#ref-lalor-speech-2010)[15](#ref-neural-speech-tracking-methods)

## 前向编码与时域响应函数

### 从连续特征预测响应

一个离散时间的多特征前向模型可表示为：

$$
\widehat r_c[n]=\sum_{f=1}^{F}\sum_{k=k_{\min}}^{k_{\max}}h_{cf}[k]s_f[n-k]+b_c.
$$

其中 $s_f$ 是第 $f$ 个特征，$r_c$ 是第 $c$ 个记录通道，$h_{cf}$ 是时域响应函数，$k$ 为以采样点计的延迟，$b_c$ 为截距。按此定义，正延迟表示声音特征早于被预测的响应；毫秒延迟需要按采样率换算。模型预测与实测记录之间还存在未解释部分。[13](#ref-neural-speech-tracking-mtrf)

该模型并不宣称听觉系统完全线性。它是在指定特征、频段和时间窗内，对可重复统计关系进行近似。对某个新特征，模型可以检验它是否提供额外预测信息；对于没有纳入的过程，则不能因模型预测较好就认为不存在。[21](#ref-neural-speech-tracking-eelbrain)[15](#ref-neural-speech-tracking-methods)

### 延迟、单位与权重解释

延迟范围表达模型允许声音与响应如何对应，而非已经测得的神经传播时间。同步偏移、设备延迟和滤波都会影响估计峰值。研究若使用负延迟，还需要解释其来源：语境预测、特征相关性或信号处理都可能产生相应权重，不能将每个负延迟峰值直接解释为大脑预知未来。[15](#ref-neural-speech-tracking-methods)

权重大小依赖特征和响应的尺度。以物理声压输入、以标准化包络输入和以事件脉冲输入，权重单位与数值均不同。多特征相关时，权重还表示在其他变量存在时的条件关系；它不是独立认知过程的绝对强度。比较研究应先确认尺度、正则化和特征集一致。[13](#ref-neural-speech-tracking-mtrf)[10](#ref-neural-speech-tracking-haufe)

### 正则化与模型选择

连续言语的相邻时间点和延迟变量常高度相关，直接拟合可能出现不稳定权重。岭回归通过对权重平方和加惩罚，限制过度拟合。以平方损失形式可写为：

$$
\widehat{\mathbf h}=\underset{\mathbf h}{\operatorname{argmin}}\left\{\frac{1}{N}\|\mathbf r-\mathbf X\mathbf h\|_2^2+\lambda\|\mathbf h\|_2^2\right\}.
$$

设计矩阵 $\mathbf X$ 包含指定特征及延迟，$N$ 为训练样本数，$\lambda$ 为正则化强度。该式展示一种约定；不同工具对数据尺度、截距和损失归一化的处理可能不同，所以同一个数值的 $\lambda$ 未必具有相同作用。截距通常应另行处理而不与其他权重同样惩罚。[13](#ref-neural-speech-tracking-mtrf)[22](#ref-neural-speech-tracking-code-python)

正则化应在训练数据内部选择，最终结果在未参与选择的数据上评估。否则，测试数据已经影响了模型设置，报告的预测表现会过于乐观。逐渐尝试频段、延迟和特征后挑选最大相关，也属于模型选择，需要纳入验证流程，而不是把每次尝试都称为独立确认。[15](#ref-neural-speech-tracking-methods)[22](#ref-neural-speech-tracking-code-python)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/neural-speech-tracking/02-forward-backward.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/neural-speech-tracking/02-forward-backward.svg" alt="前向模型用言语特征预测响应，后向模型用神经记录重建特征的示意图" loading="lazy" /></a>
<figcaption><p>图 2　前向编码与后向重建的输入和输出。前向模型需要与实测响应比较，后向模型需要与真实或候选特征比较；训练时均需要配对且同步的数据，验证时均需保留独立数据。框图描述统计建模方向，不是生理信息倒流，也不表示后向模型权重能直接解释为神经发生源。</p></figcaption>
</figure>

## 后向重建与听觉注意解码

### 从神经记录重建言语特征

后向模型将多个记录通道及延迟组合起来，估计一个指定言语特征，例如包络。重建结果常与真实包络求相关，用作该任务下的跟踪指标。模型可以利用跨通道结构提高预测，但重建包络不等于恢复完整音频，更不等于读取听者的全部思想或逐词转写理解内容。[14](#ref-osullivan-aad-2015)[13](#ref-neural-speech-tracking-mtrf)

前向与后向延迟的符号约定可能不同。若工具将解码定义为响应预测刺激，其时间轴通常需要相应变换；不能在没有检查软件定义的情况下，按前向模型的方法解释后向峰值。尤其是离线重建可能使用相对于输出时刻更晚的神经样本，这会带来等待时间，必须与实时系统区分。[23](#ref-neural-speech-tracking-code-matlab)[22](#ref-neural-speech-tracking-code-python)

### 比较目标与竞争声源

在两个说话者同时出现时，研究者可将重建包络分别与两条候选包络比较。若它与被关注说话者的相似度更高，可以据此分类注意对象。O’Sullivan 等人的研究展示了从单试次脑电中解码选择性注意的可行性，也推动了神经引导听觉设备的研究。[14](#ref-osullivan-aad-2015)

注意分类取决于两条候选之间的可区分性，而不只取决于目标跟踪绝对值。目标和竞争包络高度相似时，即使两者均有对应关系，分类也可能困难。目标相关较高还可能涉及目标声级、空间或记录条件；合理设计需要平衡这些因素，并明确关注对象的行为指令。[5](#ref-neural-speech-tracking-golumbic)[24](#ref-neural-speech-tracking-gaze)

### 解码窗口与实际响应速度

较长窗口可以积累更多样本，常有利于稳定分类，但会延迟目标切换的检测。窗口中的旧目标数据也可能影响当前判断，因此“每秒输出一次”不等于能在一秒内可靠发现切换。模型计算时间、记录延迟、窗口长度和决策规则应分别报告。[23](#ref-neural-speech-tracking-code-matlab)[25](#ref-neural-speech-tracking-code-unsup)

使用注意解码控制设备，还需要从混合输入中提取候选声源、处理错误决策并保持输出稳定。实验中使用已知的两条干净音轨，与真实餐厅中仅有麦克风混合信号，是不同难度。离线高分类率是方法证据，不能独立证明已经实现可用的实时临床设备。[25](#ref-neural-speech-tracking-code-unsup)[26](#ref-neural-speech-tracking-dataset-kul)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/neural-speech-tracking/04-attention-candidates.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/neural-speech-tracking/04-attention-candidates.svg" alt="候选特征和合成重建特征以及全时段相关系数" loading="lazy" /></a>
<figcaption><p>图 3　候选比较的说明性示例。候选 A、B 为独立生成的低通随机序列，重建序列由偏向 A 的线性组合及噪声构成，均作标准化；左图只显示前 4 s，右图相关由全 30 s 计算。它说明分类可依据候选间相似度差异，不是实际脑电解码结果，也不能从标准化特征的幅度推断声压或认知资源。</p></figcaption>
</figure>

### 解码权重与神经来源

后向权重既利用信号，也利用通道间噪声和相关结构。某通道权重大，未必说明该位置的神经活动最强；权重小，也未必说明该通道没有相关活动。Haufe 等人的分析专门说明了预测模型权重与可解释活动模式之间的区别，提出在线性条件下进行适当变换。[10](#ref-neural-speech-tracking-haufe)

即便作了活动模式变换，也仍需考虑体积传导、参考电极及源定位不确定性。模型能够解码一个状态，与已经找到该状态的唯一脑区，是不同问题。词条中的空间图若来自模型权重，应清楚标注其性质，避免直接称为“注意中心”。[10](#ref-neural-speech-tracking-haufe)[27](#ref-neural-speech-tracking-code-mne)

## 跟踪指标与统计解释

### 预测相关与重建相关

前向模型常比较预测和实测响应，后向模型常比较重建和真实特征。皮尔逊相关描述时间上的线性对应，不直接给出物理幅度是否匹配：两条曲线相差固定倍数时也可能高度相关。若需要评价幅度和误差，应另报适当的误差指标，而不只报告相关。[22](#ref-neural-speech-tracking-code-python)[21](#ref-neural-speech-tracking-eelbrain)

相关大小还受响应噪声、记录长度、特征自相关和分析频段影响。更多可用数据可能使估计稳定，较干净的记录可能提高相关，而并非听者能力发生改变。跨研究或纵向比较应交代这些条件；“相关从某值升到某值”首先是规定分析中的变化，不是统一刻度的听觉能力增长。[15](#ref-neural-speech-tracking-methods)[7](#ref-guo-tracking-2026)

### 相干、相位与频率标记

频域方法可以考察声音和神经信号在某些频率上的相干，或活动在事件间的相位一致性；频率标记则观察指定结构频率的响应。这些方法与回归模型有联系，但计算对象和基线不同，不能把相干值、回归预测相关和分类正确率当成同一个分数。[2](#ref-neural-speech-tracking-obleser)[20](#ref-neural-speech-tracking-ding)

输入本身具有周期性时，频率峰值也可能反映反复事件的响应。要解释为特定语言结构，需要材料与对照支持，最好检查实际声学特征是否同样具有该频率。不同层级的神经成分还可能有不同的年龄和注意效应；不宜将全部低频活动合并解释成一个“语言加工强度”。[20](#ref-neural-speech-tracking-ding)[28](#ref-neural-speech-tracking-hierarchyage)

### 增量预测与特征独特贡献

检验词汇或语义特征时，可比较完整模型与去掉该特征的模型，观察独立数据预测是否改善。删除一项特征后，需要按相同规则重新训练和选择参数；把完整模型中的权重直接设为零，通常不能代表公平的简化模型比较。模型差异还要在听者和材料层面评估，而不是把所有采样点视为独立重复。[12](#ref-neural-speech-tracking-gillis)[21](#ref-neural-speech-tracking-eelbrain)

额外预测价值取决于已纳入的基线。与包络模型相比有效的词语特征，未必在加入充分声学边缘后仍有独特贡献；反过来，合理控制声学后仍存在的语言效应，更能支持相应解释。单项权重不显著与“没有加工此特征”也并不等价，因为共线性和记录信噪比可能降低检出能力。[16](#ref-neural-speech-tracking-acoustic)[12](#ref-neural-speech-tracking-gillis)

### 跟踪、理解与努力的分离

包络跟踪可在任务注意较弱的条件下仍存在，也可随输入信噪比改变。这说明它包含感觉加工信息，不是“是否理解”的二元开关。2023 年一项保持退化声音本身不变、利用先前清晰版本改善理解的研究，发现部分词语相关响应发生变化，而包络及包络起点响应没有同样改变，为分离声学与理解提供了重要设计。[6](#ref-neural-speech-tracking-task)[29](#ref-neural-speech-tracking-karuna)

同样，跟踪不能直接替代听觉努力指标。努力涉及资源投入与动机，研究中的主观、行为和生理测量也具有不同维度。若希望建立跟踪与努力的关系，需要同时测量指定努力结果，控制成绩及声学变化，并在独立数据中验证；只看到某个脑电特征增加，并不足以解释为“更费力”。[30](#ref-neural-speech-tracking-sle2018)[7](#ref-guo-tracking-2026)

## 数据采集、预处理与验证

### 时间同步和刺激记录

语音与神经记录必须使用可核查的时间关系。数字文件开始时刻与声音真正到达耳边的时刻可能不同；音频输出、无线传输和设备处理都有延迟。触发标记、回录及设备延迟检查有助于发现固定偏移和漂移。若时间轴错误，模型仍可能利用特征的自相关产生某种预测，却会误导潜伏期解释。[15](#ref-neural-speech-tracking-methods)

多说话者实验还要区分干净目标音轨、竞争音轨和实际呈现的混合信号。对助听器或人工耳蜗，麦克风输入与经过处理后的特征可能不同；分析使用哪一种声音表征，应根据问题说明。用原始输入作为模型特征，可以研究输入相关响应，但不能假设它完全等于听者获得的内部刺激。[23](#ref-neural-speech-tracking-code-matlab)[31](#ref-neural-speech-tracking-ciartifact)

### 滤波、降采样与缺失片段

滤波改变可分析的频率范围，也会影响响应的时间形状；降采样应包含合适的抗混叠处理。零相位离线滤波可利用前后样本，不等于实时系统的处理方式。比较潜伏期或实时延迟时，需要注明滤波性质，并检查数据边缘与训练／测试边界受到的影响。[15](#ref-neural-speech-tracking-methods)[27](#ref-neural-speech-tracking-code-mne)

删除伪迹片段后，特征和响应必须同步裁切。不同试次之间不应在未经处理的情况下直接拼接，再让延迟变量跨越连接点；这样会形成不存在的声学—神经对应。缺失、眨眼和剔除比例也应报告，因为条件间可用数据量不同，会影响模型稳定性和比较结果。[21](#ref-neural-speech-tracking-eelbrain)[27](#ref-neural-speech-tracking-code-mne)

### 眼动与人工耳蜗伪迹

眼动不只是随机噪声。2024 年研究显示，眼位本身也可随被关注言语的特征变化；另一项空间注意解码研究发现，模型可能利用注视方向与试次特征，产生偏高分类表现。因此需要记录或控制眼动，检查解码依据，并区分候选包络重建与只按空间位置分类的不同风险。[32](#ref-neural-speech-tracking-gaze2024)[24](#ref-neural-speech-tracking-gaze)

人工耳蜗电刺激可在记录中引入与声音和设备处理相关的伪迹。如果伪迹也跟随包络，较高相关未必全部来自神经响应。滤除植入侧通道、独立成分分析或多通道滤波等方法，都需要验证是否降低伪迹并保留目标响应；不能因为处理后波形较平滑，就认定问题已解决。[31](#ref-neural-speech-tracking-ciartifact)

### 按推广对象划分训练和测试

同一试次的随机片段可能共享缓慢变化、背景噪声和个体状态，即使时间点没有重复，也未必是独立样本。留出完整试次，比随机分散同试次片段更适合检验跨试次推广；若目标是新听者或新故事，则还需要按听者或材料划分。验证目标必须与最终用途一致。[24](#ref-neural-speech-tracking-gaze)[12](#ref-neural-speech-tracking-gillis)

超参数选择、特征筛选和标准化估计应在适当训练层级完成。测试结果不应反过来用于挑选最好的滤波或延迟范围。邻近时段还可能因滤波、自相关和窗口重叠形成联系，必要时应设置边界间隔或按试次处理；仅宣称“没有重叠窗口”不足以证明不存在信息泄漏。[15](#ref-neural-speech-tracking-methods)[22](#ref-neural-speech-tracking-code-python)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/neural-speech-tracking/05-validation.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/neural-speech-tracking/05-validation.svg" alt="同试次片段混入与留出完整试次两种验证划分示意图" loading="lazy" /></a>
<figcaption><p>图 4　测试集应与推广目标匹配。上图将每个试次的片段分散到训练和测试，可能共享试次特征；下图留出一个完整试次。它是数据划分示意，不给出两种设计的准确率。留出完整试次检验的是该设计中的跨试次推广，仍不能替代留出新听者、说话者或设备条件的验证。</p></figcaption>
</figure>

### 基线与不确定性

时间错位、匹配不对应的音轨或在适当单位上置换标签，可以构建对照，但必须保留与问题有关的自相关和分组结构。逐采样点随机打乱可能破坏真实数据的时间性质，形成过于容易的基线。置换、重复和置信区间应说明统计单位，避免把数万个相关采样点当成数万个独立听者。[15](#ref-neural-speech-tracking-methods)[21](#ref-neural-speech-tracking-eelbrain)

检验“高于对照”与评价实际效果也不同。极小但稳定的相关可以有统计意义，却未必能支持个体临床判断；分类高于机会水平，也未必足够可靠地控制设备。应同时报告效应大小、个体差异、错误率及外部验证，而不仅是显著性。[7](#ref-guo-tracking-2026)[33](#ref-neural-speech-tracking-comparison2025)

## 计算模型与开放资源

### 多特征线性模型

线性前向与后向模型是常用起点。它们通过明确特征、时间延迟和正则化，形成可复核的基线。包络、频谱和语言事件可以联合建模，但增加特征维度也增加估计困难。模型越复杂并不意味着生理解释越完整，应在预测、稳定性与可解释性之间按问题选择。[13](#ref-neural-speech-tracking-mtrf)[12](#ref-neural-speech-tracking-gillis)

[mTRF-Toolbox](https://github.com/mickcrosse/mTRF-Toolbox) 提供 MATLAB 实现，包括前向、后向、训练、交叉验证和示例；[mTRFpy](https://github.com/powerfulbean/mTRFpy) 提供相应的 Python 建模工具，配有[基础使用文档](https://mtrfpy.readthedocs.io/en/stable/basics.html)。使用不同实现时，要核对数据矩阵方向、延迟定义、损失归一化和参数版本，不能只复制相同数值就假设模型等价。[23](#ref-neural-speech-tracking-code-matlab)[22](#ref-neural-speech-tracking-code-python)

### 逐步拟合与语言特征分析

[Eelbrain](https://github.com/Eelbrain/Eelbrain) 支持连续数据及多特征时域响应分析，包含基于逐步提升的估计方法和群体统计工具。其方法论文提供以连续言语为例的分析说明，适合研究多个有假设依据的表征。逐步提升与岭回归具有不同约束和选择规则，即使都输出响应函数，也不应忽略方法差别。[21](#ref-neural-speech-tracking-eelbrain)[34](#ref-neural-speech-tracking-code-eelbrain)

[MNE-Python](https://github.com/mne-tools/mne-python) 可用于脑电／脑磁预处理、时频和相关建模流程。它与特征提取、时间对齐工具共同构成分析环境，但不会自动解决特征共线性或赋予预测结果语言解释。可复现研究应记录各工具版本、处理参数、原始事件和数据划分。[27](#ref-neural-speech-tracking-code-mne)

### 典型相关分析与注意模型

典型相关分析同时寻找刺激和响应的线性投影，使投影之间的相关增大。它与只在一端预测另一端的模型不同，可用于发现共享变化或建立匹配判断。估计出来的最大相关需要在独立数据检验，维度和正则化也应控制；训练集最大相关不能直接作为泛化性能。[35](#ref-neural-speech-tracking-cca)

注意解码还包括自适应方法、空间分类和非线性模型。[无监督自适应包络重建仓库](https://github.com/AlexanderBertrandLab/unsupervised-AAD-stimulus-reconstruction)提供对应算法和实验代码。根据自身预测更新模型，可能减少人工标签需求，也可能积累错误；使用前应核对初始化、依赖、数据适用条件和测试方案。空间分类或深度模型还需要特别排查眼动与试次偏差。[25](#ref-neural-speech-tracking-code-unsup)[24](#ref-neural-speech-tracking-gaze)

### 开放数据与复现实例

[KU Leuven 听觉注意检测数据集](https://zenodo.org/records/4004271)提供脑电及对应声音，可用于研究候选声源与响应关系。它支持规定场景中的方法比较，不能替代真实会话、不同语言和临床人群的验证。分析开放数据时，应核对许可、试次与听者编号、目标标签以及与既有研究一致的数据版本。[26](#ref-neural-speech-tracking-dataset-kul)

本词条另外提供一个[可复现的合成建模脚本](/n3-hearingpedia/figures/neural-speech-tracking/generate-figures.py)：生成已知时域响应，加入噪声，使用训练集内的连续分块验证选择正则化，再在留出时段预测。它用于理解模型与验证，并不模拟完整听觉系统；第三方仓库已核对官方说明，本文未复现其全部论文结果。[13](#ref-neural-speech-tracking-mtrf)[22](#ref-neural-speech-tracking-code-python)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/neural-speech-tracking/03-trf-heldout.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/neural-speech-tracking/03-trf-heldout.svg" alt="合成时域响应函数估计与独立测试数据预测" loading="lazy" /></a>
<figcaption><p>图 5　岭回归模拟与留出数据检验。采样率 50 Hz，延迟为 0—500 ms；左图比较已知生成权重与训练估计，右图显示 65—69 s 的含噪记录和预测。正则化只在训练部分的三个连续分块中选择，并保留边界间隔；测试使用 60.5 s 后的数据，全测试段约 29.5 s，相关约 0.84。全部为合成数据，较高相关不代表真实脑电的预期表现；正则化可使权重收缩，预测较好也不等于准确恢复每个生成参数。</p></figcaption>
</figure>

## 应用与证据边界

### 注意选择与复杂声音环境

多人言语研究表明，被关注和被忽略的声源在部分神经响应中具有不同表征，支持跟踪作为研究目标选择的工具。不同神经层级和特征可能出现不同程度的选择性：声学响应、词汇响应和局部高频活动不能被简化为一个统一开关。未检出竞争声源的某种响应，也不代表它没有任何加工。[5](#ref-neural-speech-tracking-golumbic)[17](#ref-neural-speech-tracking-brodbeck)

这类研究与[听觉场景分析](../auditory-scene-analysis/)互补：场景分析关注混合输入如何被组织为声源，跟踪方法则观察指定表征如何与记录对应。若要解释[空间听觉](../spatial-hearing/)或[双耳听觉](../binaural-hearing/)的收益，还应同时测量空间条件和行为，不能将目标相关提高直接当作定位能力提高。[4](#ref-neural-speech-tracking-mesgarani)[36](#ref-mo-ci-adaptation-2026)

### 言语可懂度与个体阈值

早期研究观察到包络跟踪与可懂度之间的关系，并探索从神经指标预测个体阈值。2019 年一项结合声学和音素特征的研究在规定人群和任务中得到有希望的预测结果。但模型表现取决于材料、频段、训练和评估方案，应按这些条件理解，而不是宣布已经建立对所有人适用的客观测听替代品。[37](#ref-neural-speech-tracking-vanthornhout)[38](#ref-neural-speech-tracking-lesenfants)

区分噪声与安静、随信噪比变化和准确预测新个体阈值，需要不同证据。后两者还涉及拟合曲线是否稳定、是否有足够条件覆盖变化区间，以及误差是否小于实际需要。相关系数也不能直接换算成分贝；个体阈值需要行为参照或经过充分验证的独立目标。[7](#ref-guo-tracking-2026)[33](#ref-neural-speech-tracking-comparison2025)

### 年龄、发展与听力恢复

年龄效应可能随语言层级改变。2023 年频率标记研究观察到，老年组的低层级跟踪增强，而较高层级跟踪及其注意调节减弱；行为联系的方向也不同。它说明“跟踪越强越好”不适用于所有成分，并提示研究应区分声学表征、语言层级与注意作用。[28](#ref-neural-speech-tracking-hierarchyage)

人工耳蜗研究可利用连续言语观察听觉恢复后的变化。儿童研究提示不同时间尺度的跟踪具有不同韧性和易受影响性；成人纵向研究则考察开机后多个时点的目标、竞争声源和行为变化。群体结果可以指导研究假设，但不能规定每个人的恢复期限或仅凭跟踪决定康复方案。[39](#ref-neural-speech-tracking-ci2025)[36](#ref-mo-ci-adaptation-2026)

### 设备评价与临床转化

跟踪有望补充[助听器](../hearing-aid/)和[人工耳蜗](../cochlear-implant/)的评价，尤其在行为回答困难时。但“无需口头复述”不等于完全不受注意、语言经验和状态影响。设备处理还可能改变声音特征及伪迹，因此必须验证指标确实回答了目标问题。[6](#ref-neural-speech-tracking-task)[31](#ref-neural-speech-tracking-ciartifact)

临床用途需要进一步证明个体重复性、外部推广和有意义的误差范围。若模型相对年龄、听力图等简单基线没有稳定改善预测，即使某些群体关联显著，也未必提供额外临床信息。跟踪目前更适合作为具体协议下的研究与辅助指标，其用途应随验证证据限定。[7](#ref-guo-tracking-2026)[33](#ref-neural-speech-tracking-comparison2025)

## 研究沿革与近期进展

### 从连续响应到多层级表征

Lalor 与 Foxe 的连续言语响应提取、后续多说话者皮层记录和单试次脑电注意解码，构成重要的方法入口。开放工具使研究逐渐扩展到多特征和自然故事分析，同时也促使研究者重新检查模型权重、声学控制与验证方式。[3](#ref-lalor-speech-2010)[4](#ref-neural-speech-tracking-mesgarani)[14](#ref-osullivan-aad-2015)[13](#ref-neural-speech-tracking-mtrf)

音素、词汇和层级结构研究随后展示了多尺度的语言相关响应；较充分的声学模型与保持声学不变的理解操纵，则推动证据从“存在相关”走向“哪些额外解释成立”。这些方法互相补充，不能把其中一种模型视为完整言语理解的唯一描述。[19](#ref-neural-speech-tracking-phoneme)[20](#ref-neural-speech-tracking-ding)[16](#ref-neural-speech-tracking-acoustic)[29](#ref-neural-speech-tracking-karuna)

### 2024—2026 年的代表性研究

2024 年的眼动与空间注意解码研究强调：行为相关的非目标信号也可能提供分类线索。它们不是宣告全部注意解码无效，而是要求为具体方法设置对应控制，检查模型究竟依赖什么。对线性重建、空间分类和深度模型，应分别验证，避免一项结果被无限推广。[24](#ref-neural-speech-tracking-gaze)[32](#ref-neural-speech-tracking-gaze2024)

2025 年比较未主动关注条件下不同刺激的研究发现，群体信噪比关系与个体阈值预测并不等价；自然言语也未在所有频段中优于较简单刺激。同期听力恢复研究揭示儿童不同时间尺度的变化，为发展与临床研究提供线索，同时保留人群和记录方法的边界。[33](#ref-neural-speech-tracking-comparison2025)[39](#ref-neural-speech-tracking-ci2025)

截至 2026 年 10 月 7 日，Mo 等人的成人纵向研究已正式发表：19 名新植入使用者在开机及随后 3、6、12 月接受连续言语记录和行为测试，目标跟踪与部分行为和生活质量结果相关。群体较早阶段的变化不等于所有人的固定恢复时间，也不单独证明跟踪变化导致行为改善。[36](#ref-mo-ci-adaptation-2026)

同年 Guo 等人的三个公开数据集基准研究分别检验条件、注意和个体阈值目标，发现群体条件及注意效应较稳健，而个体阈值的推广仍依赖协议。这为词条提供一个关键结论：**言语神经跟踪是一组有价值的表征与验证方法，其意义必须由特征、任务和独立证据共同决定。**[7](#ref-guo-tracking-2026)
