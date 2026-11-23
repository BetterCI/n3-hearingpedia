# 可听度与助听可听度：证据与制作记录

核查日期：2026-11-24。正文为AI辅助深度草稿，status=draft，未进行具名专业审阅。

## 问题与范围

可听度描述什么，怎样从阈值与声学输出获得助听可听度，SII如何解释，为什么不能代替识别和长期获益？以气导声学助听器为主，区分成人与儿童。基础文献不设起始年；近期窗口明确为2023-01-01至2026-11-24。不作品牌排名、统一处方、植入决策或儿童结果保证。不是穷尽式系统综述。

## 检索、扩展与停止规则

使用官方标准工作组、专业指南、PubMed、PMC、出版社与原开发仓库。主题检索覆盖 aided audibility / SII / hearing aid verification / functional gain / input level / frequency lowering / count-the-dots。近年定向检索补入2023任务与风险研究、2024目标误差研究、2025教程与端点测试、2026数点法。

OpenAlex脚本解析种子W2229927133（McCreery等2015），向后和向前各获取12条。保存seed、backward、forward元数据；删除上游完整摘要和引文计数，避免转载摘要或将引用量误当质量。使用judge_relevance.py生成筛选提示，具体语义评估如下。引用网络用于发现，不单凭标题判定结果。

停止于一层：新候选主要转向语言、家庭、服务与教育结局，已超出本词条核心计算问题；核心声学、转换、非线性阈值与SII解释由直接核读来源覆盖，近期搜索已增加独立方法问题。该停止规则不代表所有相关论文均已检索。

## 引用网络初筛

下表的“仅元数据”意味着只用于决定是否进一步读取，不能支持论文结果；Core/Important为主题优先级，不是证据等级。

| 路径与候选 | 等级 | 研究对象及纳排原因 | 证据范围 |
| --- | --- | --- | --- |
| 种子 McCreery 2015纵向可听度 | Core | 随访儿童可听度变化及相关因素，支持声学随访边界 | 原文统计、限制、临床意义段及书目 |
| 后向 DSL multistage input/output | Important | 处方输入输出算法；算法细节由既有处方词条承载 | 仅元数据，未据此新增结果 |
| 后向早晚发现儿童三岁结局 | Background | 早期识别与结局，不能隔离可听度作用 | 仅元数据，不引 |
| 后向 Early Amplified Children auditory development | Important | 听觉交流发展，可连接长期结局，正文采用更直接声学证据 | 仅元数据，不引 |
| 后向新生儿筛查随访因素 | Exclude | 服务随访与筛查管理，不是助听可听度计量 | 仅元数据 |
| 后向 Pavlovic 1987参数 | Core | 频带重要性、阈值与言语参数，直接对应SII结构 | 原始摘要、工作组托管首页 |
| 后向儿童成人听损构型进展 | Background | 听阈构型背景，非助听输出验证 | 仅元数据，不引 |
| 后向 Ontario amplification protocol | Important | 儿童配置与验证协议，当前正文以BSA及DSL协议支撑 | 仅元数据，不引 |
| 后向 Australia pediatric protocol | Important | 同上，避免叠加不同司法地区流程 | 仅元数据，不引 |
| 后向 preschool language and services | Background | 服务与语言结局，不能直接估计声学获取 | 仅元数据，不引 |
| 后向 nonlinear frequency compression development | Important | 移频与发育，可能扩展处理限制；本稿未做结果推断 | 仅元数据，不引 |
| 后向 NAL new selection procedure evaluation | Background | 历史处方，原理由独立处方词条承载 | 仅元数据，不引 |
| 后向 in-situ output probe-microphone method | Core | 输出验证方法，与主题直接相关；采用已读BSA规范作为流程依据 | 仅元数据，不引结果 |
| 前向 Year 2007 Position Statement | Exclude | 年代早于种子，网络边或聚合记录可疑，不视为真实后续引用 | 仅元数据 |
| 前向 OCHL introduction | Background | 队列整体背景，同期文献，不代表后续验证 | 仅元数据，不引 |
| 前向 vocabulary depth/breadth mixed model | Important | 纵向语言轨迹，超出本文声学主线 | 仅元数据，不引 |
| 前向 aided hearing and academic outcomes | Important | 学业与助听关系，留作长期结局研究 | 仅元数据，不引 |
| 前向 multidimensional family-centred model | Background | 家庭早期干预概念模型，不能验证SII预测 | 仅元数据，不引 |
| 前向 parental linguistic input | Background | 语言输入情境，与声学获取互补 | 仅元数据，不引 |
| 前向 auditory experience and executive function | Important | 听觉经历及认知结局，需另行核读因果与协变量 | 仅元数据，不引 |
| 前向 family environment HA/CI | Background | 家庭环境与多种结局，装置混合且非本稿主问题 | 仅元数据，不引 |
| 前向 school career nationwide | Background | 教育安置长期结局；上游标题存在编码异常，保留原始记录但不引 | 仅元数据 |
| 前向 FCEI-DHH guiding values | Background | 家庭干预价值框架，非可听度算法 | 仅元数据，不引 |
| 前向 longitudinal hearing aid use | Important | 使用时长区别于声学可听度，正文避免未经核读的剂量公式 | 仅元数据，不引结果 |
| 前向 speech recognition and parent ratings | Important | 行为与家长报告可补声学指标，本稿以2023直接研究补充 | 仅元数据，不引 |

## 正文证据地图与实际访问

- ASHA Hearing Aids for Adults：官方实践页面。支持多声级输出与多维验证。非随机试验。
- ASA/ANSI S3.5：复用站内标准书目；未取得付费全文。S3-79工作组页面及Pavlovic原始摘要支持加权与参数解释，不宣称全文算法复现。
- BSA 2018 REM指导：官方32页PDF。复核术语、真耳/测试箱和声级测量框架；未称其2026年新指南。
- DSL 2005 clinical protocols：复用已有核读登记；本轮PMC直接请求遇到访问检查，未绕过。其耳道转换公式再以官方设备文档的RECD转换说明核对；正文只给条件化示意，不转录校准表。
- Holube 2010：PubMed原始摘要，ISTS属性、重混与百分位测量。不是识别句表。
- Kuk & Ludvigsen 2003：出版社公开助听阈值章节，阈值/功能增益与非线性。第三方聚合标2002，与出版社冲突，采用2003。未把历史20 dB HL建议作为新规范。
- Google SII仓库：读取README；2026-04-18归档。只作为学习入口，无临床认证或仍维护的断言。一次猜测raw路径404，不采用该路径或声称读过算法代码。
- Wiseman等2025教程：PMC正文定义、计算、验证及频率降低段可读。更新既有引用access至fulltext；本稿主要引用频率映射限制，骨导/CI不直接套用声压计算。
- McCreery等2015：PMC可检索Statistics、Limitations、Clinical implications及PubMed元数据；后续访问偶发检查页。重点是纵向声学差异、听损/偏差关联及未含使用时长的限制。
- Wiseman等2024：既有原始摘要与本轮PMC可检索方法/结果；RMS误差与SII不是同一量。注意原文片段把RMS称为geometric mean并不准确，本文给标准平方均值开根号定义，不照搬该措辞。
- Wiseman等2023：PubMed原始摘要；182/78样本、0.61及0.53–0.68区间。保留观察预测性质，不将教程对区间的临床解释改成统一界值。
- Pittman & Stewart 2023：出版社与PMC可检索方法/结果，16名9–17岁参与者；辨别识别、回忆与学习任务，不从未显著推出等效或可听度无用。
- Rhebergen & Pavlovic 2026：PubMed原始摘要；14776张听力图、8个BIF、安静方法比较。出版社正文访问失败，保留abstract。
- Pedersen等2025：出版社摘要、引言与方法可读；30成人、丹麦语、同访重复。HINT-L是句子识别阈而非纯检测阈，HINT-U是响度分类。

## 综合、分歧与空白

一致性：必须统一声学参照并报告输入条件；输出验证、加权获取、识别与长期获益相互补充。分歧/限制：可听度变化对不同任务与人群的预测不一致，不能由总分导出统一正确率。2026数点法在匹配条件下近似标准模型，不代表噪声/助听/高声级均可替代。频率降低、动态噪声、语言差异和双耳整合仍需专用证据。

未纳入针对警报器、通信码率或医学抗体“SII”等同名无关结果。未使用任何患者数据或品牌性能数据。

## 原创图与数值核验

三幅图均由generate.py生成SVG及PNG，参数公开。图1为四个教学频带、平均值±15 dB范围，并非ANSI动态范围或真实百分位。图2仅定义输入20—70 dB SPL的两段函数，不外推检测概率或安全输出。图3为虚构三带Q指数，明确不是标准SII。

断言核对：40+5+10=55 dB SPL、阈上余量10 dB；两个60 dB频带能量和63.0103 dB；共同检测端点(20,50)，60 dB输入时输出90/70；Q为0.31/0.67及0.60/0.60，差值0.36。已逐张查看PNG，中文无缺字、图例与曲线无明显遮挡。SVG文字使用路径，避免网页缺字体。

## 发布前工程与网页核验

内容检查通过：166词条、1181关联、7929次引用、768幅正文图。20项现有工作流测试通过，基底膜既有核验通过；其生成的无关验证文件已恢复。pnpm check：273文件，0错误、0警告、0提示。生产构建通过；全站verify覆盖373页、35422个内部链接，断链为0。构建仍有既有资源块体积提示，未新增处理逻辑。桌面及390×844视口实测：手机clientWidth=scrollWidth=375，无整页横向溢出；正文、SII与算例公式、加权图及末节表格显示正常；KaTeX错误与缺失参考锚点均为0。临时视口已复原。
