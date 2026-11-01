# 文献检索与筛选范围
日期：2026-11-02；目标是给听觉研究者建立可用的机器学习基础课程，不是系统综述、临床指南或2026年算法排行榜。

## 范围与准入
纳入直接支持定义、数学条件、验证流程的作者教材及官方方法文档，以及语音表征、神经预测和泄漏的代表性原始论文。理论不限发表年；补充方法发展以2024-01-01至2026-11-02为近期窗口。未声称穷尽2026年新发表成果。排除产品营销、博客二手推断、与基础教学关系弱的领域性能排名。

## 检索和网络扩展
使用deep-research技能的openalex_research.py，以“Leakage and the reproducibility crisis in machine-learning-based science”检索，得到2023 Patterns正式论文W4385576721。先前显式sort=relevance不被API支持，随后移除该参数成功；失败请求未当成证据。
对该种子取12条后向参考与8条前向引用，DOI优先去重。记录位于本地artifacts/machine-learning/sources/openalex-{seeds,backward,forward}.json；不是穷尽所有引用。judge_relevance.py用于生成同一问题的语义筛选提示，实际判断由本文作者完成，不冒充独立评阅者。
同时以D2L作者教材、scikit-learn官方指南及wav2vec/HuBERT原始摘要作定向检索。网页内容哈希与访问结果见source-index.json；缓存HTML不公开发布。

## 有代表性的筛选判断
| 候选 | 实际研究/性质与证据依据 | 分级与取舍 |
| --- | --- | --- |
| Kapoor与Narayanan 2023 | 摘要：跨领域泄漏调查、分类及民间冲突预测复核。 | Core，支持验证设计警示；不把个别任务结果推广为所有复杂模型无优势。 |
| 2024 Data leakage inflates prediction performance in connectome-based machine learning models，10.1038/s41467-024-46150-w | OpenAlex原始摘要：特征选择、协变量校正与个体独立性泄漏对连接组预测的影响；有的泄漏只小幅影响甚至降低成绩。 | Important，帮助避免“任何泄漏必定提高分数”的错误表述；未取得论文正文相关方法，不把其具体数量或实验作为本词条证据。 |
| 2024 Avoiding common machine learning pitfalls，10.1016/j.patter.2024.101046 | 摘要：建模前、建模、评价、比较、报告的教程。 | Background，选择原则与官方指南重复，不为增加数量重复引用。 |
| 2015 Reproducible research can still be wrong | 摘要：可重算不等于正确，强调预防和教育。 | Background；审校保留该认识，不把它当具体算法证据。 |
| Applied Predictive Modeling 2013 | 书目为预测方法教材。 | Background；与现用作者开放教材覆盖重复，未据未读章节引用。 |
| 2013 When Optimism Hurts | 书目指向精神影像预测乐观偏差，OpenAlex缺摘要。 | Important候选但证据不足，未据题名写结论。 |
| 2024/2025病理基础模型、药物发现及医疗共识 | 主题涉及专门疾病/产品场景，和本篇核心数学课程较远。 | Exclude；不因引用数高而纳入，不作医疗推荐。 |
| 2017 Transformer、2020 wav2vec 2.0、2021 HuBERT | 原始作者/正式发表摘要支持架构来源或训练目标。 | Important，选择能说明不同目标的历史代表，不报当前最好。 |
| Kell等2018 | 原始摘要：听觉任务网络与人类行为/fMRI比较。 | Important，连接听觉应用，网络不等于解剖机制。 |

## 来源与访问限制
D2L读取相关正文部分，登记为fulltext；scikit-learn为documentation。原始论文的本轮实际支持范围为abstract，不把可以下载全文误称为已阅读全文。
PubMed的Kapoor页面在本地urllib返回cookie挑战，source-index已标明；通过网页工具读取其正式摘要、图注与DOI。IEEE DOI落地页有机器人检查，未绕过；HuBERT正式书目由Crossref登记元数据核实，方法论断依据作者arXiv摘要。wav2vec会议页与旧arXiv作者姓名显示存在差异，引用按当前正式会议页。
推导、图示和合成数据为本站原创，不复制论文原图，也不将代码运行称作原始论文结果复现。

## 综合与仍待研究的问题
稳定主线是目标函数、模型偏好、数据可用性和评价协议必须共同定义；单一高分不足以证明机制或部署获益。实际听觉应用仍需回答目标人群与场景覆盖、预训练数据重叠、表示读出容量以及真实听者获益等问题。不同泄漏机制的影响大小并不一致，因此本篇用“可能夸大”和任务匹配表述，不作无条件大小或方向保证。
