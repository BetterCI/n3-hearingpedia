# 《助听器处方公式》研究与来源记录

日期：2026-10-09。用于百科深度词条的定向文献研究，不是覆盖所有数据库的系统综述。

## 问题与范围

解释气导助听器处方如何把分耳听阈、个体及声学条件映射为频率和输入声级相关的目标；区分NAL与DSL的理论、经验调整、版本和验证坐标。比较证据分为目标／模型比较、真实耳内实现、行为结局及日常偏好。本文不编制个体验配方案，不生成未公开算法的目标，也不把骨导或人工耳蜗处方并入气导范围。

## 发现与扩展

主题关键词组合包括hearing aid prescription、NAL-NL2、DSL v5、gain targets、real-ear verification、RECD、children outcomes、listening preferences及NAL-NL3。使用OpenAlex主题发现，再用DOI、标题、作者及机构线索查找原始出版源；出版社、PubMed／PMC、作者机构和专业组织资料用于核验。

主种子为Keidser等2011年《The NAL-NL2 Prescription Procedure》，DOI 10.4081/audiores.2011.e24，OpenAlex W2104058659。进行了一个层级的向后与向前扩展，保留主题相关条目；没有无限递归扩展。

- `openalex-discovery.json`：24条主题发现记录。
- `openalex-backward.json`：13条向后扩展记录；对种子引用文献进行有限核查，不声称读取了所有引用全文。
- `openalex-forward.json`：45条向前扩展记录；有限批次按引用相关信息筛查，另以定向检索补充近期来源。
- `selected-evidence.json`：23项正式来源的编号、书目信息、访问状态、发现方式、核读位置和用途。14项新登记，9项复用既有来源。

这些记录是发现和筛选痕迹；OpenAlex摘要和书目元数据不独立承担正文研究结论。停止条件为主要方法、声学验证、儿童比较、成人偏好及当前版本进展已各有对应原始来源。尚未取得全部NAL-NL3主体算法推导与独立长期比较，未据官方发布文字宣称普遍优效。

## 证据和访问限制

NAL-NL2、DSL v5及经验调整使用公开全文的实际相关章节。原始NAL-R历史研究只核对摘要；系数和软件分支另由固定版本官方代码支持。儿童比较保留LOCHI初次与随访中的版本混合；组间未显著差异不等于严格等效。2023年成人偏好试验两个程序均按即时反馈调整，不能写成未经调整的初始设置对严格处方目标的简单比较。

NAL-NL3官方资料用于版本与模块用途。Croteau与Kwok临床说明只核对原始摘要。2026年9月噪声舒适模块原始论文核读出版社公开索引返回的正文相关段落，并用PubMed核验作者、日期和摘要；保留单中心、多研究迭代、开发者参与及特定装置／场景限制。部分PMC或出版社直接打开返回访问障碍时，利用可公开读取的原始全文相关段落或作者稿；没有将访问失败标记为成功读取全部全文。

来源表分别标记fulltext、abstract和documentation。复用来源的本次或既有核读范围逐项写在evidence_location中，未统一升级为全文。文献检索及AI整理用于撰写，不替代专业审阅。

## 代码、图片与计算

Clarity官方`clarity/enhancer/nalr.py`固定提交：`dcceaabab7786a94ba5ba8bef4177040f4521ccc`。

源文件稳定链接：<https://github.com/claritychallenge/clarity/blob/dcceaabab7786a94ba5ba8bef4177040f4521ccc/clarity/enhancer/nalr.py>。

实际核对六个控制频率、bias、critical_loss两条分支、非负截断以及后续FIR步骤。本文只重算总听阈120所用分支的六个增益控制点，未运行Clarity滤波器，未把实现命名扩展为NAL-NL2或NAL-NL3。

五张图均为原创代码绘制，SVG用于网页、PNG用于预览，未转载文献图片。生成脚本为`scripts/generate-hearing-aid-prescription.py`，固定参数与核验见`figure-verification.json`。核对内容包括NAL-R控制点、分段函数连续性及单调性、RECD加法、三声级目标误差及RMS、表观输入输出比。全部听阈、目标、RECD和输出示例为人工教学设定，没有临床受试者或规范容差含义。多阶段函数只说明DSL相关概念，不调用DSL算法。

## 待确认内容

本稿保留Draft专业审阅状态。可以重点审阅NAL／DSL比较的篇幅、计算例子的难度及NAL-NL3近期研究的篇幅。正式发布授权与具名专业审阅分别记录；用户已于2026-10-09确认提交并推送本稿，具名专业审阅尚未完成。
