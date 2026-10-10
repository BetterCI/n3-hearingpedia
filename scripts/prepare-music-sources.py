"""Generate the scoped reference module from verified records and explicit reading notes."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/'docs/research/music-perception-2026-10-10'
records=json.loads((DOC/'verified-metadata.json').read_text(encoding='utf-8'))
notes={
 'music-dowling-1978':('metadata','仅核对Crossref与作者机构书目；原文获取未完成。限于旋律记忆中音阶与轮廓研究的历史定位，不用于原始实验结果或参数。'),
 'music-krumhansl-1982':('metadata','Crossref与PubMed核对，PubMed无摘要，出版方原文未获取。仅用于调性组织研究的历史定位，不引用探测音数据或原始结果。'),
 'music-large-1999':('abstract','阅读作者机构原始PDF首页的检索可见摘要：动态注意的内部振荡、对预期时刻的关注及事件速度变化。全文打开失败；不报告原始实验参数、拟合或神经振荡因果结论。'),
 'music-nozaradan-2011':('abstract','原始摘要：相同拍点上想象二拍与三拍分组、脑电周期成分与解释条件有关。PMC访问不稳定，本条保守按摘要记录；不报告未核实的频率、样本或效应量。'),
 'music-jacoby-2024':('abstract','原始摘要及出版方检索可见Discussion：15国39组、迭代节奏再现、小整数比倾向与群体差异。全文页访问受限，未逐项核验全部组别或数据。'),
 'music-consonance-2010':('fulltext','作者存档原文首页、Results与Discussion相关段：分离谐波结构与拍相关因素、个体差异及音乐经验；图3为独立解析教学计算，不是原始偏好数据。'),
 'music-tsimane-2016':('fulltext','作者存档原文首页与相关结果：Tsimane’及比较群体的协和偏好、粗糙声评价及辨别控制。只使用对应范围，不以群体差异证明随机暴露的因果效应。'),
 'music-integration-2026':('fulltext','作者存档原文第1—4页相关段、摘要与方法：全球文化／市场接触指标与协和偏好；该指标包含多类经验。正式卷期2026，在线2025-10-14；保留观察性比较限制。'),
 'music-song-2022':('fulltext','PMC原文Summary、Intracranial recordings及Song selectivity：颅内响应分解、功能成像定位、对歌唱音乐的选择性及标准声学解释的检验。成分与记录不等于单神经元计数或唯一音乐中枢。'),
 'music-salimpoor-2011':('abstract','阅读原始摘要：强烈音乐愉悦条件下PET、多巴胺与功能成像的预期／高峰区分；不把普通BOLD活动当作多巴胺的直接测量。'),
 'music-cheung-2019':('fulltext','作者原文Results、图1及STAR Methods的模型段：条件概率、熵、意外度及其与愉悦的交互。图4只用三候选教学概率，不实现IDyOM或复现原始效应。'),
 'music-mbea-2003':('abstract','PubMed原始摘要：音乐能力障碍、MBEA开发与验证的背景；分项具体操作另引用Cooper等2008原始研究正文。'),
 'music-proms-2012':('fulltext','出版方原文Introduction、Construction及相关方法段：多维音乐知觉技能、材料控制与训练身份分组的限制。仅使用概念和任务范围，不报告未核对的常模。'),
 'music-goldmsi-2014':('fulltext','出版方原始摘要与正文引言可见内容：一般人群、多维音乐经验及自述与听觉任务的关系。训练的相关性不能代替因果作用。'),
 'music-galvin-2007':('abstract','PubMed原始摘要Methods、Results：五音等时序列、九种轮廓、音程／音区、训练前后及熟悉旋律任务；不把初步改善视为所有日常体验获益。'),
 'music-kong-2004':('abstract','原始结构化摘要：速度辨别、节奏型识别、保留／去除节奏的旋律辨认、实际CI与正常听力声码器。保留任务间不同结果，不称全部节奏任务正常。'),
 'music-gfeller-2006':('abstract','原始摘要：Hybrid与长电极及正常听力比较，实际歌曲和乐器识别；低频声学听力的潜在价值。初步样本与配置差异不形成个体获益保证。'),
 'music-timbre-ci-2008':('abstract','原始摘要：六种乐器下MCI、个体表现差异及音乐经验关联；不直接据相关关系证明训练的因果效应。'),
 'music-hearingaid-2014':('abstract','原始摘要：助听器用户的现场／录音音乐聆听调查、获益与失真及音质问题。用户报告不直接定位处理算法的因果作用。'),
 'music-mehr-2019':('abstract','原始摘要：民族志与歌曲录音语料，音乐活动的广泛存在及用途、结构差异。限于研究观察范围，不把一种音乐体系当作普遍规范。'),
 'music-chen-2008':('abstract','原始摘要：两项fMRI实验、听节奏及敲击、未预告敲击条件的运动相关区域响应；活动不单独证明必要性。'),
 'music-training-2018':('fulltext','出版方Materials and Methods与Results相关段：八周儿童普通话CI轮廓训练、未训练音区、声调和安静句子、训练后保留。摘要与正文的参与者描述不一致，本条不报告样本量或数值效应；不以正常听力比较替代同期未训练CI对照。'),
 'music-mbea-ci-2008':('fulltext','PMC原文Methods的MBEA任务与刺激、Results和Discussion相关段：六分项、轮廓与间隔操纵、实际CI与正常听力声码器比较。任务表现和模拟通道数不能换算为全部音乐体验或电极常模。'),
}
urls={
 'music-large-1999':'https://musicdynamicslab.media.uconn.edu/wp-content/uploads/sites/433/2016/03/LargeJones1999Ahedits.pdf',
 'music-consonance-2010':'https://mcdermottlab.mit.edu/papers/McDermott_Lehr_Oxenham_2010_consonance_individual_differences.pdf',
 'music-tsimane-2016':'https://mcdermottlab.mit.edu/papers/McDermott_etal_2016_consonance.pdf',
 'music-integration-2026':'https://mcdermottlab.mit.edu/papers/McPherson_etal_2025_global_integration.pdf',
 'music-cheung-2019':'https://www.marcus-pearce.com/assets/papers/CheungEtAl2019.pdf',
 'music-proms-2012':'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052508',
 'music-goldmsi-2014':'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0089642',
 'music-training-2018':'https://journals.sagepub.com/doi/10.1177/2331216518759214',
}
refs={}
for row in records:
 rid=row['id'];cr=row.get('crossref');ep=row.get('europe_pmc') or {}
 assert cr and cr['title'],rid
 title=re.sub('<[^>]+>','',cr['title'][0]).rstrip('.')
 if rid=='music-mbea-2003':title='Varieties of musical disorders. The Montreal Battery of Evaluation of Amusia'
 authors=[' '.join([a.get('given',''),a.get('family','')]).strip() for a in cr['author']]
 if len(authors)>8:authors=authors[:6]+['et al.']
 pub=cr['container-title'][0]
 if cr.get('volume'):pub+=', '+cr['volume']
 if cr.get('issue'):pub+='('+cr['issue']+')'
 if cr.get('page'):pub+=', '+cr['page']
 dates=cr.get('published-print') or cr.get('published')
 year=str(dates['date-parts'][0][0])
 if rid=='music-integration-2026':year='2026（在线2025）'
 access,supports=notes[rid]
 url=urls.get(rid) or ('https://pmc.ncbi.nlm.nih.gov/articles/'+ep['pmcid']+'/' if access=='fulltext' and ep.get('pmcid') else 'https://pubmed.ncbi.nlm.nih.gov/'+ep['id']+'/' if ep.get('id') else 'https://doi.org/'+row['doi'])
 refs[rid]={'title':title,'authors':'; '.join(authors),'year':year,'publication':pub,'doi':row['doi'],'url':url,'access':access,'supports':'2026-10-10：'+supports}
out="import type { Reference } from './references';\n\nexport const musicPerceptionReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n'
(ROOT/'src/data/music-perception-references.ts').write_text(out,encoding='utf-8')
print(json.dumps({'references_created':len(refs),'metadata_only':[r for r in refs if refs[r]['access']=='metadata']},ensure_ascii=False))
