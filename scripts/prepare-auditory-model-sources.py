"""Build source registry with actual access scopes, not inferred full-text access."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/'docs/research/auditory-computational-models-2026-10-10'
rows=json.loads((DOC/'verified-metadata.json').read_text(encoding='utf-8'))
notes={
'acm-comparison':('abstract','原始摘要、机构原文首页及可访问Introduction与模型分类相关段：八个单耳模型比较，输出与配置可比性；不是所有模型的完整排名。'),
'acm-amt':('abstract','原始摘要：AMT的文档、数据、demonstrations与experiments复现组织；数量为2022论文背景，不当作当前模型总数。'),
'acm-mechanics':('abstract','原始综述摘要：哺乳类基底膜行波、级依赖调谐和压缩；用于生理目标，不将教学幂律视作完整耳蜗。'),
'acm-erb':('abstract','原始摘要：凹口噪声反推滤波器，非对称、耳机/外中耳传递与离频聆听影响；不把拟合功率形状等同完整时域处理。'),
'acm-meddis':('abstract','原始摘要：递质释放、回收与损失假设，放电及适应现象；不将功能拟合视为唯一突触机制。'),
'acm-zilany':('abstract','原始摘要：猫外周现象模型的参数与均值/方差改进、不应期影响；物种及输出方式需按实现核对。'),
'acm-bruce':('abstract','原始摘要：有限释放位点模型整合入Zilany外周前端，放电统计与前向掩蔽改进；未报告人类临床诊断性能。'),
'acm-verhulst':('abstract','原始摘要：人类外周—脑干模型、IHC/AN与群体ABR/EFR验证、增益损失与突触病变模拟；不将逆问题写成个体唯一诊断。'),
'acm-dau':('abstract','原始摘要：调制滤波器组、窄带噪声调制检测与掩蔽；阈值和载波限制，不把调制通道视为已确认的特定细胞。'),
'acm-jeffress':('metadata','Crossref与PubMed书目核对，用于1948年声音定位理论的历史节点；延迟线相关结构解释另据Breebaart原始摘要。'),
'acm-durlach':('abstract','Crossref所存原始摘要：均衡与相消、内部误差、指定双耳掩蔽刺激；不推广为全脑唯一双耳处理。'),
'acm-breebaart':('abstract','原始摘要：左右外周、对侧抑制、双耳内部表征与中心决策；双耳延迟/级差与检测读出。'),
'acm-breebaart-test':('abstract','原始摘要：固定参数的三间隔虚拟观察者、时间条件及模型未能覆盖的周期ITD和带宽相关差异阈。'),
'acm-sepsm':('abstract','原始摘要与作者机构摘要：调制域SNRenv和理想观察者、稳态语音形噪声/混响/谱减条件；不推广为全部语言和背景。'),
'acm-stoi':('abstract','作者机构原始PDF检索可见第一页摘要及Crossref书目：STOI与含时频加权的噪声言语实验相关；原文直接打开失败，未宣称阅读全文。'),
'acm-haspi':('abstract','出版方原始摘要及检索可见方法介绍：HASPI v2外周听损、参考/处理信号、包络调制与网络映射；仅核对相关可见段，未宣称完整原文阅读。'),
'acm-model-matched':('fulltext','PLOS原文Abstract、Author summary、Introduction及Results方法假设：自然/模型匹配刺激与初级/非初级fMRI差异，保留池化与匹配范围。'),
'acm-kell':('abstract','原始摘要：语音/音乐任务优化网络、人类错误与fMRI层级预测；网络层不是解剖脑区等同物。'),
'acm-saddler':('abstract','原始摘要：改变外周时域保真与训练声音统计，检验音高行为；优化任务不自动确立人脑算法。'),
'acm-connear':('abstract','原始摘要：CoNNear混合机制/神经网络、未训练的耳蜗测试刺激、级依赖调谐与加速；教师拟合和独立生理验证应区分。'),
'acm-icnet':('abstract','原始摘要及出版方Discussion相关可见段：麻醉沙鼠下丘多单元、非平稳性、复杂声预测与限制；不视为清醒人类皮层或行为模型。')}
bib={};abstracts=[]
for r in rows:
 c=r.get('crossref') or {};e=r.get('europe_pmc') or {}
 assert c.get('title'),r['id']
 authors='; '.join(' '.join(filter(None,[a.get('given'),a.get('family')])) for a in c.get('author') or [])
 date=c.get('published-print') or c.get('published') or {};year=e.get('pubYear') or str(date['date-parts'][0][0])
 if r['id']=='acm-haspi':year='2021'
 publication=', '.join(str(v) for v in [(c.get('container-title') or [''])[0],c.get('volume'),c.get('issue'),c.get('page')] if v)
 access,note=notes[r['id']]
 bib[r['id']]=dict(title=c['title'][0],authors=authors,year=year,publication=publication,doi=r['doi'],url='https://doi.org/'+r['doi'],access=access,supports='2026-10-10：'+note)
 ab=e.get('abstractText') or c.get('abstract') or ''
 abstracts.append({'id':r['id'],'abstract':html.unescape(re.sub('<[^>]+>','',ab)),'scope':note})
docs=[
('acm-hohmann-doc','HOHMANN2002 — Invertible Gammatone filterbank','Auditory Modeling Toolbox contributors','AMT 1.6.0 documentation','https://amtoolbox.org/amt-1.6.0/doc/models/hohmann2002.php','官方文档：中心频率、ERB密度、阶数与带宽参数，数字实现需要验证；不将默认值写成普遍生理常数。'),
('acm-verhulst-code','Verhulstetal2018Model — model code version 1.2','HearingTechnology / Alessandro Altoè; Sarah Verhulst and contributors','Author-maintained implementation','https://github.com/HearingTechnology/Verhulstetal2018Model','作者README：1.2版IC/CN更新及M1/M3/M5重标定、示例与许可；公开可读不意味着所有模型相同许可。'),
('acm-dau-doc','DAU1997 — monaural auditory internal representation','Auditory Modeling Toolbox contributors','AMT 1.6.0 documentation','https://amtoolbox.org/amt-1.6.0/doc/models/dau1997.php','官方接口文档：声学滤波、半波整流/低通、适应环和调制滤波的内部输出；函数调用本身不直接输出行为成绩。')]
for key,title,authors,pub,url,note in docs:bib[key]=dict(title=title,authors=authors,year='核对2026-10-10',publication=pub,url=url,access='documentation',supports='2026-10-10：'+note)
bib['acm-eeg-2026']=dict(title='A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound',authors='Thomas J. Stoll; Ross K. Maddox',year='2026',publication='arXiv:2609.20595v2, 2026-09-24（预印本，未同行评审）',doi='10.48550/arXiv.2609.20595',url='https://arxiv.org/abs/2609.20595v2',access='abstract',publicationType='preprint',supports='2026-10-10：作者预印本摘要及版本页：双耳波形到连续EEG、ABR/TRF/BIC多范式验证目标；未声称会议录用或个体听损诊断有效。')
assert len(bib)==25
(ROOT/'src/data/auditory-model-references.ts').write_text("import type { Reference } from './references';\n\nexport const auditoryModelReferences: Record<string, Reference> = "+json.dumps(bib,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(DOC/'abstracts-read.jsonl').write_text('\n'.join(json.dumps(a,ensure_ascii=False) for a in abstracts)+'\n',encoding='utf-8')
print(json.dumps({'references':len(bib),'original_doi_records':len(rows)}))
