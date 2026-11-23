# 助听器获益与效果评估：检索与编辑记录

日期：2026-11-24。成人声学助听器为主体；问题是怎样定义、测量和解释获益，而非产品购买建议或个体诊断。近期窗口为2023-01-01至2026-11-24，同时保留量表与测量方法的经典来源。本次为定向证据检索，不声称系统综述或穷尽检索。

## 检索方法

使用deep-research技能：主题检索→强种子解析→前后向扩展→语义筛选→原始来源核验。主题包括hearing aid outcomes/benefit、verification/validation、APHAB/IOI-HA/COSI、baseline/minimal important difference、ecological momentary assessment，以及服务模式随机比较。通过PubMed、出版者页面、ASHA、NAL、ICRA、HARL、NICE获取来源。

OpenAlex种子为Humes等2017随机安慰剂对照试验，DOI 10.1044/2017_AJA-16-0111，W2593164649。前向与后向各读取12条，保存在forward.json、backward.json；seed.json记录种子。公开文件仅保留书目与网络元数据，不发布摘要全文。首次重定向受Windows GBK影响，使用PYTHONIOENCODING=utf-8重跑并验证JSON。少数OpenAlex题名原始元数据仍有替换字符，未用于正文引用或擅自补写。

筛选不以引用量代表质量。每项先判断实际研究对象及方法，再判断与效果测量的关系。前后向池给出方法与研究史，针对2025–2026的新工作另作主题搜索，避免只靠高被引顺序遗漏新研究。

## 语义筛选与引用决策

| 候选或谱系 | 对象与方法 | 相关性及处置 |
| --- | --- | --- |
| Humes 2017，种子 | 老年轻至中度损失；专业、消费者选择与安慰剂设置随机比较 | Core：说明干预包、对照与多结局；复用aging-humes-2017 |
| De Sousa 2023，主题与前向 | 同设备、自验配与专业验配、六周成人试验 | Core：支持模式与人群限定；复用已有文献ID |
| Wu 2025，主题 | 服务模式与技术等级随机比较、即时结局 | Core：与2023不同设计形成解释对照；复用已有ID |
| Humes/Dhar/Singh 2025，主题 | APHAB文献及584人试验数据再分析 | Core：基线依赖、MDD与MCID；注册hao-baseline-2025 |
| Cox/Alexander 1995，主题 | APHAB开发与评价 | Core：工具起源及分量表；原始摘要核验 |
| HARL APHAB手册，主题 | 官方计分与显示规则 | Core：全局评分排除AV；documentation |
| NAL COSI，主题 | 开发机构的个体化目标测量工具 | Core：变化与最终能力、儿童版边界；documentation |
| ICRA IOI-HA，主题 | 七项目多维轮廓 | Core：用途与限制；documentation |
| Carney/Schlauch 2007，主题 | 单音节词两次成绩临界范围的模拟 | Important：误差与列表长度；摘要，不转载临界表 |
| FUEL 2016，主题 | 努力聆听的理论框架 | Important：成绩与资源投入不同；不是疗效试验 |
| Carbajo Benito等2026，主题 | 30人、15天随机交叉，直接与间接EMA | Core：检出差异、场景代表性与参与负担的取舍；摘要 |
| NASEM 2025 / ASHA实施说明，主题 | 成人听觉干预核心结局集合 | Core：实际阅读并引用ASHA官方实施说明；原报告章节被访问检查拦截 |
| NICE NG98，主题 | 成人服务与随访建议 | Important：官方1.7.1–1.7.2可读检索内容和PDF段落；直接网页403 |
| ACHIEVE 2023及2024交流分析，主题 | 随机干预主要认知与次级自评交流结局 | Important：终点不能互换，复用已有条目，不详细讨论认知机制 |
| PHAP开发1990，后向 | 较长自评工具开发 | Background：保留谱系，由APHAB原始开发及手册覆盖正文 |
| Studebaker弧正弦变换，后向 | 正确率统计变换 | Background：与误差分析相关，本词条不展开变换 |
| Contour响度测试，后向 | 响度感知测量 | Background：不是完整获益框架，留给响度或验配词条 |
| Practical Hearing Aids Skills Test，后向 | 操作技能测量 | Important：提示操作影响使用；正文仅一般性说明，不增加未核验工具细节 |
| Advanced hearing aid technology 2014，后向 | 技术比较与言语结局 | Important：已有2025直接试验覆盖本段，不重复堆叠引用 |
| Studies of outcome measures / Issues in evaluating，后向 | 老年结局与测量问题 | Background：研究史入口，不用题名推断结论 |
| Development of materials for speech audiometry，后向 | 言语材料开发 | Background：材料方法由既有言语测听词条承接 |
| NHIS与流行率、年龄损失流行病学，后向 | 人群患病率 | Exclude：不能回答获益评价方法 |
| 耳鸣欧洲指南，前向 | 耳鸣诊断治疗 | Exclude：因引用种子而进入，非本词条中心 |
| 抑郁与认知、生活质量综述，前向 | 相邻健康结局与综述 | Background：远期结局以ACHIEVE原始试验为边界示例 |
| 真实世界SNR研究，前向 | 日常声学情境描述 | Important：提示环境代表性，由EMA方法论文直接承接 |
| Cochrane助听器、替代设备综述，前向 | 干预综合证据 | Background：用于发现谱系，不作为原创试验结论的替代 |
| 自验配验证2020，前向 | 特定自验配方法 | Important：由2023和2025试验提供直接比较，不重复增加 |
| 单侧损失使用率、筛查综述，前向 | 患病/使用与筛查 | Exclude：未直接研究本词条中心测量问题 |
| 成人康复与年龄损失指南，前向 | 广泛服务框架 | Background：由ASHA与NICE具体实践说明承接 |
| 2026自验配及设备效果荟萃分析，主题 | 多设备和服务随机试验综合 | Background：用于发现新谱系；异质性高，正文保留原始试验限定，不添加合并效应 |

停止扩展：前后向新结果多数重复方法或偏离中心；定义、临床框架、工具、统计、试验、EMA与近期核心结局各主线均已有对应来源。第二层预计重复，因此不继续无边界扩张。

## 实际阅读范围与论断核验

- ASHA成人实践门户：读取Verification、Validation、Aided Sound-Field Testing、Self-Reported Outcomes及康复相关段。已有asha-hearing-aids-adults保留documentation。
- Humes2017：PMC全文可访问，读取摘要、研究设计与结局说明；既有注册access为abstract，不擅改其他词条共享的历史核验记录。本次访问增量记录于此。
- De Sousa2023：PubMed完整摘要，明确同设备、远程支持、六周及分析样本；不宣称此次通读既有注册为fulltext的全文。
- Wu2025：PMC页面遇访问检查；通过出版者原文可检索摘要及Discussion/Limitations核对服务模式、技术等级及解释边界。正文不引用未核对的个体数值。
- Humes2025：SAGE全文，阅读Introduction、Evidence for the Dependence of Benefit on Baseline、Best-Supported MCIDs and MDDs。不把作者提出的基线分类直接变成全国或所有语言的操作标准。
- APHAB原始摘要、HARL官方PDF显示/计分部分、NAL与ICRA官方页面，分别支撑工具结构和用途。无全文问卷转载。
- Carney2007：出版社结构化摘要，未获得付费全文。教学二项SE和MDC是独立数学算例，不是其临界差异表。
- FUEL：PubMed原始摘要，理论解释，不据此给出某算法减少努力的疗效值。
- EMA2026：PubMed可检索摘要与书目；直接open偶发只返回页脚。保留abstract，不虚构全文结果。
- NICE：直接网页403，使用官方检索可见1.7节及官方PDF对应内容，记录访问限制。
- NASEM：章节访问检查阻挡，改引用实际读到的ASHA官方2025报告实施说明；原报告不伪装为阅读全文。
- ACHIEVE：本次通过原作者2023会议摘要核对整体与预定分组认知结果，2024原文可检索Results核对自评交流改善；保留站内既有两条文献，不把两项终点合并。

## 综合与局限

一致性：输出、行为、自评、参与和使用属于互补对象；差值需要明确基线、方向、时间与比较条件。分歧：不同服务试验结局未完全一致，不能脱离设备实现、支持、人群、工具和时间解释。近期发展：2025核心结局、2025基线相关判据、2026直接/间接EMA。空白：普通话适用版本、长期代表性采样、重要差异的跨人群推广与失访处理。

未纳入品牌排名、儿童成功标准、统一佩戴剂量、疾病预防承诺。AI草稿保持draft，无具名专业审阅记录。

## 原创图与核验

三图为原创合成数据：终点与百分点差值；独立二项SE及抽象SEM/MDC；组内变化与组间变化差。公开generate.py与validation.json，断言检验[10,30]百分点、[8,5.6569,4]百分点SE、MDC95约11.0874分、变化差15分、SRT获益3dB。字体下标缺字已经改成普通MDC95，重新生成无缺字警告；PNG逐张视觉检查通过。所有图不含患者数据或产品性能，也不是临床阈值。

## 发布前检查

内容与引用检查、20项工作流测试、类型检查和生产构建通过。全站验证覆盖371页、35243个内部链接和652个公式，断链为0。浏览器检查桌面及390×844手机视口；手机页面clientWidth与scrollWidth均为375，无整页横向溢出，未发现KaTeX错误。正文、公式与获益图显示正常。保留draft及待专业审阅标记。
