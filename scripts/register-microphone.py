"""Register only microphone-owned references, relations and learning path."""
from pathlib import Path
import json, re, yaml
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/research/microphone-2026-10-10';OUT.mkdir(parents=True,exist_ok=True)
def ref(id,title,authors,year,publication,url,access,supports,doi=None):
    r=dict(title=title,authors=authors,year=year,publication=publication,url=url,access=access,supports=supports)
    if doi:r['doi']=doi
    return id,r
items=[
ref('mic-dpa-essentials','Microphone technology – the essentials','DPA Microphones','n.d.','制造商官方工程说明','https://www.dpamicrophones.com/mic-university/technology/microphone-technology-the-essentials/','documentation','读取压力／梯度及组合、动圈／带式／电容分类和声场影响段；支持声路与读出分类。本站方向模型和球面积分为独立教学推导，不转载原图或采用营销比较。'),
ref('mic-bk-handbook','Microphone Handbook, Volume 1 (BE 1447–12, March 2019)','Brüel & Kjær','2019','Brüel & Kjær 官方技术手册，所核版本155页','https://www.bksv.com/doc/be1447.pdf','documentation','取得PDF并核对版本页，选读PDF第25–26页声场、第32–34页恒电荷与驻极体、第89–93页场响应和噪声、第147–148页校准与检查段；未逐页通读，未转载整本手册、原图或旧标准实施条款。补充核对第37–38页均压和低频响应。'),
ref('mic-sessler-1962','Self-Biased Condenser Microphone with High Capacitance','G. M. Sessler; J. E. West','1962','The Journal of the Acoustical Society of America, 34(11), 1787–1788','https://doi.org/10.1121/1.1909130','abstract','核对OpenAlex摘要与Crossref元数据，并以作者所在机构技术词汇页交叉核对书目和驻极体机制；只引用无需外加直流极化的原理，不转录未核对全文的性能。注意此处为11期单数Microphone，区别于DOI 10.1121/1.1937012的12期补刊复数标题。','10.1121/1.1909130'),
ref('mic-tu-electret','Electret Condenser Microphone (ECM)','Institut für Nachrichtentechnik, Technische Universität Darmstadt','n.d.','作者研究机构官方技术词汇页','https://www.nt.tu-darmstadt.de/ehemalige_fachgebiete_nt/elektroakustik_nt/forschung_ea/glossar_ea_nt/ecm_ea_nt/index.en.jsp','documentation','读取驻极体薄膜、膜／背极两种安排、声压引起交流输出和1962论文书目；不使用网页旧市场份额估计或据此声称当今市场状态。'),
ref('mic-hybrid-2026','A capacitive-piezoelectric hybrid MEMS microphone with signal fusion for enhancing signal-to-noise ratio','Yangyang Guan; Michael Schneider; Dongsheng Li; Hemin Zhang; Jing Mi; Alexander Bertrand; Sina Sadeghpour; Chen Wang; Huicong Liu; Christ Glorieux; Michael Kraft','2026','Microsystems & Nanoengineering, 12, 136','https://www.nature.com/articles/s41378-026-01251-y','fulltext','通过Europe PMC XML选读结构、Measurement Setup、Frequency Response、Noise Floor、Signal Fusion与Conclusion；核对14×14 mm管、19.2 V偏置、1 kHz灵敏度与SNR。论文按1 kHz噪声密度换算的数值不当作宽带A计权噪声指标；直接混合低于压电模式是反例。本站等噪声平均例子不是论文权重复刻。','10.1038/s41378-026-01251-y'),
ref('mic-dpa-specs','How to read microphone specifications','Eddy Bøgh Brixen','n.d.','DPA Microphones 官方技术说明','https://www.dpamicrophones.com/mic-university/technology/how-to-read-microphone-specifications/','documentation','读取Directional pattern、Sensitivity、Equivalent noise、Maximum SPL、Dynamic range与SNR相关段；采用参考条件和指标区别，不采用网页中泛化的主观响度或消费者评价。'),
ref('mic-dpa-proximity','Proximity effect in microphones explained – how it affects different sound sources','Eddy Bøgh Brixen','n.d.','DPA Microphones 官方技术说明','https://www.dpamicrophones.com/mic-university/background-knowledge/proximity-effect-in-microphones-explained/','documentation','读取点／线／面源、额外幅度梯度和角度条件；不把具体乐器示例扩展为普遍声源分类。本站纯梯度点声源公式和曲线为显式假设下的独立推导，未复制产品测试曲线。'),
ref('mic-iec61094-3','IEC 61094-3:2016: Primary method for free-field calibration of laboratory standard microphones by the reciprocity technique','International Electrotechnical Commission','2016','IEC 官方标准目录','https://webstore.iec.ch/en/publication/25105','documentation','核对公开范围与2016版本：复自由场灵敏度、实验室标准等适用器件、专业设备和人员条件。未获取完整标准，不转录互易实验步骤。'),
ref('mic-iec61094-5','IEC 61094-5:2016: Methods for pressure calibration of working standard microphones by comparison','International Electrotechnical Commission','2016','IEC 官方标准目录','https://webstore.iec.ch/en/publication/24988','documentation','核对公开范围：工作标准／相关适用传声器的压力比较校准，参考传声器与频率条件；未读付费条款。'),
ref('mic-iec61094-8','IEC 61094-8:2012: Methods for determining the free-field sensitivity of working standard microphones by comparison','International Electrotechnical Commission','2012','IEC 官方标准目录','https://webstore.iec.ch/en/publication/4492','documentation','读取公开范围：工作标准传声器自由场比较法及近似自由场与后处理条件；不据目录声称具体实验符合性。'),
ref('mic-iec60942','IEC 60942:2017: Electroacoustics – Sound calibrators','International Electrotechnical Commission','2017','IEC 官方标准目录','https://webstore.iec.ch/en/publication/30045','documentation','公开范围与版本核对：LS、1、2等级声校准器，实验室及现场用途。全文付费，未获得完整条款；不把等级与某台设备合格结论混同。'),
ref('mic-iec-calibrators','MT 17 Sound calibrators','IEC Technical Committee 29','n.d.','IEC 官方工作组说明','https://tc29.iec.ch/groups-and-teams-within-tc29/mt-17-sound-calibrators-new/','documentation','读取已知声压、频率、指定器件与配置、整体灵敏度检查及压力灵敏度用途说明；支持单点现场检查的用途，不声称因此已检验宽带方向响应。'),
ref('mic-chung-2004','Challenges and Recent Developments in Hearing Aids: Part I. Speech Understanding in Noise, Microphone Technologies and Noise Reduction Algorithms','King Chung','2004','Trends in Amplification, 8(3), 83–124','https://pmc.ncbi.nlm.nih.gov/articles/PMC4111442/','fulltext','读取PMC正文3.1.1机制、方向性与整机声场、混响和实验室／现场差异相关段，作为早期方法背景综述；不转录临床效应量或据此推荐现代具体产品，未逐段通读整篇。','10.1177/108471380400800302'),
ref('mic-shure-sm58','SM58 User Guide','Shure','n.d.','Shure 官方产品手册','https://www.shure.com/en-US/docs/guide/SM58','documentation','核对Type为Dynamic (moving coil)、Polar Pattern为Cardioid、位置与近讲提示；仅用于照片型号说明和该产品特定条件，不把营销措辞或型号响应扩展为全部动圈话筒。'),
]
refs=dict(items)
(ROOT/'src/data/microphone-references.ts').write_text("import type { Reference } from './references';\n\nexport const microphoneReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
ledger=[{'id':id,**r,'reviewed_at':'2026-10-10','evidence_role':'primary prototype study' if id=='mic-hybrid-2026' else 'classic abstract' if id=='mic-sessler-1962' else 'historical orientation review' if id=='mic-chung-2004' else 'official documentation or standard public scope'} for id,r in items]
reuse={'et-ni-handbook':'转换机制、驻极体与前置供电关系','et-iec60268-4':'范围排除测量传声器；仅公开目录','et-adi-sensitivity':'V/Pa与数字满量程、有效值／峰值约定','et-adi-preamp':'噪声、带宽、供电和读出限制','et-ni-measurement':'声场和灵敏度背景','et-iec61094-2':'压力互易校准公开范围、2009/2022版本','nidcd-hearing-aids':'助听器麦克风输入的官方说明'}
ledger.extend({'id':id,'reuse_existing_registry':True,'reviewed_at':'2026-10-10','access':'documentation','read_scope':scope} for id,scope in reuse.items())
(OUT/'source-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
fm=yaml.safe_load((ROOT/'src/content/concepts/microphone.md').read_text(encoding='utf-8').split('---',2)[1]);(OUT/'frontmatter.json').write_text(json.dumps(fm,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=ROOT/'src/data/references.ts';s=p.read_text(encoding='utf-8');imp="import { microphoneReferences } from './microphone-references.ts';\n"
if imp.strip() not in s:s=imp+s
if '  ...microphoneReferences,' not in s:s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...microphoneReferences,',1)
p.write_text(s,encoding='utf-8')
edges=[('electroacoustic-transducer','related','声学输入端的具体换能器，进一步展开拾音、声路和电读出。',3),('sound-waves-and-propagation','related','声场、波长及距离决定声学入口的有效驱动。',3),('dynamic-range','related','器件自噪声与整条读出链的过载限制需采用一致条件。',3),('audiometric-calibration','related','参考传声器校准与听觉刺激校准在不同环节连接。',3),('spectrum-and-power-spectral-density','related','区分噪声谱密度、带宽积分与等效输入噪声。',3),('room-acoustics','related','反射、漫射场和测量位置影响方向响应的解释。',3),('hearing-aid','application','声学接收为增益和方向性处理提供输入。',3),('cochlear-implant','application','声处理器前端获取信号，后续电刺激需要独立评价。',2),('otoacoustic-emissions','application','声学探头接收微弱信号，需要控制刺激泄漏与背景。',2),('speech-intelligibility','related','输入端物理指标不能代替使用者的言语行为评价。',2)]
p=ROOT/'src/data/relations.ts';s=p.read_text(encoding='utf-8');s=re.sub(r"^  link\('microphone',.*\n",'',s,flags=re.M)
lines=[f"  link('microphone','{t}','{typ}','{note}',{strength})," for t,typ,note,strength in edges]
s=s.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+'\n'.join(lines),1);p.write_text(s,encoding='utf-8')
p=ROOT/'src/data/paths.ts';s=p.read_text(encoding='utf-8')
row="  { id:'microphone',title:'从声学接收到可解释的听觉实验输入',english:'Microphones and auditory measurements',description:'从换能原理进入声路、指向性与噪声，再用频谱、动态范围和校准连接录音、声学测量及言语评价。',slugs:['electroacoustic-transducer','microphone','spectrum-and-power-spectral-density','dynamic-range','audiometric-calibration','speech-intelligibility'] },"
if "id:'microphone'" not in s:s=s.replace('export const learningPaths = [','export const learningPaths = [\n'+row,1)
p.write_text(s,encoding='utf-8')
print('Registered 14 new sources, 7 reused sources, 10 relations and one learning path.')
