---
title: "听觉注意"
english: "Auditory attention"
slug: "auditory-attention"
summary: "对声音目标进行选择、维持和转换的功能，连接目标任务、竞争声源与资源分配。"
categories: ["neuroscience","speech","psychoacoustics"]
tags: ["auditory-attention"]
aliases: ["选择性听觉注意","selective auditory attention","auditory attention decoding","AAD","听觉注意解码"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["mesgarani-attention-2012","osullivan-aad-2015","fuel-2016","mo-ci-adaptation-2026"]
batch: 3
order: 37
literature_checked_at: "2026-10-04"
knowledge_area: "perception"
kind: "function"
key_facts: [{"label":"功能维度","value":"选择、维持与转换"},{"label":"实验对象","value":"目标声与竞争声"},{"label":"关键区分","value":"注意选择不等于可听性或理解"}]
---

**听觉注意**（auditory attention）是根据任务、目标和声音环境，对某些听觉信息进行选择、维持或转换处理的功能。人在多个声源中关注一位说话者时，既需要可用的声学线索，也需要组织声源并维持目标。注意并非让其他声音完全不进入神经系统，也不等于耳朵只接收目标声音。[1](#ref-mesgarani-attention-2012 "Selective cortical representation of attended speaker in multi-talker speech perception")[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 定义与分类

### 目标驱动与刺激驱动

目标驱动注意涉及主动遵循任务，如始终关注左侧说话者；刺激驱动变化可由突然出现的声音或其他显著事件引起。二者可以共同发生，实验需要区分指令、声音显著性和实际行为。不能把突然转头这一动作单独当作持续注意的完整指标。

### 选择、维持与切换

选择回答关注哪个对象，维持回答能否保持关注，切换回答目标改变时如何重新分配。某一任务中准确选择目标并不必然意味着长时维持或快速切换同样良好。连续语音任务、短声检测任务和双任务的结果因此不能直接等同。

### 注意与理解

目标更被关注，不等于它一定被正确理解；声音仍可能不清楚或语言不熟悉。反过来，听者也可能处理部分非目标信息。评价[语音可懂度](../speech-intelligibility/)时要另有正确率、阈值或理解测量，不能用神经选择性代替理解成绩。

## 机制与表征

声源的方位、音色、周期性、时序和语言背景共同影响目标组织。[空间听觉](../spatial-hearing/)可以帮助区分声源，但声源可被分开并不保证注意始终停留在目标。信号竞争、目标切换和任务要求也可能改变分配。

Mesgarani 与 Chang 的人类皮层表面记录显示，多说话者条件下的响应可以对被关注说话者具有选择性。这提供了神经层面的证据，但研究使用的 ECoG 不等同于头皮[脑电图](../electroencephalography/)。头皮 EEG 研究则常通过目标与非目标语音包络重建或跟踪比较来检验注意选择。[1](#ref-mesgarani-attention-2012 "Selective cortical representation of attended speaker in multi-talker speech perception")[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

这些指标描述神经信号与刺激或标签之间的统计关系。较高目标相关性不能唯一指出认知资源总量，也不能排除声学差异、眼动或输入可听性的影响。[聆听努力](../listening-effort/)关注有目的的资源投入，和注意选择相关，但不是同一个指标。[3](#ref-fuel-2016 "Hearing Impairment and Cognitive Energy: The Framework for Understanding Effortful Listening (FUEL)")

## 测量方法

行为任务可要求复述目标、检测目标事件或回答理解问题，并记录干扰条件下的成绩。任务应让目标和竞争声的声级、身份与方位有适当控制，必要时在不同条件中交换角色。若目标总是更响或总是同一位说话者，神经模型可能利用声学身份而非注意。

听觉注意解码常比较[语音神经跟踪](../neural-speech-tracking/)或重建声音与候选说话者特征的关系。训练和测试必须独立，验证单位还要与应用目标一致：对同一人的新试次推广，与对新人的推广，是不同问题。窗口长度、类别平衡和切换延迟都影响实际用途。[2](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 应用与局限

听觉注意研究有助于理解多说话者交流，并为听觉设备控制提供探索方向。实验室解码成功不自动意味着装置已可在真实环境稳定识别目标；运动、移动声源、混响和设备伪迹可能改变输入。用于控制[助听器](../hearing-aid/)或[人工耳蜗](../cochlear-implant/)时，还应评估识别延迟与错误切换的交流代价。

注意表现可能受睡眠、疲劳、任务熟悉和动机影响。一次任务分数不能无条件用作一般注意能力或神经疾病的判断。科学报告应把测试条件、行为成绩和神经指标分开表述。

## 分析示例

如果听者在固定的两个声音中执行“关注左侧”任务，模型正确判断目标后，应再交换方位和说话者身份测试。若性能只在固定身份条件下好，可能反映声学偏好而不是可靠注意解码。还可增加行为问题，检查听者是否遵循指令；神经模型与行为一致提供互补证据，彼此不能自动替代。

若困难条件中目标跟踪下降，同时复述成绩下降，应检查目标可听性、注意指令及模型噪声，不能直接认定听者减少了努力。困难增加时，投入可能上升，也可能因任务过难而放弃。

## 研究沿革与近期进展

从行为选择到皮层记录和单试次 EEG 解码，研究逐渐进入连续语音场景。Mo 等 2026 年 9 月研究纵向追踪 19 名新植入成人，在竞争声任务中观察目标语音跟踪比非目标更强且更早出现，并发现与行为适应相关。这是特定群体和任务中的纵向证据，不能把组平均变化理解为每个人统一的注意恢复期限。[4](#ref-mo-ci-adaptation-2026 "Longitudinal adaptations in neural and behavioral systems following hearing restoration using cochlear implants")
