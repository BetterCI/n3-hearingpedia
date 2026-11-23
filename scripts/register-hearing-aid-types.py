"""Idempotent integration and evidence-map refresh for the types entry."""
from pathlib import Path
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
def edit(name, fn):
    p=ROOT/name
    s=p.read_text(encoding='utf-8')
    t=fn(s)
    if t!=s: p.write_text(t,encoding='utf-8')

edit('src/content/concepts/hearing-aid-types.md',lambda s:s.replace(',"biomedical-engineering"','').replace('types-peters-cingle-2021','binaural-hearing-cros'))
edit('src/data/references.ts',lambda s:s if '...hearingAidTypesReferences' in s else "import { hearingAidTypesReferences } from './hearing-aid-types-references.ts';\n"+s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...hearingAidTypesReferences,'))
edit('src/data/attention-binaural-temporal-references.ts',lambda s:s.replace('"url": "https://pubmed.ncbi.nlm.nih.gov/34644322/",\n    "access": "abstract",\n    "supports": "原始摘要及书目：单侧失聪 CINGLE 随机研究，转送与植入结果的空间配置及短期范围；不作个体治疗建议。",','"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8513831/",\n    "access": "fulltext",\n    "supports": "2026-11-24 阅读公开全文的摘要、Study design、噪声中言语结果及讨论：成人单侧聋的空间配置依赖；随机分配CI或试用顺序后，BCD/CROS/不治疗由参与者选择，最终四组不全为直接随机分组。不作个体治疗建议。",'))
links=[
('hearing-aid','related','按部件位置、耳道耦合与信号路由理解装置形式。',3),
('hearing-aid-prescription','related','先明确目标输出，再核查外形与耦合能否实现。',3),
('real-ear-measurement','related','结构和耦合选择需要实际耳内输出验证。',3),
('hearing-loss','related','分耳听觉条件和频率分布影响候选方案。',3),
('binaural-hearing','related','区分两耳独立输入与CROS跨耳转送。',3),
('air-and-bone-conduction','related','传声途径与装置外形属于不同分类维度。',2),
('hearing-aid-benefit-and-outcomes','related','类型适用性还需操作、交流和日常获益评价。',2),
('cochlear-implant','related','比较声学或机械补偿与电刺激的系统边界。',2),
]
def relations(s):
    additions=''.join(f'  link("hearing-aid-types","{target}","{kind}","{note}",{strength}),\n' for target,kind,note,strength in links if f'link("hearing-aid-types","{target}"' not in s)
    return s.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n'+additions) if additions else s
edit('src/data/relations.ts',relations)
edit('src/data/paths.ts',lambda s:s.replace("slugs:['hearing-aid','wide-dynamic-range-compression'","slugs:['hearing-aid','hearing-aid-types','wide-dynamic-range-compression'").replace("slugs:['hearing-aid','hearing-aid-prescription'","slugs:['hearing-aid','hearing-aid-types','hearing-aid-prescription'"))
for slug, note in [
('hearing-aid','各类装置的定义、部件位置、典型适用条件及结构示意，见[助听器类型](../hearing-aid-types/)；外形、开放程度与跨耳路由需要分别描述。'),
('hearing-aid-prescription','目标能否实现还取决于受话器、外形和耳道耦合。不同结构的比较见[助听器类型](../hearing-aid-types/)，选择后仍需核查实际耳内输出。')]:
    edit(f'src/content/concepts/{slug}.md',lambda s: s if '../hearing-aid-types/' in s else re.sub(r'last_updated: "[^"]+"','last_updated: "2026-11-24"',s).rstrip()+'\n\n'+note+'\n')

p=ROOT/'docs/research/wiki-evidence-map.json'
data=json.loads(p.read_text(encoding='utf-8'))
for slug in ['hearing-aid-types','hearing-aid','hearing-aid-prescription']:
    s=(ROOT/f'src/content/concepts/{slug}.md').read_text(encoding='utf-8')
    front,body=s[4:].split('\n---\n',1)
    entry={'slug':slug,'knowledge_area':re.search(r'knowledge_area: "([^"]+)"',front)[1],'kind':re.search(r'kind: "([^"]+)"',front)[1],'chinese_characters':len(re.findall(r'[\u3400-\u9fff]',body)),'body_characters':len(body),'sections':len(re.findall(r'^## ',body,re.M)),'subsections':len(re.findall(r'^### ',body,re.M)),'reference_ids':json.loads(re.search(r'^references: (\[.*\])',front,re.M)[1]),'wiki_links':list(dict.fromkeys(re.findall(r'\.\./([^/]+)/',body)))}
    old=next((e for e in data['entries'] if e['slug']==slug),None)
    if old: old.update(entry)
    else: data['entries'].append(entry)
    if slug=='hearing-aid-types': print(json.dumps(entry,ensure_ascii=False))
data['date']='2026-11-24'
data['relations']=int(subprocess.check_output(['node','--input-type=module','-e',"import {knowledgeRelations} from './src/data/relations.ts'; console.log(knowledgeRelations.length)"],cwd=ROOT,text=True))
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
