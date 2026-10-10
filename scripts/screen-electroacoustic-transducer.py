"""Persist editorial semantic screening; grades are manually assessed, not keyword scores."""
from pathlib import Path
import json, importlib.util
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/research/electroacoustic-transducer-2026-10-10'
sp=importlib.util.spec_from_file_location('judge',Path('C:/Users/mengq/.codex/skills/deep-research/scripts/judge_relevance.py'));judge=importlib.util.module_from_spec(sp);sp.loader.exec_module(judge)
pool=json.loads((OUT/'candidate-pool.json').read_text(encoding='utf-8'))
# Match by title because discovery runs may complete in a different order.
decisions={
'Linearization of Electroacoustic Transducers':('Important','研究电声器件非线性及控制；与大信号边界直接相关，入口词条采用官方标准范围，未依据未读论文给出效果数值。'),
'An Electroacoustic Analysis of Transmission Line Loudspeakers':('Background','传输线扬声器的特定管道设计；可作负载进阶阅读，超出本词条最小活塞／密闭腔模型。'),
'Nonlinear Distortions in Electroacoustic Devices':('Background','综述器件非线性及其度量；提供背景而非新原型验证。'),
'The impact of micromachined ultrasonic radiators on the efficiency of transducers in air':('Background','超声辐射器的效率问题；目标频段与听觉入口不完全一致。'),
'A Novel Miniature Matrix Array Transducer System for Loudspeakers':('Important','研究微型执行器阵列驱动平板的转换结构；相关原型，但未取得全文，不纳入具体性能结论。'),
'Optimization of electroacoustic absorbers by means of designed experiments':('Background','主动电声吸收装置优化，与本词条传感和声输出入口间接相关。'),
'A Hybrid MEMS Microphone Combining Piezoelectric and Capacitive Transduction Mechanisms':('Important','制作混合压电／电容麦克风并建模；相关机制证据，仅摘要筛选，未引用定量收益。'),
'A capacitive-piezoelectric hybrid MEMS microphone with signal fusion for enhancing signal-to-noise ratio':('Important','混合检测及信号融合改善SNR；与传感链相关，但未核对全文实验条件，不转录增益。'),
'A Hybrid Piezoelectric–Capacitive MEMS Microphone With Peripheral Electrostatic Transduction':('Important','标题提示混合麦克风结构；摘要仅含资助信息，暂定相关，不能据此评判性能。'),
'A Review of MEMS Capacitive Microphones':('Background','电容MEMS麦克风发展综述；非独立机制验证，未作为多个原型的替代证据。'),
'PIEZOELECTRIC MEMS MICROPHONES NOISE SOURCES':('Important','压电麦克风的噪声来源和测量；与弱声限制相关，仅摘要筛选。'),
'Advantages of piezoelectric microelectromechanical systems (MEMS) microphones.':('Background','会议摘要中的机制比较观点；不足以支持通用优越性结论。'),
'On the Design and Modeling of a Full-Range Piezoelectric MEMS Loudspeaker for In-Ear Applications':('Important','入耳压电扬声器设计及建模；有相关原型，选择后续可读实测均衡研究形成具体例子。'),
'A piezoelectric MEMS loudspeaker for in-ear and free field applications lumped and finite element models':('Important','标题直接涉及模型与入耳／自由场负载；无摘要，暂定相关，未据此给出性能。'),
'Equalizing the In-Ear Acoustic Response of Piezoelectric MEMS Loudspeakers Through Inverse Transducer Modeling':('Core','全文验证负载等效模型与实测均衡；明确线性模型限制和声输出／THD权衡，选入正文。'),
'Discrete-Time Circuital Modeling of Hysteretic Piezo-Actuated MEMS Loudspeakers for In-Ear Applications':('Important','显式建模压电迟滞；与非线性模型边界直接相关，未读全文不宣称补偿结果。'),
'Design, Modeling, and Characterization of PZT-driven MEMS Loudspeakers for In-Ear Applications: Evolution Through Three Device Generations':('Important','标题表明多代器件的设计与表征；无摘要，暂定候选，不纳入性能比较。'),
'MEMS Loudspeaker for In-Ear Application':('Background','模型与器件改进的会议背景；未取得足够实验细节。'),
'Wave digital filters: Theory and practice':('Background','波数字滤波器理论，属于均衡论文实现背景；不直接研究声学负载或器件性能。'),
'Singular Network Elements':('Background','逆电路模型使用的网络理论基础；不是电声实测证据。'),
'Comparison of Loudspeaker Equalization Methods Based on DSP Techniques':('Important','比较扬声器均衡方法及实现稳健性；相关经典候选，未读全文不比较方法排名。'),
'The Mirror Filter-A New Basis for Reducing Nonlinear Distortion and Equalizing Response in Woofer Systems':('Important','标题涉及低音单元的非线性补偿与均衡；无摘要，暂定相关，不转录效果。'),
'Equalization of loudspeaker response using balanced model truncation':('Important','研究均衡滤波器阶数与误差；与数字处理相关，入口词条不展开算法比较。'),
'Efficient Filter Design for Loudspeaker Equalization':('Background','标题涉及均衡滤波器设计；缺少摘要，作为算法背景候选。'),
'Push–pull actuated MEMS piezoelectric speaker for enhanced sound pressure level':('Important','研究入耳压电执行方案及输出优化；相关2026候选，摘要不足以核对所有驱动和负载条件。'),
'Gradient-Based Optimization of MEMS Loudspeaker Equivalent Circuit Models via Automatic Differentiation':('Important','参数估计与模型优化，直接服务于等效模型；非独立听觉获益验证。'),
'Meander-shaped piezoelectric MEMS loudspeaker with maximized area efficiency for in-ear applications':('Core','制造新结构并以耳模拟器实测，与结构／负载／原型证据层级直接相关，阅读相关全文段落后选入。'),
'Squeeze film air damping in MEMS':('Background','微结构空气阻尼的一般理论；可解释进阶损耗，但并非听觉器件验证。'),
'Acoustics: Sound Fields and Transducers':('Background','声场与换能器教材；候选元数据，无正文访问，不据此转录公式。'),
'Optimization and characterization of wafer-level adhesive bonding with patterned dry-film photoresist for 3D MEMS integration':('Exclude','研究键合工艺，与具体听觉转换性能只有制造层面间接关系。'),
'Proceedings of the 130th Audio Engineering Society Convention':('Exclude','整本会议录元数据，不是可定位的单篇证据。'),
'Atomic Layer Deposition of Aluminum Nitride Thin films from Trimethyl Aluminum (TMA) and Ammonia':('Exclude','薄膜沉积工艺，未直接回答本文的声输出及测量问题。'),
'Simulation of the IEC 60711 Occluded Ear Simulator':('Important','耳模拟器建模与负载相关；无摘要，暂定相关，标准范围优先用官方目录核对。'),
'Microstructured Tactile Sensors With Bismuth Telluride Coatings for Vibration Detection':('Exclude','触觉／设备振动传感研究，应用终点与本文听觉接口不同。'),
'Optimization of graphene-based speaker for hearing aids':('Important','以多物理仿真优化助听器扬声器；缺少全文实测核对，不把仿真结果当成已验证产品。'),
'ОПТИМІЗАЦІЯ ФАЗОІНВЕРТОРНОГО ОФОРМЛЕННЯ САБВУФЕРА МАЛОГО ОБ’ЄМУ З ВИКОРИСТАННЯМ ДИНАМІКА 75ГДН ТА ІНТЕГРОВАНОГО ПІДСИЛЮВАЧА КЛАСУ AB':('Background','特定低音箱体及功放装配优化；相关负载案例，但不是通用换能原理的必要证据。'),
'Physics-Based Compact Modeling of an Ultrasonic Modulation MEMS Speaker Concept':('Important','超声调制MEMS声输出概念的物理紧凑建模；机制相关但本文未展开该路线，需另核对实测。'),
}
screen=[]
for r in pool:
    grade,reason=decisions[r['title']]
    basis='full_text' if grade=='Core' else ('abstract' if r.get('abstract') else 'title')
    screen.append({'id':r['id'],'doi':r.get('doi'),'title':r['title'],'grade':grade,'reason':reason,'evidence_basis':basis,'selected':grade=='Core'})
(OUT/'semantic-screening.json').write_text(json.dumps(screen,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'relevance-prompt.txt').write_text(judge.build_prompt(next(r for r in pool if 'Meander-shaped' in r['title']),'电声换能器：耦合机制、声学负载与测量参考如何决定器件表现？'),encoding='utf-8')
(OUT/'research-notes.md').write_text('''# 电声换能器研究记录 · 2026-10-10

范围：通用听觉输入／输出器件的物理接口；骨导作为相关电机械接口。经典原理不限起始年份；近期检索窗口为2021-01-01至2026-10-10。三组OpenAlex查询各6项，两个2025原型研究种子各向后6项、向前至多6项，按DOI、OpenAlex ID、标题依次去重，共37项。正文选入两个能够核对相关全文段落的原型研究；其余候选按实际研究对象与证据层级人工分级，未作关键词评分。

工程定义以官方技术资料为背景，标准以官方公开目录的范围和版本为依据；这些不是临床研究，也不构成独立的人体获益证据。19项正文参考中16项新登记，3项复用已有登记。同一出版者或制造商的多个材料不算独立重复验证。正文不声称研究覆盖全部电声技术路线。

阅读范围见source-ledger.json。Becker论文阅读出版者可访问的设计／声学表征、讨论与结论相关段落；Massi论文通过Europe PMC XML核对第2–5节相关段落。下载全文不等于逐段通读。Crossref接口本轮读取失败，错误保留；标题与DOI由OpenAlex及出版者核对，Massi作者和期刊由Europe PMC核对。未依据Crossref失败结果补造元数据。

反例与限制：Becker原型的输出与后续产品目标仍有距离；Massi线性逆模型不直接补偿非线性，部分THD降低伴随输出下降。仿真候选不作为实测；制造商宣传不作为通用音质排序；没有人体可懂度或临床获益证据可从这些器件测量直接推出。

四幅图为原创：两幅概念图，一幅解析动圈负载比较，一幅灵敏度换算。解析参数是教学假设；没有拟合产品数据或复制论文曲线。manifest.json保存假设、单位和耦合方程残差检查。图中文字与布局已检查PNG；HTML资源、公式、引用及全站检查另记录。

当前稿件为draft、in-depth，reviewer和reviewed_at为空。未完成领域专家审阅，不据目录给出标准符合性结论。网页桌面与窄屏的交互式人工视觉检查未完成；本地预览只通过静态资源与渲染检查。
''',encoding='utf-8')
print('Screened',len(screen),'candidates; two primary studies selected.')
