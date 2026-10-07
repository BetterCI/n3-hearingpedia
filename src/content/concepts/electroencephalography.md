---
title: "脑电图"
english: "Electroencephalography"
slug: "electroencephalography"
summary: "记录电极间脑活动相关电位差的方法；听觉研究用其观察诱发电位、振荡与连续语音响应。"
categories: ["neuroscience","research-methods"]
tags: ["electroencephalography"]
aliases: ["EEG","electroencephalogram","脑电记录","头皮脑电"]
status: draft
last_updated: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["osullivan-aad-2015","picton-aep-1974","mo-ci-adaptation-2026","guo-tracking-2026"]
batch: 3
order: 36
literature_checked_at: "2026-10-04"
knowledge_area: "methods"
kind: "test"
key_facts: [{"label":"实际记录","value":"电极相对参考的电位差"},{"label":"常见量纲","value":"电压，如 μV"},{"label":"验证重点","value":"同步、伪迹、参考与独立验证"}]
---

**脑电图**（electroencephalography，EEG）是通过电极记录脑活动相关电位差的方法，也常指得到的记录。听觉研究通常使用头皮电极，观察[听觉诱发电位](../auditory-evoked-potential/)、背景节律及与连续声音相关的活动。EEG 的时间分辨能力适合研究声音加工的时间过程，但一个电极的信号不是其正下方某一区域的直接读数。[2](#ref-picton-aep-1974 "Human auditory evoked potentials. I. Evaluation of components")[1](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 定义与记录形式

### 电位差与参考

每个通道记录相对于指定参考的电位差，幅度通常以微伏描述。更改参考会改变波形和头皮分布，因此“电极 A 的幅度”必须连同参考说明。平均参考等处理也具有电极覆盖和噪声方面的前提，并非没有参考的绝对脑电。

### 与其他记录技术的区别

磁脑图 MEG 记录磁场，皮层脑电 ECoG 使用皮层表面电极，二者的物理量、空间采样和可用场景不同。相关研究可以相互提供方法线索，但 ECoG 上的高频选择性结果不能直接写成普通头皮 EEG 已具有相同表现。

### 诱发活动与持续活动

对重复听觉事件分段平均可估计锁时响应；持续记录可以分析频率活动、连接性或[言语神经跟踪](../neural-speech-tracking/)。不同处理强调不同特征，不能用一条平均 ERP 代表整段脑电，也不能从某个频段能量独立推断唯一心理状态。

## 测量原理与数据结构

头皮 EEG 由多个神经源及体积传导共同形成。记录通常可以表示为通道乘时间的矩阵，还应保存采样率、事件、参考、单位及坏通道信息。较高采样率提供较细的时间采样，但系统延迟和时间同步错误仍可能限制听觉时间分析。

听觉任务特别需要校验声音从指令到实际输出的延迟。声卡缓冲、无线传输和触发通路可能引入固定偏移或时变抖动。若以软件播放时刻代替声音实际到耳时间，估计出的响应潜伏期可能混入设备延迟。

线性分段平均的教学表达为：

$$
\bar{x}(t)=\frac{1}{K}\sum_{k=1}^{K}x_k(t)
$$

$x_k$ 是第 $k$ 个对齐试次的电位记录，$K$ 是保留试次数。平均能够降低某些非锁时噪声，但眼动、肌电或设备信号若与任务时间一致，仍可能保留。不能仅因曲线平滑就确认神经来源。

## 处理与质量控制

滤波、重参考、坏通道处理、伪迹识别和分段应与目标频段和响应时程一致。方法报告需要注明滤波器、边界处理、数据剔除与保留量，检查结论对合理分析选择是否稳定。自动去伪迹输出仍需要检查，尤其是[人工耳蜗](../cochlear-implant/)电刺激信号可能与刺激特征相关时。

训练预测模型应按听者、试次或记录时段安排真正独立的验证，具体单位取决于推广目标。同一段声音的相邻窗口高度相关，随机分窗可能泄漏信息。标准化和特征选择也应只在训练部分拟合，否则测试资料影响了模型选择。[1](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")

## 听觉应用与局限

EEG 可研究[听觉注意](../auditory-attention/)、声音响应与[听觉可塑性](../auditory-plasticity/)，但“脑活动可测”不等于单次记录能够准确评估个体理解。参与者运动、视觉任务、疲劳和试次长度都可能影响结果，行为成绩和主观报告应按研究目标共同记录。

组间显著差异、个体间相关和个体预测能力是不同证据。2026 年三个公开 MEG/EEG 数据集的基准研究指出，语音跟踪区分群体条件或注意目标的效果，不能无条件转成稳定的个体噪声语音阈值预测。[4](#ref-guo-tracking-2026 "Boundary conditions for cortical speech tracking as an objective speech-in-noise marker: a three-dataset MEG/EEG benchmark")

## 分析示例

若模型利用 EEG 判断听者关注哪位说话者，应让独立的整段试次进入测试，并比较标签打乱或不含 EEG 的基线。需要确认分类依赖神经特征，而非固定说话者顺序、眼动或设备伪迹。准确率还应连同窗口长度和类别分布报告，60 秒窗口的离线表现不能直接代表短时实时控制。

## 研究沿革与近期进展

早期听觉脑电研究以重复刺激及诱发响应为主，连续语音分析随后增加了自然场景的可能性。Mo 等于 2026 年 9 月在线发表的研究在 19 名新植入成人中纵向记录连续语音选择性注意任务 EEG，观察到目标语音跟踪和头皮分布随时间变化，并与行为结果相关。它支持 EEG 作为适应研究的工具，但不证明某个 EEG 数值可单独决定个人康复进程。[1](#ref-osullivan-aad-2015 "Attentional Selection in a Cocktail Party Environment Can Be Decoded from Single-Trial EEG")[3](#ref-mo-ci-adaptation-2026 "Longitudinal adaptations in neural and behavioral systems following hearing restoration using cochlear implants")
