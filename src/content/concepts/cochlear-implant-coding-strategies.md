---
title: 人工耳蜗信号处理策略
english: Cochlear Implant Sound Coding Strategies
slug: cochlear-implant-coding-strategies
summary: 用公式、Python 教学代码、处理流程图和电极刺激图解释 CIS、ACE、FSP／FS4 与 HiRes 家族，并对照六个厂商的版本目录与研究证据。
categories: ["cochlear-implants","signal-processing","ai-hearing"]
tags: [sound-coding, cis, ace, speak, mp3000, fsp, fs4, hires, current-steering, electrodogram, deepace]
aliases: [人工耳蜗编码策略, 人工耳蜗声音编码策略, CI coding strategies, speech coding strategies, 声音编码, ACE, SPEAK, MP3000, FSP, FS4, HiRes120]
status: draft
depth: in-depth
last_updated: "2026-11-12"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["zeng-2008","ci-cochlear-cs61","ci-cochlear-guidance","ci-has-nexa-2026","ci-mp3000-2011","ci-medel-maestro11","ci-ab-target","ci-ab-legacy-specs","ci-ab-ifu","ci-gpyt-code","ci-ab-optima-fda","ci-neuro2-specs","ci-cochlear-ciom","ci-neuro-music-2022","ci-nurotron-enduro","ci-nurotron-design-2015","ci-listent-catalog","ci-pulsatile-code","ci-ccimobile-code","ci-deepace-code","ci-mixed-itd-2025","zhou-tle-2022","zhou-f0intfs-2023","ci-deepace-2023","ci-fused-deepace-2024","ci-electrodenet-2024","ci-avse-ecs-2026","ci-bace-motion-2026","ci-moc-2016","guerit-focusing-2026","wilson-1991","ci-spiking-code","ci-spiking-deepace-2026","ci-brain-separation-2026","ci-speech-music-2026"]
order: 45
batch: 4
knowledge_area: "technology"
kind: "strategy"
key_facts: [{"label":"输入与输出","value":"声音波形 → 多电极刺激序列"},{"label":"临床目录","value":"六个厂商／系统系列；注明版本与兼容范围"},{"label":"比较维度","value":"特征、选通道、脉冲时序、电映射与评价"},{"label":"代码证据","value":"区分研究仿真、硬件接口及商用等价实现"}]
---

**人工耳蜗信号处理策略**（cochlear implant sound coding strategies）是将声学输入转换为植入电极刺激序列的一组规则。它决定保留哪些频谱和时域信息、选择哪些通道、何时刺激，以及怎样把声音强度映射为电流或脉宽。[人工耳蜗](../cochlear-implant/)的声音处理器、植入体和个体 MAP 共同约束这些规则；策略名称不能单独预测听者的表现。[1](#ref-zeng-2008)

本词条汇总截至 **2026 年 10 月 4 日**能够核对的临床策略官方目录，覆盖 Cochlear、MED-EL、Advanced Bionics、Neurelec／Oticon Medical、诺尔康和力声特，并列出实际查到的代码仓库及研究策略。现行文档、旧设备兼容与实验策略分别标注。公开资料尚不足以证明“全球所有地区、全部历史型号”的完整清单；缺少算法说明或公开实现的项目直接注明，而不根据商品名称补写机制。

## 定义与知识体系

### 编码策略在处理链中的位置

**声音输入 → 前端增益／降噪 → 分频与特征提取 → 通道选择 → 电刺激映射与调度 → 电极—神经接口**

编码通常涉及中间的多个环节，而厂商“声音处理系统”还可能包括方向性、场景识别和无线输入。自动增益控制改变输入，[时域包络](../temporal-envelope/)和[时域精细结构](../temporal-fine-structure/)是信号表征，[n-of-m 编码](../n-of-m-coding/)是通道选择规则，[动态范围](../dynamic-range/)描述映射边界；它们处于不同概念层级。[1](#ref-zeng-2008)

### 五个可比较的维度

| 维度 | 需要记录的内容 | 常见误解 |
| --- | --- | --- |
| 特征提取 | 滤波器组或 FFT、频带范围、包络低通、是否提取零交叉或基频 | 包络含周期性，不等于完整保留精细结构 |
| 通道选择 | 固定全通道、能量峰值、掩蔽模型、双耳联合选择 | 分析通道数、电极数与每帧 maxima 不是同一数量 |
| 刺激时序 | 单通道速率、总脉冲率、顺序／成对／事件触发、双耳同步 | “高采样率”不说明各通道实际何时发放 |
| 空间与电映射 | 电流导向、聚焦、幅度或脉宽映射、个体阈值与舒适水平 | 虚拟刺激位置不等于独立神经信息通道 |
| 系统和评价 | 处理延迟、功耗、兼容型号、训练时间、测试材料 | 一种语言的句子收益不能代表音乐、声调和定位收益 |

这套分类用于阅读和比较算法，不是厂商排名。[通道相互作用](../channel-interaction/)及[频位映射关系](../tonotopy/)决定算法输出怎样进入神经系统，因此只比较输入频谱或声学重建分数不够。[1](#ref-zeng-2008)

## 临床常用策略：从公式读到代码

以下以 **CIS／HDCIS、ACE、FSP／FS4、HiRes／Fidelity120** 四个临床策略家族为主线。“常用”在这里指临床处理链中有代表性的策略家族，不表示已取得各地区使用率排名。SPEAK、MP3000 及国产策略的版本目录见后文。这里的公式是用于解释公共机制的教学模型，具体商用滤波器、压缩函数与调度需看指定设备文档。[1](#ref-zeng-2008)[2](#ref-ci-cochlear-cs61)[6](#ref-ci-medel-maestro11)[7](#ref-ci-ab-target)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/01-workflow.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/01-workflow.svg" alt="声音分频、包络、映射及 CIS、ACE、精细结构、电流导向分支的流程图" loading="lazy" /></a>
  <figcaption>图 1｜公共处理操作与四类策略差异。ACE 先按增益后的特征选择 maxima，再做个体电映射；零交叉和频谱位置另从分析信号提取。图中各分支不是同一软件的可互换模块。</figcaption>
</figure>

### 公共前端：分频、包络与强度压缩

设 $x[n]$ 为离散声音波形，采样率为 $f_s$；$i=1,\ldots,m$ 为从低频到高频排列的分析通道。教学模型采用带通滤波、全波整流和低通：

$$
y_i[n]=(h_i*x)[n],\qquad a_i[n]=\max\{0,(h_{\rm LP}*|y_i|)[n]\}.
$$

$h_i$ 为第 $i$ 个带通滤波器，$h_{\rm LP}$ 为包络低通滤波器，$*$ 是卷积。取最大值是数值保护，抑制低通瞬态可能产生的微小负值。包络不携带完整的带通相位；它仍可包含声带振动造成的周期性。其他实现可能用 FFT 频带能量或解析信号幅度估计包络，不能仅凭这条公式认定与 ACE 的商业分析器等价。[1](#ref-zeng-2008)[18](#ref-ci-pulsatile-code)

声音的声级范围需要压缩到较窄的电动态范围。一个可运行的无量纲模型为

$$
L_i[n]=20\log_{10}\max\left(\frac{a_i[n]}{a_{\rm ref}},10^{-12}\right),\quad
u_i[n]=\operatorname{clip}\left(\frac{L_i[n]-L_{\min}}{L_{\max}-L_{\min}},0,1\right),
$$

$$
g(u)=\frac{\ln(1+\mu u)}{\ln(1+\mu)},\qquad
I_i[n]=T_i+(C_i-T_i)g(u_i[n]).
$$

$a_{\rm ref}$ 是固定参考幅度，$L_{\min},L_{\max}$ 是相对参考的输入边界，$\mu>0$ 控制压缩曲线；这些相对 dB **未经校准不能写成 dB SPL**。$T_i,C_i$ 分别表示该电极的阈值和舒适上界；有些系统使用 M 等名称和不同标度。最后一式只说明一种映射形式，不能将厂商的 CL 数值直接当作 µA。低于输入门限时是否停发脉冲需要另定义，不能一概把静音映射成持续的 $T_i$ 刺激。[2](#ref-ci-cochlear-cs61)

```python
# env: 通道 × 声音采样点；输出为 0–1 的相对幅度
level = 20 * np.log10(np.maximum(env / 0.25, 1e-12))
u = np.clip((level + 50) / 50, 0, 1)
relative_amplitude = np.log1p(20 * u) / np.log1p(20)
```

这段代码对应下载脚本的 `compress()`，固定参考为 0.25、输入范围为 −50 到 0 dB、$\mu=20$，没有个体 $T/C$。为每个文件重新除以它自己的峰值会消除文件间声级差异，不适合比较不同输入强度。

### CIS／HDCIS：固定通道，交错发放

CIS（连续交错采样）的核心是：在所有启用通道上用包络调制脉冲幅度，各通道错开发放，减少同时刺激造成的直接电场叠加。交错不能消除神经兴奋扩散和所有通道相互作用。HDCIS 是 MED-EL 的具体家族实现，不等同于所有通用 CIS 仿真。[31](#ref-wilson-1991)[6](#ref-ci-medel-maestro11)

设每轮刺激 $K=m$ 个通道，轮次率为 $r$（轮/s），$\pi_j(q)$ 为第 $j$ 轮中第 $q$ 个发放的通道；对称双相的单相宽为 $\tau$，相间隔为 $g$，额外保护间隔为 $\delta$：

$$
\Delta=2\tau+g+\delta,\qquad
t_{j,q}=\frac{j}{r}+q\Delta,\quad q=0,\ldots,K-1,\qquad K\Delta\le\frac1r.
$$

在每轮每通道一个脉冲、全部按顺序发放的这个模型里，单通道速率是 $r$，总事件率为 $mr$。$f_s$ 是声音采样率，不能与它们混用。教学例取 $m=8,r=800$、$\tau=25$ µs、$g=8$ µs、$\delta=0$，每事件占 58 µs，一轮需 464 µs，可容纳于 1.25 ms 周期。实际设备还会受遥测、输出合规电压、保护间隔等约束，不能据这一不等式反推临床可设参数。

```python
# env 是已提取的包络；M=8；各轮按低频到高频发放
cis_events = schedule(env, n=M, fs=24000, rate=800)
```

`schedule()` 保存 `[time_s, channel_zero_based, relative_amplitude]`。这里零幅度事件只是模型中的占位，CSV 不含任何硬件协议。通道顺序低到高也是教学约定，不是所有处理器的固定顺序。

### ACE：先选 maxima，再按位置安排脉冲

ACE（先进组合编码器）在每轮从 $m$ 个候选分析通道中选 $N$ 个较强通道；CIS 使用固定启用通道。设通道增益为 $w_i$，选择特征为 $v_i[j]=w_i a_i[n_j]$：

$$
\mathcal S_j=\underset{\mathcal S\subseteq\{1,\ldots,m\},\ |\mathcal S|=N}{\arg\max}
\sum_{i\in\mathcal S}v_i[j],\qquad n_j=\left\lfloor\frac{jf_s}{r}\right\rfloor.
$$

也就是每轮取最大的 $N$ 个值。实际 ACE 的分析和特征定义比这个简化式更具体。官方手册明确：通道增益在 maxima 选择之前施加，能够改变选中结果。**按强弱选通道不意味着按强弱顺序发放**；选出的集合还要按调度规则排列。[2](#ref-ci-cochlear-cs61)[3](#ref-ci-cochlear-guidance)

```python
# 单帧选择：同值时先取较小索引，再按电极位置排序
chosen = np.sort(np.argsort(-v, kind='stable')[:N])
# 下载脚本默认通道增益均为 1，采用 8 选 4
ace_events = schedule(env, n=4, fs=24000, rate=800)
```

例如 $v=[0.2,0.8,0.5,0.1]$，取 $N=2$ 会选教学通道 2 和 3。在本模型中，总事件率为 $Nr$；某个电极只有被选中时才发放，其长期实际事件率可以低于 $r$。将 maxima 从 8 改成 4 后若保持轮次率不变，总事件数减半，不能据此声称响度和功耗也恰好减半。

SPEAK 与 ACE 都有谱峰选择思想，但分析、速率及设备实现不同。MP3000 将掩蔽模型纳入选择，已选通道可改变其余通道的评价；因此把上面的 `argsort` 或 `N` 改一下不足以实现 MP3000。[5](#ref-ci-mp3000-2011)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/03-electrodograms.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/03-electrodograms.svg" alt="相同合成输入下，包络热图与 CIS 全通道、ACE 八选四刺激事件图的对比" loading="lazy" /></a>
  <figcaption>图 2｜同一输入、相同前端和轮次率的可复现比较。上图是连续包络；下两图是实际生成的事件起点。颜色表示相对幅度，零幅度占位仍保留。展示 40–52 ms 片段；完整 120 ms 记录中，CIS 有 768 个候选事件，ACE 有 384 个。</figcaption>
</figure>

### FSP／FS4：用低频零交叉控制刺激时刻

FSP 和 FS4 家族除包络幅度外，还从低频分频波形提取时间线索：以零交叉触发通道特异采样序列 CSSS，其余通道沿用包络编码。FS4 扩展相应低频通道，FS4-p 允许兼容硬件上的并行安排。它们改变了部分通道的时刻规则，不能理解为“在 CIS 后面恢复所有精细结构”。[6](#ref-ci-medel-maestro11)

对上行零交叉，若 $y_i[n]<0\le y_i[n+1]$，线性插值给出

$$
\widehat t_{i,k}=\frac1{f_s}\left(n-\frac{y_i[n]}{y_i[n+1]-y_i[n]}\right).
$$

```python
idx = np.flatnonzero((y[:-1] < 0) & (y[1:] >= 0))
frac = -y[idx] / (y[idx + 1] - y[idx])
crossing_times = (idx + frac) / fs
```

对于单一 300 Hz 正弦，相邻上行零交叉间隔约为 3.33 ms；固定 800 次/s 的脉冲则相隔 1.25 ms。这个对照说明“事件时刻由波形决定”的含义。复杂声音的通道零交叉不必等于基频；噪声、带宽和失真也会改变交叉。

**这里仅实现零交叉时刻提取，不是完整 FSP／FS4 编码器。** CSSS 是采样序列，不能总以“每个零交叉一个脉冲”替代；真实实现还需序列内脉冲、幅度采样、速率上限、跨通道冲突处理，以及 FS4-p 的并行约束。下载脚本不会把这些单通道时刻直接并入 CIS 事件表。

### HiRes／Fidelity120／Optima：从幅度编码到电流导向

基础 HiRes 以高速包络编码为主，S/P 区别涉及顺序或成对安排；Fidelity120 进一步利用相邻电极联合刺激改变空间位置。Optima 是相关家族的功耗优化版本，不能仅用电流导向公式声称实现完整 Optima。[7](#ref-ci-ab-target)[11](#ref-ci-ab-optima-fda)

用相邻两电极 $E_i,E_{i+1}$ 说明电流分配。设总幅度为 $I$、权重为 $\alpha\in[0,1]$：

$$
I_i=(1-\alpha)I,\qquad I_{i+1}=\alpha I,\qquad I_i+I_{i+1}=I.
$$

当 $\alpha$ 从 0 变为 1，分配由一侧电极转到另一侧。频谱峰位置可用于产生权重，但真实算法还要限定导向范围、映射两电极阈值和舒适水平，并考虑载波、整流和调度。GPyT 的 `f120Mapping.py` 展示分别映射再乘权重，`f120Electrodogram.py` 展示相邻电极在同一刺激时隙的波形构造；它比这个总幅度守恒例子复杂。[10](#ref-ci-gpyt-code)

```python
def steering(amplitude, alpha):
    return (1 - alpha) * amplitude, alpha * amplitude

# 同一时刻两电极分担相对幅度 0.8：分别为 0.6 和 0.2
left, right = steering(0.8, 0.25)
```

两电极同时刺激形成的空间兴奋不等于两个完全独立通道；权重也不必与感知音高或解剖距离线性对应。“120”表示策略的空间编码设计，不能读成 120 个物理接触点或 120 个独立可分辨神经通道。[1](#ref-zeng-2008)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/04-timing-steering.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/04-timing-steering.svg" alt="低频零交叉、固定与事件时序、相邻电极电流分配、对称双相波形四幅教学图" loading="lazy" /></a>
  <figcaption>图 3｜时间编码与空间编码分别解决“何时发放”和“在哪里形成兴奋”。零交叉图仅展示事件线索；导向图仅展示权重；双相图使用无量纲幅度，正负极性是数学约定。</figcaption>
</figure>

### 怎样读电极位置图和电极刺激图

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/02-electrode-array.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/02-electrode-array.svg" alt="耳蜗内电极阵列及展开位置图，标明基底高频、顶端低频和单极模式的耳蜗外回流电极" loading="lazy" /></a>
  <figcaption>图 4｜原创电极示意图，不按解剖比例。本文用 E1→E8 统一表示低频到高频的教学顺序，代码用 0→7；厂商真实编号方向可能不同。频率分配表、电极插入深度和个体神经状态共同影响频位对应，不能只按编号推断音高。[1](#ref-zeng-2008)</figcaption>
</figure>

**电极位置图**说明接触点在哪里；**electrodogram（电极刺激图）**以时间为横轴、电极为纵轴，说明什么时候、在哪个位置、用多大幅度发放。连续包络热图只显示特征；图 2 的短竖线显示事件起点，但仍未展开每一相。需要判断电荷或同时刺激时，应读取事件表或有符号电流波形。

对起点为 $t_k$、幅度为 $I_k$ 的理想对称双相脉冲，令局部时间 $u=t-t_k$：

$$
b_k(u)=\begin{cases}
I_k,&0\le u<\tau,\\
0,&\tau\le u<\tau+g,\\
-I_k,&\tau+g\le u<2\tau+g,\\
0,&\text{其他时刻},
\end{cases}
\qquad \int b_k(u)\,du=0.
$$

这是净电荷为零的理想矩形波形。若 $I_k$ 用 A、$\tau$ 用 s，则单相电荷 $Q=I_k\tau$ 用 C；脚本使用相对幅度，因此不能把计算面积标成实际电荷。净电荷为零也不能替代电荷密度、合规电压、电极状态等真实设备检查。Neuro 的时长调制伪单相波形更不能直接用这一对称模型替代。[1](#ref-zeng-2008)[12](#ref-ci-neuro2-specs)

### 下载并运行同一教学算例

<a href="/n3-hearingpedia/code/ci-coding/teaching_encoder.py" download="teaching_encoder.py">下载完整 Python 教学脚本</a>。依赖 Python、NumPy 和 SciPy，输入是固定合成声音；不需要患者 MAP，不连接任何设备。

```bash
python -m pip install numpy scipy
python teaching_encoder.py --out ci-demo
```

输出包括 `teaching-data.npz`、`cis-events.csv`、`ace-events.csv` 和 `checks.json`。脚本采用 24 kHz 声音采样率，8 个 200–6000 Hz 对数分布频带，三阶 Butterworth 带通、全波整流、200 Hz 二阶包络低通；各滤波器均为零初始状态的因果单向处理，未实现流式分块接口，也没有商品前端 AGC。三阶带通原型经带通变换后实际为六阶。120 ms 输入产生 96 轮选择，CIS 为 8×96=768 个候选事件，ACE 为 4×96=384 个。

脚本内置检查覆盖峰值选择与同值规则、事件无重叠、压缩边界、双相面积抵消、导向权重和，以及纯音零交叉间隔；不把这些算法检查当作医疗设备安全验证。图 2、图 3 的数值均由同一代码生成。第三方商用策略仿真及其许可另见后面的仓库表；本教学脚本仅实现公共机制和局部示例，**没有实现商用 HDCIS、ACE、FS4 或 HiRes120 的完整等价编码器**。


## 临床策略的官方目录与比较

下表按厂商分别列出策略，避免把同名 CIS 在不同设备中的实现视为完全一致。**“文档列明”表示指定版本具有该名称，不表示所有在售设备、全部地区或所有使用者均能选择。** 仿真栏的“未核实专用公开实现”是此次检索结果，不是断言代码绝对不存在。

### Cochlear：CIS、SPEAK、ACE 与 MP3000

官方介绍入口：[Custom Sound 6.1 用户指南](https://assets.cochlear.com/api/public/content/4b2f503b6edf48ff9dfdadcbd9beb205?v=7476e383)，以及原厂[临床指南 1.9 节](https://www.gaesmedica.com/es-es/uploads/imgen/372-guia-clinica-de-programacion.pdf?1600874874=)。后一文件是分销商托管的旧版指南，其通道数和速率不能直接当作当代默认配置。[2](#ref-ci-cochlear-cs61)[3](#ref-ci-cochlear-guidance)

| 策略 | 核心规则 | 版本与应用范围 | 对应仿真代码 |
| --- | --- | --- | --- |
| **CIS**，Continuous Interleaved Sampling，连续交错采样 | 以包络控制刺激幅度；每周期依次刺激固定的启用通道 | 官方旧版同时使用 CIS(RE) 名称；可选组合由设备和软件决定 | [Pulsatile Vocoder](https://github.com/mohead/pulsatile-vocoder)：研究 CIS，非商用逐位等价 |
| **SPEAK**，Spectral Peak | 每帧选择较强的谱峰通道；经典实现采用较低的每通道刺激速率 | 在旧植入体兼容目录中仍列明；不能仅因提出较早就归为已停用 | 未核实专用公开实现；ACE 仿真不能直接改名为 SPEAK |
| **ACE**，Advanced Combination Encoder，先进组合编码器 | 结合谱峰选择和交错脉冲；从候选频带选择 maxima，按 MAP 映射 | 旧版有 ACE(RE) 标签；2026 Nexa 对照资料列明 ACE | [Pulsatile Vocoder](https://github.com/mohead/pulsatile-vocoder)；[CCi-MOBILE](https://github.com/CILabUTD/CCi-MOBILE)，覆盖层次见代码表 |
| **MP3000**／PACE 相关实现 | 将假设的掩蔽影响纳入通道选择，以减少冗余刺激；不只是选最大能量 | 2026 官方评估的旧植入体兼容一列仍列明；不是 Nexa 植入体的通用选项 | 未核实商用 MP3000 的专用公开实现 |

法国 HAS 2026 年 1 月的 CP1110 对照表必须按列阅读：**Nexa 植入体组合为 ACE；CI24M、CI24R/RE、CI500、CI600 兼容组合为 ACE、CIS、SPEAK、MP3000。** 同一个处理器外观或型号名不意味着植入体组合支持相同策略。MP3000 的机制依据来自原始临床论文，支持目录来自官方评估；二者承担不同证据用途。[4](#ref-ci-has-nexa-2026)[5](#ref-ci-mp3000-2011)

Custom Sound 手册还明确区分：ACE、SPEAK、MP3000 在 maxima 选择前施加通道增益，因而增益可以改变被选通道；CIS 每帧刺激所有启用通道，增益主要改变输出水平。比较策略时，频率分配和通道增益必须同时记录。[2](#ref-ci-cochlear-cs61)

### MED-EL：HDCIS 与精细结构系列

官方介绍入口：[MAESTRO 11 手册 24.5.2–24.5.3](https://download.cdn.medel.com/assets/AW44981_10_User-Manual-MAESTRO-11-EN-English_web.pdf)，印刷页 345–346（PDF 页 347–348）。[6](#ref-ci-medel-maestro11)

| 策略 | 核心规则 | 官方兼容／时序说明 | 对应仿真代码 |
| --- | --- | --- | --- |
| **HDCIS**，High Definition CIS | 提取各电极对应滤波输出的包络 | MED-EL 的 CIS 家族实现 | 未核实专用商用等价实现；[通用研究 CIS](https://github.com/mohead/pulsatile-vocoder)仅可作原理参照 |
| **FSP**，Fine Structure Processing | 低频通道用零交叉触发 CSSS，其余采用 HDCIS | 精细结构通道数及覆盖范围依赖个体参数 | 未核实专用公开实现 |
| **FS4** | 扩展 CSSS 覆盖，改善事件时间精度 | 12 个启用通道时最多 4 个 CSSS 通道；顺序刺激 | 未核实专用公开实现 |
| **FS4-p** | 沿用 FS4 表征，允许 CSSS 通道同时刺激 | 并行刺激限于兼容植入体；需要处理相互作用 | 未核实专用公开实现 |
| **CIS+** | HDCIS 的前身，原理相近、采样较慢 | 手册明确为 **TEMPO+ 专用旧设备兼容策略** | 未核实该版本的专用公开实现 |

CSSS 是 channel-specific sampling sequences（通道特异采样序列）。FineHearing 等家族名称应与 FSP／FS4 的具体算法区分；使用精细结构的电极序列也不意味着恢复了正常耳蜗的全部相位信息。[6](#ref-ci-medel-maestro11)

### Advanced Bionics：HiRes、Fidelity120 与 Optima

官方介绍入口：[Target CI 归档验配指南](https://www.advancedbionics.com/content/dam/advancedbionics/ifus/in/archived/029-M826-02_TargetCI_FittingGuide_TUV_Rev-D_EN.pdf)和[原厂 eIFU 目录](https://www.advancedbionics.com/ifu/us/en)。Q90 的旧技术规格仍可通过官方搜索索引核对策略名称，但原下载地址已返回 404，因此此处提供可访问的原厂目录。[7](#ref-ci-ab-target)[8](#ref-ci-ab-legacy-specs)[9](#ref-ci-ab-ifu)

| 策略／变体 | 核心规则与差别 | 临床目录范围 | 对应仿真代码 |
| --- | --- | --- | --- |
| **HiRes-S / HiRes-P**，HiResolution | 高速包络编码；S 为 sequential（顺序），P 为 paired（成对）刺激 | Target CI 指南与旧 Q90 资料列明；S/P 是刺激安排的区别 | 未核实基础 HiRes 两变体的完整公开等价实现 |
| **HiRes-S with Fidelity120 / HiRes-P with Fidelity120** | 在相邻电极间电流导向，以更多可配置刺激位置表征频谱 | 旧 Q90 目录及 Target CI 文档列明 S/P 变体 | [GPyT](https://github.com/jabeim/AB-Generic-Python-Toolbox)明确模拟 **HiRes120**；不保证两种调度和商用全部功能均等价 |
| **HiRes Optima-S / HiRes Optima-P** | Fidelity120 家族的功耗优化版本 | FDA 2013 年补充批准；具体设备／地区仍看相应说明 | 未核实 Optima 两变体的专用公开实现；不能把 GPyT 直接标为 Optima |
| **CIS** | 传统交错包络编码 | Q90 旧规格列明的兼容模式；不能自动外推至新处理器 | [研究 CIS](https://github.com/mohead/pulsatile-vocoder)，非 AB CIS 等价证明 |
| **MPS**，Multiple Pulsatile Sampler | 传统多通道脉冲采样模式 | Q90 旧规格的兼容策略；需核对具体处理器和验配版本 | 未核实专用公开实现 |

Fidelity120 中的“120”不能解释为 120 个独立电极或 120 个可独立分辨的神经通道。电流导向改变相邻电极间的电流分配，其感知收益受电极位置和兴奋扩散限制；GPyT 的映射和 electrodogram 模块可用于观察这一研究模型。Optima 的官方批准资料明确涉及功耗优化，不构成对所有听觉任务的优效证据。[10](#ref-ci-gpyt-code)[11](#ref-ci-ab-optima-fda)[1](#ref-zeng-2008)

### Neurelec／Oticon Medical：MPIS 与 Crystalis

官方介绍入口：[Neuro 2 产品资料 Version C](https://assets-we.cas.dgs.com/uk/-/media/medical/main/files/ci/products/neuro-2/pi/eng/183342uk_pi_neuro-2_version-c_2019-09_low.pdf?la=en)，PDF 页 7。该系列属于既有系统目录；Cochlear 于 2024 年完成 Oticon Medical 人工耳蜗业务收购。[12](#ref-ci-neuro2-specs)[13](#ref-ci-cochlear-ciom)

| 策略／变体 | 核心特点 | 官方目录与公开程度 | 对应仿真代码 |
| --- | --- | --- | --- |
| **MPIS CAP / MPIS XDP**，Main Peak Interleaved Sampling | MPIS 是主要谱峰交错采样家族 | Neuro 2 正式列明两个名称；后缀不能被当作独立临床效果证明 | 未核实专用公开实现 |
| **CRYSTALIS CAP / CRYSTALIS XDP** | Crystalis 家族；XDP 研究资料描述谱线索处理与多频带输出压缩 | Neuro 2 正式列明两个名称；本文不根据后缀补写未公开算法 | 未核实专用公开实现；论文使用的厂内 MATLAB 程序未公开仓库 |

这一系统的资料描述**时长调制的伪单相脉冲及被动放电**，不能套用所有系统都以固定脉宽改变电流幅度的模型。CrystalisXDP 的原始音乐研究报告部分任务收益，但不能推出所有音乐维度或语音任务均改善。VoiceTrack、VoiceGuard 和方向性功能应另外记录。[12](#ref-ci-neuro2-specs)[14](#ref-ci-neuro-music-2022)

### 诺尔康：CIS、APS、C-Tone 与 Symphony

官方介绍入口：[高歌 Enduro 产品画册](https://www.nurotron.com/uploads/20230530/64759ae167fce.pdf)，PDF 页 9；算法背景参照原厂托管的[系统开发论文 2.1 节](https://www.nurotron.com/uploads/20230524/646d5afb315d8.pdf)。[15](#ref-ci-nurotron-enduro)[16](#ref-ci-nurotron-design-2015)

| 策略 | 核心特点 | 官方资料的边界 | 对应仿真代码 |
| --- | --- | --- | --- |
| **CIS** | 对固定的可用通道进行分析与交错刺激 | 2015 系统论文及 Enduro 画册列明 | [研究 CIS](https://github.com/mohead/pulsatile-vocoder)可作原理参照，非诺尔康版本等价实现 |
| **APS** | 依据频带能量进行峰值选择，属于 n-of-m 相关设计 | 2015 论文给出最多 24 个分析通道的示例；不能等同为 Cochlear ACE | 未核实 APS 专用公开实现 |
| **C-Tone** | 官方画册列出的编码策略名称 | 未取得完整公开算法说明，不据名称断言具体基频提取或刺激规则 | 未核实专用公开实现 |
| **Symphony** | 将虚拟通道／相邻电极联合刺激与谱峰提取结合 | 原厂系统论文描述机制，Enduro 画册列明名称 | 未核实专用公开实现 |

论文中的随访效果来自 APS，不是 CIS、APS、Symphony 的随机比较。Enduro 目录也不能自动覆盖后续所有 3.0 型号。eVoice 在画册中单列为降噪处理，不应另算一种编码策略。[16](#ref-ci-nurotron-design-2015)[15](#ref-ci-nurotron-enduro)

### 力声特：L-CIS 与 MTone

官方介绍入口为[上海力声特官网](http://www.shlst.com.cn/)；当前可检索文字目录见署名为厂商的[“臻听”展商介绍](https://www.crexpo.cn/exhibition/product/2306)。后者属于产品介绍，**不是详细算法手册**。[17](#ref-ci-listent-catalog)

| 策略 | 厂商介绍明确的信息 | 尚未公开核实的内容 | 对应仿真代码 |
| --- | --- | --- | --- |
| **L-CIS** | 通用编码策略名称 | 与其他 CIS 实现的精确参数对应及型号兼容矩阵 | 未核实专用公开实现；通用 CIS 仿真仅作基线 |
| **MTone** | 针对汉语四声设计的策略名称 | 基频提取、包络修饰、脉冲时序等完整算法及独立效果证据 | 未核实专用公开实现 |

MTone 的设计目标涉及[普通话汉语声调](../mandarin-lexical-tone/)，但商品名称和宣传文字不足以证明它怎样编码[基频](../fundamental-frequency/)。MTone 与诺尔康 C-Tone 也不能仅因名称相关就认定是同一策略。

### 历史策略和容易混入目录的名称

早期特征提取策略包括 F0/F2、F0/F1/F2、MPEAK；压缩模拟 CA、同时模拟刺激 SAS 等属于发展史。它们帮助解释从显式语音特征到多频带包络编码的演变，不能在缺少当代型号手册时写成当前常规可选项。爱益声等系统本次未取得足以核对的现行官方策略清单，保留为目录缺口。[1](#ref-zeng-2008)

ADRO、ASC、SCAN、ForwardFocus、ClearVoice、SoftVoice、VoiceTrack、eVoice 等涉及增益、场景、方向性或降噪，应作为配置记录，不能各自计为与 ACE 或 FS4 平行的刺激编码策略。EAS／Hybrid 表示电声联合刺激模式，ABF 表示解剖信息参与验配；二者也不是单一声音编码算法。临床比较必须同时报告这些配套条件。[4](#ref-ci-has-nexa-2026)[7](#ref-ci-ab-target)[12](#ref-ci-neuro2-specs)[15](#ref-ci-nurotron-enduro)

## 可用的仿真代码与复现入口

### 已核实仓库及其实际覆盖

核验包括 README、许可文件和关键目录，**未在本次环境安装、运行或训练第三方程序**。下表只承诺仓库和覆盖说明已核对。声学[声码器](../vocoder/)输出、electrodogram（电极刺激图）和真实硬件输出是三个不同层次。

| 仓库 | 明确覆盖／入口 | 输出层次 | 许可、局限与适合的用途 |
| --- | --- | --- | --- |
| [Pulsatile Vocoder](https://github.com/mohead/pulsatile-vocoder) | ACE、CIS；`CI_Sim.m`，`CI_CODING_STRAT/` | 电刺激模型和可听声学模拟 | **MIT**；作者明确是概念实现，不保证等价商用策略；适合峰值数量、速率及兴奋扩散的教学比较 |
| [CCi-MOBILE](https://github.com/CILabUTD/CCi-MOBILE) | MATLAB `ACE_Process.m`／`initialize_ACE.m`，Android `ACE.java` | 研究处理器与设备通信链 | 部分安全函数为受保护 `.p`，未检出顶层统一许可；适合理解 ACE 研究接口；不可宣称全套代码完全开放 |
| [AB Generic Python Toolbox](https://github.com/jabeim/AB-Generic-Python-Toolbox) | HiRes120；`RunDemos.py`、`pipelineTemplate.py`、`f120Mapping.py`、`f120Electrodogram.py` | `Results['elGram']` 及声码器再合成 | **GPL-3.0**；研究移植、老版本 Python／NumPy／SciPy 依赖；不能代表完整 HiRes Optima S/P |
| [DeepACE 1.0](https://github.com/APGDHZ/DeepACE) | 原始音频 → 学习的去噪编码；Python／TensorFlow | 研究模型的电刺激表征 | **GPL-3.0**；早期版本，实验及训练配置与 2.0 不同 |
| [DeepACE 2.0](https://github.com/APGDHZ/DeepACE2.0) | 端到端 ACE 表征与去噪；`main.py`、`model.py`、`requirements.txt` | 去噪 electrodogram 研究模型 | 仓库公开，但本次未检出许可文件；应与 2023 期刊论文及附带学位论文分别阅读 |
| [Spiking Deep ACE](https://github.com/NECOTIS/spiking-deep-ace) | `models/spiking_deep_ace.py`、`ace/`、`train.py`、`evaluate.py` | 脉冲神经网络预测的编码表征与客观指标 | 作者论文直接链接；PyTorch；未检出许可文件，未核实已训练权重或临床硬件输出链 |

前三个仓库对应临床策略的**研究实现或研究平台**，后三项属于实验算法。没有查到专用实现的策略，应使用上方“未核实”标记，而不是填入不相关仓库。[GET 声码器](../get-vocoder/)等再合成方法能比较感知假设，却不能凭输出 WAV 文件证明实现了某个厂商编码器。[18](#ref-ci-pulsatile-code)[19](#ref-ci-ccimobile-code)[10](#ref-ci-gpyt-code)[20](#ref-ci-deepace-code)[32](#ref-ci-spiking-code)

### 怎样建立可复现的比较

先固定原始输入及其声级，再分别保存前端处理输出、各频带特征、被选通道和刺激序列。至少记录仓库提交版本、采样率、频率分配表、帧长与步长、maxima、包络截止频率、刺激速率、相宽、个体映射和声码器模型。仓库提供的“默认参数”只是该实现的起点，不是临床统一标准。

如果研究问题是峰值选择，比较时应尽量固定前端和电映射；如果研究问题是时域精细结构，应检查时序输出而不只检查频谱；如果研究问题是双耳编码，应同时检查通道匹配、脉冲同步、[ITD](../interaural-time-difference/)和 ILD。人类实验还须记录响度平衡、适应期和个体差异。[2](#ref-ci-cochlear-cs61)[21](#ref-ci-mixed-itd-2025)

## 研究策略与当前前沿

以下十三个方向包含持续发展的较早研究和 2025–2026 年进展。**“植入者实验”不等于“临床常规采用”；“仿真改善”也不等于“植入者感知改善”。** 本表以原始论文为依据，未把普通前端降噪网络或 AI 验配模型直接算成新编码策略。

| 方向／策略 | 改变哪个编码环节 | 已有证据及边界 | 论文／代码入口 |
| --- | --- | --- | --- |
| **TLE：时域限制编码器** | 根据时域限制组织包络和脉冲时间，改善可用周期性线索 | 2022 年有真实 CI 使用者的音高任务；效果须按频率与任务解释 | [TLE 词条](../temporal-limits-encoder/)；[原始论文](https://pubmed.ncbi.nlm.nih.gov/36044501/)；未核实专用公开仓库 |
| **F0inTFS** | 利用低频信息增强谱峰通道中的时域周期性 | 2023 年论文是正常听力者声码器验证；不是植入者试验 | [F0inTFS 词条](../f0-in-tfs/)；[论文全文](https://www.isca-archive.org/interspeech_2023/zhou23c_interspeech.html)；未核实专用公开仓库 |
| **DeepACE** | 把 ACE 表征与去噪联合为音频到 electrodogram 的端到端模型 | 2023 年 8 名 CI 使用者的噪声语音实验有收益；未建立全场景、长期效果 | [期刊论文](https://pubmed.ncbi.nlm.nih.gov/37030808/)；[1.0](https://github.com/APGDHZ/DeepACE)／[2.0](https://github.com/APGDHZ/DeepACE2.0) |
| **Fused DeepACE／双耳潜在表征融合** | 双侧编码模型通过 latent fusion 共享信息 | 2024 年有客观指标和双侧 CI 使用者语音结果；完整双耳公开实现仍待核实 | [期刊论文](https://pubmed.ncbi.nlm.nih.gov/38376983/)；单耳 DeepACE 仓库是相关基线，不能冒充完整双耳版本 |
| **ElectrodeNet／ElectrodeNet-CS** | 学习包络计算，进一步嵌入 maxima 选择 | 正式论文／作者稿报告客观指标和正常听力者声码器普通话句子结果 | [作者稿与正式 DOI](https://arxiv.org/abs/2305.16753)；未核实作者公开仓库 |
| **AVSE-ECS：视听联合编码** | 将视觉辅助语音增强与 ElectrodeNet-CS 联合训练 | 2026 年 JASA Express Letters 为仿真和客观指标；未证明 CI 使用者收益 | [作者稿 v2 与期刊 DOI](https://arxiv.org/abs/2508.13576)；未核实对应公开仓库 |
| **混合速率＋显式 ITD 的双耳同步编码** | 结合不同脉冲速率，将双耳时间线索显式写入刺激 | 2025 年输出 ITD 更准确，但短期自由场定位**未改善** | [原始全文](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1682452/full)；[CCi-MOBILE 平台](https://github.com/CILabUTD/CCi-MOBILE)，具体研究补丁未核实 |
| **BACE／双耳联合谱峰选择** | 协调两耳峰值选择与相应刺激通道 | 2026 年 9 名双侧使用者运动跟踪中，谱峰同步本身无效应；硬件同步有小范围收益 | [原始摘要](https://pubmed.ncbi.nlm.nih.gov/42422910/)；CCi-MOBILE 为研究平台，不保证包含论文算法 |
| **MOC 仿生双耳动态压缩** | 模拟对侧内侧橄榄耳蜗反馈，耦合两侧频带压缩 | 2016 年小样本植入者研究在特定空间分离噪声条件有收益；不泛化到所有声场 | [原始论文](https://pubmed.ncbi.nlm.nih.gov/26862711/)；未核实完整作者代码仓库 |
| **电流聚焦与个体化空间刺激** | 调整回流和空间兴奋分布，权衡通道分离、响度与刺激需求 | 2026 年原始研究结合使用者实验与模型；不能仅凭兴奋更窄宣称语音改善 | [原始研究](https://doi.org/10.1007/s10162-026-01076-6)；属于刺激设计方向，未核实完整新编码器仓库 |
| **Spiking Deep ACE／低功耗脉冲神经网络** | 将去噪和编码映射转为事件式网络计算 | 2026 年会议研究有客观指标与运算能耗估计；不是植入者行为或处理器续航实测 | [作者全文](https://arxiv.org/html/2608.28493v1)；[作者代码](https://github.com/NECOTIS/spiking-deep-ace) |
| **注意线索引导 electrodogram** | 融合目标说话者注意包络，引导模型生成所关注声音的刺激表征 | 2026 年方法使用由语音构造的**代理注意线索**；不是完整真实 EEG 闭环 | [作者全文与正式会议 DOI](https://arxiv.org/html/2601.22260v1)；未核实对应作者仓库 |
| **语音／音乐源分离的端到端编码** | 对比分离后再编码与直接生成刺激表征 | 2026 年 9 名双侧 CI 使用者研究：端到端语音任务更好，前端音乐欣赏评分更好 | [原始全文](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1696669/full)；未核实该完整研究管线仓库 |

前两项的证据分别见音高植入者研究与 F0inTFS 原始方法。[22](#ref-zhou-tle-2022)[23](#ref-zhou-f0intfs-2023) 神经网络各行的证据分别来自对应论文，ElectrodeNet 与 AVSE-ECS 保留了仿真证据标签。[24](#ref-ci-deepace-2023)[25](#ref-ci-fused-deepace-2024)[26](#ref-ci-electrodenet-2024)[27](#ref-ci-avse-ecs-2026) 双耳和空间刺激各行分别对应原始研究，不以理论目标替代结果。[21](#ref-ci-mixed-itd-2025)[28](#ref-ci-bace-motion-2026)[29](#ref-ci-moc-2016)[30](#ref-guerit-focusing-2026)

### 计算目标与多模态证据

这三项 2026 年研究分别依据作者全文：低功耗结果采用能耗模型，注意引导结果采用代理线索，语音与音乐结果体现不同任务的取舍。它们不能合并成“AI 编码已解决噪声和音乐问题”的结论。[33](#ref-ci-spiking-deepace-2026)[34](#ref-ci-brain-separation-2026)[35](#ref-ci-speech-music-2026)

### 时域信息：提取成功与利用成功

基频估计器可以输出正确的 $F_0$，但转换后的脉冲序列是否保留周期性、该线索是否落在听者可用速率范围，以及它能否支持[音高](../pitch-perception/)或声调识别，仍是独立问题。FSP 的零交叉事件、TLE 的时域组织与 F0inTFS 的周期性增强，分别改变不同环节；不能按“都处理精细结构”就判定等价。[6](#ref-ci-medel-maestro11)[22](#ref-zhou-tle-2022)[23](#ref-zhou-f0intfs-2023)

### 双耳编码：硬件、通道与行为三个层次

2025 年混合速率研究展示了较可靠的 ITD 传递，却没有短期定位收益；2026 年运动研究也未发现同步谱峰选择的独立收益。这意味着应分别测量硬件同步、输出线索和听者利用，而不是仅凭电极图更整齐便宣称空间听觉改善。长期学习、双耳电极对应及优势线索的竞争仍需独立验证。[21](#ref-ci-mixed-itd-2025)[28](#ref-ci-bace-motion-2026)

### AI 编码：目标函数与临床推广

重建 ACE 包络、提高输出信噪比、提高 STOI 或提升句子识别率不是相同目标。DeepACE 有植入者行为数据，而 AVSE-ECS 此处依据的是仿真；两类证据应分开。延迟、视觉输入可得性、未见噪声、非语音声音、双耳线索和个体 MAP 的适用性，都需要在实验设计中明确。[24](#ref-ci-deepace-2023)[27](#ref-ci-avse-ecs-2026)

## 策略评价与分析示例

### 电极刺激图应包含哪些量

一个简化的脉冲事件可表示为：

$$
p_k=(e_k,t_k,I_k,\tau_k,s_k),\qquad Q_k=I_k\tau_k
$$

其中 $e_k$ 为电极或刺激配置标识，$t_k$ 为发放时间（s），$I_k$ 为某一相的电流（A），$\tau_k$ 为该相宽度（s），$s_k$ 标明极性和波形配置；$Q_k$ 是该相电荷量（C）。这个事件模型用于比较算法输出，不是刺激剂量建议。真实记录还需保存相间隔、回流电极、并行事件以及设备校验信息；一幅包络热图可能没有这些信息。[1](#ref-zeng-2008)[12](#ref-ci-neuro2-specs)

### 一个通道选择的教学例子

假设一帧有 $m=12$ 个分析频带。研究 CIS 模型可按固定顺序发放 12 个通道；研究 ACE 模型若设 $n=8$，则根据该帧特征选择 8 个通道。这里的 12 和 8 是**教学假设**，不是任何厂商的统一配置。

比较时至少查看四件事：保留的频带信息是否改变；总脉冲数和调度周期是否相同；幅度映射是否一致；改变 maxima 后响度是否发生变化。若另一策略加入掩蔽模型、电流导向或事件触发，只有“选了几个通道”还不能解释差异。[2](#ref-ci-cochlear-cs61)[5](#ref-ci-mp3000-2011)

### 感知评价与合理结论

[言语可懂度](../speech-intelligibility/)和[语音接收阈](../speech-reception-threshold/)评价交流任务；音高排序、普通话声调、旋律和[空间听觉](../spatial-hearing/)需要独立材料。还应考虑延迟、功耗、可靠性及[听觉努力](../listening-effort/)。重复测量中，响度平衡、练习、策略适应、顺序随机化与噪声类型，会影响结果解释。

官方手册最适合证明“这一版本列了什么、怎样设置”；原始临床比较适合证明“特定听者在特定任务发生了什么”；代码适合检验“公开模型到底怎样产生输出”。把这三类证据连接起来，才能评价策略，而不把产品介绍当作跨厂商疗效排名。

## 研究沿革与参见

早期人工耳蜗从语音特征与模拟刺激逐渐发展为多频带包络和脉冲编码。1991 年 CIS 原始研究是重要节点，此后形成谱峰选择、事件触发精细结构、电流导向及个体映射等路线。近年的变化包括双耳共同处理、神经模型与机器学习直接生成刺激表征。它们并非相互替代的单一进步序列：算法目标、硬件约束和评价任务各不相同。[31](#ref-wilson-1991)[1](#ref-zeng-2008)

相关概念：[人工耳蜗](../cochlear-implant/)、[n-of-m 编码](../n-of-m-coding/)、[时域包络](../temporal-envelope/)、[时域精细结构](../temporal-fine-structure/)、[通道相互作用](../channel-interaction/)、[频位映射关系](../tonotopy/)、[动态范围](../dynamic-range/)、[声码器](../vocoder/)、[时域限制编码器](../temporal-limits-encoder/)、[F0inTFS](../f0-in-tfs/)。

## 附录：算法推导、实现顺序与复现细节

本附录把正文的公共机制展开到能够跟读代码的程度。A–G 对应可下载的 `teaching_encoder.py`；H、I 说明它仅实现了哪些局部操作；J 补充其他策略的算法边界；K 给出复现实验与输出核查方法。全部数值算例均为教学设定。临床策略的名称、兼容范围和证据仍以正文目录及其引用为准，不能用本附录替代商用编码器规范。

每节末尾配有附图 A–K，可按“数组 → 分频 → 包络 → 压缩 → 选择 → 调度 → 波形 → 时间线索 → 空间权重 → 掩蔽选择 → 输出核查”的顺序阅读；点击图像可查看完整 SVG。

### A．先确定索引、单位和数据形状

| 符号／变量 | 含义与形状 | 教学值或约定 |
| --- | --- | --- |
| $x[n]$／`x` | 单声道声音，形状 $(L,)$ | 无量纲；$L=2880$ |
| $f_s$／`FS` | 声音采样率，单位 Hz | 24000 |
| $m$／`M` | 分析通道数 | 8；通道索引由低频到高频 |
| $y_i[n]$／`bands` | 分频波形，形状 $(m,L)$ | 保留有符号波形，用于局部零交叉分析 |
| $a_i[n]$／`env` | 非负包络，形状 $(m,L)$ | 整流、低通后的相对幅度 |
| $r$／`RATE` | 通道选择轮次率，单位轮/s | 800；每 30 个声音样本选一次 |
| $N$／`n` 参数 | 每轮候选事件数 | CIS 为 8；ACE 模型为 4 |
| $j,q$ | 轮次索引、轮内发放位置 | 均从 0 开始 |
| `events` | 事件矩阵，形状 $(J N,3)$ | 每行：起点 s、零基通道索引、相对幅度 |

正文数学中的第 $i$ 通道与代码索引 `i-1` 对应；CSV 的通道 0 对应图中的 E1。`events` 由混合数值构成的 NumPy 数组保存，通道列导出时可能显示为浮点数，读回后应显式转成整数。这里没有存储回流电极、极性、相宽和设备控制字；脉冲波形由全局教学参数另外定义，因此 CSV 不是完整设备指令。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/05-array-to-events.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/05-array-to-events.svg" alt="包络矩阵的一列如何变成四行刺激事件" loading="lazy" /></a>
  <figcaption>附图 A｜先看左图第 1080 个声音样本，再看右图第 36 轮生成的 4 行事件。声音数组列号、轮次编号、事件表行号和电极编号分别计数；这里展示的是同一个实际教学输入的中间量。</figcaption>
</figure>

### B．滤波器组：边界、二阶节与状态

教学频带的边界按几何级数生成：

$$
f_k=f_{\rm lo}\left(\frac{f_{\rm hi}}{f_{\rm lo}}\right)^{k/m},
\quad k=0,\ldots,m,\quad f_{\rm lo}=200\ {\rm Hz},\ f_{\rm hi}=6000\ {\rm Hz}.
$$

相邻频带具有相同频率比，不具有相同 Hz 带宽。代码 `np.geomspace(200, 6000, m + 1)` 生成这些边界，再以每对边界设计一个 Butterworth 带通。它是一套便于观察的分析滤波器组，没有要求各带幅度或能量相加后严格重建输入，也不是厂商的频率分配表。

`butter(3, [lo, hi], btype='bandpass', fs=fs, output='sos')` 中，3 为低通原型阶数，最终带通为六阶。`sos` 每行是一个二阶节的六个系数；把 $a_0$ 归一成 1 后，该节满足

$$
v[n]=b_0u[n]+b_1u[n-1]+b_2u[n-2]-a_1v[n-1]-a_2v[n-2].
$$

多个二阶节依次串联。采用 SOS 可以降低高阶多项式直接实现的数值问题；它并不取消滤波器的群延迟。对应实现可对照 SciPy 官方的 [butter 参数说明](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)和 [sosfilt 状态接口](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.sosfilt.html)。

下载脚本一次处理完整输入，所有滤波器从静止状态启动。改成实时分块时，每个通道的带通状态、包络低通状态都必须跨块保存。单通道的一般状态传递写法是：

```python
# sos 已设计；zi 首次为 np.zeros((len(sos), 2))
y_block, zi = signal.sosfilt(sos, x_block, zi=zi)
# 下一块继续使用返回的 zi，不能再次清零
```

块边界还需维护全局声音样本计数和下一轮选择时间；仅保存滤波器状态，仍不足以复现一次性编码结果。`sosfiltfilt` 会使用双向离线处理，幅度和相位性质也随之改变，不能拿它直接充当此处的实时因果前端。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/06-filterbank-state.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/06-filterbank-state.svg" alt="八个教学带通滤波器频响及分块保留状态与清零状态的差别" loading="lazy" /></a>
  <figcaption>附图 B｜左图展示实际设计的 8 个滤波器，频带之间有重叠；右图在同一个块边界对比是否保留状态。保留状态与连续处理的曲线重合，清零会重新引入启动瞬态。</figcaption>
</figure>

### C．包络：整流、平滑与轮次取样

全波整流令 $z_i[n]=|y_i[n]|$。对幅度为 $A$ 的稳定正弦，整流后一个周期的平均值为 $2A/\pi$，不等于 $A$，也不等于均方根值 $A/\sqrt2$。因此换用 Hilbert 幅度或 RMS 特征后，需要重新核对幅度标定；不能共用同一个参考值就认定输出可比。

脚本在整流之后施加 200 Hz 二阶低通，最后以 `maximum(..., 0)` 保护非负性。截止频率决定包络调制保留的程度，同时伴随时间平滑和延迟；200 Hz 并非“低于 200 Hz 的声音才能通过”，因为这里滤的是整流后的调制变化，而不是原始声频。

第 $j$ 轮在包络数组上的取样位置为

$$
n_j=\left\lfloor\frac{jf_s}{r}\right\rfloor,\qquad A_i[j]=a_i[n_j].
$$

本例 $f_s/r=30$，所以 $n_j=30j$。若比值不是整数，应从全局 $j$ 计算每个取样点，避免对块长度或步长反复四舍五入造成累积漂移。在这个教学组合里，轮次率 800 对应的奈奎斯特频率为 400 Hz，200 Hz 低通提供了部分高频抑制；二阶低通并不是理想抗混叠滤波器，仍需按应用容差检查阻带衰减。随意降低轮次率而保持相同包络滤波器，可能改变输出。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/07-envelope-sampling.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/07-envelope-sampling.svg" alt="分频波形经整流低通后得到包络并按轮次读取" loading="lazy" /></a>
  <figcaption>附图 C｜按从上到下的顺序阅读：有正负号的分频振荡 → 非负整流波形与平滑包络 → 每 1.25 ms 读取一次包络。中间曲线来自因果滤波，时间延迟没有被人为移除。</figcaption>
</figure>

### D．压缩映射：算一个数，再讨论个体 MAP

下载脚本依次进行相对声级变换、截断归一化、对数压缩。以某个通道包络 $a=0.025$ 为例，相对参考 $a_{\rm ref}=0.25$，有 $L=-20$ dB；在 −50 到 0 dB 区间归一后，$u=0.6$。压缩结果是

$$
g(0.6)=\frac{\ln(13)}{\ln(21)}\approx0.8425.
$$

这表示输出达到相对幅度尺度的约 84.25%，并不表示达到舒适响度的 84.25%。若为了演示再假设 $T=0.1,C=0.9$，则 $I=0.1+0.8\times0.8425\approx0.7740$；这两个端点仍是无量纲假设，没有临床电流含义。

压缩函数的斜率为

$$
g'(u)=\frac{\mu}{(1+\mu u)\ln(1+\mu)}>0,\qquad 0\le u\le1.
$$

斜率随 $u$ 增大而减小，所以相同的输入增量在较高水平产生较小输出增量。函数在截断前严格单调，但 `clip` 会使下限以下、上限以上的值分别并为同值。下载代码在 `schedule()` 中预先计算整张 `mapped` 数组，只是计算上的便利：**选通道仍使用原始 `env`，不能改为对截断后的 `mapped` 排序**。否则多个饱和通道会因相同映射值丢失原本的强弱关系。

真实个体 MAP 要区分输入门控、响度增长、各电极阈值和舒适水平、幅度与脉宽的联合约束。尤其要定义 $a$ 低于门限时是停发、输出零幅度占位，还是执行其他规则。下载脚本选择零幅度占位，没有持续发放临床阈值电流。[2](#ref-ci-cochlear-cs61)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/08-compression-example.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/08-compression-example.svg" alt="相对声级到输出幅度的压缩曲线及不同压缩参数对比" loading="lazy" /></a>
  <figcaption>附图 D｜左图把正文的 a=0.025 算例放在整条输入输出曲线上：相对声级 −20 dB 对应约 0.8425 的输出。阴影区表示截断平台；右图比较不同压缩参数，虚线是线性参照。纵轴不是感知响度。</figcaption>
</figure>

### E．CIS 和 ACE：集合选择、排序与复杂度

CIS 模型的集合固定为全部启用通道；ACE 模型每轮重新选取。若 $v_i=w_iA_i$，增益 $w_i$ 应在选择前乘入，且乘法增益对应的 dB 表达为 $20\log_{10}w_i$。当前代码默认所有增益为 1；增加增益功能时，必须明确增益是否也进入幅度映射，而不能只改选择分支后继续宣称已复现完整厂商增益控制。[2](#ref-ci-cochlear-cs61)

`select_channels(v, N)` 有两步：先用稳定降序排序获得最强的 $N$ 个索引，再将这些索引按位置升序排列。前者决定保留哪些信息，后者决定本模型的轮内时序。以

$$
\boldsymbol v=[0.20,0.80,0.50,0.10],\quad N=2
$$

为例，零基索引集合为 $\{1,2\}$，发放顺序为通道 1 后通道 2。若所有值相等，稳定排序使较小原索引优先；这只是可复现的平局规则，不代表生理优先级。全部输入为零时，函数仍选出 $N$ 个索引，但对应幅度均为零。

完整排序的每轮复杂度约为 $O(m\log m)$，$J$ 轮约为 $O(Jm\log m)$。当 $m$ 很大，可以用部分选择减少工作量，但 `argpartition` 本身不保证相等值的稳定顺序，需要另行处理。对 8 或数十个分析通道，清楚的索引规则通常比这个微小的计算优化更有教学价值。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/09-ace-selection.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/09-ace-selection.svg" alt="ACE 原理模型从强弱排序到通道集合再到位置顺序发放" loading="lazy" /></a>
  <figcaption>附图 E｜另设 v=[0.20, 0.50, 0.80, 0.10]，使 E3 比 E2 更强。尽管强弱排序中 E3 在前，保留集合仍为 {E2,E3}，本教学调度按位置先发 E2、后发 E3。右图色块宽度包括双相及相间隔，不是连续单相电流。</figcaption>
</figure>

### F．脉冲调度：一轮怎样装下所有事件

教学调度把选中通道紧凑排列在轮次开头。设 $\Delta=58$ µs，$r=800$，第 $j$ 轮的第 $q$ 个事件起点为 $j/r+q\Delta$。8 通道 CIS 的本轮起点依次为 0、58、116、174、232、290、348、406 µs，最后一个事件在 464 µs 结束；下一轮在 1250 µs 开始。4 通道 ACE 模型则在 232 µs 结束本轮事件。

同一轮也可以设计成均匀分布的时隙 $t_{j,q}=j/r+q/(Nr)$，但这会改变跨通道时间差，属于另一种调度定义。下载脚本采用前一种紧凑安排；它不模拟任何厂商全部脉冲时序。

对某个电极 $i$，观察 $J$ 轮后，其候选事件率为

$$
\widehat r_i=\frac{r}{J}\sum_{j=0}^{J-1}\mathbf 1\{i\in\mathcal S_j\}.
$$

CIS 中每个启用电极恒为 $r$。ACE 中若电极在半数轮次被选中，候选事件率为 $r/2$；其实际脉冲间隔还会因轮内排序位置变化而变化。若只计非零脉冲，统计时还要排除零幅度占位。

`schedule()` 用 $J=\lfloor Lr/f_s\rfloor$ 只生成完整轮次；末端不足一轮的输入被舍去。当前示例恰好有 96 轮。它用浮点秒记录连续起点，尚未量化到植入体时钟。若要研究时钟效应，可令 $\widetilde t_k=\operatorname{round}(t_kf_{\rm clk})/f_{\rm clk}$，随后重新检查相邻事件是否重叠；不能认为量化前通过检查就足够。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/10-cycle-budget.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/10-cycle-budget.svg" alt="同一轮次率下 CIS 八事件与 ACE 四事件的脉冲时间预算" loading="lazy" /></a>
  <figcaption>附图 F｜两条时间轴都以 1250 µs 为一轮；每个色块占 58 µs。CIS 模型在 464 µs 后结束本轮事件，ACE 模型在 232 µs 后结束；灰区为本调度定义下的剩余时间，格内数字表示轮内发放次序。</figcaption>
</figure>

### G．把事件表变成有符号电极波形

对电极 $e$，将属于它的双相事件逐个相加：

$$
I_e(t)=\sum_{k:e_k=e}b_k(t-t_k).
$$

同一个波形可以显示成每电极一行的轨迹，也可以按时间—电极栅格着色。若每像素宽度大于单相宽，正负相可能相互抵消或被最大值汇总掩盖，所以热图必须注明记录的是事件起点、绝对幅度、峰值还是有符号瞬时值。正文图 2 明确使用事件起点与相对幅度。

本例每相 25 µs，声音采样周期约 41.67 µs，因此不能在原始 24 kHz 声音时间网格上忠实显示双相脉冲。可以在独立的高分辨率时间网格上调用 `biphasic()`，也可以直接用分段矩形边界绘图。若按离散时间积分检查净面积，应说明时间步长及边界采样规则；脚本的检查采用 1 µs 步长和区间中点。

理想等幅等宽双相的每相面积为 $\pm I\tau$，净面积为零。在电流导向中，两电极都应各自满足所定义的电荷平衡波形；不能只检验两电极相加的净值。真实回流配置、主动或被动放电及相序由系统另行规定。[1](#ref-zeng-2008)[12](#ref-ci-neuro2-specs)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/11-events-to-pulses.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/11-events-to-pulses.svg" alt="两个电极的事件展开为有符号双相波形及单相面积" loading="lazy" /></a>
  <figcaption>附图 G｜上图将两个事件起点展开为真实宽度的数学波形，并把电极轨迹纵向错开以便观察；下图把同一电极的正负面积着色。每相面积的单位为相对幅度×µs，不能标成临床电荷。</figcaption>
</figure>

### H．零交叉与 CSSS：从一个时间戳到一个序列

插值公式来自假设相邻样本之间线性变化：令 $y[n]+\lambda(y[n+1]-y[n])=0$，可得 $\lambda=-y[n]/(y[n+1]-y[n])$，交叉时刻是 $(n+\lambda)/f_s$。代码只识别“前一点严格负、后一点非负”，因此开头恰为零不产生事件；采样点恰为零但没有负到非负过渡，也不产生事件。这一约定可以避免部分重复计数，但它不是通用去噪器。

对于单频 $y(t)=A\sin(2\pi ft+\phi)$，相邻上行交叉间隔为 $1/f$；幅度随时间变化、含多个分量或夹噪声的带通信号，交叉间隔通常不再服从一个固定基频。要讨论“精细结构线索”，必须说明是哪一频带、哪一极性交叉及哪些事件被接受。

将交叉扩展为一般的通道特异序列，可以抽象写成

$$
\mathcal P_{i,k}=\{(\widehat t_{i,k}+d_{i,\ell},\ A_{i,k,\ell}):\ell=0,\ldots,L_{i,k}-1\}.
$$

$d_{i,\ell}$ 为序列内延时，$A_{i,k,\ell}$ 为各脉冲幅度，$L_{i,k}$ 为脉冲个数。**这只是说明 CSSS 需要比零交叉多哪些变量的通用记法，不是 MED-EL 的参数公式。** 把它做成编码器还需定义序列与下一次交叉重叠时如何处理，以及不同通道冲突时延后、删去或并行的规则；这些处理会改变原来的时间线索。FSP、FS4、FS4-p 的商用序列和兼容限制仍需按原厂资料区分。[6](#ref-ci-medel-maestro11)

本教学代码只返回 `upward_crossings()` 的单通道交叉时间；没有生成上述序列，也没有实现 FS4-p 并行调度。不能将下载脚本的 CIS 事件表加上几个交叉时间，就标为 FS4 输出。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/12-crossing-sequence.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/12-crossing-sequence.svg" alt="零交叉线性插值及单次触发生成多个事件的通用序列示意" loading="lazy" /></a>
  <figcaption>附图 H｜左图用相邻样本 −0.4 和 0.6 求得交叉位置 n+0.4；右图把一次交叉展开成三个带延时的事件。0、0.3、0.6 ms 是专为解释序列而设的延时，不是 FSP／FS4 商用参数，也没有执行跨通道调度。</figcaption>
</figure>

### I．电流导向：权重来自哪里，映射放在哪里

若仅做一个连续空间位置的教学例，可以假定在相邻分析中心频率 $f_i,f_{i+1}$ 之间得到峰值估计 $\widehat f$，再定义

$$
\alpha=\operatorname{clip}\left(\frac{\ln\widehat f-\ln f_i}{\ln f_{i+1}-\ln f_i},0,1\right).
$$

这是按对数频率插值的**自定义例子**，并非 Fidelity120 的峰值定位算法，也没有证明分析中心频率与电极位置严格一致。它只解释从一个估计位置得到一个 0–1 权重的思路；峰值本身的估计误差会直接使权重变化。

正文 `steering(I, alpha)` 假定两电极共用一个总幅度标度，所以两份额之和是 $I$。若两个电极各有映射 $F_i(a),F_{i+1}(a)$，另一种模型则写为

$$
I_i=(1-\alpha)F_i(a),\qquad I_{i+1}=\alpha F_{i+1}(a).
$$

这时两输出和一般不等于预先指定的同一个 $I$。GPyT 的映射模块包含分别映射、限幅及权重相乘；因此不能把“每对电极的总电流守恒”当作所有商用映射的恒等式。相关实现可直接对照作者仓库的 [f120Mapping.py](https://github.com/jabeim/AB-Generic-Python-Toolbox/blob/master/GpyT/Mapping/f120Mapping.py)。[10](#ref-ci-gpyt-code)

进一步讨论空间兴奋时，可用一个线性叠加的教学近似

$$
V(z)=I_iG_i(z)+I_{i+1}G_{i+1}(z),
$$

其中 $G_i(z)$ 表示电极到空间位置 $z$ 的传递关系，$V(z)$ 表示某个电位响应量。它显示电流权重为何可能改变空间分布，但神经激活和音高判断并不是这个电位的简单线性读出。因此，$\alpha=0.5$ 不自动意味着神经兴奋峰位于解剖中点，也不自动意味着两个音高的感知中点。[1](#ref-zeng-2008)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/13-steering-fields.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/13-steering-fields.svg" alt="相邻电极电流份额扫描与假设空间传递关系的叠加" loading="lazy" /></a>
  <figcaption>附图 I｜先看左图：α 改变时，两电极分担同一教学总幅度。再看右图：用两个假设的高斯空间传递关系做线性叠加，曲线形状和峰的位置未必随权重简单线性移动。右图不是神经激活、解剖位置或感知音高的预测。</figcaption>
</figure>

### J．SPEAK、MP3000 与未公开策略：可讲到哪一层

SPEAK 与 ACE 都使用谱峰选择，但选择更新、刺激速率、分析和设备参数存在差别。用同一个教学函数改变 $N$ 和 $r$，只能产生“较慢或较快的峰值选择模型”，不能据此完成 SPEAK 的商用复现。[3](#ref-ci-cochlear-guidance)

为了理解 MP3000 的掩蔽思想，可以写一个**自定义贪心选择模型**：令 $\ell_i$ 是第 $i$ 通道的特征声级，$M_{ki}$ 是已选通道 $k$ 对候选通道 $i$ 的假设掩蔽阈贡献，$B_i$ 是底噪／基线阈值，定义

$$
\theta_i(\mathcal S)=\max\left(B_i,\max_{k\in\mathcal S}M_{ki}\right),\qquad
s_i(\mathcal S)=\ell_i-\theta_i(\mathcal S).
$$

初始集合为空时，令 $\theta_i=B_i$。每次选取尚未入选且 $s_i$ 最大的通道，更新掩蔽阈，再选下一个：

```text
S ← 空集合
重复 N 次：
    对每个未选通道计算当前掩蔽阈和剩余得分
    k ← 得分最大的未选通道（同分时按约定处理）
    S ← S ∪ {k}
对 S 按指定刺激顺序调度
```

例如两个邻近强通道中，第二个可能在第一个入选后得分下降，一个较远且原本稍弱的通道反而被保留。这说明它与一次性 `argsort` 的区别。上式没有指定真实掩蔽函数、声级依赖或商用终止规则，**不是 MP3000 的公开完整算法**；将 dB 阈值直接相加、或把不同声级基准混入同一比较，也不成立。临床 MP3000 的依据仍是其原始研究。[5](#ref-ci-mp3000-2011)

国产 APS、Symphony 可按原始系统论文讨论峰值选择与虚拟通道，但不能由此认定与 ACE、Fidelity120 逐步相同；C-Tone、MTone 等缺少完整公开算法说明的名称，仍保持“未核实”标记，不用一个自编基频提取器填补商业实现空白。[16](#ref-ci-nurotron-design-2015)[17](#ref-ci-listent-catalog)

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/14-masking-selection.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/14-masking-selection.svg" alt="自定义掩蔽模型中入选通道更新阈值并改变下一通道选择" loading="lazy" /></a>
  <figcaption>附图 J｜按从左到右阅读：只按强度会保留 E1、E2；先选 E1 并更新假设掩蔽阈后，E2 的剩余得分降至 6 dB，E6 为 29 dB，所以下一步选 E6。图中设基线阈为 0 dB、M(1,i)=max(0,60−8|i−1|) dB；这是自定义算例，不是商用 MP3000 参数。</figcaption>
</figure>

### K．怎样复现、诊断差异和报告结果

复现应先固定输入、前端和幅度标度，再单独改变一个策略环节。建议沿下表检查中间量；这里是教学实验步骤，未报告新的听者或临床结果。

| 实验 | 只改变什么 | 应观察的量与解释 |
| --- | --- | --- |
| 强度扫描 | 合成输入乘以固定比例 | `env` 的比例、压缩曲线与饱和位置；输入倍增在未限幅特征上对应约 +6.02 dB |
| maxima 对比 | $N=8,4,2$，保持 $r$ 不变 | 通道集合、每电极事件数、总事件数；响度与功耗需要另外评价 |
| 轮次率对比 | 改变 $r$ | 包络取样间隔、时间预算和事件数；先检查 $N\Delta\le1/r$ |
| 零交叉核查 | 单独改变纯音频率和噪声 | 时间间隔分布，而不只看平均事件数 |
| 导向权重扫描 | $\alpha=0,0.25,0.5,0.75,1$ | 两电极相对幅度与每电极双相面积；不将份额直接称为感知音高 |
| 流式一致性 | 改变分块长度，保持算法参数 | 保存全部滤波器与时钟状态后，与一次性计算逐样本比较 |

固定输入时，总候选事件数为

$$
P=N\left\lfloor\frac{Lr}{f_s}\right\rfloor.
$$

但若改变 `RATE` 常量后调用 `schedule()` 时省略 `rate`，Python 已创建的默认参数不一定随该常量重新赋值而改变。做参数实验应显式传入 `schedule(env, n=4, fs=FS, rate=new_rate)`。内置 `verify()` 的 768／384 事件断言专门对应默认算例；自定义参数要用上式计算预期值，不能把该断言的失败一概解释为调度错误。

读取默认输出的最小示例为：

```python
from pathlib import Path
import numpy as np

folder = Path('ci-demo')
data = np.load(folder / 'teaching-data.npz')
events = np.loadtxt(folder / 'ace-events.csv', delimiter=',', skiprows=1)
channel = events[:, 1].astype(int)
counts = np.bincount(channel, minlength=data['envelope'].shape[0])
print(data['envelope'].shape, len(events), counts, counts.sum())
# 默认形状 (8, 2880)，384 行候选事件，各通道计数之和为 384
```

完整报告至少保留声音采样率、滤波器定义、参考幅度、包络截止频率、轮次率、maxima、排序规则、相宽、相间隔、时间单位及是否包含零幅度占位。还应记录输入、代码版本、NumPy／SciPy 版本及初始状态。输出可重复只证明所定义的模型实现一致；要判断临床可用性，仍需设备输出验证和适当的听者实验。

<figure>
  <a href="/n3-hearingpedia/figures/ci-coding/15-event-counts.svg" target="_blank" rel="noopener"><img src="/n3-hearingpedia/figures/ci-coding/15-event-counts.svg" alt="默认输入下每个电极的候选事件分布和 maxima 改变后的总事件数" loading="lazy" /></a>
  <figcaption>附图 K｜左图来自默认 120 ms 输入的实际输出：CIS 每电极均为 96 个候选事件，ACE 各电极次数不同且合计 384。右图在同一输入与轮次率下改变 N，事件总数分别为 192、384、768；没有据此推算听者响度或处理器功耗。</figcaption>
</figure>
