import { readFile, writeFile, mkdir, copyFile, readdir, access } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { z } from 'astro/zod';
import ts from 'typescript';
import { knowledgeAreas, kindLabels } from '../src/data/knowledge.ts';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
import { learningPaths } from '../src/data/paths.ts';

const slug = 'phase-and-group-delay';
const researchDir = 'docs/research/phase-and-group-delay-2026-10-27';
const date = '2026-10-27';
const source = (await readFile(`src/content/concepts/${slug}.md`, 'utf8')).replaceAll('\r\n','\n');
const metadata = JSON.parse(await readFile(`${researchDir}/frontmatter.json`,'utf8'));
const schemaText = (await readFile('src/content.config.ts','utf8')).match(/schema: (z\.object\([\s\S]*?)\n\}\);/)[1].replace(/,\s*$/,'');
const schemaJs = ts.transpileModule(`const schema = ${schemaText};`, { compilerOptions: { target: ts.ScriptTarget.ESNext } }).outputText;
Function('z', 'knowledgeAreas', 'kindLabels', `${schemaJs}; return schema;`)(z, knowledgeAreas, kindLabels).parse(metadata);
const body = source.split('\n---\n').slice(1).join('\n---\n');
const ids = metadata.references;
const citations = [...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g)];
for (const match of citations) assert.equal(ids[Number(match[1])-1],match[2]);
for (const match of body.matchAll(/href="#ref-([^"]+)">(?:\[)?(\d+)/g)) assert.equal(ids[Number(match[2])-1],match[1]);
for (const id of ids) assert(references[id] && body.includes('#ref-'+id), 'Missing/unused reference '+id);
const wikiLinks = [...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\//g)].map(m=>m[1]))];
for (const target of wikiLinks) await access(`src/content/concepts/${target}.md`);
const figs = [...body.matchAll(/<img src="\/n3-hearingpedia\/figures\/phase-and-group-delay\/([^"]+)"/g)].map(m=>m[1]);
assert.equal(figs.length,5);
assert.equal(ids.length,17);
const edges = knowledgeRelations.filter(r=>r.source===slug||r.target===slug);
assert.equal(edges.length,12);
assert(learningPaths.some(p=>p.slugs.includes(slug)));

const assets = `docs/drafts/assets/${slug}`;
await mkdir(`${assets}/fonts`,{recursive:true});
for (const name of await readdir(`public/figures/${slug}`)) await copyFile(`public/figures/${slug}/${name}`,`${assets}/${name}`);
for (const name of await readdir('node_modules/katex/dist/fonts')) if (/\.woff2$/.test(name)) await copyFile(`node_modules/katex/dist/fonts/${name}`,`${assets}/fonts/${name}`);
await copyFile('node_modules/katex/LICENSE', `${assets}/fonts/KaTeX-LICENSE.txt`);
const esc = s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const bibliography=ids.map((id,i)=>{
  const r=references[id];
  return `<p id="ref-${id}">[${i+1}] ${esc(r.authors)} (${esc(r.year)}). <a href="${esc(r.url)}">${esc(r.title)}</a>. ${esc(r.publication)}。访问范围：${r.access}。${esc(r.supports)}</p>`;
}).join('\n\n');
const facts=metadata.key_facts.map(r=>`| ${r.label} | ${r.value} |`).join('\n');
let review=`# ${metadata.title}\n\n> ${metadata.english} · 深度词条 · ${date} · Draft，待专业审阅\n\n${metadata.summary}\n\n| 术语信息 | 内容 |\n| --- | --- |\n${facts}\n\n${body}\n\n## 参考文献与证据范围\n\n${bibliography}\n`;
review=review.replaceAll(`/n3-hearingpedia/figures/${slug}/`,`assets/${slug}/`).replace(/\]\(\.\.\/([^/]+)\/\)/g,'](https://betterci.github.io/n3-hearingpedia/concepts/$1/)');
const processor=await createMarkdownProcessor({remarkPlugins:[remarkMath],rehypePlugins:[[rehypeKatex,{throwOnError:true}]]});
let rendered=(await processor.render(review)).code;
assert(!rendered.includes('katex-error'));
for (const id of ids) assert(rendered.includes(`id="ref-${id}"`));
rendered=rendered.replaceAll('<table>','<div class="table-wrap"><table>').replaceAll('</table>','</table></div>');
const katex=(await readFile('node_modules/katex/dist/katex.min.css','utf8')).replaceAll('url(fonts/',`url(assets/${slug}/fonts/`);
const css=`*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f7f8;color:#253743;font-family:"Microsoft YaHei",system-ui,sans-serif;line-height:1.95}.page{max-width:1020px;margin:24px auto;padding:40px 52px;background:#fff}h1{font-size:36px;line-height:1.4}h2{margin-top:44px;border-bottom:1px solid #d9e2e7;padding-bottom:10px}h3{margin-top:28px}p{font-size:17px}a{color:#22658c}img{display:block;width:100%;max-width:100%;height:auto}figure{margin:30px 0}figcaption{font-size:14px;color:#526873;line-height:1.8}table{width:100%;border-collapse:collapse;font-size:14px}th,td{border:1px solid #d9e2e7;padding:10px;text-align:left;vertical-align:top}.table-wrap{overflow-x:auto}.katex-display{overflow-x:auto;overflow-y:hidden;padding:10px 0}p[id^=ref-]{font-size:14px;overflow-wrap:anywhere;scroll-margin-top:20px}blockquote{color:#526873;border-left:3px solid #d9e2e7;padding-left:16px;margin-left:0}a[href^="#ref-"]{font-size:.72em;vertical-align:super;white-space:nowrap;text-decoration:none;padding:0 2px}@media(max-width:700px){.page{margin:0;padding:22px 18px}p{font-size:16px}h1{font-size:30px}h2{font-size:23px}table{min-width:570px}figure{margin:24px 0}}`;
const preview=`docs/drafts/${slug}-preview.html`;
const citationCss='a[href^="#ref-"]::before{content:"["}a[href^="#ref-"]::after{content:"]"}@media(max-width:700px){.page>.table-wrap:first-of-type table{min-width:0}.page>.table-wrap:first-of-type td:first-child{width:5.5em}}';
await writeFile(preview,`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${metadata.title} · 阅读预览</title><style>${katex}\n${css}\n${citationCss}</style></head><body><main class="page">${rendered}</main></body></html>`,'utf8');
await writeFile(`docs/drafts/${slug}-review-2026-10-27.md`,review,'utf8');

// Refresh only the new entry and the two entries receiving textual backlinks.
const wikiPath='docs/research/wiki-evidence-map.json';
const wiki=JSON.parse(await readFile(wikiPath,'utf8'));
let stats;
for (const target of [slug,'otoacoustic-emissions','vocoder']) {
  const text=(await readFile(`src/content/concepts/${target}.md`,'utf8')).replaceAll('\r\n','\n');
  const b=text.split('\n---\n').slice(1).join('\n---\n');
  const index=wiki.entries.findIndex(e=>e.slug===target);
  const entry={...(index>=0?wiki.entries[index]:{}),slug:target,
    knowledge_area:text.match(/^knowledge_area: "([^"]+)"/m)[1],kind:text.match(/^kind: "([^"]+)"/m)[1],
    chinese_characters:(b.match(/[\u3400-\u9fff]/g)||[]).length,body_characters:b.length,
    sections:(b.match(/^## /gm)||[]).length,subsections:(b.match(/^### /gm)||[]).length,
    reference_ids:JSON.parse(text.match(/^references: (.+)$/m)[1]),
    wiki_links:[...new Set([...b.matchAll(/\]\(\.\.\/([^/]+)\//g)].map(m=>m[1]))],
    status:'draft',depth:'in-depth'};
  if(index<0)wiki.entries.push(entry);else wiki.entries[index]=entry;
  if(target===slug)stats=entry;
}
wiki.relations=knowledgeRelations.length;
wiki.date=date;
await writeFile(wikiPath,JSON.stringify(wiki,null,2)+'\n','utf8');
await writeFile(`${researchDir}/relation-additions.json`,JSON.stringify(edges,null,2)+'\n','utf8');
const report={...stats,figures:figs,numbered_citations:citations.length,relationships_added:edges.length,
  preview,display_equations:(rendered.match(/class="katex-display"/g)||[]).length,
  schema:'passed against src/content.config.ts',validation_scope:'Entry content, references, math, assets, cross-links, relations and learning path. Full-site and browser validation recorded separately.'};
await writeFile(`${researchDir}/entry-verification.json`,JSON.stringify(report,null,2)+'\n','utf8');
console.log(JSON.stringify(report,null,2));
