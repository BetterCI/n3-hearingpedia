import { readFile, writeFile, access } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
import { learningPaths } from '../src/data/paths.ts';
const slug='mathematical-statistics';
const record='docs/research/mathematical-statistics-2026-11-02';
const source=(await readFile(`src/content/concepts/${slug}.md`,'utf8')).replaceAll('\r\n','\n');
const body=source.split('\n---\n').slice(1).join('\n---\n');
const ids=JSON.parse(source.match(/^references: (.+)$/m)[1]);
const citations=[...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g)];
for(const c of citations)assert.equal(ids[Number(c[1])-1],c[2]);
for(const id of ids)assert(references[id] && citations.some(c=>c[2]===id),id);
const links=[...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(m=>m[1]))];
for(const target of links)await access(`src/content/concepts/${target}.md`);
for(const edge of knowledgeRelations.filter(r=>r.source===slug || r.target===slug)){
  await access(`src/content/concepts/${edge.source}.md`);
  await access(`src/content/concepts/${edge.target}.md`);
}
assert(learningPaths.some(p=>p.id==='mathematical-statistics-foundations' && p.slugs[0]===slug));
assert(/^kind: "course"$/m.test(source) && /^depth: in-depth$/m.test(source) && /^status: draft$/m.test(source));
const media=[...new Set([...body.matchAll(/src="(\/n3-hearingpedia\/(?:figures|audio)\/mathematical-statistics\/[^\"]+)"/g)].map(m=>m[1]))];
assert.equal(media.filter(p=>p.endsWith('.svg')).length,8);
assert.equal(media.filter(p=>p.endsWith('.wav')).length,0);
for(const path of media)await access('public'+path.replace('/n3-hearingpedia',''));
for(const caption of body.matchAll(/<figcaption>[\s\S]*?<\/figcaption>/g))assert(!caption[0].includes('$'),'Raw TeX in HTML figure caption');
const snippets=[...body.matchAll(/```python\n([\s\S]*?)\n```/g)];
assert.equal(snippets.length,3);
for(const [i,snippet] of snippets.entries())await writeFile(`${record}/example-${i+1}.py`,snippet[1]+'\n','utf8');
await writeFile(`${record}/run-examples.py`,'from pathlib import Path\nimport runpy\nfor i in range(1,4):\n    runpy.run_path(str(Path(__file__).with_name(f"example-{i}.py")), run_name="__main__")\n','utf8');
const result={slug,chinese_characters:(body.match(/[\u3400-\u9fff]/g)||[]).length,body_characters:body.length,
  sections:(body.match(/^## /gm)||[]).length,subsections:(body.match(/^### /gm)||[]).length,
  reference_ids:ids,wiki_links:links,figures:8,audio:0,code_examples:snippets.length};
await writeFile(`${record}/content-validation.json`,JSON.stringify(result,null,2)+'\n','utf8');
console.log(JSON.stringify(result,null,2));
