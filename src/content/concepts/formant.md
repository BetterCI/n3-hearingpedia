---
title: "共振峰"
english: "Formant"
slug: "formant"
summary: "声道共振相关的谱特征，是元音等语音分析的重要概念，不能与基频、谐波或任意谱峰混同。"
categories: ["acoustics","speech","signal-processing"]
tags: ["formant"]
aliases: ["formants","F1","F2","F3","formant frequency","共振峰频率"]
status: draft
depth: in-depth
last_updated: "2026-10-07"
authors: ["AI 辅助编写"]
references: ["formant-titze", "formant-kent", "formant-sourcefilter", "formant-whalen", "formant-harmonics", "formant-synthesis", "yun-formant-2026", "formant-soprano", "formant-hillenbrand", "formant-normalization", "formant-peterson", "formant-dialect", "formant-guide", "formant-dynamic", "formant-clear", "formant-spectrogram", "formant-shadle", "formant-chen", "formant-children", "formant-accuracy", "formant-burg", "formant-track", "formant-path", "formant-discrimination", "formant-praatcode", "formant-parselmouth", "formant-vtl", "formant-soundgen", "zebe-formants-2026"]
batch: 3
order: 43
literature_checked_at: "2026-10-07"
knowledge_area: "sound"
kind: "quantity"
key_facts: [{"label":"主要对象","value":"声道共振相关频率与带宽"},{"label":"常见记号","value":"F1、F2、F3 等"},{"label":"主要区别","value":"基频、谐波与声道共振"}]
---

**共振峰**（formant）是声音频谱包络中局部能量相对集中的区域。在语音研究中，它通常与声道的声学共振联系起来，按频率由低到高记为第一共振峰、第二共振峰、第三共振峰等，常用符号为 $F_1$、$F_2$、$F_3$。共振峰频率、带宽、相对强度及其随时间的变化，是描述元音音质、发音动作和言语感知的重要参数。[1](#ref-formant-titze)[2](#ref-formant-kent)

共振峰与[基频](../fundamental-frequency/)提供不同的信息。一个人可以用较低或较高的音调发同一个元音，也可以在大致相同的音调上发出“衣”“啊”“乌”等不同声音。前一种变化主要涉及声源振动周期，后一种变化主要涉及声道形状及其滤波作用；实际发音中二者还可能相互影响。把某条较强的谐波直接当作共振峰，或者把第一共振峰当成基频，都会混淆声源结构与声道作用。[3](#ref-formant-sourcefilter)[4](#ref-formant-whalen)

“共振峰”在不同研究中存在相近但不完全相同的用法：有时指输出声音的谱包络峰，有时指推断的声道共振，有时指线性预测模型的极点频率。本词条以谱包络及其声道共振基础为主线；讨论估计或合成参数时，明确区分物理共振、观测谱峰和模型极点，避免将它们无条件视为完全相等。[1](#ref-formant-titze)[4](#ref-formant-whalen)

## 定义、参数与相邻概念

### 频率、带宽和强度

共振峰频率一般以 Hz 表示，用于描述谱包络增强区域的位置。带宽描述该区域的频率扩展程度；对孤立且形状规则的共振响应，常以峰值功率下降到一半的两个频率之差定义半功率带宽，对应幅度下降约 3 dB。真实语音中多个峰可以重叠，声源谱倾斜也会改变外观，因此测得的谱峰宽度不必等于模型给出的共振带宽。[2](#ref-formant-kent)

共振峰强度描述谱包络局部峰或相关频带的幅度、功率或相对声级，报告时应说明参考和计算方法。它不是[响度](../loudness/)的直接读数，也不等同于某个频带的总声能。一个共振峰可能因声源激励不足而很弱，两个相近共振也可能共同形成一个宽的增强区域；“图上没有清楚峰形”不能单独证明声道没有相应共振。[1](#ref-formant-titze)[4](#ref-formant-whalen)

### 基频、谐波与共振峰

有声语音的声源近似周期性，频谱中通常出现位于基频整数倍的谐波。基频决定这些离散成分的间隔，声道滤波则影响哪些谐波被相对增强。[谐波性](../harmonicity/)描述成分是否接近同一个基频的整数倍结构，共振峰描述较宽的谱包络特征，二者并不是同一维度。即使多个谐波共同处于第一共振峰区域，也不能把每个谐波称作一个共振峰。[1](#ref-formant-titze)[5](#ref-formant-harmonics)

| 概念 | 描述对象 | 典型观察 | 不能据此直接断定 |
| --- | --- | --- | --- |
| 基频 | 近似周期声源的重复频率 | 周期长度、谐波间距 | 元音类别或声道共振位置 |
| 谐波 | 声源周期性产生的离散频率成分 | 长窗语谱图中的细条纹 | 每条条纹都是一个共振峰 |
| 共振峰 | 谱包络增强及其共振基础 | 较宽的能量带、谱包络局部峰 | 精确舌位或唯一发音姿态 |
| 共振峰估计值 | 算法对局部声音的模型化结果 | 频率、带宽和轨迹输出 | 无误差的声道物理测量 |

### 共振峰不只存在于有声元音

声道共振并不因声带停止周期振动而消失。耳语等非周期激励也可以携带声道滤波的信息，只是其声源与常规有声元音不同。辅音中的声道约束、噪声激励位置和鼻腔耦合，又会形成比简单元音模型更复杂的频谱。不能将所有无声段都解释为“没有共振峰”，也不能把所有辅音噪声谱峰都按元音的方式编号和解释。[2](#ref-formant-kent)[3](#ref-formant-sourcefilter)

## 声源—滤波器原理

### 周期声源经过声道

简化的声源—滤波器模型把发声分为声源、声道传递及唇端辐射等环节。在频域可以写为：

$$
X(f)=G(f)\,H(f)\,R(f).
$$

其中 $G(f)$ 为声源谱，$H(f)$ 为声道传递函数，$R(f)$ 为辐射相关项，$X(f)$ 为输出声音的频谱。该模型说明共振怎样改变声源各频率成分的相对幅度，却不意味着共振会在没有激励的频率处自动产生新的谐波。对周期声源而言，输出仍主要出现在原来的谐波位置，只是幅度不同。[3](#ref-formant-sourcefilter)[6](#ref-formant-synthesis)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/formant/01-source-filter-spectrum.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/formant/01-source-filter-spectrum.svg" alt="周期声源、声道滤波与输出频谱" loading="lazy" /></a>
<figcaption><p>图 1　声源—滤波器原理的合成示例。A 为基频 120 Hz、谐波幅度随阶次下降的离散声源；B 为三个二阶共振器级联的响应，设定极点频率为 700、1200、2500 Hz；C 为声源与滤波响应相乘后的输出，红线表示连续谱包络模型，蓝线表示谐波采样。纵轴使用一致的模型参考，不是 dB SPL；图中未单独加入唇端辐射或声源—声道相互作用。虚线标记模型参数，其位置不要求与输出谱包络的局部最大值精确重合。</p></figcaption>
</figure>

### 管道近似与共振位置

将声道近似为一端封闭、另一端开放的均匀管道，可以理解共振频率为何依赖声道长度。忽略损耗及端部修正时，其共振频率近似为：

$$
f_n\approx\frac{(2n-1)c}{4L},\qquad n=1,2,3,\ldots
$$

其中 $L$ 为管长，$c$ 为声速。取教学值 $L=0.17$ m、$c=340$ m/s，可得到约 500、1500、2500 Hz 的前三个共振。这个例子解释长度与共振尺度的关系，不是任何具体元音的标准频率表；真实声道的截面积沿位置变化，还包含舌、唇、咽腔及边界条件。[6](#ref-formant-synthesis)

声道并非一个可按“一个腔体对应一个共振峰”简单拆分的装置。局部收缩和腔体耦合可以同时影响多个共振，某个共振频率对不同部位形状的敏感性也会不同。因此，共振峰是理解发音的声学线索，却不能凭一个频率值唯一重建整个声道。[2](#ref-formant-kent)[7](#ref-yun-formant-2026)

### 模型的适用边界

线性声源—滤波器分离对很多语音分析有用，但声门边界、鼻腔耦合和发声方式会使实际情况更复杂。鼻腔通路可增加共振并产生反共振，即某些频率区域的削弱；只包含极点、不含零点的模型可能无法充分描述这种频谱。声源与声道还可能相互作用，尤其不宜把歌唱中基频变化时的所有谱变化都解释为同一固定滤波器的被动输出。[2](#ref-formant-kent)[8](#ref-formant-soprano)[7](#ref-yun-formant-2026)

## 元音空间与发音关系

### 第一、第二共振峰的典型联系

在许多口元音中，第一共振峰与开口程度、舌高具有经验联系：较高舌位的闭元音常具有较低的第一共振峰，较开放的元音常具有较高的第一共振峰。第二共振峰常用于描述前后舌位相关的音质差异，前元音通常较高，后元音通常较低。但唇形、声道长度和其他部位的变化也参与其中，这些对应不应理解为一对一的解剖测量。[2](#ref-formant-kent)[9](#ref-formant-hillenbrand)

元音空间通常将第二共振峰放在横轴，第一共振峰放在纵轴，并将两轴反向排列。这样，较低的第一共振峰位于图上方，较高的第二共振峰位于左侧，便于与常见的发音元音图比较。图的方位是一种约定，并非听觉系统的实际空间地图；也有研究使用其他轴向或频率尺度。[9](#ref-formant-hillenbrand)[10](#ref-formant-normalization)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/formant/03-vowel-space.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/formant/03-vowel-space.svg" alt="三个示意元音在第一第二共振峰空间中的位置" loading="lazy" /></a>
<figcaption><p>图 2　i、a、u 的示意元音空间。使用人工设定的第一、第二共振峰参数：i 为 330、2300 Hz，a 为 750、1200 Hz，u 为 350、800 Hz；横纵轴均反向排列。数值仅用于教学和图 3 的合成，不是普通话常模，也不是某位说话者的实测结果。三个点没有表达群体分布、发音容许范围或分类边界。</p></figcaption>
</figure>

### 相同元音不具有唯一频率

不同说话者的声道长度及形状不同，同一个元音的频率可以呈现较大差异。方言、语境、重音及发声方式也会影响位置和轨迹。Peterson 与 Barney 的经典研究以及 Hillenbrand 等的后续研究，提供了元音声学测量的重要基础；它们涉及特定英语材料和说话者，不能直接作为普通话、儿童或歌唱的通用参考表。[11](#ref-formant-peterson)[9](#ref-formant-hillenbrand)[12](#ref-formant-dialect)

跨说话者比较时，可以研究原始 Hz 值，也可以在明确目标下使用归一化。原始值适于保留绝对频率及声道尺度差异，归一化则可能帮助比较元音系统的相对结构。采用某种方法之前，应说明希望减少哪类差异、保留哪类语言或生理信息，而不能先归一化，再把被消除的差异当作不存在。[10](#ref-formant-normalization)[13](#ref-formant-guide)

### 动态轨迹与协同发音

真实言语的共振峰通常随时间变化。元音起始会受前面的辅音影响，结束会向后续发音过渡；双元音还包含明显的音质运动。取一个稳定时刻的第一、第二共振峰有助于简化描述，但会丢失轨迹、时长和变化速率。Hillenbrand 等的结果表明，加入时长及频谱变化能改善其材料中元音的区分，静态坐标并不包含全部相关信息。[9](#ref-formant-hillenbrand)[14](#ref-formant-dynamic)

研究动态元音时，可以记录多个相对时间点或拟合整段轨迹，但应说明如何分段、是否排除边界，以及时间归一化是否抹去了实际时长。不同语境或方言产生的轨迹差异，不宜仅用一个平均坐标概括；反过来，轨迹长度变大也不自动表示发音更清楚或更接近某种规范。[14](#ref-formant-dynamic)[15](#ref-formant-clear)

## 如何从语谱图观察共振峰

### 宽带能量与细谐波条纹

短分析窗提供较好的时域定位、较差的频率分辨，常便于观察发音起止、周期性竖纹和较宽的能量集中区域。较长分析窗提供较细的频率分辨，常能看到一条条谐波。两种图呈现的是同一信号的不同分析结果，不应把短窗图中的宽带区域与长窗图中的单条谐波混为一谈。零填充可以使显示频率网格更密，却不能替代较长有效窗口提供的信息。[2](#ref-formant-kent)[16](#ref-formant-spectrogram)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/formant/04-synthetic-vowel-spectrogram.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/formant/04-synthetic-vowel-spectrogram.svg" alt="同一组合成元音的波形与短窗长窗语谱图" loading="lazy" /></a>
<figcaption><p>图 3　同一组合成元音的波形与两种语谱图。A 的相对幅度限制在 −1 至 1，信号峰值为 0.9；i、a、u 的基频均为 130 Hz，持续时间各 450 ms，间隔 80 ms。B 使用 8 ms 汉宁窗，红色虚线标记预先设定的三个模型极点频率；C 使用 40 ms 窗，展示较细的谐波条纹。两幅语谱图均以各自全图最大谱幅度为 0 dB，采用相同显示范围；不同窗长的幅度不能据色深直接定量比较。红线是已知合成参数，不是自动估计轨迹或人工测量结果。图为合成信号的计算结果，不是自然语音录音。</p></figcaption>
</figure>

### 不能只看最黑的一条线

语谱图的颜色反映分析后的谱幅度或功率，还受到声源谱、显示动态范围和频率分辨影响。最强的谐波可能处在共振附近，但不一定精确落在共振中心；某个高频共振区域可能因声源能量弱而不显著。观察时应结合邻近成分、整体谱包络和多个时间帧，而不是只选最深色的细线。[4](#ref-formant-whalen)[17](#ref-formant-shadle)

叠加的自动共振峰点也不能代替原始图。一个视觉上平滑的轨迹可能沿着错误谐波延续，两个候选峰可能被合并，噪声或瞬态也可能引出额外估计。好的核查不仅删除异常高值，还要确认轨迹与声学结构是否相符，并保留无法确定的区间。[17](#ref-formant-shadle)[13](#ref-formant-guide)

## 共振峰频率、带宽与声源采样

### 带宽改变什么

在中心频率相同的理想单峰中，较小带宽意味着增强更集中、峰形更尖；较大带宽意味着增强分布更宽。带宽受声道损耗、边界与耦合影响。实际语音的带宽估计通常比频率估计更困难，也不能直接把“峰更宽”解释为舌位变化、发音障碍或听觉滤波器变宽。声道滤波与[听觉滤波器](../auditory-filter/)是两个不同环节。[2](#ref-formant-kent)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/formant/05-formant-bandwidth.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/formant/05-formant-bandwidth.svg" alt="理想单峰的半功率带宽" loading="lazy" /></a>
<figcaption><p>图 4　中心频率相同、带宽不同的理想单峰。两曲线中心均为 1000 Hz，按峰值归一化；蓝色和红色的半功率带宽分别为 60 和 180 Hz，横线标记约 −3.01 dB 处的宽度。曲线采用局部洛伦兹形近似，以独立说明频率和带宽；它不是从图 3 的元音测得的带宽，也不包含多峰重叠、声源谱倾斜或实际声道损耗的全部机制。</p></figcaption>
</figure>

### 基频升高时的谐波稀疏

当基频较低时，同一个共振区域内可能有多个谐波，便于从相对幅度推断谱包络；基频升高后，谐波间距增大，局部包络只能从较少采样点推断。即使声道模型完全不变，最强谐波的频率和自动输出的第一共振峰也可能变化。这是测量不确定性的重要来源，尤其需要注意高音、儿童及部分歌唱材料。[17](#ref-formant-shadle)[18](#ref-formant-chen)[19](#ref-formant-children)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/formant/02-harmonic-sampling.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/formant/02-harmonic-sampling.svg" alt="固定滤波器在不同基频下的谐波采样" loading="lazy" /></a>
<figcaption><p>图 5　相同滤波器和声源谱倾斜下，基频改变带来的采样差异。上、下图基频分别为 120 和 400 Hz，连续包络模型相同，灰色虚线标记 700、1200、2500 Hz 的设定极点频率。400 Hz 条件在第一共振区域没有恰好位于 700 Hz 的谐波，不能因此断定第一共振频率变为 800 Hz。该图展示模型采样关系，不模拟所有高音发声中的声道调整。</p></figcaption>
</figure>

### 系统偏差与统计解释

共振峰估计可能偏向较强的谐波，误差与基频、共振位置及算法有关。Shadle 等在合成与自然元音中比较多种方法，发现合成材料中的改善不保证自然语音具有同样表现。Chen 等的模拟进一步表明，基频相关误差可以造成有系统的变异性偏差，大样本不一定能消除这种问题。[17](#ref-formant-shadle)[18](#ref-formant-chen)

因此，如果研究观察到儿童共振峰变异较大，或者提高基频后第一共振峰出现变化，应先检查测量误差，再解释发音控制或声道改变。仪器重复测得相近结果属于一致性，不等于已经知道真实声道共振；自然语音通常缺少可直接用于逐帧验证的物理真值。[4](#ref-formant-whalen)[19](#ref-formant-children)

## 估计方法与参数选择

### 频谱切片与谱包络

在相对稳定的元音区间提取短时频谱，可以结合谐波幅度和谱包络定位候选共振峰。平滑、倒谱分析及重分配等方法提供不同观察方式，但都需要选择时间与频率尺度。过度平滑可能合并邻近峰，平滑不足又会把谐波起伏误作包络结构；因此，频谱图是证据的一部分，不能只凭自动局部峰搜索确定共振。[17](#ref-formant-shadle)[20](#ref-formant-accuracy)

### 线性预测分析

线性预测通过前若干个样本预测当前样本，用一个全极点滤波器描述短时谱结构。采用 $x[n]+\sum_{k=1}^{p}a_kx[n-k]=e[n]$ 的系数约定时，可写为：

$$
\hat H(z)=\frac{g}{1+\sum_{k=1}^{p}a_kz^{-k}}.
$$

其中 $p$ 为模型阶数，$g$ 为增益。若存在共轭复极点 $z_i=r_i e^{j\theta_i}$，常用极点角度估计频率，用半径估计带宽：

$$
\hat F_i=\frac{\theta_i f_s}{2\pi},\qquad
\hat B_i=-\frac{f_s}{\pi}\ln r_i.
$$

这里 $f_s$ 为采样率；带宽公式是二阶共振器的常用参数关系，在多峰及复杂声源条件下不能自动等同于观测谱峰的半功率宽度。实极点、过宽峰、边缘候选或不稳定结果需要处理。全极点近似还难以充分表达反共振，因此返回的每一对复极点不都对应一个明确物理声道共振。[21](#ref-formant-burg)[2](#ref-formant-kent)

### 窗长、阶数与搜索上限

窗长应在近似平稳性与频率分辨之间权衡；模型阶数过低可能合并峰，过高可能拟合谐波或噪声。搜索上限决定算法在哪个频率范围内分配候选峰，应与说话者和材料相适应。Praat 的官方文档给出成人及儿童的示例设置，但也明确指出个体及元音之间存在差异，不能按性别标签固定使用一套数值而不核查。[21](#ref-formant-burg)

采样率和预加重同样需要报告。降采样要先进行适当抗混叠处理；预加重可以减轻声源谱倾斜对估计的影响，却不会把信号变成纯粹的声道响应。强噪声、削波、低质量压缩、录音设备频响及鼻音化，都可能影响候选峰。比较组间频率时，应尽量匹配录音与处理条件。[21](#ref-formant-burg)[2](#ref-formant-kent)

### 从候选峰到连续轨迹

追踪算法依据相邻帧的频率、带宽及变化代价选择路径，可以减少明显跳峰，但不能创造第一阶段没有可靠估计出的共振。若错误候选本身很平滑，追踪也可能稳定地选错。Praat 的轨迹追踪与 FormantPath 提供不同的整理方式，后者可比较不同分析参数产生的候选结果，仍需要声学核查。[22](#ref-formant-track)[23](#ref-formant-path)[17](#ref-formant-shadle)

### 测量区间与缺失值

报告应明确分析对象是元音中点、稳定段平均还是整段轨迹，同时说明边界、异常值和缺失值如何处理。不能先选择最符合预期的参数或帧，再把结果当成独立证据。可预先定义核查规则，对部分材料进行重复标注或参数敏感性比较，并保留难以可靠测量的区间，而不是强制每帧输出第一至第三共振峰。[13](#ref-formant-guide)[20](#ref-formant-accuracy)

## 共振峰与言语感知

### 元音音质并非两个数字

第一、第二共振峰为许多元音差异提供重要线索，但听者还利用更高频谱结构、谐波幅度关系、时长和动态变化。Assmann 与 Nearey 的合成元音实验显示，第一共振峰区域中的谐波结构会影响匹配与辨认；Kewley-Port 与 Watson 的辨别研究也说明，共振位置与谐波对齐关系会改变部分测量结果。不能把共振峰感知当作完全独立于声源的包络读取。[5](#ref-formant-harmonics)[24](#ref-formant-discrimination)

实验中的共振峰频率辨别阈，应结合刺激、训练、任务和声源条件解释，不是所有听者、元音和噪声条件共有的精度。声学上存在可测差异，也不保证产生相同程度的语音类别改变；语言经验和周围声音共同影响最终辨认。[24](#ref-formant-discrimination)[9](#ref-formant-hillenbrand)

### 普通话元音与声调

普通话中，共振峰支持元音及音节音质，基频轨迹则为[普通话汉语声调](../mandarin-lexical-tone/)提供重要线索。两类信息可以同时存在，也可能随发音方式共同改变。拼音中的字母与国际音标并非总是一对一对应，图 2 的 i、a、u 只是教学标签，不宜直接用其三个坐标描述全部普通话单元音、韵母或不同语境中的读音。

若研究希望建立普通话参考元音空间，需要明确说话者、方言背景、音节结构、声调、语速、取样位置和归一化方法。当前图示没有提供这样的语料数据，因此不能作为发音评价或临床判断的界限；英语经典数据也不能替代普通话常模。[9](#ref-formant-hillenbrand)[12](#ref-formant-dialect)[10](#ref-formant-normalization)

### 听力损失和听觉设备

[听力损失](../hearing-loss/)可能改变频谱线索的可听性与利用方式。[助听器](../hearing-aid/)的增益和压缩、[人工耳蜗](../cochlear-implant/)的频率分配与有效通道分辨率，以及[声码器](../vocoder/)的频谱降质，都可能改变共振相关信息。不过共振峰保存程度只是评价的一部分，不能单独保证完整[言语可懂度](../speech-intelligibility/)。[15](#ref-formant-clear)

Ferguson 与 Kewley-Port 在特定清晰与会话言语材料中发现，元音目标、动态变化和时长都参与辨认，而年轻正常听力与年长听力损失组的收益及线索利用并不相同。该设计同时涉及年龄和听力差异，不能只凭两组结果把全部变化归因于听力损失。设备研究应在目标群体及具体材料中测量收益，而不是从漂亮的共振峰图直接推断理解改善。[15](#ref-formant-clear)

## 归一化、声道尺度与比较

### 为什么要归一化

同一语言类别可能因说话者的声道尺度而具有不同绝对频率。归一化尝试减少某些说话者差异，使相对元音模式更容易比较。Adank 等比较多种方法时，区分只使用单个元音信息的方法与利用说话者多个元音的方法，发现不同方法的表现并不等价。因此，不存在脱离研究目标的“最佳归一化”。[10](#ref-formant-normalization)

常见方法包括对数或知觉频率转换、共振峰比值，以及在说话者内按均值和标准差标准化。它们改变的尺度和信息不同，结果应注明方法，归一化坐标也不应继续标作原始 Hz。只记录少数类别、每类样本数不同或语境不平衡，都可能影响说话者内统计量。[10](#ref-formant-normalization)[13](#ref-formant-guide)

### 声道长度推断的限度

均匀管道近似说明声道尺度与共振频率的整体关系，但自然语音的多个共振不是均匀排列。根据共振峰估计的“表观声道长度”依赖模型、使用的频率数量及测量误差，并不等同于影像测得的解剖长度。Anikin、Barreda 与 Reby 的方法论文提供相关统计和软件框架，同时强调多样本、多共振峰及人工核查的重要性。[13](#ref-formant-guide)

因此，声道尺度、元音构形与语言类别应分别处理。某一组共振峰整体偏低，可能涉及尺度，也可能涉及材料和发音策略；单一元音的比值不能自动消除所有说话者差异。报告推断结果时，应同时保留原始频率、模型假设及不确定区间。[13](#ref-formant-guide)[10](#ref-formant-normalization)

## 计算模型与公开实现

### 共振器合成模型

级联或并联的共振器可以合成具有指定频率及带宽的声音，适合检验某类声学改变对感知的影响。Praat 的[声源—滤波器合成教程](https://praat.org/manual/Source-filter_synthesis.html)提供从声源与滤波对象构造声音的入口；[官方源码仓库](https://github.com/praat/praat.github.io)可查阅实现。合成参数可作为受控模型中的已知值，但它们不是自然语音中无需验证的物理真值。[3](#ref-formant-sourcefilter)[25](#ref-formant-praatcode)

本词条的[配图生成代码](/n3-hearingpedia/figures/formant/generate-figures.py)实现了固定参数的二阶共振器级联、谐波声源以及短时语谱图。代码生成稳定滤波器并将波形峰值归一化为 0.9，可以复现图 1 至图 5；它是教学模型，没有模拟真实声门流、鼻腔零点、完整辐射或设备传递。

### 共振峰估计与脚本处理

Praat 的[Burg 共振峰分析文档](https://fon.hum.uva.nl/praat/manual/Sound__To_Formant__burg____.html)说明模型和参数，[FormantPath 文档](https://uvafon.hum.uva.nl/praat/manual/FormantPath.html)介绍多参数候选整理。[Parselmouth](https://github.com/YannickJadoul/Parselmouth)及其[官方文档](https://parselmouth.readthedocs.io/en/stable/)将 Praat 的功能接入 Python，适合批量处理和可重复分析；自动批处理仍应保留参数、异常记录及抽样核查。[21](#ref-formant-burg)[23](#ref-formant-path)[26](#ref-formant-parselmouth)

使用线性预测时应区分“设置的候选峰数量”和“声音中可靠存在的共振数量”。软件返回候选频率，是一次模型拟合的输出，而不是直接测得发音器官。参数敏感性、缺失值以及跨方法一致性，应作为分析报告的一部分。[17](#ref-formant-shadle)[13](#ref-formant-guide)

### 声道构形模型与尺度工具

[VocalTractLab 官方网站](https://www.vocaltractlab.de/)提供发音合成及声道模型的信息，适合研究构形如何影响声音；它与直接设定共振器频率的合成方式不同。模型采用的几何、边界及声源仍需要和目标材料匹配，不能把一个拟合构形当作某个自然元音的唯一真实姿态。[27](#ref-formant-vtl)[7](#ref-yun-formant-2026)

声道尺度及共振模式分析可参考 Anikin 等的[方法论文](https://doi.org/10.3758/s13428-023-02288-x)和 [soundgen 官方软件说明](https://cran.r-project.org/package=soundgen)。论文讨论的工具适于标注、核查和建模，应用前应理解采用的尺度假设；本轮未执行这些外部模型，因此不报告其性能或运行结果。[13](#ref-formant-guide)[28](#ref-formant-soundgen)

## 研究沿革与当前问题

### 从静态元音图到动态分析

早期元音研究建立了频谱与语言辨认之间的联系，随后线性预测及交互式测量工具使较大规模的共振峰分析成为可能。研究逐渐从元音中点扩展到动态轨迹、语境和说话者差异，同时更重视算法误差与共振定义。与其把每个新算法视为精确解剖测量，不如明确它在何种声音、参数及验证条件下有效。[11](#ref-formant-peterson)[9](#ref-formant-hillenbrand)[20](#ref-formant-accuracy)[4](#ref-formant-whalen)

### 发声边界与歌唱

2026 年 Yun 等的研究同步记录德语元音声音、发音相关测量及鼻气流，考察声门和腭咽边界对第一共振峰的影响。摘要报告，声门开放相关的变化方向并未完全符合先前模拟预测，而小幅腭咽开放与第一共振峰升高有关。它提示边界条件不能忽略，也不能把模拟方向直接当作自然发声中的确定规律。[7](#ref-yun-formant-2026)

同年 Zebe-Sheng 与 Immerz 比较专业女歌者的朗读、吟诵与歌唱德语元音，报告总体上吟诵更偏向强化发音，歌唱更偏向元音空间中央化，但存在例外。这类群体、语言与发声方式均有特定范围；结果不应变成所有歌唱者或普通话材料的普遍方向。高音歌唱还可能发生主动共振调整，需要把声源采样与实际声道改变共同考虑。[29](#ref-zebe-formants-2026)[8](#ref-formant-soprano)

### 尚需解决的测量问题

对高基频、儿童、鼻音化、非典型发声及自然连续言语，获得准确且可解释的共振参数仍有困难。合成信号提供已知模型参数，自然语音提供实际适用性，二者的验证不能互相替代。新方法应报告失败条件和不确定性，并检查误差是否与组别、基频或任务系统关联。[18](#ref-formant-chen)[19](#ref-formant-children)[17](#ref-formant-shadle)

## 相关词条

理解声源与声道的区别，可先阅读[基频](../fundamental-frequency/)、[谐波性](../harmonicity/)和[音高感知](../pitch-perception/)；理解声音怎样被听觉系统利用，可结合[听觉滤波器](../auditory-filter/)、[言语可懂度](../speech-intelligibility/)及[普通话汉语声调](../mandarin-lexical-tone/)；理解频谱处理的应用，可进一步阅读[声码器](../vocoder/)、[助听器](../hearing-aid/)和[人工耳蜗](../cochlear-implant/)。
