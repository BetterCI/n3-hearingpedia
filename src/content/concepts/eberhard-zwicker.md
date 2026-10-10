---
title: "Eberhard Zwicker"
english: "Eberhard Zwicker"
slug: "eberhard-zwicker"
summary: "从临界带与Bark尺度，到特定响度、声品质和Zwicker音：介绍Eberhard Zwicker如何把听觉实验转化为可计算的心理声学模型，以及这些模型的应用条件与边界。"
categories: ["psychoacoustics", "acoustics", "signal-processing", "research-methods"]
tags: ["研究人物", "科学史", "临界带", "Bark", "响度", "声品质", "Zwicker音"]
aliases: ["埃伯哈德·茨维克", "埃伯哈德·兹维克", "茨维克", "兹维克", "Zwicker", "E. Zwicker"]
level: ["undergraduate", "graduate"]
status: draft
depth: in-depth
last_updated: "2026-10-10"
literature_checked_at: "2026-10-10"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
knowledge_area: "perception"
kind: "person"
key_facts: [{"label":"生卒","value":"1924—1990"},{"label":"主要机构","value":"斯图加特、慕尼黑工业大学"},{"label":"研究主线","value":"临界带、响度与听觉模型"},{"label":"代表遗产","value":"Bark尺度、Zwicker响度、Zwicker音"}]
references: ["zwicker-fastl2024", "zwicker-tumhistory", "zwicker-asa", "zwicker-dega", "zwicker-band1957", "zwicker-bark1961", "zwicker-analytic1980", "zwicker-volk2015", "zwicker-scharf1965", "zwicker-quality2005", "zwicker-program1991", "zwicker-iso1", "zwicker-iso2", "zwicker-after1964", "zwicker-norena2003", "zwicker-review2025", "zwicker-florentine1979", "psychoacoustics-fastl-2007", "zwicker-mathworks"]
batch: 4
order: 119
---

**Eberhard Zwicker**（埃伯哈德·茨维克，1924—1990）是德国声学与心理声学研究者，曾在斯图加特开展听觉研究，1967年到慕尼黑建立电声学研究与教学中心。他的重要贡献，是把“声音的物理变化怎样成为听觉变化”拆成可以实验检验的问题，再用临界带、特定响度和时变处理等概念构造定量模型。[1](#ref-zwicker-fastl2024)[2](#ref-zwicker-tumhistory)

今天，Bark尺度、Zwicker响度计算和“Zwicker音”分别出现在音频分析、声音评价和听觉后效研究中。它们指向不同层次：Bark是与经典临界带相关的频率坐标，响度模型预测规定条件下的知觉量，Zwicker音则是噪声停止后可报告的短暂听觉错觉。理解人物贡献，需要同时看实验、模型和模型适用范围。[6](#ref-zwicker-bark1961)[12](#ref-zwicker-iso1)[14](#ref-zwicker-after1964)

本页四幅图均为本站原创教学图。谱级与积分算例使用明确给出的假设；解析曲线由文献公式计算，不是原论文数据、个体听觉测量或完整ISO算法复现。

<figure class="person-photo-figure person-portrait">
  <a href="/n3-hearingpedia/people/eberhard-zwicker/at-desk.jpg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/people/eberhard-zwicker/at-desk.jpg" alt="Eberhard Zwicker本人照片，© T. Zwicker" width="412" height="347" loading="lazy" /></a>
  <figcaption>Eberhard Zwicker。Zwicker在书桌前。来源：Hugo Fastl《Eberhard Zwicker – Zum 100. Geburtstag》，《Akustik Journal》2024年第1期，第7页图1；原图署名 © T. Zwicker。拍摄年代未注明。 <a href="https://www.dega-akustik.de/fileadmin/dega-akustik.de/publikationen/akustik-journal/24-01/akustik_journal_2024_01_online_artikel1.pdf" target="_blank" rel="noopener">原始来源</a>。图片版权归原权利人，本站内容开放许可不涵盖此图。</figcaption>
</figure>

## 生平与慕尼黑心理声学的形成

### 从通信技术走向信息的接收者

Zwicker于1924年1月15日出生于德国Öhringen。第二次世界大战后，他在斯图加特技术大学学习物理与电气通信技术，1950年取得工程学位，1952年完成博士研究，1956年取得大学任教资格。博士课题研究纯音振幅调制与频率调制的可听界限，已经把传输技术与听觉实验放在一起。[1](#ref-zwicker-fastl2024)

Hugo Fastl的机构历史回顾解释了这一转向：早期磁带录音的质量评价，不能只检查设备输出的物理误差，还要询问人耳能否听见误差。这样，工程中的“失真有多大”便成为心理声学中的“在什么条件下可以察觉”。这是一段后来的学术回顾；它说明研究动机，并不证明现代感知编码的每个具体方案都由Zwicker提出。[2](#ref-zwicker-tumhistory)

他曾赴Harvard、Syracuse和贝尔实验室开展研究。1957年的临界带响度论文署名Zwicker、Gunnar Flottorp和S. S. Stevens，体现了这一阶段的合作。原文还交代了研究分工：多纯音实验与噪声带实验并非由同一人独立完成，不能把整篇论文简化成个人发明故事。[1](#ref-zwicker-fastl2024)[5](#ref-zwicker-band1957)

### 研究传统与荣誉

1967年，他出任慕尼黑新设电声学教席负责人。Ernst Terhardt也从斯图加特来到慕尼黑，Hugo Fastl于1971年加入。机构回顾把临界带、响度、粗糙度、起伏强度、主观时长和声品质等研究的交流，称为“慕尼黑心理声学学派”的形成。这是一种学术传统的概括，并不意味着所有相关模型具有同一结构。[2](#ref-zwicker-tumhistory)

Zwicker于1990年11月22日在Icking去世。美国声学学会记录了他获得1987年心理与生理声学银奖；德国声学学会的官方名单则记载1991年追授Helmholtz奖章。后者发生在他去世之后，应与在世期间的研究和任职区分。[1](#ref-zwicker-fastl2024)[3](#ref-zwicker-asa)[4](#ref-zwicker-dega)

| 年份 | 代表节点 | 研究史中的意义 |
| --- | --- | --- |
| 1952／1956 | 博士研究／大学任教资格 | 用听觉可察觉性研究通信与信息接收 |
| 1957 | 临界带与响度总和合作论文 | 将频谱分布与响度匹配联系起来 |
| 1961 | 可听频率范围的临界带划分 | 提供经典频率分组与坐标框架 |
| 1964 | 报告听觉“负后像” | 后来称为Zwicker音的听觉后效 |
| 1967 | 到慕尼黑主持电声学研究 | 形成持续的心理声学研究与教学环境 |
| 1980 | 与Terhardt发表解析表达式 | 使临界带相关坐标便于计算机使用 |
| 1991 | 响度计算程序论文发表 | 把既有计算方法转为可执行程序；发表于身后 |

这些节点的来源分别是机构回顾和原始论文。[1](#ref-zwicker-fastl2024)[2](#ref-zwicker-tumhistory)[5](#ref-zwicker-band1957)[6](#ref-zwicker-bark1961)[7](#ref-zwicker-analytic1980)[11](#ref-zwicker-program1991)[14](#ref-zwicker-after1964)

## 从实验现象到可检验的模型

Zwicker相关研究的一条方法主线，是先精确规定外部刺激，再规定听者要完成的任务，最后检验模型能否解释行为结果。声音可以用声压级、频率、带宽、持续时间和调制描述；听者的回答则可能是检出、等响匹配、大小估计或品质评分。它们需要不同实验程序，不能因为都涉及“听声音”就交换使用。[5](#ref-zwicker-band1957)[10](#ref-zwicker-quality2005)

例如，研究掩蔽时可以问“目标音是否被听见”；研究响度时，可以让听者把比较声音调到与标准声音同样响；研究声品质时，则要规定“尖锐”“粗糙”或“愉悦”的评价维度。目标音能被检出，并不能单独给出整个复合声的响度；两个声音同样响，也不说明它们具有同样音色或同样烦扰程度。

模型中的中间量也应按其功能理解。激励分布、特定响度轮廓和时间加权有助于计算与解释，但如果模型主要由行为实验约束，就不能仅凭框图把每一步指定为某个神经核团的真实运算。生理证据可以提供约束，仍需独立检验行为预测和实现机制。[9](#ref-zwicker-scharf1965)[10](#ref-zwicker-quality2005)

这种研究方式与[信号检测论](../signal-detection-theory/)可以互相补充：检出实验需要区分敏感性与回答准则，等响匹配需要考察比较策略和重复性，评分实验需要控制任务措辞与参照。模型给出的数值，只有与相应任务、刺激和听者条件相匹配，才有可解释的意义。

## 临界带：相同总能量为何可能不同响

### 1957年的问题与操作

1957年论文研究两类刺激：改变若干纯音分量之间的间隔，以及改变固定总声压级噪声的带宽。关键现象是，频率分布在较小范围内扩展时，响度变化不大；扩展超过某个范围后，响度增加。这个范围随中心频率而变，成为用响度总和考察临界带的重要证据。[5](#ref-zwicker-band1957)

原文使用耳机向双耳呈现标准声和比较声，听者调整比较声使其等响。信号交替呈现，每个约1秒，相邻信号之间约有0.5秒静音；调整时要求从偏高和偏低两侧逐步夹逼等响点。这里的输出是等响判断，不是仪器直接读取“大脑中的响度”。这些细节也提醒读者：呈现时序、比较方法和校准都会进入结果解释。[5](#ref-zwicker-band1957)

物理上，固定总能量的噪声扩宽后，每单位频率所分配的能量会降低。如果响度仍增加，就说明知觉不能只由总声压平方的和决定。在经典响度模型中，能量分散到多个听觉频率区域后，各区域经过非线性转换，再形成总体贡献。这是一种对现象的建模解释；具体带宽与响度增幅需要在相应条件下测量。[5](#ref-zwicker-band1957)[9](#ref-zwicker-scharf1965)

### 一个必须控制的变量

“把噪声变宽”至少有两种不同做法：固定总声压级，或者固定带内功率谱密度。后一做法会同时增加总能量，不能用来单独证明频谱分散导致的响度总和。对于理想平坦带通噪声，谱级与总级的声学算术为：

$$
L_{\mathrm{total}}=L_{\mathrm{PSD}}+10\log_{10}\!\left(\frac{B}{1\,\mathrm{Hz}}\right).
$$

这里$B$为噪声带宽；$L_{\mathrm{total}}$以$p_0^2$为参考，$L_{\mathrm{PSD}}$以$p_0^2/\mathrm{Hz}$为参考，$p_0=20\,\mu\mathrm{Pa}$。该式只描述声压功率的积分，不计算响度。假设总级都是60 dB SPL，100 Hz带宽的谱级为40 dB，1000 Hz带宽则为30 dB；若两者谱级都保持40 dB，总级便从60变为70 dB SPL。

<figure class="encyclopedia-figure" id="fig-zwicker-controls">
  <a href="/n3-hearingpedia/figures/eberhard-zwicker/bandwidth-controls.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/eberhard-zwicker/bandwidth-controls.svg" alt="固定总声压级与固定谱级两种带宽扩展控制：前者谱级降低，后者总级增加" width="1890" height="766" loading="lazy" /></a>
  <figcaption><strong>图1｜扩宽带宽时，究竟固定了什么？</strong>中心频率1500 Hz，理想矩形频带宽度分别为100与1000 Hz。左图固定总级，右图固定谱级。本站原创声学算例，非1957年实测图；响度现象及匹配方法见<a href="#ref-zwicker-band1957">5</a>。<a href="/n3-hearingpedia/figures/eberhard-zwicker/bandwidth-controls.png">PNG</a></figcaption>
</figure>

实际实验还应保持中心频率、呈现时长、耳别与声场条件可比，检查带外泄漏、频谱起伏、滤波器边缘和起止瞬态。应报告各听者的重复结果，而非只给一条看似没有误差的曲线。接近可听阈、不同呈现级和异常听觉条件，都可能改变经典规律的表现；“超过临界带就一定更响”不适合作为没有条件的判断。

## Bark尺度、临界带宽与ERB

### 两个函数回答不同问题

1961年的频率分组与1980年Zwicker—Terhardt解析表达式，让临界带框架更容易进入声音分析。经典划分常用24个临界带描述到约15.5 kHz的频率范围；这是一套经过概括的坐标与带宽描述，不是耳蜗里24个互不重叠、边界固定的解剖格子。[6](#ref-zwicker-bark1961)[8](#ref-zwicker-volk2015)

令$f_{\mathrm{Hz}}=f/(1\,\mathrm{Hz})$，经典解析近似可写为：

$$
\begin{aligned}
\frac{z(f)}{\mathrm{Bark}}={}&13\arctan(0.00076f_{\mathrm{Hz}})\\
&+3.5\arctan\!\left[\left(\frac{f_{\mathrm{Hz}}}{7500}\right)^2\right],
\end{aligned}
$$

$$
\frac{\Delta f(f)}{\mathrm{Hz}}=25+75\left[1+1.4\left(\frac{f_{\mathrm{Hz}}}{1000}\right)^2\right]^{0.69}.
$$

第一式给出频率在Bark坐标上的位置，反正切使用弧度；第二式给出经典临界带宽近似。两式分别回答“位于什么坐标”和“相关频带有多宽”，不能把$z$直接当成Hz带宽。公式的原始出处为1980年论文，本页表达式也与Völk的2015年原文式1、式9交叉核对。[7](#ref-zwicker-analytic1980)[8](#ref-zwicker-volk2015)

| 频率 | 解析Bark坐标 | 解析临界带宽 | 解释 |
| --- | --- | --- | --- |
| 1000 Hz | 约8.51 Bark | 约162 Hz | 坐标数值与带宽数值具有不同单位 |
| 4000 Hz | 约17.26 Bark | 约685 Hz | 高频处一个经典临界带对应更宽的Hz范围 |

表中数值直接代入上述公式，适合学习尺度换算，不是对某位听者测得的精确分辨能力。两个听者在同一中心频率处可能具有不同的频率选择性，听力损失和呈现条件也可能改变结果。[8](#ref-zwicker-volk2015)[17](#ref-zwicker-florentine1979)

<figure class="encyclopedia-figure" id="fig-zwicker-bark">
  <a href="/n3-hearingpedia/figures/eberhard-zwicker/bark-bandwidth.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/eberhard-zwicker/bark-bandwidth.svg" alt="100至15500 Hz范围的Bark坐标曲线与经典临界带宽曲线，标出1000和4000 Hz算例" width="1889" height="736" loading="lazy" /></a>
  <figcaption><strong>图2｜Bark位置与临界带宽不是同一量。</strong>本站依公开公式生成，横轴为对数频率。曲线范围为100—15500 Hz，不代表该范围内每一点均有个体测量，也不展示更新公式的实测优劣。<a href="#ref-zwicker-analytic1980">7</a><a href="#ref-zwicker-volk2015">8</a> <a href="/n3-hearingpedia/figures/eberhard-zwicker/bark-bandwidth.png">PNG</a></figcaption>
</figure>

### 为什么不能把Bark、ERB和FFT频点混称

临界带可从不同心理声学任务估计；ERB是等效矩形带宽，用与原滤波器等高、等面积矩形的宽度描述听觉滤波器。ERB-rate则是另一种频率坐标。经典临界带宽与ERB具有不同定义、估计方法和经验近似，不能只因为都带有“听觉频带”的含义，就逐项互换。[8](#ref-zwicker-volk2015)

FFT频点间隔则由采样率与分析长度决定。把FFT结果映射到Bark轴，有助于以听觉相关坐标展示频谱；这一步本身不会把FFT变成真实耳蜗，也不能证明两个频率分量是否被个体分辨。纯音频率差别阈、两个同时声音的可分离性、噪声掩蔽下的选择性，仍是不同任务，详见[频率分辨率](../frequency-resolution/)与[听觉滤波器](../auditory-filter/)。

解析表达式还有范围限制。Völk指出，经典公式来自有限频率表；很低频处，把近似带宽机械地对称放在中心频率两边，可能跨入负频率，高频外推也会偏离原表的坐标趋势。工程应用应记录使用哪套公式、频率范围及边界处理，而不能把“用了Bark”当作充分的听觉有效性证明。[8](#ref-zwicker-volk2015)

## 响度模型与特定响度

### 从物理频谱到知觉轮廓

响度描述声音听起来有多响。声压级描述物理量，响度级以phon表示与参考纯音的等响关系，响度常以sone表示。三个量有联系，但不能只给一个整体dB值，就确定任意声音的sone数。频谱、声场、呈现方式和持续时间都可能进入预测条件。[10](#ref-zwicker-quality2005)[12](#ref-zwicker-iso1)

Zwicker与Bertram Scharf在1965年发表响度总和模型。其重要表示方式，是把沿听觉频率坐标分布的局部贡献写成特定响度，再汇总为总体响度。后续模型和标准继承并发展了这一思路；1965年的框架、1991年的程序和2017年的标准应按各自年代与具体版本理解。[9](#ref-zwicker-scharf1965)[10](#ref-zwicker-quality2005)[11](#ref-zwicker-program1991)

特定响度$N'(z)$的单位是sone/Bark。对于经典0—24 Bark框架，其面积给出总体响度：

$$
N=\int_{0\,\mathrm{Bark}}^{24\,\mathrm{Bark}}N'(z)\,\mathrm{d}z.
$$

这一表达强调两件事：同一谱区的局部贡献经历了模型中的转换，最后的面积才是总体量；某处特定响度峰值较高，不保证总面积更大。它也使“声音的响度分布在哪里”可以与“声音总共多响”分开讨论。[10](#ref-zwicker-quality2005)

### 面积相同，轮廓仍可不同

设教学轮廓A在7—9 Bark之间恒为1 sone/Bark，其他位置为零；轮廓B在4—12 Bark之间恒为0.25 sone/Bark，其他位置为零。则：

$$
\begin{aligned}
N_A&=(1\,\mathrm{sone/Bark})(2\,\mathrm{Bark})=2\,\mathrm{sone},\\
N_B&=(0.25\,\mathrm{sone/Bark})(8\,\mathrm{Bark})=2\,\mathrm{sone}.
\end{aligned}
$$

<figure class="encyclopedia-figure" id="fig-zwicker-specific">
  <a href="/n3-hearingpedia/figures/eberhard-zwicker/specific-loudness.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/eberhard-zwicker/specific-loudness.svg" alt="两个矩形特定响度轮廓：高而窄与低而宽，面积都为2 sone" width="1890" height="719" loading="lazy" /></a>
  <figcaption><strong>图3｜总响度是面积，特定响度是分布。</strong>两条轮廓人为指定，仅演示积分；未从真实噪声、声压谱或标准算法计算，也不表示相同声压级或相同音色。面积表示思想见<a href="#ref-zwicker-quality2005">10</a>。<a href="/n3-hearingpedia/figures/eberhard-zwicker/specific-loudness.png">PNG</a></figcaption>
</figure>

这并不表示把任意声音扩宽四倍，就能得到上述B轮廓。真实模型需要先由输入谱或时域信号建立频率相关激励，处理阈值、非线性和频谱扩展，再产生特定响度。算例从已经给定的$N'$出发，跳过了这些步骤，不能反过来指定生成某个真实声音所需的声压级。

两个声品质方案如果总响度相近，仍可具有不同的高频贡献、音调成分和时间起伏。保存特定响度轮廓，往往比只保存一个总数更利于发现这种区别。但轮廓也不能独自预测所有音色、语言可懂度或情绪评价；后者需要另外的任务与证据。[10](#ref-zwicker-quality2005)

## 掩蔽、非线性与时变声音

[掩蔽](../masking/)描述一种声音使另一种声音的可听性下降。经典响度建模利用掩蔽相关的频率分布来约束激励与局部贡献，却不能把每条掩蔽阈曲线直接解释为听者对整个掩蔽声的响度评分。一个量问目标能否检出，另一个量问整体听起来多响，两者在任务上有明确区别。[9](#ref-zwicker-scharf1965)[10](#ref-zwicker-quality2005)

频谱总和之外，声音的时间结构也很重要。相同平均能量可以来自连续声、间歇声或快速变化的声；仅用平均谱计算，会丢掉起止、间隔和包络变化。Fastl讨论的动态响度模型包括包络提取、后掩蔽相关处理和时间积分等功能，说明“先把时间平均掉”不总能替代时变处理。[10](#ref-zwicker-quality2005)

1991年的程序论文直接指出，它计算稳态声音的响度；对强烈时变声音，需要另外的非线性时间加权。ISO 532-1:2017则分别规定稳态与时变方法。将历史程序用于短促冲击声时，应先核对适用方法，而不是因为程序名称包含Zwicker就默认能够处理所有声音。[11](#ref-zwicker-program1991)[12](#ref-zwicker-iso1)

时变计算还会产生不同摘要：最大响度、某一时段的响度轨迹和百分位响度描述不同信息。MathWorks文档中的$N_5$表示只有约5%的时间超过的响度，不是把响度从小到大排序后取第5百分位。报告一个数值时，应同时说明统计定义、分析区间和是否包括静音，防止不同软件输出被错误比较。[19](#ref-zwicker-mathworks)

## 从响度走向声品质

慕尼黑的研究传统并不只追求一个总体响度数值。声音可能同样响，却听起来更尖锐、更粗糙或更有起伏。这些属性分别涉及频谱分布与调制结构，因此在产品声、音乐和噪声研究中有不同作用。Fastl的声品质章节也讨论了声音意义、品牌信息与视觉线索对评价的影响。[2](#ref-zwicker-tumhistory)[10](#ref-zwicker-quality2005)

| 维度 | 主要描述的问题 | 解释时需保留的条件 |
| --- | --- | --- |
| 响度 | 整体听起来有多响 | 输入校准、频谱、时变处理及听者条件 |
| 尖锐度 | 声音是否具有较强的高频尖锐感 | 特定响度的高频分布与所用加权模型 |
| 粗糙度 | 较快调制造成的粗糙感 | 调制速率、深度和频谱位置 |
| 起伏强度 | 较慢变化造成的明显起伏感 | 时间包络、调制结构与评价任务 |
| 烦扰或愉悦 | 声音在具体情境中的综合评价 | 意义、使用场景、预期及个体差异 |

表中是维度与条件的概括，不能视为一套通用打分公式。某些组合指标可以预测特定实验中的烦扰程度，但验证应与声音集合和情境一致；减少某个声学指标，也可能改变提示功能或使用者对产品的判断。[10](#ref-zwicker-quality2005)

例如，比较两种设备声时，可以先保留实际运行条件和校准声级，记录总体响度、轮廓与调制，再让听者完成明确定义的评价。如果研究“哪个方案更悦耳”，不应把响度归一化后的偏好结论直接用于原声级方案；如果研究“哪个更尖锐”，应避免把音量差当作唯一线索。不同问题允许不同控制，但控制必须跟着结论公开。

这些属性还应保留合作史。Terhardt对粗糙度与起伏强度的研究、Fastl对模型和应用的延续，都属于这一传统的重要部分。人物词条可以解释Zwicker的推动作用，而不把后来声品质工程中的每个指标、实现和应用归于他一个人。[2](#ref-zwicker-tumhistory)

## Zwicker音：外部声音停止后的听觉后效

### 1964年的“负后像”

1964年，Zwicker报告一种听觉后效：在呈现含频谱凹口的噪声后，部分听者在噪声停止时听到逐渐衰减的音调，其音高对应凹口内的频率。论文称之为听觉“负后像”，后来常称Zwicker tone。原始摘要描述的是特定声级、凹口和较长刺激时长条件，不宜把其数值写成所有人都适用的演示配方。[14](#ref-zwicker-after1964)

这里的“凹口”表示噪声中某个频率范围的功率被压低，不是给外部噪声添加一个纯音。刺激终止后的音调是知觉报告，不能在外部信号的频谱上画一个新峰，再把它称为测得的后效。麦克风记录的声波与听者报告的声音，必须分别标记。

<figure class="encyclopedia-figure" id="fig-zwicker-afterimage">
  <a href="/n3-hearingpedia/figures/eberhard-zwicker/zwicker-afterimage.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/eberhard-zwicker/zwicker-afterimage.svg" alt="上方为理想凹口噪声功率谱，下方分别标出外部刺激停止与部分听者的短暂音调报告" width="1729" height="1067" loading="lazy" /></a>
  <figcaption><strong>图4｜缺少一段频率能量，停止后却可报告音调。</strong>凹口2—3 kHz为本站任意选定的示意参数，下方为定性先后顺序；虚线表示主观报告，不是外部波形或神经记录。现象见<a href="#ref-zwicker-after1964">14</a>，个体与条件差异见<a href="#ref-zwicker-review2025">16</a>。<a href="/n3-hearingpedia/figures/eberhard-zwicker/zwicker-afterimage.png">PNG</a></figcaption>
</figure>

### 与皮层研究和耳鸣的联系

Noreña与Eggermont的2003年研究，在氯胺酮麻醉猫的初级听觉皮层记录白噪声与不同凹口噪声条件下的多单位活动，并考察刺激停止后的放电及相关变化。作者提出可能的神经对应物；动物记录不是动物对主观音调的口头报告，也不能凭一个活动变化就确定人类错觉的完整产生机制。[15](#ref-zwicker-norena2003)

2025年的范围综述汇总了人类Zwicker音研究，指出诱发参数、报告方式和个体差异会影响现象是否被报告。它与耳鸣都涉及没有相应外部声源的声音体验，因此可以帮助研究错觉与听觉适应，但短暂实验后效和持续临床耳鸣之间的因果联系仍需检验。[16](#ref-zwicker-review2025)

因此，听到Zwicker音不能直接诊断[耳鸣](../tinnitus/)，没有听到也不能排除耳鸣；不能把该刺激当作已确立的治疗方法。研究若要比较两者，应保留临床状况、听力信息、刺激条件及回答准则。物理上削弱某一频带的刺激，也不等于证实该听者的耳蜗或突触已经发生结构性损伤。

这一后效适合体现心理声学的研究价值：外部刺激完全可描述，知觉却有持续性和情境依赖。研究者可以控制诱发声的谱形和先后顺序，再检查报告与神经指标的联系。模型解释需要同时通过条件变化和对照检验；只让听者听一次噪声、随后询问“是否有音调”，不足以排除提示和回答策略的影响。

## 教材、标准与可复现计算

### 模型怎样进入计算机

1991年的论文提供按DIN 45631与当时ISO 532B计算响度的程序。一个有历史意味的细节是：为适应日本常用的NEC PC-9801，作者调整了原本面向IBM兼容机的BASIC程序。可复现并不只意味着有公式，还包括输入格式、计算步骤和平台的一致性；论文也说明该版本与既有标准程序的结果对应。[11](#ref-zwicker-program1991)

这篇合作论文发表于Zwicker去世之后，收稿时间为1990年9月。其输入、稳态范围与程序结构属于当时的方法，不能直接标记成2017年的标准实现。标准继承理论时会补充方法和验证要求，历史上的同名算法并不保证数值完全相同。[11](#ref-zwicker-program1991)[12](#ref-zwicker-iso1)

《Psychoacoustics: Facts and Models》将听觉实验与模型组织为教材体系。出版社记录的2007年第三版作者为Hugo Fastl与Eberhard Zwicker，目录覆盖掩蔽、临界带、响度、音高、调制、粗糙度、双耳听觉和应用等主题。该版体现了研究传统的延续，不能解读为Zwicker在2007年继续亲自完成新研究。[18](#ref-psychoacoustics-fastl-2007)

### 使用模型时记录什么

ISO 532-1:2017以Zwicker方法估计规定听觉条件下的稳态和时变响度；ISO 532-2:2017规定Moore—Glasberg方法的稳态计算，包含单耳与双耳条件。两者并列为不同方法，不能通过改换单位就变成同一算法。这里引用2017版的范围说明，未宣称通读付费标准或验证完整实现。[12](#ref-zwicker-iso1)[13](#ref-zwicker-iso2)

| 记录项 | 为什么影响可复现性 |
| --- | --- |
| 输入单位与校准 | 数字文件的满幅归一化不自动等于真实Pa或dB SPL |
| 自由场、扩散场或耳机条件 | 声场与传输修正要与所用方法相匹配 |
| 稳态／时变与分析区间 | 平均谱、轨迹、峰值和百分位量回答不同问题 |
| 算法与版本 | 历史ISO 532B、2017版方法和软件实现不能只写同一简称 |
| 耳别与输出单位 | 单耳、双耳、每声道输出与sone、phon需分别说明 |
| 对照材料 | 用已知输入与参考输出检查实现，实际评价仍需要听觉任务验证 |

MathWorks的公开文档展示了校准因子、声场、时变选项和特定响度输出，可作为理解接口的例子；本页没有运行该函数或完成标准一致性测试。一个经过标准化的模型仍需正确输入，未经校准的录音只允许在保留处理条件的前提下解释，不能直接报告现实环境的绝对响度。[19](#ref-zwicker-mathworks)

## 贡献边界与关联阅读

Zwicker的长久影响，在于用有条件的行为规律建立可计算的声音描述。Bark尺度帮助组织频率信息，特定响度让总体感觉具有分布表示，时变模型关注刺激历程，听觉后效则提出适应与内部活动的问题。这些工具使心理声学能够进入工程，仍不替代个体测听或真实任务中的感知验证。

Florentine与Zwicker在1979年的合作研究已经指出，将响度模型用于噪声性听力损失观察者时，需要考虑重振和频率选择性降低并修改参数。因而，健康听觉条件下的标准输出不能直接充当听力受损者的个体感受，更不能由一个sone值推出助听器增益或人工耳蜗电流设置。[17](#ref-zwicker-florentine1979)

响度评价还不等于噪声健康风险评价。ISO 532-1与532-2的公开范围均把声音有害效应评价排除在外；模型量能说明规定条件下的响度预测，不能替代暴露时间、剂量及专门的风险评估。这一边界来自方法本身的目标，并非说响度与声音评价无关。[12](#ref-zwicker-iso1)[13](#ref-zwicker-iso2)

阅读人物之间的联系时，可从[Harvey Fletcher](../harvey-fletcher/)的听觉测量与语音通信出发，经[心理声学](../psychoacoustics/)、[响度](../loudness/)和[听觉滤波器](../auditory-filter/)理解Zwicker的方法；再到[Manfred R. Schroeder](../manfred-r-schroeder/)和[James L. Flanagan](../james-l-flanagan/)查看感知约束如何进入声音处理与通信。[Albert Bregman](../albert-bregman/)的知觉组织和[Bertrand Delgutte](../bertrand-delgutte/)的神经编码研究，则提出另外的证据层次，不应仅由一套响度模型替代。

历史照片可在[Fastl的2024年百年纪念文章](https://www.dega-akustik.de/fileadmin/dega-akustik.de/publikationen/akustik-journal/24-01/akustik_journal_2024_01_online_artikel1.pdf)及[TUM的机构历史回顾](https://mediatum.ub.tum.de/doc/1138439/98963.pdf)中查看，包含桌前肖像、实验工作与研究环境。本页选用百年纪念文章的桌前照片，并在图注中保留来源与原署名。[1](#ref-zwicker-fastl2024)[2](#ref-zwicker-tumhistory)

本词条为AI辅助本地深度稿，专业审核待完成。文献访问层级、公式来源、图示参数和图片权利记录保存在研究台账中；教学算例与原始实验结果分别标明。
