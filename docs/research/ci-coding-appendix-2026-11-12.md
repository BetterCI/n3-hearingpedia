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
