# 八个核心词条与时域线索定义修订：发布记录

2026-10-06，根据用户“开始推送这些未推送的内容”的确认，将掩蔽、响度、空间听觉、声码器、听力损失、基频、频位映射关系、听觉诱发电位八篇审阅稿整合到正式网站，并同步时域包络、时域精细结构的定义澄清。

八篇均有独立的“计算模型与公开实现”小节。空间听觉采用“优先效应”，扩写其融合、定位主导和辨别抑制；响度增加等响曲线，基频增加真实语音的波形、语谱、基频和谐波对照。两篇时域线索词条先定义一般信号，再说明分频分析，避免将指定频带写为概念成立的前提。

## 文献与发布转换

`draft-evidence-records.json`保留本批使用的书目和实际阅读范围，`reference-id-map.json`记录审阅稿ID与站点ID的对应。同一来源复用站点既有记录，保留此前核验范围；50项新增来源集中于`src/data/core-eight-references.ts`。`research-notes.md`与`revision-audit-2026-10-06.md`是发布前各阶段的历史记录，其中原始检索工作文件路径指本地审阅目录，不表示这些工作副本也已公开。

正式词条移除本地审阅提示和重复参考文献段，使用站点统一书目与上标。图片转换为可点击的百科图框，保留说明和来源。基频补回原词条的两项研究线索，以免扩写时丢失原有文献关联；不把声码器实验写成真实植入者验证。保留专业审阅状态，不把授权发布视作具名同行审阅。

## 配图与复现资料

26幅新图的SVG与PNG位于`public/figures/core-eight/figures`。原24幅教学图可由`generate-figures.py`生成；等响曲线与语音图由`additions/build-supplementary-figures.py`生成。依赖Python、NumPy、SciPy、Matplotlib；后者另需SoundFile和praat-parselmouth。脚本默认使用Windows微软雅黑，其他系统需修改字体路径。

等响曲线依据ISO 226:2023公开预览公式与参数计算，不代表个体常模。未公开标准PDF。真实语音来源为LibriSpeech / librosa libri1，朗读者Garth Comira，CC BY 4.0；保留原始音频、裁剪片段、许可和处理记录。波形峰值归一化至0.98，基频轨迹是算法估计而非人工标注真值。数据、参数和文件哈希见`additions/supplementary-figure-provenance.json`。

发布检查包括Astro类型检查、完整构建、全站链接与引用校验，以及十篇页面的桌面和移动端图片、上标、公式及布局检查。正文数量和引用数量见`publication-manifest.json`。
