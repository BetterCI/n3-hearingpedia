"""Build verified bibliography from the archived original records, without new network access."""
from pathlib import Path
import json, re, html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-aging-2026-10-10'
rows=json.loads((OUT/'verified-metadata.json').read_text(encoding='utf-8-sig'))
notes={
'aging-schuknecht-1993':('abstract','病理分类、混合与不能归类的标本；历史上的耳蜗机械性假说不等同中耳传导性损失，也不用于个体分型。'),
'aging-wu-2020':('abstract','原始摘要：人体颞骨中毛细胞损失与听阈预测、血管纹变量及听力图斜率的限制。全文访问未完成；不据此排除血管纹正常功能或所有人群的机制。'),
'aging-genetics-2022':('abstract','原始摘要及原文检索可见Results/Discussion：广泛听损表型的遗传关联与小鼠细胞表达定位；保守按摘要记录，不作为老年血管纹功能的直接测量。'),
'aging-fullgrabe-2015':('fulltext','出版方摘要、Introduction和Methods相关段：听力图匹配的年龄组比较、噪声中言语、时域与认知因素；控制与选择样本限制。'),
'aging-schoof-2014':('fulltext','出版方Methods、Results 3.2/3.4与总结：不同掩蔽条件下的年龄差异以及AM/FM/间隙任务的阴性结果；不合并为普遍时域缺陷。'),
'aging-hopkins-2011':('abstract','原始摘要：年龄、听损、频率选择性与两种TFS测量的关系；不把所有指标归为一个时间分辨率。'),
'aging-anderson-2012':('abstract','原始摘要：语音诱发响应时序与噪声中编码的年龄比较；不将头皮响应直接定位为某一种突触损失。'),
'aging-presacco-2016':('abstract','原始摘要：脑干和皮层语音响应的年龄及噪声差异；增强响应不等于行为更好。全文API未成功，不报告未核实的细节。'),
'aging-levels-2021':('abstract','原始摘要：高低声级下时域与言语任务的年龄效应，多数任务未出现预期的更强高声级效应；阴性结果约束简化突触病变解释，不否定人体神经退变。正式卷期2021，在线2020。'),
'aging-cassarly-2020':('abstract','原始摘要：HHIE/HHIA的因子和项目分析及修订问卷；自述影响与病变定位有别。'),
'aging-peelle-2011':('abstract','原始摘要：听觉状态与语言相关功能响应、听觉皮层灰质的观察性关联；不推断助听器逆转或损失单向导致全部改变。'),
'aging-lin-2011':('abstract','原始摘要：听力损失与随访中的痴呆风险关联；观察性风险不能替代因果或干预结论。'),
'aging-mocah-2023':('fulltext','出版方原文Methods与Discussion相关段：书面呈现及部分项目替换后验证MoCA-H；版本、语言与验证人群限制，筛查不等于诊断。'),
'aging-humes-2017':('abstract','PubMed原始摘要及出版方检索可见设计：专业验配、消费者决定模式与安慰剂的短期试验；具体人群和支持模式限制。'),
'aging-social-2025':('fulltext','Europe PMC原文XML摘要、Methods与Discussion：ACHIEVE的探索性社会网络/孤独结局，统计差异与临床意义有别；不据此认定认知中介路径。'),
'aging-training-2013':('abstract','原始摘要：老年听者训练后部分时序与行为变化；不能推断神经再生、长期保持或无条件迁移。'),
'aging-cochrane-2026':('abstract','Europe PMC原始2026年更新摘要（16项随机试验、2261人）；交流获益与其他生活/认知结局的不确定性。官方网页仍混有旧版5项试验摘要，未混用旧版数字。'),
}
def clean(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',s or ''))).strip()
bib={'aging-nidcd':dict(title='Age-Related Hearing Loss (Presbycusis)',authors='National Institute on Deafness and Other Communication Disorders',year='2023（核对2026-10-10）',publication='NIH / NIDCD health information',url='https://www.nidcd.nih.gov/health/age-related-hearing-loss',access='documentation',supports='2026-10-10：阅读官方公众说明全文，最后更新2023-03-17；渐进双耳变化、多因素背景、评估与交流支持。')}
abstracts=[]
for r in rows:
 c=r['crossref'];e=r.get('europe_pmc') or {};key=r['id']
 abstracts.append(dict(id=key,doi=r['doi'],title=clean(c['title'][0]),abstract=clean(e.get('abstractText') or c.get('abstract')),pmid=e.get('id'),pmcid=e.get('pmcid')))
 if key not in notes:continue
 authors=[' '.join(filter(None,[a.get('given'),a.get('family')])) for a in c['author']]
 if key=='aging-fullgrabe-2015':authors[0]='Christian Füllgrabe' # Publisher's original spelling; Crossref has mojibake.
 if len(authors)>8:authors=authors[:6]+['et al.']
 year=str(c['published']['date-parts'][0][0])
 if key=='aging-fullgrabe-2015':year='2015'
 if key=='aging-levels-2021':year='2021（在线2020）'
 if key=='aging-cassarly-2020':year='2020（在线2019）'
 pub=clean(c['container-title'][0]);vol=c.get('volume');issue=c.get('issue');page=e.get('pageInfo') or c.get('page')
 if vol:pub+=', '+vol+(('('+issue+')') if issue else '')
 if page:pub+=', '+page
 access,support=notes[key]
 url=('https://pmc.ncbi.nlm.nih.gov/articles/'+e['pmcid']+'/') if access=='fulltext' and e.get('pmcid') else 'https://doi.org/'+r['doi']
 if key in ['aging-fullgrabe-2015','aging-schoof-2014']:url='https://www.frontiersin.org/journals/aging-neuroscience/articles/'+r['doi']+'/full'
 if key=='aging-mocah-2023':url='https://agsjournals.onlinelibrary.wiley.com/doi/'+r['doi']
 bib[key]=dict(title=clean(c['title'][0]),authors='; '.join(authors),year=year,publication=pub,doi=r['doi'],url=url,access=access,supports='2026-10-10：'+support)
assert len(bib)==18
(ROOT/'src/data/auditory-aging-references.ts').write_text("import type { Reference } from './references';\n\nexport const auditoryAgingReferences: Record<string, Reference> = "+json.dumps(bib,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(OUT/'abstracts-read.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in abstracts)+'\n',encoding='utf-8')
print(json.dumps(dict(new_references=len(bib),archived_original_abstracts=len(abstracts)),ensure_ascii=False))
