# 《相位锁定》深度词条研究记录

核验日期：2026-10-10。沿用 `phase-locking` 和《相位锁定》，增加“神经锁相”“神经相位锁定”别名。由既有基础稿扩展，不另建重复概念。参照贡献规范、深度词条模板及《频率分辨率》等成熟词条；重点是外周机制、统计方法、实验控制、分析算例和感知应用。

## 检索与筛选

- 种子文献：Rutherford、von Gersdorff与Goutman（2021），DOI `10.1113/JP279189`；OpenAlex `W3134091674`。
- 查询主题：auditory nerve phase locking vector strength；human temporal fine structure phase locking；auditory phase locking envelope binaural；phase locking hearing 2024 2025 2026。
- 通过OpenAlex抽取8篇后向与8篇前向文献，依据正文问题进行语义筛选；这是一轮有范围的引文扩展，不声称遍历全部引文网络。
- 历史定位：Rose等1967、Goldberg与Brown1969。只核对正式书目，未据题名补写数值或具体实验结果。
- 机制和方法：Heil与Peterson2015、Rutherford等2021、Peterson与Heil2020、Vinck等2010；保留事件数、独立性、多峰和平均方向的解释。
- 感知与测量：Cariani与Delgutte1996、Joris等2004、Joris与van der Heijden2019、Verschooten等2018/2019、Coffey等2019，以及双侧人工耳蜗动物实验。
- 近期范围为2024-01-01至2026-10-10。纳入Saddler与McDermott2024的正式论文（PMC11618365），Heeringa等2025，Ashida2026。Saddler同研究预印本PMC11071365不另计证据。
- 扩展命中的离子通道、带状突触、遗传和光遗传论文作为背景筛选；不为增加引用数量展开本词条未讨论的分子机制。前庭非量子传递工作因对象不同排除；皮层theta同步与听神经载波锁相不作为同一证据对象。

原始题名、DOI、正式URL、访问层级与本词条支持范围见 `source-ledger.json`。OpenAlex原始响应与全文临时缓存位于忽略的 `artifacts/phase-locking-2026-10-10/`，不作为网页图片或公开附件。

## 可访问性与证据层级

通过Europe PMC公开全文XML选读Verschooten2018/2019、Coffey2019、Saddler2024、Heeringa2025和Ashida2026的相关方法、结果与讨论段落；未声称每篇全文逐字通读。Rutherford2021、Peterson2020和部分Delgutte论文的本轮全文请求出现HTTP 500，因此本轮使用可核验原始摘要；Rutherford的共享书目保留既往全文核验记录。本词条的实际读取范围另行记录，不覆盖其他词条的核验历史。

动物单纤维记录、人类复合电位、头皮FFR、心理物理行为和计算模型分别表述。人类锁相的可用上限保留刺激、任务和推断方法的分歧；不提供统一诊断阈值或人工耳蜗临床参数。较大向量强度不直接等于较好行为成绩。

## 算例与图示

四图均为原创教学计算，非真实神经记录或论文图复刻。脚本 `scripts/generate-phase-locking.py`、事件文件 `teaching-events.npz`、参数和环境版本 `figure-parameters.json` 可复算。保持两组事件数和观察时长相同；另比较固定延迟、独立高斯抖动、一阶平均向量和相反双峰。高斯抖动曲线来自特征函数解析关系，未拟合生理截止频率。

PPC与R的关系从不同事件对余弦均值进行代数展开；对总体估计的解释明确限定独立同分布，不能忽略试次内相关。未运行完整AMT听觉模型或MNE分析，仅阅读官方方法文档并运行原创NumPy/Matplotlib教学脚本。

## 本地审核状态

保留Draft、空reviewer和reviewed_at，待专业审阅。新增机制/概念联系及江渊声、Delgutte、Jeffress人物入口。保持已有未发布词条与其他本地改动；本次只同步相位锁定内容及其直接依赖，不提交或推送。
