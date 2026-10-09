# n³ Hearingpedia

**An AI-native Knowledge System for Hearing Science**

面向学生、研究者与专业读者的听觉科学知识网络，连接机制、感知、工程与临床方法。

网站地址：<https://betterci.github.io/n3-hearingpedia/>

## 为什么建立这个项目

听觉科学的概念跨越机制、感知与工程。项目以一个概念一页解释、每个概念连接其他概念的方式，组织前置知识、研究方法及可追溯文献。

## v0.5 内容

本轮近十天文献扩充见 [选词与核验记录](docs/research/monitor-expansion-2026-10-04.md)、[来源映射](docs/research/monitor-expansion-2026-10-04.json)和[逐词条证据映射](docs/research/wiki-evidence-map.json)。[v0.4 百科重构](docs/research/wiki-restructure-2026-10-04.md)与 [v0.3 深度扩写](docs/research/depth-expansion-2026-10-04.md)保留为历史版本。

- 64 个百科式词条：无标题导言、术语信息框、定义与分类、原理、方法、应用边界、分析示例及研究沿革。
- 7 个知识层面和 18 种概念类型，区分物理量、知觉功能、病理状态、神经响应、测试、指标、技术和模型；226 条带说明的知识关系，双向可遍历。
- 正文约 35 万中文字符，517 处逐词条去重的正文交叉链接；分级目录、编号引文、参见与相关概念。
- 753 项登记参考来源，配有教学图；文献使用范围逐项标注，图示明确区分理想模型、概念流程与实测。普通话汉语声调图对应“妈 mā、麻 má、马 mǎ、骂 mà”。
- [人工耳蜗](src/content/concepts/cochlear-implant.md)：系统流程图、临床使用配置、个体映射、双耳听觉及八个研究方向，27 项来源支持；保留成人、儿童、EAS 和个体化调机的任务及证据差异。见[扩写核验记录](docs/research/cochlear-implant-expansion-2026-10-05.md)。
- [人工耳蜗信号处理策略](src/content/concepts/cochlear-implant-coding-strategies.md)：六个厂商／系统系列的官方临床目录、策略对照表、六个已核实代码仓库及十三个研究方向；明确版本、旧设备兼容与仿真证据边界。见[核验记录](docs/research/ci-coding-strategies-2026-10-04.md)。
- 新增听力损失、助听器、响度、动态范围、外毛细胞、ABR、AEP、EEG、听觉注意、语音神经跟踪、听觉可塑性、聆听努力、噪声性听力损失、耳蜗突触病变、共振峰、空间听觉。
- 主题覆盖时域精细结构、音高、基频、谐波性、振幅调制、通道相互作用、ITD、SRT、纯音测听、校准、普通话声调、混淆矩阵、双耳整合、n-of-m、TLE、F0inTFS、GET、ASM、ZIN、BILD。
- [调研与证据记录](docs/research/meng-zhou-literature-and-batch-2.md)及[第二批目录](docs/research/second-batch-catalog.json)保留来源、选词理由与审阅状态。
- 13 个学科入口作为交叉索引；无独立词条的领域如实显示 0。
- 7 条节点完整的学习路径、研究专题和 Three.js 动态三维知识地图。支持旋转、缩放、暂停、概念定位、层面与关系筛选、全屏与退出全屏，以及从词条进入所选节点。
- KaTeX 公式、Pagefind 中文／英文搜索、移动端导航。
- 文献 DOI、引用用途与核验范围。当前全部词条为 Draft；预印本单独标注未同行评审，尚未完成专业审阅。
- 互动实验及自动文献跟踪为后续建设方向，尚未启用。

Tonotopy 的中文统一使用 **频位映射关系**。

Temporal 在信号表征与编码术语中优先译为“时域”：时域包络、时域精细结构、时域限制编码器、时域周期性等；时间差、时间延迟、时长和实际时间过程保留对应含义。Mandarin lexical tone 统一译为 **普通话汉语声调**。术语与图示更新见 [记录](docs/research/terminology-and-fullscreen-2026-10-04.md)。

## 本地运行

需要 Node.js 24 和 pnpm 11.19.0（与 CI 一致）。

    pnpm install --frozen-lockfile
    pnpm dev

默认地址：<http://127.0.0.1:4321/n3-hearingpedia/>

搜索索引在构建后生成。测试完整搜索使用生产预览：

    pnpm check
    pnpm build
    pnpm verify
    pnpm preview

页面链接、资源和搜索包统一处理仓库子路径。若使用其他部署地址，通过环境变量覆盖 SITE_URL（站点 origin）和 BASE_PATH（路径前缀）；构建、验证与预览应使用相同配置。默认分别为 https://betterci.github.io 和 /n3-hearingpedia。

## 普通话辅音语音学基础

2026-10-09 新设同级类目 **普通话辅音感知**，首批增加用户确认的14篇语音学基础词条：辅音与声母、发音部位与方式、塞音、塞擦音、擦音、鼻音、边音、送气、清浊、舌尖前后音、舌面前音及国际音标。新增学习路径、专题与知识关系，全部内容为待审阅草稿。来源范围和记音选择见[核读记录](docs/research/mandarin-phonetics-2026-10-09/research-notes.md)。

## 词条分享图片

每个词条的「帮助完善这个词条」右侧有「词条分享」文字链接，点击后在当前页面的小窗中显示分享图，支持复制、保存、关闭及 Esc 退出。图片在首次打开时生成，宽 1080 像素，包含中英文名称、简介、分类、前四项关键事实、更新时间、审阅状态及原词条二维码。内容直接读取词条元数据，文字较长时自动换行并增加图片高度。原有 `/share/词条slug/` 地址继续可用。

电脑上点击「复制图片」后可粘贴到微信聊天；手机上可保存图片、长按图片保存，或在支持的浏览器中使用系统分享菜单。图片剪贴板需要 HTTPS（本机 localhost 也可）及浏览器支持，复制不可用或被拒绝时页面提示保存方式。二维码按 `SITE_URL` 和 `BASE_PATH` 指向正式词条，独立分享页不进入 Pagefind 搜索索引。

## 新增词条

潜在合作者可先阅读[词条编写规范与协作模板](docs/contributor-kit/README.md)，分别按基础词条或深度词条的要求提交正文、文献和图片。网站“参与贡献”页提供[在线规范](https://betterci.github.io/n3-hearingpedia/contribute/writing-guide/)与可下载模板，包内附 AI 辅助撰写提示词、交稿清单及网站接入说明。

深度词条的结构、内容深度、配图格式和验收要点见[早期经验与撰写参照](docs/in-depth-entry-writing-guide.md)，其中保留历史样本统计与可复用的起草骨架。

1. 在 src/content/concepts/ 新建 Markdown 文件，可以复制一个已有词条。
2. 填写 title、english、slug、summary、categories、tags、status、日期、作者、references 和 order；添加 knowledge_area、kind 与至少两项 key_facts。batch 仅保留来源批次，不用于公众导航。
3. categories 使用 [学科定义](src/data/domains.ts) 的 ID；knowledge_area 和 kind 使用 [知识体系](src/data/knowledge.ts) 的定义；slug 与文件名保持一致。
4. 在 [文献定义](src/data/references.ts) 中登记文献，并在 references 中填写对应 ID。
5. 正文引用使用 `[1](#ref-文献ID "来源标题")`，编号与 references 的顺序一致。正文概念链接使用 `../词条slug/`。
6. 在 [关系定义](src/data/relations.ts) 登记关联，每条包含 source、target、type 与 note；同一条关系只登记一次，页面自动显示正向与反向描述。
7. 运行 check、build、verify，检查页面后提交 PR。

更新 [证据映射](docs/research/wiki-evidence-map.json) 的字符数、章节数、文献与交叉链接。验收检查校验关系端点、重复关系、类型循环、测量与分析对象、学习路径、编号引文、页面资源与搜索索引。学习路径定义在 [paths.ts](src/data/paths.ts)。

关系类型包括 subtype（属于类型）、describes（表征）、mechanism（机制联系）、measured-by（测量）、analyzed-by（分析）、application（应用）和 related（概念联系）。方向由定义决定；机制联系与概念联系为对称关系。学习顺序单独组织。知识分类是本网站的编辑框架，不宣称为统一学科本体；地图位置、连线动画不编码因果效应、证据强弱或解剖距离。

## 内容与科学审阅

新词条及 AI 草稿默认 Draft。Reviewed 或 Stable 必须提供实际 reviewer 和 reviewed_at，构建会检查这两个字段。实质论断改变后，应重新审阅；旧记录不能自动覆盖新版本。

last_updated 是词条修改日期；literature_checked_at 是记录过检索范围的文献检查日期；reviewed_at 是专业审阅日期。三者不能互相代替。

参考文献中 access 区分全文、摘要、书目和官方方法文档，supports 说明引用用途。书目信息已核验不代表科学论断已核验。AI 生成文字不能作为引用来源。

写作以百科导言为入口，随后分层解释定义、机制、测量和应用。章节按概念性质调整，避免为了统一模板制造空栏目。术语信息框记录稳定事实；方法参数注明版本和条件。研究沿革是有来源的发展线索，不是完整历史。公式定义变量与单位，分析示例明确区分推导、教学假设和实测数据。

## AI 辅助文献更新

先由贡献者提供与研究问题相关的论文，AI 协助形成草稿；之后再考虑主题检索。更新记录模板位于 [docs/update-proposal-template.md](docs/update-proposal-template.md)。

流程：论文输入 → 核验与筛选 → 对应词条 → 逐项引用与修改草稿 → 专业审阅 → 合并发布。

基础概念保留经典证据，新论文补充研究进展、边界条件与争议。不将单篇新论文自动视为替代共识的依据，不声称有限检索覆盖全部最新研究。

## GitHub Pages 部署

目标仓库：<https://github.com/BetterCI/n3-hearingpedia>，主分支为 main。

1. 仓库 Settings → Pages → Build and deployment → Source 选择 **GitHub Actions**。
2. 推送到 main，工作流检查类型、构建页面、生成搜索索引并验证内部链接。
3. build 成功后，deploy 发布 GitHub Pages。PR 仅进行构建验证，不发布。

工作流位于 [.github/workflows/deploy.yml](.github/workflows/deploy.yml)。如果更改账户或仓库名，同时更新工作流的 SITE_URL、BASE_PATH，以及站点与 README 中的 GitHub 链接。

## 目录

    src/content/concepts/    Markdown 词条
    src/content.config.ts   元数据校验
    src/data/domains.ts     13 个学科索引
    src/data/knowledge.ts   知识层面与概念类型
    src/data/relations.ts   单一关系数据源
    src/data/paths.ts       学习路径
    src/data/references.ts  文献与核验范围
    src/pages/              页面与动态词条路由
    src/layouts/            统一网站布局
    src/styles/             响应式样式
    src/scripts/            三维地图与浏览器交互
    docs/                   编辑及更新记录
    scripts/verify.mjs      构建产物的链接、公式与索引检查

## 如何贡献

通过 Fork / Pull Request 提交，附修改目的、对应证据和待核实项。项目维护者协调作者与审阅者。代码和原创内容的开放许可证尚待项目维护者确定；第三方论文与其他资料保留原有权利。
