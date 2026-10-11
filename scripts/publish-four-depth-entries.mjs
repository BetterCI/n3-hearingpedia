// One-time integration of the four author-approved 2026-10-11 drafts.
// Run from the repository root before these concept routes exist.
// Keeps professional-review status separate from publication and preserves drafts.
import { readFile, writeFile, mkdir, copyFile, readdir, access } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { parseFrontmatter } from '@astrojs/markdown-remark';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';

const date='2026-10-12';
const entries=[
 ['outer-middle-ear-transmission','outer-middle-ear'],
 ['interaural-level-difference','ild'],
 ['acoustic-immittance-tympanometry','immittance'],
 ['real-ear-measurement','real-ear'],
];
for(const [slug] of entries){
 try { await access(`src/content/concepts/${slug}.md`); throw new Error(`Already integrated: ${slug}`); }
 catch(e){ if(e.code!=='ENOENT')throw e; }
}
const doi=d=>d?.toLowerCase().replace(/^https?:\/\/doi.org\//,'').trim();
const url=u=>u?.replace(/\/$/,'').toLowerCase();
const known={...references}, added={}, mappings={};
const overrides={
 'nidcd-hearing':'nidcd-hearing-2022',
 'asha-adult-assessment':'pure-tone-audiometry-adult-assessment',
 'bsa-tympanometry-2024-2026':'audiology-bsa-immittance',
 'kan-mismatch-2013':'binaural-hearing-kan',
};
for(const [slug,dir] of entries){
 const records=JSON.parse(await readFile(`docs/research/${dir}-2026-10-11/references.json`,'utf8'));
 const map={};
 for(const r of records){
  const existing=overrides[r.id] || (known[r.id] ? r.id : Object.keys(known).find(id=>
   (r.doi&&doi(known[id].doi)===doi(r.doi))||url(known[id].url)===url(r.url)));
  if(existing){ assert(known[existing]); map[r.id]=existing; }
  else {
   const {id,relevance,verified_at,verification_date,pmid,pmcid,...record}=r;
   record.year=String(record.year);
   added[id]=record; known[id]=record; map[id]=id;
  }
 }
 mappings[slug]=map;
}

function insertBefore(text,needle,heading){
 assert(text.includes(needle),needle); return text.replace(needle,`### ${heading}\n\n${needle}`);
}
const newEvidence=[];
for(const [slug] of entries){
 let source=(await readFile(`docs/drafts/${slug}.md`,'utf8')).replaceAll('\r\n','\n');
 const {frontmatter:meta}=parseFrontmatter(source);
 const ids=meta.references.map(id=>mappings[slug][id]);
 assert.equal(new Set(ids).size,ids.length,slug);
 source=source.replace(/^references: .*$/m,`references: ${JSON.stringify(ids)}`)
  .replace(/^last_updated: .*$/m,`last_updated: "${date}"`)
  .replace(/^order: .*$/m,`batch: 3\norder: ${107+entries.findIndex(([s])=>s===slug)}`)
  .replace(/^(## )\d+\. /gm,'$1')
  .replaceAll('本草稿','本文').replaceAll('随草稿保存','随词条保存');
 for(const [old,id] of Object.entries(mappings[slug]))source=source.replaceAll(`#ref-${old})`,`#ref-${id})`).replaceAll(`#ref-${old}"`,`#ref-${id}"`);
 source=source.replaceAll(`assets/${slug}/`,`/n3-hearingpedia/figures/${slug}/`);
 source=source.replace(/\n\*\*当前状态：待作者确认[^\n]+\n?/,'\n**审阅状态：AI辅助编写，尚未完成专业审阅。** 文献核对不代表临床结论已经获得专业审核。\n');
 if(slug==='outer-middle-ear-transmission'){
  source=source.replace('鼓室图正是通过改变耳道静压','[鼓室测量](../acoustic-immittance-tympanometry/)正是通过改变耳道静压');
  source=source.replace('与双耳时间差、强度差共同参与','与双耳时间差、[双耳强度差](../interaural-level-difference/)共同参与');
  source=source.replace('及其验配则需要区分设备输出与实际耳道声学条件','及其[真耳测量](../real-ear-measurement/)则需要区分设备输出与实际耳道声学条件');
 } else if(slug==='interaural-level-difference'){
  source=source.replace('耳廓、躯干、耳道入口以及声源仰角也参与方向滤波','[外耳传声](../outer-middle-ear-transmission/)、躯干以及声源仰角也参与方向滤波');
  source=source.replace('输入处的ILD、耳模或接收器输出的ILD和鼓膜处的ILD需分开测量','输入处的ILD、耳模或接收器输出的ILD和鼓膜处的ILD需分开测量；耳道响应可联系[真耳测量](../real-ear-measurement/)理解');
 } else if(slug==='acoustic-immittance-tympanometry'){
  source=source.replace('利用耳道内声学响应评估外耳与中耳机械状态','利用耳道内声学响应评估[外耳与中耳](../outer-middle-ear-transmission/)机械状态');
  for(const [needle,heading] of [
   ['在一个明确的测量平面','端口定义与单位'],
   ['声压与流动存在相位关系','实部、虚部与历史显示单位'],
   ['在成人低频近似下','耳道补偿与常见指标'],
   ['在刚性、密闭、尺寸远小于波长','等效容积与复数相减'],
   ['在单端口、线性、近似无损管道中','反射系数与功率比例'],
   ['由 $Z/Z_0=','相位信息与传声边界'],
  ])source=insertBefore(source,needle,heading);
 } else {
  source=source.replace('外耳几何、鼓膜负载','[外耳与中耳传声](../outer-middle-ear-transmission/)涉及的几何和鼓膜负载');
  source=source.replace('耳模、耳道声学或中耳状况改变时','耳模、耳道声学或[中耳状况](../acoustic-immittance-tympanometry/)改变时');
  source=source.replace('真耳压力测量不能单独验证双耳定位、耳间线索或认知负荷','真耳压力测量不能单独验证双耳定位、[耳间声级线索](../interaural-level-difference/)或认知负荷');
  for(const [needle,heading] of [
   ['术语中的R表示response','响应与增益的定义'],
   ['REOR可显示耳模','堵耳响应与功能增益'],
   ['**真耳—耦合腔差值**','转换定义与坐标'],
   ['真实系统需要处理泡沫耳塞','耦合修正与适用条件'],
   ['研究“REM是否有益”时','研究设计与比较条件'],
   ['言语可听性也应独立报告','可听性与实际获益'],
  ])source=insertBefore(source,needle,heading);
 }
 await writeFile(`src/content/concepts/${slug}.md`,source);
 await mkdir(`public/figures/${slug}`,{recursive:true});
 for(const file of await readdir(`docs/drafts/assets/${slug}`))if(/\.(svg|png)$/.test(file))await copyFile(`docs/drafts/assets/${slug}/${file}`,`public/figures/${slug}/${file}`);
 const {content:body,frontmatter:m}=parseFrontmatter(source);
 newEvidence.push({slug,knowledge_area:m.knowledge_area,kind:m.kind,chinese_characters:(body.match(/[\u3400-\u9fff]/g)||[]).length,body_characters:body.length,sections:(body.match(/^## /gm)||[]).length,subsections:(body.match(/^### /gm)||[]).length,reference_ids:m.references,wiki_links:[...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(v=>v[1]))],status:m.status,depth:m.depth});
}
await writeFile('src/data/four-depth-entries-references.ts',`import type { Reference } from './references.ts';\n\nexport const fourDepthEntriesReferences: Record<string, Reference> = ${JSON.stringify(added,null,2)};\n`);
let refsFile=await readFile('src/data/references.ts','utf8');
refsFile=`import { fourDepthEntriesReferences } from './four-depth-entries-references.ts';\n`+refsFile.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...fourDepthEntriesReferences,');
await writeFile('src/data/references.ts',refsFile);

const edges=[
 ['outer-middle-ear-transmission','sound-waves-and-propagation','related','传播、复数压力与边界条件构成传声的物理基础。',3],
 ['outer-middle-ear-transmission','cochlea','mechanism','传声在耳蜗入口形成机械与液体声学驱动，入口量不等于感觉换能。',3],
 ['outer-middle-ear-transmission','hearing-loss','related','外中耳机械改变与行为听阈需结合病理及测量解释。',3],
 ['outer-middle-ear-transmission','acoustic-immittance-tympanometry','measured-by','声导抗观察输入端机械关系，不能直接代替完整传递函数。',3],
 ['outer-middle-ear-transmission','real-ear-measurement','measured-by','探管测量耳道声压，需保留位置、反射与负载条件。',3],
 ['outer-middle-ear-transmission','otoacoustic-emissions','related','正向刺激与反向返回传声共同影响探头端耳声发射。',3],
 ['outer-middle-ear-transmission','audiometric-calibration','related','耳道驻波和参考平面影响刺激声压的解释。',2],
 ['outer-middle-ear-transmission','interaural-level-difference','related','外耳方向滤波与头部散射影响两耳声级关系。',2],
 ['interaural-level-difference','interaural-time-difference','related','声级与时间线索共同参与空间任务，符号和条件须分别定义。',3],
 ['interaural-level-difference','binaural-hearing','related','声级差是双耳输入线索，感知利用仍依赖任务与神经处理。',3],
 ['interaural-level-difference','spatial-hearing','describes','以频带声级差表征部分空间线索，不给出固定角度映射。',3],
 ['interaural-level-difference','auditory-pathway','related','LSO兴奋抑制与后续群体处理参与声级线索编码。',3],
 ['interaural-level-difference','hearing-aid','application','双侧压缩、增益与声学耦合可能改变输入声级差。',3],
 ['interaural-level-difference','cochlear-implant','application','电刺激电平差、响度匹配和声学ILD需分别解释。',3],
 ['interaural-level-difference','real-ear-measurement','related','比较耳道响应需统一输入与校准，单耳曲线不能验证全部双耳功能。',2],
 ['acoustic-immittance-tympanometry','audiology','related','补充行为及电生理检查，机械输入不等于听觉能力。',3],
 ['hearing-loss','acoustic-immittance-tympanometry','measured-by','通过机械输入与反射信息辅助鉴别，不能单独确定病因。',3],
 ['acoustic-immittance-tympanometry','pure-tone-audiometry','related','鼓室图与气骨导听阈提供不同层面的互补信息。',3],
 ['acoustic-immittance-tympanometry','otoacoustic-emissions','related','压力、年龄及中耳状态共同影响声学刺激和返回路径。',3],
 ['acoustic-immittance-tympanometry','auditory-development','related','婴儿耳道壁与中耳发育要求频率及年龄适配。',3],
 ['acoustic-immittance-tympanometry','cochlear-synaptopathy','related','人类MEMR作为突触损伤线索仍有限制，不能据此个体确诊。',2],
 ['acoustic-immittance-tympanometry','real-ear-measurement','related','中耳与耦合变化影响耳内声压及RECD转换的适用性。',2],
 ['hearing-aid','real-ear-measurement','measured-by','核对个体耳道输出与处方目标，并另行评价功能获益。',3],
 ['real-ear-measurement','hearing-aid-prescription','related','目标版本、坐标与输入声级一致后才能解释符合度。',3],
 ['real-ear-measurement','audiometric-calibration','related','声场、探管与听阈坐标校准属于不同环节。',3],
 ['real-ear-measurement','speech-audiometry','related','声学验证与言语任务分别评价输出及使用者表现。',3],
 ['real-ear-measurement','speech-intelligibility','related','平均频谱和SII可听性不能直接当作言语识别率。',3],
 ['real-ear-measurement','auditory-development','related','儿童个体耳道与RECD变化要求保持转换和重测记录。',2],
];
let relationFile=await readFile('src/data/relations.ts','utf8');
relationFile=relationFile.replace('export const knowledgeRelations: KnowledgeRelation[] = [','export const knowledgeRelations: KnowledgeRelation[] = [\n  // Four in-depth entries published together, 2026-10-12.\n'+edges.map(e=>`  link(${e.map(v=>JSON.stringify(v)).join(',')}),`).join('\n'));
await writeFile('src/data/relations.ts',relationFile);

let paths=await readFile('src/data/paths.ts','utf8');
paths=paths.replace("slugs:['cochlea','outer-hair-cell'","slugs:['outer-middle-ear-transmission','cochlea','outer-hair-cell'")
 .replace("'spatial-hearing','interaural-time-difference','binaural-integration'","'spatial-hearing','interaural-time-difference','interaural-level-difference','binaural-integration'")
 .replace("'pure-tone-audiometry','speech-audiometry','otoacoustic-emissions'","'pure-tone-audiometry','speech-audiometry','acoustic-immittance-tympanometry','otoacoustic-emissions'")
 .replace("slugs:['hearing-aid','hearing-aid-prescription','dynamic-range'","slugs:['hearing-aid','hearing-aid-prescription','real-ear-measurement','dynamic-range'");
await writeFile('src/data/paths.ts',paths);

const backlinks=[
 ['binaural-hearing','这一差值称为双耳声级差，常缩写为 ILD。','这一差值称为[双耳声级差](../interaural-level-difference/)，常缩写为 ILD。本词条采用右耳减左耳，专门词条采用左耳减右耳；比较数值时需反转符号。'],
 ['interaural-time-difference','耳廓谱线索、双耳声级差、头部运动','耳廓谱线索、[双耳声级差](../interaural-level-difference/)、头部运动'],
 ['audiology','声导抗是声阻抗与声导纳相关测量的统称。','[声导抗](../acoustic-immittance-tympanometry/)是声阻抗与声导纳相关测量的统称。'],
 ['audiology','真耳测量通过探管麦克风观察','[真耳测量](../real-ear-measurement/)通过探管麦克风观察'],
 ['audiology','外耳和中耳传递会影响','[外耳和中耳传声](../outer-middle-ear-transmission/)会影响'],
];
for(const [slug,old,replacement] of backlinks){
 const path=`src/content/concepts/${slug}.md`; const text=await readFile(path,'utf8'); assert(text.includes(old),old); await writeFile(path,text.replace(old,replacement));
}
const wiki=JSON.parse(await readFile('docs/research/wiki-evidence-map.json','utf8'));
wiki.date=date; wiki.relations=knowledgeRelations.length+edges.length; wiki.entries.push(...newEvidence);
for(const e of wiki.entries){
 const {content:body}=parseFrontmatter(await readFile(`src/content/concepts/${e.slug}.md`,'utf8'));
 e.chinese_characters=(body.match(/[\u3400-\u9fff]/g)||[]).length; e.body_characters=body.length;
 e.wiki_links=[...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(v=>v[1]))];
}
await writeFile('docs/research/wiki-evidence-map.json',JSON.stringify(wiki,null,2)+'\n');
await mkdir('docs/research/four-depth-release-2026-10-12',{recursive:true});
await writeFile('docs/research/four-depth-release-2026-10-12/reference-id-map.json',JSON.stringify(mappings,null,2)+'\n');
console.log(JSON.stringify({entries:newEvidence.map(e=>({slug:e.slug,characters:e.chinese_characters,references:e.reference_ids.length,sections:e.sections,subsections:e.subsections})),newReferenceRecords:Object.keys(added).length,newRelations:edges.length},null,2));
