# 《概率论》交稿与接入记录

完成于2026-11-02。目的：沿用《线性代数》的基础课程定位，用听觉/声学实例学习数学，并发布到既有补充学习入口。

正文为深度词条，约9000个汉字、11节、29个小节，17项直接引用；包含8张原创数值SVG、3段共同增益的PCM音频、3个可运行的正文代码示例、完整下载脚本及6道有答案的自检题。基础概率为主体，随机过程与统计推断作为听觉研究连接，导言明确课程范围及先修要求。

AI用于资料定位、相关段落对照、解释与推导撰写、图/音频/代码生成、独立数值核验与网站接入。没有真实受试者数据，没有转载图，没有填写虚构审阅者。公式的假设、模型单位和声学解释在正文相邻位置说明。

## 接入范围

- `src/content/concepts/probability-theory.md`：正式课程正文，保留Draft。
- `src/data/probability-theory-references.ts`：14项新登记来源；复用已有正态文档、Wichmann/Hill论文与NIST Wilson来源，共17项引用。
- `src/data/paths.ts`：新增默认折叠的补充路线，从课程进入心理声学、信号检测、混淆矩阵与PSD。
- `src/data/relations.ts`：8条相关概念边；证据映射与README统计同步更新。
- 复用已有 `course` 展示：学习页主要路线之后可找到，首页及主概念列表不展示，搜索和知识地图仍保留。

## 科学与工程核验

详见 `scientific-audit.md`、`numerical-validation.json`、`content-validation.json` 与 `publication-validation.json`。

独立核验不是只重复绘图代码：二项分布用组合数枚举，正态/后验用积分，平均噪声用完整协方差矩阵，Wilson区间用score等式逆验，音频检查实际PCM头信息与逐样本重建。3个正文代码块及完整下载代码均实际执行。

逐图审阅后修复了缺字与离散图坐标范围；浏览器检查发现HTML图注中的原始TeX未渲染，已替换为普通符号和HTML上标并加入针对图注的检查。数学审读将四格样本空间改用0/1坐标，以严格区分基本结果与事件；补明AR创新的零均值、初始值独立、样本方差n至少为2及条件类别正概率。

## 位置与链接

文章目标：`https://betterci.github.io/n3-hearingpedia/concepts/probability-theory/`。

默认折叠入口：`https://betterci.github.io/n3-hearingpedia/learn/#foundations`。

直接展开路线：`https://betterci.github.io/n3-hearingpedia/learn/#probability-theory-foundations`。

发布版本和线上核验状态由发布后记录给出，以上目标URL本身不作为部署成功证据。
