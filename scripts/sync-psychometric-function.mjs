// Update only this entry and the four intentional backlinks in the evidence map.
import { readFile, writeFile } from 'node:fs/promises';
import { parseFrontmatter } from '@astrojs/markdown-remark';
import { knowledgeRelations } from '../src/data/relations.ts';
const path='docs/research/wiki-evidence-map.json';
const map=JSON.parse(await readFile(path,'utf8'));
for(const slug of ['psychometric-function','psychoacoustics','speech-reception-threshold','speech-intelligibility','signal-detection-theory']) {
  const source=(await readFile(`src/content/concepts/${slug}.md`,'utf8')).replaceAll('\r\n','\n');
  const {frontmatter:data,content:body}=parseFrontmatter(source);
  let entry=map.entries.find(e=>e.slug===slug);
  if(!entry){entry={slug};map.entries.push(entry);}
  Object.assign(entry,{
    knowledge_area:data.knowledge_area,kind:data.kind,
    chinese_characters:(body.match(/[\u3400-\u9fff]/g)||[]).length,
    body_characters:body.length,sections:(body.match(/^## /gm)||[]).length,
    subsections:(body.match(/^### /gm)||[]).length,reference_ids:data.references,
    wiki_links:[...new Set([...body.matchAll(/\.\.\/([a-z0-9-]+)\//g)].map(m=>m[1]))],
    status:data.status,
  });
  if(slug==='psychometric-function')Object.assign(entry,{depth:data.depth,figures:4,audio:0,code_examples:1});
}
map.relations=knowledgeRelations.length;map.date='2026-11-06';
await writeFile(path,JSON.stringify(map,null,2)+'\n');
console.log('Evidence map: added psychometric-function, refreshed four backlinks and relationship count.');
