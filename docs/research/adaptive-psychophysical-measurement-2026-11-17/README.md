# 自适应心理物理测量：编写与核验记录

日期：2026-11-17。基于远程主分支3054fa9在独立发布工作树编写，未纳入原工作目录的其他修改。

## 内容范围

9节正文、9项来源、2张原创数值教学图；涵盖目标概率、阶梯状态、反转、步长、边界、贝叶斯更新、QUEST/Psi/QUEST+、停止与估计，以及言语和辨别任务的限制。保留Draft，工程与AI内容核查不冒充具名专业审阅。

## 来源范围

本轮打开Levitt原文公开PDF、Watson与Pelli作者PDF、Kontsevich与Tyler公开PDF、Soranzo与Grassi原刊全文、Shen 2013 PMC原文及PsychoPy官方API。QUEST+只核对原始摘要索引，出版方全文403，PubMed直接打开不完整，因此只引用其方法范围。既有Shen与Richards、Wichmann与Hill来源沿用注册表已有核验记录。没有声称穷尽最新研究或执行第三方心理物理工具包。

原文入口及逐项访问范围见词条references和主题参考表；既有同一文献复用ID。

## 数值与图示

public/code/adaptive-psychophysical-measurement/simulate.py保存参数、种子、逐试次CSV、500次估计与results.json。反函数核验、常数正确率下20万试次更新方向比例核验及直方图计数检查通过。真实70.7%阈值为−6.551692 dB SNR；500次成功、0失败；偏差−0.405308 dB、标准差1.917029 dB、RMSE 1.957530 dB。固定2 dB步长、100试次、最后8反转平均是教学设定，不是实验通用处方。

复核修正直方图初始固定横轴遗漏尾部的4个估计，改用全范围分箱并断言计数和等于成功数。查看PNG确认中文、坐标、图例与图注一致。

## 工程与页面检查

- pnpm check：0 errors、0 warnings、0 hints。
- verify-basilar-membrane及CI现有20项测试通过。
- pnpm build和pnpm verify通过；最终统计见构建输出。
- 本地浏览器检查桌面标题、目录、正文及窄屏页面；窄屏DOM宽度与滚动宽度均375，无横向溢出，KaTeX错误节点为0。
- 新增6条知识关系、一条学习路径和心理测量函数的反向正文入口，更新证据映射与自动统计。

补充检查：旧版verify-source-content.mjs在既有mathematical-statistics词条因禁止“组内”的宽泛正则而失败（会匹配统计术语“组内相关”）；该文件与既有词条不属本次修改，未更改。生产构建验证通过，354页、31,454个内部链接、0断链。推送前远程增加5490bd2微信入口更新，本词条提交将重放在该更新之后。

重放5490bd2后最终验证：pnpm check为262文件、0错误、0警告、0提示；pnpm build成功，pnpm verify为354页、33,153内部链接、157词条、0断链。git diff --check通过。
