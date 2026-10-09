# 《听觉皮层》本地交稿说明

- 词条：听觉皮层 / Auditory cortex；深度词条。
- 日期：2026-10-09。
- 署名：AI 辅助编写。AI用于文献发现与核读整理、提纲、正文、教学计算、配图代码和工程接入；尚无具名专业审阅。
- 正文：`src/content/concepts/auditory-cortex.md`。
- 范围：人类区域与表征为主，动物证据解释局部回路；与《听觉通路》形成从多层级网络到皮层机制的衔接。
- 当前 9,060 个正文区汉字，10 个一级章节、31 个二级章节、23 项参考来源（含一项图源）、五张原创图及一张转载解剖示意图。
- 发布状态：用户于2026-10-09确认提交并推送，保留Draft专业审阅状态。

## 来源材料

逐项来源见 `selected-evidence.json`，检索、证据分层、访问限制及引用版本见 `research-notes.md`。所有正式来源已登记 DOI 或稳定链接。全文与摘要范围分别标记；未把访问失败、书目元数据或 AI 文字当作研究结论来源。

## 图片与复现

| 正文图号 | 文件 | 性质及解释任务 | 原理依据 |
| --- | --- | --- | --- |
| 1 | `brain-motor-sensory-blausen.png` | 大脑皮层功能分区及听觉位置；保留英文原图及中文对照 | Blausen Medical 2014；CC BY 3.0；Moerel 2014限定定位范围 |
| 2 | `01-regions-and-connections.svg` | 区域连接框架；框不编码面积或解剖距离 | Moerel 2014；Dick 2012 |
| 3 | `03-context-and-windows.svg` | 共享片段和窗口几何；不生成神经响应 | 时间整合研究 2022、2025 |
| 4 | `04-adaptation-and-controls.svg` | 事件序列角色；不代表完整概率设计 | Parras 2017 |
| 5 | `05-evidence-and-intervention.svg` | 记录、解码及干预的证据区别 | Hamilton 2021；Lee 2024 |
| 6 | `02-strf-teaching-example.svg` | 原创离散计算；预测为12和7 spikes/s | STRF方法和Mesgarani 2014 |

图片路径为 `public/figures/auditory-cortex/`。五张原创图各附同名PNG预览，生成代码为 `scripts/generate-auditory-cortex.py`；设定、尺寸及核验见 `figure-verification.json`。新增图1为 Blausen Medical 原图（1600×1493），原始标识 Blausen 0102，原图未修改；作者、来源URL、CC BY 3.0许可、尺寸及SHA-256见 `image-sources.json`，图注附完整署名、许可链接、中文对照及定位边界。

## 接入与检查

已接入主题参考表、知识关系、证据映射和结构机制学习路径，链接均指向已有词条。未改其他词条正文。

- [x] 自足导言、章节范围和术语定义。
- [x] 23 项引文编号与来源 ID对应。
- [x] 教学矩阵、窗口几何、变量及单位核对。
- [x] 五张原创PNG预览及新增转载PNG检查，图源与许可记录齐全。
- [x] 状态及署名真实；无具名审阅记录。
- [x] `pnpm check`：81个文件，0错误、0警告、0提示。
- [x] `pnpm build` 与 `pnpm verify`：164个页面，65个可搜索词条，0断链。
- [x] 桌面1440像素与手机390像素预览：正文无水平溢出，六张图均加载，23项参考和引文锚点有效，公式无渲染错误。
- [x] `git diff --check`：通过；本次获用户明确授权提交及推送。

本地预览：<http://127.0.0.1:4338/n3-hearingpedia/concepts/auditory-cortex/>。页面检查摘要同步记录于 `draft-verification.json`，完整浏览器记录保存在本地 `artifacts/cortex-research/local-qa.json`。

## 发布授权与专业审阅

用户可重点审阅：区域组织的解释尺度、因果证据的篇幅、教学算例的难度，以及与《听觉通路》的衔接。用户已确认上传本稿及新增大脑分区图；专业审阅尚未完成，继续保留Draft标识。
