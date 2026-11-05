"""Register the FFR entry and narrowly scoped navigation links."""
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
def read(p): return (ROOT/p).read_text(encoding='utf-8')
def write(p,s): (ROOT/p).write_text(s,encoding='utf-8')
refs={}
def ref(key,title,authors,year,publication,doi,url,access,supports,preprint=False):
    refs[key]={'title':title,'authors':authors,'year':year,'publication':publication,'doi':doi,'url':url,'access':access,'supports':'2026-11-06：'+supports}
    if preprint: refs[key]['publicationType']='preprint'
ref('ffr-krizman-2019','Analyzing the FFR: A tutorial for decoding the richness of auditory function','Jennifer Krizman; Nina Kraus','2019','Hearing Research, 382, 107779','10.1016/j.heares.2019.107779','https://brainvolts.northwestern.edu/wp-content/uploads/boxtrx/Krizman_Kraus_HR_2019.pdf','fulltext','作者机构PDF第2–4节相关段落：极性、单次记录、触发抖动、时频分析及一致性。数值教学图为独立解析推导，不复制论文实验数据。')
ref('ffr-aiken-2008','Envelope and spectral frequency-following responses to vowel sounds','Steven J. Aiken; Terence W. Picton','2008','Hearing Research, 245(1–2), 35–47','10.1016/j.heares.2008.08.004','https://pubmed.ncbi.nlm.nih.gov/18765275/','abstract','PubMed摘要：自然元音、反极性加减与基频／共振峰附近谐波；不把操作性分量当作纯解剖来源。')
ref('ffr-bidelman-2018','Subcortical sources dominate the neuroelectric auditory frequency-following response to speech','Gavin M. Bidelman','2018','NeuroImage, 175, 56–69','10.1016/j.neuroimage.2018.03.060','https://www.sciencedirect.com/science/article/pii/S1053811918302702','fulltext','出版商摘要及可读Introduction、Results/Discussion相关段落：64通道EEG模型中的皮层下优势，限定刺激、成像与源模型条件。')
ref('ffr-gnanateja-2021','Frequency-Following Responses to Speech Sounds Are Highly Conserved across Species and Contain Cortical Contributions','G. Nike Gnanateja; Kyle Rupp; Fernando Llanos; Madison Remick; Marianny Pernia; Srivatsun Sadagopan; Tobias Teichert; Taylor J. Abel; Bharath Chandrasekaran','2021','eNeuro, 8(6), ENEURO.0451-21.2021','10.1523/ENEURO.0451-21.2021','https://pmc.ncbi.nlm.nih.gov/articles/PMC8704423/','fulltext','PMC摘要及Discussion：两名人类颅内受试者、猕猴与豚鼠跨层次记录支持皮层发生源；不能由小样本推出固定皮层百分比。')
ref('ffr-tichko-2017','Frequency-dependent fine structure in the frequency-following response: The byproduct of multiple generators','Parker Tichko; Erika Skoe','2017','Hearing Research, 348, 1–15','10.1016/j.heares.2017.01.014','https://pubmed.ncbi.nlm.nih.gov/28137699/','abstract','摘要与可检索作者论文段落支持不同延迟来源的相长／相消；图1使用自设两等幅来源，不拟合其多源模型。')
ref('ffr-myogenic-2024','Myogenic artifacts masquerade as neuroplasticity in the auditory frequency-following response','Gavin M. Bidelman; Alexandria Sisson; Rose Rizzi; Jessica MacLean; Kaitlin Baer','2024','Frontiers in Neuroscience, 18, 1422903','10.3389/fnins.2024.1422903','https://pmc.ncbi.nlm.nih.gov/articles/PMC11260751/','fulltext','PMC摘要、Methods及讨论相关段落：眼位、参考电极及100/200 Hz刺激下耳后肌污染；不据此否定全部训练效应，不把颈部参考当通用无伪迹保证。')
ref('ffr-song-retest-2011','Test–retest reliability of the speech-evoked auditory brainstem response','Judy H. Song; Trent Nicol; Nina Kraus','2011','Clinical Neurophysiology, 122(2), 346–355','10.1016/j.clinph.2010.07.009','https://brainvolts.northwestern.edu/wp-content/uploads/boxtrx/Song_Test_Retest_2011.pdf','fulltext','作者PDF摘要与方法入口：年轻成人两次记录、安静与多人语噪；支持条件限定的重复性，不将均值无差异等同个体一致性。')
ref('ffr-krishnan-2005','Encoding of pitch in the human brainstem is sensitive to language experience','Ananthanarayan Krishnan; Yisheng Xu; Jackson Gandour; Peter Cariani','2005','Cognitive Brain Research, 25(1), 161–168','10.1016/j.cogbrainres.2005.05.004','https://pubmed.ncbi.nlm.nih.gov/15935624/','abstract','原始摘要：普通话与英语母语者对四声的自相关／谱指标差异；横断面关联，不证明单一脑区或排除背景混杂。')
ref('ffr-song-training-2008','Plasticity in the adult human auditory brainstem following short-term linguistic training','Judy H. Song; Erika Skoe; Patrick C. M. Wong; Nina Kraus','2008','Journal of Cognitive Neuroscience, 20(10), 1892–1902','10.1162/jocn.2008.20131','https://pubmed.ncbi.nlm.nih.gov/18370594/','abstract','PubMed及PMC可检索摘要：英语成人词汇声调训练前后FFR变化；未完整读取全文，不声称随机对照疗效。')
ref('ffr-schuller-2024','The Early Subcortical Response at the Fundamental Frequency of Speech Is Temporally Separated from Later Cortical Contributions','Alina Schüller; Achim Schilling; Patrick Krauss; Tobias Reichenbach','2024','Journal of Cognitive Neuroscience, 36(3), 475–491','10.1162/jocn_a_02103','https://pubmed.ncbi.nlm.nih.gov/38165737/','abstract','原始摘要及机构PDF首页：连续语音MEG的早期4–11 ms与较晚20–58 ms成分；仅为该分析的窗口，不作为所有FFR来源分界。')
ref('ffr-rapid-2025','Rapid FFR: A rapid method for obtaining Frequency Following Responses','Jonas Huber; Tim Schoof; Hannah Stewart; Alain de Cheveigné; Stuart Rosen','2025','bioRxiv, version 1, 2025.05.20.655073（预印本）','10.1101/2025.05.20.655073','https://pmc.ncbi.nlm.nih.gov/articles/PMC12139732/','fulltext','PMC预印本摘要与方法入口：128 Hz连续锯齿波、按周期平均、年轻正常听力样本；未核实到正式期刊版本，保留未同行评审标识。',True)
ref('ffr-danielou-2026','Event-Related Brain Potentials and Frequency-Following Response to Syllables in Newborns and Adults','G. Danielou; E. Hervé; A. S. Dubarry; B. Desnous; C. François','2026','European Journal of Neuroscience, 63(3), e70418','10.1111/ejn.70418','https://pmc.ncbi.nlm.nih.gov/articles/PMC12884137/','fulltext','出版商／PubMed摘要及PMC可检索Methods、Results、Discussion段落：17名足月新生儿与21名成人，F0和共振峰编码成熟不同；不能据此建立婴儿诊断常模。')
ref('ffr-whiteford-2025','Large-scale multi-site study shows no association between musical training and early auditory neural sound encoding','Kelly L. Whiteford et al.','2025','Nature Communications, 16, 7152','10.1038/s41467-025-62155-5','https://www.nature.com/articles/s41467-025-62155-5','fulltext','出版方可检索正文及作者机构PDF摘要／引言：六中心、超过260人、预注册复现未支持所检验的音乐训练／能力与早期编码关联；不推广为所有音乐神经可塑性均不存在。')
write('src/data/frequency-following-response-references.ts',"import type { Reference } from './references';\n\nexport const frequencyFollowingResponseReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n')
p='src/data/references.ts';s=read(p)
if 'import { frequencyFollowingResponseReferences }' not in s:
    s="import { frequencyFollowingResponseReferences } from './frequency-following-response-references.ts';\n"+s
    s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...frequencyFollowingResponseReferences,')
write(p,s)
backlinks={'auditory-evoked-potential':'周期性声音的来源、极性控制与分析方法，详见[频率跟随反应（FFR）](../frequency-following-response/)。',
'auditory-brainstem-response':'持续周期编码与瞬态ABR的区别，以及相应的记录和解释边界，见[频率跟随反应（FFR）](../frequency-following-response/)。',
'phase-locking':'头皮群体电位中的相位一致性、来源叠加与测量偏差，见[频率跟随反应（FFR）](../frequency-following-response/)。'}
for slug,line in backlinks.items():
    p=f'src/content/concepts/{slug}.md';s=read(p)
    if line not in s:
        at=s.index('\n## ');s=s[:at]+'\n'+line+'\n'+s[at:]
        s=re.sub(r'last_updated:.*','last_updated: "2026-11-06"',s,count=1)
    write(p,s)
p='src/data/relations.ts';s=read(p)
relations=[('auditory-evoked-potential','属于听觉诱发电位，关注持续时间结构。'),('auditory-brainstem-response','持续跟随与瞬态起始反应需要分别分析。'),('phase-locking','群体同步及跨试次一致性连接周期刺激与电位。'),('temporal-envelope','极性相加突出某些包络相关成分。'),('temporal-fine-structure','极性相减保留极性敏感成分，也可能保留伪迹。'),('auditory-pathway','皮层下与皮层来源依赖刺激、记录及模型。'),('pitch-perception','周期表征与主观音高能力需要独立验证。'),('audiometric-calibration','声级、声学延迟与数字时间基准决定可比性。')]
if "link('frequency-following-response'" not in s:
    lines='\n'.join(f"  link('frequency-following-response','{target}','related','{note}',3)," for target,note in relations)
    at=s.index('\n];\nexport function relationshipsFor');s=s[:at]+'\n'+lines+s[at:]
write(p,s)
p='src/data/paths.ts';s=read(p)
line=next(l for l in s.splitlines() if "id:'measurement'" in l)
if "'frequency-following-response'" not in line:s=s.replace(line,line.replace("'auditory-brainstem-response',","'auditory-brainstem-response','frequency-following-response',"))
write(p,s)
print('Registered',len(refs),'sources, three backlinks and eight relations.')
