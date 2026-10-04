---
title: "听力测量校准"
english: "Audiometric calibration"
slug: "audiometric-calibration"
summary: "解释数字输出、声压级、听力级和参考等效阈声压级的转换。"
categories: ["audiology"]
tags: ["Audiometric calibration","组内文献"]
aliases: ["听力校准","RETSPL","参考等效阈声压级"]
batch: 2
status: "draft"
last_updated: "2026-10-04"
literature_checked_at: "2026-10-04"
authors: ["AI 辅助初稿"]
related: [{"slug":"pure-tone-audiometry","relation":"prerequisite"},{"slug":"zodiac-in-noise","relation":"related"}]
references: ["guo-audiometry-2021","zhou-anc-audiometry-2024","asha-audiometry-2005"]
order: 18
---

## 一句话理解

听力测量校准是把设备的数字或电输出，与规定测量条件下的实际声输出和参考听阈建立联系。没有这一步，屏幕显示的“听力级”可能只是一个未经验证的标签。

## 从数字量到声压

数字幅度、系统音量、耳机输出、耳道耦合和频率响应共同决定声音。相同文件在不同设备上播放，不能假定声压一致。声压级定义为：

$$
L_p=20\log_{10}\left(\frac{p_{\mathrm{rms}}}{p_0}\right),\qquad p_0=20\,\mu\mathrm{Pa}.
$$

空气声的参考声压 $p_0$ 如上，$L_p$ 单位为 dB SPL。若使用规定耳模拟器或耦合腔，并有匹配的参考等效阈声压级（RETSPL），可在相应条件下理解 $L_{\mathrm{HL}}=L_p-\mathrm{RETSPL}(f)$。换能器、频率和耦合条件不同，参考值也不同；这不是任意消费耳机可直接套用的转换表。

## 声学校准与行为校准

声学校准用规定测量系统检查输出；行为校准通过合适参考人群或参照测量建立听阈关系。二者回答的问题不同。耳机的最大输出、输出线性、重复佩戴及左右差异都需要考虑。

ASHA 指南强调设备与换能器匹配及校准记录。其年代与引用的标准版本应明确，不能把历史指南中的版本号当作当前全部要求。[ASHA，2005](#ref-asha-audiometry-2005)

## 共同论文为什么先研究校准

真无线耳机自动测听研究同时处理设备输出与参考听阈关系，随后再比较测听结果。[Guo 等，2021](#ref-guo-audiometry-2021) ANC 耳机研究还检查主动降噪开启后的声学特性和佩戴相关问题。[Zhou 等，在线发表于 2024](#ref-zhou-anc-audiometry-2024)

ANC 改变噪声条件，不会自动建立正确的 dB HL 零点。固件、音量路径或处理模式变化后，也不能假设先前校准仍适用。

## 记录与后续更新

保留设备型号、换能器、测量系统、模式、音量、频率和校准日期。后续补充耳模拟器、环境噪声与校准不确定度，具体转换参数必须对应经验证的系统。
