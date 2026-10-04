# n³ Hearingpedia

> **An AI-native Knowledge System for Hearing Science**

## 1. 项目目标

建立一个面向听觉科学、听力学、心理声学、人工耳蜗、助听器、语音感知、听觉神经科学、声信号处理与 AI for Hearing 的开放知识网站。

**首批主要服务课题组成员，围绕组内学习、文献阅读、实验设计和跨领域交流组织知识；在内容与维护流程成熟后，逐渐扩大到外部学生、研究者及其他专业读者。**

初期成功标准是成员能理解研究中遇到的概念、找到对应证据，并沿关联词条补齐前置知识。开放网站的长期定位保留，首批内容不要求覆盖所有领域。

项目名称统一写作：

# **n³ Hearingpedia**

注意：

- `n` 必须小写。
- `3` 使用上标形式：`n³`
- 不写成 `N³`
- 英文主名称为 `n³ Hearingpedia`
- 推荐副标题：

> **An AI-native Knowledge System for Hearing Science**

术语约定：**Tonotopy 的中文统一使用“频位映射关系”**，用于词条标题、正文、目录与知识地图。

第一版的首要目标不是建立完整百科，而是建立一个：

**看起来已经像一个真正项目、可以浏览、可以扩展、可以持续加入知识节点的 MVP。**

项目必须适合部署到 **GitHub Pages**。

---

## 2. 核心设计思想

n³ Hearingpedia 不应只是一个传统 Wikipedia clone。

它应该逐渐发展为：

**Knowledge Base + Textbook + Knowledge Graph + Interactive Lab + Literature Map + AI Tutor**

第一版重点完成前三项中的基础框架：

1. Knowledge Base
2. Textbook-style explanation
3. Knowledge Graph navigation

暂时不要实现复杂后台。

---

## 3. 三小时开发原则

整个 v0.1 必须以：

> **3 小时内能够部署上线**

为约束。

三小时约束针对可部署的工程演示版。词条数量与科学审阅分阶段完成，不因上线期限将未审阅内容标记为 Reviewed。

因此禁止过度工程化。

优先级：

```text
可用
↓
好看
↓
内容结构合理
↓
容易扩展
↓
以后再增加 AI
```

不要一开始构建：

- 用户系统
- 数据库后台
- 登录
- CMS
- AI Agent backend
- 自动 PubMed crawler
- 复杂知识图数据库
- 在线编辑器

这些全部留到后续版本。

---

## 4. 推荐技术栈

优先使用：

```text
Astro
+
Markdown / MDX
+
GitHub Pages
```

推荐：

- Astro
- TypeScript
- Markdown / MDX
- KaTeX
- Mermaid
- Pagefind
- GitHub Actions

如果 Astro 配置影响三小时目标，可退化为：

```text
HTML
CSS
JavaScript
Markdown
GitHub Pages
```

原则：

**部署稳定 > 技术先进。**

---

## 5. 网站整体结构

首页顶部：

```text
n³ Hearingpedia
An AI-native Knowledge System for Hearing Science
```

下面放一句项目定位：

> Explore how sound becomes hearing — from acoustics and cochlear mechanics to perception, cochlear implants and artificial intelligence.

首页需要包含以下主要入口。

---

## 6. 一级知识领域

建立 12 个一级领域。

### 01 Acoustics

内容包括：

- Sound
- Frequency
- Amplitude
- Phase
- Spectrum
- Fourier transform
- Resonance
- Sound pressure level
- Decibel
- Impulse response

### 02 Ear & Cochlea

内容包括：

- Outer ear
- Middle ear
- Inner ear
- Cochlea
- Basilar membrane
- Hair cells
- Tonotopy
- Cochlear amplifier
- Cochlear compression

### 03 Auditory Neuroscience

内容包括：

- Auditory nerve
- Phase locking
- Temporal coding
- Rate coding
- Auditory brainstem
- Inferior colliculus
- Auditory cortex
- Neural plasticity

### 04 Psychoacoustics

内容包括：

- Loudness
- Pitch
- Masking
- Critical bands
- Auditory filters
- Temporal resolution
- Frequency selectivity
- Modulation detection

### 05 Spatial & Binaural Hearing

内容包括：

- ITD
- ILD
- HRTF
- Binaural unmasking
- Localization
- Binaural fusion

### 06 Speech Perception

内容包括：

- Speech acoustics
- Formants
- Vowels
- Consonants
- Voice onset time
- Mandarin tones
- Speech intelligibility
- Speech in noise

### 07 Hearing Loss

内容包括：

- Conductive hearing loss
- Sensorineural hearing loss
- Hidden hearing loss
- Presbycusis
- Noise-induced hearing loss
- Auditory neuropathy

### 08 Audiology

内容包括：

- Pure-tone audiometry
- Audiogram
- Hearing level
- RETSPL
- Speech audiometry
- SRT
- Word recognition
- Tympanometry

### 09 Hearing Aids

内容包括：

- Amplification
- WDRC
- Prescription
- NAL
- DSL
- Real-ear measurement
- Directional microphones
- Noise reduction

### 10 Cochlear Implants

内容包括：

- Cochlear implant
- Electrode array
- Electrical stimulation
- CIS
- ACE
- n-of-m
- Channel interaction
- Temporal coding
- Current spread
- Electrode-neuron interface

### 11 Auditory Signal Processing

内容包括：

- Filter banks
- STFT
- Envelope extraction
- Hilbert transform
- Modulation spectrum
- Vocoder
- Beamforming
- Noise reduction

### 12 AI for Hearing

内容包括：

- ASR
- Speech enhancement
- Hearing-aid AI
- Cochlear-implant AI
- Deep learning
- Self-supervised speech models
- Hearing foundation models
- Computational audiology

---

## 7. 首页结构

首页建议采用以下视觉结构。

### Hero

中央显示：

```text
n³
Hearingpedia
```

以及：

```text
An AI-native Knowledge System for Hearing Science
```

提供搜索框：

```text
Search hearing science...
```

下面放三个按钮：

```text
Explore Concepts
Explore the Map
Start Learning
```

---

## 8. Explore 页面

建立：

```text
/explore
```

显示 12 个知识领域。

使用 card grid。

例如：

```text
Psychoacoustics

How physical sound becomes auditory perception.

38 concepts
```

点击进入：

```text
/psychoacoustics
```

---

## 9. Knowledge Graph

建立：

```text
/map
```

第一版不需要真正复杂的 graph database。

使用简单 SVG / Mermaid / JavaScript graph 即可。

中心节点：

```text
Hearing Science
```

一级连接：

```text
Acoustics
Ear
Neuroscience
Psychoacoustics
Speech
Audiology
Hearing Aids
Cochlear Implants
Signal Processing
AI
```

点击节点进入相关领域。

目标是让用户产生：

> “这不是普通百科，而是一张知识地图”

的感觉。

---

## 10. 每个知识词条统一模板

这是整个项目最重要的设计。

所有 concept 页面必须采用统一结构。

例如：

```text
/concepts/auditory-filter
```

页面模板：

### Auditory Filter

#### One-sentence idea

用一句话解释这个概念。

例如：

> The auditory system behaves approximately like a bank of overlapping band-pass filters.

#### Intuition

避免直接上公式。

先用通俗语言解释：

“耳朵不是一次把所有频率一起分析，而像同时开着很多相互重叠的小窗户。”

#### Why it matters

解释：

- 对听觉意味着什么
- 对实验意味着什么
- 对临床意味着什么
- 对工程意味着什么

#### Core idea

正式解释理论。

#### Key equation

支持 KaTeX。

例如：

```math
ERB(f)=24.7(4.37f/1000+1)
```

公式下面必须解释每一个关键变量。

不要只显示公式。

#### Interactive intuition

预留：

```text
[Interactive demo coming soon]
```

以后可以接 Hearing PhET。

#### Classic experiment

简单介绍经典实验范式。

#### Hearing impairment

解释听力损失如何改变该现象。

#### Hearing aids / CI

如果相关，解释：

- hearing aid
- cochlear implant

中的意义。

#### Related concepts

例如：

```text
Critical band
Frequency selectivity
Masking
ERB
Cochlear tuning
```

#### Key references

列出：

- 经典论文
- 经典教材
- 综述
- 最新代表性论文

所有 reference 尽可能包含 DOI。

---

## 11. 页面阅读层级

首批词条主要服务课题组成员，包括新入组学生、跨专业成员和正在开展相关研究的成员。

优先回答：

1. 这个概念是什么意思，与哪些熟悉的概念相连？
2. 阅读组内相关论文前，需要掌握哪些前置知识？
3. 它如何影响实验设计、参数选择、结果解释或算法实现？
4. 哪些结论已有较充分支持，哪些仍存在争议或适用条件？

后续根据实际反馈逐渐扩展到本科生、工程师、临床听力师及外部科研人员，不要求首版同时满足所有读者。

因此页面采用：

```text
Intuition
↓
Core concept
↓
Equation
↓
Experiment
↓
Clinical relevance
↓
Research frontier
```

这种逐层深入结构。

---

## 12. 首批知识词条的选择

第一版不要追求数量。

首批按课题组当前课题、组会论文和成员反复遇到的概念选择，并补齐它们的前置知识。先完成一条可连续学习的路径，避免为了覆盖 12 个领域而平均分配词条。

工程演示版先发布 5–8 个有实质内容的节点；内容验证阶段逐步扩展到 20–30 个节点，其中至少 10 个具有较完整内容并经人工审阅。

当前 v0.1 首批目录：Cochlea（耳蜗）、Tonotopy（频位映射关系）、Auditory Filter（听觉滤波器）、Masking（掩蔽）、Temporal Envelope（时间包络）、Vocoder（声码器）、Speech Intelligibility（语音可懂度）、Cochlear Implant（人工耳蜗）。首批均标记 Draft，科学审阅由课题组成员后续完成。

以下为候选清单，不是三小时内必须全部完成的任务：

```text
Sound
Frequency
Decibel
Spectrum
Fourier Transform

Cochlea
Tonotopy
Hair Cell
Cochlear Compression

Auditory Filter
Critical Band
Masking
Pitch
Loudness
Temporal Resolution

ITD
ILD

Speech Spectrum
Formant
Voice Onset Time
Speech Intelligibility

Audiogram
Pure-tone Audiometry
Speech Reception Threshold

Hearing Aid
WDRC
Real-ear Measurement

Cochlear Implant
ACE
Channel Interaction

Vocoder

AI for Hearing
```

允许部分页面暂时只有简短内容，但必须标记实际状态。学习路径中的每个节点都应有可阅读的解释和有效链接。

---

## 13. 推荐额外创建的特色词条

为了体现 n³ Hearingpedia 的特色，可以加入：

```text
Atomic Speech
GET Vocoder
GEN Vocoder
Cochlear Implant Temporal Coding
Consonant Perceptual Space
Hidden Hearing Loss
Computational Audiology
Digital Hearing Health
```

这些词条可以形成与普通 Wikipedia 不同的特色。

---

## 14. Markdown Front Matter

每个词条使用统一 metadata。

实现中的字段与有效取值以 `src/content.config.ts` 为准：分类字段使用 `categories` 与领域 ID；关联项包含 `slug` 和 `relation`；`references` 使用 `src/data/references.ts` 中的文献 ID。下面的示例仅说明设计意图，新增实际词条时请复制已有 Markdown 词条。

例如：

```yaml
---
title: Auditory Filter
slug: auditory-filter

category:
  - Psychoacoustics

tags:
  - cochlea
  - masking
  - frequency-selectivity

level:
  - undergraduate
  - graduate

status: draft

last_updated: 2026-10-04
authors: []
reviewer: null
reviewed_at: null
literature_checked_at: null

related:
  - critical-band
  - masking
  - erb
  - cochlear-tuning

references: []
---
```

正式内容须填写实际作者和可核验参考文献；审阅者、审阅日期与文献检查日期仅在相应工作确实完成后填写。`last_updated` 表示词条修改时间，不等同于文献检索或科学审阅时间。

---

## 15. 页面状态系统

所有词条保留：

```text
Draft
Reviewed
Stable
Needs Update
```

页面顶部显示轻量状态标记。

例如：

```text
Reviewed · Updated Oct 2026
```

新建及 AI 起草的词条默认 Draft。Reviewed 必须有人工审阅记录；Stable 也不意味着无需更新。发现可能改变已有论断的新证据时，可标记 Needs Update 并建立更新草稿；未经审阅的新论断不得继续沿用 Reviewed 标记。

---

## 16. 搜索

第一版实现本地搜索。

推荐：

```text
Pagefind
```

搜索结果可以匹配：

- title
- text
- tag
- category

首页必须有搜索框。

---

## 17. Wiki Links

Markdown 中允许类似：

```text
[[Auditory Filter]]
```

如果实现成本高，可以第一版暂时使用普通 Markdown link：

```markdown
[Auditory Filter](/concepts/auditory-filter)
```

但代码结构应方便以后升级为 wiki-link。

---

## 18. UI 风格

整体风格：

**现代科学感 + 极简 + 高级 + 非传统 Wikipedia**

避免：

- 大量边框
- 老式 Wiki 排版
- Bootstrap 风格
- 企业官网风
- 过度渐变
- 过度动画

参考感觉：

```text
Notion
+
Linear
+
Arc
+
Nature / Science
+
modern AI product
```

---

## 19. Logo

文字 Logo：

```text
n³
```

下面或旁边：

```text
Hearingpedia
```

视觉中突出：

```text
n³
```

字体可以使用：

```text
Inter
或
system sans-serif
```

无需复杂图片 Logo。

---

## 20. 色彩

默认：

```text
white / off-white background
dark text
subtle blue / violet accent
```

支持：

```text
light mode
dark mode
```

如果 dark mode 会影响三小时目标，可以先不做。

---

## 21. 导航栏

顶部：

```text
n³ Hearingpedia

Explore
Map
Learn
Topics
About
GitHub
```

右侧：

```text
Search
```

---

## 22. Learn 页面

建立：

```text
/learn
```

第一版优先建立一条与课题组研究相关的完整学习路径，确保所有节点已存在；再逐步增加其他路径。以下为后续路径示例，并非首版必须全部实现。

例如：

### Hearing Science 101

```text
Sound
→ Cochlea
→ Auditory Nerve
→ Auditory Filter
→ Pitch
→ Loudness
→ Speech
```

### Cochlear Implant 101

```text
Cochlea
→ Hearing Loss
→ Cochlear Implant
→ Electrical Stimulation
→ CIS
→ ACE
→ Channel Interaction
```

### Psychoacoustics 101

```text
Auditory Filter
→ Masking
→ Loudness
→ Pitch
→ Temporal Resolution
```

---

## 23. Topics 页面

建立：

```text
/topics
```

显示专题。

例如：

```text
Cochlear Implants
Hearing Aids
Speech Perception
Psychoacoustics
Binaural Hearing
Audiometry
AI for Hearing
```

---

## 24. About 页面

说明：

n³ Hearingpedia 是：

> an open, AI-native knowledge infrastructure for hearing science.

强调：

```text
Open
Evidence-based
Human-reviewed
AI-assisted
Continuously evolving
```

可以写：

> AI helps organize knowledge. Humans remain responsible for scientific judgment.

说明项目从课题组成员的实际学习和研究需求出发，逐渐面向更广泛读者。Human-reviewed 描述审阅机制，各词条是否已审阅以页面状态和审阅记录为准。

---

## 25. Contributors

建立：

```text
/contribute
```

说明如何贡献：

```text
1. Fork repository
2. Add or edit Markdown
3. Add references
4. Submit Pull Request
5. Expert review
6. Merge
```

---

## 26. 文献原则

知识页面中的科学判断应该尽量对应可靠文献。

优先来源：

```text
Books
↓
Major reviews
↓
Peer-reviewed papers
↓
Consensus / guidelines
```

AI 生成内容不能作为引用来源。

文献使用区分两个层次：

- 基础概念、定义和经典机制以经典研究、教材及可靠综述为支撑。
- 研究进展根据近期相关文献持续补充，注明研究对象、方法、适用条件和证据局限。

不以发表时间作为唯一排序依据，不因单篇新论文直接覆盖已有共识。存在相互矛盾的结果时，说明差异与不确定性。

关键论断应对应具体引用。核对文献身份与文献是否支持该论断是两项不同工作；仅有摘要时，不据此补写未核实的实验细节。

---

## 27. AI 原则

第一版不实现真正 AI backend。

但是页面和项目结构必须为以后 AI 功能预留。

未来 AI 可以承担：

```text
Literature monitoring
Knowledge extraction
Draft generation
Reference verification
Outdated-page detection
Cross-link suggestion
Knowledge graph generation
```

基本原则：

> AI proposes. Humans approve.

### 从组内文献阅读逐渐发展为 AI 辅助更新

首版先由成员提供组会或课题相关论文，在成员发起的任务中使用 AI 辅助提取概念、整理证据和起草词条，无需自动抓取或模型后台。

后续在流程成熟后，再增加按主题跟踪近期文献的能力。检索主题来自课题组研究方向及现有词条，记录检索日期和覆盖范围，避免将有限检索表述为覆盖所有最新研究。

更新流程：

```text
成员提供论文 / 后续文献检索
↓
核验文献信息，筛选相关证据
↓
映射到现有概念，识别需要新增的概念
↓
生成更新草稿、逐项引用和变更说明
↓
课题组成员审阅科学判断
↓
合并发布，保留版本历史
```

每个更新草稿说明：涉及哪个词条、准备修改哪项论断、对应哪篇文献及其具体证据、有哪些适用条件或待核实问题。

优先补充研究进展、边界条件和跨词条关联；基础解释仅在证据充分且经审阅后修改。若新增实质内容，审阅记录必须对应更新后的版本。

先由维护者协调作者与审阅成员，明确词条责任；更新能力逐步增加，本方案不代表已经启用自动检索或定时更新服务。

---

## 28. Interactive Lab 预留

所有知识页面允许出现：

```text
Try it
```

入口。

未来指向：

```text
/lab/*
```

例如：

```text
/lab/auditory-filter
/lab/masking
/lab/itd
/lab/cochlear-implant
```

这是未来“听觉版 PhET”的入口。

第一版只需要一个：

```text
Interactive Lab — Coming Soon
```

页面。

---

## 29. 推荐目录结构

```text
n3-hearingpedia/

README.md
PROJECT.md

src/

  pages/
    index.astro
    explore.astro
    map.astro
    learn.astro
    topics.astro
    about.astro
    contribute.astro

  content/

    concepts/

      sound.md
      frequency.md
      decibel.md
      cochlea.md
      auditory-filter.md
      masking.md
      pitch.md
      itd.md
      cochlear-implant.md
      ace.md

  components/

    Header.astro
    Footer.astro
    ConceptCard.astro
    TopicCard.astro
    RelatedConcepts.astro
    ReferenceList.astro

  layouts/

    BaseLayout.astro
    ConceptLayout.astro

public/

  images/
  favicon.svg

.github/

  workflows/
    deploy.yml
```

---

## 30. GitHub Pages

必须配置 GitHub Actions。

目标：

```text
git push
↓
GitHub Action
↓
build
↓
deploy
↓
GitHub Pages
```

README 中写清楚部署步骤。

---

## 31. README

README 至少说明：

```text
What is n³ Hearingpedia?

Why does it exist?

How to run locally?

How to add a concept?

How to deploy?

How to contribute?
```

---

## 32. 第一版验收标准

工程演示版 v0.1 完成时必须满足：

- [ ] 首页可以正常打开
- [ ] `n³ Hearingpedia` 品牌显示正确
- [ ] 有 12 个知识领域
- [ ] Explore 页面可用
- [ ] 有 5–8 个与课题组需求相关且有实质内容的知识节点
- [ ] 词条状态真实，未审阅内容标记 Draft
- [ ] 每个 concept 有统一 layout
- [ ] Markdown 可直接新增页面
- [ ] KaTeX 数学公式正常
- [ ] Related Concepts 可以跳转
- [ ] Knowledge Map 页面可用
- [ ] Learn 页面有一条可连续阅读、节点完整的学习路径
- [ ] 搜索可用
- [ ] 手机端正常
- [ ] GitHub Pages 自动部署
- [ ] README 完整
- [ ] 不存在明显 placeholder / broken link

后续内容验证阶段完成：

- [ ] 扩展到 20–30 个知识节点
- [ ] 至少 10 个词条有较完整内容并经人工审阅
- [ ] 关键论断可追溯至具体参考文献
- [ ] 有实际作者、审阅者及相应日期记录
- [ ] 用组内文献完成一次 AI 起草、成员审阅、合并发布的更新流程
- [ ] 根据课题组成员使用反馈修正解释与关联路径

---

## 33. 三小时开发顺序

### Phase 1 — 0–30 min

完成：

```text
Astro project
layout
CSS
navigation
GitHub Pages config
```

### Phase 2 — 30–75 min

完成：

```text
Home
Explore
Topics
About
Learn
```

### Phase 3 — 75–120 min

完成：

```text
Concept content collection
Concept template
5–8 substantive concept pages
Related concepts
KaTeX
```

### Phase 4 — 120–150 min

完成：

```text
Knowledge Map
Search
Mobile layout
```

### Phase 5 — 150–180 min

完成：

```text
QA
fix broken links
README
GitHub Action
deploy
```

---

## 34. 如果时间不足

删除优先级最低功能：

```text
dark mode
animations
advanced graph
complex search
interactive demos
```

绝对不能牺牲：

```text
首页
知识结构
concept 页面
导航
移动端
GitHub Pages 部署
```

---

## 35. Codex 工作方式

不要一次生成大量复杂代码。

采用：

```text
implement
→ run
→ inspect
→ fix
→ continue
```

每完成一个模块：

1. 启动本地服务器
2. 检查页面
3. 检查 console
4. 检查 link
5. 再继续下一阶段

如果某个 dependency 导致问题：

**立即替换为更简单方案。**

不要为了某个库浪费大量时间。

---

## 36. 内容质量

不要生成大量“AI味百科文字”。

优先：

```text
short
clear
visual
conceptual
connected
```

每个词条首先回答：

> What is the idea?

然后回答：

> Why should I care?

最后再进入：

> What does the science say?

---

## 37. 长期愿景

网站未来可以演化为：

```text
n³ Hearingpedia
        │
        ├── Knowledge
        │
        ├── Learn
        │
        ├── Lab
        │
        ├── Literature
        │
        ├── Knowledge Graph
        │
        └── AI Tutor
```

最终目标不是：

> a website about hearing

而是：

> **an open knowledge operating system for hearing science.**

---

## 38. 最重要的产品原则

始终保持：

> **One concept, one beautiful page.**

以及：

> **Every concept should connect to another concept.**

最终让 n³ Hearingpedia 从一个静态百科逐渐成长为：

**可以阅读、可以学习、可以实验、可以探索、可以研究的听觉科学知识网络。**

---

## Codex 最高优先级指令

> **先完成一个真正可部署的 v0.1，不要在任何单项功能上过度开发；3 小时后必须有公网 GitHub Pages 可访问版本。**
