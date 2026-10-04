# 人工耳蜗信号处理策略：官方目录、代码与研究证据

核验日期：2026-10-04。新增词条：[人工耳蜗信号处理策略](https://betterci.github.io/n3-hearingpedia/concepts/cochlear-implant-coding-strategies/)。逐项来源、仓库覆盖及检索筛选见[结构化记录](ci-coding-strategies-2026-10-04.json)。

## 范围和方法

以可公开核验的厂商验配手册、产品规格及官方器械评估确定临床名称，按处理器、植入体和软件版本保留兼容范围。分别整理 Cochlear、MED-EL、Advanced Bionics、Neurelec／Oticon Medical、诺尔康、力声特六个系列。历史策略与仍列于兼容目录的策略分开；不将前端降噪、EAS、ABF、产品家族名称作为独立编码器。

研究检索采用 deep-research 工作流，从 OpenAlex 主题检索得到 15 项结果，DeepACE 2023 原始论文种子 W4361767319 的后向结果 44 项、前向结果 30 项，去重得到 87 项候选。按题名与可用摘要人工筛选，补充厂商原始文档及 2025–2026 年原始研究。通用增强网络、统计方法、语料及综述用于背景发现，不直接支撑临床编码结论。没有将命中数量称为全部研究数量，也没有把文献引用数当作科学质量评分。

本次词条共引用 **35 项来源**，核实 **6 个代码仓库**，总结 **13 个研究方向**。包含现行／归档厂商文档、原始论文、作者稿和软件文档。文章默认 Draft；文献检索不等于专业审阅。

## 官方目录中需要保留的条件

- **Cochlear**：Custom Sound 6.1 页 51–53、71 和原厂 Clinical Guidance 1.9 节确定选择／映射规则；HAS 2026 评估的 Nexa 与旧植入体列必须分别读取。Nexa 列为 ACE，旧植入体兼容列才为 ACE/CIS/SPEAK/MP3000。
- **MED-EL**：MAESTRO 11 印刷页 345–346（PDF 页 347–348）明确 HDCIS、FSP、FS4、FS4-p 及 TEMPO+ 专用 CIS+；FS4-p 并行兼容限制不能省略。
- **AB**：可访问的 Target CI 原厂归档指南确定 HiRes S/P、Fidelity120 S/P、Optima S/P 与前端选项；Q90 旧规格的 CIS/MPS 来自官方搜索索引，旧 PDF 下载返回 404。提供当前 eIFU 目录并说明该证据限制，不把旧清单扩展到全体新型号。
- **Neuro 系列**：Neuro 2 Version C PDF 页 7 列明 MPIS CAP/XDP、CRYSTALIS CAP/XDP，刺激方式为时长调制伪单相脉冲及被动放电。2024 年 CI 业务收购背景取自 Cochlear 原厂年报。
- **诺尔康**：Enduro 画册 PDF 页 9 列明 APS、CIS、C-Tone、Symphony；原厂托管 2015 系统论文 2.1 节支持前三种已公开机制中的 CIS、APS、Symphony。C-Tone 算法细节未取得，不按名称推断。
- **力声特**：官网当前产品页可访问，文本可核对名称的材料来自厂商署名福祉展产品介绍，列明 L-CIS 与 MTone。清楚标注其为产品介绍而非技术手册，不使用宣传效果陈述作为疗效证据。

爱益声的现行官方策略目录仍存在资料缺口。以上是六个系列的公开证据目录，不宣称覆盖所有地区、全部历史设备或所有可选软件配置。

## 代码核验

| 仓库 | 核实内容 | 边界 |
| --- | --- | --- |
| [mohead/pulsatile-vocoder](https://github.com/mohead/pulsatile-vocoder) | README、MIT、ACE/CIS 相关 MATLAB 文件 | 作者明确否认商用逐位等价保证 |
| [CILabUTD/CCi-MOBILE](https://github.com/CILabUTD/CCi-MOBILE) | MATLAB ACE、Android ACE.java、受保护 .p 校验 | 未检出统一顶层许可；不称全套完全开源；具体 BACE／混合速率补丁未核实 |
| [jabeim/AB-Generic-Python-Toolbox](https://github.com/jabeim/AB-Generic-Python-Toolbox) | GPL-3.0、HiRes120、F120 电映射与电极图、真实入口文件 | 不冒充 HiRes Optima；README 中旧入口名称与当前树有差异，正文采用实际文件名 |
| [APGDHZ/DeepACE](https://github.com/APGDHZ/DeepACE) | 1.0、GPL-3.0、main.py／model.py | 与 2.0 分开 |
| [APGDHZ/DeepACE2.0](https://github.com/APGDHZ/DeepACE2.0) | 2.0、README、模型与依赖文件 | 未检出许可；所附长 PDF 为学位论文，未冒充期刊全文 |
| [NECOTIS/spiking-deep-ace](https://github.com/NECOTIS/spiking-deep-ace) | 由原论文直达，ACE 模块、PyTorch 模型、train/evaluate | 未检出许可／预训练发布；能耗估计不是设备续航实测 |

记录保存检索时 API 返回的树 SHA、默认分支、最后推送时间和文件覆盖。未执行、训练或向植入设备输出第三方代码。未核实专用实现的临床策略如实标注，研究 CIS 仅是机制基线，不能替代 HDCIS、L-CIS 或某厂商 CIS 的等价验证。

排除同名但属于因果推断／DNA 的 DeepACE 项目；Clarity SAMII 支持仓库不是 CI 编码器，未加入代码表。

## 研究证据的关键边界

十三个方向为 TLE、F0inTFS、DeepACE、Fused DeepACE、ElectrodeNet-CS、AVSE-ECS、混合速率 ITD 编码、双耳联合谱峰选择、MOC 仿生压缩、电流聚焦、Spiking Deep ACE、注意代理线索引导、语音／音乐源分离端到端编码。

- TLE 2022 有植入者音高数据；F0inTFS 2023 与 ElectrodeNet 的相关行为数据是正常听力声码器实验。
- AVSE-ECS 2026 为仿真；DeepACE 2023 和 Fused DeepACE 2024 有植入者语音数据，仍属于实验策略。
- 2025 混合速率研究保留 ITD 更好，但短期自由场定位未改善；2026 双耳谱峰同步没有独立收益，硬件同步只有受任务限制的小范围收益。
- Spiking Deep ACE 已有 ICASSP 2026 正式 DOI；作者稿在 2026-08-28 提交。能耗依据运算及 45 nm 成本模型，不能解读为实际临床处理器续航结果。
- Brain-Informed 方法 2.4 节明确由目标语音产生代理包络；不能写成真实 EEG—注意解码—植入体的闭环验证。
- 2026 语音／音乐研究的端到端方法在语音任务更好，前端方法在音乐欣赏问卷更好，说明任务目标不能混用。

正文通过编号引文连接以上论断，并为每项来源标注全文／摘要／官方文档及用途。已加入人工耳蜗主词条、学习路径和 12 条语义关系；三维地图、索引和搜索由构建更新。
