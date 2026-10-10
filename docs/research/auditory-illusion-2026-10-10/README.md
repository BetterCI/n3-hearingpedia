# 听觉幻觉：本地深度稿研究记录

核验日期：2026-10-10。讨论 auditory illusion，即听觉错觉；不将临床幻听、耳鸣或音乐想象作为同一现象。按百科写作规范形成本地待审阅稿，未提交或推送。

## 检索与证据范围

围绕连续性、音素恢复、循环音高、双耳音乐错觉、语音变歌、视听语音和多稳定知觉检索。以 Riecke 等 2007 年连续性研究（OpenAlex W2097874091）展开第一层前向、后向引文。`search.json`、`backward.json`、`forward.json` 各保存八项发现，`seed.json` 保存种子，`relevance-prompt.txt` 保存筛选任务。

近期定向检索覆盖 2021-01-01 至 2026-10-10；选入 Chen 等 2025 年语音变歌研究与 Le 等 2025 年鸟类神经恢复研究。没有据此宣称已穷尽全部研究，也没有将 2025 年结果写成 2026 年新论文。

最终采用 18 篇原始论文和 5 项作者说明资料。`verified-metadata.json` 保存 Crossref/Europe PMC 书目，`abstracts-read.jsonl` 保存实际读取的摘要及证据范围，`selected-sources.json` 对应正文引用。另通过原出版方、PubMed、PMC 或作者页面核对可访问资料。无摘要记录只作为发现线索，未据题名推断结果；相关全文段落与摘要访问分别标注。Leonard 等采用保守的摘要访问等级，备注说明另外读取的检索可见原文范围。

## 筛选与停止依据

筛选详见 `relevance-screening.md`。第一层引文已明显延伸至一般皮层映射、语音分析与非听觉研究；进一步扩大不能直接回答本条代表错觉的输入、报告与对照。已有经典发现、机制争议、否定任务替代的证据、真实植入者比较及近期研究，足以支撑百科草稿，因此在本轮停止扩展。此停止依据不构成系统综述或全面文献覆盖声明。

## 原创媒体与复现

四幅说明图与七段 WAV 为本站原创刺激说明、功能框图和合成教学材料，无论文图片或作者录音转载。生成脚本为 `scripts/generate-auditory-illusion.py`；独立导出检查为 `scripts/verify-auditory-illusion.py`。参数和数值结果见 `figure-audio-verification.json` 与 `wav-verification.json`。没有受试者数据，没有保证诱发错觉的声明；数字幅度不作为耳旁校准声压。

正文统计与引用、链接、公式检查见 `draft-verification.json`；页面与构建核验见 `qa-report.md`。
