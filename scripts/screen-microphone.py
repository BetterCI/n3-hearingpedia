"""Manual semantic screening and research notes; no keyword relevance scoring."""
from pathlib import Path
import json, importlib.util
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/research/microphone-2026-10-10'
pool=json.loads((OUT/'candidate-pool.json').read_text(encoding='utf-8'))
decisions={
'Measurement Uncertainty in Microphone Free-Field Comparison Calibrations':('Important','自由场比较校准的不确定度，与校准条件直接相关；未取得摘要／全文，不转录误差数值。'),
'Phase Calibration of Microphones by Measurement in the Free-field':('Important','研究MEMS阵列的自由场相位校准，说明通道幅度之外还需相位控制；仅摘要筛选，正文不转录研究性能。'),
'Free-field calibration of measurement microphones at high frequencies':('Important','扩展高频自由场校准，相关方法证据；超声频带超出词条可听声主范围，不采用未读全文的上限。'),
'An investigation on methods for free-field comparison calibration of measurement microphones.':('Important','比较先后测量的时间稳定与同时测量的空间一致条件；校准设计相关，正文范围优先用官方标准。'),
'Free-field reciprocity calibration of measurement microphones at frequencies up to 150 kHz':('Important','超声互易校准及可追溯性，方法相关但频段不是正文重点。'),
'Uncertainty analysis on free-field reciprocity calibration of measurement microphones for airborne ultrasound':('Important','超声校准不确定度及标准建立；仅摘要，未用作人体安全结论。'),
'Micromachined piezoelectric microphones with in-plane directivity':('Important','制作压电端簧／旋转梁并测方向性；与声路和压电检测维度直接相关，未取得全文不复制性能。'),
'Effect of microphone position on voice quality':('Important','讨论拾音位置造成喷气、齿音和音色变化；相关录音控制背景，仅摘要可核对。'),
"Estimation of the pressure at a listener's ears in an active headrest system using the remote microphone technique":('Background','远程监测点估计耳部压力的滤波器与系统仿真／实验；与位置解释有关，超出直接传声器入口。'),
'Bioinspired flow-sensing capacitive microphone':('Important','仿动物声致粒子速度驱动的多孔旋转结构，说明声学输入不必限于压力振膜；正文聚焦常见压力／梯度，不宣称涵盖全部路线。'),
'Listening broadband physical model for microphones: a first step':('Important','宽带模型把传统方向图作为低频远场极限并解释近场；模型背景，与本文假设边界直接相关，仅摘要。'),
'Tutorial on microphone technologies for directional hearing aids':('Background','综述单胶囊双声孔与双单元电子组合、头部和风噪；以旧技术教程作背景，正文选另一可核对全文的早期综述，不把二者算独立临床实验。'),
'A capacitive-piezoelectric hybrid MEMS microphone with signal fusion for enhancing signal-to-noise ratio':('Core','读取结构和实测／融合相关全文；直接混合高灵敏度却低于单压电SNR，提供噪声读出反例和具体条件，选入。'),
'A Hybrid MEMS Microphone Combining Piezoelectric and Capacitive Transduction Mechanisms':('Important','同一混合器件研究线的2025工作，2026论文用作比较；不把两代原型视为独立研究组的重复验证。'),
'MEMS-based piezoresistive and capacitive microphones: A review on materials and methods':('Background','MEMS材料与方法综述；未取得摘要，仅根据对象暂列背景，不推断优劣。'),
'Recent development and futuristic applications of MEMS based piezoelectric microphones':('Background','汇总工艺、参数及应用的综述；用于定位候选，性能结论采用原始原型与条件。'),
'A piezoelectric MEMS microphone optimizer platform':('Important','参数与模型优化平台，相关设计方法；未核对实测，不将模型优化直接当作器件改善。'),
'On the PZT/Si unimorph cantilever design for the signal-to-noise ratio enhancement of piezoelectric MEMS microphone':('Important','模拟、制作并比较不同覆盖结构的PZT悬臂阵列；相关原型，未读全文不转录SNR。'),
'Self-Biased Condenser Microphone with High Capacitance':('Core','1962原始摘要直接描述驻极体薄膜与无需外加直流极化；元数据／作者机构书目核对，选入机制沿革，未取得全文不转录性能。'),
'Actuation Mechanisms of Soft Actuator Materials Driven by Electric Field':('Exclude','软执行器电场驱动，非声学接收或校准研究；仅题名元数据，超出范围。'),
'Sustainability aspect of wearable clean room filters: a review':('Exclude','可穿戴洁净过滤器综述，检索词表面相近，与传声器输入／测量无直接关系。'),
'A review on the application of advanced soil and plant sensors in the agriculture sector':('Exclude','土壤和植物物理化学监测，目标测量对象不同，不因传感器关键词纳入。'),
'Piezoelectric Micromachined Microphone with High Acoustic Overload Point and with Electrically Controlled Sensitivity':('Important','微压电传声器高声压测试与可调灵敏度，直接相关过载边界；仅摘要不列器件排名。'),
'A mechanical manipulated electromechanical coupling design with stretchable electret film: mechanical sensing, energy harvesting, and actuation':('Background','可拉伸驻极体一般机电耦合，包含机械传感与能量转换；不是本文声音接收验证。'),
'Review on piezoelectric actuators: materials, classifications, applications, and recent trends':('Exclude','逆压电执行器综述，声学接收不是研究终点。'),
'A Micromachined Dual-Backplate Capacitive Microphone for Aeroacoustic Measurements':('Important','双背板结构制作和表征，提供经典微传声器研究候选；正文选择可读混合原型，不比较未读全文的动态范围。'),
'Modeling of viscous damping of perforated planar microstructures. Applications in acoustics':('Background','穿孔平面结构黏性阻尼模型，属于背板空气负载理论背景。'),
'An analytical analysis of the sensitivity of circular piezoelectric micromachined ultrasonic transducers to residual stress':('Background','圆形超声压电结构残余应力解析模型；机制相关，频带和器件角色需另核对，未作为可听声原型。'),
'Silicon microphone development and application':('Background','硅传声器发展主题与沿革有关；无摘要，背景候选，不推断具体成果。'),
'Effects of scaling and geometry on the performance of piezoelectric microphones':('Important','尺寸／几何与压电传声器参数相关；无摘要，仅暂列研究候选，不作性能比较。'),
'Analysis and design of an electrostatic MEMS microphone using the PolyMUMPs process':('Important','特定工艺的电容MEMS设计候选；无摘要，不把设计标题当实测证据。'),
'Self‐Sustaining Sensing Systems: Integration Strategies and Signal–Power Matching in Energy‐Harvesting Electronics':('Exclude','能量采集与自持传感电子综述，没有直接传声器声学表征或校准证据。'),
'A semi-analytical method for efficient directivity simulation of receiving transducers in uniform background flow':('Background','均匀流场的接收换能器方向性模型，超出静止空气教学模型；无摘要，不推断实验。'),
}
rows=[]
for r in pool:
    grade,reason=decisions[r['title']]
    basis='related fulltext sections' if 'signal fusion for' in r['title'] else 'abstract' if r.get('abstract') else 'metadata only; provisional topic classification'
    rows.append({'id':r['id'],'doi':r.get('doi'),'title':r['title'],'type':r.get('type'),'grade':grade,'reason':reason,'evidence_basis':basis,'selected':grade=='Core'})
(OUT/'semantic-screening.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sp=importlib.util.spec_from_file_location('judge',Path('C:/Users/mengq/.codex/skills/deep-research/scripts/judge_relevance.py'));judge=importlib.util.module_from_spec(sp);sp.loader.exec_module(judge)
(OUT/'relevance-prompt.txt').write_text(judge.build_prompt(next(r for r in pool if 'signal fusion for' in r['title']),'传声器的拾音、声路、噪声与校准怎样影响听觉实验的可解释性？'),encoding='utf-8')
(OUT/'research-notes.md').write_text('''# 传声器研究记录 · 2026-10-10

范围：常见可听声传声器的换能机制、声路、指向性、近场、噪声与测量校准，连接听觉实验和辅助设备。声粒子速度／仿生结构列入候选但不完整展开；超声、生物体效应、所有阵列算法和产品推荐超出本词条范围。经典机制不限起始年份，近期窗口2021-01-01至2026-10-10。

三组OpenAlex主题查询各6项，1962驻极体论文与2026混合MEMS论文两个种子各向后、向前至多6项，DOI→OpenAlex ID→标题去重，共33项；人工按研究对象、摘要及证据性质分级。缺少摘要者只作暂定主题分类，没有依据题名推断结果。原urllib传输因本机CA路径错误失败，错误保留，改用requests传输后发现步骤全部成功；使用技能客户端的简化和筛选提示函数。没有声称穷尽文献。

正文21项参考，14项新登记、7项复用；原始研究、历史综述、官方技术说明和标准公开目录分别标注。1962条目核对为DOI10.1121/1.1909130、34(11)、1787–1788，区别于12期补刊复数标题DOI10.1121/1.1937012；未取得经典原文，机制仅据摘要及作者机构说明。2026原型通过Europe PMC XML核对Measurement Setup、Frequency Response、Noise Floor、Signal Fusion和Conclusion相关段。下载全文不等于逐段通读。

关键反例：2026原型直接混合后灵敏度增大，但噪声密度换算的SNR低于纯压电通道，优化融合后才提高。SNR按该论文1 kHz噪声密度方法报告，不能直接与宽带A计权产品SNR比较；论文将μV/√Hz标为PSD，本站按实际单位区分幅度谱密度与功率谱密度，没有复制这种单位混用。不同研究的量产、电耗或用户获益缺少共同条件，不据单原型排名技术。

Brüel & Kjær手册核对March2019版本，选读PDF第25–26、32–34、37–38、89–93、147–148页相关机制和校准段；全文PDF和抽取文本仅保存在忽略的artifacts/microphone-sources，未转载到站点。Chung2004综述读取PMC方向机制及混响／现场差异相关段，作为早期背景，不替代原始临床试验或现代产品验证。Europe PMC该综述XML取回500，正文经PMC公开页面阅读；错误保留。厂商说明支持机制和测量条件，不支持通用音质优越性。

四幅图为原创概念／解析教学图，保存SVG、PNG、生成脚本和manifest。参数不是产品推荐或论文拟合：球面积分验证Q，纯梯度点声源按相同局部压力比较，增益例子明确0.5Vrms正弦ADC满量程，双路平均限定等方差且同信号增益／相位。实物三张保留原JPEG，许可、作者、来源与校验摘要单独记录，其中驻极体与MEMS图片复用已核对条目。实物照片不提供性能比较证据。

编辑状态：draft、in-depth，reviewer与reviewed_at为空。图片PNG及实物已视觉检查；修复近讲图图例与注记重叠。HTML通过资源、引用、KaTeX和schema静态核验；桌面及约390px窄屏浏览器人工视觉检查未完成。专业科学审阅仍待完成，不声称标准符合性。
''',encoding='utf-8')
(OUT/'directionality-fulltext-error.json').write_text(json.dumps({'url':'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4111442/fullTextXML','error':'HTTP 500','read_alternative':'PMC official public HTML; only relevant sections read'},indent=2)+'\n',encoding='utf-8')
print('Screened',len(rows),'candidates; selected one classic abstract and one current original prototype.')
