---
title: "双耳可懂度级差"
english: "Binaural intelligibility level difference"
slug: "binaural-intelligibility-level-difference"
summary: "连接双耳同相与反相语音测试及双耳去掩蔽评价。"
categories: ["binaural","audiology"]
tags: ["BILD"]
aliases: ["BILD","双耳可懂度差","双耳去掩蔽"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["he-antiphasic-zin-2026","de-sousa-2020"]
illustration: {"src":"figures/binaural-phase.svg","alt":"左右耳同相和目标反相的理想纯音波形","caption":"教学示意：1000 Hz 纯音显示同相与反相；左右 RMS 不变。DIN 的 N0Sπ 例子另规定噪声同相。本图不代替 ZIN 版本的刺激配置。"}
order: 28
knowledge_area: "measurement"
kind: "metric"
key_facts: [{"label":"缩写","value":"BILD"},{"label":"单位","value":"dB（两项可比 SRT 的差）"},{"label":"关键条件","value":"双耳关系、基线、相减方向与评分"}]
---

**双耳可懂度级差**（binaural intelligibility level difference，BILD）是规定双耳关系条件之间的语音识别阈值差。它用于描述特定双耳解[掩蔽](../masking/)或测试收益，必须注明刺激配置与相减方向；纯音检测的 BMLD 和全部空间释放不是同一指标。[2](#ref-de-sousa-2020 "Improving Sensitivity of the Digits-In-Noise Test Using Antiphasic Stimuli")

## 定义与分类

BILD 是配对差值，[SRT](../speech-reception-threshold/)是构成它的阈值，[双耳整合](../binaural-integration/)是更广的功能。目标反相与延迟属于不同操作，二耳 RMS 相同也不意味着跨耳信息相同。反相 ZIN 的指标与验证应按原版本定义，不能使用 DIN 示例替代专属参数。

### 级差的方向与单位

若阈值以 SNR 表示，可定义：

$$
\mathrm{BILD}=\mathrm{SRT}_{N_0S_0}-\mathrm{SRT}_{N_0S_\pi}.
$$

两项单位同为 dB SNR，差值单位为 dB；正值表示本定义下反相条件所需 SNR 更低。例如 −4 与 −9 dB SNR 的差为 5 dB。示例仅解释符号，不是常模或判定界限。若论文使用不同基线或反向相减，应保留其定义。

### 与 BMLD 和空间释放的区别

纯音检测中的双耳掩蔽级差 BMLD 评价目标是否被检测到；BILD 评价语音识别阈值，两者任务不同。自由声场的空间释放还可包含头影和更好耳优势，不能将所有双耳 SRT 改善都命名为同一种级差。

两种相位条件单耳能量相同，有助于约束纯能量解释；但行为差值仍取决于噪声、语言材料、频率内容和听者状态，不能单凭 BILD 数值定位一个神经损伤位置。

## 原理与表征

### 先写差值方向

对于在噪声中以 dB SNR 报告的阈值，本词条采用：

$$
\mathrm{BILD}=\mathrm{SRT}_{\mathrm{diotic}}-
\mathrm{SRT}_{\mathrm{antiphasic}}.
$$

$\mathrm{diotic}$ 表示规定的双耳相同呈现条件，$\mathrm{antiphasic}$ 表示测试规定的反相配置。正值表示反相条件需要更低的 SNR，单位 dB；若论文采用反向相减，数值符号也会改变。必须同时说明究竟对语音还是噪声实施反相，以及另一信号的两耳关系。

### 为什么两耳关系会影响阈值

两耳接收到的目标与掩蔽声关系不同，可能提供有助于分离的信息。BILD 用行为阈值差描述这种效果，却不单独确定某一个神经机制。它也不是“两耳比一耳好多少”，因为比较条件可以均为双耳。

反相是相位操作，不能等同于对所有频率添加同一个时间延迟。纯音的双耳掩蔽级差（BMLD）与[语音可懂度](../speech-intelligibility/)级差，材料和任务均不同，不能直接互换。

## 测量与研究方法

### 配对比较与误差

差值需要同一受试者在可比材料、噪声和计分条件下测量。两次 SRT 自身的误差会传播到差值，顺序、学习与疲劳也可能影响结果。报告差值时应同时展示两种原始阈值及不确定性。

### 统计上应保留配对关系

同一个体两次阈值都含测量误差。差值的不确定性既取决于各条件误差，也取决于二者相关性；只给两组均值误差棒不足以说明配对差的可靠性。顺序应平衡，必要时重复测量，以区分练习和相位条件效应。

## 应用与解释边界

### 研究应用

2026 年反相 ZIN 研究比较测试配置，考察阈值和 BILD 与听力损失指标的联系。其验证提供特定版本和人群中的筛查线索，不构成所有语言和设备的通用常模。[1](#ref-he-antiphasic-zin-2026 "Optimizing the Chinese Zodiac-in-Noise Test With Antiphasic Stimuli for Better Hearing Loss Detection")

ZIN 专属测试细节目前依据摘要与书目整理，DIN 示例另有来源。测试的精确反相实现、适应规则和常模分层仍需专业审阅者逐项阅读全文复核后补充。

### 在筛查中的用途与边界

反相 ZIN 的正式研究将双耳级差与听力状态及较差耳检出联系起来，提供版本特定的验证。[1](#ref-he-antiphasic-zin-2026 "Optimizing the Chinese Zodiac-in-Noise Test With Antiphasic Stimuli for Better Hearing Loss Detection") 低频敏感度、左右不对称以及较好耳作用应分开考察。一个 BILD 指标不能取代整张听力图、病因判断或多任务听觉评价。

复现时先检验左右波形、相位及 RMS，再检查各条件阈值和个体差值；若只重现平均 BILD 而两项绝对阈值均异常，仍不能认定测试方法已经正确实现。

## 分析示例

### 一个明确的相位条件示例

在数字噪声研究中，常用 $N_0S_0$ 表示两耳噪声及目标同相，$N_0S_\pi$ 表示噪声同相、目标跨耳反相；目标反相是一个耳信号乘以 −1，不会改变其单耳 RMS。二者因此可以在单耳能量相同的条件下改变跨耳关系。[2](#ref-de-sousa-2020 "Improving Sensitivity of the Digits-In-Noise Test Using Antiphasic Stimuli")

这是 DIN 的明确示例，不据此替代 ZIN 各版本的实际实现。若研究延迟而非反相，对宽带信号各频率的相位差不同，也不能把两种处理统称为相同条件。

### 解释示例：差值相同仍有不同来源

两名听者 BILD 都为 4 dB，一名两条件阈值都较好，另一名两条件都较差。差值相同不意味着绝对语音能力相同。另一个听者差值较小，也可能来自同相基线已经很好、反相收益较小或测量波动，不能自动归因于某种损伤。

可同时展示两个条件的阈值散点和配对连线，再观察差值与频率相关听力指标。若要判定筛查意义，应使用对应版本的常模、参照目标和验证数据。[1](#ref-he-antiphasic-zin-2026 "Optimizing the Chinese Zodiac-in-Noise Test With Antiphasic Stimuli for Better Hearing Loss Detection")

BILD 是任务中利用双耳关系的指标之一。与纯音检测、定位或互补频带整合之间的关系，是需要研究的问题，不能把一个正常差值视为所有双耳功能均正常。

## 研究沿革

2020 年正式 DIN 反相研究提供相位条件与筛查评价背景，2026 年正式反相 ZIN 研究将双耳级差与听力状态联系。它们支持对应材料、人群和版本的应用，而不建立脱离任务的普适界限或病变定位规则。[2](#ref-de-sousa-2020 "Improving Sensitivity of the Digits-In-Noise Test Using Antiphasic Stimuli") [1](#ref-he-antiphasic-zin-2026 "Optimizing the Chinese Zodiac-in-Noise Test With Antiphasic Stimuli for Better Hearing Loss Detection")
