# 词条网站接入说明

本说明供直接提交仓库的作者和接入维护者使用。非技术作者先按编写规范交正文、证据和图即可。以下代码为格式模板，占位符需要替换，来源需要登记；模板不能原样作为可发布词条。

## 文件与元数据

词条放在 `src/content/concepts/<slug>.md`，文件名与 `slug` 一致；slug 使用简洁的小写英文及连字符。先检索已有词条，避免重复。正式词条开头采用 YAML 元数据，正文不另加 `#` 大标题。

```yaml
---
title: "填写中文名称"
english: "Fill in English name"
slug: "replace-with-concept-slug"
summary: "用一至两句说明概念及词条范围"
categories: ["signal-processing"]
tags: ["填写主题标签"]
aliases: []
level: ["graduate"]
status: "draft"
depth: "standard"
last_updated: "YYYY-MM-DD"
literature_checked_at: null
authors: ["填写实际作者署名"]
reviewer: null
reviewed_at: null
knowledge_area: "methods"
kind: "model"
key_facts:
  - { label: "性质", value: "填写稳定的基本事实" }
  - { label: "方法或用途", value: "填写稳定的基本事实" }
references: ["source-01"]
order: 1000
---
```

基础词条保留 `depth: standard`，深度词条改为 `depth: in-depth`。示例中的分类、类型和排序只是格式展示，必须依主题替换。`categories` 取 `src/data/domains.ts` 的 ID；`knowledge_area` 和 `kind` 取 `src/data/knowledge.ts` 的合法值。`key_facts` 至少两项，建议三至五项，不能把有条件的研究数值写成稳定事实。

`last_updated` 使用真实修改日期。只有完成有范围记录的文献检查，才填写 `literature_checked_at`。新稿的 `reviewer` 和 `reviewed_at` 保持空值；Reviewed 或 Stable 必须有真实具名专业审阅记录。`batch` 可省略，由维护者按项目约定处理，不作读者导航。

## 文献与引用

在 `src/data/references.ts` 或由其导入的主题参考表中登记来源。记录包括 `title`、`authors`、`year`、`publication`、`url`、`access`、`supports`，有 DOI 时填写 `doi`；预印本另加 `publicationType: 'preprint'`。

`access` 使用 `fulltext`、`abstract`、`metadata` 或 `documentation`，依实际访问范围填写。`supports` 写明来源支持什么以及限制；只有书目核验不能支持方法与结果。已有相同来源优先复用，不为新词条重复创建同一论文。

元数据 `references` 填登记后的真实 ID。正文使用 `[1](#ref-source-01)`，图注可使用 `<a href="#ref-source-01">1</a>`；编号与 `references` 的顺序一致。这里的 `source-01` 是占位 ID。正式参考列表由页面生成，正文不再手工重复一份参考文献。

## 图片嵌入

图片放在 `public/figures/<slug>/`，采用描述内容的稳定文件名。以下示例尺寸和名称需按实际资源替换：

```html
<figure class="encyclopedia-figure">
  <a href="/n3-hearingpedia/figures/replace-with-concept-slug/01-mechanism.svg"
     target="_blank" rel="noopener" aria-label="查看完整图">
    <img src="/n3-hearingpedia/figures/replace-with-concept-slug/01-mechanism.svg"
         alt="用一句话说明图中的对象及关系"
         width="1400" height="800" loading="lazy" />
  </a>
  <figcaption><strong>图 1　填写短标题。</strong>
    填写分面、参数、单位、图意、数据性质、边界及来源。
    <a href="#ref-source-01">1</a>
  </figcaption>
</figure>
```

部署前缀与站点配置保持一致。信息框可选 `illustration: { src: 'figures/...', alt: '...', caption: '...' }`，由页面处理路径。图片替代文本不能只写“图 1”；位图记录实际尺寸。原创图的脚本、参数和转载图的许可记录随稿保存，路径由维护者整理。

## 概念链接与关系

正文中的已存在词条用 `../<slug>/` 链接；新概念建议先在交稿说明中列出，未创建前不写成可点击的正式链接。

知识关系统一登记在 `src/data/relations.ts`，字段为 `source`、`target`、`type`、`note` 和 `strength`，端点必须存在。`type` 使用 `subtype`、`describes`、`mechanism`、`measured-by`、`analyzed-by`、`application` 或 `related`，方向以现有定义为准，同一关系只登记一次。`strength` 为维护者选择的 1、2 或 3 级导航权重，不代表因果效应或科学证据等级。

## 接入与工程验收

1. 替换全部占位符，核对元数据、来源 ID 与正文编号。
2. 检查图源、图片路径、公式和已存在的概念链接。
3. 登记适当知识关系，更新 `docs/research/wiki-evidence-map.json` 中对应记录；学习路径确有需要时更新。
4. 依项目 README 配置依赖，执行 `pnpm check`、`pnpm build`、`pnpm verify`。
5. 预览桌面与手机页面，检查目录、中文字体、公式、表格、图片点击与引用跳转。
6. 提交 Pull Request，附交稿说明和实际检查结果，保留真实审阅状态。

工程检查保证页面与数据可用，科学审阅保证论断与解释可靠，两者分别记录。
