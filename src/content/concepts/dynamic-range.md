---
title: "动态范围"
english: "Dynamic Range"
slug: "dynamic-range"
summary: "声音、听觉系统或听觉设备能够有效表示和利用的水平跨度；它连接听阈、响度增长、耳蜗非线性、助听器压缩和人工耳蜗电刺激映射。"
categories: ["psychoacoustics","hearing-loss","hearing-aids","cochlear-implants"]
tags: ["dynamic-range","loudness","loudness-recruitment","compression","WDRC","electrical-dynamic-range","input-dynamic-range"]
aliases: ["auditory dynamic range","perceptual dynamic range","residual dynamic range","electrical dynamic range","input dynamic range","听觉动态范围","电动态范围","残余动态范围"]
status: draft
last_updated: "2026-10-05"
authors: ["AI 辅助重构"]
reviewer: null
reviewed_at: null
literature_checked_at: "2026-10-05"
illustration: {"src":"figures/dynamic-range-populations.svg","alt":"正常听力、耳蜗性听损、声音耐受下降和人工耳蜗的动态范围概念比较","caption":"动态范围缩窄可以来自下界升高、上界下降，或设备接口本身可用范围较窄；图为概念示意，不是统一临床常模。"}
knowledge_area: "perception"
kind: "quantity"
key_facts:
  - {label: "核心含义", value: "从最低有效水平到最高有效或可接受水平之间的跨度"}
  - {label: "正常声学听觉", value: "threshold–LDL 临床范围典型约 95 dB，但随频率和测量定义变化"}
  - {label: "耳蜗性听损", value: "阈值升高通常大于 LDL/UCL 上移，可形成缩窄的 residual dynamic range"}
  - {label: "助听器", value: "WDRC 把较宽声学输入范围映射到较窄残余听觉范围"}
  - {label: "人工耳蜗", value: "声学 IDR 需非线性映射到更窄的 electrical T–C/M range"}
  - {label: "关键边界", value: "范围宽度不等于响度增长，也不等于范围内可辨信息数量"}
references: ["moore-loudness-2014","sherlock-formby-2005","wen-dynamic-range-2009","keidser-nalnl2-2011","zeng-2008","zeng-speech-dr-2002","nunn-ci-idr-2019","mo-maxima-2023","iso-16832-2006","liu-ci-range-2026"]
batch: 3
order: 32
---

**动态范围**（dynamic range, DR）是听觉科学中最基础、也最容易被低估的概念之一。它描述一个**声音、设备、感觉系统或刺激接口能够有效表示、传输或利用的水平跨度**。真正重要的并不只是“上界减下界”这个数值，而是：外部声音的宽声级范围，怎样经过耳蜗、神经系统或听觉设备，被重新映射到有限的知觉范围中。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

> **从正常听觉到听力损失、助听器和人工耳蜗，很多核心问题都可以重新表述为：有限动态范围内的信息应该怎样分配和保留？**

![不同听觉状态的动态范围](/n3-hearingpedia/figures/dynamic-range-populations.svg)

## 动态范围不是只有一种

### 1. 声学或信号动态范围

对于声音、麦克风、放大器或数字系统，动态范围通常描述**噪声底以上的最低有效信号到饱和、削波或指定最大输出之间的跨度**。它可以用 dB SPL、dB FS 或其他工程标度表达。

工程动态范围并不等于听觉动态范围。一个 ADC 能表示 100 dB 范围，并不表示听者就能在这 100 dB 内获得正常响度或正常信息分辨率。

### 2. 听觉或知觉动态范围

临床上常把某频率的可听阈值与 loudness discomfort level（LDL）或 uncomfortable loudness level（UCL）之间的差定义为听觉动态范围：

$$
DR(f)=L_{\mathrm{UCL/LDL}}(f)-L_{\mathrm{threshold}}(f)
$$

Sherlock 与 Formby 对 59 名正常听力成人的规范性研究中，pure-tone LDL 大约在 100 dB HL 附近，threshold-to-LDL 动态范围平均约 **95 dB**；具体数值会随频率、程序和指导语变化。[2](#ref-sherlock-formby-2005 "Estimates of loudness, loudness discomfort, and the auditory dynamic range: normative estimates, comparison of procedures, and test-retest reliability")

这里的上界是**不舒适/不能继续舒适聆听的行为边界**，不是“从这一声级开始一定造成听力损伤”的安全边界。

### 3. 残余动态范围

对听力损失者，更有意义的是 **residual auditory dynamic range**：在听阈升高后，还剩多少范围可以用来承载响度、语音和环境强度变化。

例如，若某频率听阈从 0 dB HL 升至 60 dB HL，而 UCL 仍接近 100 dB HL，那么可利用范围从约 100 dB 缩窄到约 40 dB。真实个体不会如此整齐，但这个例子揭示了助听器压缩的根本问题。

### 4. 人工耳蜗电动态范围

在[人工耳蜗](../cochlear-implant/)中，electrical dynamic range（EDR）通常位于行为阈值 T/THR 与最高舒适水平 C/M 之间。具体命名和设备标度随厂商而异，且必须连同：
- 电极；
- 脉宽；
- 脉冲率；
- 刺激模式；
- 电流单位/clinical unit

一起解释。[5](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

### 5. CI 输入动态范围

CI 的 input dynamic range（IDR）是另一个完全不同的概念：它描述**多宽的声学输入范围被处理器纳入并映射进电刺激动态范围**。EDR 是“电刺激能用多少”，IDR 是“外界哪些声级被送进这段电范围”。

## 正常听觉为什么能处理如此宽的声级范围

人类行为听觉可以在极宽的声级范围内保持有用的强度辨别，而单个听神经纤维的 rate–level function 通常只覆盖远窄于整个行为范围的区间。Wen 等的听神经研究把这个矛盾称为重要的 **dynamic-range problem**：外部声级跨度可达约 100–120 dB，而单根听神经纤维的放电率动态范围往往只有几十 dB。[3](#ref-wen-dynamic-range-2009 "Dynamic Range Adaptation to Sound Level Statistics in the Auditory Nerve")

这意味着正常听觉并不是靠一个神经元“从最小声一直编码到最大声”，而要依赖多个机制共同完成：
- 不同阈值和自发放电率的神经纤维群体；
- 神经群体招募；
- 不同响应饱和区间；
- 外周与中枢增益调节；
- 对当前环境声级统计的适应。

Wen 等还显示，听神经 rate–level function 可以随环境声级分布发生一定程度的移动，把更多编码精度放在当前更常出现的声级附近。[3](#ref-wen-dynamic-range-2009 "Dynamic Range Adaptation to Sound Level Statistics in the Auditory Nerve")

因此，**动态范围既是一个“范围宽度”问题，也是一个“自适应信息编码”问题。**

## 耳蜗本身就是非线性动态范围转换器

正常[耳蜗](../cochlea/)并不是线性放大器。[外毛细胞](../outer-hair-cell/)参与的主动过程在低声级附近提供较大增益，而随声级升高，增益逐渐减小，使局部机械输入—输出关系呈压缩性非线性。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

其功能意义可以概括为：

**弱声需要高增益 → 中等声需要较少增益 → 强声几乎不需要同等增益。**

这让有限的毛细胞、突触和神经放电范围能够承载更宽的外部声音范围。

因此，动态范围问题并不是助听器才有的问题；**正常耳蜗本身就在持续做动态范围映射。**

## 听力损失：动态范围为什么会缩窄

典型耳蜗性[听力损失](../hearing-loss/)并不是把整条响度函数简单向右平移。常见情况是：
- 听阈明显升高；
- 高声级响度可以接近正常；
- LDL/UCL 的上移通常小于听阈上移；
- 因此 residual dynamic range 缩窄。

这种现象与 **loudness recruitment** 密切相关：在阈值升高后，从“刚刚听到”到“很响”的响度增长发生在更窄的物理声级区间内。[1](#ref-moore-loudness-2014 "Development and Current Status of the “Cambridge” Loudness Models")

但需要严格区分两个概念：

- **dynamic range**：主要描述上下界之间的跨度；
- **loudness growth**：描述整个声级—响度函数的形状。

两名听者即使 DR 宽度相近，中间的响度函数也可能完全不同。

## Recruitment 不是“声音耐受低”的同义词

耳蜗性 recruitment 常见的概念模式是**下界上升得多，上界变化较小**，因此范围从低声级端被压缩。

另一些声音耐受异常则可以表现为 UCL/LDL 本身下降，即**上界向下移动**。两种情况都可以得到“动态范围缩小”，但病理和临床意义并不相同。

因此研究和临床不能仅报告一个 DR 数字，还应同时保留：
- threshold；
- MCL；
- UCL/LDL；
- categorical loudness growth。

## Categorical Loudness Scaling：比两个端点更完整

如果只测 threshold 与 UCL，就只知道动态范围的两端。categorical loudness scaling（CLS）则要求听者把多个声级评价为 very soft、soft、medium、loud、very loud 等类别，从而估计完整的声级—响度函数。

ISO **16832:2006** 专门规定了听力学 categorical loudness scaling 的基本方法，该标准在 2025 年系统审查后仍被确认继续有效。[9](#ref-iso-16832-2006 "ISO 16832:2006 Acoustics — Loudness scaling by means of categories")

从 Hearingpedia 的角度，CLS 非常重要，因为它把“动态范围”从一个差值升级成了一个**函数**：

$$
\mathrm{Loudness}=F(\mathrm{Sound\ Level})
$$

未来个体化 hearing-device fitting 很可能更应该拟合这个函数，而不仅是使用听阈。

## 助听器：本质上就是动态范围映射器

[助听器](../hearing-aid/)面对的根本任务之一是：

> **把环境中较宽的 acoustic input range 映射进听损者较窄的 residual auditory range。**

这就是 WDRC（wide dynamic range compression）的核心生理学理由之一。[4](#ref-keidser-nalnl2-2011 "The NAL-NL2 Prescription Procedure")

对于某一近似线性压缩区段：

$$
CR=\frac{\Delta L_{\mathrm{in}}}{\Delta L_{\mathrm{out}}}
$$

若输入增加 20 dB，输出增加 10 dB，则该区段 compression ratio 为 2:1。

理想化理解是：

- 弱输入：更多增益；
- 中等输入：适度增益；
- 强输入：较少增益；
- 接近上限：MPO/limiting 避免过大输出。

![正常耳、助听器与人工耳蜗的动态范围映射](/n3-hearingpedia/figures/dynamic-range-mapping.svg)

## 压进去，不等于信息完整保留

动态范围压缩的最大矛盾是：

**提高可听性**  
可能同时  
**降低原来的强度对比。**

过强或过快的压缩可能改变：
- [时域包络](../temporal-envelope/)深度；
- 辅音与元音之间的声级关系；
- 频谱对比；
- 瞬态；
- 两耳 ILD；
- 音乐强弱层次。

因此最优策略不是“把所有声音全部塞进残余范围”，而是**在有限范围中保留最有价值的信息结构**。

这也是为什么仅报告 compression ratio 不足以描述一个助听器：attack/release time、frequency channels、kneepoint、MPO 与双耳同步都会改变最终结果。

## 语音本身也有动态范围

传统言语可懂度模型常用一个有限声级窗口描述每个频带中对识别最重要的语音能量，但这不应被误解为“自然语音的物理动态范围只有几十 dB”。

Zeng 等直接分析语音包络并研究 CI 的 input dynamic range，报告语音包络声级分布约 **50 dB**；在 10 名 CLARION 用户中，约 **50–60 dB IDR** 对语音识别最有利。[6](#ref-zeng-speech-dr-2002 "Speech dynamic range and its effect on cochlear implant performance")

这说明“有效语音动态范围”本身也取决于：
- 语料；
- 时间尺度；
- 频带；
- 说话人；
- 是否关注长期平均还是瞬时包络。

## 人工耳蜗：动态范围问题被推到极端

CI 把声学输入映射到电刺激，而电刺激的可用知觉范围通常远窄于正常声学听觉。[5](#ref-zeng-2008 "Cochlear Implants: System Design, Integration and Evaluation")

可以把这一链条写成：

**acoustic input → processor IDR → amplitude mapping → electrode-specific T–C/M range → neural recruitment → loudness**

其中任何一步改变，都可能影响最终感知。

### EDR 与 IDR 必须分开

两个人可以有相似 EDR，但若处理器 IDR 不同，弱声可听性和输入声级分布仍可能不同。

反过来，即使 IDR 相同，不同电极的 T/C、神经状态和电流扩散也会产生不同的实际响度映射。

Nunn 等系统综述汇总了 32 项关于 T level、IDR 和 stimulation rate 的研究，结论指向明显的参数交互和研究异质性，并不支持一个适用于所有 CI 用户的统一最优设置。[7](#ref-nunn-ci-idr-2019 "A systematic review of the impact of adjusting input dynamic range (IDR), electrical threshold (T) level and rate of stimulation on speech perception ability in cochlear implant users")

## 范围宽度不等于范围内的信息分辨率

这是动态范围词条最重要的概念之一。

设两名听者的 EDR 都是 20 个单位，并不能推出：
- 两人有相同数量的 loudness JND；
- 两人有相同 neural recruitment；
- 两人有相同 speech information capacity。

因此必须区分：

### Dynamic-range width
从下界到上界有多宽。

### Resolution within the range
在这段范围里有多少个稳定、可辨、可用的知觉状态。

既有 CI 研究也提示，electrical dynamic range 与 maxima 数、语音任务和个体刺激条件会相互作用，不能把“更宽 EDR”直接解释成“更多有效信息”。[8](#ref-mo-maxima-2023 "Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy")

## 动态范围与音乐、韵律和情感

声音强度不只是“能不能听见”的参数，它还承载：
- stress；
- prosody；
- musical dynamics；
- onset/transient；
- emotional arousal；
- auditory-object boundaries。

因此动态范围压缩的代价可能不是语音正确率立即下降，而是：
- 音乐缺少强弱层次；
- 语调变平；
- 情绪表达减弱；
- 多声源之间的显著度关系改变。

这也是为什么 speech-optimal compression 未必等于 music-optimal compression。

## 动态范围与双耳/空间听觉

两耳之间的声级关系构成 ILD。如果左右设备分别进行快速、独立的增益控制，就可能改变天然的跨耳声级差。

因此动态范围管理不仅是“单耳 loudness fitting”，还可能直接影响[空间听觉](../spatial-hearing/)。

未来双耳 HA/CI 的重要问题之一是：

> **两耳是否应该共享动态范围估计与压缩控制，而不是独立 AGC？**

## 儿童为什么同样需要个体动态范围

儿童的 threshold、MCL、LDL/UCL 直接影响：
- 助听器 MPO；
- WDRC；
- CI T/C/M mapping；
- 可听性；
- 舒适性；
- 长期设备接受度。

儿童无法稳定理解任务时，临床可能借助客观指标和经验参数，但这些并不能天然替代长期个体化行为估计。

因此动态范围不是“成人响度测量的小问题”，而是贯穿儿童听觉康复的核心安全与信息映射参数。

## 测量动态范围时最容易犯的错误

### “UCL 就是安全上限”
不成立。声音不舒适、设备最大输出和长期噪声损伤风险是不同概念。

### “一个频率的 DR 能代表整只耳”
不成立。threshold 与 UCL 都具有明显频率依赖性。

### “听损 60 dB，就等于 DR 减少 60 dB”
不成立。上界也可能改变，必须实际测量。

### “DR 窄，就等于 loudness growth 一定陡”
不完全成立。端点差值与完整响度函数不是同一指标。

### “更大 CI EDR 一定更好”
不成立。还要考虑 JND、神经状态、电流扩散、[通道相互作用](../channel-interaction/)和刺激映射。

### “助听器压缩恢复了耳蜗压缩”
不成立。WDRC 是工程输入—输出变换，并没有重建正常耳蜗的机械、频率和神经非线性。

## 一个统一的多层框架

Hearingpedia 可以把动态范围组织成五层：

**Physical DR → Cochlear DR → Neural DR → Perceptual DR → Device DR**

### Physical DR
环境或信号本身有多宽的声级跨度。

### Cochlear DR
耳蜗机械和毛细胞系统如何把宽范围压缩为可转导范围。

### Neural DR
听神经和中枢群体如何表示强度，以及怎样适应环境统计。

### Perceptual DR
听者从可听到不舒适之间能够利用的范围，以及其中的响度关系。

### Device DR
麦克风、ADC、AGC、WDRC、IDR、T/C/M 等设备层面的可表示和映射范围。

真正的 HA/CI 设计，本质上就是让这些层之间的映射**尽量保留有用信息，而不是仅仅避免削波或避免过响**。

## 当前前沿研究问题

### 1. Dynamic range 是否应成为 auditory phenotype 的核心维度？
临床是否应该像保存 audiogram 一样，保存频率相关的 threshold、MCL、UCL 和 loudness-growth profile？

### 2. 两个端点是否远远不够？
未来 fitting 是否应该直接估计完整的 loudness function，而不只是 HTL + 平均 UCL？

### 3. 能否从生理指标预测个体动态范围？
OAE、ABR、EcochG、MEMR、ECAP/NRT、eABR 能否可靠预测 UCL、C/M level 或 loudness growth，而不是只在群体上相关？

### 4. CI 的真正瓶颈是 EDR 太窄，还是 EDR 内有效状态太少？
应该优化 range width，还是优化 number of discriminable states？

### 5. 在有限范围里应该优先保留什么？
overall level、speech envelope、consonant–vowel contrast、prosody、music dynamics、ILD、transient 和 emotion 之间如何分配“强度信息预算”？

### 6. Fast 与 slow compression 的最优策略是否取决于声景？
是否需要 scene-dependent、task-dependent 的动态范围控制？

### 7. 双耳设备怎样联合管理动态范围？
如何避免压缩破坏 ILD 和空间稳定性？

### 8. AI 能否实现 context-aware dynamic-range mapping？
未来设备是否可以利用实时声景、用户偏好、EMA 与行为结果，持续更新 input→output mapping？

### 9. 动态范围能否成为连接 rate–distortion 与听觉设备设计的桥梁？
有限输出范围本质上意味着有限的“信息预算”。哪些声学维度最值得被保留，是一个可正式用 information-theoretic 方法表达的问题。

## 与其他词条的关系

建议继续阅读：

- [响度](../loudness/)：动态范围内部的知觉增长函数；
- [耳蜗](../cochlea/) 与 [外毛细胞](../outer-hair-cell/)：生物学压缩从哪里产生；
- [听力损失](../hearing-loss/)：残余动态范围为什么因个体而异；
- [助听器](../hearing-aid/)：WDRC 如何进行声学范围映射；
- [人工耳蜗](../cochlear-implant/)：IDR 与 EDR 的区别；
- [时域包络](../temporal-envelope/)：压缩如何改变强度随时间的结构；
- [通道相互作用](../channel-interaction/)：相同 EDR 为什么不等于相同有效信息；
- [空间听觉](../spatial-hearing/)：动态范围处理怎样影响 ILD；
- [言语可懂度](../speech-intelligibility/)：范围映射是否真正转化为交流收益；
- [听觉脑干反应](../auditory-brainstem-response/)：客观指标预测行为动态范围的边界。

## 研究沿革与近期方向

动态范围研究最初主要属于响度心理物理和电声工程问题，随后成为听觉神经编码、助听器压缩和 CI mapping 的共同基础变量。近年来一个明显趋势，是从“测量两个端点”逐步转向：
- 完整 loudness-growth function；
- 环境统计适应；
- 个体化 IDR/EDR；
- 客观指标预测；
- 数据驱动 fitting。

2026 年 Liu 等提出联合神经反应遥测与 eABR 阈值预测 CI 动态范围参数，体现了这一方向从经验 mapping 向多模态预测发展的趋势；在缺少完整独立验证前，它仍应被视为研究方向而非成熟替代方案。[10](#ref-liu-ci-range-2026 "A dual-data-driven approach for predicting cochlear implant dynamic range parameters using neural response telemetry and electrically evoked auditory brainstem response thresholds")

动态范围最终不应只被理解成一个单位为 dB 的差值。它更像是听觉系统的一项**资源约束**：

> **外部世界的信息远比任何单一神经通道或设备输出范围更丰富；听觉系统和听觉设备必须决定，在有限范围内保留什么、压缩什么、牺牲什么。**
