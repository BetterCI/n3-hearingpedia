/** Update this article's evidence record and preserve a scoped editorial QA report. */
import { readFile, writeFile, readdir, mkdir } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { references } from '../src/data/references.ts';
import { knowledgeRelations, relationshipsFor } from '../src/data/relations.ts';
import { learningPaths } from '../src/data/paths.ts';

const slug='speech-perception';
const folder='docs/research/speech-perception-2026-10-10';
await mkdir(folder,{recursive:true});
const source=(await readFile(`src/content/concepts/${slug}.md`,'utf8')).replaceAll('\r\n','\n');
const body=source.split('\n---\n').slice(1).join('\n---\n');
const refIds=JSON.parse(source.match(/^references: (.+)$/m)[1]);
const inline=[...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g)].map(m=>({number:Number(m[1]),id:m[2]}));
const figures=[...body.matchAll(/<img src="([^\"]+)"[^>]*width="(\d+)" height="(\d+)"/g)].map(m=>({url:m[1],width:Number(m[2]),height:Number(m[3])}));
for(const c of inline)assert.equal(refIds[c.number-1],c.id,'Incorrect reference number: '+c.id);
for(const m of body.matchAll(/href="#ref-([^"]+)">(\d+)<\/a>/g))assert.equal(refIds[Number(m[2])-1],m[1]);
for(const id of refIds){assert(references[id],'Missing source '+id);assert(body.includes('#ref-'+id),'Unused reference '+id);}
assert.equal(new Set(refIds).size,refIds.length);
assert.equal(figures.length,4);
for(const f of figures){
 const svg=await readFile('public'+f.url.replace('/n3-hearingpedia',''),'utf8');
 assert(svg.includes(`width="${f.width}" height="${f.height}"`),'Figure dimensions mismatch');
}
const wikiLinks=[...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(m=>m[1]))];
const entries=await readdir('src/content/concepts');
for(const target of wikiLinks)assert(entries.includes(target+'.md'),'Missing cross-link '+target);
assert(learningPaths.some(p=>p.slugs.includes(slug)));
assert(relationshipsFor(slug).length>=10);
const stats={slug,knowledge_area:'perception',kind:'function',
 chinese_characters:(body.match(/[\u3400-\u9fff]/g)||[]).length,body_characters:body.length,
 sections:(body.match(/^## /gm)||[]).length,subsections:(body.match(/^### /gm)||[]).length,
 reference_ids:refIds,wiki_links:wikiLinks,status:'draft',depth:'in-depth'};
const wiki=JSON.parse(await readFile('docs/research/wiki-evidence-map.json','utf8'));
const index=wiki.entries.findIndex(e=>e.slug===slug);
if(index<0)wiki.entries.push(stats);else wiki.entries[index]=stats;
wiki.relations=knowledgeRelations.length;
wiki.date='2026-10-10';
await writeFile('docs/research/wiki-evidence-map.json',JSON.stringify(wiki,null,2)+'\n','utf8');
const report={...stats,figures,equations:(body.match(/^\$\$$/gm)||[]).length/2,
 citations:inline.length,relations:relationshipsFor(slug).length,
 validation:'source IDs, numbering, figure dimensions, equations and existing links checked; build and visual QA recorded separately'};
await writeFile(folder+'/draft-verification.json',JSON.stringify(report,null,2)+'\n','utf8');
const sourceRows=refIds.map(id=>({id,...references[id],relevance:['speech-liberman-1957','speech-dev-1984','speech-mcgurk-1976'].includes(id)?'background: history metadata':'core or important: explicit claim support'}));
await writeFile(folder+'/selected-sources.json',JSON.stringify(sourceRows,null,2)+'\n','utf8');
console.log(JSON.stringify({slug,characters:stats.chinese_characters,sections:stats.sections,references:refIds.length,figures:figures.length,relations:report.relations,equations:report.equations},null,2));
