---
title: "深度学习"
english: "Deep Learning"
slug: "deep-learning"
summary: "作为《机器学习》的配套篇，从多层表示与张量形状进入反向传播、稳定训练、卷积、循环网络和Transformer，再理解语音自监督、序列对齐、生成学习、泛化与实时评价；以可复算模型说明梯度、掩码、未来信息和概率输出的边界。"
categories: ["research-methods", "ai-hearing", "signal-processing", "neuroscience"]
tags: ["基础课程", "深度学习", "反向传播", "卷积神经网络", "Transformer", "自监督学习", "序列建模", "泛化"]
aliases: ["深度学习基础", "深层神经网络", "深度神经网络", "Deep Neural Networks"]
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
  - {label: "课程定位", value: "与机器学习配套，深入多层表示、梯度计算、训练与架构"}
  - {label: "核心区别", value: "表示能力、优化成功、独立泛化和实际获益是不同问题"}
  - {label: "声音连接", value: "波形与时频输入、变长序列、语音预训练、流式处理和评价"}
  - {label: "解释边界", value: "网络单元、注意力权重与高分预测不自动等同生物机制或因果解释"}
references: ["dl-mlp", "dl-backprop", "dl-init", "dl-sgd", "dl-adam", "dl-dropout", "dl-batchnorm", "dl-conv", "dl-rnn", "dl-lstm", "dl-attention", "dl-transformer", "dl-generalization", "dl-resnet", "dl-he-init", "dl-transformer-paper", "dl-adamw", "dl-wav2vec", "dl-hubert", "dl-vae", "dl-gan", "dl-diffusion", "dl-ctc", "dl-calibration", "dl-ce-api", "dl-ln-api", "dl-grad-api"]
order: 1019
---

**深度学习**（deep learning）是使用多层可学习变换来构造表示、完成预测或生成任务的机器学习方法族。“表示”是数据进入后续计算的形式：声音可以从波形变成局部模式、时间序列特征，再变成类别分数或其他输出。深度通常指变换的复合层次，没有跨所有架构通用的“几层才算深”的严格门槛，也不等于参数量、训练轮数或推理链条的长度。[1](#ref-dl-mlp)

本篇与[机器学习](../machine-learning/)配套。前篇建立任务、数据、损失、验证与常见方法的框架；本篇进一步解释多层网络怎样表示函数、怎样计算梯度，以及卷积、循环、注意力和生成模型各自加入什么假设。数学在使用处补充；十幅图及全部数值为原创指定模型或模拟数据，不是听者、患者、神经系统或真实语音基准的实测。

声音应用会贯穿输入表示、时间掩码、序列对齐和延迟，但深度学习的特征不依赖听觉例子才能成立。本篇不列不断变化的排行榜；少量单元和浅网络用于隔离计算机制，不能被当作深层性能比较。文末有三个独立短程序，另提供[完整实验脚本](/n3-hearingpedia/code/deep-learning/experiments.py)，不需下载录音、预训练权重或安装GPU框架。

## 阅读准备与独立阅读

**起步知识。** 能理解函数输入输出、加权求和、平均数和简单概率即可进入。先读网络图、形状与声音任务，再读求导和训练。机器学习是配套参照，不要求先通读；本篇会重新解释参数、损失、验证及训练/推理的区别。

**随用随补。** 向量是一组数，矩阵是按行列排列的数，张量把更多轴保留下来；梯度说明参数微小变化怎样影响一个标量目标。链式法则把复合函数的局部变化率连接起来，批次平均则把多个样本的损失合成训练目标。

**分层阅读。** 第一遍读多层表示、数据形状、训练流程和架构，再读声音研究例子；第二遍复算反向传播、感受野、掩码与对齐路径。需要完整推导时，可按知识点查阅[线性代数](../linear-algebra/)、[微积分](../calculus/)、[概率论](../probability-theory/)及[最优化方法](../optimization-methods/)。

## 多层表示 为什么堆叠变换能改变问题

### 层 参数与非线性

**层**把输入表示变成另一种表示，**参数**是训练拟合的权重、偏置等。**隐藏层**位于输入与最终任务输出之间；**激活函数**对中间数值作规定变换。ReLU为max(0,z)，tanh为有界的双曲正切；它们增加非线性，也改变梯度的传播。神经网络计算单元是数学对象，不能直接等同生物神经元。[1](#ref-dl-mlp)

本文采用批次为行的约定。若第l层宽度为dₗ，B个样本的表示Hₗ为B×dₗ，权重Wₗ为dₗ₋₁×dₗ，偏置bₗ有dₗ个元素，则

$$
\begin{aligned}
H_0&=X,\\
Z_l&=H_{l-1}W_l+\mathbf1 b_l^\mathsf T,\\
H_l&=\phi_l(Z_l).
\end{aligned}
$$

向每行广播同一偏置，不代表给每条样本另学一套偏置。若所有层都仅为不受其他约束的仿射变换，复合后仍是仿射变换；层数本身不会产生非线性。深层表示的作用还依赖连接方式、激活及任务，不能只数方框。[1](#ref-dl-mlp)

### 一个能手算的表示变化

图1的输入是0或1组成的两维向量，标签为异或XOR：00、11为0，01、10为1。四点不能被一条直线严格分开。令s=x₁+x₂，再计算r=ReLU(s)−2ReLU(s−1)+ReLU(s−2)，四点就分别映为0、1、1、0；若用8r−4作为二分类logit，sigmoid输出约0.018或0.982。

这个只有一层隐藏层的例子展示**表示变换**如何让后续简单分类成为可能，不证明“更深总是更好”。某类网络有很强表达能力，也不保证有限样本足够、优化能找到所需参数，或新条件下仍能推广。需要分别讨论函数类、数据、算法和任务。[13](#ref-dl-generalization)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/representation.svg" target="_blank" rel="noopener" aria-label="查看完整图1"><img src="/n3-hearingpedia/figures/deep-learning/representation.svg" alt="一个由输入、三个ReLU单元和输出构成的网络，以及XOR四点在变换后可以区分的分数图" width="1400" height="550" loading="lazy" /></a><figcaption>图1　隐藏单元依次计算ReLU(s)、ReLU(s−1)、ReLU(s−2)，输出线性组合系数为1、−2、1。颜色表示指定分类概率，不是训练得到的准确率；一层隐藏层仅用于说明非线性机制。</figcaption></figure>

## 输入 输出与损失 先把形状写清楚

### 声音可以怎样进入网络

**张量轴**必须对应明确对象。波形常保留批次、通道、采样点；时频输入常保留批次、频带、时间，有时另加通道。代码库的轴顺序并不统一，把时间轴当特征轴做归一化或池化，会实现另一个模型。

短时傅里叶变换和mel滤波组可把声音变成时频表示；若采用功率对数，要写清参考量、下限和单位，例如log(P+ε)与10log₁₀(P/P₀)并非不加约定就相同。对数mel数值不能直接称为校准声压级。原始波形模型也有采样、滤波、局部窗口与归一化等前端设计，并不意味着没有信号处理。[8](#ref-dl-conv)[18](#ref-dl-wav2vec)

### 输出分数不是已经校准的可信度

**logit**是归一化之前的实数分数。互斥C分类常用softmax：pₖ=exp(zₖ)/Σⱼexp(zⱼ)，单个硬标签y的交叉熵为−log pᵧ。计算时可写成logsumexp(z)−zᵧ；logsumexp用最大值平移实现，以减少直接指数的溢出。[25](#ref-dl-ce-api)

二分类单logit可用sigmoid概率σ(z)=1/(1+exp(−z))，损失为log(1+exp(z))−yz；稳定实现使用logaddexp(0,z)。多标签声音事件允许多个标签同时成立，通常需要相应的逐标签目标，不能直接套“所有事件概率之和必须为1”的互斥分类假设。

交叉熵衡量对目标的概率损失，准确率衡量某种决策规则的正确比例，两者不是一回事。官方CrossEntropyLoss的类索引模式接收未归一化logits；先softmax再交给该接口，会改变计算，不能把它当成对原交叉熵的必要步骤。类别权重、软标签、标签平滑和忽略项也会改变具体目标及平均分母，需要核对接口约定。[25](#ref-dl-ce-api)

### 变长输入必须处理填充

把长度不等的序列补成同样长，只是方便并行计算，补入位置并不成为新的真实样本。**填充掩码**标明有效位置，可用于注意力、池化与损失；这三个环节的掩码作用不同，不能只在最后乘一次零就自动修正所有中间计算。

在未加权硬标签的特例中，逐位置平均交叉熵应为有效位置损失之和除以有效位置数。若两条序列有效长度为1和3，分母是4而非补齐后的6。按位置平均与先对每条序列平均再对序列平均，也具有不同权重，应该按任务选择并报告。[25](#ref-dl-ce-api)

## 反向传播 计算梯度不等于更新参数

### 前向 反向与优化器

**前向传播**根据输入和当前参数计算中间表示、输出与损失。**反向传播**利用计算图与链式法则，从标量目标向前面的变量累积局部梯度。**优化器**再用梯度及自身状态更新参数；这三步是相关而不同的操作。反向传播既不是把错误标签“倒放”进网络，也不是只能用于某一种架构。[2](#ref-dl-backprop)

同一个参数可能被多个位置重复使用，例如卷积核或循环权重；其总梯度必须把所有路径的贡献相加。自动微分实现这些规则，但不能替人确认目标、维度和数据划分是否正确。断开计算图、错误的原地修改或重复累积梯度，都可能使计算偏离原先意图。[2](#ref-dl-backprop)

### 平均损失下的矩阵求导

对逐元素激活组成的前馈网络，设最后一层为softmax，P是预测概率，Y是one-hot标签矩阵，目标J为批次平均交叉熵加λ/2倍的权重平方和，偏置不惩罚。记Δₗ为J对Zₗ的数据项梯度，则

$$
\begin{aligned}
\Delta_L&=(P-Y)/B,\\
\nabla_{W_l}J&=H_{l-1}^{\mathsf T}\Delta_l+\lambda W_l,\\
\Delta_{l-1}&=(\Delta_lW_l^{\mathsf T})\odot\phi'_{l-1}(Z_{l-1}).
\end{aligned}
$$

偏置梯度是Δ沿样本轴求和。⊙表示对应元素相乘；隐藏层公式用于存在相应隐藏层的情况。因平均因子1/B已在输出Δ中，后面不能每经过一层再除一次B。若损失按和计算、加入权重、归一化、残差或其他操作，需要按实际计算图调整，不能只套这三行。[2](#ref-dl-backprop)

ReLU在0处不可微，软件需采用明确约定；在其他点常按正侧1、负侧0求导。有限差分比较函数的微小扰动与解析梯度，是**梯度检查**的一种方法；步长太大、太小或跨越非光滑点都可能误导。检查通过核对的是给定计算的实现，不证明目标适合实际任务。

图2的三条二维输入、两个tanh隐藏单元和一个二分类输出，共9个参数。平均损失约0.637418；各梯度与独立中心差分核对。模型很小是为了能逐个追踪链式法则，不作为真实声音网络的尺寸建议。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/backpropagation.svg" target="_blank" rel="noopener" aria-label="查看完整图2"><img src="/n3-hearingpedia/figures/deep-learning/backpropagation.svg" alt="前向计算与反向梯度的功能图，以及九个参数的解析梯度与中心差分比较" width="1400" height="550" loading="lazy" /></a><figcaption>图2　三条输入为(0.2,−0.4)、(1,0.3)、(−0.5,0.8)，标签为0、1、1；参数和顺序见完整脚本。tanh平滑，损失按三条样本平均，无正则项；检查不涉及真实语音准确率。</figcaption></figure>

## 优化 初始化与深层稳定性

### 批次 学习率与训练进度

**小批次**是一次更新所用的样本集合，**step**通常指一次参数更新，**epoch**通常指一次遍历训练集。N条样本、批次大小B且保留最后不满批次时，一个epoch常有ceil(N/B)次更新；梯度累积、分布式采样和丢弃尾批会改变关系。[4](#ref-dl-sgd)

随机梯度下降可写为θ←θ−ηg，其中η为学习率，g为所选批次的梯度。在适当均匀抽样下，批次平均可作为完整数据梯度的估计；这不保证每一步损失下降，更不保证一般非凸深网找到全局最优。学习率、批次、损失缩放和更新次数应一起报告，换更大批次也不自动等价于原过程。[4](#ref-dl-sgd)

### Adam与AdamW的差别不只是名称

Adam维护梯度的一阶矩与平方梯度的指数平均，并作偏差校正，再按坐标调整更新尺度。平方梯度的二阶原始矩不是Hessian，也不直接等同方差；它仍有学习率、数值稳定常数与优化限制。[5](#ref-dl-adam)

普通无动量SGD中，将λθ加入梯度与按相应系数收缩权重可以代数等价；对自适应预条件更新，一般不成立。令D为固定对角尺度，L2惩罚的一步为θ−ηD(g+λθ)，解耦衰减则为(1−ηλ)θ−ηDg。取θ=(2,1)、g=(0.5,−0.25)、D=diag(1,0.1)、η=0.1、λ=0.2，分别得到(1.91,1.0005)和(1.91,0.9825)。这是说明差异的固定D反例，不冒充Adam全部状态更新。[17](#ref-dl-adamw)

### 梯度为何消失或爆炸

**Jacobian（雅可比矩阵）**收集多输入、多输出函数的各个局部偏导。深层反向传播包含许多这类矩阵的乘积。方向上的增益持续小于1可能使梯度很小，持续大于1可能使其很大；饱和激活、初始化、路径结构和数据也会参与。梯度裁剪限制某次更新所用梯度的幅度，有助于控制爆炸，但不能恢复已经丢失的远程梯度信息。[3](#ref-dl-init)

零初始化若使隐藏单元完全对称，它们可能收到相同更新，无法分工。**初始化**不仅设起始数值，也影响信号与梯度的尺度。在线性或适当近似下，Xavier尺度考虑输入和输出宽度；对零偏置、独立零均值对称权重及相应输入条件，ReLU使前激活二阶矩约保留一半，He型权重方差2/fan-in可平衡该尺度。fan-in是一个单元汇入的输入数，卷积中需计入输入通道与核位置。这里说的是二阶矩，不是声称ReLU输出均值仍为0，或真实训练中每层方差严格不变。[3](#ref-dl-init)[15](#ref-dl-he-init)

### 残差连接提供路径 而非自动保证收敛

**残差块**把输出写成h+F(h)，形状不同时可用投影匹配。其局部Jacobian为I+J_F，增加了不同于纯长链的传播路径。它不自动等于恒等映射：J_F接近−I时仍可能抵消，过大时也可能放大。[14](#ref-dl-resnet)

图3比较指定缩放的二阶矩递推与标量Jacobian乘积。100次乘0.5约为7.89×10⁻³¹，100次乘1.01约为2.7048；这些是固定系数的数学例子，不是对所有残差网络训练的预测。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/depth-stability.svg" target="_blank" rel="noopener" aria-label="查看完整图3"><img src="/n3-hearingpedia/figures/deep-learning/depth-stability.svg" alt="不同初始化尺度下ReLU二阶矩的理想递推，以及固定标量Jacobian连乘的缩小和放大" width="1400" height="550" loading="lazy" /></a><figcaption>图3　左侧假定每层同宽、独立对称权重、零偏置，比较权重方差1/n、2/n、4/n；右侧只计算a的L次方，不能据此宣称残差必然消除梯度问题。</figcaption></figure>

## 归一化 随机失活与训练推理状态

### BatchNorm和LayerNorm沿什么轴计算

**BatchNorm**通常为每个特征使用跨批次、并按架构可能包含空间位置的统计量；常见推理模式使用训练时累积的运行统计。**LayerNorm**在每条样本的指定特征维度上计算均值与方差，训练和推理通常都使用当前输入的这些统计。[7](#ref-dl-batchnorm)[26](#ref-dl-ln-api)

二者都可含可学习的缩放和平移，但统计轴、样本依赖与模式不相同。不能因为名称里有“层”，就任意把整个张量全部标准化。方差的具体估计与运行平均更新还需核对实现；归一化有效的机制也不能简化为只解决一个被命名的分布变化。[7](#ref-dl-batchnorm)

图4设三行样本为(1,4)、(3,8)、(5,6)，ε=10⁻⁵、缩放1、平移0。改变第三行会改变第一行的批次归一化结果，却不改变对第一行自身两个特征作LayerNorm的结果。它说明统计依赖，不表示某一种方法在所有声音任务更好。

### Dropout保持的是哪一个期望

**Dropout**在训练时随机屏蔽部分激活。若丢弃率为p、保留概率q=1−p>0，倒置缩放使用m·h/q，其中m为Bernoulli(q)。对固定h且掩码独立，其期望为h，但方差会增加；经过后续非线性以后，平均预测通常不等于直接使用均值激活的预测。[6](#ref-dl-dropout)

单个h=1、p=0.5时，训练激活取0或2，各概率一半；均值为1。若再经过sigmoid，平均约0.6904，而sigmoid(1)约0.7311。推理中关闭这种随机失活是一种规定，不是精确计算了所有随机子网络的非线性平均。[6](#ref-dl-dropout)

### 不记录梯度与推理模式不同

在PyTorch中，eval()改变依赖模块状态的行为，例如常见Dropout与BatchNorm；no_grad()关闭相应作用域的梯度记录。二者作用不同，不能把“禁用梯度”当作自动进入推理状态。冻结部分参数、不更新运行统计和关闭随机操作也需要分别安排。[27](#ref-dl-grad-api)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/normalization-dropout.svg" target="_blank" rel="noopener" aria-label="查看完整图4"><img src="/n3-hearingpedia/figures/deep-learning/normalization-dropout.svg" alt="改变批次其他样本时BatchNorm和LayerNorm对同一样本的影响，以及倒置Dropout保持激活均值但不保持后续非线性预测" width="1400" height="550" loading="lazy" /></a><figcaption>图4　左侧只画第一行的第一个输出，第三行从(5,6)改成(50,60)；右侧p=0.5，sigmoid为后续非线性示例。均为指定数学模型，非框架全配置的逐项仿真。</figcaption></figure>

## 卷积 局部共享与时间因果

### 深度学习中的卷积常是互相关

**卷积层**用局部核在不同位置共享参数。许多库实际计算不翻转核的互相关；称为卷积层是通行术语，但索引不能因此混淆。单通道一维形式可写为y[t]=b+Σⱼw[j]x[ts−p左+jd]，j从0到K−1，s为步长、d为膨胀间隔。[8](#ref-dl-conv)

输入长度L、左右零填充p左与p右时，在相应有效配置下，输出长度为floor((L+p左+p右−d(K−1)−1)/s)+1。卷积可有多个输入/输出通道，参数数目由核长度与通道决定，不随使用同一核的位置数直接成倍增加。

权重共享给出局部结构偏好；它不意味着声音在任何频带平移都具有相同意义。边界填充、步长下采样和频率轴单位都会影响平移性质。下采样也不自动完成抗混叠滤波，应与[数字信号处理](../digital-signal-processing/)中的采样问题一起考虑。

### 感受野不等于实际利用的全部信息

**理论感受野**是结构上可能影响某输出的输入范围。令初始范围r₀=1、间距j₀=1，第l层核长Kₗ、步长sₗ、膨胀dₗ，则rₗ=rₗ₋₁+(Kₗ−1)dₗjₗ₋₁，jₗ=jₗ₋₁sₗ。三层K=3、步长1、膨胀1、2、4，理论范围为15个输入位置。实际权重、激活和输入会影响哪些位置贡献较大，不能把结构可达当成已经利用。[8](#ref-dl-conv)

### 因果卷积和真实延迟

**因果**在这里指时点t的输出只依赖允许的当前及过去输入。步长1时，左补d(K−1)、右不补的一种实现可满足这一索引条件；居中窗口可能使用未来点。图5中20号输入的脉冲会让居中输出在19号位置提前变化，而因果输出从20号起才变化。

即使网络主体因果，居中声学窗口、整段均值方差、双向编码器或其他预处理仍可能访问未来。实时系统要报告采集、分帧等待、模型前视、缓存、计算和输出的整体延迟。以中心时刻标记的25 ms窗口通常需要等待后半窗输入；“模型前视为0”并不自动表示系统总延迟为0。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/convolution-causality.svg" target="_blank" rel="noopener" aria-label="查看完整图5"><img src="/n3-hearingpedia/figures/deep-learning/convolution-causality.svg" alt="20号位置的输入脉冲经过居中与因果局部滤波后的差别，以及三层膨胀卷积的感受野扩展" width="1400" height="550" loading="lazy" /></a><figcaption>图5　左侧核为(0.25,0.5,0.25)，步长1，因果版本左补2个零；右侧K=3、膨胀1/2/4，结构范围为3/7/15。理论范围与真实系统延迟需分别报告。</figcaption></figure>

## 循环网络 序列状态与对齐

### 状态递推与门控

**循环神经网络RNN**通过共享参数更新状态，例如hₜ=φ(xₜWₓ+hₜ₋₁Wₕ+b)。状态可携带历史信息，但有限状态不是原始全部历史的无损副本。训练沿时间展开计算图，再使用时间反向传播；截断展开可节省计算，也限制梯度跨越多长历史。不同录音间是否重置状态应与任务一致。[9](#ref-dl-rnn)

**LSTM**使用门控调节细胞状态、候选信息和输出，使长期信息传递更容易组织；GRU也用门控更新状态。门控不保证所有长依赖都会被学到，门值也不是已观察的生理开关。双向循环网络使用前后文，对离线任务有用，但其输出不能未经修改就声称只使用过去。[10](#ref-dl-lstm)

### CTC怎样在没有逐帧标签时训练

输入声音帧多于输出文字，通常没有每帧精确对应的文字标签。**连接时序分类CTC**引入空白符，并对能够折叠成目标标签串的路径概率求和。基本CTC将给定输入后的路径概率分解为逐时点输出概率的乘积；这是输出路径模型的假设，不意味着原始语音帧彼此独立。[23](#ref-dl-ctc)

折叠规则先合并相邻重复符号，再移除空白。因而a、a、a折叠为a，a、空白、a则为aa；空白不是普通文字空格。目标概率需要求和全部允许路径，实际长序列常用动态规划与对数域计算，不能只取概率最大的单一路径。[23](#ref-dl-ctc)

图6设三帧输出分布均为P(空白)=0.4、P(a)=0.6，并按CTC乘积假设计算。八条路径的总概率为1，折叠为空串、a、aa的概率分别为0.064、0.792、0.144。最可能路径aaa的概率仅0.216，不能代替目标串a的0.792。另取两帧各P(空白)=0.6、P(a)=0.4，贪心会输出空串，但a的路径总概率0.64高于空串的0.36，说明贪心逐帧解码不保证得到概率最大的标签串。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/ctc-alignment.svg" target="_blank" rel="noopener" aria-label="查看完整图6"><img src="/n3-hearingpedia/figures/deep-learning/ctc-alignment.svg" alt="三帧双符号CTC的八条路径、各自概率和折叠标签，以及目标串概率" width="1400" height="550" loading="lazy" /></a><figcaption>图6　先合并相邻重复，再删空白；路径a、空白、a得到aa。每帧的0.4/0.6为教学指定输出，概率乘积和动态规划均独立复核，不是语音识别系统的实测。</figcaption></figure>

## 注意力与Transformer

### 查询 键和值分别做什么

**查询Q**表示当前位置希望匹配什么，**键K**用于比较，**值V**提供聚合内容；这些通常是输入经过可学习投影后的表示。查询数量Tq可以不同于键数量Tk，Q、K的最后一维为dₖ，V的最后一维为dᵥ。缩放点积注意力可写为

$$
\begin{aligned}
A&=\operatorname{softmax}_{\rm row}
\left(QK^{\mathsf T}/\sqrt{d_k}+M\right),\\
O&=AV.
\end{aligned}
$$

M在允许位置为0、屏蔽位置可用−∞表示；每个查询沿允许的键归一化。A的形状为Tq×Tk，O为Tq×dᵥ。除以√dₖ缓和维度增加时点积分数的尺度：在两组分量彼此独立、零均值、单位方差的参考分析中，点积方差为dₖ，真实投影未必满足这些条件。**自注意力**的查询、键和值来自同一序列；**交叉注意力**的查询与键值可来自不同序列。“注意力”是计算名称，不等同心理学的[听觉注意](../auditory-attention/)。[11](#ref-dl-attention)[16](#ref-dl-transformer-paper)

### 因果掩码与填充掩码不能混用

因果掩码限制读取未来位置，填充掩码排除无效键，两者可能需要组合。有效查询至少要有一个允许键；对全为−∞的一行直接计算通常的softmax没有定义，不能假定任意实现都会自动返回零。填充查询的输出和损失还需另行处理。

图7设Q=K=V为四条二维输入。改变最后一条输入时，完整注意力可改变前面位置的输出，只允许当前位置及此前位置的下三角掩码则保持此前三条输出。这个检查只核对单个注意力运算；若前端已经使用未来，后面加因果掩码也不能清除泄漏。

### 完整Transformer还包含哪些结构

**多头注意力**用不同投影并行计算多个聚合，再合并；前馈子层对位置表示作进一步变换，残差与归一化支持信息和梯度传递，位置编码或其他位置机制补充顺序信息。仅有一个注意力矩阵不是完整Transformer。[12](#ref-dl-transformer)

不含位置信息的纯自注意力在相应无掩码条件下具有置换等变性，不能凭空知道原有时间顺序。编码器、因果解码器和编码器—解码器可以有不同可访问上下文；不能把“使用Transformer”直接解释成单向、双向或实时。

标准密集自注意力显式构造长度T的两两分数，相关计算常有T²项，分数矩阵也有T²个元素；前馈与投影另有开销。这是特定实现的分析，不是所有注意力变体都必须存储同样大的矩阵。处理长音频时应同时核对序列长度、降采样、分块和允许的上下文。[16](#ref-dl-transformer-paper)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/attention-masks.svg" target="_blank" rel="noopener" aria-label="查看完整图7"><img src="/n3-hearingpedia/figures/deep-learning/attention-masks.svg" alt="四个位置的完整注意力与因果注意力权重矩阵，以及修改未来位置后前缀输出的差别" width="1400" height="550" loading="lazy" /></a><figcaption>图7　指定输入为(1,0)、(0,1)、(1,1)、(−1,1)，单头Q=K=V，dₖ=2；最后位置改成(6,−5)以检查依赖。权重不自动构成因果解释，掩码结论只适用于这个前端无未来混入的算子。</figcaption></figure>

## 表征学习 自监督与迁移

### 预训练 微调和冻结是不同阶段

**预训练**先在某个目标上学习参数，**微调**再用下游任务数据调整其中一部分或全部参数；**冻结**表示不更新指定参数。线性探测通常只在固定表示上训练较简单的输出层，用于研究表示可利用的信息，但探测成功不等于相应信息在真实系统里以相同方式被使用。[18](#ref-dl-wav2vec)[19](#ref-dl-hubert)

**自监督学习**从数据本身构造目标。声音可遮挡后预测、比较不同视图，或预测离散伪标签。目标依然由研究者设计；增强方式规定什么变化应被忽略，也可能删掉任务重要线索。无人工转写的预训练，不等于整个流程没有任何标签或选择依据。

原始wav2vec 2.0在潜在语音表示中遮挡，通过量化目标的对比任务等训练，再用转写微调识别。HuBERT使用离线聚类得到对齐伪标签，训练遮挡位置预测并可迭代更新目标。它们说明两种设计，不代表所有语音自监督都相同；聚类单元也不能直接当作已确认的真实音素。[18](#ref-dl-wav2vec)[19](#ref-dl-hubert)

### 迁移成功需要重新评价

预训练数据的说话人、语言、设备和内容会影响适用范围。冻结参数仍可能因目标域选择、归一化或校准而使用新数据；测试是否独立，应覆盖整个流程而非仅看主网络有没有更新。外部预训练与自行拟合预处理的使用范围都应记录，不能在未知预训练污染时声称完全严格的未见评价。

应用于声音检测、言语识别、增强或听觉响应预测时，应比较有意义的简单基线，保留新说话人、新会话或目标设备的独立评价。网络层能预测神经响应，也不自动证明层与脑区一一对应；这与[计算神经科学](../computational-neuroscience/)中的机制检验相互关联。

## 生成学习 重建与真实性

### 编码器 解码器与生成目标

**编码器**把输入映为中间表示，**解码器**从表示形成输出；这两个名称本身不指定是Transformer或何种概率模型。自编码器通过重建目标学习表示；**变分自编码器VAE**还引入潜变量分布，用变分目标约束重建与分布近似。潜变量是模型中未直接观测、参与生成数据的随机变量；变分方法用便于计算的分布近似难以直接求出的后验。不能仅因有压缩和重建就称为VAE。[20](#ref-dl-vae)

**生成对抗网络GAN**使用生成器与判别器相互作用的训练目标，学习使生成样本符合指定数据分布。逼真或更受偏好，不等于对某条输入事实更忠实；声音增强或补全尤其要区分改善感知品质、保留内容和凭分布补入内容。[21](#ref-dl-gan)

### 扩散模型的前向加噪与反向学习

一种离散扩散模型设βₜ在0与1之间，aₜ=1−βₜ，前向每步加入独立标准高斯噪声。给定原始x₀，其第t步边缘可写为

$$
\begin{aligned}
\bar a_t&=\prod_{s=1}^t a_s,\\
x_t&=\sqrt{\bar a_t}\,x_0+
\sqrt{1-\bar a_t}\,\epsilon,\quad
\epsilon\sim N(0,I).
\end{aligned}
$$

边缘公式描述一个噪声级别的条件分布；模拟整条Markov前向链时，每一步要按递推使用相应独立增量。反向过程不是把某个已知随机数简单减掉，而要学习由噪声状态形成更接近数据分布的过程。一类训练目标让网络在给定噪声状态与时间时预测加入的噪声，但不同生成模型的目标与采样方式可以不同。[22](#ref-dl-diffusion)

图8只展示指定波形的前向高斯链，没有训练去噪模型。β=0.02，t=10、40、100时的a连乘约为0.8171、0.4457、0.1326；它们是信号系数的平方，不是人耳可懂度，也不等于某次有限样本中实际测得的功率比例。带条件的生成仍需检验内容、失真与目标使用条件，不能由模型家族名称保证保真。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/diffusion-forward.svg" target="_blank" rel="noopener" aria-label="查看完整图8"><img src="/n3-hearingpedia/figures/deep-learning/diffusion-forward.svg" alt="同一条标准化指定波形沿前向高斯链在0、10、40和100步的变化" width="1400" height="800" loading="lazy" /></a><figcaption>图8　512个样点，原始波形由5周与13周正弦合成并标准化，β恒为0.02，各步独立高斯增量，种子20261102。只展示加噪链，不是已训练生成或去噪结果；横轴为归一化位置，不标实际声音频率。</figcaption></figure>

## 泛化 概率校准与评价

### 训练下降不能代替模型选择

**训练集**拟合参数，**验证集**选择超参数、轮数和流程，**测试集**用于约定后的独立评价。一个同说话人多片段的数据集，可以有片段数很多但独立说话人很少的问题；随机切片是否合理取决于部署目标，不能只凭网络很大就忽略数据结构。[13](#ref-dl-generalization)

**早停**按验证表现选择训练检查点，是正则化与模型选择的一种方式；反复试验、选择种子或挑选最有利的检查点也会消耗验证信息。训练和验证差距可能来自过拟合，也可能混有分布差异，应该核查数据与过程。

图9为隔离训练与选择，用一层32个tanh单元的回归网络拟合18个指定输入，目标为0.7sin(3πx)加标准差0.25的高斯噪声。Adam固定训练12000步，在每100步检查点中按96条独立验证记录选择。选中的600步与最终12000步，训练MSE约0.03191与0.0006805；已知教学总体的期望MSE约0.09717与0.13427。继续训练降低了本次训练误差，却没有降低该总体风险。

总体风险由指定均匀输入分布的数值求积加0.0625噪声方差得到，不是额外测试数据；检查点选择只使用验证损失，没有使用这个已知总体风险。该小模型不是深度优劣实验，曲线也不宣称所有网络、数据和优化都呈同一形状。[13](#ref-dl-generalization)

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/training-selection.svg" target="_blank" rel="noopener" aria-label="查看完整图9"><img src="/n3-hearingpedia/figures/deep-learning/training-selection.svg" alt="指定tanh回归网络的训练、验证和已知总体期望MSE，以及按验证集选择的检查点和最终检查点" width="1400" height="550" loading="lazy" /></a><figcaption>图9　种子20261102，18个等距训练输入、96个独立均匀验证输入，均有独立高斯噪声；32个tanh单元，Adam学习率0.01，12000次全批更新。总体期望使用256点Gauss–Legendre求积并计噪声方差，不参与选择。</figcaption></figure>

### 概率归一化不等于概率校准

**校准**关心报出的概率与相应事件频率是否相符。softmax把分数归一化，但不能自动保证在目标人群中校准；模型可以很自信地错。温度缩放用正温度T把logits改为z/T，通常在独立校准数据上拟合；同一样本内的类别排序不变，但概率与对数损失会改变。[24](#ref-dl-calibration)

图10设总体Y为Bernoulli(0.6)，模型对每条样本都预测类别1、概率0.9。取logit=log9，T=log9/log1.5约5.4190后，概率变为0.6，已知总体期望对数损失由0.98425降到0.67301 nat，0.5阈值下期望准确率仍为0.6。这是已知总体的精确教学算例，不是使用同一批测试标签调温后又宣称获得独立效果。现实校准也可能在分布变化后失效。[24](#ref-dl-calibration)

### 声音研究还要测什么

类别不平衡时，应同时报告相应的召回、精确率、阈值与误判代价；序列识别要明确字/词错误率的单位、解码条件和语言模型；增强除了信号指标，还应核查内容、主观品质和适用听者。实时应用则报告整体延迟与资源。训练损失、离线基准和实际听觉获益之间，需要分别建立证据。

<figure class="encyclopedia-figure"><a href="/n3-hearingpedia/figures/deep-learning/calibration.svg" target="_blank" rel="noopener" aria-label="查看完整图10"><img src="/n3-hearingpedia/figures/deep-learning/calibration.svg" alt="正温度缩放怎样改变固定logit的概率，以及指定Bernoulli总体中的精确期望对数损失" width="1400" height="550" loading="lazy" /></a><figcaption>图10　logit=log9，总体P(Y=1)=0.6，最优温度约5.4190；正温度不改变本例类别排序和0.5决策结果。已知总体仅用于数学示范，不是实际测试集上的校准操作。</figcaption></figure>

## 三个复算练习与研究实践

以下使用Python、NumPy和SciPy，输入全部就地指定。完整脚本包含训练、CTC和图中其他模型；无需真实录音。接口说明参考PyTorch版本文档，但这些程序不依赖PyTorch。

### 练习一 对照一个小网络的梯度

```python
import numpy as np
from scipy.special import expit
X = np.array([[.2, -.4], [1., .3], [-.5, .8]])
y = np.array([0., 1., 1.])
theta = np.array([.3, -.2, .5, .4, .1, -.1, .7, -.6, .05])

def loss_grad(t):
    W, b, v, c = t[:4].reshape(2, 2), t[4:6], t[6:8], t[8]
    h = np.tanh(X @ W + b)
    z = h @ v + c
    delta = (expit(z) - y) / len(y)
    hidden = delta[:, None] * v * (1 - h*h)
    grad = np.r_[(X.T @ hidden).ravel(), hidden.sum(0),
                 h.T @ delta, delta.sum()]
    return np.mean(np.logaddexp(0, z) - y*z), grad

eps = 1e-5
numeric = np.array([(loss_grad(theta + eps*e)[0] -
                     loss_grad(theta - eps*e)[0]) / (2*eps)
                    for e in np.eye(len(theta))])
loss, grad = loss_grad(theta)
print(loss, np.max(np.abs(grad - numeric)))
assert np.allclose(grad, numeric, atol=1e-8)
```

再问：若忘记批次平均，哪些梯度会多乘3？若在每层都再除以3，又会发生什么？

### 练习二 修改未来输入 检查因果掩码

```python
import numpy as np
from scipy.special import logsumexp
X = np.array([[1., 0.], [0., 1.], [1., 1.], [-1., 1.]])
allow = np.tril(np.ones((4, 4), dtype=bool))

def attend(x, causal):
    scores = x @ x.T / np.sqrt(x.shape[1])
    if causal:
        scores = np.where(allow, scores, -np.inf)
    A = np.exp(scores - logsumexp(scores, axis=1, keepdims=True))
    return A @ x

changed = X.copy()
changed[-1] = [6., -5.]
assert np.allclose(attend(X, True)[:3], attend(changed, True)[:3])
print("完整注意力前缀变化：",
      np.max(np.abs(attend(X, False)[:3] - attend(changed, False)[:3])))
```

这只证明当前算子的前缀依赖关系；若X先经过整段统计归一化，为什么上述“过去不变”的前提可能已经不成立？

### 练习三 填充不应偷偷改变损失分母

```python
import numpy as np
from scipy.special import logsumexp
z = np.array([[[2., 0.], [100., -100.], [-100., 100.]],
              [[0., 2.], [2., 0.], [0., 2.]]])
y = np.array([[0, 0, 0], [1, 0, 1]])
valid = np.arange(3)[None, :] < np.array([1, 3])[:, None]
scores, labels = z[valid], y[valid]
loss = np.mean(logsumexp(scores, axis=1) -
               scores[np.arange(len(labels)), labels])
print(valid.sum(), loss)
assert valid.sum() == 4
assert np.isclose(loss, np.logaddexp(0, -2))
```

改变补入位置的logits，核对本例有效位置损失不变；再思考为何这不能修复先前已经混入填充的注意力或池化。

### 留下能够复查的研究记录

记录任务和目标人群、样本与独立组数、输入单位与各轴、预测时能看到的内容、训练验证测试划分；再记录模型、初始化、损失分母、优化器、学习率、随机种子、预训练来源和选择规则。保存最佳与最终检查点的含义，区分训练状态与推理状态。

报告时保留简单基线、分组及条件差异、相应不确定性、整体延迟和失败情形。随机种子有助于追踪一次运行，但并不保证不同硬件、算法和软件版本逐位一致。本篇的梯度、数值和来源核对可排除一部分实现与表述错误，不能替代独立实证或外部专业审阅。
