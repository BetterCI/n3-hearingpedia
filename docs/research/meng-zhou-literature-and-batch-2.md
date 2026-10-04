# Qinglin Meng 和 Huali Zhou 共同论文与第二批词条

调研日期：2026 年 10 月 4 日。面向 n³ Hearingpedia 的课题组成员，建议在现有 8 个词条之后新增 20 个词条，总量达到 28 个。本文件记录有文献依据的编写目录；目录选择属于编辑判断。2026-10-04 已完成对应 20 个 Draft 词条并纳入 v0.2；正文及其科学内容尚未经过成员审阅。

## 调研范围和方法

以两位作者共同署名的听觉科学研究为主线，不限定发表起始年份，截止 2026 年 10 月 4 日。通过姓名检索寻找种子论文，再以 ORCID、机构和合作作者核实身份：Qinglin Meng 为 0000-0003-0544-1967，Huali Zhou 为 0000-0002-5710-5271。排除同名作者的电力、建筑、计算机理论等无关记录。

OpenAlex 双作者交集检索获得 25 条记录；Crossref 的两次作者检索补入遗漏项，合并后逐个 DOI 核对题名和作者，共获得 29 条已核实共同署名记录。其中 23 条为正式发表记录：14 篇期刊文章、8 篇会议全文、1 篇书章；另有 3 条会议摘要和 3 条预印本。这里计数的是出版记录，不等于独立实验或独立研究数量。

核心条目的选词进一步依据出版方、PubMed 或作者公开正式稿的摘要及指定章节。只读到元数据的论文仅作为书目线索，不依据题名写入结果。OpenAlex 可能漏收作者关联，Crossref 也可能把会议摘要标为期刊文章，故不能用数据库类型或作者 ID 自动替代核查。

对 TLE 音高论文做一层后向检索，筛查 30 条参考文献；对 GET 正式论文做一层前向检索，获得 6 条引文记录。前向引文主要回到已识别的声码器、原子语音及谐波性主题，因此停止向下一层扩展。相关但未同时署名的论文单独标记，不并入共同发表记录。

此结果是快速证据地图，不是穷尽书目。中文期刊、未索引会议和作者分裂记录仍可能遗漏。作者主页列出的中文综述《人工耳蜗的音高感知编码机制和限制》在本轮未取得出版方记录，暂列待核实，不计入上述 29 条。

## 研究主线及其选词意义

时间信息与音高编码是首条主线。2022 年 TLE 论文比较真实 CI 听者的音高辨别和排序；2023 年 F0inTFS 则在模拟 CI 条件下检验轻量周期性增强。两种证据的听者和任务不同，因此基础条目应先解释 TFS、基频、振幅调制和音高，再介绍具体算法。[TLE](https://pubmed.ncbi.nlm.nih.gov/36044501/)，[F0inTFS](https://www.isca-archive.org/interspeech_2023/zhou23c_interspeech.html)。

声码器与稀疏语音是第二条主线。GET 正式稿描述高斯刺激的时频权衡和逐脉冲映射；原子语音论文进一步使用 Gabor 原子考察原子率、谱峰选择、两耳分配和回声条件。它们支持建立 GET 声码器和原子语音模型两个专题，分别解释模拟器和感知研究工具的用途。[GET 正式稿](https://doi.org/10.1016/j.apacoust.2023.109386)，[原子语音](https://pubmed.ncbi.nlm.nih.gov/40106275/)。

普通话语音感知是第三条主线。DiTone 研究通过独立操控音高与幅度线索考察声调识别；谐波性研究区分安静与竞争语音条件；2026 年辅音论文用混淆、聚类、多维尺度和信息传递分析补充整体正确率。这些研究支持普通话词汇声调、谐波性和混淆矩阵三个入口，而不宜把所有结果压缩成一个语音识别百分比。[DiTone](https://doi.org/10.3389/fpsyg.2022.1026116)，[谐波性](https://doi.org/10.1016/j.specom.2025.103199)，[辅音感知](https://doi.org/10.1121/10.0044108)。

数字听力测量与筛查是第四条主线。TWS 自动纯音测听系列涉及设备校准和噪声环境，ZIN 系列涉及材料设计、适应性测量与筛查效能。2026 年反相 ZIN 正式论文进一步引出 BILD；旧会议摘要中的数值不能直接作为正式版本的测试参数。[TWS 测听](https://doi.org/10.1177/23312165211057367)，[ANC 测听](https://doi.org/10.1080/14992027.2024.2428854)，[ZIN](https://pubmed.ncbi.nlm.nih.gov/38062570/)，[反相 ZIN](https://pubmed.ncbi.nlm.nih.gov/41680979/)。

双耳研究贯穿以上主线。ITD、两耳互补信息整合和反相去掩蔽应分别解释；DBD-CI 的初步模拟研究适合作为双耳整合和通道相互作用的案例，暂不把模拟结果写成真实双侧植入者的确定获益。[ITD 与 TLE](https://www.isca-archive.org/interspeech_2020/wan20b_interspeech.html)，[DBD-CI](https://www.isca-archive.org/interspeech_2024/shi24c_interspeech.html)。

## 第二批二十个词条

表内为建议正式条目名称；TLE 的中文暂用“时间限度编码器”，编写时保留英文全称和缩写。Tonotopy 继续统一为“频位映射关系”。

| 序号 | 中文词条 | 英文与缩写 | 解决的问题 | 主要论文 |
|---|---|---|---|---|
| 1 | 时间精细结构 | Temporal fine structure / TFS | 分清频带信号的精细结构、时间包络与周期性线索。 | [文献](https://doi.org/10.1109/tnsre.2022.3203079)；[文献](https://doi.org/10.21437/interspeech.2023-652) |
| 2 | 音高感知 | Pitch perception | 连接时间音高、位置音高和音高辨别任务。 | [文献](https://doi.org/10.1109/tnsre.2022.3203079)；[文献](https://doi.org/10.3389/fpsyg.2022.1026116) |
| 3 | 基频 | Fundamental frequency / F0 | 解释基频、周期、谐波及在语音中的变化。 | [文献](https://doi.org/10.21437/interspeech.2023-652)；[文献](https://doi.org/10.1016/j.specom.2025.103199) |
| 4 | 谐波性 | Harmonicity | 解释谐波关系及其在安静与竞争语音中的作用。 | [文献](https://doi.org/10.1016/j.specom.2025.103199) |
| 5 | 振幅调制 | Amplitude modulation / AM | 解释调制频率、调制深度以及电刺激包络调制。 | [文献](https://doi.org/10.1109/tnsre.2022.3203079)；[文献](https://doi.org/10.64898/2025.12.03.25341217) |
| 6 | 通道相互作用 | Channel interaction | 说明电流扩散、通道重叠与有效频谱分辨率的关系。 | [文献](https://doi.org/10.1016/j.apacoust.2023.109386)；[文献](https://doi.org/10.21437/interspeech.2024-1505) |
| 7 | 双耳时间差 | Interaural time difference / ITD | 区分波形与包络的双耳时间差，连接空间听觉任务。 | [文献](https://doi.org/10.21437/interspeech.2020-2507)；[文献](https://doi.org/10.1109/icsp58490.2023.10248809) |
| 8 | 语音接收阈 | Speech reception threshold / SRT | 介绍达到规定识别正确率时所需的测量条件、阈值和适应程序。 | [文献](https://doi.org/10.1097/aud.0000000000001441)；[文献](https://doi.org/10.1121/10.0036144) |
| 9 | 纯音测听 | Pure-tone audiometry / PTA | 介绍听阈、频率、气导测听与自动测听流程。 | [文献](https://doi.org/10.1177/23312165211057367)；[文献](https://doi.org/10.1080/14992027.2024.2428854) |
| 10 | 听力测量校准 | Audiometric calibration | 解释数字输出、声压级、听力级和参考等效阈声压级的转换。 | [文献](https://doi.org/10.1177/23312165211057367)；[文献](https://doi.org/10.1080/14992027.2024.2428854) |
| 11 | 普通话词汇声调 | Mandarin lexical tone | 解释基频轮廓、时长和幅度等声调识别线索。 | [文献](https://doi.org/10.3389/fpsyg.2022.1026116)；[文献](https://doi.org/10.21437/interspeech.2023-652) |
| 12 | 混淆矩阵 | Confusion matrix | 用普通话辅音识别解释刺激和反应之间的系统混淆。 | [文献](https://doi.org/10.1121/10.0044108)；[文献](https://doi.org/10.21437/interspeech.2023-536) |
| 13 | 双耳整合 | Binaural integration | 解释两耳互补的频谱时间信息能否合并支持识别。 | [文献](https://doi.org/10.1121/10.0036144)；[文献](https://doi.org/10.21437/interspeech.2024-1505) |
| 14 | n-of-m 编码策略 | n-of-m coding strategy | 解释分析频带、谱峰选择、刺激通道及 ACE 实现。 | [文献](https://doi.org/10.1016/j.bspc.2022.104169)；[文献](https://doi.org/10.1016/j.apacoust.2023.109386) |
| 15 | 时间限度编码器 | Temporal Limits Encoder / TLE | 解释将频带时间信息转换到电听觉时间音高范围的策略。 | [文献](https://doi.org/10.1109/tnsre.2022.3203079)；[文献](https://doi.org/10.21437/interspeech.2020-2507) |
| 16 | F0inTFS 周期性增强策略 | F0inTFS | 介绍利用最低频带精细结构向高频带包络引入周期性信息的方法。 | [文献](https://doi.org/10.21437/interspeech.2023-652) |
| 17 | 脉冲式高斯包络音声码器 | Pulsatile Gaussian-enveloped-tone vocoder / GET vocoder | 解释高斯包络音、逐脉冲模拟和时频权衡。 | [文献](https://doi.org/10.1016/j.apacoust.2023.109386)；[文献](https://doi.org/10.1109/tnsre.2023.3274604) |
| 18 | 原子语音模型 | Atomic speech model / ASM | 解释基于 Gabor 原子的稀疏语音表示和原子率。 | [文献](https://doi.org/10.1121/10.0036144) |
| 19 | 生肖噪声测试 | Chinese Zodiac-in-Noise test / ZIN | 解释基于生肖三元组材料的远程噪声下语音筛查。 | [文献](https://doi.org/10.1097/aud.0000000000001441)；[文献](https://doi.org/10.1097/aud.0000000000001791) |
| 20 | 双耳可懂度级差 | Binaural intelligibility level difference / BILD | 连接双耳同相与反相语音测试及双耳去掩蔽评价。 | [文献](https://doi.org/10.1097/aud.0000000000001791) |

## 条目边界与现有词条衔接

- **时间精细结构**：改变信号表示不等于已经恢复神经系统中的全部精细结构。
- **音高感知**：主观音高、物理基频和声调识别成绩分别定义。
- **基频**：基频与感知音高相关，但不是可互换的量。
- **谐波性**：不能把正常听力、声码器模拟和真实人工耳蜗的结果混写。
- **振幅调制**：调制频率与脉冲率分别记录；协变刺激的新证据单列为预印本。
- **通道相互作用**：电极数量与可独立利用的通道数量不能直接画等号。
- **双耳时间差**：定位、侧化和时间差辨别是不同实验任务。
- **语音接收阈**：在噪声中通常报告阈值信噪比；安静条件的呈现级阈值另行说明。
- **纯音测听**：PTA 在部分文献也指 pure-tone average，检索和正文须区分。
- **听力测量校准**：校准依赖设备、佩戴和测量系统；ANC 开启不替代校准。
- **普通话词汇声调**：DiTone 作为语料案例；识别成绩不能单独证明基频线索被正确编码。
- **混淆矩阵**：报告行列方向和归一化方式；MDS、聚类与信息传递作为后续方法入口。
- **双耳整合**：两耳同时呈现不保证整合获益；整合与双耳去掩蔽分别解释。
- **n-of-m 编码策略**：ACE 为具体实现，不作为所有 n-of-m 策略的同义词；电动态范围作为参数小节。
- **时间限度编码器**：中文暂用时间限度编码器，保留英文和缩写；不同版本与任务的证据分别列出。
- **F0inTFS 周期性增强策略**：2023 年该论文的行为验证为声码器模拟实验，不写成真实植入者验证。
- **脉冲式高斯包络音声码器**：GET 是刺激单元，GET vocoder 是模型；声学模拟的限制需要独立小节。
- **原子语音模型**：该文的 SRT 调整变量为原子率，不应套用所有 SRT 都是信噪比的说法。
- **生肖噪声测试**：双耳同相与反相版本分别描述；筛查阈值和目标耳依验证条件限定。
- **双耳可懂度级差**：明确差值方向和刺激配置，不能与纯音的双耳掩蔽级差直接互换。

现有 Speech Intelligibility 条目的检索别名包含 SRT。新增 SRT 条目时应移出该别名并改为相关链接：可懂度是感知表现或指标类别，SRT 是在规定任务和正确率下估计的阈值，二者不应作为同义词。原子语音研究的阈值调整变量为原子率，也说明 SRT 并不总以信噪比表示。

n-of-m 条目第一版应包括 ACE 示例、谱峰选择数和电动态范围的小节。基础原理与设备编程建议分开；单项实验中较好的参数设置不能推成对所有植入者的通用配置。

每个新条目均从 Draft 开始。正文要明确证据来自正常听力、声码器模拟、真实 CI 或 HA 听者，并记录语言、材料、噪声和任务；科学审阅后再升级状态。书目信息核实不等于实验结果或条目正文已经审阅。

## 编写顺序

建议先写时间精细结构、基频、音高感知、语音接收阈、通道相互作用和纯音测听，补齐阅读论文所需的基础。随后编写其他基础及测量词条，再写 GET、TLE、F0inTFS、原子语音、ZIN 和 BILD 等专题。机器可读目录中的 prerequisites 已包含现有与新条目的依赖关系。

对课题组的后续问题包括：哪些声码器参数同时匹配多个感知任务；音高增强在真实 CI 上能否转移到普通话或竞争语音任务；两耳信息整合失败来自刺激表示还是听者差异；反相筛查对目标耳、听力损失类型和设备条件的依赖有多大。这些是本调研提出的问题，不是现有论文已确证的结论。

## 后续储备及近期文献

下一批可储备电动态范围、刺激脉冲率、适应性心理物理法、语音增强、主动降噪、频谱时间调制纹波、多维尺度分析和 DBD-CI。此次先把电动态范围及脉冲率放入相关条目的参数小节，避免起步阶段出现过多依赖基础解释的小专题。

本轮近期窗口定义为 2025 年 1 月 1 日至 2026 年 10 月 4 日。已核实的共同正式论文新增原子语音、谐波性、反相 ZIN 和辅音感知组织等主题。AM 与脉冲率协变刺激的 2025 medRxiv 和 2026 SSRN 稿件作者及实验规模高度重合，暂按同一研究线索处理，保留两个出版记录，未作为两项独立已审稿证据。预印本可进入“新进展”小节，必须注明状态。

前向引文中的 [2026 年双耳老化研究](https://doi.org/10.1097/AUD.0000000000001863) 和 [2024 年 ASR 评价论文](https://doi.org/10.1109/ISCSLP63861.2024.10800026) 未同时署名两位作者，故只作为相关研究，不计入共同论文数量。第二批没有为了补齐 AI 领域而强行纳入 ASR。

## 核心论文阅读记录

| 论文 DOI | 证据范围 | 为什么保留 |
|---|---|---|
| [10.3389/fnins.2020.00301](https://doi.org/10.3389/fnins.2020.00301) | Frontiers 原文 Abstract、eVoice of Nurotron、Experiment 2。 | 在真实 CI 听者中评价单通道噪声抑制 eVoice；支持语音增强和 SRT 的方法背景。 |
| [10.21437/interspeech.2020-2507](https://doi.org/10.21437/interspeech.2020-2507) | ISCA Archive 摘要；其验证材料为 vocoded speech。 | 使用声码器语音比较双耳 TLE 与 CIS 的 ITD 识别，构成 ITD 和编码策略的入口。 |
| [10.1177/23312165211057367](https://doi.org/10.1177/23312165211057367) | SAGE 作者名单和摘要。 | 报告 TWS 自动纯音测听的校准和临床对照流程，支撑 PTA 与听力测量校准。 |
| [10.1109/tnsre.2022.3203079](https://doi.org/10.1109/tnsre.2022.3203079) | PubMed 36044501 摘要。 | 在 CI 听者中比较 TLE 与 ACE 的音高辨别和音高排序，连接 TFS、AM、F0 与音高任务。 |
| [10.3389/fpsyg.2022.1026116](https://doi.org/10.3389/fpsyg.2022.1026116) | Frontiers 原文 Abstract、2.2 Stimuli、5 Conclusion。 | 用双音节语料独立操控音高与幅度线索，说明声调识别任务需要分辨所用线索。 |
| [10.1016/j.bspc.2022.104169](https://doi.org/10.1016/j.bspc.2022.104169) | ScienceDirect 摘要，卷期为 2023 年，DOI 含 2022。 | 在 CI 及声码器条件下考察谱峰选择数和电动态范围与噪声下语音接收阈的关系。 |
| [10.1016/j.apacoust.2023.109386](https://doi.org/10.1016/j.apacoust.2023.109386) | UCI 作者公开正式稿第 1 节和第 2 节 GET Theory。 | 提出逐脉冲 GET 声码器并讨论高斯刺激的时频约束，用于连接模型和电听觉参数。 |
| [10.1109/tnsre.2023.3274604](https://doi.org/10.1109/tnsre.2023.3274604) | PubMed 37159306 摘要。 | 比较声学模拟与真实电听觉中的感知模式，支撑模型评价需要多个感知任务。 |
| [10.21437/interspeech.2023-652](https://doi.org/10.21437/interspeech.2023-652) | ISCA Archive 摘要和论文第 1 页；未据此声称真实 CI 已验证。 | 提出无需显式基频检测的 F0inTFS 算法，并用模拟 CI 的词汇声调实验评价。 |
| [10.21437/interspeech.2023-536](https://doi.org/10.21437/interspeech.2023-536) | ISCA Archive 摘要。 | 考察听力损失和助听器放大下的普通话辅音识别及混淆模式。 |
| [10.1097/aud.0000000000001441](https://doi.org/10.1097/aud.0000000000001441) | PubMed 和出版元数据摘要；2023 在线发表，2024 卷期。 | 开发 ZIN 并将其与纯音测听比较，构成 SRT、筛查评价及组内测试专题的入口。 |
| [10.21437/interspeech.2024-1505](https://doi.org/10.21437/interspeech.2024-1505) | ISCA Archive 摘要；暂不据此声称真实 BiCI 获益。 | 提出跨两耳分配频带的 DBD-CI，并报告初步声码器实验；用于连接通道相互作用和双耳整合。 |
| [10.1080/14992027.2024.2428854](https://doi.org/10.1080/14992027.2024.2428854) | 作者公开稿第 2 页 Objective measurement、Method；2024 在线发表。 | 在 TWS 自动测听中加入 ANC，评价声学性能并进行校准和行为对照。 |
| [10.1016/j.specom.2025.103199](https://doi.org/10.1016/j.specom.2025.103199) | ScienceDirect 摘要和 Introduction；其结果不直接确证 CI 的谐波性去掩蔽机制。 | 比较谐波与非谐波普通话在安静和竞争语音条件下的感知，区分真实 CI 与模拟条件。 |
| [10.1121/10.0036144](https://doi.org/10.1121/10.0036144) | PubMed 40106275 摘要；这里的适应性阈值调整变量为原子率。 | 用稀疏 Gabor 原子语音操控原子率，考察谱峰选择、跨耳整合和单次回声条件。 |
| [10.1097/aud.0000000000001791](https://doi.org/10.1097/aud.0000000000001791) | PubMed 41680979 正式论文摘要；采用正式稿而非 2024 会议摘要数值。 | 评价反相 ZIN 的听力筛查和 BILD 与听阈的关系，支撑双耳去掩蔽指标专题。 |
| [10.1121/10.0044108](https://doi.org/10.1121/10.0044108) | AIP、PubMed 42307486 与 Crossref 的摘要；未完成全文审阅。 | 用辅音识别、聚类、多维尺度分析及信息传递描述 CI 的普通话辅音感知组织。 |

## 完整核实书目

以下保留每个 DOI 的出版记录。年份来自出版方提交的 Crossref 字段；在线发表和卷期年份可能不同。会议摘要单独分类，不能因 Crossref 将其标成 journal-article 就视作期刊全文。没有写阅读笔记的记录，只完成署名与题名核查。

| 类型 | 出版年 | 题名 | DOI |
|---|---|---|---|
| 会议摘要 | 2020 | Enhancing the temporal fine structure with the temporal limits encoder for cochlear implants: Effects on pitch discrimination | [10.1121/1.5147512](https://doi.org/10.1121/1.5147512) |
| 会议摘要 | 2020 | Automated pure tone audiometry with true wireless stereos earbuds | [10.1121/1.5147525](https://doi.org/10.1121/1.5147525) |
| 会议全文 | 2020 | Enhancing the Interaural Time Difference of Bilateral Cochlear Implants with the Temporal Limits Encoder | [10.21437/interspeech.2020-2507](https://doi.org/10.21437/interspeech.2020-2507) |
| 期刊全文 | 2020 | A New Approach for Noise Suppression in Cochlear Implants: A Single-Channel Noise Reduction Algorithm | [10.3389/fnins.2020.00301](https://doi.org/10.3389/fnins.2020.00301) |
| 会议摘要 | 2021 | Enhancing the temporal fine structure with the temporal limits encoder for cochlear implants: Effects on pitch ranking | [10.1121/10.0004661](https://doi.org/10.1121/10.0004661) |
| 期刊全文 | 2021 | Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry | [10.1177/23312165211057367](https://doi.org/10.1177/23312165211057367) |
| 书章 | 2022 | Channel-Vocoder-Centric Modelling of Cochlear Implants: Strengths and Limitations | [10.1007/978-981-19-4703-2_11](https://doi.org/10.1007/978-981-19-4703-2_11) |
| 期刊全文 | 2022 | Effect of listener head orientation on speech reception threshold in an automotive environment | [10.1016/j.apacoust.2022.108782](https://doi.org/10.1016/j.apacoust.2022.108782) |
| 预印本 | 2022 | Pulsatile Gaussian-Enveloped Tones (GET) Vocoders for Cochlear-Implant Simulation | [10.1101/2022.02.21.22270929](https://doi.org/10.1101/2022.02.21.22270929) |
| 会议全文 | 2022 | Internet Streaming Audio Based Speech Reception Threshold Measurement in Cochlear Implant Users | [10.1109/icassp43922.2022.9747404](https://doi.org/10.1109/icassp43922.2022.9747404) |
| 会议全文 | 2022 | Interaural time difference based spatial release from masking with asymmetric hearing over a video conference app | [10.1109/icsp54964.2022.9778684](https://doi.org/10.1109/icsp54964.2022.9778684) |
| 期刊全文 | 2022 | Pitch Perception With the Temporal Limits Encoder for Cochlear Implants | [10.1109/tnsre.2022.3203079](https://doi.org/10.1109/tnsre.2022.3203079) |
| 会议全文 | 2022 | The Relationship Between Pulse Rate and Mandarin Tone Recognition: A Preliminary Study with CCi-Mobile Cochlear Implant Research Processor | [10.1145/3543081.3543082](https://doi.org/10.1145/3543081.3543082) |
| 期刊全文 | 2022 | Cochlear-implant Mandarin tone recognition with a disyllabic word corpus | [10.3389/fpsyg.2022.1026116](https://doi.org/10.3389/fpsyg.2022.1026116) |
| 期刊全文 | 2023 | Pulsatile Gaussian-Enveloped Tones (GET) for cochlear-implant simulation | [10.1016/j.apacoust.2023.109386](https://doi.org/10.1016/j.apacoust.2023.109386) |
| 期刊全文 | 2023 | Effects of number of maxima and electrical dynamic range on speech-in-noise perception with an “n-of-m” cochlear-implant strategy | [10.1016/j.bspc.2022.104169](https://doi.org/10.1016/j.bspc.2022.104169) |
| 期刊全文 | 2023 | The Chinese Zodiac-in-Noise Test: An Internet-Based Speech-in-Noise Test for Large-Scale Hearing Screening | [10.1097/aud.0000000000001441](https://doi.org/10.1097/aud.0000000000001441) |
| 会议全文 | 2023 | Effects of Hearing Loss on Interaural Time Difference Discrimination in an Oddball Paradigm | [10.1109/icsp58490.2023.10248809](https://doi.org/10.1109/icsp58490.2023.10248809) |
| 期刊全文 | 2023 | Comparable Encoding, Comparable Perceptual Pattern: Acoustic and Electric Hearing | [10.1109/tnsre.2023.3274604](https://doi.org/10.1109/tnsre.2023.3274604) |
| 会议全文 | 2023 | Effects of hearing loss and amplification on Mandarin consonant perception | [10.21437/interspeech.2023-536](https://doi.org/10.21437/interspeech.2023-536) |
| 会议全文 | 2023 | F0inTFS: A lightweight periodicity enhancement strategy for cochlear implants | [10.21437/interspeech.2023-652](https://doi.org/10.21437/interspeech.2023-652) |
| 期刊全文 | 2024 | Automated pure-tone audiometry using true wireless stereo earbuds with active noise control | [10.1080/14992027.2024.2428854](https://doi.org/10.1080/14992027.2024.2428854) |
| 会议全文 | 2024 | DBD-CI: Doubling the Band Density for Bilateral Cochlear Implants | [10.21437/interspeech.2024-1505](https://doi.org/10.21437/interspeech.2024-1505) |
| 期刊全文 | 2025 | Effects of harmonicity on Mandarin speech perception in cochlear implant users | [10.1016/j.specom.2025.103199](https://doi.org/10.1016/j.specom.2025.103199) |
| 期刊全文 | 2025 | Sparse representation of speech using an atomic speech model | [10.1121/10.0036144](https://doi.org/10.1121/10.0036144) |
| 预印本 | 2025 | Covarying Amplitude Modulation and Pulse Rate Enhances Pitch Discrimination in Cochlear Implant Users | [10.64898/2025.12.03.25341217](https://doi.org/10.64898/2025.12.03.25341217) |
| 期刊全文 | 2026 | Optimizing the Chinese Zodiac-in-Noise Test With Antiphasic Stimuli for Better Hearing Loss Detection | [10.1097/aud.0000000000001791](https://doi.org/10.1097/aud.0000000000001791) |
| 期刊全文 | 2026 | Perceptual organization of Mandarin consonants in cochlear implant users | [10.1121/10.0044108](https://doi.org/10.1121/10.0044108) |
| 预印本 | 2026 | Covarying Amplitude Modulation and Pulse Rate Improves Pitch-Related Discrimination in Cochlear Implant Users | [10.2139/ssrn.6714210](https://doi.org/10.2139/ssrn.6714210) |

本轮数据文件：meng-zhou-papers.json 保存全部署名、日期字段和阅读范围；second-batch-catalog.json 保存 20 个词条的范围、前置知识和 DOI 关联。
