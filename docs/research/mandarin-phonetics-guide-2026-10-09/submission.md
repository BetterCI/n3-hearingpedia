# 普通话辅音语音学基础：五篇联合交稿说明

交稿日期：2026-10-09。稿件为 **Draft，可供专业审阅**，没有完成具名专业审阅。本说明依照 `docs/contributor-kit/submission-template.md` 整理；保留五篇独立概念及其合并结构，不恢复原先十四篇划分，也不修改词条状态。

本次 AI 辅助完成可访问资料阅读、正文组织、教学观察设计、引用核对、原创绘图代码和交稿材料整理。正文实际署名为“AI 辅助编写”。没有把 AI 核对者写成人类作者或专业审阅者，AI 核对、工程验证与专业审阅分别记录。

## 词条信息

五篇均属基础词条（`depth: standard`）、`kind: linguistic`、知识类目 `mandarin-consonants`。正文修改日期及文献检查日期均为 2026-10-09；这些日期不是专业审阅日期。

| 中文名与英文名 | 类型与状态 | 正文文件 | 内容范围与其他篇的区别 | 实际作者署名 | 日期 |
| --- | --- | --- | --- | --- | --- |
| 普通话辅音；Mandarin consonants | 基础 / standard；Draft | [mandarin-consonants.md](../../../src/content/concepts/mandarin-consonants.md) | 系统总论，集中介绍声母、鼻音韵尾、零声母、拼音与 IPA 综合表及 y/w/ü/i 拼写。动作细节由部位、方式两篇展开。 | AI 辅助编写 | 2026-10-09 |
| 辅音的发音部位；Place of articulation | 基础 / standard；Draft | [consonant-place-of-articulation.md](../../../src/content/concepts/consonant-place-of-articulation.md) | 活动器官与被动目标、七类传统部位、平翘舌与龈腭音；包含材料选择及接触资料观察，不重复总论综合表。 | AI 辅助编写 | 2026-10-09 |
| 辅音的发音方式；Manner of consonant articulation | 基础 / standard；Draft | [consonant-manner-of-articulation.md](../../../src/content/concepts/consonant-manner-of-articulation.md) | 闭塞、释放、摩擦、鼻腔与舌侧通路；塞音、塞擦音、擦音、鼻音、边音保留五个独立小节。 | AI 辅助编写 | 2026-10-09 |
| 送气与不送气；Aspiration and unaspiration | 基础 / standard；Draft | [aspiration.md](../../../src/content/concepts/aspiration.md) | 释放与发声的相对时序、普通话配对、VOT 定义与录音观察；区分塞擦摩擦和送气，不把时长当作行为阈值。 | AI 辅助编写 | 2026-10-09 |
| 清音与浊音；Voiceless and voiced consonants | 基础 / standard；Draft | [voicing.md](../../../src/content/concepts/voicing.md) | 声带振动、周期与摩擦并存、音段区间标注和轻声浊化；不将不送气等同浊音或将周期比例当作识别成绩。 | AI 辅助编写 | 2026-10-09 |

五篇均有中文术语与英文名称起笔的自足导言、核心机制、代表性观察、例子、用途及解释边界。观察流程属于本次据概念拟订的教学或研究设计示例，没有采集新录音、接触资料或听者数据，不是论文实验步骤的完整复现。

## 来源与论断对应

下表用来源 ID 跨篇定位，**不是重新编排各正文引用编号**。参考注册表为 `src/data/mandarin-phonetics-references.ts`，各篇编号以各自 frontmatter 的 references 顺序为准。共同作者 Anderson, C.; Bjorkman, B.; Denis, D.; Doner, J.; Grant, M.; Sanders, N.; Taniguchi, A. 对应以下三个开放教材章节。

| 来源 ID；题名、作者、年份及出版信息 | DOI 或稳定链接 | 实际访问范围 | 具体证据位置 | 支持论断及限制 |
| --- | --- | --- | --- | --- |
| `lee-zee-standard-chinese-2003`；Lee, W.-S. & Zee, E. (2003), *Standard Chinese (Beijing)*, Journal of the International Phonetic Association 33(1), 109–112 | [10.1017/S0025100303001208](https://doi.org/10.1017/S0025100303001208) | 已核读出版方全文；保存文本及第 109、112 页图可追溯。 | p.109 导言和 Consonants；pp.110–111 Conventions；p.111 儿化规则；p.112 Notes 1–6。 | 普通话辅音类别、送气配对、m/n/ng 分布、j/q/x 后续音分布、轻声起首阻碍音浊化、r 后齿龈近音及 ng 尾儿化后的鼻化。示例录音为一位 25 岁北京女性；注 1 另述二十岁出头男女北京说话人的腭位和舌面印迹资料，不自行推定样本数，不把该范围推广为所有普通话人的唯一实现。 |
| `ipa-chart-official`；International Phonetic Association，*The International Phonetic Alphabet and the IPA Chart*，2026 重发版；表底注明修订至 2015/2005 | [官方图表入口](https://www.internationalphoneticassociation.org/content/ipa-chart) | 已核读官方说明并查看保存的官方表图。 | Consonants (Pulmonic) 方式和部位行列；Other Symbols 的连接线；Diacritics 的 Aspirated、Syllabic、Nasalized、No audible release。 | 定义符号类别、清浊左右排列、送气上标、塞擦连接线及鼻化等附加符号。不是普通话唯一音位清单，也不提供普通话发音时长、行为阈值或精确舌形常模。 |
| `hanyu-pinyin-scheme`；中国文字改革委员会，《汉语拼音方案》，1958 年全国人大通过；现用公开原文转录 | [固定转录版本](https://zh.wikisource.org/w/index.php?title=%E6%B1%89%E8%AF%AD%E6%8B%BC%E9%9F%B3%E6%96%B9%E6%A1%88&oldid=1958216) | 已在线核读正文及有关表注。 | “二 声母表”；“三 韵母表”附注 1、4、5、6；声调符号。 | 支持 21 声母、七音节中的 i、零声母 y/w、ü 省点及 n/l 后保留区别等拼写。入口是维基文库转录，不宣称教育部托管；拼写不自动决定音位分析或每次实际音值。 |
| `essentials-consonant-place-phonation`；Anderson 等 (2022), *Essentials of Linguistics*, 2nd edition，eCampusOntario，3.3 *Describing consonants: Place and phonation* | [3.3 全文](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-3-describing-consonants-place-and-phonation/) | 实际在线读取章节正文。 | Consonants as constrictions、Active articulators、Passive articulators、Place of articulation、Glottal articulation，以及表 3.1 前后和 buzz/bus 示范。 | 通用部位、主动/被动器官、舌尖/舌叶/舌背及声带活动。英语例词只作机制示范，不替代普通话音类或听者表现。网页版无固定页码。 |
| `essentials-consonant-manner`；Anderson 等 (2022)，同上教材，3.4 *Describing consonants: Manner* | [3.4 全文](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-4-describing-consonants-manner/) | 实际在线读取章节全文相关机制和例子。 | Stops 与 Figure 3.9；Fricatives；Approximants 与 Figure 3.10；Affricates；Other classes of consonants；Putting it all together!。 | 闭塞、摩擦释放、软腭升降、鼻腔与舌侧通路、近音和擦音、塞擦音与辅音序列。通用机制不是完整的普通话采集协议，也不单独提供送气时长实验参数。 |
| `essentials-vot-phonemes`；Anderson 等 (2022)，同上教材，13.2 *Evidence for phonemes as mental categories* | [13.2 全文](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/evidence-for-phonemes-as-mental-categories/) | 已实际读取英语送气与 VOT 教学段、类别任务说明。 | “The specific contrast they examined…” 后的 /dæ/、/tæ/、Voice Onset Time 定义及相应任务。 | 支持塞音释放至后续元音发声起始的 VOT 一般定义，以及声学量、类别反应与脑反应应分开。英语类别边界和 MEG 结果没有移写为普通话结果；图中 12/60 ms 等不来自其测量。 |
| `lisker-abramson-vot-1964`；Lisker, L. & Abramson, A. S. (1964), *A Cross-Language Study of Voicing in Initial Stops: Acoustical Measurements*, WORD 20(3), 384–422 | [10.1080/00437956.1964.11659830](https://doi.org/10.1080/00437956.1964.11659830) | **仅 metadata**：Crossref 核实书目；本轮读取已保存注册和证据记录，尚未获得全文。 | 书目题名、作者、年份、卷期、页码及 DOI；没有科学结果页段可登记。 | 仅作为进一步阅读入口，不支持正文的原始实验结果、专门分段参数或跨语言阈值。VOT 一般定义由已读教材 13.2 支持，未取该文全文不影响当前一般定义。 |

逐项修订和访问记录见 [foundations-evidence.md](foundations-evidence.md)、[manner-evidence.md](manner-evidence.md)、[contrasts-evidence.md](contrasts-evidence.md)。这些分篇记录保留各编辑阶段的实际工作范围；以下交付图表以当前 `figure-sources.json` 及实际文件为准。

## 图片与复现材料

五张图均已生成可编辑 SVG 和 PNG 展示副本，文件及统一脚本已检查存在。创作者登记为 **n³ Hearingpedia, AI-assisted code and editorial verification**。均为原创教学示意或合成信号，**非实测数据，没有复制或描摹第三方图，原始第三方图号为 null**。

根据 manifest，使用范围为：“Created for display, editing and publication in this repository; no separate external reuse license assigned”，即为本仓库展示、编辑和发布而创建，尚未单独赋予外部复用许可。本说明不宣称这些原创图已采用 CC 或其他公开再利用许可；原理来源的公开访问或教材许可也不自动转移为本图许可。

统一生成脚本：[generate-mandarin-phonetics-figures.py](../../../scripts/generate-mandarin-phonetics-figures.py)。图源、完整参数和使用范围登记：[figure-sources.json](figure-sources.json)。脚本无 CLI 参数；依赖 NumPy、Matplotlib 与 Windows Microsoft YaHei 字体，固定常量决定可复现教学输出。

| 所属词条；该篇图 1 | 实际 SVG 与 PNG 文件 | 图的性质与原理来源 | 生成函数、参数与简化边界 |
| --- | --- | --- | --- |
| 普通话辅音；音节位置与拼音记写 | [SVG](../../../public/figures/mandarin-consonants/consonant-system.svg)；[PNG](../../../public/figures/mandarin-consonants/consonant-system.png) | 原创分类与位置图；来源 `hanyu-pinyin-scheme`、`lee-zee-standard-chinese-2003`，不转载原文音表图。 | `makeSyllableFigure()`：妈 mā、衣 yī、昂 áng；展示声母/零声母/韵尾与拼写，框宽不是时长，声调附着音节。 |
| 辅音的发音部位；主动器官与被动目标 | [SVG](../../../public/figures/consonant-place-of-articulation/articulator-pairs.svg)；[PNG](../../../public/figures/consonant-place-of-articulation/articulator-pairs.png) | 原创器官配对图；来源 `essentials-consonant-place-phonation`、`lee-zee-standard-chinese-2003`。 | `makePlaceFigure()`：七类传统部位；不是口腔比例剖面，箭头不表示实测距离或运动幅度。 |
| 辅音的发音方式；阻塞、释放与气流通路 | [SVG](../../../public/figures/consonant-manner-of-articulation/airflow-manners.svg)；[PNG](../../../public/figures/consonant-manner-of-articulation/airflow-manners.png) | 原创五类过程与条件图；来源 `essentials-consonant-manner`、`lee-zee-standard-chinese-2003`。 | `makeMannerFigure()`：闭塞释放、摩擦、鼻腔与舌侧通气；箭头表示关系，不表示流速、位置或持续时间，省略个体解剖及协同发音。 |
| 送气与不送气；释放到周期起始的时序 | [SVG](../../../public/figures/aspiration/aspiration-timing.svg)；[PNG](../../../public/figures/aspiration/aspiration-timing.png) | 原创合成波形；原理来源 `essentials-vot-phonemes`、`lee-zee-standard-chinese-2003`，不是任何文献或说话人的录音。 | `makeAspirationFigure()`：8 kHz 采样、150 Hz 周期，释放 0 ms，周期起始 12/60 ms，seed 20261009；完整参数见下表。不能形成普通话常模或感知界值。 |
| 清音与浊音；周期、噪声和混合 | [SVG](../../../public/figures/voicing/voicing-patterns.svg)；[PNG](../../../public/figures/voicing/voicing-patterns.png) | 原创合成声源分量图；来源 `essentials-consonant-place-phonation`、`essentials-consonant-manner`。 | `makeVoicingFigure()`：8 kHz 采样、150 Hz 周期，seed 20261010；三种分量不是某个自然辅音的完整声学仿真，周期存在不自动决定感知类别。 |

图中数字均为**教学选参**，不是论文实测、设备推荐设置或普通话类别阈值。

| 合成图 | 实际参数记录 |
| --- | --- |
| 送气时序 | 采样率 8000 Hz；周期频率 150 Hz；seed 20261009；时间窗 −20 至 100 ms；释放点 0 ms；周期起始点 12/60 ms；噪声标准差 0.16；归一化前周期幅度 0.68；释放脉冲幅度 0.9、宽度参数 0.35 ms；两条信号使用共同峰值尺度归一化。 |
| 清浊分量 | 采样率 8000 Hz；周期频率 150 Hz；seed 20261010；时间窗 0 至 40 ms；噪声标准差 0.25；归一化前周期幅度 0.65；混合噪声权重 0.55；三条信号使用共同峰值尺度归一化。 |

无量纲的幅度及噪声参数只是脚本内部生成值，不代表声压级。原始数据文件不适用；输出由脚本固定参数生成。配套完整图注、替代文本、原图查看与手机/桌面展示检查由主任务接入后统一更新；此处不把尚未执行的页面检查记作通过。

## 相关概念与知识关系

五个存续节点为 `mandarin-consonants`、`consonant-place-of-articulation`、`consonant-manner-of-articulation`、`aspiration`、`voicing`。关系注册保持 `src/data/relations.ts` 中这批的 **12 条**，另连既有声调、共振峰、基频和混淆矩阵；不将合并前的音类继续保留为独立节点。

| source → target | type | 与正文的关系 |
| --- | --- | --- |
| 发音部位 → 普通话辅音 | describes | 用器官和目标描述辅音。 |
| 发音方式 → 普通话辅音 | describes | 用阻塞、摩擦和气流路线描述辅音。 |
| 送气与不送气 → 普通话辅音 | describes | 用释放与发声时序描述常见配对。 |
| 清音与浊音 → 普通话辅音 | describes | 用声带振动描述辅音，与送气分开。 |
| 发音部位 → 发音方式 | related | 同部位可有不同方式，同方式可分布于不同部位。 |
| 送气与不送气 → 发音方式 | related | 塞音和塞擦音的释放组织影响分段。 |
| 清音与浊音 → 发音方式 | related | 声带状态与口腔、鼻腔和侧向通气分别记录。 |
| 送气与不送气 → 清音与浊音 | related | 不送气不等于浊音。 |
| 普通话辅音 → 普通话汉语声调 | related | 描述音节的不同层面。 |
| 发音部位 → 共振峰 | related | 后续元音过渡可供观察，不能当作固定部位标签。 |
| 清音与浊音 → 基频 | related | 周期可形成基频，清浊不等同声调或音高。 |
| 普通话辅音 → 混淆矩阵 | analyzed-by | 刺激—反应记录用于整理后续识别错误。 |

`related` 是对称知识联系，箭头沿用注册顺序，不声明因果方向。术语 aliases 保留旧中文/英文标题作为检索入口；声母和 IPA 内容集中在总论，舌尖前后与龈腭内容集中在部位篇，五类方式集中在方式篇。

## 历史网址兼容

现有 `src/data/merged-concepts.ts` 保持九个旧网址映射到对应存续小节。下表省略共同站点前缀 `/n3-hearingpedia/concepts/`；这些历史入口不是新增独立词条。

| 旧 slug | 目标存续 slug 与稳定锚点 |
| --- | --- |
| mandarin-initials | mandarin-consonants/#initials |
| mandarin-consonant-ipa | mandarin-consonants/#ipa |
| mandarin-alveolar-retroflex | consonant-place-of-articulation/#alveolar-retroflex |
| mandarin-alveolo-palatal | consonant-place-of-articulation/#alveolo-palatal |
| plosive | consonant-manner-of-articulation/#plosive |
| affricate | consonant-manner-of-articulation/#affricate |
| fricative | consonant-manner-of-articulation/#fricative |
| nasal-consonant | consonant-manner-of-articulation/#nasal |
| lateral-consonant | consonant-manner-of-articulation/#lateral |

## 待核实或未完成事项

1. **缺少具名专业审阅。** 五篇仍需语音学专业人员审阅术语、教学宽式选符、音系分析范围与观察设计；没有 reviewer 或 reviewed_at，不由 AI 核对自动升级为 Reviewed/Stable。
2. **样本外推广与记音差异。** Lee 与 Zee 的青年北京样本不能代表所有普通话人的唯一舌形；[ʈʂ]/[tʂ] 和 [ɻ]/[ʐ] 等教学宽式与原文后齿龈细转写需保留层次。历史 Karlgren/Chao 说明来自论文注释，本轮未直接核读原著，不登记为已阅读全文。
3. **采集细参数与方法执行。** 腭位、舌面印迹及本文拟订录音观察尚缺适用于复现的实际设备、详细采集参数、样本和标注一致性资料。正文只说明观察对象和设计边界，没有填造接触面积、坐标、时长常模、识别成绩或诊断界值。
4. **Lisker 与 Abramson 全文。** 尚未取得 1964 年论文全文；当前仅作经典阅读入口，不支持其具体结果。VOT 一般定义已有已读教材来源，因此这个缺口不影响当前一般定义；若以后增加其参数或跨语言结果，应先取全文核对。
5. **图的接入与交叉核对。** 当前五对 SVG/PNG 和脚本已存在，原理、参数及仓库使用范围已记录；完整图注、替代文本、公式、图文一致性及桌面/390 px 手机阅读效果已由主任务核对，点击原图检查通过。
6. **工程与浏览器新检查。** 本轮 check、build、verify 与源码检查通过：149页、58个搜索词条、10,281个内部链接、119处公式、0断链。五张图加载与打开原SVG、桌面/390 px手机布局、9个旧网址跳转和地图均通过；见 [validation.json](validation.json)。

## 作者与 AI 检查记录

以下勾选表示 AI 辅助编辑已经核对的交稿材料，不表示具名人类作者或专业审阅者签署。

- [x] 五篇导言、定义、机制、代表性方法、具体例子、应用与解释边界有实质内容。
- [x] 各来源的实际访问范围、页段与适用限制已单列；Lisker metadata 未被当作科学结果。
- [x] 五篇署名、日期、Draft 与 standard 状态如实记录；没有修改状态。
- [x] 五个存续节点、12 条关系、九个历史入口及检索 aliases 已据当前登记核对。
- [x] 五对实际 SVG/PNG、脚本、教学参数与原创使用范围已据 manifest 记录。
- [x] 未完成的采集、专业审阅及工程/浏览器检查已单列。
- [x] 公式、单位、教学选参、图文及桌面/手机页面效果已完成统一核对。
- [x] 新的 check、build、verify、源码检查及浏览器检查通过。
- [ ] 具名专业审阅完成。

## 维护与专业审阅记录

- 接入维护者与日期：Codex 自动接入，2026-10-09；仓库提交账号 tuobamao。此记录不代表人类科学审阅。
- 工程检查与页面预览：已执行并通过，具体数据见 validation.json。
- 专业审阅者：
- 专业审阅日期：
- 专业审阅覆盖范围与遗留问题：尚未执行；待具名专业审阅后填写。
- 词条状态：五篇均为 Draft，可供专业审阅。
图文科学核对补充：部位图例项是拼音；鼻音/边音条件箭头不代表先后动作；12/60 ms及150 Hz不是分类阈值，合成信号不替代真实声带活动或患者资料。VOT引用的教材第13章网页标注为更新中，本次仅使用其通用定义，不采用其英语阈值或神经结果。

合入主分支3827812后重新通过源码、类型、构建及链接检查，保留新增两篇深度词条、分享和统计功能。五篇配图在桌面/手机正常；分享弹窗的图片生成、保存入口、复制按钮启用及关闭恢复滚动均已检查，未发送外部消息或改写用户剪贴板。

最终同步到主分支435cfb6（PR #11已合并，保留新音色词条），重新通过源码、类型、构建与页面验收；IPA首次出现的中文释义已补齐。专业审阅记录仍为空，五篇保持Draft。
