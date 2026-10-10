"""Create bibliography from archived metadata; explicitly preserve actual reading scope."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/research/auditory-development-2026-10-10'
rows=json.loads((DOC/'verified-metadata.json').read_text(encoding='utf-8'))
notes={
'dev-moore-2007':('abstract','原始综述摘要：结构、响应与行为时间线；用于多层框架，不将综述年龄段作为个体诊断切点。'),
'dev-hepper-1994':('abstract','原始摘要：母腹附近纯音与超声运动观察，频率、孕周和反应级有关；不把最早个案反应作为所有胎儿统一起点或家庭刺激处方。'),
'dev-partanen-2013':('abstract','原始摘要与图说明：指定产前材料暴露后的失匹配响应变化；神经学习线索不等于词义、智力或长期语言结局。'),
'dev-eimas-1971':('abstract','原始摘要：1与4月龄合成语音习惯化和反应恢复，跨成人类别边界差异；不推断词义或成人音位系统。'),
'dev-werker-1984':('metadata','Crossref书目核对；出版方打开失败、原始扫描PDF未取得可读文本。本轮只用于历史定位，发展解释引用作者2024回顾，不报告未核实的原始参数。'),
'dev-kuhl-1992':('abstract','原始摘要、PubMed与作者机构原文首页：6月龄美国/瑞典婴儿的语言经验差异，不推断所有音类或双语发展的一致年龄。'),
'dev-kuhl-2003':('abstract','PubMed及Crossref原始摘要：短时面对面普通话经验、英语比较和所用录音条件；不把该结果扩写为所有媒介与年龄无效。'),
'dev-maye-2002':('abstract','原始摘要及出版方检索可见Methods/Discussion相关段：6/8月龄单峰与双峰分布暴露影响辨别。图3独立教学概率，不是原始次数。'),
'dev-saffran-1996':('abstract','原始摘要：8月龄人工语流的相邻音节统计与短时学习；不等于词义理解，0.9/0.25为本条教学算例。'),
'dev-werner-2001':('abstract','原始摘要：婴儿与成人的纯音/宽带噪声检测差异、心理测量函数及候选因素；不从摘要分离每个因素的因果贡献。'),
'dev-observer-1987':('fulltext','作者机构原始PDF第627—629页摘要与程序原理：观察者yes/no判断、儿童可变行为、空白试次与观察者控制；不采用1987年对现代ABR频率特异性的旧限制作为当前指南。'),
'dev-litovsky-2005':('abstract','原始摘要：4—7岁儿童与成人四选一词语、空间分离、绝对阈值与空间获益的区别；不能直接确认全部双耳神经成熟。'),
'dev-buss-2017':('abstract','原始摘要：学龄儿童与成人一/两说话者、附加噪声及可用时频片段；任务依赖的发展模式。'),
'dev-leibold-2016':('abstract','原始摘要：婴儿、学龄儿童与成人统一观察者检测任务；掩蔽模式和反应偏差，不当作全部词句理解常模。'),
'dev-sharma-2002':('abstract','原始摘要：先天耳聋植入者P1潜伏期与剥夺/植入年龄；3.5和7岁来自样本及神经结局，不是等待期限或全部学习能力界限。'),
'dev-kral-2000':('abstract','原始摘要：先天耳聋猫电刺激和皮层电流源密度的层间活动差异；保留动物及电生理层次，不推算人类手术年龄。'),
'dev-ching-2017':('abstract','原始摘要：LOCHI前瞻性队列、调整后的5岁语言结局；图4三项估计及真实95%CI均来自摘要，不是随机延迟或设备间直接比较。'),
'dev-tomblin-2015':('abstract','原始摘要：OCHL纵向语言增长与助听可听度、验配及使用关系，较晚验配者仍可随经验进步；不将观察性关联写成逐个儿童必然结果。'),
'dev-werker-2024':('abstract','作者回顾的原始摘要及出版方介绍：第一年知觉重组的扩展、分布和词汇机制、不同群体；作为历史与现状定位，不声称新原始实验。'),
'dev-bruner-2025':('abstract','Europe PMC原始摘要：2025年宽带声导抗横断面年龄组比较；声学参数不直接等同语言功能，未声称个体纵向轨迹。')}
def clean(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',s or ''))).strip()
bib={};abstracts=[]
for r in rows:
 key=r['id'];c=r['crossref'];e=r.get('europe_pmc') or {};access,note=notes[key]
 title=clean(c['title'][0]);authors=[' '.join(filter(None,[a.get('given'),a.get('family')])) for a in c['author']]
 if key=='dev-observer-1987':authors[0]='Lynne Werner Olsho'
 if key=='dev-moore-2007':authors[1]='Fred H. Linthicum Jr.'
 pub=clean(c['container-title'][0]);vol=c.get('volume');issue=c.get('issue');page=e.get('pageInfo') or c.get('page')
 if vol:pub+=', '+vol+(('('+issue+')') if issue else '')
 if page:pub+=', '+page
 url='https://doi.org/'+r['doi']
 if key=='dev-observer-1987':url='https://faculty.washington.edu/lawerner/IHL/page11/files/wernerolshoetal87.pdf'
 bib[key]=dict(title=title,authors='; '.join(authors),year=str(c['published']['date-parts'][0][0]),publication=pub,doi=r['doi'],url=url,access=access,supports='2026-10-10：'+note)
 abstracts.append(dict(id=key,doi=r['doi'],title=title,abstract=clean(e.get('abstractText') or c.get('abstract')),pmid=e.get('id'),errors=r['errors']))
bib['dev-gap-1992']=dict(title='Infant auditory temporal acuity: gap detection',authors='L. A. Werner; G. C. Marean; C. F. Halpin; N. B. Spetner; J. M. Gillenwater',year='1992',publication='Child Development, 63(2), 260–272',url='https://pubmed.ncbi.nlm.nih.gov/1611932/',access='abstract',supports='2026-10-10：PubMed原始摘要：不同月龄、频谱控制与观察者间隙检测；个体差异及条件依赖。不填入未核实DOI或常模阈值。')
docs=[
('dev-jcih-2019','Year 2019 Position Statement: Principles and Guidelines for Early Hearing Detection and Intervention Programs — Executive Summary','Joint Committee on Infant Hearing','2019','JCIH official executive summary','https://www.jcih.org/JCIH_2019_Executive_Summary.pdf','官方三页摘要，重点第1—2页：1–3–6与1–2–3服务目标、连续监测和可访问语言支持；未声称已读全部主声明。'),
('dev-jcih-faq-2024','JCIH 2019 Position Statement FAQs: Audiology','Joint Committee on Infant Hearing','2024','JCIH official FAQs, updated 2024-01-01','https://www.jcih.org/docs/JCIH%20Frequently%20Asked%20Questions_Audiology%20(2024).pdf','官方五页听力学FAQ：综合交叉核对、频率耳别ABR、风险随访及早产延长住院的诊断；发育比较不自行推迟识别。'),
('dev-corrected-age','Corrected Age For Preemies','American Academy of Pediatrics','2018（核对2026-10-10）','HealthyChildren.org','https://www.healthychildren.org/English/ages-stages/baby/preemie/Pages/Corrected-Age-For-Preemies.aspx','官方说明：以40周预产期参考计算矫正年龄。34/12/46/6周为本站教学设定，不是听觉常模或改变医学诊断安排。'),
('dev-nidcd-milestones','Speech and Language Developmental Milestones','National Institute on Deafness and Other Communication Disorders','2022（核对2026-10-10）','NIH / NIDCD health information','https://www.nidcd.nih.gov/health/speech-and-language','官方定义及里程碑说明：语言与口语不同、个体发展差异、关注与评估；不复制英文音类清单为普通话常模。'),
('dev-nidcd-screening',"Your Baby’s Hearing Screening and Next Steps",'National Institute on Deafness and Other Communication Disorders','访问日期2026-10-10','NIH / NIDCD health information','https://www.nidcd.nih.gov/health/your-babys-hearing-screening-and-next-steps','官方说明：筛查与后续诊断、持续监测及交流支持；未通过不直接诊断，初次通过不排除迟发变化。')]
for key,title,authors,year,pub,url,note in docs:bib[key]=dict(title=title,authors=authors,year=year,publication=pub,url=url,access='documentation',supports='2026-10-10：'+note)
assert len(bib)==26
(ROOT/'src/data/auditory-development-references.ts').write_text("import type { Reference } from './references';\n\nexport const auditoryDevelopmentReferences: Record<string, Reference> = "+json.dumps(bib,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(DOC/'abstracts-read.jsonl').write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in abstracts)+'\n',encoding='utf-8')
print(json.dumps({'references':len(bib),'doi_records':len(rows)}))
