# 心理测量函数：检索、论断与发布核查

日期：2026-11-06（Asia/Shanghai）。目标：新建可独立阅读的中文深度词条，解释行为概率曲线、参数与单位、阈值、采样、拟合、不确定性和听觉应用。状态保持 Draft；AI 核查不填写专业审阅者。

## 检索与取舍

采用 deep-research 技能：OpenAlex 主题检索 `psychometric function estimation lapse rate`，保留16条发现记录；以 Wichmann & Hill 2001 I（W2035912487）为经典种子，向后与向前各取15条记录。原始结果分别在 `openalex-search.json`、`openalex-backward.json`、`openalex-forward.json`。它们是有限结果窗口，不代表全部引用网络。

使用技能的 judge_relevance.py 为 quickpsy 候选生成 `screening-prompt.txt`，再按摘要所研究的问题、方法与本文关系进行人工语义筛选。证据重点为1971—2018年的方法及实证，另核查截至2026-11-06可访问的官方工具说明；没有把本次检索称为最新论文综述。

核心：Wichmann & Hill I/II（统计模型、拟合、区间）；Schütt 等（额外离散）；Prins 2012（失误率偏差的复核）；Shen & Richards 2012及Shen 2013（听觉任务、参数采样与程序比较）；Prins & Kingdom 2018（共享参数与模型比较）。

重要：Stanislaw & Todorov（任务与判据），Levitt和QUEST（刺激选择背景），Wallis等（视觉跨时段汇总的具体实证及其有限影响），quickpsy与psignifit（独立工具的参数定义和推断实现），PSYCHOACOUSTICS（听觉任务实现）。

背景或暂不纳入：一般bootstrap和GLM教材属于前置统计；非参数或高斯过程论文值得后续专题展开，本篇只说明一维参数模型的边界。部分仅有题名或缺少可读摘要的候选未据此添加研究结果。虚拟现实渲染、橡胶手和嗅觉/运动任务等前向引用主要使用该方法，而非直接研究本篇的核心估计问题，排除其应用结果。继续扩张主要增加相近方法或其他感官应用，且当前提纲已有不同团队的直接材料覆盖，因此本轮不做第二层扩张。

## 论断与来源对应

| 论断或处理 | 直接依据 | 核查限制 |
| --- | --- | --- |
| 条件反应概率、上下渐近线、二项似然 | Wichmann & Hill I；quickpsy原刊 §1 | 逻辑斯蒂逆函数和导数由本篇独立推导 |
| 原始概率与归一化阈值不同 | psignifit Get thresholds and slopes / Change the threshold percentage correct | 文档是latest快照，不据其字段名推定其他版本参数化 |
| 上端错误概率不同于走神事件比例 | 本文随机猜测混合推导；quickpsy §1.2 | 仅限规定的随机脱离任务机制，不做注意诊断 |
| 忽略失误可能偏倚；放开参数不保证消偏 | Wichmann & Hill I；Prins 2012摘要、作者说明 | 不给出统一先验、试次数或采样配方 |
| 参数bootstrap与采样布局 | Wichmann & Hill II；本文固定设计复算 | 分位区间不当作已验证覆盖率，同时带与逐点带区分 |
| 额外离散与状态变化 | Schütt等2016相关章节 | 不由额外参数唯一定位生理/行为原因 |
| 多参数的信息位置、自适应程序比较 | Shen & Richards 2012相关段落；Shen 2013摘要 | 不将其听觉任务结果推广为普遍算法排序 |
| 跨时段合并可影响斜率 | Wallis等2013摘要；本文概率混合计算 | 原研究所测非稳定性小、两种估计差异可忽略；教学图不复现原数据 |
| 参数共享和模型比较 | Prins & Kingdom 2018相关章节 | 共享假设需对应科学问题，本文未运行Palamedes |

已有来源复用原ID，新增来源在 `src/data/psychometric-function-references.ts`。六项新增论文的Crossref题名、作者、卷期等均返回200，见 `bibliographic-check.json`。Leek来源另据PubMed原始摘要与书目。quickpsy的网页日期2015-11-08与期刊年不同，采用DOI及期刊2016口径；Shen 2013的卷期核为75(4)，没有把页码771误配到第3期。Wallis采用2013期刊年，并保留在线2012的说明。

## 访问范围与未使用材料

`access-log.json`记录直接HTTP访问：psignifit两页成功；Palamedes官网模型比较页返回403；部分PubMed请求返回Cookies中间页。必要内容用已核实的原始摘要、原刊或官方文档交叉补足，未将拦截页当作原文。Palamedes官网不单列为“已读”来源，工具介绍和方法以2018原刊为依据。既有全文文献的supports保留其原有阅读记录，本轮不宣称重新通读全部旧文献。

没有运行psignifit、Palamedes、quickpsy或真实听觉实验。实际运行的是公开教学脚本，使用NumPy、SciPy与Matplotlib。

## 公式与数值核查

运行 `python public/code/psychometric-function/demo.py`：

- 检查逆函数代回、解析导数与数值差分、单调性、上下渐近线和含二项组合数的似然。
- γ=0.5、λ=0.02、α=−6、β=1.5时，原始74%、75%、90%对应−6、−5.8749275866、−3.5858431313 dB SNR；中点斜率0.08/dB。
- 200次模拟反应，五水平各40次，计数为25、21、32、37、38；拟合α=−6.54666、β=1.88404，75%阈值−6.38957 dB SNR。
- 400次固定设计参数bootstrap：阈值分位区间约[−7.97976,−4.91813]，4份拟合触及边界。正文已说明约束影响及未验证覆盖率。
- 混合两条位置不同的曲线，在中心处导数为0.03359795/dB，低于单一中间位置曲线0.08/dB；不将平均曲线声称为同一逻辑斯蒂族的精确成员。

完整结果在本目录及 `public/figures/psychometric-function/numerical-checks.json`。四图保留SVG、PNG与生成脚本；图2的邻近阈值标签经视觉检查后分开，曲线增加线型区别。代码和数据均为原创教学构造，未复制论文图或参与者数据。

## 网站接入与检查

新增7条知识关系，加入methods学习路线；在心理声学、信号检测论、言语接收阈和言语可懂度中各增加一处导读链接，保持既有标题与章节锚点。同步证据映射和README统计。修正本篇复用的Wichmann I书目中的字面`&amp;`并补卷期页码。

工程检查与发布结果见 `validation.json`。先执行pnpm check、build、verify，再按最终文件变动重建。桌面及390像素手机视图已检查：4图、10章，无KaTeX错误，长公式在公式框内横向滚动，整页不横向溢出。确认提交范围后推送main；最终部署与线上结果另据实际返回记录，不由本说明预先认定成功。
