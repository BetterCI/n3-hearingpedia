# 送气与清浊词条：规范修订和证据对应

更新日期：2026-10-09。类型：基础词条；状态：Draft。作者署名沿用“AI 辅助编写”。本轮 AI 协助阅读可访问材料、组织正文和检查引用，未进行具名专业审阅。AI 核对、作者核验和工程检查不等于专业审阅。

## 任务范围与规范

实际完整阅读 docs/contributor-kit/README.md、basic-entry-template.md、submission-template.md 及仓库 README.md 的写作、来源和状态要求。此次仅完善 aspiration.md、voicing.md，并写入本记录；五篇结构中的两个独立概念保持原 slug、标题、order、状态、别名和其他元数据。参考列表追加实际使用来源，原编号保持不变。

两篇均改为两段中文与英文术语导言，补足机制、代表性录音观察、分段与描述指标、展开对照、教学及听觉研究用途和条件。正文不复制普通话 IPA 总表，保留综合表及已存在概念的链接。方法段为解释概念而提出的观察设计，不冒称来源中的标准化普通话程序。

此次未添加图标签、未制作配图、未借图中教学参数声称自然语音常模。主任务负责时序教学图、周期／噪声教学图及相应参数、图源和复现记录；本记录不将这些图提前登记为已完成。

## 实际核读来源

| 来源 ID／编号 | 书目与稳定链接 | 本轮实际访问范围及定位 | 可支持的内容和限制 |
|---|---|---|---|
| lee-zee-standard-chinese-2003；两篇 [1] | Lee, W.-S. & Zee, E. (2003). Standard Chinese (Beijing). Journal of the International Phonetic Association 33(1), 109–112. DOI: https://doi.org/10.1017/S0025100303001208 | 完整阅读本地保存的出版方 PDF 提取文本 artifacts/mandarin-phonetics/lee-zee-2003.txt；第109页 Consonants、第110–111页 Conventions、第112页 Notes | 普通话清塞音及清塞擦音的送气配对，m/n/l等音类；第111页明确轻声韵母前清阻碍音可浊化。文章录音是一名25岁北京女性，舌形注释另述青年北京样本；不推广为所有普通话说话人的唯一实现或常模。 |
| ipa-chart-official；两篇 [2] | International Phonetic Association. The International Phonetic Alphabet and the IPA Chart，2026重发表。https://www.internationalphoneticassociation.org/content/ipa-chart | 查看本地保存的官方音标表渲染图 artifacts/mandarin-phonetics/ipa-chart.png；肺气流辅音表及 Diacritics 区域 | 一格中左右清浊排列、[p b]/[s z] 等符号类别、上标送气 ʰ。官方总表定义符号，不提供普通话行为阈值或音位数量结论。 |
| lisker-abramson-vot-1964；送气 [3] | Lisker, L. & Abramson, A. S. (1964). A Cross-Language Study of Voicing in Initial Stops: Acoustical Measurements. WORD 20(3), 384–422. DOI: https://doi.org/10.1080/00437956.1964.11659830 | 读取仓库参考注册表中的已核验书目及历史核读记录；本轮未取得全文，出版方访问仍受限 | 仅作为进一步阅读的经典书目入口。未用于VOT公式的具体方法、原始数值、跨语言阈值或实验结果。 |
| essentials-consonant-manner；两篇 [4] | Anderson, C. et al. (2022). 3.4 Describing consonants: Manner. Essentials of Linguistics, 2nd edition. https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-4-describing-consonants-manner/ | 实际请求页面并阅读 Stops、Fricatives、Affricates、Other classes of consonants 及 Putting it all together 相关正文 | 完全闭塞、爆破、口腔狭窄摩擦、塞擦音摩擦释放、鼻腔与侧向气流机制。没有VOT或送气实验参数，不能单独支撑普通话送气时长效果。 |
| essentials-consonant-place-phonation；清浊 [3] | Anderson, C. et al. (2022). 3.3 Describing consonants: Place and phonation. Essentials of Linguistics, 2nd edition. https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-3-describing-consonants-place-and-phonation/ | 实际请求页面并阅读 Glottal articulation 后的声门、声带振动、voicing/phonation 段，以及 buzz/bus 触感示范 | 清浊定义、声带与声门、振动触感观察；英语例词只作跨语言机制示范，不是普通话清浊对立的例词或效果证据。 |
| essentials-vot-phonemes；送气 [5] | Anderson, C. et al. (2022). Evidence for phonemes as mental categories. Essentials of Linguistics, 2nd edition. https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/evidence-for-phonemes-as-mental-categories/ | 实际请求页面，阅读英语送气段及 “The specific contrast they examined…” 后的 /dæ/、/tæ/、Voice Onset Time 定义与任务说明 | 支撑释放到元音发声起始的VOT一般定义及声学变化、类别与任务应分开理解。页面中的英语类别边界与 Phillips et al. 的MEG研究没有被改写为普通话结果；未采用其中的数值边界。主任务负责新增source ID的注册。 |

## 新增或展开的论断与证据位置

| 正文位置／改动 | 依据或性质 | 条件和解释范围 |
|---|---|---|
| 送气导言：普通话 b/p 等以送气配对，且清浊是另一维度 | Lee & Zee，第109页辅音表；通用清浊定义另见教材3.3 | 说明常见音类，不要求自然语流每个音段全程保持相同振动状态。 |
| 送气机制：闭塞后释放、后续发声衔接；塞擦音摩擦不等于全部送气 | 教材3.4 Stops/Affricates；VOT定义见 Evidence for phonemes… | 一般机制解释。塞擦音的分段约定必须另外说明，不提供未核实的专门测量协议。 |
| VOT = t_v - t_r，说明同一时间基准和毫秒单位 | 教材 VOT 定义的直接时间间隔表达 | 本节限定释放后开始元音振动的材料，不讨论未核读的跨语言正负分类或固定阈值。 |
| 送气观察：同说话人、同部位韵母声调、重复录音、结合波形和语谱图分段 | 编辑提出的代表性观察设计，使用上述音类及时间量定义 | 不是已验证临床工具；正文不报告样本统计、正常范围或诊断界值。分段不清楚时记录不确定性。 |
| 送气展开例子：bā/pā 的噪声与周期衔接；声学标注不等于识别成绩 | 教学假设与观察问题，不是实测 | 未设定数字。自然材料与受控材料分别有多线索和人工边界问题；操纵流程是研究设计建议，不是文献实验复现。 |
| 两篇新增轻声浊化条件 | Lee & Zee，第111页 Conventions 原句 | 限于该文描述的普通话北京材料；不据此规定所有轻声音节实现。 |
| 清浊机制：声带振动与摩擦噪声可以并存，响度不决定清浊 | 教材3.3清浊；3.4摩擦；IPA [s z]配对 | IPA [z]示范不等于拼音 z，也不为普通话增列浊擦音声母。 |
| 清浊观察：先定辅音区间，再记录周期段起止、持续时间及区间比例 | 编辑提出的描述性标注方式 | 比例仅说明人工所选录音区间，不是统一“清浊分数”或临床指标；软件输出和周期干扰需要回到原始材料检查。 |
| 清浊展开例子：持续[s]+元音与[m]+元音比较，整音节有周期不决定声母有声 | 教学分析，基于Lee的音类和教材声源定义 | [m]/[s]还改变部位和方式，不能作为只操纵清浊的实验。补充[s]/[z]示范须注明跨语言音标背景。 |
| 听觉技术与教学应用：声学保留需与行为验证分开 | 解释范围和实验设计原则，没有提出效果数值 | 不宣称助听器或人工耳蜗收益，不从波形、VOT或周期段比例推算真实患者识别率。 |

## 核对与待完成事项

- 已核对同调例词：八/趴、低/踢、哥/科、租/粗、知/吃、鸡/七均为第一声；不存在以异调词对说明纯送气差别的情况。
- 已保留两段导言、原别名、Draft状态及order 60/61；新增来源排在原参考列表之后，原编号不变。
- 已检查禁止用语、正文未插入不存在的图片链接、未复制完整IPA声母表。
- 待主任务登记 essentials-vot-phonemes，统一完成图源记录、配图插入、公式与链接工程检查及移动端/桌面端预览；本子任务没有将这些检查勾选为已完成。
- Lisker与Abramson1964全文未核读；现有正文只保留书目入口，如需介绍其具体参数或结果，应先补全文证据。
- 尚无具名专业审阅者、reviewed_at或专业审阅记录。两篇继续为Draft，未填写虚构审阅者。
