# n³ Hearingpedia

**An AI-native Knowledge System for Hearing Science**

面向课题组成员共建的听觉科学知识网络。先支持组内学习、文献阅读和实验设计，再逐渐扩大读者范围。

网站地址：<https://betterci.github.io/n3-hearingpedia/>

## 为什么建立这个项目

听觉科学的概念跨越机制、感知与工程。项目以一个概念一页解释、每个概念连接其他概念的方式，组织前置知识、研究方法及可追溯文献。

## v0.1 内容

- 8 个实质词条：耳蜗、频位映射关系、听觉滤波器、掩蔽、时间包络、声码器、语音可懂度、人工耳蜗。
- 12 个领域入口，实际数量按词条元数据统计；无独立词条的领域如实显示 0。
- 2 条节点完整的学习路径、研究专题和可点击知识地图。
- KaTeX 公式、Pagefind 中文／英文搜索、移动端导航。
- 文献 DOI、引用用途与核验范围。全部首批词条为 Draft，未获成员科学审阅。
- 互动实验及自动文献跟踪为后续建设方向，尚未启用。

Tonotopy 的中文统一使用 **频位映射关系**。

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

## 新增词条

1. 在 src/content/concepts/ 新建 Markdown 文件，可以复制一个已有词条。
2. 填写 title、english、slug、summary、categories、tags、status、日期、作者、related、references 和 order。
3. categories 使用 [领域定义](src/data/domains.ts) 中的领域 ID；slug 与文件名保持一致。
4. 在 [文献定义](src/data/references.ts) 中登记文献，并在 references 中填写对应 ID。
5. 正文引用使用 Markdown 链接，目标格式为 #ref-文献ID，其锚点由页面生成。
6. related 使用已有词条 slug，并注明关系类型。
7. 运行 check、build、verify，检查页面后提交 PR。

首批固定数量的验收检查可在后续扩容时相应调整，实际领域和词条卡片自动生成。学习路径定义在 [paths.ts](src/data/paths.ts)。

关系类型包括 prerequisite（前置知识）、mechanism（机制）、application（应用）、method（研究方法）和 related（相关概念）。关联是从当前词条指向所列词条的阅读提示；地图不把连线解释为因果关系。

## 内容与科学审阅

新词条及 AI 草稿默认 Draft。Reviewed 或 Stable 必须提供实际 reviewer 和 reviewed_at，构建会检查这两个字段。实质论断改变后，应重新审阅；旧记录不能自动覆盖新版本。

last_updated 是词条修改日期；literature_checked_at 是记录过检索范围的文献检查日期；reviewed_at 是成员审阅日期。三者不能互相代替。

参考文献中 access 区分全文、摘要、书目和官方方法文档，supports 说明引用用途。书目信息已核验不代表科学论断已核验。AI 生成文字不能作为引用来源。

正文建议包含一句话理解、直觉、核心概念、公式与变量、实验／方法入口、阅读组内论文时的检查点、后续更新关注点。公式和临床／工程栏目按相关性使用。

## AI 辅助文献更新

先由成员提供组会或课题相关论文，AI 协助形成草稿；之后再考虑主题检索。更新记录模板位于 [docs/update-proposal-template.md](docs/update-proposal-template.md)。

流程：论文输入 → 核验与筛选 → 对应词条 → 逐项引用与修改草稿 → 成员审阅 → 合并发布。

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
    src/data/domains.ts     12 个领域
    src/data/paths.ts       学习路径
    src/data/references.ts  文献与核验范围
    src/pages/              页面与动态词条路由
    src/layouts/            统一网站布局
    src/styles/             响应式样式
    docs/                   编辑及更新记录
    scripts/verify.mjs      构建产物的链接、公式与索引检查

## 如何贡献

通过 Fork / Pull Request 提交，附修改目的、对应证据和待核实项。课题组维护者协调作者与审阅者。代码和原创内容的开放许可证尚待项目维护者确定；第三方论文与其他资料保留原有权利。
