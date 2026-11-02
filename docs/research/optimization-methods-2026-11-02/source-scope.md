# 来源使用范围

2026-11-02核对17条一手来源记录：MIT Farina讲义10份、CMU Tibshirani讲义2份、Stanford次梯度笔记1份、FNC作者教材章节1份、SciPy官方API页面3份。它们是理论与实现说明，不是17项独立实验研究。

MIT作者HTML使用字形重映射，提取文字含私用区字符；科学核查使用同页链接的可读PDF全文，文献直接链接官方PDF。source-index.json记录页面与PDF的URL、字节数和SHA-256。原始来源缓存仅在本地artifacts/optimization-methods/sources，不复制到网站。

| 来源ID | 针对性使用 |
| --- | --- |
| opt-intro | 建模、可行、全局/局部、Weierstrass存在性 |
| opt-first | 内点与可行方向的一阶必要性 |
| opt-convex | 凸定义、支撑、Hessian、严格/强凸及唯一性 |
| opt-kkt | 乘子、活跃集、互补、LICQ、Slater与充分性 |
| opt-dual | 下确界、弱/强对偶、可行上下界及证书 |
| opt-gradient | L光滑、下降引理、步长、收敛对象及速率 |
| opt-projection | 闭凸投影、投影梯度与凸收敛条件 |
| opt-sgd | 条件平均、随机估计、噪声及收敛意义 |
| opt-newton | Hessian、预条件、局部Newton及保护 |
| opt-barrier | 障碍路径、中央路径与内点基本作用 |
| opt-prox | 复合目标、近端、软阈值与步长速率 |
| opt-bfgs | 曲率差、割线、正定更新及有限历史 |
| opt-subgrad | 次梯度、非下降性质、最佳已见目标及步长 |
| opt-nlsq | Gauss–Newton、线性化与Levenberg阻尼 |
| opt-minimize-api | 方法支持、边界、导数接口与返回状态 |
| opt-slsqp-api | ftol、多项停止判断与约束实现 |
| opt-lsq-api | TRF/LM、bounds、loss、x_scale及终止 |

正文不逐句翻译或复制讲义，不复用来源配图。十幅科学图、课程简笔画、三个短程序与完整脚本均为原创教学材料。数值来自本地指定计算，不伪称来源报告了这些案例。

来源读取是针对性论断核查，不表示逐页审读所有讲义或完成系统文献综述。MIT讲义自身声明未经正式同行评审；一手课程资料用于教学定理与假设，不代替听觉实证证据。
