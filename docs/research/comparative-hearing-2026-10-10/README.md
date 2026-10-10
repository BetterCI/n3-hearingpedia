# 比较听觉：研究与交付记录

2026-10-10。正式词条名为“比较听觉”，主题为动物听觉对人类听觉研究的启示。新稿保持 Draft，尚未完成具名专业审阅。

## 问题与范围

比较仓鸮的双耳时间计算与空间校准、蝙蝠的主动回声定位、寄生蝇鼓膜耦合以及鸡和鹌鹑的毛细胞再生。以哺乳动物生理、人体行为和工程器件作为外推对照。主体证据从1988年起；近期发展按2021-01-01至2026-10-10检索和筛选，最终所选近期研究发表于2021—2025年。不声称2026年没有其他相关研究。

收录条件是来源能够支持某个具体机制、实验结果、比较限制或应用验证阶段。保留成年小鼠重编程中的有限结果。排除新闻、社交媒体转述、单纯听觉能力排名，以及与四组案例无直接关系的泛神经网络或其他感觉系统研究。

## 检索与选文

按 deep-research 技能运行 OpenAlex 客户端，主题查询为 `comparative hearing sound localization hair cell regeneration`，保留8项；从Carr与Konishi（1990）、Robert等（1996）、Ryals与Rubel（1988）三个强种子各展开至多8项后向和8项前向文献，保存原始记录。前向按引用次数取有限候选，只作为发现路径，不作质量判断。主题池偏向再生，前向池包含广义时序研究，故补充定向检索仓鸮、人类回声定位、仿生MEMS和成熟小鼠再生。没有继续第二层扩展。

三个种子及引用网络分别保存在 `owl-*`、`fly-*`、`bird-*` JSON；主题与网络候选按DOI、OpenAlex ID、题名顺序去重，得到55项，见 `candidate-pool.json`。逐项语义筛选见 `candidate-screening.json`，根据有无摘要据实记录判断范围；此池为发现材料，并非55篇都完成全文审阅。通过技能 `judge_relevance.py` 生成统一判定提示，保存在 `relevance-prompt.txt`。定向检索最终选入17项来源，逐项的研究对象、访问范围、引用用途和选择理由见 `source-ledger.json`。

网络发现中的个别书目关联出现年代或主题异常，例如1990年论文的后向结果包含2012年的科普题名；未据此建立科学沿革，也没有用引用网络替代原研究核验。所引用的题名、作者、期刊、页码与摘要用Europe PMC核心书目和PubMed或出版社页面交叉核对。Konishi（2000）的一次DOI查询未命中，改用PubMed PMID 10989338的记录。

定向查询包括：`Study of sound localization by owls and its relevance to humans`、`A neural code for low-frequency sound localization in mammals`、`Visual instruction of the neural map of auditory space`、`How frequency hopping suppresses pulse-echo ambiguity in bat biosonar`、`Human click-based echolocation 10-week`、`Ormia mechanical coupling`、`hair cell regeneration adult 2025`。浏览器反爬页面和XML访问失败记录为不可访问，未声称绕过限制或读到失败全文。

## 证据主题与边界

仓鸮延迟线、符合检测和经验校准为机制实验；豚鼠下丘和人类双耳去掩蔽模型构成对照。符合检测与输出读出分层说明，不把模型成功写成唯一人类神经实现。

蝙蝠的频率归属研究包含行为与模型；群体回声检测是生物参数约束的计算预测。人类10周训练是独立的人体证据，两组年龄与听觉条件、任务熟悉及自述随访限制均保留。作者代码归档仅核验关联，没有运行。

寄生蝇原研究说明声学输入与机械响应的差异。2016年窄带器件报告实际制作测量；2025年多频带结构报告有限元仿真。两者不合并为已证实的助听器收益。

鸟类再生的细胞证据与功能恢复分开解释。2025年成熟小鼠研究中双标志细胞增加，报告时点的Myo阳性毛细胞数量并未显著不同；不据此宣称听力恢复或人体疗效。鸟类细胞与人类内、外毛细胞功能不直接等同。

全文访问成功的相关来源为人体训练（2021）、双通道模型（2022）、仓鸮可靠性（2023）、MEMS实物（2016）、MEMS仿真（2025）及鸟类细胞再生综述（2000）。前五项XML与分段文本保存在对应 `PMC*-text.json`；再生综述通过作者机构公开PDF核对相关段落，原XML访问失败记录保留。其余来源按摘要范围使用，未引用未核验的实验参数或逐图数据。综述中的原始功能研究尚未逐项复核，属于后续专业审阅的可扩展方向。

## 图与交付

三张图均为原创：证据路线、修复评价框架和传播时间计算；没有转载论文图或用AI生成解剖图片。`figure-manifest.json`记录性质与参数，生成脚本包含教学计算断言，PNG已逐张视觉检查。图3采用统一对数纵轴比较两种接收间距，避免不同纵轴造成幅度比较歧义；18 cm是教学设定，0.52 mm引用寄生蝇耳间距资料。

正式源文件：`src/content/concepts/comparative-hearing.md`。独立阅读预览与审阅稿位于 `docs/drafts/comparative-hearing-preview.html` 和 `docs/drafts/comparative-hearing-review-2026-10-10.md`，预览资源置于对应 `assets/comparative-hearing`。增加动物模型小节后共登记25项来源、12条可双向遍历的概念联系及一条学习路径，并更新本词条的证据映射。

## 动物模型小节增补

根据用户后续要求，在研究范围之后、四组详细案例之前增加“听觉研究中的常用动物模型”。表格列11组研究对象：小鼠、大鼠、豚鼠、蒙古沙鼠、南美栗鼠、猫、鸟类、蝙蝠、斑马鱼、昆虫及非人灵长类。每行说明研究用途、优势或实例，以及比较和人体外推的限制。随后说明具体模型需注明品系、基因型、年龄、基线听力、诱导或干预方式及测量终点。侧线与内耳、鸣唱与语言、电刺激表征与儿童语言收益均作区分。

这是针对模型概览的定向增补，没有重跑原55项候选池，也不声称全面覆盖所有动物模型。补充查询涉及 `animal models hearing research mouse gerbil guinea pig chinchilla`、`Drosophila genetic screen hearing Eberl 1997`、`Bendor Wang 2005 pitch marmoset`、`zebrafish lateral line hair cell screen`、`Brainard Doupe auditory feedback 2000` 和 `cat cochlear implant inferior colliculus Snyder 1990`。最终新增8项来源：3篇模型综述用于概览，5篇原研究用于猫、鸣禽、绒猴、斑马鱼和果蝇的具体实例。综述归为Background，原研究归为Core；判断范围与用途见更新后的 `source-ledger.json`。

`animal-models-metadata.json`保存Europe PMC核心书目与摘要及全文访问结果，生成脚本为 `scripts/research-comparative-hearing-models.py`。南美栗鼠综述和斑马鱼原研究的全文XML及文本保存为 `PMC6881193-models.*`、`PMC2265478-models.*`；阅读相关段落核对表格用途、频率范围和侧线感受功能。果蝇XML访问失败后阅读作者机构公开PDF，核对触角、行为遗传筛选及听觉特异性限制。小鼠综述按PubMed摘要和图注使用；啮齿类综述及猫、斑胸草雀、绒猴原研究按摘要使用。没有从失败全文中引用实验参数，也没有逐项复核综述中的所有原始研究。

本次增补重新生成独立预览、审阅稿、来源账本与证据映射，编号引文和内容Schema检查通过；浏览器复核新增表格的桌面与窄屏布局。此增补阶段只执行本词条检查，后续全站发布校验见下节。

## 工程验证与限制

`node scripts/render-comparative-hearing-draft.mjs`对本词条执行生产内容Schema、编号引文、参考锚点、概念链接、资源、KaTeX公式、知识关系及学习路径检查；结果见 `verification.json`。独立预览的1280像素桌面与390像素窄屏检查见 `site-checks.json`。图、公式与正文保持页面范围，表格在自身容器横向滚动。

`pnpm check`和`pnpm build`均被工作区既有Albert Bregman人物词条的`kind`与当前内容Schema不匹配阻止，错误发生在内容同步阶段。未修改该人物词条或扩展其类型，也未将新词条标为全站构建通过。构建未完成，因此没有在旧产物上运行`pnpm verify`或将其结果当作新词条验证。初稿阶段未提交、推送或部署，后续发布校验见下节。

AI用于检索组织、正文起草、来源整理、原创教学绘图和技术检查；来源核验、自动检查和视觉检查不代替专业科学审阅。

## 发布校验（2026-10-10）

用户要求推送后，以远端主分支 88bfd0c7bc302d71b3451a88faa2af074f9425fd 创建独立工作区，只迁入本词条、图片、研究与预览文件，以及参考文献、关系、路径和README中的对应增量。保留远端其他更新和原工作区未提交内容。当前主分支已支持人物类型，因此初稿工作区的Schema阻碍不再出现。

pnpm install --frozen-lockfile --prefer-offline成功；本词条引用、资源、概念链接与完整内容Schema重新验证通过；pnpm check检查121个文件，0 errors、0 warnings、0 hints；访客统计4项既有测试通过；pnpm build成功并生成正式词条路由和搜索索引；pnpm verify检查224个页面、17708个内部链接，brokenLinks为0。结果见更新后的 site-checks.json。推送目标为origin/main，仍保留Draft与尚未完成具名专业审阅的状态。

首次推送前远端新增纯音与复合音、赵元任两个提交，正常推送被非快进检查拒绝。将本提交变基到 5ddd7ad，保留远端内容，仅重新应用本词条参考登记、12条关系和证据映射增量。随后重新通过全站检查（124个文件、零错误）、构建与验证（226个页面、17942个内部链接、零断链、96个可检索词条、539条关系）。

网络连接恢复前，远端继续发布六个听觉感知词条；再次变基至 88482b8197dd4ac776f4544a183009cdf4354e07，保留全部远端更新并重新应用本词条的登记增量。最后一次检查136个文件，零错误；构建通过；验证238个页面、19417个内部链接、102个可检索词条、641条关系，零断链。GitHub API备用上传只创建了内容对象，因远端已改变而停止，未移动主分支或覆盖更新。
