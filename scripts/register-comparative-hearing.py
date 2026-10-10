"""Register checked bibliography and preserve the existing shared workspace."""
from pathlib import Path
import json
import html
import re
import importlib.util
import yaml

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'docs/research/comparative-hearing-2026-10-10'
entry_source=(ROOT/'src/content/concepts/comparative-hearing.md').read_text(encoding='utf-8')
(RESEARCH/'frontmatter.json').write_text(json.dumps(yaml.safe_load(entry_source.split('---',2)[1]),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
raw = json.loads((RESEARCH/'verified-metadata.json').read_text(encoding='utf-8'))
raw += json.loads((RESEARCH/'animal-models-metadata.json').read_text(encoding='utf-8'))
rows = {r['requested_doi'].lower(): r for r in raw}
rows['10.1016/s1095-6433(00)00232-4'] = {
    'title': 'Study of sound localization by owls and its relevance to humans',
    'authorString': 'M. Konishi', 'pubYear': '2000', 'id': '10989338',
    'journalInfo': {'volume': '126', 'issue': '4', 'journal': {'title': 'Comparative Biochemistry and Physiology Part A: Molecular & Integrative Physiology'}},
    'pageInfo': '459–469', 'metadata_source': 'https://pubmed.ncbi.nlm.nih.gov/10989338/'
}
plan = [
 ('comp-konishi-2000','10.1016/S1095-6433(00)00232-4','abstract','阅读PubMed摘要与书目；支持动物模型外推问题、仓鸮与人类定位比较的背景；不把综述的机制观点视作人体回路直接记录。'),
 ('comp-carr-1990','10.1523/JNEUROSCI.10-10-03227.1990','abstract','阅读原研究摘要，核对仓鸮层状核输入时序、延迟线与符合检测证据；正文不报告摘要以外的刺激参数或逐图结果。'),
 ('comp-mcalpine-2001','10.1038/86049','abstract','阅读PubMed原研究摘要并核对物种索引；支持豚鼠下丘最佳频率、ITD调谐斜率及双通道读出解释；不是人体生理证据。'),
 ('comp-knudsen-1991','10.1126/science.2063209','abstract','阅读原研究摘要；核对棱镜改变发育仓鸮视觉经验后听觉空间调谐改变；不外推成人康复疗效。'),
 ('comp-shadron-2023','10.7554/eLife.84760','fulltext','阅读摘要及欧洲PMC全文相关引言、结果与讨论，核对发育期面盘处理、ITD可靠性与频率调谐关系；未重新分析单元记录。'),
 ('comp-ming-2020','10.1073/pnas.2001105117','abstract','阅读原研究摘要与出版社公开Significance；核对大棕蝠、最低FM1频率与脉冲回声归属的行为及模型解释；全文XML访问失败，未核对完整实验方法或运行SCAT模型。'),
 ('comp-beleyur-2019','10.1073/pnas.1821722116','abstract','阅读原研究摘要并核对作者代码归档；支持有生物参数约束的群体回声检测模型及空间限制；不能作为自然群飞逐只感知测量，未运行代码。'),
 ('comp-norman-2021','10.1371/journal.pone.0252330','fulltext','阅读摘要、方法中参与者与训练任务、相关结果和讨论；核对14名有视力与12名盲人参与者、10周20次训练、迁移及自述随访限制；没有重分析数据。'),
 ('comp-robert-1996','10.1007/BF00193432','abstract','阅读原研究摘要；核对520 μm耳间距、鼓膜耦合、激光测振与机械响应中的方向线索增强。几何算例为独立计算，未作为原文实测数值。'),
 ('comp-wilmott-2016','10.1038/srep29957','fulltext','阅读摘要及全文器件结构、方向响应与实验相关段落；支持窄带MEMS传感器实物测量、余弦方向歧义和双传感器组合；没有助听器使用者试验。'),
 ('comp-liu-2025','10.3390/mi16040451','fulltext','阅读全文摘要、机械分析、仿真结果和结论；相关性能属于有限元仿真，不是已制作器件测量或人体应用证据。'),
 ('comp-corwin-1988','10.1126/science.3381100','abstract','阅读原研究摘要；核对鸡声损伤后感受细胞替代及支持细胞分裂的解释；未据此宣称已证明人体功能恢复。'),
 ('comp-ryals-1988','10.1126/science.3381101','abstract','阅读原研究摘要；核对成年鹌鹑损伤后细胞数量与标记胸腺嘧啶核苷的再生证据；正文不报告摘要之外的暴露参数。'),
 ('comp-stone-2000','10.1073/pnas.97.22.11714','fulltext','XML访问失败后阅读作者机构公开PDF的摘要、支持细胞来源及细胞分化相关段落；支持鸟类再生研究范围、来源及成熟与连接需要分层考察；未逐项复核综述引用的原始数据。'),
 ('comp-function-2013','10.1016/j.heares.2012.11.019','abstract','阅读原文摘要；支持鸟类再生后纯音敏感性与复杂声学知觉恢复不完全同步；全文XML访问失败，未逐一核对该综述中的原始行为研究。'),
 ('comp-gunewardene-2025','10.1016/j.heares.2024.109170','abstract','阅读原研究摘要，核对成年小鼠Atoh1/Pou4f3/Kdm1a组合干预、双标志细胞变化及Myo阳性细胞数量未显著不同的有限结果；未宣称听觉恢复。'),
 ('comp-encke-2022','10.1038/s42003-022-04098-x','fulltext','阅读摘要及全文模型、行为资料比较与讨论段落；支持双通道计算与既有人类双耳去掩蔽资料的拟合；不作为人体回路唯一实现的证明。'),
 ('comp-ohlemiller-2016','10.1007/s10162-016-0589-1','abstract','阅读作者综述摘要、PubMed图注与书目；支持小鼠遗传研究用途、品系及年龄影响与模型外推原则。全文XML访问失败，未逐项复核其引用的原始实验。'),
 ('comp-rodents-2024','10.1016/j.lfs.2024.123156','abstract','阅读综述摘要与书目；支持小鼠、大鼠、豚鼠、蒙古沙鼠及南美栗鼠属于常用感音神经性听力损失研究模型，及按问题选择模型的原则；不提供特定品系或损伤参数的选型结论。'),
 ('comp-chinchilla-2019','10.1121/1.5132950','fulltext','阅读作者综述全文中听力范围、行为研究、结构生理联系与总结相关段落；支持南美栗鼠模型用途及与人类听力范围重叠；没有逐项复核其引用的原始研究，不外推损伤剂量或言语理解。'),
 ('comp-snyder-1990','10.1016/0378-5955(90)90030-S','abstract','阅读原研究摘要与书目；支持新生期致聋猫、慢性耳蜗电刺激及下丘表征研究用途；不外推儿童植入后语言收益。'),
 ('comp-brainard-2000','10.1038/35008083','abstract','阅读原研究摘要与出版社书目；支持成年斑胸草雀听觉反馈、鸣唱维持及前脑回路可塑性研究；不将鸣唱等同于人类语言。'),
 ('comp-bendor-2005','10.1038/nature03867','abstract','阅读原研究摘要与书目；支持绒猴听觉皮层对纯音与同基频缺失基频复合音的音高选择性响应；全文XML失败，未引用未核验的刺激参数或等同人体主观体验。'),
 ('comp-owens-2008','10.1371/journal.pgen.1000020','fulltext','阅读PLOS原研究全文摘要、侧线结构、遗传与化合物筛选及哺乳动物验证相关结果；支持侧线毛细胞筛选用途，并区分水体运动感受、内耳听觉和人体功能；未运行筛选或重分析数据。'),
 ('comp-eberl-1997','10.1073/pnas.94.26.14837','fulltext','XML失败后阅读作者机构公开PDF的引言、听觉行为筛选与触角去除结果；支持果蝇听觉遗传筛选与触角感受结构；保留行为缺陷可能并非听觉特异的限制。'),
]
refs = {}
ledger = []
for rid,doi,access,support in plan:
    r=rows[doi.lower()]
    assert r.get('title'), doi
    title=re.sub('<[^>]+>','',html.unescape(r['title'])).rstrip('.')
    j=r['journalInfo']
    pub=j['journal']['title'] + ', ' + j.get('volume','')
    if j.get('issue'): pub+='('+j['issue']+')'
    if r.get('pageInfo'): pub+=', '+r['pageInfo']
    refs[rid]={'title':title,'authors':r['authorString'],'year':r['pubYear'],'publication':pub,
               'doi':doi,'url':('https://pmc.ncbi.nlm.nih.gov/articles/'+r['pmcid']+'/') if access=='fulltext' else 'https://pubmed.ncbi.nlm.nih.gov/'+r['id']+'/',
               'access':access,'supports':support}
    if rid == 'comp-stone-2000':
        refs[rid]['url']='https://depts.washington.edu/rubelab/personnel/Stone%2C%20Rubel%2C%20PNAC%2000.pdf'
    if rid == 'comp-eberl-1997':
        refs[rid]['url']='https://genepath.med.harvard.edu/perrimon/papers/eberlpnas.pdf'
    ledger.append({'id':rid,**refs[rid], 'grade':'Background' if rid in ['comp-konishi-2000','comp-stone-2000','comp-function-2013','comp-ohlemiller-2016','comp-rodents-2024','comp-chinchilla-2019'] else 'Core',
                   'selection_reason':support,'checked_at':'2026-10-10','status':'source checked; not professional review'})
(ROOT/'src/data/comparative-hearing-references.ts').write_text("import type { Reference } from './references';\n\nexport const comparativeHearingReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(RESEARCH/'source-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Generate a consistent relevance prompt and deduplicate the bounded discovery pool.
pool=[]
for name in ['topic-discovery.json','owl-backward.json','owl-forward.json','fly-backward.json','fly-forward.json','bird-backward.json','bird-forward.json']:
    for item in json.loads((RESEARCH/name).read_text(encoding='utf-8')):
        item['discovery_from']=name
        pool.append(item)
seen=set();unique=[]
for item in pool:
    key=(item.get('doi') or item.get('id') or item['title'].lower()).lower()
    if key in seen: continue
    seen.add(key);unique.append(item)
(RESEARCH/'candidate-pool.json').write_text(json.dumps(unique,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
spec=importlib.util.spec_from_file_location('judge',Path('C:/Users/mengq/.codex/skills/deep-research/scripts/judge_relevance.py'))
judge=importlib.util.module_from_spec(spec);spec.loader.exec_module(judge)
(RESEARCH/'relevance-prompt.txt').write_text(judge.build_prompt(unique[0],'动物听觉对人类机制研究、仿生传感器与听觉修复的启示'),encoding='utf-8')
print('Registered',len(refs),'sources; original candidate pool deduplicated:',len(unique))
