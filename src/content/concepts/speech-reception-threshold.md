---
title: "言语接收阈"
english: "Speech reception threshold"
slug: "speech-reception-threshold"
summary: "系统介绍言语接收阈的定义、安静与噪声测试、材料与评分、心理测量函数、自适应程序、临床解读与公开计算模型。"
categories: ["audiology","speech","research-methods"]
tags: ["SRT"]
aliases: ["SRT", "言语识别阈", "言语接受阈", "言语接收阈值", "语音接收阈", "speech recognition threshold"]
batch: 2
status: draft
depth: in-depth
last_updated: "2026-10-07"
literature_checked_at: "2026-10-07"
authors: ["AI 辅助编写"]
references: ["speech-reception-threshold-asha", "speech-reception-threshold-iso", "speech-reception-threshold-gb", "speech-reception-threshold-manual", "speech-reception-threshold-adult", "speech-reception-threshold-zhu", "speech-reception-threshold-hint", "speech-reception-threshold-mhint", "speech-reception-threshold-levitt", "speech-reception-threshold-atomic", "speech-reception-threshold-wichmann", "speech-reception-threshold-thornton", "speech-reception-threshold-bilger", "speech-reception-threshold-psignifit", "speech-reception-threshold-nissen", "speech-reception-threshold-chen", "speech-reception-threshold-vermiglio", "speech-reception-threshold-plomp", "speech-reception-threshold-fade-paper", "speech-reception-threshold-bsa", "speech-reception-threshold-fade-code", "speech-reception-threshold-plomp-reliability", "speech-reception-threshold-smits", "speech-reception-threshold-zin", "speech-reception-threshold-aladdin"]
order: 16
knowledge_area: "measurement"
kind: "metric"
key_facts: [{"label":"缩写","value":"SRT"},{"label":"定义","value":"达到规定识别水平所需的条件"},{"label":"单位","value":"按任务采用 dB SNR、声级或原子率"}]
---

**言语接收阈**（speech reception threshold，SRT）是听者在指定言语材料、呈现方式和评分规则下，达到规定识别水平所需的言语声级或信噪比。传统临床定义通常以 **50% 识别正确率**为目标，英文也称 speech recognition threshold，即“言语识别阈”。这里的“接收”包含辨认言语内容的要求，不只是察觉有声音。[1](#ref-speech-reception-threshold-asha)[2](#ref-speech-reception-threshold-iso)

在安静环境中，SRT 回答“言语需要多大声才能被辨认”；在噪声中，它常回答“言语相对于干扰声需要占多大优势才能被辨认”。两者分别描述不同的测量条件。即使都使用分贝，也不能将安静中的 30 dB HL 与噪声中的 −5 dB SNR 放在同一数轴上比较。只有同时知道材料、目标正确率、单位和测试设置，一个 SRT 数值才有明确含义。

SRT 是连接[纯音测听](../pure-tone-audiometry/)与[言语可懂度](../speech-intelligibility/)的重要指标。前者主要描述频率相关的检测敏感度；后者涉及声学线索、语言知识、记忆和注意等过程。言语接收阈提供了一种可重复的行为测量，但不会把这些过程全部压缩为一种不依赖任务的“听力能力”。我国现行 GB/T 16296.3-2017 与 ISO 8253-3:2022 分别提供言语测听的国家标准和国际标准框架。[3](#ref-speech-reception-threshold-gb)[2](#ref-speech-reception-threshold-iso)

## 定义、名称与相关指标

### 接收阈、识别阈与检测阈

“言语接收阈”和“言语识别阈”在传统 SRT 语境中指向同一个识别任务。ASHA 优先使用后一个英文名称，以突出听者需要指出刺激内容。中文“言语接受阈”也出现在一些设备手册中；本词条统一采用“言语接收阈”，同时保留上述同义名称，避免因翻译差异误认为存在三种不同检查。[1](#ref-speech-reception-threshold-asha)[4](#ref-speech-reception-threshold-manual)

**言语检测阈**（SDT；也常称言语察觉阈 SAT）只要求报告声音出现，不要求知道是什么词。一个人可能已察觉轻微声音，却仍无法辨认词义。检测与识别分别对应不同的反应事件，两条心理测量函数也可以不同。因此，无法完成识别任务时得到的检测阈，应按检测任务报告，不宜直接填入 SRT 栏。[2](#ref-speech-reception-threshold-iso)[1](#ref-speech-reception-threshold-asha)

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/speech-reception-threshold/01-detection-recognition-and-ceiling.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/speech-reception-threshold/01-detection-recognition-and-ceiling.svg" alt="言语检测与识别的不同阈值，以及无法达到50%正确率的示意" loading="lazy" /></a>
<figcaption><p>图 1　检测、识别与目标阈值。左图分别构造检测和识别曲线，50% 点为 18 和 28 dB HL；这 10 dB 差值只服务本图，不是固定换算常数。右图的识别上限为 40%，曲线未达到 50%；上限一半对应的 20% 点不能改称 50% 言语接收阈。两图不是患者资料。</p></figcaption>
</figure>

### 阈值与阈上识别率

固定呈现水平下得到的言语识别率，回答“在这个水平能认对多少”；SRT 则回答“达到目标需要什么水平”。前者通常用百分比，后者通常用分贝。单音节词、双音节词和句子在固定水平下的得分，都可能是有价值的功能指标，但不能仅因出现“识别”二字就称为接收阈。[5](#ref-speech-reception-threshold-adult)[6](#ref-speech-reception-threshold-zhu)

最高识别率、最舒适言语声级和 SRT 也不是同一指标。若听者在可用且适宜的条件下始终达不到 50%，应报告目标阈值未能确定及测量范围，而不是把最高分的一半、最后一次正确反应或设备最大输出作为 SRT。高声级处的曲线还可能不再单调；此时需要保留完整结果与解释条件。[2](#ref-speech-reception-threshold-iso)

| 指标或任务 | 听者需要做什么 | 主要结果 | 解释重点 |
| --- | --- | --- | --- |
| 纯音听阈 | 判断某频率声音是否出现 | 各频率 dB HL | 检测敏感度与频率分布 |
| 言语检测阈 | 察觉言语刺激的声音出现 | 标明参考的言语声级 | 不要求识别内容 |
| 安静中的言语接收阈 | 辨认规定词语或其他材料 | dB HL、dB SPL 或测试规定的声级 | 参考零点及材料必须明确 |
| 噪声中的言语接收阈 | 在指定干扰中辨认内容 | 常为 dB SNR | 干扰、评分单位和空间条件必须明确 |
| 固定水平言语识别率 | 在一个指定水平辨认材料 | 正确率（%） | 不自动提供目标阈值 |

### 50% 是哪一种正确率

50% 可以指一半词语、一半关键词、一半数字串，或一半句子被判为正确。整句全部正确与逐词得分是不同事件；一个句子遗漏一个关键词，在逐词计分中只损失部分得分，在整句计分中却可能被判错。报告“句子 SRT”时，应说明究竟采用哪一种计分方式。[7](#ref-speech-reception-threshold-hint)[8](#ref-speech-reception-threshold-mhint)

研究中也可以估计 70%、75% 或其他正确率所需的水平，宜明确写作相应目标的阈值，例如“75% 言语识别阈”（$\mathrm{SRT}_{75}$），而不默认读者理解为传统 50% SRT。另一些实验调整的是言语稀疏程度而非声级：原子语音模型研究使用每秒原子数作为自变量。它应用了识别阈值思想，但其量纲不能与临床声级或噪声信噪比互换。[9](#ref-speech-reception-threshold-levitt)[10](#ref-speech-reception-threshold-atomic)

## 心理测量函数与阈值的意义

### 从一组反应到一条曲线

在固定材料和环境下，可以于多个呈现水平测试，统计识别正确率，再描述正确率随声级或信噪比变化的函数。通常较有利的条件对应较高正确率，但一个有限词表中的百分比仍是抽样结果，不是没有误差的概率。阈值是曲线在目标正确率附近的位置，曲线斜率则描述这一带表现改变的快慢。[11](#ref-speech-reception-threshold-wichmann)[12](#ref-speech-reception-threshold-thornton)

相同 SRT 可以伴随不同斜率。例如，两条曲线都在 −6 dB SNR 达到 50%，一条随后迅速上升，另一条上升较缓；在高正确率区间，两种条件的差别便可能不同。反过来，相同的 10 个百分点变化，在不同斜率下对应的分贝变化也不同。阈值便于比较，但不能完整代替识别曲线。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/speech-reception-threshold/02-threshold-slope-and-asymptotes.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/speech-reception-threshold/02-threshold-slope-and-asymptotes.svg" alt="相同阈值不同斜率，以及猜测和失误影响50%点的心理测量函数" loading="lazy" /></a>
<figcaption><p>图 2　曲线位置、斜率与渐近线。左图两条教学曲线均在 −6 dB SNR 达到 50%，斜率不同。右图人为设定下渐近线 10%、上渐近线 95%，曲线位置参数为 −6 dB SNR，但原始正确率的 50% 点约为 −6.21 dB SNR。图中参数不是任何测试的常模，也不由某一实际材料的选项数推导。</p></figcaption>
</figure>

### 开放集合、封闭集合与猜测

开放集合允许听者自由复述，封闭集合则从有限选项中选择。封闭集合提供了额外的候选信息，随机选择也可能获得正确反应；选项熟悉程度、相似性和反应偏好还可能影响实际表现。因此，改变界面中的备选词数量，会改变任务本身，不能认为只改变了操作便利性。英文等重音双音节词的研究也表明，仅匹配词语阈值不足以保证整个识别函数等价。[13](#ref-speech-reception-threshold-bilger)

若界面有十个数字，逐个数字的等概率随机猜测率可为 1/10；若要求三个位置全部正确，独立随机选择的整串正确率才是 1/1000。这是概率计算，不代表真实听者一定按这种方式猜测。逐数字、整串与部分正确计分必须分别定义，不能用一个“十个选项”代替任务的统计描述。

### 注意失误与目标可达性

听者可能在较容易的刺激上偶尔漏答，难度很高时也可能靠猜测答对。拟合模型可用上下渐近线描述这些现象，但参数需要数据支持。短测验只在阈值附近采样时，往往难以同时估计斜率、猜测和失误；过多自由参数可能使结果看似精细，实际却很不稳定。[11](#ref-speech-reception-threshold-wichmann)

在有明显下渐近线的任务中，50% 原始正确率不一定处于整个可用反应范围的中点。研究报告应区分原始正确率、经猜测校正的正确率和函数位置参数。程序给出的一个参数名为“threshold”，并不保证它就是该任务定义的 SRT；需要核对拟合函数与取值规则。[14](#ref-speech-reception-threshold-psignifit)

## 言语材料与中文测试

### 好的测试材料需要怎样验证

词语熟悉度、声学质量、难度一致性和词表间等价性共同影响测量。两个词即使均方根声级相同，也可能因发音、时长、音节线索或语言熟悉度而具有不同识别难度。一个词表在容易条件下均为满分，也不能证明它在接收阈附近、降质言语或听力损失人群中保持等价。[13](#ref-speech-reception-threshold-bilger)[6](#ref-speech-reception-threshold-zhu)

材料开发因而需要测量识别函数，检查词表差异及复测表现，而不只是从词典中挑选常用词。英语临床 SRT 常用两个音节重音相当的词，即等重音双音节词；这是特定语言传统，并不意味着中文必须机械寻找一套相同韵律结构的翻译词。跨语言比较应依据经过验证的各自版本。[15](#ref-speech-reception-threshold-nissen)[2](#ref-speech-reception-threshold-iso)

### 普通话词语与声调

普通话材料涉及声母、韵母及[普通话汉语声调](../mandarin-lexical-tone/)的分布。声调改变词义，熟悉的词语组合又能帮助补全不清晰的音节。词表平衡需要与测量目的对应：测量安静中低水平识别、测量阈上词语表现、评价人工耳蜗线索利用，可能需要不同的材料和验证条件。[6](#ref-speech-reception-threshold-zhu)

Nissen 等 2005 年开发普通话三音节 SRT 材料，测量每个词的心理测量函数，并选择、调整材料，使识别阈值和斜率更一致。它说明中文 SRT 可以通过原生材料建立，不必直接套用英文词表。该研究的正常听力样本和特定录音，也不代表材料已在所有地区、年龄及听觉状态下具有同一参考值。[15](#ref-speech-reception-threshold-nissen)

Zhu 等 2012 年开发的普通话双音节识别材料，重视声母、韵母和声调平衡，并在正常听力者聆听原始及声码器处理言语的条件下检验词表表现。该实验主要使用固定呈现水平和音节计分，不能把“材料经过验证”自动解释为已经建立临床 SRT 常模。[6](#ref-speech-reception-threshold-zhu)

### 句子、数字与生肖材料

噪声下汉语言语测试 MHINT 使用句子，并通过自适应程序测量安静及噪声条件下的句子接收阈。Wong 等 2007 年分别开发大陆普通话与台湾普通话版本，验证材料难度、词表可靠性及参考表现；两版本的绝对结果并非完全一致。测试时还包含不同噪声方位，说明“用同一种语言”并不足以定义完整测试条件。[8](#ref-speech-reception-threshold-mhint)

数字噪声测试常使用连续数字串，使材料和自动评分较容易控制。Smits 等开发的电话数字噪声筛查建立了自身材料与参考体系，不能把某一种语言的数字常模直接搬到另一种语言。数字测试减少了一部分词汇复杂性，但仍需要听者认识数字、理解顺序和完成规定的反应。[23](#ref-speech-reception-threshold-smits)

[生肖噪声测试](../zodiac-in-noise/)使用生肖材料构造中文识别任务。Zhou 等的开发与验证工作说明，常用中文词汇可以支持网络噪声言语筛查；它的 SRT 与生肖词组、评分、呈现和参考人群相联系。该指标不等同于安静中的词语接收阈，也不应直接与数字或句子测试的数值比较。[24](#ref-speech-reception-threshold-zin)

## 安静条件下的测量

### 准备、熟悉与反应方式

测试前应确认听者理解任务，并能在适当可听水平识别所用词语。临床词语阈值测量中的材料熟悉，是减少陌生词带来误差的步骤；不宜将听者本来不认识的词当作听觉失败。反应可以是复述、指出图片或其他适合能力的方式，但替换方式后，任务及参考数据也可能改变。[1](#ref-speech-reception-threshold-asha)[5](#ref-speech-reception-threshold-adult)

熟悉材料与正式识别测试要区分目的。有的测试要求预先熟悉固定词集，有的开放集合词语测试则避免提前暴露正式项目。不能把一种程序的熟悉规则推广到所有言语检查。复测还需考虑重复材料带来的学习，尽量按测试说明安排训练和等价词表。

### 阈值程序与纯音测听的区别

言语刺激每次包含不同信息，既要控制呈现水平，又要判断内容是否正确。ASHA 1988 年程序采用词语熟悉、下降系列及统计计算来估计 50% 点；它不是将纯音的“下降 10、上升 5 dB”规则原样移植后，记录最后一次认对的水平。正式结果应来自所采用言语测试的计分与阈值规则。[1](#ref-speech-reception-threshold-asha)

其他经过验证的程序可以采用不同步长、项目数量或自适应方法。更短的流程需要证明节省时间后仍能保留适当的重复性和准确性。对儿童、语言困难者或反应方式受限者的调整，还应明确记录，避免将调整后的结果无条件纳入成人原版常模。[16](#ref-speech-reception-threshold-chen)[2](#ref-speech-reception-threshold-iso)

### 与纯音平均听阈相互核对

安静中的传统词语 SRT 可用于核对纯音结果：若两类测量对同一耳的敏感度描述明显不一致，应检查纯音可靠性、言语材料、语言理解及测量条件。常见的比较对象是 500、1000、2000 Hz 的平均听阈，但在明显倾斜的听力图中，概括方式及言语频谱会影响这一关系，不能把任何三频平均都当作 SRT 的精确预测式。[1](#ref-speech-reception-threshold-asha)

这种核对是寻找不一致的工具，不是仅凭差值确定病因的诊断算法。还应分清耳别：双耳呈现或声场中的识别结果不能直接与任意单耳平均听阈对应。噪声中的 SRT 涉及另一组限制；Vermiglio 等的 HINT 研究表明，纯音平均值与安静识别及稳态噪声识别的关系并不相同。[17](#ref-speech-reception-threshold-vermiglio)

## 声级、校准、耳别与掩蔽

### 言语声级的参考零点

报告 dB HL 时，需要使用相应言语材料、录音及呈现条件的参考框架，不能把纯音某一频率的参考声压直接作为所有言语的参考。报告 dB SPL 时，则要说明在何处、采用何种测量设置确定声压。声场测试还涉及扬声器、位置与距离；这些条件共同决定数值的可追溯性。[2](#ref-speech-reception-threshold-iso)

相同数字增益不保证不同词语具有相同可懂度。峰值、整段均方根、活跃言语段声级和设备表头读数也不一定相等；录音中的停顿会影响某些平均方法。比较两套材料时，应核对其校准说明、参考录音及响度控制方式，而不只是把文件峰值归一化。[13](#ref-speech-reception-threshold-bilger)[7](#ref-speech-reception-threshold-hint)

录音材料便于固定说话人和声音质量；现场口述则增加了语速、发音和声级变化。为了让复测与跨地点结果可比，应记录呈现方式及材料版本。手机、耳机或浏览器能播放音频，并不自动建立有效的听力级零点，尤其不能把系统音量百分比写成 dB HL。可结合[听力测量校准](../audiometric-calibration/)理解量值来源。[2](#ref-speech-reception-threshold-iso)

### 对侧掩蔽与同侧竞争声

耳机给一耳呈现言语时，声音仍可能经跨耳路径被另一耳识别。需要建立耳别结果时，应评估非测试耳贡献，并在必要时使用覆盖言语频谱的适当掩蔽声。言语包含较宽的频谱，不能不加区分地把纯音窄带掩蔽的设置直接套用。判断与记录还需考虑换能器和耳间衰减。[1](#ref-speech-reception-threshold-asha)[2](#ref-speech-reception-threshold-iso)

对侧掩蔽与噪声言语测试中的竞争声承担不同任务：前者控制“究竟是哪一耳在提供反应”，后者构成要评价的聆听困难。竞争声可以与言语送到同一耳、双耳或不同空间位置。若报告只写“有噪声”，却不写噪声送到哪里，读者便无法判断它是在建立耳别还是在测量噪声识别能力。

## 噪声中的言语接收阈

### 信噪比及负值的含义

噪声中常将言语与竞争声的声级差作为自变量。在相同声级参考和测量约定下：

$$
\mathrm{SNR}=L_{\mathrm{speech}}-L_{\mathrm{noise}}.
$$

例如，言语为 57 dB SPL、噪声为 65 dB SPL 时，信噪比为 −8 dB。负号表示言语总体声级低于噪声，而不是声压为负或没有声音。若同一测试和目标下某条件的 SRT 从 −5 降至 −8 dB SNR，便表示能够在更不利信噪比下达到相同识别水平，阈值改善为 3 dB。

信噪比没有保留绝对声级的全部信息。噪声较低时，言语可能先受自身可听性限制；绝对水平改变还会影响听觉和设备处理。因此，“两次都是 −5 dB SNR”不保证两次测试完全等价。应同时报告固定的是言语还是噪声、其声级，以及另一信号怎样调整。[18](#ref-speech-reception-threshold-plomp)[8](#ref-speech-reception-threshold-mhint)

### 竞争声的类型与空间位置

稳态言语谱噪声、起伏噪声、多人嘈杂声和单个竞争说话人提供不同干扰。稳态噪声主要降低频谱中信息的可听性；起伏背景还可能留出短暂的较有利时域片段；竞争言语则同时涉及相似声源的分组与选择。换用干扰后，即使平均声级不变，识别曲线和阈值也可能改变。[19](#ref-speech-reception-threshold-fade-paper)[20](#ref-speech-reception-threshold-bsa)

言语与噪声的空间分离可带来两耳信噪比差及双耳线索收益。因此，正前方言语、正前方噪声的阈值，与噪声来自侧面的阈值应分别记录。耳机模拟的空间条件还需说明信号实现方式，不能等同于任意房间的实际扬声器布置。这与[空间听觉](../spatial-hearing/)和[掩蔽](../masking/)直接衔接。[8](#ref-speech-reception-threshold-mhint)

### 原始 SRT 与信噪比损失

原始 SRT 是该测试的目标信噪比；**信噪比损失**则是听者阈值相对同一测试参考人群所需额外信噪比。例如，参考阈值为 −8 dB SNR，听者为 −3 dB SNR，差值为 5 dB。它描述相对表现，不是把纯音听力损失换成另一种分贝，也不能借用别的测试参考零点计算。[20](#ref-speech-reception-threshold-bsa)[18](#ref-speech-reception-threshold-plomp)

一个筛查版本设定的截断值，还承担分类任务。其灵敏度、特异度、目标听力损失定义及参考人群与连续 SRT 指标有关，却不是同一概念。不能因为某测试阈值低于另一个测试，就认定其筛查性能更好。只有在相应验证设计中，才可评价分类能力。[23](#ref-speech-reception-threshold-smits)[24](#ref-speech-reception-threshold-zin)

## 自适应测量与评分规则

### 正确后更难、错误后更容易

自适应程序根据听者反应选择下一次刺激，使测量集中在目标附近。对信噪比越大越容易的任务，正确识别后通常降低信噪比，错误后提高信噪比。在等步长、反应近似独立且稳定的二元反应条件下，一次正确下降、一次错误上升的规则追踪约 50% 正确率；连续两次正确才下降、一次错误即上升的规则则约追踪 70.7%。这些是特定升降规则的性质，不是“自适应”这个名称自动赋予的目标。[9](#ref-speech-reception-threshold-levitt)

若每次句子提供多个关键词得分，程序还可以根据部分正确率改变下一次水平。这时调整幅度、目标和收敛性质要按具体算法解释，不能把多级得分粗略当作一次二元正确或错误。改变升降步长比例，也可能改变追踪的目标。因此，软件版本和实际算法应作为方法的一部分保存。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/speech-reception-threshold/03-adaptive-search-and-snr.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/speech-reception-threshold/03-adaptive-search-and-snr.svg" alt="自适应信噪比搜索的人工反应序列与负信噪比计算示例" loading="lazy" /></a>
<figcaption><p>图 3　搜索规则与单位。左图人工指定 24 次正确／错误反应，以 2 dB 等步长生成下一次信噪比；本例排除前四次，仅展示后 20 次呈现水平平均值的计算。它不是任何测试的完整正式流程，也没有模拟真实听者。右图单独说明声级相减：57−65 为 −8，60−65 为 −5 dB SNR；这些数值与左图没有配对关系。</p></figcaption>
</figure>

### 起始阶段、步长与终止规则

较大的起始步长可较快接近目标，较小步长则有助于在目标附近采样。估计值可能来自指定呈现水平的平均、转折点平均或模型拟合；这三种计算不是同一操作。起始试次是否计入、列表长度与结束后如何计算，应依测试说明处理，不能从其他论文拼接出一个未经验证的新程序。[7](#ref-speech-reception-threshold-hint)[22](#ref-speech-reception-threshold-plomp-reliability)

项目数量增加不必然线性提高精度。词表等价性、斜率、起始点和练习同样影响效率；疲劳还可能改变后段反应。较短流程应在目标人群中检查测试—重测误差，较长流程也应确认不会仅重复熟悉内容。阈值没有到达稳定范围或超过设备条件时，应保存轨迹和失败原因。[22](#ref-speech-reception-threshold-plomp-reliability)[16](#ref-speech-reception-threshold-chen)

### 逐词计分与整句计分

评分改变的不是标签，而是被估计的事件。为说明这一点，可以假设一句含五个等难、相互独立的关键词，单个关键词正确概率为 $p$。逐关键词正确率为 $p$，五个关键词全部正确的概率为 $p^5$。因此，逐词 50% 与整句 50% 在这个教学模型中对应不同难度。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/speech-reception-threshold/04-word-versus-sentence-scoring.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/speech-reception-threshold/04-word-versus-sentence-scoring.svg" alt="五个关键词独立等难的教学模型中逐词与整句计分得到不同阈值" loading="lazy" /></a>
<figcaption><p>图 4　评分单位决定“50%”的含义。教学模型假设五个关键词等难且相互独立：逐词 50% 时，整句全部正确约为 3.1%；整句 50% 时，单词正确概率约需 87.1%。真实句子存在语境和词间依赖，不能按照本图换算实际测试结果。图中曲线不是 MHINT 或其他句子测试的实测函数。</p></figcaption>
</figure>

复述中允许哪些同义词、语序变体、音节遗漏或声调错误，也需要预先规定。现场评分人员应按统一规则记录，自动识别系统则需检查误转写和评分偏差。评分器本身会犯错，因此不能用机器“没认出”直接代替听者“没听懂”。

## 重复性、比较与研究报告

### 误差、学习和材料效应

Plomp 与 Mimpen 的经典句子研究展示了通过筛选词表提高阈值可靠性的思路；其特定列表的误差不能作为所有 SRT 的统一精度。英语 HINT、普通话版本、数字测试以及不同听觉状态都应具有各自的可靠性资料。材料熟悉、任务练习、词表顺序和设备设置改变，也可能影响复测。[22](#ref-speech-reception-threshold-plomp-reliability)[7](#ref-speech-reception-threshold-hint)[8](#ref-speech-reception-threshold-mhint)

固定水平识别分数有项目抽样波动。Thornton 与 Raffin 的二项模型研究解释了词表长度与百分比变异的关系，但一个得分的置信区间不能原样用作自适应 SRT 的分贝置信区间。阈值误差还受曲线斜率及采样程序影响；应优先使用该方法的重复测量或适当模型估计。[12](#ref-speech-reception-threshold-thornton)[11](#ref-speech-reception-threshold-wichmann)

### 配对改善与不确定性

对同一听者比较两种噪声处理、设备设置或空间条件，应保留配对结果。若约定改善为 $\mathrm{SRT}_A-\mathrm{SRT}_B$，正值表示 B 的阈值更低。组平均改善并不保证每个人都改善，统计显著也不自动等于某个听者的变化超过复测误差或具有实际交流价值。

<figure class="encyclopedia-figure">
<a href="/n3-hearingpedia/figures/speech-reception-threshold/05-paired-srt-differences.svg" target="_blank" rel="noopener" aria-label="查看完整图片"><img src="/n3-hearingpedia/figures/speech-reception-threshold/05-paired-srt-differences.svg" alt="人工构造的个体配对SRT与阈值改善量分布" loading="lazy" /></a>
<figcaption><p>图 5　个体与平均结果。八位教学听者的组平均改善为 2.0 dB，但其中一位为 −1 dB、一位为 0 dB。所有数值人工构造；图中没有复测或置信区间，不能据此推断统计显著、临床获益或设备效能。</p></figcaption>
</figure>

方法比较还应检查偏差与一致性。两套测试的相关系数高，可能表示它们均随听觉状态变化，却不证明数值可互换。语料、计分或参考值不同带来的系统差，不能简单归因于某套方法更准确。用于随访时，应尽量维持原来的材料版本和测试条件。

### 一个可解释的 SRT 报告

报告宜明确材料名称与语言版本、词表、目标正确率及评分单位、呈现声级参考、耳别或声场、助听状态、竞争声与空间条件、自适应或固定水平程序、训练安排、阈值计算方式及重复性。若使用了对侧掩蔽，应把它与任务竞争声分开说明；若未能得到目标阈值，应保留范围和原因。[2](#ref-speech-reception-threshold-iso)

可以写成：“普通话某版本句子测试，目标为 50% 整句正确；双耳耳机呈现，稳态言语谱噪声固定于规定声级，自适应调整言语；SRT 为 −5.2 dB SNR。”这只是报告结构示例，其中没有指定真实测试协议。比起“言语阈值为 −5.2”，完整描述能让读者判断比较是否成立。

## 应用、适用人群与解释边界

### 综合听觉评价与设备效果

安静中的词语 SRT 可补充检测敏感度评价，噪声中的 SRT 则帮助描述困难背景下的识别。两者与纯音听阈、阈上言语识别率及听者自述相互补充。对安静中表现较好却在多人场景困难的听者，增加合适噪声任务通常比仅重复同一安静测试更能提供相关信息。[5](#ref-speech-reception-threshold-adult)[20](#ref-speech-reception-threshold-bsa)

助听器或人工耳蜗研究可用 SRT 比较处理设置，但裸耳、助听、双耳及单耳结果需要明示。方向性和降噪收益与场景有关；扬声器的方位、噪声类型和声级变化，都可能使算法效果改变。因此，实验中改善几分贝应解释为该条件下的识别收益，而不是所有日常交流场景的一般提升。[19](#ref-speech-reception-threshold-fade-paper)

### 儿童、语言与认知因素

儿童对词汇、句子长度及反应方式的掌握随年龄变化。Chen 与 Wong 的儿童 MHINT 开发研究建立了适龄句子及年龄相关参考，说明成人材料和成人常模不宜直接用于儿童。图片选择也需考虑图像理解与候选信息；当任务不适合能力时，较差结果不应全部归因于听觉敏感度。[16](#ref-speech-reception-threshold-chen)

语言经验、注意和记忆参与识别反应。普通话口音和地区用语差异也会影响对材料的熟悉，因此需要注明听者的语言背景及测试版本。对外语使用者或认知沟通受限者，应选择经过相应验证的材料和任务。SRT 不是脱离语言的纯粹感官读数，也不能凭单次异常定位某一神经结构。[5](#ref-speech-reception-threshold-adult)[8](#ref-speech-reception-threshold-mhint)

### 筛查与远程测试

网络数字或生肖任务能扩展测试可及性，但筛查输出只回答其验证的分类或功能问题。双耳同时呈现可能主要由较好耳或双耳过程决定，不能自动排除单侧问题；噪声、耳机佩戴、音频链及参与者是否按指令操作，都需要质量控制。筛查后的建议还应遵循该项目设定的复核路径。[23](#ref-speech-reception-threshold-smits)[24](#ref-speech-reception-threshold-zin)

远程噪声 SRT 对总增益在部分条件下可较为稳健，但不意味着可以忽略绝对可听性和设备频率响应。尤其在听力损失、低输出或背景干扰条件下，呈现链可能改变结果。验证一种网站或耳机配置获得的证据，不应扩展成所有消费设备均适合测听的结论。

## 计算模型、算法与公开实现

### 心理测量函数与阈值求解

一个常用教学模型为：

$$
P(x)=\gamma+(1-\gamma-\lambda)\frac{1}{1+\exp[-(x-\theta)/b]},\qquad b>0.
$$

$x$ 为呈现水平或信噪比，$\theta$ 为曲线位置，$b$ 控制斜率，$\gamma$ 为下渐近线，$1-\lambda$ 为上渐近线。二元识别反应可用伯努利似然，多项目得分在适当独立假设下可用二项模型；相关关键词或过度变异则需要更合适的统计处理。模型应匹配真实评分事件。[11](#ref-speech-reception-threshold-wichmann)[12](#ref-speech-reception-threshold-thornton)

若目标 $p_t$ 严格位于两条渐近线之间，令 $q=(p_t-\gamma)/(1-\gamma-\lambda)$，其对应水平为：

$$
x_t=\theta+b\ln\frac{q}{1-q}.
$$

仅当目标位于可用范围中点时，$x_t$ 才等于 $\theta$。在 $\gamma=\lambda=0$ 的情况下，50% 点为 $\theta$；若最高可达概率低于目标，则没有有限的该目标阈值。这一公式用于解释拟合，不规定所有临床 SRT 都应使用逻辑斯蒂模型。

[psignifit 的 Python 仓库](https://github.com/wichmann-lab/python-psignifit)提供心理测量函数估计工具。使用时要核对实验类型、函数参数和阈值选取方式，并检查不确定性与拟合质量。它可以分析已有行为数据，但不包含临床材料验证、播放链校准或完整言语测听流程。[14](#ref-speech-reception-threshold-psignifit)

### 可听性与噪声识别的功能模型

Plomp 的衰减与失真框架将检测相关的水平损失与噪声下所需额外信噪比分开描述。这个区分有助于解释：共同放大言语与噪声可改善部分可听性，却不必改变外部信噪比或完全恢复噪声识别。模型中的“失真”是功能参数，不应直接等同于某一病变、认知诊断或助听器失真测量。[18](#ref-speech-reception-threshold-plomp)

这一框架提供解释结构，具体参数则依任务与数据确定。不能只用纯音平均值填入两个参数，就声称得到了个人的真实 SRT。模型预测还要与相同材料、掩蔽声及目标下的行为结果比较，并检查它是否同时解释安静和噪声条件。

### 基于自动识别的 FADE

FADE，即听觉辨别实验仿真框架，使用面向具体任务的自动识别系统，在不同信噪比下训练、测试并预测识别表现。它可以引入听觉加工限制及信号处理条件，构建预测曲线并求得 SRT。相关研究比较了稳态及起伏噪声中的表现，体现了从刺激和处理过程推断行为指标的路线。[19](#ref-speech-reception-threshold-fade-paper)

[作者公开的 FADE 仓库](https://github.com/m-r-s/fade)包含示例和说明，依赖 Linux 环境、HTK 及相应计算工具。仓库明确说明音频标度和材料要求，德国矩阵句子材料需要另外取得授权。开放代码不等于所有语料均可自由使用，也不保证未经重新验证的中文版本可以预测真人表现。[21](#ref-speech-reception-threshold-fade-code)

模型是评价机制假设和处理算法的工具，不是用机器识别结果代替个人听觉检查。更换声学特征、训练集、语言或识别器，可能改变输出。报告应区分真人测得 SRT 与模型预测 SRT，并保留训练测试条件及验证误差。

### 自动开发材料与本词条代码

Polspoel 等 2025 年的 Aladdin 研究结合合成言语与自动识别，对数字材料进行难度调整，并用真人验证荷兰语和英语测试。这提示计算模型还可辅助材料开发；其证据来自所验证的两种语言，不能认为合成中文词语后便自然获得有效的中文 SRT 参考体系。[25](#ref-speech-reception-threshold-aladdin)

本稿附有[配图生成代码](/n3-hearingpedia/figures/speech-reception-threshold/generate-figures.py)及[数值核查记录](/n3-hearingpedia/figures/speech-reception-threshold/figure-verification.json)。代码演示心理测量函数、自适应序列、计分概率与配对差值，全部使用人工构造数据，不播放音频、不连接设备，也不提供临床阈值测量功能。

## 研究沿革与关联词条

言语阈值测量由标准词语和录音程序逐渐扩展到句子、噪声、空间条件和网络筛查。1979 年的句子可靠性研究以及 1994 年 HINT 的开发，推动了以阈值而非单一固定水平得分描述噪声识别；普通话词语、MHINT 和生肖材料随后建立各自的语言与评分体系。计算模型又为材料等价、自动估计及处理算法评价提供了方法。共同的核心仍是明确“什么材料、什么反应、什么条件”才对应一个可解释阈值。[22](#ref-speech-reception-threshold-plomp-reliability)[7](#ref-speech-reception-threshold-hint)[15](#ref-speech-reception-threshold-nissen)[8](#ref-speech-reception-threshold-mhint)[24](#ref-speech-reception-threshold-zin)

可进一步阅读[纯音测听](../pure-tone-audiometry/)、[言语可懂度](../speech-intelligibility/)、[听力损失](../hearing-loss/)、[掩蔽](../masking/)、[空间听觉](../spatial-hearing/)、[助听器](../hearing-aid/)和[生肖噪声测试](../zodiac-in-noise/)。这些词条分别补充敏感度、识别功能、干扰机制、双耳线索和测量应用。
