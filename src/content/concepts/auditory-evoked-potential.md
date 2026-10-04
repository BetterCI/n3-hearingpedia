---
title: "听觉诱发电位"
english: "Auditory evoked potential"
slug: "auditory-evoked-potential"
summary: "听觉刺激相关电位变化的统称，涵盖多个潜伏期和任务条件下的神经生理响应。"
categories: ["neuroscience","audiology"]
tags: ["auditory-evoked-potential"]
aliases: ["AEP","AEPs","听觉事件相关电位","auditory ERP"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["picton-aep-1974","itoh-aep-2026","osullivan-aad-2015","lalor-speech-2010"]
batch: 3
order: 35
literature_checked_at: "2026-10-04"
knowledge_area: "measurement"
kind: "physiological-response"
key_facts: [{"label":"测量对象","value":"刺激相关电位变化"},{"label":"主要分类","value":"早期、中潜伏期与较晚响应"},{"label":"关键条件","value":"刺激、任务、参考电极和分析规则"}]
---

**听觉诱发电位**（auditory evoked potential，AEP）是听觉刺激相关电位变化的统称，包含早期到较晚时程、不同来源和任务敏感性的响应。[听觉脑干反应](../auditory-brainstem-response/)是其中一类。记录通常使用[脑电图](../electroencephalography/)技术，但“记录方法”“神经响应”和“分析得到的成分”属于不同层次。[1](#ref-picton-aep-1974 "Human auditory evoked potentials. I. Evaluation of components")

## 定义与分类

### 按潜伏期分类

常见分类区分早期脑干、中潜伏期和较晚皮层响应。不同论文使用的边界可能略有差别，刺激与受试者情况还会改变具体峰值时刻。分类方便组织观察，但潜伏期不是唯一定位依据：一个时刻的头皮电位可能来自多个叠加源，不能仅凭峰出现得早晚精确定位结构。[1](#ref-picton-aep-1974 "Human auditory evoked potentials. I. Evaluation of components")

### 成分与事件相关电位

皮层响应常用 P、N 及序号或潜伏期命名，例如某些条件下的 P1、N1、P2。字母指在指定参考和绘图惯例下的极性，数字并非固定的神经核团。事件相关电位 ERP 是更广的概念，既可由听觉事件引起，也可与其他感官、反应或认知事件有关；并非所有 ERP 都是听觉诱发电位。

### 离散与连续刺激

短声或音节的离散呈现有助于按刺激起点平均；连续语音的响应相互重叠，可用[语音神经跟踪](../neural-speech-tracking/)和响应函数建模。后者并不是把每个语音包络峰都当成一条独立 ERP；分析需要说明声音特征、时间延迟、模型和验证方式。[4](#ref-lalor-speech-2010 "Neural responses to uninterrupted natural speech can be extracted with precise temporal resolution")

## 原理与表征

表面电极记录多个神经源通过体积传导形成的电位差。刺激锁时平均可以强调在重复事件间较一致的活动，非锁时背景则可能减弱。这是有条件的估计，并不说明平均曲线包含某一次试次的全部神经过程，也不说明没有平均峰就没有听觉处理。

成分幅度、潜伏期、分布及条件差异都可作为描述。一个较大 N1 并不自动代表听得更好；刺激频率、强度、重复间隔、适应、任务和注意都可能改变它。参考电极改变还可能改变局部波形极性和幅度，比较时必须把参考方式写清。[1](#ref-picton-aep-1974 "Human auditory evoked potentials. I. Evaluation of components")[2](#ref-itoh-aep-2026 "Frequency, intensity, and reference dependence of scalp-recorded auditory evoked potentials in the common marmoset")

头皮分布与源定位也不等同。有限数量电极与多个可能源之间形成逆问题；不同头模型、约束和噪声条件可能给出不同解。若论文只展示头皮响应，百科不能把它改写为已经直接测量了某一个特定皮层区。

## 测量与分析方法

典型过程包括记录电极与参考、设置刺激、同步事件时间、分段、处理伪迹、基线与统计分析。每一步都应按研究目标说明。滤波可能改变峰形和时序；不恰当的基线或条件间试次数差异也可能影响比较。剔除规则、保留试次数和重复性比一张光滑曲线更能帮助判断证据。

预先定义时间窗和电极区域可以减少观察结果后挑选的偏差。探索性多电极、多时间点比较应采用相应统计控制并明确性质。若目标是个体预测，则还需要在独立资料中验证，群体平均显著差异并不等于可靠的个体分类器。

## 应用与边界

AEP 用于研究感官输入、时域编码、任务与适应，也可支持特定听力评估。不同成分回答不同问题；早期反应的存在不能证明句子理解或日常交流正常，较晚响应变化也未必唯一反映认知改善。[听觉注意](../auditory-attention/)相关实验还需要控制目标难度和行为表现。[3](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

真实人工耳蜗记录还受到电刺激伪迹影响。伪迹处理需要独立检查；与声音时间相关的电信号可能包含设备成分，不能仅以其锁时性证明神经来源。

## 分析示例

研究比较两种声级时，发现 P2 幅度增加，应先确认参考、试次数、听觉可听性和刺激重复率是否一致。结论可以是“该记录条件下 P2 对输入水平敏感”，而不是“注意能力增强”。若同时改变频率，声级效果与频率效果可能交互，需要分别设计或建模。

## 研究沿革与近期进展

经典人类研究建立了多个潜伏期成分的系统描述，连续语音建模随后扩展了生态任务。2026 年 9 月 Itoh 等在两只清醒普通狨猴中考察频率、强度与参考依赖性，摘要显示这些条件可改变头皮 P1、N1、P2 的表现，参考还影响极性。它为跨物种和跨记录比较提供方法提醒，但不能用两只动物的波形建立人类诊断常模。[1](#ref-picton-aep-1974 "Human auditory evoked potentials. I. Evaluation of components")[2](#ref-itoh-aep-2026 "Frequency, intensity, and reference dependence of scalp-recorded auditory evoked potentials in the common marmoset")
