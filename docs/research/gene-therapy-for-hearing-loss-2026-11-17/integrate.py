from pathlib import Path
import json,re
root=Path('.')
if 'geneTherapyReferences' in (root/'src/data/references.ts').read_text(encoding='utf8'):
    raise SystemExit('Already integrated; do not reapply mutations.')
p=root/'docs/research/gene-therapy-for-hearing-loss-2026-11-17'
keys=['roux','akil','almoyed','askew','gao','yeh','dbmouse','lv','wang','anc80','dboto','jiang','sequential','regeneration']
supports=['耳畸蛋白缺失与胞吐障碍；动物机制','双载体在成熟小鼠中的功能恢复','快速胞吐与囊泡补充恢复不完全；动物实验','Tmc补充与感觉转导；动物实验','显性Tmc1等位基因选择性失活；动物实验','隐性Tmc1碱基编辑及暂时听觉改善；动物实验','DB-OTO启动子、双载体与定向表达；临床前','6名儿童单耳治疗、26周随访及安全性','5名儿童双侧治疗、定位及随访差异','Anc80L65方案、10人及年龄相关探索分析','12名儿童、24周终点与正常敏感性的区分','42人、多中心、最长2.5年与基线因素关联','4名儿童对侧耳再次给药，不代表同耳补打','成年小鼠毛细胞样细胞重编程，不证明人类功能康复']
refs={}
for k,s in zip(keys,supports):
 data=json.loads((p/(k+'.json')).read_text(encoding='utf8'))['resultList']['result']
 x=next((x for x in data if x.get('doi')=='10.1093/pnasnexus/pgae445'),data[0]) if k=='regeneration' else data[0]
 refs['gt-'+k]={'title':re.sub('<[^>]+>','',x['title']).replace('&lt;i&gt;','').replace('&lt;/i&gt;',''),'authors':x['authorString'],'year':x['pubYear'],'publication':x['journalInfo']['journal']['title'],'doi':x['doi'],'url':'https://doi.org/'+x['doi'],'access':'abstract','supports':s+'。2026-11-17 核对 Europe PMC 正式书目信息与摘要；未据摘要推断完整方法或逐时点人数。'}
refs['gt-fda-label']={'title':'OTARMENI prescribing information (Revised 4/2026)','authors':'U.S. Food and Drug Administration; Regeneron Pharmaceuticals, Inc.','year':'2026','publication':'FDA product label','url':'https://www.fda.gov/media/192098/download','access':'documentation','supports':'美国适应证、外毛细胞功能与同耳既往植入限制、给药相关风险和加速批准条件；2026-11-17核对官方说明书相关章节。'}
refs['gt-fda-approval']={'title':'FDA Approves First-Ever Gene Therapy for Treatment of Genetic Hearing Loss Under National Priority Voucher Program','authors':'U.S. Food and Drug Administration','year':'2026','publication':'FDA news release, April 23, 2026','url':'https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher','access':'documentation','supports':'美国2026-04-23加速批准及持续批准的确认性要求；不支持其他地区可及性。'}
(root/'src/data/gene-therapy-references.ts').write_text("import type { Reference } from './references.ts';\n\nexport const geneTherapyReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf8')
f=root/'src/data/references.ts';t=f.read_text(encoding='utf8');t="import { geneTherapyReferences } from './gene-therapy-references.ts';\n"+t;t=t.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...geneTherapyReferences,',1);f.write_text(t,encoding='utf8')
f=root/'src/data/relations.ts';t=f.read_text(encoding='utf8');rels=[('hearing-loss','application','针对特定分子病因与残存细胞条件的听力损失干预。'),('inner-hair-cell','mechanism','OTOF补充以恢复内毛细胞耳畸蛋白相关突触传递为目标。'),('cochlea','related','局部递送需要考虑耳蜗结构、可达性和组织状态。'),('cochlear-implant','related','生物接口修复与电刺激是不同路径，适用条件及效果需分别评价。'),('otoacoustic-emissions','related','外毛细胞相关功能为基线状态提供信息，不证明内毛细胞突触已恢复。'),('auditory-plasticity','related','恢复外周输入后，长期感知使用与语言发展仍需观察。')]
lines='\n'.join("  link('gene-therapy-for-hearing-loss','%s','%s','%s',3),"%x for x in rels)
t=t.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+lines,1);f.write_text(t,encoding='utf8')
for name,needle in [('cochlea','OTOF相关遗传性耳聋提供了前一类机制的具体例子。'),('inner-hair-cell','OTOF 相关遗传性耳聋说明，')]:
 f=root/f'src/content/concepts/{name}.md';t=f.read_text(encoding='utf8');replacement=needle.replace('OTOF相关遗传性耳聋','[OTOF 相关基因治疗](../gene-therapy-for-hearing-loss/)') if name=='cochlea' else '[OTOF 相关基因治疗](../gene-therapy-for-hearing-loss/)说明，';t=t.replace(needle,replacement,1);f.write_text(t,encoding='utf8')
(p/'source-map.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2),encoding='utf8')
print('Registered',len(refs),'references and',len(rels),'relations')
