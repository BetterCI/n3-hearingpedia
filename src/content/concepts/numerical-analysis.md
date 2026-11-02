---
title: "数值分析"
english: "Numerical Analysis"
slug: "numerical-analysis"
summary: "从误差、条件数与稳定性判断计算是否可信，再学习线性方程与最小二乘、非线性求根、插值、数值微积分、刚性初值问题、边值离散和预条件迭代；用可复算的反例解释残差、收敛和精度的边界。"
categories: ["research-methods", "acoustics", "signal-processing"]
tags: ["基础课程", "数值分析", "数值稳定性", "条件数", "插值", "最小二乘", "微分方程"]
aliases: ["Numerical Analysis", "数值计算基础", "计算方法"]
level: ["undergraduate", "graduate"]
status: draft
depth: in-depth
last_updated: "2026-11-02"
literature_checked_at: "2026-11-02"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
knowledge_area: "methods"
kind: "course"
key_facts:
  - {label: "研究对象", value: "有限精度下近似求解数学问题，并控制误差与计算成本"}
  - {label: "核心区别", value: "问题的条件性、算法的稳定性和离散近似的收敛分别检查"}
  - {label: "研究连接", value: "响应拟合、逆问题、滤波与重采样、连续模型离散和仿真核验"}
  - {label: "重要边界", value: "小残差不自动保证小解误差，内部误差估计不等于一般严格误差界"}
references: ["na-float", "na-conditioning", "na-stability", "na-condition-number", "na-pivoting", "na-qr", "na-svd", "na-fixed-point", "na-newton", "na-brent-api", "na-interp-stability", "na-splines", "na-interp-api", "na-fd", "na-integration", "na-adaptive", "na-rk", "na-absstab", "na-stiff", "na-ivp-api", "na-bvp", "na-sparse-api", "na-cg", "na-precond", "na-cg-api"]
order: 1015
---

**数值分析**（numerical analysis）研究怎样用有限次运算、有限存储和有限精度，近似求解数学问题，并说明结果的误差、稳定性和计算成本。它既关心“怎样算”，也关心“算出的数代表什么、可靠到什么程度”。数学公式存在，不保证直接照着输入计算机就能得到准确答案。[1](#ref-na-float)[2](#ref-na-conditioning)

声学响应拟合、听觉模型仿真、参数估计、数字滤波和逆问题都会遇到数值计算。本篇与[微积分](../calculus/)、[线性代数](../linear-algebra/)、[信号与系统](../signals-and-systems/)和[数字信号处理](../digital-signal-processing/)配套：前两者提供变化、累积及矩阵关系，这里进一步检查实现、误差与验证。读者可按当前问题补读，无需先完整修完这些课程。

十幅图和全部数值来自明确设定的教学计算，不是听者、房间、神经元或器件实测。近乎重合的正弦、窄峰积分和缩放矩阵是刻意选择的反例；它们展示计算边界，不构成听觉干预效果证据。文末有三个短例子，另提供[完整实验脚本](/n3-hearingpedia/code/numerical-analysis/experiments.py)。

目标函数、约束、梯度与曲率、KKT和求解后的最优性核对，可配合[最优化方法](../optimization-methods/)按需阅读；数值收敛、模型有效性和统计证据应分别判断。

## 阅读准备与独立阅读

**起步知识。** 会读函数图像、使用比例、解简单方程就可以先看例子。导数、积分、向量、矩阵和误差在首次需要时作局部说明；涉及完整收敛证明和大规模算法理论时，再补相应数学训练。

**随用随补。** 向量是排成一列的数，矩阵是按行列排列的数表，Ax表示按行作乘积求和。实向量的2范数 $\|x\|_2=\sqrt{\sum_i x_i^2}$，衡量整组数的大小；矩阵2范数表示它对这种长度的最大放大倍数。导数是局部变化率，积分是带区间权重的累积。本文默认有限区间[a,b]满足a<b，计算误差优先使用一致的单位和尺度。

**分层阅读。** 第一遍看误差来源、小残差反例、插值曲线、窄峰积分和网格加密。第二遍核对条件数、QR/SVD、迭代收敛与步长约束。向量范数、Taylor余项和特征值可在相关课程按点补读；图与短数组帮助理解，但不能替代一般定理证明。

## 数字表示和误差要先有共同尺度

### 近似误差不只有一种来源

测量噪声、模型简化、空间或时间离散、迭代未收敛，以及浮点舍入，可能同时影响结果。提高浮点位数主要针对最后一类；它不能补回漏采的窄峰、错误边界条件或没有辨认出的模型参数。

真值为x、近似为x̂时，绝对误差是|x̂−x|；x≠0时可定义相对误差|x̂−x|/|x|。向量则用相应范数。真值接近0时相对误差可能很大，应结合绝对容差、数据尺度及任务需求报告，不能机械地把“百分比大”当作结果一定失效。[2](#ref-na-conditioning)

报告小数位数也不等于拥有同样多的准确数字。算法输出十六位小数，只能说明显示格式；输入误差和问题的敏感性可能早已限制可相信的位数。

### 浮点数只是实数的有限集合

常见float64使用二进制有效数字与指数表示数值。1附近向上相邻数的间隔为ε=2⁻⁵²≈2.22×10⁻¹⁶；在舍入到最近数的通常模型中，单位舍入误差u=2⁻⁵³约为其一半。不同教材可能把“机器精度”用于不同约定，比较公式时应先核对定义。[1](#ref-na-float)

在不发生溢出、且结果处于正常数范围等条件下，基本运算常用fl(a∘b)=(a∘b)(1+δ)、|δ|≤u描述。这个相对误差模型不能无条件覆盖下溢、非正规数和所有数学库函数。NaN（非数值标记）、无穷、整数转换及数据类型混用也应检查，不能只看程序是否运行结束。

由于1+x可能先被舍入为1，直接计算log(1+x)在很小的正x处可能得到0。log1p(x)为这种表达提供更合适的专用计算；这并非把数学函数换了一个，而是选择了不同的数值实现。[3](#ref-na-stability)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/cancellation.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/numerical-analysis/cancellation.svg" alt="比较直接计算log(1+x)与log1p在很小输入下的结果和相对误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图1　相同数学表达可以有不同计算精度。正x从10⁻¹⁸至10⁻¹，float64结果与对同一二进制输入用80位Decimal计算的参考比较；右图为相对误差，显示下限10⁻²⁰仅用于绘图。坐标均无量纲，高精度对照不是经过区间算术认证的严格包围界。</figcaption></figure>

## 条件性 稳定性与残差分别说明什么

### 条件数描述问题对输入扰动的敏感性

若f可导且x和f(x)都非零，局部相对条件数可写成 $\kappa_f(x)=|xf'(x)/f(x)|$。它比较很小的相对输入变化会造成多大相对输出变化；近似成立需要扰动足够小，不能把局部系数当作任意范围的精确误差倍数。[2](#ref-na-conditioning)

对非奇异实方阵A，2范数条件数为 $\kappa_2(A)=\|A\|_2\|A^{-1}\|_2=\sigma_{\max}/\sigma_{\min}$，σ为奇异值。条件数大表示某些方向特别敏感，不表示每一种输入扰动都会恰好放大这么多。单位、缩放和参数化会改变条件数的解释，因此应记录采用的尺度。[4](#ref-na-condition-number)

### 前向误差与后向误差面向不同对象

**前向误差**比较计算输出与原问题真解；**后向误差**则问：对输入作多小改动，计算输出就能成为改动后问题的精确解？若某算法总能把计算解释为很小输入扰动后的精确求解，通常称其后向稳定，具体仍取决于误差度量、问题类别及常数。[3](#ref-na-stability)

稳定算法能避免引入不必要的误差放大，却不能消除原问题的病态性。正则化则改变求解目标以换取更稳定的推断，两者不是同一操作；增加先验约束会带来偏差，需要任务层面的依据。

### 小残差为什么仍可能对应大解误差

求Ax=b得到x̂后，残差r=b−Ax̂是在原方程上的不满足量。对非零b、非奇异A，以一致2范数可得
$$
\frac{\|\hat x-x\|_2}{\|x\|_2}\le\kappa_2(A)\frac{\|r\|_2}{\|b\|_2}.
$$

所以残差必须结合条件数解释。常用归一化量 $\eta=\|r\|/(\|A\|\|\hat x\|+\|b\|)$ 还把矩阵、解和右端的尺度一起纳入；它不等于直接观测了真解误差。[4](#ref-na-condition-number)

设A=diag(1,δ)、b=(1,δ)ᵀ，δ>0，真解x=(1,1)ᵀ。如果输出x̂=(1,0)ᵀ，相对解误差始终为1/√2≈0.707；相对残差却约为δ。当δ=10⁻⁸时，看起来极小的残差仍遗漏了整个第二分量。这是问题敏感性造成的，不需要假设程序崩溃。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/conditioning-residual.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/numerical-analysis/conditioning-residual.svg" alt="对角矩阵的相对残差随小参数下降，但相对解误差不变；同时展示矩阵把不同方向放大得不同。" width="1400" height="550" loading="lazy" /></a><figcaption>图2　残差小还需要问方程是否敏感。左图δ从10⁻¹至10⁻¹²，近似解固定为(1,0)，误差按2范数；右图另取δ=0.15，将单位圆映射成椭圆，两个面板参数范围不同且明确标出。全部量无量纲，非声学测量。</figcaption></figure>

## 线性方程优先考虑分解 结构与主元

### 消元中的小主元可能放大中间误差

高斯消元通过消去未知量形成三角系统；LU分解把矩阵表示为下三角L和上三角U的乘积，再用前代、回代求解。带行主元时还要记录行置换P，常写成PA=LU。主元是当前用于除法消元的元素，不等于矩阵的特征值。[5](#ref-na-pivoting)

例如A的两行为(10⁻²⁰,1)与(1,1)，b=(1,2)ᵀ。A的条件数约2.62，并不大；若不交换行，第一步会除以10⁻²⁰，生成巨大中间数。本篇float64直接无主元实现得到近似(0,1)，带主元求解则得到约(1,1)。这次问题主要出在计算路径，和上节的病态矩阵反例不同。

部分主元选择通常显著改善消元的数值行为，但不能对所有矩阵保证任何精度要求；消元增长因子、缩放及输入误差仍需检查。只为了求Ax=b，通常直接使用合适分解求解，不必先显式计算A⁻¹再乘b。

### 利用结构不等于忽略适用条件

对称正定矩阵可用Cholesky分解A=LLᵀ；正定指任意非零实向量z都满足zᵀAz>0。若矩阵只对称而不正定，不能直接当作满足这一条件。三对角、带状和稀疏矩阵有专门存储与求解方法，可避免把大量零也当成普通元素存储。

稠密一般矩阵的分解成本常随维数约按n³增长；同一A对应多组右端时，重复利用分解可节省成本。实际速度还取决于稀疏填充、数据布局、硬件与库实现，不能只按维数或某一次计时判断所有问题。

## 最小二乘要把拟合与参数可辨识性分开

### QR与SVD保留了哪些信息

观测多于未知参数时，可求使‖Ax−b‖₂最小的x。实矩阵A列满秩时，薄QR分解A=QR使Q的列正交归一，QᵀQ=I，R为非奇异上三角；最小二乘解由Rx=Qᵀb得到。它不要求Q在矩形情形下还满足QQᵀ=I。[6](#ref-na-qr)

本节列满秩矩形A的条件数也按最大与最小奇异值之比定义，不需要普通方阵逆A⁻¹存在。这样才能把条件数用于256行、2列的设计矩阵，而不是错误地要求它先有普通逆。

正规方程AᵀAx=Aᵀb在精确算术下给出同一列满秩问题的解，但 $\kappa_2(A^\mathsf{T}A)=\kappa_2(A)^2$，会恶化数值条件。QR通常能避免这种额外损失；这不等于任何病态最小二乘都因此获得高精度参数。

奇异值分解SVD把A写成UΣVᵀ，正交方向的放大倍数由奇异值给出。很小的奇异值对应难从数据可靠辨认的参数组合；秩不足时，最小范数解、截断阈值和允许误差应另行说明。是否把某个小奇异值当作0，还涉及单位和噪声尺度，不是所有资料都能共用一个阈值。[7](#ref-na-svd)

### 近乎重合的声音基函数可以产生不稳定系数

图3取16 kHz采样、256点记录，矩阵两列为1000与1000.0001 Hz的单位正弦，系数真值(0.8,−0.3)以Pa计。频率间隔被刻意设得极小，仅用来构造近乎相关的列，不代表听者分辨阈或实际实验建议。

该矩阵条件数约3.47×10⁵。沿最弱输出方向加入2范数仅10⁻⁴ Pa的扰动，最小二乘系数向量却改变约2.17 Pa；对应记录的输出变化仍只有10⁻⁴ Pa。短记录拟合得好，不代表两项系数都已可靠确定。

以λ>0求 $\min_x\{\|Ax-b\|_2^2+\lambda\|x\|_2^2\}$ 称一种Tikhonov或岭正则化；可把[A;√λI]与[b;0]组成增广最小二乘，避免直接依赖正规方程。图中λ=10⁻⁴用于展示抑制弱方向的同时也引入系数偏差，不是最佳参数推荐。真实逆问题还需噪声模型、独立验证和物理约束，连接[数理统计](../mathematical-statistics/)与[机器学习](../machine-learning/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/least-squares.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/numerical-analysis/least-squares.svg" alt="两列近乎相同的正弦基函数及小输出扰动引起的大系数变化，并比较正则化结果。" width="1400" height="550" loading="lazy" /></a><figcaption>图3　拟合波形接近，不保证系数稳定。16 ms记录、频率1000与1000.0001 Hz，图左仅显示前4 ms；右图扰动沿左奇异向量的最弱方向确定，范数10⁻⁴ Pa，无随机听者数据。正则化λ=10⁻⁴，纵轴系数以Pa计，示例中基函数与λ无量纲。</figcaption></figure>

## 非线性求根先考虑区间与收敛条件

### 二分法用区间保住一个根

若实函数f在[a,b]连续，且端点非零、f(a)f(b)<0，则区间至少含一个根。二分法反复取中点并保留异号子区间；若已缩短k次，区间宽为原宽的2⁻ᵏ，再取其中点的根误差不超过当前宽度的一半。端点恰为0时可直接接受该端点。

这些保证依赖连续性；跨越不连续点的符号变化未必对应零点。二分法也不能保证隔离的是唯一根，更不能靠端点同号断言没有根。固定点迭代xₖ₊₁=g(xₖ)则需要另一套条件：例如g将闭区间映入自身，且全区间|g′|≤q<1时，可得到唯一固定点及线性收敛保证。[8](#ref-na-fixed-point)

### Newton法的快速性是局部结论

Newton更新为 $x_{k+1}=x_k-f(x_k)/f'(x_k)$。在简单根附近、函数足够光滑、导数不为0且初值足够接近时，可得到局部二次收敛，即误差大致按前一步误差的平方缩小。重根、坏初值、小导数或非光滑点会改变这种行为。[9](#ref-na-newton)

对cos x−x，在[0,1]中的根约0.73908513，Newton从1出发很快接近；但对x³−2x+2，从0出发恰好形成0→1→0的循环，既没有收敛，也没有因为两次更新都“合法”而得到根。

实用方法常把快速插值与区间保护结合。SciPy的brentq要求连续函数和合适的异号端点，并提供绝对/相对根位置容差；仍须检查返回状态、函数域与尺度，不把它视为任意非线性问题的通用保证。[10](#ref-na-brent-api)

### 停止条件不能只看一步变化

小步长可能因为舍入、导数过大或迭代停滞产生；小|f(x̂)|也会受f的缩放影响。若根与x̂位于同一适用区间，f在两者之间连续可导，且|f′|≥m>0，平均值定理才给出|x̂−根|≤|f(x̂)|/m这类误差界。应结合区间宽、残差、相邻步和最大迭代次数解释。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/root-iteration.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/numerical-analysis/root-iteration.svg" alt="比较cosx减x的迭代误差，并用三次函数展示Newton法在零与一之间循环。" width="1400" height="550" loading="lazy" /></a><figcaption>图4　快收敛需要条件。左图cos x−x，固定点法和Newton初值1、二分初始区间[0,1]，参考根由高精度容差的float64 brentq计算，误差显示下限10⁻¹⁶不是严格精度证书；右图三次函数在0与1处的切线分别交到1与0，显示确定性循环。变量无量纲。</figcaption></figure>

## 插值必须考虑节点 光滑性和形状约束

### 增加次数不总使全局多项式更好

n+1个互异节点可确定次数不超过n的插值多项式，使它通过所有节点；重心公式能更合适地计算这个多项式，却不改变所选择的插值问题。带噪节点也会被插值精确穿过，所以插值不同于平滑或统计估计。[11](#ref-na-interp-stability)

经典Runge函数1/(1+25x²)在[−1,1]上光滑，但等距高阶插值可在边缘严重振荡。本文用重心公式重新计算：20次时，在10001点检验网上，等距方案最大绝对误差约59.8，Chebyshev–Lobatto节点 $x_j=\cos(j\pi/n)$ 则约0.0177。后者在端点附近更密，改变了节点布局。

Runge现象不只是浮点舍入造成；提高字长或把多项式换一种求值方式，不能自动根治等距节点带来的敏感性与不收敛。Chebyshev节点也不是对所有非光滑函数和所有噪声资料的普遍最佳选择。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/interpolation-nodes.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/numerical-analysis/interpolation-nodes.svg" alt="Runge函数的等距与Chebyshev节点插值，以及随次数变化的网格最大误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图5　节点设计与求值实现是两件事。左图20次插值，三条曲线共用完整纵轴，不截去大幅振荡；右图次数4—40，误差取10001点检验网格的最大值，并非连续区间严格极值。所有变量无量纲，重心权重按节点解析给出以固定复算条件。</figcaption></figure>

### 分段样条还要指定端点条件

三次样条用分段三次多项式，通常在节点处保持函数、一阶与二阶导数连续，即C²；还需端点条件，例如自然样条的两端二阶导数为0。自然条件不是从任意数据自动推得的物理事实，其他条件可能产生不同结果。[12](#ref-na-splines)

PCHIP是保形分段三次Hermite插值，通常C¹，对单调数据可保持相应单调形状，但一般不保证C²。图6用节点(0,0)、(1,0.01)、(2,0.02)、(3,1)比较自然三次样条与PCHIP：前者在部分区间出现约−0.0616的负值，后者在本例保持非负单调。若目标量有非负或单调约束，曲线“更光滑”并不是唯一标准。[13](#ref-na-interp-api)

这不说明PCHIP在所有误差指标上都更准确；节点间真值仍未知。插值区间之外属于外推，风险和模型依据不同；本例显式关闭外推，不能把端点附近曲线随意延伸为实验结论。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/spline-shape.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/numerical-analysis/spline-shape.svg" alt="单调非负节点的自然三次样条与PCHIP，以及各自导数对单调性的影响。" width="1400" height="550" loading="lazy" /></a><figcaption>图6　形状要求要与光滑要求一起说明。四个无量纲节点，CubicSpline使用natural端点条件，两方法均关闭外推；左图比较数值，右图比较一阶导数。负导数表示该区间下降，不把平滑插值称为已验证的真实响应曲线。</figcaption></figure>

## 数值微积分要检查采样是否解决了问题

### 差分的截断误差与噪声会竞争

中心差分[f(x+h)−f(x−h)]/(2h)在有足够有界高阶导数等条件下通常具有O(h²)截断误差；但相近数相减的舍入误差、样值噪声还会被小h放大。若两样值噪声独立且方差均为σ²，差分噪声方差为σ²/(2h²)。这个统计条件不是所有录音的普遍性质。[14](#ref-na-fd)

O(hᵖ)表示h足够小时误差可由某个常数乘hᵖ控制，常数与函数及单位有关。端点用什么差分、样本是否等距、是否已平滑、时间单位是s还是样本，都影响解释；对数字序列求导时不能漏掉采样间隔。

### 求积规则与误差估计都有前提

梯形法把相邻样点连成线段后累积，光滑等距情况下整体误差常为O(h²)；复合Simpson法在偶数个小区间和相应四阶光滑性等条件下可达O(h⁴)。使用更高阶规则，不会恢复根本没有采到的局部变化。[15](#ref-na-integration)

若已进入 $Q_h=I+Ch^p+\text{更高阶项}$ 的渐近范围，可用 $Q_{h/2}+(Q_{h/2}-Q_h)/(2^p-1)$ 作Richardson外推；下标h/2表示步长减半，不是把积分估计除以2。这个公式依赖主导误差项确实按该幂变化；网格尚未分辨函数、噪声占主导或含奇点时，直接套用可能失效。

自适应求积根据局部比较分配更多样点，通常比盲目全局加密高效；但内部误差估计依赖已采到的信息，不是所有函数上的严格误差证书。[16](#ref-na-adaptive)

### 一个可能被自动算法漏掉的窄峰

图7取g(x)=exp[−((x−0.37)/0.001)²]，x∈[0,1]，真实积分约0.00177245。16、32、64个等宽小区间的梯形结果都极小，三次粗网格彼此接近，仍远离真实值；加密到足够分辨峰宽后才开始可靠。

在本文SciPy 1.17.1、epsabs=epsrel=10⁻¹⁰设置下，未提供峰位置的quad调用返回约3.7×10⁻⁶¹，并给出同量级内部误差估计；已知峰位置后显式分段，得到约0.00177245。数值与实现版本、采样策略有关，这不是对该程序的普遍失败率估计。正确做法是结合已知结构、分段、独立算法与网格检查，而非只相信返回的一项“error”。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/narrow-quadrature.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/numerical-analysis/narrow-quadrature.svg" alt="粗网格漏掉宽度很窄的高斯峰，以及网格加密后积分值才接近解析参考。" width="1400" height="550" loading="lazy" /></a><figcaption>图7　看起来已经稳定，仍可能只是没有看见峰。峰中心0.37、尺度0.001，变量无量纲；左图放大局部并显示16区间网格的邻近样点，右图展示16—2048区间的梯形积分。参考由误差函数表达式计算，自动求积对照的参数与版本在正文和脚本中记录。</figcaption></figure>

## 初值问题区分精度 步长稳定性和刚性

### 局部误差阶数不等于全局结果保证

对y′=f(t,y)、y(t0)=y0，显式Euler用yₖ₊₁=yₖ+hf(tₖ,yₖ)。在适当光滑性与稳定条件下，它的单步局部误差为O(h²)、固定有限时间内的全局误差为O(h)；经典四阶Runge–Kutta相应可达局部O(h⁵)、全局O(h⁴)。所需条件和误差常数不能由方法名称自动满足。[17](#ref-na-rk)

自适应算法通常根据嵌入式或局部误差估计调整内部步长。输出点t_eval与内部计算步并非同一件事，rtol和atol也不直接给出全局真实误差界。应检查求解成功、初值、参数尺度、事件及不连续处的处理。[20](#ref-na-ivp-api)

### 以测试方程检查衰减是否保留

对y′=λy、Re λ<0，显式Euler的放大因子为 $R(h\lambda)=1+h\lambda$。希望离散误差也衰减，需|R|<1；对实λ=−a、a>0，得到0<ha<2。隐式Euler因子为 $1/(1-h\lambda)$，在负实部范围有更大的稳定性优势，但大步长仍可能不准确。[18](#ref-na-absstab)

**刚性**常表现为：我们关心的解变化较慢，显式方法却因快速衰减模态的稳定约束，被迫用很小步长。它与问题、时间范围、误差要求及方法有关，不应仅凭“方程看起来复杂”判断。[19](#ref-na-stiff)

取a=1000 s⁻¹、ω=1 rad/s，无量纲输出满足y′=−a[y−cos(ωt)]−ω sin(ωt)，y(0)=0，解析解为cos(ωt)−exp(−at)。它同时含约1 ms快速暂态和较慢振荡；显式Euler用10 ms步长会不稳定，1 ms处于衰减范围。隐式Euler用10 ms可避免这种增长，却不能精细解析起始的1 ms暂态。

刚性问题可评估Radau、BDF等方法；选隐式方法还意味着每步要处理线性或非线性方程，不能只比较一步公式长度。本文用同一容差复算RK45与Radau，记录函数调用与对解析解的误差，不把单个算例的成本排名推广到所有模型。[20](#ref-na-ivp-api)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/stiff-integration.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/numerical-analysis/stiff-integration.svg" alt="带快速暂态的连续模型，在不同显式和隐式Euler步长下的轨迹和长期误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图8　稳定不等于分辨了所有时间尺度。a=1000 s⁻¹、ω=1 rad/s、初值0，左图只放大0—30 ms，右图误差显示至1 s并采用对数纵轴；显式步长1与10 ms、隐式步长10 ms。输出无量纲，非膜电位或电声器件测量。</figcaption></figure>

## 边值离散要同时核对方程 网格和边界

### 连续问题变成矩阵时改变了什么

边值问题在区间不同端点给条件，不同于只指定起点的初值问题。例如无量纲区间[0,1]上，−u″=π²sin(πx)，u(0)=u(1)=0，解析解为sin(πx)。若只离散方程却漏掉或误写边界，就在求另一个问题。[21](#ref-na-bvp)

等距h=1/N、内部节点xᵢ=ih，用 $(-u_{i-1}+2u_i-u_{i+1})/h^2$ 近似−u″，得到三对角线性系统。一般非零Dirichlet端值须按系数移入右端；本例两端为0，所以相应项恰好消失，并非所有边界都可以省略。

在光滑性与离散稳定性等条件下，这个模型可得到二阶误差。N=16、32、64时，网格最大误差约0.003219、0.0008036、0.0002008，逐次接近四倍下降；相对线性残差已在约10⁻¹⁵—10⁻¹³范围，却不等于连续解误差也这么小。[22](#ref-na-sparse-api)

### 网格收敛应比较同一个问题

已知真解时，观察阶数可用log₂(Eh/Eh/2)估计。真解未知时，需要对齐网格或以一致插值比较多组解，并确认已进入渐近区间；同时保持边界、材料参数、几何和误差指标不变。改变模型后两条曲线接近，不构成原模型的网格收敛证据。

有限差分、有限元和谱方法使用不同近似空间及离散关系，不能只按“网格点数相同”认定精度可比。真实声场的网格还要解析相应波长、边界及局部结构，后续可接[数学物理方法](../mathematical-physics-methods/)和[波动方程](../wave-equation/)。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/boundary-grid.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/numerical-analysis/boundary-grid.svg" alt="一维零端值问题的中心差分解，与解析正弦和网格误差下降率比较。" width="1400" height="550" loading="lazy" /></a><figcaption>图9　线性方程已解准，连续离散误差仍要查。左图N=16个小区间，端点值另补0；右图N=16、32、64、128的内部网格最大误差，对照h²趋势线。坐标与输出均无量纲，不代表实际房间声场的网格推荐。</figcaption></figure>

## 大矩阵迭代利用结构 也需要停止依据

### 特征值 奇异值与迭代各有角色

特征关系Av=λv描述被A作用后方向保持不变的向量；奇异值描述不同方向长度的放大，二者不是同一套数。对称矩阵有更好的谱性质，一般非正规矩阵的小特征残差不能不加条件地转成小特征值误差。不要因为程序返回一串特征值，就跳过残差与矩阵性质检查。[7](#ref-na-svd)

对定常迭代xₖ₊₁=Gxₖ+c，精确算术下从任意初值都收敛到同一固定点，与谱半径ρ(G)<1等价；ρ是特征值模的最大值。这不保证每一步的2范数残差都下降，也不自动给出足够快的计算。

### CG与预条件必须匹配矩阵性质

标准共轭梯度法CG用于实对称正定系统，复数情形对应Hermitian正定；它利用矩阵乘向量和逐步形成的Krylov子空间逼近解。精确算术下n维问题至多n步的结论，不应原样当作浮点计算的迭代次数保证。欧氏残差也可能非单调，不能看到一次回升就宣布算法失败。[23](#ref-na-cg)

预条件用易处理的P改善等价系统的尺度或谱分布；它需要构造与应用成本，不能只看迭代数。Jacobi预条件取P=diag(A)，对本例SPD矩阵对角均为正。SciPy cg参数M接收近似逆作用P⁻¹，而非把P原样传进去，这个约定尤其要核对。[24](#ref-na-precond)[25](#ref-na-cg-api)

图10令T为80阶对称三对角矩阵，对角2、相邻对角−1，D的对角从1几何增长到1000，A=DTD。以真解全1生成b，rtol=10⁻¹⁰、atol=0、最多1000步；本环境CG约875步、Jacobi预条件约80步达到停止标准。这里同时检查真解误差，不把迭代数视为硬件运行时间，也不把结果推广到所有稀疏系统。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/numerical-analysis/preconditioned-cg.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/numerical-analysis/preconditioned-cg.svg" alt="缩放正定系统的CG与Jacobi预条件残差历史，并比较最终残差和解误差。" width="1400" height="550" loading="lazy" /></a><figcaption>图10　预条件改变求解过程，不改变本例目标方程。A=DTD、维数80、D对角范围1—1000，初值0；左图逐次实际相对残差，右图最终相对残差与相对解误差，均用2范数。所有量无量纲，函数库与容差见正文，数值行为不作为普遍速度基准。</figcaption></figure>

## 用可复算的记录判断结果能否使用

### 验证要覆盖模型与实现两层

先用已知解、短数组、零输入、对称性和极限情形检查实现，再检查目标模型是否适合资料。不同公式、独立算法、高精度或网格加密的交叉核对可发现问题，但所有方法若共用一个错误边界或单位，也可能一致地给出错误结果。

记录输入、单位、缩放、算法、数据类型、版本、容差、随机种子、网格及失败状态。迭代器返回成功只说明符合其停止规则；内部误差估计、方程残差、离散误差和实际测量误差应分开报告。研究[听觉计算模型](../auditory-computational-models/)或[计算神经科学](../computational-neuroscience/)时，还需另检验机制与观测的对应。

本篇使用NumPy 1.26.4、SciPy 1.17.1复算，所查SciPy在线文档为1.18.0，区分文档版本与运行环境。参数显式指定，不声称在未运行的版本上测试；教学函数均可由文首完整脚本重现。

### 三个短例子

例1用80位Decimal参考检查很小x的对数。将输入float精确转为Decimal后再计算，避免把两种不同输入的表示误差混在一起；高精度计算用于核对，不宣称是一切问题的严格误差证明。

```python
from decimal import Decimal, localcontext
import numpy as np
x = np.float64(1e-16)
naive = np.log(1+x)
stable = np.log1p(x)
with localcontext() as ctx:
    ctx.prec = 80
    reference = (Decimal(1)+Decimal.from_float(float(x))).ln()
    error = abs(Decimal.from_float(float(stable))-reference)
assert naive == 0
assert float(error) < 1e-30
print(naive, stable, error)
```

例2用列满秩的小矩阵核对QR最小二乘与SVD求解，并检查残差对列空间近似正交。不同问题上的误差容差应按尺度重新设置。

```python
import numpy as np
t = np.linspace(-1, 1, 31)
A = np.column_stack([np.ones_like(t), t, t*t])
truth = np.array([0.3, 0.8, -0.2])
b = A@truth + np.random.default_rng(20261102).normal(0, 0.02, len(t))
Q, R = np.linalg.qr(A, mode="reduced")
x = np.linalg.solve(R, Q.T@b)
reference = np.linalg.lstsq(A, b, rcond=None)[0]
assert np.allclose(x, reference, atol=1e-12, rtol=1e-12)
assert np.linalg.norm(A.T@(b-A@x)) < 1e-12
print(x, np.linalg.norm(b-A@x))
```

例3验证零端值边界问题的网格收敛。N表示小区间数，内部未知量有N−1个；数组只列内部值，零边界已进入离散模型。[22](#ref-na-sparse-api)

```python
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
errors = []
for N in [16, 32, 64]:
    h = 1/N
    x = np.arange(1, N)*h
    A = diags([-np.ones(N-2), 2*np.ones(N-1), -np.ones(N-2)],
              [-1, 0, 1], format="csc")/(h*h)
    y = spsolve(A, np.pi**2*np.sin(np.pi*x))
    errors.append(np.max(np.abs(y-np.sin(np.pi*x))))
ratios = np.array(errors[:-1])/np.array(errors[1:])
assert np.all((ratios > 3.9) & (ratios < 4.1))
print(errors, ratios)
```

### 检查自己是否理解了误差的对象

1. float64的ε与单位舍入误差u差在哪里？为什么输出很多位小数不能证明结果准确？
2. 病态问题与不稳定算法各自需要怎样的对照？为何小残差仍可能遗漏一个完整参数分量？
3. 正规方程为什么可能额外损失精度？正则化又为什么不能只解释成“更稳定的算法”？
4. Newton法在哪些条件下快？符号变化、迭代步长和函数残差分别能保证什么？
5. Runge现象为什么不能只靠提高浮点位数解决？自然样条与PCHIP保留了哪些不同性质？
6. 多组粗网格积分接近，为什么仍可能没有分辨窄峰？自适应误差估计能否代替独立检查？
7. 隐式Euler稳定时为何仍会漏掉快速暂态？线性残差、网格误差和真实测量误差分别针对哪个对象？

来源主要为Driscoll与Braun的作者在线教材对应章节及SciPy官方文档；同一教材的多个章节只用于定位论断，不当作多项独立实验。图形、数值和反例设置另行复算，保留待专业审阅状态。
