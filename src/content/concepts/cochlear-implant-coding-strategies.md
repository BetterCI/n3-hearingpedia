---
title: 人工耳蜗信号处理策略
english: Cochlear Implant Sound Coding Strategies
slug: cochlear-implant-coding-strategies
summary: 从临床编码、官方设备文档和仿真仓库比较声音到电刺激的转换，并区分研究进展与临床应用。
categories: ["cochlear-implants","signal-processing","ai-hearing"]
tags: [sound-coding, cis, ace, speak, mp3000, fsp, fs4, hires, current-steering, electrodogram, deepace]
aliases: [人工耳蜗编码策略, 人工耳蜗声音编码策略, CI coding strategies, speech coding strategies, 声音编码, ACE, SPEAK, MP3000, FSP, FS4, HiRes120]
status: draft
last_updated: "2026-10-04"
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

[言语可懂度](../speech-intelligibility/)和[语音接收阈](../speech-reception-threshold/)评价交流任务；音高排序、普通话声调、旋律和[空间听觉](../spatial-hearing/)需要独立材料。还应考虑延迟、功耗、可靠性及[聆听努力](../listening-effort/)。重复测量中，响度平衡、练习、策略适应、顺序随机化与噪声类型，会影响结果解释。

官方手册最适合证明“这一版本列了什么、怎样设置”；原始临床比较适合证明“特定听者在特定任务发生了什么”；代码适合检验“公开模型到底怎样产生输出”。把这三类证据连接起来，才能评价策略，而不把产品介绍当作跨厂商疗效排名。

## 研究沿革与参见

早期人工耳蜗从语音特征与模拟刺激逐渐发展为多频带包络和脉冲编码。1991 年 CIS 原始研究是重要节点，此后形成谱峰选择、事件触发精细结构、电流导向及个体映射等路线。近年的变化包括双耳共同处理、神经模型与机器学习直接生成刺激表征。它们并非相互替代的单一进步序列：算法目标、硬件约束和评价任务各不相同。[31](#ref-wilson-1991)[1](#ref-zeng-2008)

相关概念：[人工耳蜗](../cochlear-implant/)、[n-of-m 编码](../n-of-m-coding/)、[时域包络](../temporal-envelope/)、[时域精细结构](../temporal-fine-structure/)、[通道相互作用](../channel-interaction/)、[频位映射关系](../tonotopy/)、[动态范围](../dynamic-range/)、[声码器](../vocoder/)、[时域限制编码器](../temporal-limits-encoder/)、[F0inTFS](../f0-in-tfs/)。
