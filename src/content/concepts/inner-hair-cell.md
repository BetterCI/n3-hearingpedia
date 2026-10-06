---
title: "内毛细胞"
english: "Inner Hair Cell"
slug: "inner-hair-cell"
summary: "耳蜗主要的传入感觉受体，将柯蒂器的机械运动转换为受体电位，并经 CaV1.3、otoferlin 和带状突触驱动Ⅰ型螺旋神经节神经元。"
categories: ["ear-cochlea","neuroscience","hearing-loss"]
tags: ["inner-hair-cell","mechanotransduction","ribbon-synapse","otoferlin","CaV1.3","spiral-ganglion","auditory-nerve"]
aliases: ["IHC","cochlear inner hair cell","内毛细胞受体"]
status: draft
depth: standard
last_updated: "2026-10-06"
authors: ["AI 辅助重构"]
reviewer: null
reviewed_at: null
literature_checked_at: "2026-10-06"
illustration: {"src":"figures/inner-hair-cell-transduction.svg","alt":"内毛细胞从 stereocilia 偏转、MET 通道、受体电位、CaV1.3、otoferlin 和 ribbon synapse 到听神经放电的功能链","caption":"内毛细胞把柯蒂器中的机械运动转换为受体电位，再通过带状突触驱动Ⅰ型螺旋神经节神经元。图为教学示意。"}
knowledge_area: "biology"
kind: "anatomy"
key_facts:
  - {label: "核心角色", value: "耳蜗主要传入感觉受体，把机械运动转换为听神经输入"}
  - {label: "解剖位置", value: "沿柯蒂器内侧形成单行，与三行外毛细胞具有不同功能分工"}
  - {label: "主要传入通路", value: "绝大多数耳蜗传入神经纤维属于连接 IHC 的Ⅰ型 SGN"}
  - {label: "突触机制", value: "CaV1.3 触发 Ca²⁺ 进入，otoferlin 参与囊泡融合，谷氨酸激活 SGN"}
  - {label: "编码意义", value: "多个异质带状突触共同参与声强与时序信息的群体编码"}
  - {label: "技术边界", value: "助听器仍依赖 IHC 通路；人工耳蜗绕过 IHC/突触而直接刺激神经"}
references: ["fettiplace-2017","jia-met-2025","holt-met-2025","moser-diversity-2023","jaime-moser-2024","valayannopoulos-dboto-2026","mcgovern-cox-2025","robles-2001"]
batch: 4
order: 46
---

**内毛细胞**（inner hair cell，IHC）是哺乳动物耳蜗中最主要的传入感觉受体。声音经过外耳、中耳和[耳蜗](../cochlea/)机械处理后，IHC 将局部机械运动转换为连续的受体电位，再通过带状突触释放谷氨酸，驱动Ⅰ型螺旋神经节神经元产生动作电位。绝大多数进入中枢听觉系统的外周声学信息都经过这一接口。[1](#ref-fettiplace-2017)

IHC 与[外毛细胞](../outer-hair-cell/)承担不同任务。OHC 主要参与耳蜗主动机械过程、频率选择性和压缩性非线性；IHC 则主要负责把已经经过这些机械处理的信息送入听神经。理解 IHC，需要把**柯蒂器微力学、机械电转导、受体电位、带状突触和螺旋神经节编码**作为一条连续链路来考察。[1](#ref-fettiplace-2017)[8](#ref-robles-2001)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/inner-hair-cell-transduction.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/inner-hair-cell-transduction.svg" alt="内毛细胞从毛束偏转到听神经放电的功能链" width="1200" height="720" loading="lazy" /></a>
<figcaption><p><strong>图1｜内毛细胞的机械—电—突触—神经转换链。</strong> 柯蒂器运动使毛束偏转，机械电转导通道改变开放概率，引起受体电位；基底侧 CaV1.3 通道和 otoferlin 参与突触囊泡释放，谷氨酸随后驱动Ⅰ型螺旋神经节神经元。图中箭头表示功能顺序，不表示各过程只有单一分子或单一路径。<a href="#ref-fettiplace-2017">1</a><a href="#ref-jia-met-2025">2</a></p></figcaption>
</figure>

## 解剖位置与 IHC／OHC 分工

哺乳动物柯蒂器通常具有一行 IHC 和三行 OHC。IHC 位于 Corti 隧道内侧、靠近蜗轴；OHC 位于外侧。两类细胞都具有 stereocilia 毛束和机械电转导装置，但它们在成熟耳蜗中的系统功能明显不同。[1](#ref-fettiplace-2017)

成熟耳蜗绝大多数传入螺旋神经节神经元属于Ⅰ型 SGN，并与 IHC 形成突触。单条Ⅰ型 SGN 通常只接受一个 IHC 的输入，而一个 IHC 可与多条Ⅰ型 SGN 建立独立突触。因此，一个频率位置上的 IHC 输出并不是一条单一神经通道，而是由多个并行传入单元共同承载。[1](#ref-fettiplace-2017)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/ihc-vs-ohc.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/ihc-vs-ohc.svg" alt="内毛细胞与外毛细胞的主要功能分工" width="1200" height="650" loading="lazy" /></a>
<figcaption><p><strong>图2｜IHC 与 OHC 的主要功能分工。</strong> OHC 主要影响耳蜗机械输入，IHC 主要形成传入神经输出。两类细胞共享部分机械电转导机制，但其下游功能、神经连接和病理后果不同。图中数量和位置为教学示意，不代替组织学比例测量。<a href="#ref-fettiplace-2017">1</a></p></figcaption>
</figure>

## 毛束运动与柯蒂器微力学

IHC 顶端具有阶梯状排列的 stereocilia。相邻 stereocilia 之间由 tip link 等结构连接，毛束朝兴奋方向偏转时，tip-link 张力增大并提高机械电转导通道的开放概率。

IHC 毛束的实际位移并不能由基底膜位移直接推出。成熟哺乳动物 IHC 的毛束并非简单固定插入盖膜；reticular lamina、tectorial membrane、subtectorial fluid 以及局部柯蒂器形变共同决定 IHC 毛束受到的力学刺激。因此，“某处基底膜振动多少”与“该处 IHC 毛束偏转多少”属于不同层面的量。[8](#ref-robles-2001)

## 机械电转导：从毛束偏转到受体电流

毛束向兴奋方向偏转后，机械电转导（mechano-electrical transduction，MET）通道开放，来自内淋巴的阳离子进入毛细胞，引起去极化；反方向偏转则降低通道开放概率，使膜电位朝相反方向变化。[1](#ref-fettiplace-2017)

2025 年综述将当前 MET 复合体中的关键组分概括为 TMC1/2、TMIE、LHFPL5、CIB2/3、CDH23 和 PCDH15 等。CDH23 与 PCDH15 参与 tip-link 结构，TMC1/2 被广泛视为通道孔道核心候选组分。[2](#ref-jia-met-2025)

不过，关键分子被识别并不意味着完整门控机制已经解决。MET 复合体的完整结构、机械力怎样传递到通道、以及不同组分如何共同控制门控构象，仍是当前毛细胞生物物理的重要问题。[2](#ref-jia-met-2025)[3](#ref-holt-met-2025)

## 内淋巴环境与电化学驱动力

IHC 顶端浸润在内淋巴中。内淋巴具有高 K⁺ 浓度和正的 endocochlear potential，这一特殊环境为 MET 电流提供强电化学驱动力。进入细胞的 K⁺ 和其他阳离子使 IHC 去极化，随后由基底外侧膜的离子通道和突触装置把这种变化转换为神经输出。[1](#ref-fettiplace-2017)

因此，IHC 的机械电转导不是孤立的“毛束通道事件”。它依赖 stria vascularis、内淋巴离子组成、endocochlear potential 以及 IHC 基底外侧电导共同维持。任何一个环节异常，都可能改变最终声学—神经转换。

## 受体电位及其频率依赖

成熟 IHC 主要以**渐变式受体电位**工作，而不是像成熟神经元那样为每个声周期产生全或无动作电位。声音引起的 MET 电流改变膜电位，再由膜电位控制突触释放；动作电位主要在突触后的 SGN 中形成。[1](#ref-fettiplace-2017)

IHC 膜具有电容和离子通道形成的时间常数，因此对快速电位变化呈低通特性。在较低频率，受体电位中的周期性成分能够较好跟随刺激；频率升高后，快速交流成分逐渐被滤除，平均去极化成分的重要性增加。[1](#ref-fettiplace-2017)

这一区别对[时域精细结构](../temporal-fine-structure/)和[音高感知](../pitch-perception/)尤其重要。低频下，IHC 受体电位和突触释放可以支持更强的相位同步；高频下，听神经表征则更多依赖平均放电率、群体模式和耳蜗位置线索。不能把声波中的每个快速周期都理解为被 IHC 膜电位逐周期完整复制。

## CaV1.3、otoferlin 与带状突触

IHC 基底外侧分布多个 presynaptic active zones。IHC 去极化后，L 型 CaV1.3 通道开放，使 Ca²⁺ 在释放位点附近形成局部高浓度区域，并触发突触囊泡融合。释放的谷氨酸作用于Ⅰ型 SGN 末梢，使神经元产生动作电位并把信息传向耳蜗核。[1](#ref-fettiplace-2017)

IHC 使用的突触释放机制具有高度专门化特征。**Otoferlin（OTOF）** 是成熟 IHC 中 Ca²⁺ 触发囊泡融合和囊泡循环的重要蛋白。OTOF 功能缺失时，毛细胞本体和部分机械转导功能可以保留，但 IHC 向 SGN 的突触传递严重受损。这种情况说明，**感觉细胞存在、机械电转导存在和有效神经传输是三个不同层次。**

带状突触（ribbon synapse）使大量囊泡集中在释放位点附近，有利于在持续刺激条件下维持较高释放速率和较高时间精度。这一结构是 IHC 区别于许多普通中枢突触的重要特征，也是[耳蜗突触病变](../cochlear-synaptopathy/)的关键病理接口。[1](#ref-fettiplace-2017)

## 一个 IHC 为什么连接多条 SGN

正常听觉需要覆盖很宽的声强范围，但单条听神经纤维的有效工作范围有限。因此，一个 IHC 通过多条 SGN 构成的群体输出，能够把同一频率位置上的不同声强区间分配到不同神经单元。

Moser 等提出的 **dynamic-range fractionation** 框架强调：不同 SGN 具有不同阈值、自发放电率和工作范围；多个传入单元共同工作，才能使一个 IHC 位置覆盖更宽的输入强度范围。[4](#ref-moser-diversity-2023) 这使 IHC 与[动态范围](../dynamic-range/)和[响度](../loudness/)之间形成直接联系。

## 同一个 IHC 的突触并非重复副本

同一 IHC 上的 active zones 在 Ca²⁺ 通道数量、激活电压、Ca²⁺—囊泡耦合、释放时延和突触后 SGN 性质等方面存在异质性。柱侧（pillar side）与蜗轴侧（modiolar side）突触长期被认为具有结构和功能梯度。[4](#ref-moser-diversity-2023)

2024 年配对记录进一步直接连接了 IHC 突触前性质与 SGN 响应特征：高自发放电率纤维更多与柱侧突触相关，并表现出较低激活阈值、更紧密的 Ca²⁺—释放耦合、更短时延和较高初始释放率。[5](#ref-jaime-moser-2024)

这些结果支持一个更细致的外周编码观点：**同一个 IHC 的多个突触并非简单复制同一信号，而可能在第一突触层面已经对强度和时间信息进行并行分配。** 这一映射在不同物种和人类中的具体形式仍需进一步验证。

## IHC 在时间、强度和频率编码中的作用

### 时间信息

低频条件下，IHC 受体电位中的周期成分可以调制递质释放，从而支持 SGN 对刺激相位形成同步放电。IHC 膜滤波、突触适应、囊泡释放随机性和 SGN 不应期又会限制最终时间精度。因此，声学信号包含精细时间结构，并不意味着听神经完整保留了全部时间细节。[1](#ref-fettiplace-2017)

### 强度信息

声级升高通常会增加 IHC 去极化和突触释放，但最终 SGN 输出还受到上游耳蜗压缩、突触异质性、神经阈值、自发放电率、适应和饱和等因素共同影响。[4](#ref-moser-diversity-2023) 声强编码因此更接近一个群体响应问题，而不是单一的“声压级—IHC 电位—放电率”线性关系。

### 频率与音高信息

IHC 接收到的频率选择性主要由上游耳蜗机械和局部[频位映射](../tonotopy/)塑造。某个 IHC 位于哪一段耳蜗，决定了它主要接收哪个频率区域的机械输入；低频下，它又可通过受体电位和突触释放保留一定时间周期信息。这构成正常听觉中 place 与 timing 信息共同进入神经系统的外周基础。

## 发育中的 IHC

发育早期的 IHC 与成熟 IHC 在电生理上并不相同。在听觉开始前，IHC 可以出现 Ca²⁺ 依赖的自发动作电位，并参与塑造早期听觉通路的自发活动。随着耳蜗成熟，膜离子通道、突触结构和释放机制发生改变，IHC 转变为以渐变受体电位和高精度突触传输为主的成熟感觉受体。[1](#ref-fettiplace-2017)

因此，成年 IHC 的受体电位和突触机制不能直接套用于发育期耳蜗。

## IHC 病理的不同层级

IHC 功能异常并不等于“细胞已经死亡”。病理可以发生在多个层级：

| 层级 | 可能异常 | 主要后果 |
| --- | --- | --- |
| 毛束／MET | TMC1、TMIE、PCDH15 等相关异常 | 毛束运动不能正常转换为受体电流 |
| 基底外侧电生理 | 离子通道或膜性质异常 | 受体电位和突触驱动改变 |
| 突触释放 | OTOF 等功能异常 | MET 可存在，但 IHC→SGN 传递失败 |
| 带状突触 | 突触丢失或功能改变 | 神经输入数量、阈值和时序改变 |
| IHC 本体 | 细胞损失 | 局部声学—神经转导链中断 |

MET 相关分子异常与遗传性听力损失之间已有大量机制证据，但具体临床表型依赖基因、变异类型和受累环节，不能从单一分子名称直接预测全部听觉表现。[2](#ref-jia-met-2025)

## 临床测量能否直接评价 IHC

目前没有一种常规无创临床检查可以直接给出活体人耳 IHC 的数量或完整功能状态。不同测量只能观察链路中的不同部分：

| 测量 | 主要反映层面 | 对 IHC 的解释边界 |
| --- | --- | --- |
| 纯音听阈 | 整条听觉通路的检测敏感度 | 不能定位到 IHC |
| OAE | 主要反映 OHC 与耳蜗机械 | OAE 正常不保证 IHC 或突触正常 |
| cochlear microphonic | 毛细胞受体电流的群体成分 | 常受 OHC 贡献影响 |
| ABR／CAP | 神经群体同步输出 | 同时受 IHC、突触、SGN 和记录条件影响 |
| EcochG | 耳蜗与听神经近场反应 | 多成分叠加，特异性有限 |
| 语音／时间任务 | 系统级行为功能 | 不能单独定位病理层级 |

因此，“OAE 正常而 ABR 异常”可以提示毛细胞机械功能与神经同步之间存在脱节，但不能仅凭这一组合确定具体 IHC 或突触病理。

## IHC、耳蜗突触病变与听力图

[耳蜗突触病变](../cochlear-synaptopathy/)的关键病理界面位于 IHC presynaptic active zone 与Ⅰ型 SGN 末梢之间。IHC 本体仍然可以存在，纯音听阈也未必与突触数量一一对应，但传入神经通路的数量、时序和强度编码可能已经发生改变。

这也是为什么“hair-cell survival”“正常纯音阈值”和“正常耳蜗神经输出”不能互相替代。

## 与助听器和人工耳蜗的关系

[助听器](../hearing-aid/)通过改变进入耳蜗的声学输入工作，因此仍依赖残余 IHC 机械电转导、突触释放和 SGN 传输。若主要限制位于 IHC 突触或听神经，增加声学增益不一定能够恢复相同比例的有用信息。

[人工耳蜗](../cochlear-implant/)则绕过 IHC 的机械电转导和 IHC–SGN 化学突触，通过电刺激直接招募耳蜗神经元。因此，即使 IHC 严重受损或突触释放失败，只要仍存在可刺激的神经组织，电听觉仍可能建立。两种技术的根本区别不只是“一个放大声音、一个更强”，而是**是否依赖天然 IHC–SGN 接口**。

## OTOF 基因治疗提供了什么证据

OTOF 相关耳聋是理解 IHC 突触功能的一个重要人类模型。患者的毛细胞结构可以部分保留，但 otoferlin 缺陷会严重损害 IHC 囊泡释放，使声学输入难以形成正常听神经活动。

DB-OTO 研究采用双 AAV 载体在 OTOF 相关重度耳聋儿童中恢复 otoferlin 表达，并报告部分受试者出现显著听敏感度改善；12 名接受治疗的儿童中有 3 名达到正常听敏感度范围。[6](#ref-valayannopoulos-dboto-2026)

这项结果提供了一个重要的临床概念验证：**当 IHC 本体和下游神经通路仍具备足够结构基础时，修复特定突触分子缺陷可以重新建立声学—神经传输。** 这一结论不能外推到所有遗传性听力损失，也不能替代对长期语言、空间听觉和神经编码质量的持续随访。

## 毛细胞再生为什么仍然困难

成熟哺乳动物耳蜗缺乏像鸟类和鱼类那样稳定的功能性毛细胞再生能力。支持细胞重编程、转录因子调控和基因治疗已经产生大量实验进展，但从“出现 hair-cell-like cell”到“恢复可用听觉”之间仍有很长距离。[7](#ref-mcgovern-cox-2025)

一个真正具有功能的再生 IHC 至少需要重新建立：
- 正确的 apical–basal identity；
- 正确的 stereocilia 极性和形态；
- 可工作的 MET apparatus；
- 成熟的基底外侧膜电生理；
- CaV1.3 active zones 与带状突触；
- 适当的 SGN 再支配；
- 与原有 tonotopic organization 相匹配的连接。

因此，再生研究的终点不能只用毛细胞样细胞数量定义，还需要证明机械转导、突触传输、神经编码和行为功能得到恢复。[7](#ref-mcgovern-cox-2025)

## 当前研究问题

### MET 复合体的结构和门控机制

TMC1/2、TMIE、CIB2/3、LHFPL5 等关键分子已经被确认，但机械力怎样传递到通道孔道、完整复合体如何重排和门控，仍缺少完整模型。[2](#ref-jia-met-2025)[3](#ref-holt-met-2025)

### 人类 IHC 与动物模型的对应程度

大多数 IHC 膜电生理、Ca²⁺ 纳米域和突触配对记录来自啮齿动物。人类组织研究和临床间接指标仍不足以重建同等精度的人类 IHC 生理，因此跨物种外推需要保留明确边界。

### 突触异质性如何形成 SGN 功能亚型

现有配对记录已经把部分突触前差异与 SGN 自发率、阈值和时序响应联系起来，但不同 SGN 分子亚型、pillar–modiolar 梯度与真实声刺激下的完整功能映射尚未统一。[4](#ref-moser-diversity-2023)[5](#ref-jaime-moser-2024)

### 一个 IHC 怎样覆盖宽声强范围

dynamic-range fractionation 为 IHC 多突触和 SGN 异质性提供了有吸引力的解释，但不同突触、神经亚型、适应和传出调节各自贡献多少，仍需要定量模型和体内验证。[4](#ref-moser-diversity-2023)

### 如何同时维持高吞吐量和高时间精度

IHC 突触需要在连续声音下持续释放，同时保持对快速时间变化的敏感。囊泡库补充、Ca²⁺ 耦合、释放随机性和突触适应怎样共同决定最终时间精度，是连接细胞生理与听觉心理物理的重要问题。

### 哪些 IHC 病理具有可逆治疗窗口

OTOF 已经提供了基因治疗的临床概念验证，但 MET 蛋白异常、IHC 丢失、突触退化和 SGN 退化属于不同病理层级，治疗窗口和可逆性不能简单类推。[6](#ref-valayannopoulos-dboto-2026)[7](#ref-mcgovern-cox-2025)

### 能否建立 IHC 特异的人体生物标志物

目前 OAE 更偏 OHC 与耳蜗机械，ABR、CAP 和 EcochG 又同时包含多个环节。能够在活体中区分 OHC dysfunction、IHC transduction dysfunction、IHC synaptic dysfunction 和 SGN dysfunction 的多模态指标体系仍然缺失。

### 再生 IHC 后能否恢复正确神经连接

真正的功能再生不仅要求产生新的 IHC，还要求重新建立正确的带状突触、SGN 连接和 tonotopic organization。细胞数量恢复与听觉编码恢复应分别验证。[7](#ref-mcgovern-cox-2025)

## 常见解释错误

**“IHC 负责耳蜗主动放大。”**  
主要主动机械放大与 OHC 有关，IHC 的核心任务是传入感觉转导。

**“IHC 直接产生听神经动作电位。”**  
成熟 IHC 主要产生渐变受体电位，经化学突触驱动 SGN；动作电位主要在神经元中形成。

**“一个 IHC 对应一根听神经纤维。”**  
一个 IHC 与多条Ⅰ型 SGN 形成独立带状突触。

**“所有 IHC 突触只是同一信号的复制。”**  
突触前性质和对应 SGN 响应存在系统异质性。[5](#ref-jaime-moser-2024)

**“OAE 正常即可说明 IHC 正常。”**  
OAE 主要反映 OHC 和耳蜗机械功能，不能排除 IHC、突触或神经异常。

## 与其他词条的关系

- [耳蜗](../cochlea/)：IHC 所处的完整机械—电环境；
- [外毛细胞](../outer-hair-cell/)：与 IHC 形成互补的机械反馈系统；
- [听觉滤波器](../auditory-filter/)：IHC 接收的频率选择性机械输入；
- [动态范围](../dynamic-range/)：IHC–SGN 群体怎样覆盖宽声强范围；
- [时域精细结构](../temporal-fine-structure/)：低频时间信息怎样进入传入神经；
- [音高感知](../pitch-perception/)：place 与 timing 信息怎样进入音高编码；
- [耳蜗突触病变](../cochlear-synaptopathy/)：IHC–SGN 接口的病理；
- [听觉脑干反应](../auditory-brainstem-response/)：外周同步神经输出的间接测量；
- [助听器](../hearing-aid/)：仍依赖残余 IHC–SGN 通路；
- [人工耳蜗](../cochlear-implant/)：绕过 IHC 与带状突触的人工神经接口。

## 研究沿革

IHC 最初常被概括为“把耳蜗振动转换成神经信号的感觉细胞”。现代研究则把它视为一个更复杂的多级接口：**机械输入经分子级 MET 转换为渐变受体电位，再由多个具有异质性的带状突触把信息分配到不同 SGN。**

因此，当前问题已经从“一个 IHC 是否响应声音”推进到：**同一个 IHC 如何在宽声强范围内同时保存足够的强度、时间和频率信息，并通过多个不完全相同的突触形成可供中枢利用的神经群体表征。** 这一问题把耳蜗力学、分子生物学、突触神经科学、心理声学、听力损失和人工听觉连接在同一条研究链上。
