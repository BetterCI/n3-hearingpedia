"""Register verified sources and this entry's owned integration additions."""
from pathlib import Path
import json, yaml, re
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'docs/research/electroacoustic-transducer-2026-10-10'
SLUG='electroacoustic-transducer'
def ref(id,title,authors,year,publication,url,access,supports,doi=None):
    r=dict(title=title,authors=authors,year=year,publication=publication,url=url,access=access,supports=supports)
    if doi:r['doi']=doi
    return id,r
items=[
ref('et-comsol-lumped','Lumped Loudspeaker Driver','COMSOL','n.d.','COMSOL Multiphysics 6.4 官方模型文档','https://doc.comsol.com/6.4/doc/com.comsol.help.models.aco.lumped_loudspeaker_driver/lumped_loudspeaker_driver.html','documentation','阅读 Introduction、Model Definition 及集总电／机械参数、反电动势和背腔比较段落；作为线性建模背景。本文公式采用独立简化，参数非文档产品参数。'),
ref('et-comsol-driver','Loudspeaker Driver — Frequency-Domain Analysis','COMSOL','n.d.','COMSOL Multiphysics 6.4 官方模型文档','https://doc.comsol.com/6.4/doc/com.comsol.help.models.aco.loudspeaker_driver/loudspeaker_driver.html','documentation','阅读电磁力、声固耦合、阻抗、声压和辐射评价段落；支持多物理域分析与不同输出量的区分，不把示例仿真当作通用产品性能。'),
ref('et-ni-handbook','Microphone Handbook: Types, Components & Testing','NI / PCB Piezotronics','2025','NI 官方传感器技术资料（PCB 材料获许可转载）','https://www.ni.com/en/shop/data-acquisition/sensor-fundamentals/measuring-sound-with-microphones/microphone-handbook.html','documentation','阅读电容、驻极体、动圈结构及极化／前置放大器说明；解释基本转换和供电关系。转载内容不计为第二个独立研究。'),
ref('et-ni-measurement','Measuring Sound with Microphones','NI','n.d.','NI 官方传感器技术资料','https://www.ni.com/en/shop/data-acquisition/sensor-fundamentals/measuring-sound-with-microphones.html','documentation','阅读麦克风物理类型、选择、场响应及信号调理说明；支持压电和电容检测、场条件和测量链。未将声压与声压级混作同一单位。'),
ref('et-knowles-ba','Balanced Armature','Knowles Electronics','n.d.','制造商官方结构说明','https://product.knowles.com/audio/receivers/balanced-armature','documentation','仅采用固定线圈与低质量振膜的结构描述，并对照制造商技术资料；不采用音质或消费者满意度宣传证明比较优势。'),
ref('et-adi-sensitivity','Understanding Microphone Sensitivity','Jerad Lewis','2012','Analog Dialogue, 46 (May), Analog Devices','https://www.analog.com/en/resources/analog-dialogue/articles/understanding-microphone-sensitivity.html','documentation','阅读 Analog vs. Digital 和 Choosing Sensitivity：模拟／数字参考、峰值／有效值约定及灵敏度不等于质量。换算图使用独立假设的20 mV/Pa，不引用产品性能。'),
ref('et-adi-preamp','AN-1165: Op Amps for MEMS Microphone Preamp Circuits (Rev. A)','Jerad Lewis','2013','Analog Devices Application Note','https://www.analog.com/media/en/technical-documentation/application-notes/AN-1165.pdf','documentation','阅读第1–3页 Introduction、Noise、THD+N、Supply Voltage 及电路说明；支持读出增益、噪声带宽和供电限制。不照搬示例器件推荐。'),
ref('et-iec60268-21','IEC 60268-21:2018: Acoustical (output-based) measurements','International Electrotechnical Commission','2018','IEC 官方标准目录','https://webstore.iec.ch/en/publication/28687','documentation','读取公开 Scope 与版本状态；支持电输入到声输出物理测量，不含知觉评价。未获得完整付费标准，不据目录声称符合性。'),
ref('et-iec60268-22','IEC 60268-22:2020: Electrical and mechanical measurements on transducers','International Electrotechnical Commission','2020','IEC 官方标准目录','https://webstore.iec.ch/en/publication/60560','documentation','读取公开 Scope 与版本状态；区分电／机械测量、小大信号和应用边界。未获得完整付费条款。'),
ref('et-iec62458','IEC 62458:2010: Electroacoustical transducers — Measurement of large signal parameters','International Electrotechnical Commission','2010','IEC 官方标准目录','https://webstore.iec.ch/en/publication/7062','documentation','公开范围列出电动／电磁电机、悬挂及力因子、刚度、电感等主要非线性；不把这一范围扩展成所有换能器的通用模型。未读完整条款。'),
ref('et-iec60268-4','IEC 60268-4:2018: Microphones (RLV 目录)','International Electrotechnical Commission','2018','IEC 官方标准目录','https://webstore.iec.ch/en/publication/63860','documentation','读取公开范围：声系统麦克风的灵敏度、指向性、阻抗、动态范围和外界影响，范围不含测量麦克风；目录 RLV 含官方版本及红线版本，未获取完整标准。'),
ref('et-iec60268-7','IEC 60268-7:2025: Headphones and earphones','International Electrotechnical Commission','2025','IEC 官方标准目录','https://webstore.iec.ch/en/publication/86573','documentation','读取2025版公开范围及排除项，核对测听耳机、助听器受话器及 ANC 特性不在本标准所述范围内；不引用未读测试条款。'),
ref('et-iec60118-0','IEC 60118-0:2022: Measurement of the performance characteristics of hearing aids','International Electrotechnical Commission','2022','IEC 官方标准目录','https://webstore.iec.ch/en/publication/62974','documentation','读取公开范围：气导助听器的耦合器或耳模拟器电声特性，区分类型／生产质量测量与真实耳内表现。未获得完整付费条款。'),
ref('et-iec61094-2','IEC 61094-2:2009: Pressure calibration by the reciprocity technique; AMD1:2022','International Electrotechnical Commission','2009/2022','IEC 官方标准目录','https://webstore.iec.ch/en/publication/4486','documentation','读取基础版公开范围，并核对2022修订目录 https://webstore.iec.ch/en/publication/67521；限定实验室标准等适用麦克风及复杂压力灵敏度。未转录互易校准步骤。'),
ref('et-becker-2025','Meander-shaped piezoelectric MEMS loudspeaker with maximized area efficiency for in-ear applications','Becker D, Scharf R, Leonhard T, Merz A, Bittner A, Dehé A.','2025','Sensors and Actuators Reports, 9, 100319','https://doi.org/10.1016/j.snr.2025.100319','fulltext','读取出版者公开全文的设计、声学表征、Discussion 和 Conclusion 相关段落；核对16 Vp、1 kHz、64 dB SPL及耳模拟器条件。区分制造原型与未来预测，未声称逐段通读全文。','10.1016/j.snr.2025.100319'),
ref('et-massi-2025','Equalizing the In-Ear Acoustic Response of Piezoelectric MEMS Loudspeakers Through Inverse Transducer Modeling','Massi O, Giampiccolo R, Bernardini A.','2025','Micromachines, 16(6), 655','https://europepmc.org/articles/PMC12195080','fulltext','通过 Europe PMC XML 阅读第2节负载模型、第3节线性逆模型限制、第4节实测与 THD 权衡、第5节结论；支持线性均衡及声输出下降的代价，不迁移论文峰值／DFT幅度到本文RMS示例。','10.3390/mi16060655'),
]
refs=dict(items)
(ROOT/f'src/data/{SLUG}-references.ts').write_text("import type { Reference } from './references';\n\nexport const electroacousticTransducerReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
ledger=[{'id':id,**r,'evidence_role':'primary prototype research' if r.get('doi') else 'official engineering documentation or standard scope','reviewed_at':'2026-10-10'} for id,r in items]
ledger +=[{'id':id,'reuse_existing_registry':True,'access':'documentation','reviewed_at':'2026-10-10','read_scope':scope} for id,scope in [('audiometric-calibration-iec603184','官方目录范围：规定的入耳负载；未获得全文标准'),('audiometric-calibration-iec603186','官方目录范围：骨导振子的机械耦合器；未获得全文标准'),('nidcd-hearing-aids','官方说明的麦克风、放大器、扬声器及助听器作用；不据此宣称特定器件的临床优势')]]
(OUT/'source-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
fm=yaml.safe_load((ROOT/f'src/content/concepts/{SLUG}.md').read_text(encoding='utf-8').split('---',2)[1])
(OUT/'frontmatter.json').write_text(json.dumps(fm,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
path=ROOT/'src/data/references.ts';s=path.read_text(encoding='utf-8');imp="import { electroacousticTransducerReferences } from './electroacoustic-transducer-references.ts';\n"
if imp.strip() not in s:s=imp+s
if '  ...electroacousticTransducerReferences,' not in s:s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...electroacousticTransducerReferences,',1)
path.write_text(s,encoding='utf-8')
edges=[('sound-waves-and-propagation','related','声学端口、传播与边界条件构成换能输出的解释基础。',3),('dynamic-range','related','噪声端、线性范围与最大输出需要使用一致参考量。',3),('audiometric-calibration','related','校准把刺激设定、器件输出及规定负载连接起来。',3),('pure-tone-audiometry','application','纯音刺激经耳机或骨导振子转为受试者接收的物理输入。',3),('otoacoustic-emissions','application','探头同时包含刺激输出与声学接收，需检验整条测量链。',2),('hearing-aid','application','输入麦克风与输出受话器共同约束助听器电声表现。',3),('cochlear-implant','application','麦克风负责声学接收，后续电刺激接口不能套用耳道声输出模型。',2),('speech-intelligibility','related','器件物理指标与使用者言语可懂度属于不同评价终点。',2),('room-acoustics','related','开放空间的声输出响应取决于距离、方向及反射。',2),('vocoder','related','声学模拟仍需要输出器件，文件幅度不能单独确定入耳声压。',1)]
lines=[f"  link('{SLUG}','{target}','{type}','{note}',{strength})," for target,type,note,strength in edges]
path=ROOT/'src/data/relations.ts';s=path.read_text(encoding='utf-8')
s=re.sub(r"^  link\('electroacoustic-transducer',.*\n",'',s,flags=re.M)
if f"link('{SLUG}'," not in s:s=s.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+'\n'.join(lines),1)
path.write_text(s,encoding='utf-8')
row="  { id:'electroacoustic-transducer',title:'从物理端口理解电声器件与听觉应用',english:'Electroacoustic transducers',description:'从声波和边界进入换能机制、阻抗及负载，再通过动态范围与校准理解实验刺激、助听器和实际言语评价。',slugs:['sound-waves-and-propagation','electroacoustic-transducer','dynamic-range','audiometric-calibration','pure-tone-audiometry','hearing-aid','speech-intelligibility'] },"
path=ROOT/'src/data/paths.ts';s=path.read_text(encoding='utf-8')
if "id:'electroacoustic-transducer'" not in s:s=s.replace('export const learningPaths = [','export const learningPaths = [\n'+row,1)
path.write_text(s,encoding='utf-8')
print('Registered 16 new sources, 3 existing sources, 10 relations and 1 path.')
