# 《语音冗余性》检索与证据边界

日期：2026-10-09。目标是百科深度词条，不是系统综述或临床建议。范围为声学线索、语言约束、信息重复／互补／协同、时频删减、恢复及听者利用；近期观察范围为2023-01-01至2026-10-09，同时纳入经典原始研究。

## 检索与筛选

- OpenAlex主题查询：`speech redundancy phonemic restoration`，返回前8项。
- 强种子：Leonard等2016，DOI `10.1038/ncomms13619`，OpenAlex `W2563866812`。向后和向前各取12项；前向结果是有限返回窗口，不是全部引用或全部近期研究。
- 用deep-research的judge_relevance脚本生成种子评估提示，再按实际摘要和任务相关性人工筛选。无摘要者只标为待核查背景，不由标题推出结果。
- 补充定向检索：`speech redundancy acoustic linguistic context spectral temporal information phonemic restoration review`；`phonemic restoration cochlear implant users 2024 2025 2026`；`Miller Licklider 1950 interrupted speech DOI`；`Spectral redundancy Warren Bashford 1995 DOI`；`Perceptual restoration of masked speech Leonard 2016`；`site.aclanthology.org time scale of redundancy 2025`；`Quantifying the redundancy between prosody and text`；`Pitch and spectral resolution Clarke DOI`；`Missing phonemes are perceptually restored doi authors`；`Shannon 1948 A Mathematical Theory Communication pdf mit`。
- 发现平台只用于找文献；正文依据原始摘要、作者机构或作者公开全文、官方ACL正式会议论文和既有已核对来源。未引用ResearchGate、第三方综述页或搜索摘要拼接出的实验结果。
- 以DOI去重，复用7个既有引用ID，新增11个。将既有Shannon1948条目从metadata更新为实际核对的fulltext，并保持原ID。

## 主题证据与选择

1. Miller1950：直接操纵中断速率、比例和噪声操作；读取原始PDF摘要及静音中断方法。作为Core；不移植原样本的普遍阈值。
2. Warren1970：噪声替换与静音替换的音位恢复，Core；仅用已核对摘要。
3. Boothroyd1988：音位／词／句子与语境概率关系，Core；公式在原始摘要可核对。参数0.4与2为自拟教学值，非拟合结果。
4. Warren等1995：窄带句子及组合效应，Core；仅用摘要，避免搬用无法完整核对的滤波细节和全部数据。
5. Shannon1948与Schneidman2003：信息定义和线索关系的Background理论。三种离散模型、熵值和门控条均为原创教学计算，不能宣称复现人类实验。
6. Shannon等1995与Kong2006：特定声学线索／任务利用，Important；解释声码器保留与声调任务依赖，不宣称固定通道数适用于所有语言。
7. Bhargava2014、Clarke2016、Benard2015：真实CI、声学模拟、音高／谱分辨和视觉输入，Important；保留整体识别、连续感和恢复差值之间的分离结果。
8. Leonard2016：人体直接皮层记录与恢复，Core；读取Abstract、Introduction及实验词对说明，不把关联记录当作完整因果机制。
9. Ishida2016：母语／二语、词／非词、噪声叠加／替换及相似性任务，Important；经Europe PMC原始XML读取摘要、任务和Results。
10. FUEL2016：聆听努力框架，Background；正确率不代表全部资源投入。
11. Kates2023：语境与关键词／句子预测模型，Important；复用已核对全文条目，本次PMC正文访问遇到验证码，未声称重新读完全文。
12. Wolf2023、Regev2025：韵律与文本的估计互信息，Core；官方正式版本，非仅引用预印本。2025原始PDF读取方法、结果和Limitations；朗读语料、特征和模型估计不能直接证明人类记忆或恢复。
13. Kong2025：稀疏时频表示和跨耳分配，Important；原始摘要支持整合条件及个体差异，不把原子当比特。

逐条访问等级、DOI与正文支持位置见`selected-evidence.json`；OpenAlex池的筛选结论见`discovery-screening.json`。完整下载和原始返回保留在忽略目录`artifacts/redundancy-research/`，不作为出版附件。

## 访问和停止条件

PMC部分HTML遇到验证码，部分Europe PMC全文接口返回500；未绕过验证或把失败访问记作全文阅读。原始Miller PDF和ACL2025 PDF成功下载并以pdftotext读取。Clarke作者PDF本轮超时，保持abstract等级。Warren1970的PubMed摘要通过索引和种子后向记录交叉核对。

不继续扩展：第一轮网络已经覆盖中断、恢复和神经语境；其余多为广泛预测理论、视觉哲学、语音网络综述或临床解码，并不添加本篇必要的直接行为证据。补充定向检索补足谱删减、听者及近年韵律／模型方法。有限检索不保证穷尽2026年发表内容。

## 尚需专业审阅

术语“冗余”的宽义与严格信息论义需要持续分开；行为协同不自动等于信息论协同。中文示例与原创离散算例不是普通话实测数据。本地稿保持draft、reviewer=null、reviewed_at=null。用户要求确认后才上传，本轮不提交、不推送。
