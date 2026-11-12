<!-- 2026-11-12 撰写记录：下文为已整合入词条的机制章节原稿。
增量核查：Custom Sound 6.1（maxima、增益先于选择）、MAESTRO 11（CSSS）、
GPyT 的 f120Mapping.py 与 f120Electrodogram.py。完整目录仍保持 2026-10-04 的核验日期，
此次不是全目录重新检索。公式与教学代码为原创简化模型，不复刻商用参数。
运行结果：python public/code/ci-coding/teaching_encoder.py --out artifacts/ci-coding 通过；
node scripts/verify-ci-coding.mjs 通过：9 组显示公式、4 张图、35 条文献、9 个资源引用。
python scripts/generate-ci-coding.py 生成 SVG/PNG；全部 PNG 已逐张目视核查。
整站 pnpm build 在 active-auditory-sensing 引用缺失的 auditory-cortex 时失败，
该关系及缺失词条非此次修改；已提供独立 HTML 预览。
-->

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
