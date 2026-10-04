---
title: "听力测量校准"
english: "Audiometric calibration"
slug: "audiometric-calibration"
summary: "解释数字输出、声压级、听力级和参考等效阈声压级的转换。"
categories: ["audiology","acoustics"]
tags: ["Audiometric calibration"]
aliases: ["听力校准","RETSPL","参考等效阈声压级"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
references: ["guo-audiometry-2021","zhou-anc-audiometry-2024","asha-audiometry-2005","iso-389-1-2017"]
order: 18
knowledge_area: "measurement"
kind: "calibration"
key_facts: [{"label":"目的","value":"建立设备输出与参考标度的关系"},{"label":"关键对象","value":"信号链、换能器、耦合与参考零点"},{"label":"质量量","value":"偏差、重复性与不确定度"}]
---

**听力测量校准**（audiometric calibration）是建立测听设备输出与规定参考量之间对应关系的过程。它涵盖电声输出、换能器、耦合条件与标度，并需考虑重复性和不确定度。主动降噪、环境控制和校准承担不同任务。[4](#ref-iso-389-1-2017 "Acoustics — Reference zero for the calibration of audiometric equipment — Part 1: Reference equivalent threshold sound pressure levels for pure tones and supra-aural earphones")

## 定义与分类

本方法为[纯音测听](../pure-tone-audiometry/)建立输出与参考标度的对应，也与远程听力测试的质量控制有关。

校准是输出与参考的对应，验证是检验方法在目标条件下的表现，质量控制是持续发现偏差。三者需要联系却不能等同。标准耦合器声压、真实耳道声压和听力级具有不同参考条件；任意耳机不能直接套用另一换能器的参考零点。

## 原理与表征

### 从数字量到声压

数字幅度、系统音量、耳机输出、耳道耦合和频率响应共同决定声音。相同文件在不同设备上播放，不能假定声压一致。声压级定义为：

$$
L_p=20\log_{10}\left(\frac{p_{\mathrm{rms}}}{p_0}\right),\qquad p_0=20\,\mu\mathrm{Pa}.
$$

空气声的参考声压 $p_0$ 如上，$L_p$ 单位为 dB SPL。若使用规定耳模拟器或耦合腔，并有匹配的参考等效阈声压级（RETSPL），可在相应条件下理解 $L_{\mathrm{HL}}=L_p-\mathrm{RETSPL}(f)$。换能器、频率和耦合条件不同，参考值也不同；这不是任意消费耳机可直接套用的转换表。

### 声学校准与行为校准

声学校准用规定测量系统检查输出；行为校准通过合适参考人群或参照测量建立听阈关系。二者回答的问题不同。耳机的最大输出、输出线性、重复佩戴及左右差异都需要考虑。

ASHA 指南强调设备与换能器匹配及校准记录。其年代与引用的标准版本应明确，不能把历史指南中的版本号当作当前全部要求。[3](#ref-asha-audiometry-2005 "Guidelines for Manual Pure-Tone Threshold Audiometry")

### 相关研究为什么先研究校准

真无线耳机自动测听研究同时处理设备输出与参考听阈关系，随后再比较测听结果。[1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry") ANC 耳机研究还检查主动降噪开启后的声学特性和佩戴相关问题。[2](#ref-zhou-anc-audiometry-2024 "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control")

ANC 改变噪声条件，不会自动建立正确的 dB HL 零点。固件、音量路径或处理模式变化后，也不能假设先前校准仍适用。

### 校准链条与参考条件

校准需要明确被测量：数字输出幅度、电压、耦合器声压，还是佩戴时的声压。电压相同并不保证耳机声压相同；标准耦合器中的声压也不等于所有真实耳道中的声压。完整记录应连接信号、放大输出、换能器、耦合方式及参考标度。

若把幅度设置 $a$ 变为 $ga$，在线性工作区间内声级变化为 $20\log_{10}|g|$。超出线性范围后，限幅、压缩或设备增益控制可能使这个关系失效。校准不仅要测一个声级，还应检查目标输出区间及各频率。

### 参考零点不可跨设备套用

ISO 389-1 的对象为特定条件下压耳式耳机的参考等效阈声压级，不能直接当作任意插入式、包耳式或 TWS 耳机的通用换算表。标准换能器类型、耦合器和频率应匹配。[4](#ref-iso-389-1-2017 "Acoustics — Reference zero for the calibration of audiometric equipment — Part 1: Reference equivalent threshold sound pressure levels for pure tones and supra-aural earphones")

若新设备没有可直接适用的参考数据，研究中可能需要电声测量及行为参考建立；两者回答不同问题。行为校准还取决于参考听者、样本及测量流程。具体数值应来自对应系统的验证，不能用本文的示意公式代替。

### 主动降噪为何不能替代校准

ANC 改变外部噪声进入耳道的方式，也可能随佩戴、噪声频谱和工作模式改变传递特性。较安静的主观体验不证明测试音的实际声级正确。涉及 ANC 耳机的研究采用了对应设备和多层校准过程，其结果不能自动扩展到其他耳机或固件。[2](#ref-zhou-anc-audiometry-2024 "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control")

### 不确定性来自哪里

| 来源 | 可能后果 | 记录方式 |
| --- | --- | --- |
| 仪器与参考校准 | 共同声级偏差 | 仪器、日期、参考与溯源 |
| 耳机佩戴与密封 | 频率相关变化 | 重复佩戴及耦合状态 |
| 环境噪声 | 尤其影响较弱测试音 | 频谱和测试环境 |
| 自动处理与限幅 | 输出随条件变化 | 工作模式、输入范围与版本 |

互相独立的小误差有时可用平方和开根号合成标准不确定度；共同或相关误差不能简单按独立项处理。随机重测一致并不能排除系统性偏差。

### 验证比一个校准常数更完整

宜比较多频率和多个输出水平，检查失真和重复性，并与参考测听系统进行配对验证。相关系数高只说明共同变化，不保证绝对一致；应同时检查差值、频率趋势及可接受范围。TWS 测听论文的证据属于所验证系统，应保留设备与流程边界。[1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry")

## 分析示例

### 解释示例：一致性不等于准确性

一套便携系统连续测量很稳定，但所有频率的输出声级都有共同偏移，它具有较好重复性却存在系统误差。与参考系统比较时，相关系数可能仍很高，差值图却会显示偏移。准确性、重复性和相关性必须分别报告。

更换耳机、固件或 ANC 模式后，应判断原校准关系是否仍有效；同一产品名称不保证输出链条完全相同。研究记录中的设备版本和模式，是证据可迁移性的条件。[2](#ref-zhou-anc-audiometry-2024 "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control")

值得检验的问题包括重新佩戴对低频输出的影响，以及自动音量或限幅在不同输入水平的行为。将这些变化纳入不确定度分析，通常比给一个过多小数位的校准常数更有意义。

## 研究沿革

测听参考零点和气骨导方法由相应标准规定范围。便携设备研究进一步检验具体耳机与信号链；2024 年 ANC 耳机研究把工作模式与多层校准相联系。设备与版本是证据迁移的条件，不能把一个系统的验证当作全部同类耳机有效。[4](#ref-iso-389-1-2017 "Acoustics — Reference zero for the calibration of audiometric equipment — Part 1: Reference equivalent threshold sound pressure levels for pure tones and supra-aural earphones") [1](#ref-guo-audiometry-2021 "Utilizing True Wireless Stereo Earbuds in Automated Pure-Tone Audiometry") [2](#ref-zhou-anc-audiometry-2024 "Automated pure-tone audiometry using true wireless stereo earbuds with active noise control")
