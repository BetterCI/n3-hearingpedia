# 波动方程与亥姆霍兹方程：起草与核验

日期：2026-10-29。按用户补充，将主题组织为两篇互链的深度词条，默认 Draft，未进行具名专业审阅，经科学复核修正后，按用户指令提交发布；仍保留 Draft 标记。

## 内容分工

- 波动方程：守恒推导、初态与双向传播、边界反射、能量、时域离散、传播时延和频域联系。
- 亥姆霍兹方程：单频相量、源量纲、阻抗与辐射、模态与受迫响应、格林函数、有限元／边界元及听觉应用。
- 统一采用 exp(jωt) 和峰值声压相量；实际压力取实部，纯正弦有效值另除以√2。

## 来源核验

本次为针对性教学与方法来源核验，不是系统文献综述。`source-ledger.json` 保留逐来源访问范围及用途；复用两项既有MIT声学讲义，新增九项来源。检索采用大学、作者或软件维护者原始页面，不以第三方百科作科学依据。

检索线索包括 acoustic wave equation、Helmholtz boundary conditions、FEniCSx Helmholtz、Bempp Green representation、k-Wave first order、thermoviscous acoustics，以及MIT wave finite differences。Demanet 2016讲义先经公开网页核对，再临时提取PDF文字，重点阅读1.2.2、1.2.4及附录B；不保留整本提取文字，以原始链接与章节记录为准。

发现并处理的来源差异：

- FEniCSx 教程的一般源q与点源总量Q不能使用相同单位。正文明确分布密度q为s⁻¹、Q为m³/s。
- Bempp 格林函数采用exp(+ikr)；本站约定转换为exp(−ikr)。原页中间式Δg=k²g有符号问题，未采纳，以源点外(Δ+k²)G=0独立求导检验。
- COMSOL网页部分公式未被文本解析器完整提取；只将公开说明用于模型范围，具体守恒形式、边界符号和量纲独立推导。
- 官方实现文档只支持方法与复现入口，未声称安装运行FEniCSx、Bempp、k-Wave或COMSOL。

## 配图与复现

运行 `python scripts/generate-wave-helmholtz.py` 生成六组SVG与PNG。图内文字采用Microsoft YaHei，SVG字形转路径。所有数据是明确参数下的独立教学计算，不是人体、耳道或器件实测，不转载第三方插图。

`figure-manifest.json` 保存参数；`numerical-checks.json` 保存边界阻抗、能流、传播时延及声压级核对。模态图各自归一化且竖直错开，不比较响应强弱；高斯包无限长尾部不用于判断严格波前。

运行 `node scripts/prepare-wave-helmholtz.mjs` 校验元数据、引文顺序、概念链接、图片、学习路径和公式，生成本地HTML阅读预览，更新逐词条证据映射。全站运行check、build、verify，结果见`validation.json`。阅读预览和站点均保留Draft状态。
