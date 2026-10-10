# 候选语义筛选

研究问题是听觉模型的解释目标、输入输出、任务读出与验证。等级依据实际研究对象和方法，非关键词或引文数量。缺少摘要的记录只能用作发现背景，不据其题名写结果。以下为第一层发现记录的逐项判断；定向核验来源再列于文末。

## 宽主题发现

| 候选 | 实际对象与关联 | 判断 |
| --- | --- | --- |
| Verhulst 等，2018，人类外周建模 | 连接外周、听神经和诱发电位，并操纵听损配置；直接支持模型层次和输出 | Core；采用 |
| Giguère/Woodland，1994，上行路径 | 电学类比外中耳、耳蜗及感觉细胞；代表早期生理路线 | Important；未纳入，当前原始来源已覆盖该路线 |
| Phonemic degradation in sensorineural hearing loss，2009 | 以计算听神经表示研究语音退化；特定会议应用不等于临床成功 | Important；未采用应用结果 |
| Giguère/Woodland，1994，下行路径 | 模拟反馈与传出联系；有助说明模型可能遗漏的控制 | Important；本条核心聚焦输入至预测，没有声称覆盖完整传出系统 |
| Sound localization with hearing protection devices，2017 | 模型用于防护设备定位预测，验证条件具体 | Important；特定应用暂不展开 |
| Dynamic computational auditory scene analysis ANN | 缺少可核验摘要与 DOI，不能判断具体结果 | Background；不据题名引用 |
| Spatial hearing models in three dimensions（芬兰语学位研究） | 空间听觉框架背景，非本轮核心原始模型来源 | Background；未采用结果 |
| Auditory models in music recognition tasks，2017 | 比较起音、音高与乐器分类计算任务，机器成绩与听者结果不同 | Important；当前任务网络来源提供更直接神经、行为约束 |

## 后向引文

| 候选 | 实际对象与关联 | 判断 |
| --- | --- | --- |
| Moore/Glasberg/Baer，1997，响度模型 | 稳态输入、激励与特定响度整合；摘要支持其建模目标 | Important；本条用现有响度入口，不展开另一整套模型 |
| Auditory Modeling Toolbox，2013 章节 | 早期工具框架，缺少摘要 | Background；优先采用 2022 原始 AMT 论文与当前文档 |
| Computational Models of the Auditory System，2010 图书 | 广泛框架，发现记录缺少章节摘要 | Background；不据书名推断具体模型表现 |
| Modeling auditory coding: from sound to spikes，2015 | 综述声音至放电模型和验证问题 | Important；定位后选择 Meddis、Zilany、Bruce 原始研究 |
| Peripheral tuning and speech ENV/TFS cues 章节 | 特定语音线索，记录缺少摘要 | Background；不引用具体效应 |
| Spectral processing: facts and models 章节 | 频谱背景，记录缺少摘要 | Background；由滤波器与原始模型来源承担 |
| Sound quality assessment using auditory models | 音质应用，缺少摘要 | Background；音质不与可懂度合并，新应用另行检索 |
| Auditory Processing Models 章节 | 广泛章节背景，记录缺少摘要 | Background；未采用特定结果 |

## 前向引文

| 候选 | 实际对象与关联 | 判断 |
| --- | --- | --- |
| AMT 1.x，2022 | 多模型、文档、演示和出版实验复现 | Core；采用 |
| Subcortical EEG predictors for continuous speech，2024 | 连续语音记录的回归变量选择与模型连接 | Important；提供后续神经追踪专题方向，不据局部摘要声称比较结论 |
| Human auditory ecology framework，2023 | 自然声环境与生态检验，关联推广问题 | Background；未作为模型性能证据 |
| ICNet，2025 | 麻醉沙鼠下丘多单元响应与非平稳性模型 | Core；采用，保留物种与记录边界 |
| Individualised hearing loss compensation neural framework，2023 | 可微模型辅助个体化处理优化 | Important；未将计算优化写成真实听者获益 |
| Speech categorization and temporal coherence，2021 | 时域一致性与语音组织模型 | Important；具体场景分析机制另有词条，未扩展结果 |
| Temporal information in healthy/synaptopathic auditory nerve，2022 | 对指定调制输入及纤维群体的模拟 | Important；不把特定参数设定写成损伤常模 |
| Intrinsic envelopes and modulation reverse correlation，2022 | 受控调制检测与反向相关，联系功能假设检验 | Important；本条验证逻辑已有直接例子，暂不加入另一整套实验 |

## 定向补充与最终来源分工

Core：Meddis、Zilany、Bruce、Verhulst 支持转导、响应与统计；Dau 支持调制功能，Durlach 与 Breebaart 支持双耳路线和失败条件；sEPSM、STOI、HASPI 支持不同言语指标；Kell 与 Saddler 支持任务训练；Norman-Haignere/McDermott 支持模型匹配刺激检验；CoNNear 支持机制近似。原始摘要访问与全文相关段访问据实区分，不推断未阅读的细节。

Important：Robles/Ruggero 生理综述与 Glasberg/Moore 滤波器研究支持前端目标；Hohmann、Dau 和 Verhulst 官方文档支持具体接口。Background：Jeffress 书目仅用于历史节点。近期 EEG 预印本直接相关，按 Important 纳入研究方向，明确未同行评审，不作为确证性能或临床证据。

纳入 25 项并不是质量排名。工具文档与综述服务框架，原始研究支持对应结果；同一研究的导航关联强度也不是科学证据权重。
