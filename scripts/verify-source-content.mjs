// Source-level checks usable when the native Astro compiler is unavailable.
// These do not replace the built-site checks in verify.mjs.
import { readFile, readdir, stat } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
import { knowledgeAreas, kindLabels } from '../src/data/knowledge.ts';
import { learningPaths } from '../src/data/paths.ts';

const wiki=JSON.parse(await readFile('docs/research/wiki-evidence-map.json','utf8'));
const monitor=JSON.parse(await readFile('docs/research/monitor-expansion-2026-10-04.json','utf8'));
const catalog=JSON.parse(await readFile('docs/research/second-batch-catalog.json','utf8'));
const files=(await readdir('src/content/concepts')).filter(f=>f.endsWith('.md'));
assert.equal(files.length,wiki.entries.length);
const ids=new Set(wiki.entries.map(e=>e.slug));
assert.equal(ids.size,files.length);
let citations=0,figures=0;
for(const e of wiki.entries){
 const source=(await readFile(`src/content/concepts/${e.slug}.md`,'utf8')).replaceAll('\r\n','\n');
 const [front,...pieces]=source.slice(4).split('\n---\n');const body=pieces.join('\n---\n');
 const refIDs=JSON.parse(front.match(/^references:\s*(\[[\s\S]*?\])/m)[1]);
 assert.deepEqual(refIDs,e.reference_ids,e.slug);
 assert.equal((body.match(/[\u3400-\u9fff]/g)||[]).length,e.chinese_characters,e.slug);
 assert.equal((body.match(/^## /gm)||[]).length,e.sections,e.slug);
 assert.equal((body.match(/^### /gm)||[]).length,e.subsections,e.slug);
 assert(e.chinese_characters>=1000&&e.sections>=4&&e.subsections>=3,e.slug);
 assert(body.trimStart().startsWith('**'),e.slug);
 assert(!/\n## [^\n]+\n\s*(?=## |$)/.test(body),e.slug);
 assert(!/课题组|组内|成员/.test(source),e.slug);
 assert(knowledgeAreas.some(a=>a.id===e.knowledge_area)&&e.kind in kindLabels,e.slug);
 for(const id of refIDs)assert(references[id],id);
 for(const [_,n,id] of body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)/g)){assert.equal(refIDs[Number(n)-1],id,e.slug);citations++;}
 for(const [_,id,n] of body.matchAll(/<a href="#ref-([^"]+)">(\d+)<\/a>/g)){assert.equal(refIDs[Number(n)-1],id,e.slug);citations++;}
 for(const slug of e.wiki_links)assert(ids.has(slug)&&body.includes('../'+slug+'/'),`${e.slug}: ${slug}`);
 for(const [_,file] of body.matchAll(/<img src="\/n3-hearingpedia\/([^"]+)"/g)){assert((await stat('public/'+file)).size>0);figures++;}
}
assert.equal(wiki.relations,knowledgeRelations.length);
for(const r of knowledgeRelations)assert(ids.has(r.source)&&ids.has(r.target)&&r.source!==r.target);
const pathIds=new Set(learningPaths.flatMap(p=>p.slugs));for(const id of ids)assert(pathIds.has(id),id);
for(const e of monitor.entries){assert.deepEqual(wiki.entries.find(w=>w.slug===e.slug).reference_ids,e.reference_ids);for(const id of e.monitor_source_ids)assert(e.reference_ids.includes(id));}
for(const e of catalog.entries){assert(ids.has(e.slug));for(const id of e.reference_ids)assert(wiki.entries.find(w=>w.slug===e.slug).reference_ids.includes(id));}
console.log(JSON.stringify({concepts:files.length,relations:knowledgeRelations.length,citations,inlineFigures:figures,sourceContent:'passed',builtSite:'not checked by this script'},null,2));
