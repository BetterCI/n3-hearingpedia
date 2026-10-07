---
title: "纯音测听"
english: "Pure-tone audiometry"
slug: "pure-tone-audiometry"
summary: "系统介绍气导与骨导听阈、听力图、声级标度、临床搜索与掩蔽程序、校准和质量控制，以及自动测听和主动学习模型。"
categories: ["audiology","hearing-loss"]
tags: ["PTA"]
aliases: ["PTA"]
batch: 2
status: draft
depth: in-depth
last_updated: "2026-10-07"
literature_checked_at: "2026-10-07"
authors: ["AI 辅助编写"]
references: ["pure-tone-audiometry-asha", "pure-tone-audiometry-iso8253", "pure-tone-audiometry-gb16296", "pure-tone-audiometry-bsa", "pure-tone-audiometry-iso3891", "pure-tone-audiometry-iso3892", "pure-tone-audiometry-iso3893", "pure-tone-audiometry-symbols", "pure-tone-audiometry-adult-assessment", "pure-tone-audiometry-who", "pure-tone-audiometry-psychometric", "pure-tone-audiometry-false-gap", "pure-tone-audiometry-osha", "pure-tone-audiometry-high-frequency", "pure-tone-audiometry-swanepoel", "pure-tone-audiometry-guo", "pure-tone-audiometry-anc", "pure-tone-audiometry-song", "pure-tone-audiometry-bal-paper", "pure-tone-audiometry-bal-code", "pure-tone-audiometry-psignifit", "pure-tone-audiometry-auto-review", "pure-tone-audiometry-digital-review", "pure-tone-audiometry-carhart"]
order: 17
knowledge_area: "measurement"
kind: "test"
key_facts: [{"label":"测量对象","value":"各频率的检测敏感度"},{"label":"主要方式","value":"气导与骨导"},{"label":"常用标度","value":"dB HL；参照条件需匹配"}]
---

**纯音测听**（pure-tone audiometry）是使用经过校准的纯音刺激，按照规定的呈现和反应判定程序，测量听者在不同频率上的听觉检测阈的方法。测量通常分别记录左右耳的气导听阈和骨导听阈，并以听力图或数据表报告。它是描述听觉敏感度、评估听力损失和开展听觉研究的重要基础，但测得的“最小可听水平”不等于听者理解言语、分离声源或辨别音高的全部能力。[1](#ref-pure-tone-audiometry-asha)[2](#ref-pure-tone-audiometry-iso8253)

纯音测听把一个复杂的听觉过程转化为可比较的测量结果：在明确的频率、传入方式、耳别和环境条件下，听者能否可靠地报告一个声音。声音的实际输出由设备与换能器决定，听者的反应又受到听觉状态、注意和反应判据影响。因此，准确测听既依赖物理校准，也依赖行为程序和质量控制；只有标明这些条件，听力图上的数值才具有清楚的含义。

我国现行的 GB/T 16296.1-2018《声学 测听方法 第1部分：纯音气导和骨导测听法》对应采用 ISO 8253-1:2010。ISO 官方目录显示，后者在 2026 年复审确认。本文以这些标准的公开适用范围及专业学会可访问的指南说明概念与方法，不转录未取得全文的标准表格。成人及能理解任务的较大儿童的常规行为测听是本文的主要对象；婴幼儿或反应困难者需要相应的行为方法与客观检查。[3](#ref-pure-tone-audiometry-gb16296)[2](#ref-pure-tone-audiometry-iso8253)[4](#ref-pure-tone-audiometry-bsa)

## 测量对象与基本概念

### 纯音、检测阈与听力图

理想纯音具有单一频率。测听中的声音则有有限持续时间和起止过渡，不能理解为无限长的正弦波。实际设备还可能使用脉冲纯音或调频音，以便与耳鸣区分，或满足特定测试环境的需要。改变刺激形式时，应记录其类型和呈现条件，不能把所有声音都笼统标为同一种“纯音”。[1](#ref-pure-tone-audiometry-asha)

检测阈不是每次呈现都能被听见的绝对边界。靠近阈值时，同一声级可能有时引起反应、有时没有反应；规定的搜索规则把这种不确定性转化为一个可复测的估计值。研究中的心理测量函数可以描述“呈现水平—反应概率”的关系，临床程序则用有限的上升试次和重复反应作出判断，两者相关，但不能把临床听阈当作已经精确拟合出的概率参数。[11](#ref-pure-tone-audiometry-psychometric)[4](#ref-pure-tone-audiometry-bsa)

听力图通常以频率为横轴、听力级为纵轴。频率按对数间距排列，一个倍频程所占的横向距离相同；听力级数值从上向下增大，所以较低的图上位置代表需要更高的呈现水平，而不是“听得更好”。左右耳、气导与骨导、掩蔽与未掩蔽需要使用可以区分的符号。[8](#ref-pure-tone-audiometry-symbols)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/pure-tone-audiometry/01-audiogram-coordinates-and-symbols.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/pure-tone-audiometry/01-audiogram-coordinates-and-symbols.svg" alt="听力图坐标、左右耳气骨导符号及独立的无反应记录示例" loading="lazy" /></a>
<figcaption><p>图 1　听力图的坐标与记录符号。左图使用人工构造的双耳气导及掩蔽骨导数据；骨导符号的轻微横向错开只为避免重叠，实际测试频率没有改变。右图列出常见符号，并单独展示带向下箭头的无反应记录：它表示在标示的可用呈现水平未获得反应，不是已经测得该处听阈。红、蓝分别辅助标识右、左耳，符号本身也保留耳别信息。[8](#ref-pure-tone-audiometry-symbols)</p></figcaption>
</figure>

### 气导、骨导与声场测量

气导测听通过耳机把声音送入耳道，刺激经外耳、中耳及内耳传入听觉系统。骨导测听通过骨振器施加机械振动，使颅骨振动激励听觉系统。骨导常被简化为“绕过外耳和中耳”，但它并不是只由某一个内耳结构决定的纯粹读数；放置、接触力、耳道是否闭塞以及两耳的敏感度都可能影响结果。[9](#ref-pure-tone-audiometry-adult-assessment)[7](#ref-pure-tone-audiometry-iso3893)

骨振器放在右侧，不保证反应一定来自右耳。颅骨振动可能被两耳接收，较敏感的一耳可能决定未掩蔽骨导结果；气导在足够高的输出下也可能跨耳被听见。因此，“设备放在哪一侧”和“最终是哪一耳提供反应”必须分开考虑，需要时通过对侧掩蔽建立耳别信息。[4](#ref-pure-tone-audiometry-bsa)

声场测量通过扬声器呈现声音，常用于特定人群或助听条件下的功能评价。未采取特定控制时，双耳均可接收声场输入，结果不能直接当作某一耳的耳机听阈。佩戴助听器获得的声场检测结果也涉及设备处理与测试设置，不能与裸耳气导听力图简单相减得到“恢复的听力”。ISO 8253-1 的公开范围不包含以扬声器为声源的测听。[2](#ref-pure-tone-audiometry-iso8253)[9](#ref-pure-tone-audiometry-adult-assessment)

### PTA 缩写与平均听阈

PTA 既可能指“纯音测听”，也可能指“纯音平均听阈”。后者把若干指定频率的听阈取平均，例如：

$$
\overline{H}=\frac{1}{K}\sum_{i=1}^{K}H(f_i).
$$

其中，$H(f_i)$ 为某一耳在频率 $f_i$ 上的听阈，单位为 dB HL。报告平均值必须注明耳别和频率组合。500、1000、2000 Hz 的三频平均，与加入 4000 Hz 的四频平均不是同一指标；较好耳、较差耳和双耳分别平均也回答不同的问题。世界卫生组织的听力损失分级使用特定的频率及耳别规则，不能把任意“PTA”值直接套入同一分级。[10](#ref-pure-tone-audiometry-who)

## 听力级、声压级与校准

### 0 dB HL 为什么不等于没有声音

声压级 dB SPL 以空气中的参考声压为零点；听力级 dB HL 则使用相应频率、换能器及规定耦合条件下的参考听阈作为零点。对气导设备，在匹配的校准条件下可以写成：

$$
L_{\mathrm{HL}}(f)=L_{\mathrm{SPL,coupler}}(f)-\mathrm{RETSPL}(f).
$$

RETSPL 是参考等效阈声压级。这个关系用于说明听力级的参考含义，不能把某个耦合器声压直接视为每位听者的实际鼓膜声压。0 dB HL 不等于零声压，也不保证每位听力正常者的听阈恰好为零；个体阈值可以高于或低于参考零点。[5](#ref-pure-tone-audiometry-iso3891)

压耳式、插入式和其他换能器不能任意交换参考值。ISO 389-1 与 ISO 389-2 分别规定相应类型的气导参考零点及适用条件。普通真无线耳机即使外形类似插入式耳机，也不能直接沿用某一标准耳机的参考数据；需要核对型号、耳塞、耦合装置与校准方法。[5](#ref-pure-tone-audiometry-iso3891)[6](#ref-pure-tone-audiometry-iso3892)

### 骨导的参考量与感觉级

骨振器的校准使用规定机械耦合条件下的振动力及参考等效阈振动力级，不能把气导的声压级换算式原样用于骨导。ISO 389-3 的公开范围包括骨振器校准所需的参考量与条件。骨导图上也可以用 dB HL 报告，但气导与骨导的物理输出量不同，共同的听力级标度来自各自的参考框架。[7](#ref-pure-tone-audiometry-iso3893)

研究中还常见感觉级 dB SL，它表示某一呈现水平高于指定个体听阈的程度。若某人在 1000 Hz 的听阈为 30 dB HL，使用相同频率、换能器和测试条件呈现 50 dB HL，便相当于该条件下的 20 dB SL。感觉级不能自动跨频率或跨刺激类型转用，也不是响度的直接单位。可结合[响度](../loudness/)与[动态范围](../dynamic-range/)进一步理解阈上感知。

### 校准不仅是把音量调到某个数字

设备校准与检查需要关注输出水平、频率准确性、失真、信号起止、掩蔽噪声及换能器状态。日常功能检查与周期性客观校准承担不同作用：前者可发现接触不良、异常声或设备故障，后者建立量值与规范要求的联系。把手机音量滑块固定在某一位置，不足以建立可比较的 dB HL 标度。[1](#ref-pure-tone-audiometry-asha)[3](#ref-pure-tone-audiometry-gb16296)

## 测试环境、准备与换能器

### 环境噪声与佩戴

环境噪声可能掩蔽测试音，使测得阈值偏高；这种影响与噪声频谱、测试频率和耳机隔声有关。仅凭房间“听起来很安静”或一个总的 A 计权声级，不能充分判断能否在所有频率测到较低听阈。骨导测试时外界声音更容易进入耳道，环境要求尤其需要注意。间歇噪声也可能影响某一次反应，应记录并在必要时重测。[4](#ref-pure-tone-audiometry-bsa)[15](#ref-pure-tone-audiometry-swanepoel)

佩戴决定声音怎样到达耳朵。压耳式耳机的位置和压紧程度、插入式耳机的耳塞尺寸与插入状态、密封和漏声，均可能改变有效输出。压耳式耳机还可能使某些人的耳道塌陷，产生表面上的气导听阈升高；这类现象不能立即解释为听觉功能改变。换能器位置不应在测试过程中随意移动，重新佩戴后的结果也应保留条件说明。[4](#ref-pure-tone-audiometry-bsa)[16](#ref-pure-tone-audiometry-guo)

### 测试前信息与反应方式

测听前通常需要了解主诉、近期噪声暴露、耳鸣、既往听觉情况和可能影响配合的因素，并检查外耳道及鼓膜可见情况。耳道阻塞、近期噪声暴露和耳部不适都可能改变测量解释；儿童或沟通困难者则需要适合其理解能力的指令和反应任务。这些信息应与听阈结果一起保存。[9](#ref-pure-tone-audiometry-adult-assessment)

听者通常通过按键、举手或其他约定方式表示听见测试音。指导语应说明需要关注微弱声音，以及如何表示声音开始和结束；熟悉阶段用来确认听者理解了任务。可见的设备操作、机械声或固定的呈现节律可能提供与测试音无关的线索，应避免让这些线索决定反应。[1](#ref-pure-tone-audiometry-asha)

## 频率选择与听阈搜索

### 常规频率与测量顺序

常规气导听力图主要覆盖 250–8000 Hz，通常包括 1000、2000、4000、8000、500、250 Hz，并按需要增加 3000、6000 Hz 等中间频率；部分目的还需要 125 Hz。骨导常用范围较窄，常规评价主要集中在较低频率至 4000 Hz，具体能力受骨振器和校准条件限制。不能因为设备菜单里出现某个频率，就认定该频率的测量已经具有充分准确性。[1](#ref-pure-tone-audiometry-asha)[9](#ref-pure-tone-audiometry-adult-assessment)

通常从听者自述较好的一耳和易于理解的 1000 Hz 开始，随后完成其他频率，并用重复测量检查一致性。具体顺序与加测条件应根据测量目的和采用的规范说明。研究中如采用随机频率、更多频点或不同顺序，还应考虑熟悉、疲劳与时间变化是否影响结果。[4](#ref-pure-tone-audiometry-bsa)

### 下降 10 dB、上升 5 dB 的基本逻辑

临床常用的改良 Hughson–Westlake 方法不是不断降低声音直到听者第一次说“听不见”就停止。熟悉任务后，先找到低于可检测水平的位置，再逐步上升；出现反应后降低水平，重新开始上升序列。常见的调整是“无反应时增加 5 dB，有反应时降低 10 dB”，并根据上升试次中的重复反应判定听阈。[1](#ref-pure-tone-audiometry-asha)[4](#ref-pure-tone-audiometry-bsa)

不同指南的有限试次规则需要分别说明。ASHA 2005 年指南给出的最低要求是在同一水平的三次呈现中有两次反应；BSA 2018 年程序允许同一水平在两次、三次或四次上升试次中获得至少两次反应，并达到至少一半的反应比例。两者都强调最低水平、上升试次和重复反应，不能仅记录最后一个有反应的声级，也不能把任意升降算法都称为同一种标准程序。[1](#ref-pure-tone-audiometry-asha)[4](#ref-pure-tone-audiometry-bsa)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/pure-tone-audiometry/02-threshold-probability-and-search.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/pure-tone-audiometry/02-threshold-probability-and-search.svg" alt="理想化心理测量函数与下降10上升5分贝的人工反应序列" loading="lazy" /></a>
<figcaption><p>图 2　概率意义的听阈与有限试次的搜索规则。左图为人为设置的心理测量函数，50% 反应点为 30 dB HL，不含虚报或注意失误。右图是单独构造的教学反应序列：第 6、9 次刺激均在上升过程中于 30 dB HL 获得反应，展示 BSA 程序允许的两次上升反应判定；前面的下降阶段不参与这一计数。两幅图不是同一次模拟的原始数据，也不表示临床读数已经精确等于一个拟合的 50% 点。[4](#ref-pure-tone-audiometry-bsa)[11](#ref-pure-tone-audiometry-psychometric)</p></figcaption>
</figure>

### 时长、间隔与可疑反应

刺激需要有足够持续时间，并控制起止过渡，避免额外的点击线索。呈现间隔应变化，防止听者只按节律作答。若反应迟缓、频繁在无声时按键、无法区分耳鸣与测试音，或对明显可听刺激漏答，应重新确认指令、调整适当的反应安排，并保留可靠性说明。自动程序中的固定反应时间窗尤其需要考虑个体反应速度和设备延迟。[1](#ref-pure-tone-audiometry-asha)[16](#ref-pure-tone-audiometry-guo)

骨导低频高水平刺激可能同时引起振动触觉，骨振器还可能存在空气辐射和输出限制。听者“感觉到振动”与“听到声音”不是同一反应；疑似触觉反应应单独说明。遇到最大可用输出仍无反应，应记录无反应符号及实际呈现水平，而不是填入一个被假定的听阈。[9](#ref-pure-tone-audiometry-adult-assessment)[8](#ref-pure-tone-audiometry-symbols)

## 跨耳听见与临床掩蔽

### 为什么需要向另一耳加入噪声

当测试音经颅骨等路径到达非测试耳，并被该耳检测到时，按键反应可能被误归给测试耳。这会让较差耳看起来比实际更敏感。两耳听阈不对称以及气骨导差较明显时，尤其需要核对跨耳听见的可能性；不能仅凭耳机接在右耳就把所有反应记为右耳结果。[4](#ref-pure-tone-audiometry-bsa)

临床掩蔽向非测试耳呈现与测试频率匹配的窄带噪声，目的是抑制该耳对测试音的贡献，同时继续测量测试耳。这里的[掩蔽](../masking/)是建立耳别测量条件的工具。判断是否需要掩蔽，要考虑测试耳气导水平、非测试耳骨导敏感度、换能器的耳间衰减，以及骨导测试中的耳别不确定性，不能用一个不区分耳机类型的固定数字概括所有情形。[4](#ref-pure-tone-audiometry-bsa)

### 掩蔽平台、过度掩蔽与堵耳效应

掩蔽不足时，非测试耳仍可能听见测试音；噪声逐步增加后，若在一段掩蔽水平范围内重新测得的测试耳听阈保持稳定，便出现掩蔽平台。如果噪声进一步增强并跨到测试耳，测试耳阈值也会受到影响，形成过度掩蔽。平台不是“噪声越大越可靠”的理由，它要求在两种失效情况之间找到可解释的测量范围。[4](#ref-pure-tone-audiometry-bsa)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/pure-tone-audiometry/04-cross-hearing-and-masking.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/pure-tone-audiometry/04-cross-hearing-and-masking.svg" alt="测试音跨耳传递、非测试耳窄带掩蔽以及人工构造的掩蔽平台" loading="lazy" /></a>
<figcaption><p>图 3　跨耳听见和掩蔽平台。左图只表示主要测量关系，不是骨导传播的完整解剖模型。右图用人工构造的曲线说明掩蔽不足、平台和过度掩蔽：平台处测试耳听阈为 40 dB HL。横轴的 dB EML 表示有效掩蔽级，与纵轴 dB HL 不同；图中数值不能用来设定实际患者的起始噪声、步长或平台判据。[4](#ref-pure-tone-audiometry-bsa)</p></figcaption>
</figure>

低频骨导测量还要注意堵耳效应：覆盖或堵塞耳道可能增强部分骨导声音的可听性，从而改变测得阈值。用于对侧掩蔽的耳机、原来未掩蔽的测量状态以及重新测量步骤需要相互对应。部分双侧传导问题可能使可用掩蔽范围受限；无法确认耳别听阈时，应记录测量限制，而不是把未充分确认的数值当作确定结果。[4](#ref-pure-tone-audiometry-bsa)

## 听力图判读与解释边界

### 气骨导关系提供的线索

若气导阈值升高，而同一耳经确认的骨导阈值较好，气骨导差可提示声音传导环节的影响。若气导与骨导均升高且差值不明显，则支持感音神经性模式；若骨导阈值升高，同时仍有明显气骨导差，则可能呈混合性模式。这些是测量模式的解释，需要结合耳镜、声导抗、病史及其他检查，不能单凭一组阈值直接确定病因或具体受损结构。[9](#ref-pure-tone-audiometry-adult-assessment)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/pure-tone-audiometry/03-air-bone-patterns.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/pure-tone-audiometry/03-air-bone-patterns.svg" alt="人工构造的传导性、感音神经性和混合性气骨导听力图模式" loading="lazy" /></a>
<figcaption><p>图 4　三种气骨导模式的教学对照。三图均用右耳掩蔽气导三角形和掩蔽骨导方括号表示已经建立耳别的阈值条件，骨导只绘至 4000 Hz。传导性示例的骨导较好而气导升高；感音神经性示例的两种阈值接近且共同升高；混合性示例同时出现骨导升高与气骨导差。图中数据和差值为解释概念而构造，不是诊断截断值，也不规定所有此类听力损失的图形。[9](#ref-pure-tone-audiometry-adult-assessment)[8](#ref-pure-tone-audiometry-symbols)</p></figcaption>
</figure>

实际测量也可能出现假性气骨导差。Margolis 等对 4000 Hz 的研究说明，气骨导差的大小可能受到骨导参考与测量系统影响，即使听者并不存在相应的传导病变也可能出现差值。遇到孤立频点的异常，应检查校准、佩戴、掩蔽与重复性；这项研究也不能被反向用于宣称所有 4000 Hz 气骨导差都是假性结果。[12](#ref-pure-tone-audiometry-false-gap)

### 程度、形状、耳别与时间过程

描述听力图应至少包含程度、频率形状和左右耳关系。例如，高频下降、较平坦、低频较差或某些频率的局部凹陷，是对图形的描述，不是病因名称。与既往结果比较时，还需要时间和测试条件。程度分级采用哪套标准、平均哪些频率、按哪一耳报告，都应明确；成人、儿童、筛查和职业监测不必使用相同的判断框架。[10](#ref-pure-tone-audiometry-who)[9](#ref-pure-tone-audiometry-adult-assessment)

同一平均听阈可以对应不同的频率分布。下面两位教学听者在 500、1000、2000、4000 Hz 的平均值均为 40 dB HL，但一位较平坦，另一位低频较好、高频明显较差。因此，平均值适合概括某个指定指标，却不能代替完整听力图，也不足以说明不同频率的言语信息是否同样可听。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/pure-tone-audiometry/05-equal-average-different-audiograms.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/pure-tone-audiometry/05-equal-average-different-audiograms.svg" alt="四频平均听阈相同的平坦型与高频下降型人工听力图" loading="lazy" /></a>
<figcaption><p>图 5　相同平均值不意味着相同频率敏感度。甲的四个平均频点均为 40 dB HL；乙依次为 10、20、50、80 dB HL，平均仍为 40 dB HL。右图显示乙减甲的听阈差，正值表示乙需要更高水平才能检测。两组数据没有附带言语识别实验，不能据此计算或断言谁在实际交流中表现更好。</p></figcaption>
</figure>

### 听阈正常仍可能有聆听困难

纯音测听主要考察安静、规定频率及简单刺激下的检测敏感度。[言语可懂度](../speech-intelligibility/)、声音分组、时域线索利用、双耳处理和聆听努力需要其他任务评价。常规频率听阈较好，不排除噪声中的交流困难；反过来，也不能仅凭这种困难就诊断某一种隐匿性损伤。[9](#ref-pure-tone-audiometry-adult-assessment)[10](#ref-pure-tone-audiometry-who)

对检测阈与言语表现的关系，应结合刺激可听性、听觉加工及语言和认知条件解释。测听结果提供了重要基础，但不能独立预测助听器或人工耳蜗的全部获益。设备评价宜同时保留裸耳听阈、适当的助听测量、言语任务和听者自述，避免把“检测到声音”与“理解交流内容”混为一谈。

## 重复性、随访与研究报告

### 单个频点变化怎样理解

临床读数常以 5 dB 为间隔，重复测量会受佩戴、环境、注意及反应判据影响。一次测量比上次差 5 dB，不自动证明出现永久性损伤；应结合重复测量、相邻频率、两耳模式和测试条件判断。骨导及扩展高频的误差来源又与常规气导不同，不宜为所有频率规定一个没有来源的统一“允许误差”。[1](#ref-pure-tone-audiometry-asha)[14](#ref-pure-tone-audiometry-high-frequency)

职业监测中的“标准听阈位移”是特定制度下的定义。例如，美国 OSHA 规定中，该指标涉及一耳在 2000、3000、4000 Hz 相对基线的平均变化达到 10 dB 或更多。它不是所有临床情境下的损伤诊断界限，也不能替代中国适用的职业健康规范。引用这类指标时，应同时说明制度来源、基线和计算频率。[13](#ref-pure-tone-audiometry-osha)

### 方法比较应报告什么

比较手动与自动测听、不同耳机或不同环境时，应分别报告有方向的偏差、绝对差、差值分布与重复性。平均正负差接近零，可能只是正负误差相互抵消；相关系数较高，也不证明两套系统在绝对听阈上可以互换。最好按频率、耳别和听力程度检查误差，并说明两种方法的测试顺序。[16](#ref-pure-tone-audiometry-guo)[17](#ref-pure-tone-audiometry-anc)

研究报告应保留换能器型号、校准依据、频率与刺激形式、声级搜索规则、阈值判据、掩蔽状态、环境控制、无反应处理和参与者特征。把同一人的两耳作为完全独立样本，或把超过输出上限的无反应记录当作精确数值进行平均，都会改变统计解释。复测、异常点处理及数据排除规则宜在分析前明确。[1](#ref-pure-tone-audiometry-asha)[23](#ref-pure-tone-audiometry-digital-review)

## 扩展高频、筛查与自动测听

### 扩展高频测听

高于 8000 Hz 的扩展高频测听能够补充常规频率之外的检测敏感度信息，但对耳机位置、个体耳道条件、设备可用输出和参考量提出额外要求。Casolani 等在 2024 年比较了标准、迫选和贝叶斯主动学习程序的 8–16 kHz 测量，发现方法差异及变异程度与频率有关。其结果支持进一步验证这类工具，不能据常规测听的精度假定扩展高频具有完全相同的重复性。[14](#ref-pure-tone-audiometry-high-frequency)

### 固定水平筛查与阈值测量

固定水平筛查通常回答“在规定频率和水平上是否通过”，完整阈值测量则估计各频率的最小可检测水平。通过某套筛查，不等于已经测得一张正常听力图；筛查未通过也需要结合噪声、佩戴、任务理解及复核流程解释。手机筛查研究显示，校准、环境监测与数据质量控制是系统的组成部分，而不是获得结果后的附加选项。[15](#ref-pure-tone-audiometry-swanepoel)[2](#ref-pure-tone-audiometry-iso8253)

### 自动测听与真无线耳机

自动测听可以按预先规定的逻辑呈现刺激、收集反应、搜索阈值并保存记录；自动化并不限定为某一种算法，也不意味着不再需要质量控制。Mahomed 等的系统综述与后续数字听力评估综述都强调，需要分别考虑气导、骨导、人群及使用环境的验证证据，不能把某个系统的有效性概括为“所有自动测听都准确”。[22](#ref-pure-tone-audiometry-auto-review)[23](#ref-pure-tone-audiometry-digital-review)

Guo 等 2021 年研究使用真无线耳机建立电声与行为校准，并与常规气导测量比较，还处理了蓝牙延迟和个体反应时间的问题。该研究说明消费级换能器可以在经过专门设计与验证的系统中承担测听功能，同时指出低频、佩戴以及左右耳不对称等限制。不能把论文中的校准结果转用于任意手机、耳机或软件版本。[16](#ref-pure-tone-audiometry-guo)

Zhou 等于 2024 年在线发表的研究进一步考察带主动降噪的真无线耳机。经校准的特定系统，在 125–8000 Hz 的倍频程测量中，相对安静环境标准手动测听的平均绝对差分别为 5.2 dB（安静、未开启主动降噪）、5.4 dB（40 dBA 粉红噪声、开启主动降噪）和 9.3 dB（55 dBA 粉红噪声、开启主动降噪）。这些是论文中的特定条件和样本结果，显示性能仍随噪声水平变化；主动降噪的状态还可能影响耳机输出，不能把降噪开关当作独立于校准的功能。[17](#ref-pure-tone-audiometry-anc)

## 计算模型、算法与公开实现

### 心理测量函数模型

单一频率下，可以用呈现水平 $L$ 与报告听见的概率建立模型。一个教学表达式是：

$$
P(y=1\mid L,f)=\gamma+(1-\gamma-\lambda)\,
\frac{1}{1+\exp\left[-(L-\theta(f))/s(f)\right]}.
$$

$y=1$ 表示报告听见；$\theta(f)$ 描述曲线位置，$s(f)>0$ 控制斜率；$\gamma$ 和 $\lambda$ 分别描述低水平虚报与高水平失误。对“听见／未听见”任务，$\gamma$ 不能不经说明地固定为二选一迫选任务的 0.5。参数的含义、阈值概率点与反应任务需要相互匹配；加入虚报和失误后，$\theta$ 也不必恰好对应 50% 的原始反应概率。[11](#ref-pure-tone-audiometry-psychometric)

公开的 [psignifit Python 实现](https://github.com/wichmann-lab/python-psignifit)可用于心理测量函数估计及不确定性分析。它是分析工具，不是已经校准的听力计；选择模型时应核对任务类型、上下渐近线和先验，并检查拟合及数据量。临床的有限上升试次读数与模型拟合结果可以比较，但不能默认它们遵循相同的统计定义。[21](#ref-pure-tone-audiometry-psignifit)

### 高斯过程与贝叶斯主动学习

传统测听常逐个频率搜索阈值。高斯过程方法则把频率—声级平面上的反应关系作为一个联合估计问题，利用已有反应更新模型，并选择预计能减少不确定性的下一次刺激。模型可以给出连续频率上的估计，但未实际测试的频点仍然是依赖假设的推断，不是新增的直接测量值。Song 等 2015 年和 Schlittenlacher 等 2018 年的研究提供了这条方法路线的原始证据。[18](#ref-pure-tone-audiometry-song)[19](#ref-pure-tone-audiometry-bal-paper)

Schlittenlacher 等比较了计数任务与考虑失误的“是／否”任务。其研究中主动学习估计较常规听力图出现约 2–4 dB 的系统性较低阈值，作者讨论了反应判据的可能影响。这提示更快或更平滑的估计并不自动等于更“真实”的听阈；验证需要同时检查测量时间、系统偏差、局部异常和反应任务。[19](#ref-pure-tone-audiometry-bal-paper)

论文对应的 [BALaudiogram 仓库](https://github.com/cambridge-mlg/BALaudiogram)提供 MATLAB 程序，依赖 GPML 工具箱。仓库说明要求修改耳机至耳膜的传递校正与参考量，不能下载后直接把默认输出当作有效 dB HL。模型可能平滑窄频异常，也可能在先验与真实听力图不匹配时产生较小但不可靠的不确定性，因此应保留足够的探索、重复性检查和无声检查试次。[20](#ref-pure-tone-audiometry-bal-code)[18](#ref-pure-tone-audiometry-song)

### 本词条的可复现教学代码

本词条提供[配图生成代码](/n3-hearingpedia/figures/pure-tone-audiometry/generate-figures.py)与[数值核查记录](/n3-hearingpedia/figures/pure-tone-audiometry/figure-verification.json)，展示听力图坐标、阈值搜索序列、掩蔽平台和平均听阈的计算。代码仅生成图形，不播放声音、不连接听力计，也不实现完整临床测量或贝叶斯主动学习程序。它适合检查图示的数学和记录逻辑；需要进行真实测听时，仍须使用经过校准和验证的系统。

## 研究沿革与关联词条

纯音测听的发展同时依赖可控的刺激输出、参考零点和一致的行为判定程序。Carhart 与 Jerger 1959 年的经典方法论文是临床阈值确定的重要历史来源，后续专业指南进一步规范设备、反应和记录。近年来，研究从自动执行既有搜索程序扩展到移动筛查、连续听力图估计、主动学习及噪声环境中的换能器验证，核心问题仍是结果是否可追溯、可复测，以及能否在目标人群和环境中成立。[24](#ref-pure-tone-audiometry-carhart)[23](#ref-pure-tone-audiometry-digital-review)

与本词条直接衔接的内容包括[听力损失](../hearing-loss/)、[听力测量校准](../audiometric-calibration/)、[掩蔽](../masking/)、[言语接收阈](../speech-reception-threshold/)以及[听觉诱发电位](../auditory-evoked-potential/)。它们分别补充损伤表型、物理量值、耳别控制、言语任务和神经生理测量，帮助把一张听力图放回完整的听觉评价体系。
