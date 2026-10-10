---
title: "曼弗雷德·施罗德"
english: "Manfred Robert Schroeder"
slug: "manfred-r-schroeder"
summary: "从混响测量、音乐厅与数论扩散体，到CELP语音编码和施罗德相位：理解曼弗雷德·施罗德如何连接声学、数学与听觉实验。"
categories: ["acoustics", "psychoacoustics", "speech", "binaural"]
tags: ["研究人物", "科学史", "房间声学", "施罗德相位", "语音编码", "数论"]
aliases: ["Manfred Schroeder","Manfred Schröder","曼弗雷德·施罗德","曼弗雷德·罗伯特·施罗德","施罗德","Manfred R. Schroeder"]
level: ["undergraduate", "graduate"]
status: draft
depth: in-depth
last_updated: "2026-10-10"
literature_checked_at: "2026-10-10"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
knowledge_area: "sound"
kind: "person"
core_work: {"year":1965,"title":"混响时间测量的新方法","reference":"room-acoustics-schroeder"}
key_facts: [{"label":"生卒","value":"1926—2009"},{"label":"研究领域","value":"声学、语音信号处理、心理声学与应用数学"},{"label":"代表方法","value":"混响逆向积分、施罗德相位、二次剩余扩散体"},{"label":"合作贡献","value":"与Bishnu S. Atal提出CELP语音编码"}]
references: ["schroeder-nae","schroeder-oral","schroeder-frequency-1996","room-acoustics-lecture","room-acoustics-schroeder","room-acoustics-rew-rt","schroeder-phase-1970","schroeder-smith-1986","schroeder-kohlrausch-1995","schroeder-summers-1998","schroeder-wojtczak-2009","schroeder-green-2013","schroeder-halls-1974","schroeder-diffusers-1979","schroeder-celp-1985","schroeder-computer-speech","schroeder-number-theory","schroeder-zkm","schroeder-portrait","schroeder-fractals-book-1991"]
batch: 4
order: 112
---

**曼弗雷德·施罗德**（Manfred R. Schroeder，全名 Manfred Robert Schroeder，1926—2009）是德国声学家、物理学家与应用数学研究者，长期在贝尔实验室和哥廷根大学工作。他的研究连接[房间声学](../room-acoustics/)、语音信号处理和[心理声学](../psychoacoustics/)：既研究声音在空间中怎样传播，也研究声音怎样有效表示，以及听者怎样利用这些信息。[1](#ref-schroeder-nae)

听觉研究中多个熟悉的名称与他有关，包括施罗德频率、混响的施罗德逆向积分、施罗德相位和基于数论的声扩散体。他还与 Bishnu S. Atal 合作提出码激励线性预测（CELP），成为低码率语音编码的重要研究起点。[3](#ref-schroeder-frequency-1996)[5](#ref-room-acoustics-schroeder)[7](#ref-schroeder-phase-1970)[14](#ref-schroeder-diffusers-1979)[15](#ref-schroeder-celp-1985)

理解这些工作，可以抓住一个共同问题：**怎样选择数学表示，使声学问题能够测量、比较和验证？** 衰减积分把起伏的响应转为能量曲线；相位设计在固定幅度谱时改变波形；编码则用有限参数和索引描述可重建的语音。这些操作的有效性仍要由实际测量和听觉任务检验。

<figure class="person-photo-figure person-portrait">
<a href="/n3-hearingpedia/people/manfred-r-schroeder/portrait.jpg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/people/manfred-r-schroeder/portrait.jpg" alt="1993年哥廷根的Manfred Schroeder彩色肖像，戴眼镜，穿深色外套和花纹领带" width="280" height="350" loading="lazy" /></a>
<figcaption>图1．Manfred Schroeder，1993年，哥廷根。文件署名：GFHund / Gerhard Hund；文件说明提及Friedrich Hund遗存照片。<a href="https://commons.wikimedia.org/wiki/File:Schr%C3%B6der,Manfred_1993_G%C3%B6ttingen.jpg" target="_blank" rel="noopener">Wikimedia Commons来源页</a>，采用<a href="https://creativecommons.org/licenses/by/3.0/" target="_blank" rel="noopener">CC BY 3.0</a>许可。本站保留原文件，未再修改，网页显示缩小。<a href="#ref-schroeder-portrait">19</a></figcaption>
</figure>

## 生平：哥廷根与贝尔实验室之间

### 从物理训练进入声学问题

Schroeder 在哥廷根大学接受数学与物理训练，师从 Erwin Meyer，1954年取得博士学位，同年进入美国贝尔实验室。他后来负责声学及语音研究相关部门；1969年回到哥廷根担任教授，同时保持与贝尔实验室的联系。这种横跨大学和工业研究机构的经历，为他的房间声学、通信与数学研究提供了共同环境。[1](#ref-schroeder-nae)[2](#ref-schroeder-oral)

他的研究对象并不局限于单一尺度：房间中的波动、语音中的短时结构、听觉实验中的谐波关系，都可以成为数学与实验相遇的地方。人物页中的“研究领域”因此需要理解为相互连接的问题，而不是将他归入某一种听力辅助设备的发明史。

### 合作比姓名标签更能说明工作

| 研究方向 | 本文涉及的合作或成果 | 需要辨认的贡献 |
| --- | --- | --- |
| 房间测量 | 1965年混响测量方法 | 用脉冲响应的逆向积分估计能量衰减 |
| 音乐厅评价 | 与D. Gottlob、K. F. Siebrasse的1974年研究 | 将听者的配对偏好与声学参数联系 |
| 相位与掩蔽 | 与B. K. Smith、U. K. Sieben、A. Kohlrausch的1986年论文 | 连接外部相位、内耳色散解释与行为阈值 |
| 语音编码 | 与Bishnu S. Atal的1985年CELP论文 | 通过合成反馈搜索有效激励 |
| 计算图形 | 与Suzanne（Sue）Hanauer的合作 | 把计算与视觉创作联系起来 |

表中的论文与合作分别有对应来源。它们说明为什么“施罗德相位”“CELP”“数论扩散体”不能被写成一次发明的不同名称：各自面对的约束、验证任务和合作者都不同。[8](#ref-schroeder-smith-1986)[13](#ref-schroeder-halls-1974)[15](#ref-schroeder-celp-1985)[18](#ref-schroeder-zkm)

## 施罗德频率：何时需要逐个讨论房间模态

### 模态重叠是一种过渡

房间里的低频响应往往出现明显峰谷。某些共振的频率、宽度和空间分布，需要结合房间形状、边界与声源和接收点位置来解释。频率升高后，可用模态数量增多，相邻模态也可能重叠，按频带平均的统计描述逐渐更有用。**施罗德频率**用于粗略指示从稀疏、可辨认的模态向较充分重叠的模态过渡的区域。[3](#ref-schroeder-frequency-1996)[4](#ref-room-acoustics-lecture)

它不是人的听阈，也不是耳蜗频率分辨率；它描述的是空间声场。房间响应的峰谷可以改变听者收到的声音，却不能直接当成[听觉滤波器](../auditory-filter/)的带宽。测量前者需要改变位置或检查房间响应，测量后者需要受控的听觉任务。

### 从参数关系理解，不把估计值当作开关

粗略估计具有 $f_s\propto\sqrt{T/V}$ 的形式，其中 $f_s$ 是过渡频率，$T$ 是混响时间，$V$ 是房间体积。在以秒和立方米表示参数时，常用估计的系数约为 $2\times10^3$；本文核对的大学讲义按其模态重叠约定写为约2100。[4](#ref-room-acoustics-lecture)

由此可理解两个趋势：同样体积下，衰减较慢、共振较窄的房间，需到较高频率才出现充分重叠；同样混响时间下，较大的房间在较低频率就已有较高模态密度。作为本文教学计算，取 $T=0.5$ s、$V=100$ m³、系数2100，得到约148 Hz。这个数值只是讨论频段的起点，不能证明148 Hz以上每个位置都已经形成理想扩散场。

实际分析还需检查频带、阻尼是否相近，以及几何和吸声条件。小房间中的驻波、早期反射和强烈的空间不均匀，不会在跨过一个估计频率后突然消失。人物贡献在于提出可用的模态重叠尺度，而不是替代所有房间声学判断。

## 混响测量：把脉冲响应转为衰减曲线

### 为什么从后向前积分

脉冲响应 $h(t)$ 记录一个系统受到短时输入后的响应。直接观察房间响应时，反射密集、正负振荡和随机起伏，会使衰减趋势不容易读出。Schroeder 在1965年提出的方法，利用一次脉冲响应构造与噪声激励平均衰减有关的能量曲线，减少反复声源开关测试所带来的工作。[5](#ref-room-acoustics-schroeder)

教学上可写为：

$$
E(t)=\int_t^{\infty}h^2(\tau)\,\mathrm{d}\tau,\qquad L_E(t)=10\log_{10}\frac{E(t)}{E(0)}.
$$

$E(t)$ 表示从时刻 $t$ 往后的剩余响应能量；归一化后 $L_E(t)$ 以dB表示。离散实现把平方采样值从末尾向前累加，积分中的采样间隔在归一化比值里消去。这里是能量比，所以使用 $10\log_{10}$，不能直接套用振幅比的系数20。[6](#ref-room-acoustics-rew-rt)

### T20名称中的“20”不是最终下降量

测量者可以对衰减曲线的指定范围拟合直线。T20使用相对初始能量约−5至−25 dB的20 dB范围，再把拟合斜率外推到下降60 dB所需的时间；它不要求曲线实际测到−60 dB。如果斜率为 $b<0$，单位dB/s，则 $T_{20}=-60/b$，单位为秒。[6](#ref-room-acoustics-rew-rt)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/manfred-r-schroeder/energy-decay.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/manfred-r-schroeder/energy-decay.svg" alt="合成指数衰减响应及其逆向能量积分曲线，标出负5至负25分贝的T20拟合范围" width="1280" height="650" loading="lazy" /></a>
<figcaption>图2．从响应到能量衰减。（a）随机噪声乘以指数衰减包络的合成响应；（b）平方后逆向累加的归一化能量曲线，着色区为−5至−25 dB的拟合范围。采样率48 kHz、时长2 s、随机种子1926，设定衰减参数0.60 s；两面板分别使用振幅与能量dB坐标。原创教学计算，非房间实测，也未模拟真实频带或仪器噪声。原理依据施罗德方法与官方方法说明。<a href="#ref-room-acoustics-schroeder">5</a><a href="#ref-room-acoustics-rew-rt">6</a></figcaption>
</figure>

### 噪声底、截断与非直线衰减

有限录音不能真正积分到无穷远。若把噪声尾部一起累计，衰减曲线的后段会被抬高；若截断过早，剩余能量又可能被低估。合适的记录长度、信噪比、积分终点和噪声处理，需要与拟合区间共同检查。只输出一个T20数字而不检查曲线，容易掩盖这些问题。[6](#ref-room-acoustics-rew-rt)

还应报告声源与传声器位置、使用的频带和分析方法。多个空间或不同衰减阶段可能使曲线出现弯折，此时不同拟合范围给出的时间并不相同。用于讨论[言语可懂度](../speech-intelligibility/)时，混响时间也不能单独代表早期反射、背景噪声和目标语音到达听者的全部条件。

## 施罗德相位：幅度谱相同，波形可以不同

### 低峰值因子是一个信号设计问题

Schroeder 的1970年论文研究低峰值因子的信号合成。峰值因子是峰值振幅与均方根振幅（RMS）的比值；在相同RMS下，较小峰值有助于减少测量或传输系统受到的瞬时幅度限制。改变多频信号各分量的相位，是控制峰值的一条路线。[7](#ref-schroeder-phase-1970)

多谐波合成可写为：

$$
x_C(t)=\sqrt{\frac{2}{N}}\sum_{n=1}^{N}\cos\left(2\pi n f_0t+\phi_n\right),\qquad \phi_n=C\frac{\pi n(n-1)}{N}.
$$

$f_0$ 为基频，$n$ 为谐波序号，$N$ 为分量数，$\phi_n$ 以弧度表示；$C=+1$和$C=-1$分别给出本文约定的正、负施罗德相位，$C=0$为余弦同相。这个二次相位形式见后来的语音掩蔽研究方法。前面的幅度系数是本文为单位RMS加入的归一化，适用于这些等幅分量、完整周期和足够采样的教学信号。[12](#ref-schroeder-green-2013)

### 同谱不等于相同的时间结构

固定各谐波幅度而只改变相位，保留的是幅度谱及按完整周期计算的平均能量。多个分量在什么时候相加、什么时候相消仍可改变，所以波形、峰值因子和局部起伏可以不同。这里“同谱”特指幅度谱相同，不表示包含相位的完整复频谱相同。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/manfred-r-schroeder/harmonic-phase.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/manfred-r-schroeder/harmonic-phase.svg" alt="零相位、正施罗德相位和负施罗德相位在共同振幅尺度下的波形，以及三者相同的谐波幅度谱" width="1280" height="850" loading="lazy" /></a>
<figcaption>图3．只改变相位的三个等幅谐波复合声。（a）余弦同相；（b）正施罗德相位；（c）负施罗德相位；（d）三者相同的单边谐波幅度，重叠曲线用不同点形标记。基频100 Hz、20个谐波、采样率48 kHz；波形展示一个10 ms周期，共用振幅尺度，三个信号RMS均为1（任意单位）。图内CF为采样峰值/RMS。原创解析合成，不是听觉滤波后响应或阈值数据；未加入播放用淡入淡出。<a href="#ref-schroeder-phase-1970">7</a><a href="#ref-schroeder-green-2013">12</a></figcaption>
</figure>

正、负二次相位还提供了有用的配对：在本文余弦约定中，一者可由另一者作周期性的时间反转得到。两者的整体RMS和峰值因子相同，却不一定在经过具有特定相位响应的系统后仍保持相同输出起伏。相位正负标签应连同合成公式说明；不同论文的正弦、余弦及时间原点约定，需要先统一再比较。

## 心理声学：用相位检查听觉处理

### 外部波形与滤波后的内部表征

Schroeder 相位信号后来成为[掩蔽](../masking/)实验的重要工具。研究者能控制谐波组成和幅度谱，同时改变相位关系；如果目标音检测阈值随之改变，就需要解释听觉系统为何没有把这些信号当成完全等价的刺激。1986年Smith及合作者（包括Schroeder）的论文，把这种现象与内耳色散联系起来。[8](#ref-schroeder-smith-1986)

色散在这里指不同频率分量经历不同的相位变化或延迟。刺激进入一个频率选择通道后，输入的相位曲率与通道的相位响应共同决定输出起伏。某些相位条件可形成较深的内部包络谷，短目标可能更容易在谷中被察觉。这里的“内部包络”是模型或功能解释，不是直接从人的基底膜上测得的波形。[8](#ref-schroeder-smith-1986)[9](#ref-schroeder-kohlrausch-1995)

### 短目标与长语音回答不同问题

短目标可以放在掩蔽声一个周期中的不同位置，测量阈值如何随时机变化。这种掩蔽周期图样，比单个平均阈值更能限制候选解释：若模型预测某时刻最有利，却与行为结果不符，就需要重新检查滤波、时间积分或其它环节。[9](#ref-schroeder-kohlrausch-1995)

语音材料则包含跨频带、跨时间的多种线索。Green与Rosen在正常听力听者中研究了谐波复合声掩蔽句子的情况，发现正负相位的效应随声级和实验条件改变；较低声级与较高声级不能合并成一个固定的“相位优势”。因此，纯音目标的结果不能直接换算成日常语音在噪声中的改善幅度。[12](#ref-schroeder-green-2013)

| 实验操纵 | 主要观测 | 可以帮助判断 | 不能单独得出的结论 |
| --- | --- | --- | --- |
| 固定幅度谱，改变相位曲率 | 目标音检测阈值 | 相位与时间结构是否影响掩蔽 | 人能逐一报告所有谐波的初始相位 |
| 改变短目标在周期中的位置 | 掩蔽周期图样 | 时间谷和模型预测是否对应 | 直接测出了人的基底膜运动 |
| 改变掩蔽声级、基频或目标材料 | 阈值、语音识别或接收阈 | 效应适用的刺激与任务范围 | 得到适用于所有环境的改善量 |
| 改变听力状态或使用前向掩蔽 | 人群差异、随条件变化的函数 | 功能解释是否跨条件一致 | 一个指标即可诊断某种细胞损伤 |

表格把不同论文的研究问题放在同一阅读框架中，并非将它们合并为同一协议。[9](#ref-schroeder-kohlrausch-1995)[10](#ref-schroeder-summers-1998)[11](#ref-schroeder-wojtczak-2009)[12](#ref-schroeder-green-2013)

### 听力损失与机制解释的边界

Summers与Leek比较了正常听力及听力受损听者的纯音、语音掩蔽表现。相位效应的人群差异使研究者关注听觉滤波、压缩和利用时间起伏的能力，但这些机制在行为上可能共同作用。[10](#ref-schroeder-summers-1998)

Wojtczak与Oxenham进一步研究同频、异频条件下的前向掩蔽。目标在掩蔽声之后出现，改变了同时掩蔽中可利用的线索；他们也讨论了掩蔽声时长和其它过程的影响。由此不能把一种相位条件下的阈值差，当成跨任务恒定的耳蜗压缩量。[11](#ref-schroeder-wojtczak-2009)

设计此类实验时，应把频率范围、分量数量、RMS、声级校准、目标时机、持续时间和播放边缘处理一起报告。还需区分[时域包络](../temporal-envelope/)、[时域精细结构](../temporal-fine-structure/)与经滤波重新形成的起伏。这些控制使相位刺激成为有约束的探针，而不只是三段“听起来不同”的声音。

## 音乐厅与扩散体：把空间体验变成比较问题

### 在实验室比较不同音乐厅

1974年，Schroeder、Gottlob和Siebrasse发表欧洲音乐厅的比较研究。研究将无混响的管弦乐录音送入厅内，在听者位置用仿真人头记录，再在实验室重建耳边信号，进行快速配对偏好比较。相同音乐输入与可切换的聆听条件，帮助减少音乐演奏和长时听觉记忆造成的混杂。[13](#ref-schroeder-halls-1974)

他们把偏好与几何、混响及双耳相关指标联系起来。这样的关联能提出空间体验的候选线索，但不是随意改变某个参数就必然提高偏好的因果证明。回放链是否保留双耳信息、不同听者是否具有一致偏好，也需要单独检查。读者可结合[空间听觉](../spatial-hearing/)与[双耳听觉](../binaural-hearing/)理解这类评价的目的。

### 二次剩余如何变成深度序列

声扩散体希望改变反射能量的方向分布。Schroeder研究了利用数论安排表面结构的方法：取奇素数 $p$，用 $s_n=n^2\bmod p$ 得到二次剩余序列，再把它映射为不同深度。在理想化、正入射的设计关系中，可写 $d_n=\lambda_0s_n/(2p)$，其中 $\lambda_0$ 是设计波长，$d_n$ 是槽深。[14](#ref-schroeder-diffusers-1979)

深度不同，使声音往返传播的相位不同。二次剩余序列的离散相位和具有有用的数学性质，为把规则结构转成较分散的反射提供设计起点。这不是随意把墙面做凹凸：槽宽、深度、重复周期与设计波长之间存在约束。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/manfred-r-schroeder/quadratic-residue.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/manfred-r-schroeder/quadratic-residue.svg" alt="素数7的二次剩余序列及映射到槽深的条形图，展示数学序列怎样成为扩散体的几何设计起点" width="1280" height="650" loading="lazy" /></a>
<figcaption>图4．从二次剩余到槽深。（a）p=7、序号0至6的二次剩余为0、1、4、2、2、4、1；（b）按设计频率1 kHz、声速343 m/s计算，设计波长34.3 cm，槽深为0、2.45、9.80、4.90、4.90、9.80、2.45 cm，深度向下增加。原创教学计算，采用论文原理另选七槽示例；未规定槽宽、壁厚或实际材料，不是制造图，也不是实测散射指向图。<a href="#ref-schroeder-diffusers-1979">14</a></figcaption>
</figure>

### 扩散、吸收和听觉偏好分别验证

材料是否吸收声能、结构把反射送向哪些方向、听者是否喜欢由此形成的声场，是三个不同问题。理想序列不能证明实际扩散体在所有频率、入射角和距离下都具有均匀散射；有限尺寸、重复结构与损耗会影响结果。[14](#ref-schroeder-diffusers-1979)

对听觉研究而言，这一贡献也提示：空间线索首先由声音传播和测量链决定，然后由听者利用。房间或表面的几何设计、耳边信号的保真度、行为偏好应连续讨论；缺少中间环节时，数学上的优美结构不能直接代表聆听效果。

## CELP：通过合成反馈寻找语音表示

### 从传输波形到传输重建所需的信息

1985年，Schroeder与Bishnu S. Atal发表CELP方法。它结合短时线性预测、长期预测与码本激励，利用语音结构减少直接传输每个采样值的需求。短时预测描述局部谱包络，长期预测利用较长时间的周期性，码本候选则提供合成语音的激励。[15](#ref-schroeder-celp-1985)

这与[共振峰](../formant/)和[谐波性](../harmonicity/)有关，但编码参数不等于一个个被准确测出的生理器官或语音学标签。预测器是信号模型；谱包络可以与声道共振联系，模型误差仍需要通过重建质量评价。

### “分析—合成”闭环与听觉加权

编码端试用候选激励，经合成器生成重建语音，再与输入比较。感知加权误差用于影响候选选择：不同频率处的误差不被简单地视作同样重要。编码器发送选定码本索引以及重建所需的增益、预测等参数，解码器据此生成输出。[15](#ref-schroeder-celp-1985)

因此，“码本”不是存有全部词句的语音字典，也不是听神经活动的数据库。它提供用于合成的候选向量；一个码本索引必须结合相同码本、合成模型与其它参数才有意义。[声码器](../vocoder/)词条可作为了解分析与合成分工的入口，但不同编码系统的结构需要分别比较。

### 一道有用的码率计算

原论文方法使用1024个候选码向量；选一个需要10 bit。每5 ms发送一次该索引，对应每秒200次，即索引部分约为2000 bit/s。论文讨论的总码率为4.8 kbit/s；**2 kbit/s只是这部分索引，不能写成完整系统码率**，其它参数也需要传输。[15](#ref-schroeder-celp-1985)

这段计算揭示了压缩的代价与收益：接收端依靠共享结构重建大量采样值，而发送端承担搜索与模型选择。它并不保证每种语音、噪声、丢包或语言条件下都同样自然。波形误差、主观音质、词句识别和算法复杂度是不同评价维度。

感知加权的存在也不表示系统复制了完整听觉通路。尤其不能从通信语音编码直接推导[人工耳蜗编码策略](../cochlear-implant-coding-strategies/)的效果：后者还涉及电刺激和神经接口，输入输出条件已经改变。

## 历史故事与著作：数学怎样跨过学科边界

### 导师把“缺少数学”的声学变成研究机会

1994年的IEEE口述史中，Schroeder回忆，他早年曾觉得声学没有足够吸引他的数学内容。Erwin Meyer则把微波腔体的模态问题与音乐厅中的声学问题联系起来，引导他认识声学也包含值得处理的波动与统计问题。[2](#ref-schroeder-oral)

这个故事适合解释他的研究兴趣，而不是证明电磁波与声波在任何条件下完全相同。可迁移的是对边界、模态和波动方程的思考；具体物理变量、极化、材料与实验尺度仍需要重新定义。科学史中的类比若不保留这些条件，容易把启发性变成错误的等同。

### 计算机也成为图形创作工具

Schroeder与Sue Hanauer在1968年开展计算图形创作，作品随后进入包括1969年“Some More Beginnings”在内的展览。ZKM艺术与媒体中心的记录，为这条较少出现在声学教材中的活动提供了机构来源。[18](#ref-schroeder-zkm)

这部分历史说明他的计算兴趣也包含可视化和形式探索。本站没有将未核验转载许可的艺术图形直接当作配图；本文的三个科学图由代码独立生成，各自给出变量、计算条件和验证记录。肖像则采用单独核对的开放许可照片。

### 按问题选择著作，而非按书名堆砌

| 著作入口 | 适合带着什么问题阅读 | 本文使用范围 |
| --- | --- | --- |
| *Number Theory in Science and Communication*，所列来源为2006年第4版 | 数论结构怎样用于通信、物理和信息表示 | 出版社书目与内容介绍；不声称逐章核验全部证明 |
| *Computer Speech: Recognition, Compression, Synthesis*，1999年第1版 | 听觉、语音分析、合成和压缩怎样联系 | 出版社书目与目录；编码方法另引原论文 |
| IEEE 1994年口述史 | 研究问题从哪里来，机构与合作者怎样参与 | 当事人回忆；与同期论文区分 |

这些书把多个领域组织到共同的计算语言中；学习时仍应返回原始问题，检查近似假设与测试结果。书籍版本、电子发行日期和第一版年份也需分开，不能用当前目录页的上线日期替代原著出版年。[2](#ref-schroeder-oral)[16](#ref-schroeder-computer-speech)[17](#ref-schroeder-number-theory)

## 怎样继续学习与检验这些方法

### 三条阅读路线

研究房间与聆听环境，可从[房间声学](../room-acoustics/)进入脉冲响应、频带衰减与空间线索；研究听觉机制，可从[心理声学](../psychoacoustics/)、[听觉滤波器](../auditory-filter/)和[掩蔽](../masking/)进入相位实验；研究语音表示，可结合[语谱图](../spectrogram/)、[共振峰](../formant/)与[声码器](../vocoder/)，再阅读CELP原论文。

三条路线可以共享信号分析工具，却不能共享未经说明的结论。房间响应需要验证采集链；相位实验需要验证刺激与行为协议；语音编码需要验证码率、解码结构和质量评价。对Schroeder的贡献最有帮助的理解，是看清他怎样为不同问题选择可检验的表示。

### 从图中关系到可复现计算

本文配图代码分别检查了能量曲线的单调性与拟合区间、三种谐波信号的RMS及幅度谱一致性、正负相位的周期性时间反转，以及二次剩余和槽深映射。计算验证回答“图是否按所述公式生成”；它不能替代房间测量、听者实验或实体扩散体的性能测试。

若将这些教学信号用于播放或研究，还需增加校准、设备响应检查、适当的边缘处理与完整实验设计。语谱图可以帮助检查频率组成，但只看一张幅度图不足以确认相位；测量差异是否由目标机制引起，也需要对照条件。本文保留为待专业审阅的深度人物稿，研究史、方法与应用各按实际访问范围记录来源。

## 出版著作与代表论文

以下按本文涉及的研究主线选列著作和代表成果，便于查找原文，并非完整作品目录或按引用次数排名。署名保留合作与编辑关系，所核版本与原始发表年份分别记录。

### 出版著作

| 出版时间 | 著作、署名与出版信息 | 定位与阅读线索 |
| --- | --- | --- |
| 2006（第4版） | [Number Theory in Science and Communication: With Applications in Cryptography, Physics, Digital Information, Computing, and Self-Similarity](https://link.springer.com/book/10.1007/b137861)<br />Manfred R. Schroeder<br />Springer Series in Information Sciences, 7 | 独著；所列为2006年第四版，连接数论与科学、通信。[17](#ref-schroeder-number-theory) |
| 1991 | [Fractals, Chaos, Power Laws: Minutes from an Infinite Paradise](https://www.cambridge.org/core/journals/mathematical-gazette/article/abs/fractals-chaos-power-laws-minutes-from-an-infinite-paradise-by-manfred-schroeder-pp-429-2449-1991-isbn-0716721368-freeman/D9280A19DD2DF4126D71473F8A2FBCAF)<br />Manfred Schroeder<br />W. H. Freeman；ISBN 0-7167-2136-8 | 跨学科著作；作为分形、混沌与幂律的阅读入口，不替代听觉实验。[20](#ref-schroeder-fractals-book-1991) |
| 1999（第1版） | [Computer Speech: Recognition, Compression, Synthesis](https://link.springer.com/book/10.1007/978-3-662-03861-1)<br />Manfred R. Schroeder<br />Springer Series in Information Sciences, 35 | 独著；所列1999年第一版，涵盖识别、压缩与合成。[16](#ref-schroeder-computer-speech) |

### 代表论文与研究成果

| 年份 | 论文、作者与发表信息 | 主要贡献与阅读范围 |
| --- | --- | --- |
| 1965 | [New Method of Measuring Reverberation Time](https://doi.org/10.1121/1.1909343)<br />Manfred R. Schroeder<br />The Journal of the Acoustical Society of America, 37(3): 409–412 | 提出由脉冲响应积分取得混响衰减的测量方法。[5](#ref-room-acoustics-schroeder) |
| 1970 | [Synthesis of low-peak-factor signals and binary sequences with low autocorrelation (Corresp.)](https://ieeexplore.ieee.org/document/1054411)<br />Manfred R. Schroeder<br />IEEE Transactions on Information Theory, 16(1), 85–89 | 研究低峰值因数信号与低自相关二进制序列。[7](#ref-schroeder-phase-1970) |
| 1974 | [Comparative study of European concert halls: correlation of subjective preference with geometric and acoustic parameters](https://doi.org/10.1121/1.1903408)<br />M. R. Schroeder; D. Gottlob; K. F. Siebrasse<br />Journal of the Acoustical Society of America, 56(4), 1195–1201 | 与Gottlob、Siebrasse联系音乐厅主观偏好、几何与声学参数。[13](#ref-schroeder-halls-1974) |
| 1979 | [Binaural dissimilarity and optimum ceilings for concert halls: More lateral sound diffusion](https://languagelog.ldc.upenn.edu/myl/SchroederQuadraticResidueDiffusors.pdf)<br />Manfred R. Schroeder<br />Journal of the Acoustical Society of America, 65(4), 958–963 | 研究侧向扩散、双耳不相似性与音乐厅顶棚。[14](#ref-schroeder-diffusers-1979) |
| 1985 | [Code-excited linear prediction (CELP): High-quality speech at very low bit rates](https://www.csd.uoc.gr/~hy474/bibliography/CELP.pdf)<br />Manfred R. Schroeder; Bishnu S. Atal<br />IEEE ICASSP, 10, 937–940 | 与Atal研究低码率码激励线性预测语音编码。[15](#ref-schroeder-celp-1985) |
| 1996 | [The “Schroeder frequency” revisited](https://doi.org/10.1121/1.414868)<br />Manfred R. Schroeder<br />Journal of the Acoustical Society of America, 99(5), 3240–3241 | 重新讨论Schroeder频率的定义与应用。[3](#ref-schroeder-frequency-1996) |
