import { readFile, writeFile, mkdir, copyFile, readdir, access } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
import { learningPaths } from '../src/data/paths.ts';

const slug = 'sound-waves-and-propagation';
const source = (await readFile(`src/content/concepts/${slug}.md`, 'utf8')).replaceAll('\r\n', '\n');
const body = source.split('\n---\n').slice(1).join('\n---\n');
const refIds = JSON.parse(source.match(/^references: (.+)$/m)[1]);
const wikiLinks = [...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\//g)].map(m => m[1]))];
const stats = { slug, knowledge_area: 'sound', kind: 'acoustic-environment',
  chinese_characters: (body.match(/[\u3400-\u9fff]/g) || []).length,
  body_characters: body.length, sections: (body.match(/^## /gm) || []).length,
  subsections: (body.match(/^### /gm) || []).length,
  reference_ids: refIds, wiki_links: wikiLinks, status: 'draft', depth: source.match(/^depth: "([^"]+)"/m)[1] };
assert(stats.chinese_characters >= 2000);
assert(stats.sections >= 4 && stats.subsections >= 3);
for (const m of body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g))
  assert.equal(refIds[Number(m[1])-1], m[2], 'Citation numbering');
for (const m of body.matchAll(/href="#ref-([^"]+)">(?:\[)?(\d+)/g))
  assert.equal(refIds[Number(m[2])-1], m[1], 'Caption citation numbering');
for (const target of wikiLinks) await access(`src/content/concepts/${target}.md`);
const edges = knowledgeRelations.filter(r => r.source === slug || r.target === slug);
assert.equal(edges.length, 6);
assert(learningPaths.some(p => p.slugs.includes(slug)));
const figures = [...body.matchAll(/<img src="\/n3-hearingpedia\/figures\/sound-waves-and-propagation\/([^"]+)"/g)].map(m => m[1]);
assert.equal(figures.length, 4);
assert.equal(stats.depth, 'in-depth');
assert.equal(refIds.length, 21);
assert.equal(new Set(refIds).size, refIds.length);
const citedIds = new Set([...body.matchAll(/#ref-([\w-]+)/g)].map(m => m[1]));
for (const id of refIds) assert(citedIds.has(id), 'Listed but unused source '+id);
for (const name of figures) await access(`public/figures/${slug}/${name}`);
const assets = `docs/drafts/assets/${slug}`;
await mkdir(assets, { recursive: true });
for (const name of await readdir(`public/figures/${slug}`))
  await copyFile(`public/figures/${slug}/${name}`, `${assets}/${name}`);
const fontDir = `${assets}/fonts`;
await mkdir(fontDir, { recursive: true });
for (const name of await readdir('node_modules/katex/dist/fonts'))
  if (name.endsWith('.woff2')) await copyFile(`node_modules/katex/dist/fonts/${name}`, `${fontDir}/${name}`);
const escape = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const bibliography = refIds.map((id, i) => {
  const r = references[id]; assert(r, 'Missing source '+id);
  return `<p id="ref-${id}">[${i+1}] ${escape(r.authors)} (${escape(r.year)}). <a href="${escape(r.url)}">${escape(r.title)}</a>. ${escape(r.publication)}。访问范围：${r.access}。${escape(r.supports)}</p>`;
}).join('\n\n');
let review = body.replaceAll(`/n3-hearingpedia/figures/${slug}/`, `assets/${slug}/`);
review = review.replace(/\]\(\.\.\/([^/]+)\/\)/g, '](https://betterci.github.io/n3-hearingpedia/concepts/$1/)');
review = `# 声波与传播\n\n> 深度词条 · 本地预览 · 2026-10-10 · Draft，尚未完成专业审阅\n\n${review}\n\n## 参考文献与证据范围\n\n${bibliography}\n`;
const processor = await createMarkdownProcessor({ remarkPlugins: [remarkMath],
  rehypePlugins: [[rehypeKatex, { throwOnError: true }]] });
const rendered = (await processor.render(review)).code;
assert(!rendered.includes('katex-error'));
for (const id of refIds) assert(rendered.includes(`id="ref-${id}"`));
const katex = (await readFile('node_modules/katex/dist/katex.min.css', 'utf8')).replaceAll('url(fonts/', `url(assets/${slug}/fonts/`);
const css = `*{box-sizing:border-box}body{margin:0;font-family:"Microsoft YaHei",system-ui,sans-serif;line-height:1.95;color:#253743;background:#f7f9fa}.page{max-width:980px;margin:24px auto;padding:40px 54px;background:white}h1{font-size:36px}h2{margin-top:44px;border-bottom:1px solid #d9e2e7;padding-bottom:10px}h3{margin-top:28px}p{font-size:17px}a{color:#22678f}img{display:block;max-width:100%;height:auto;margin:auto;background:white}figure{margin:30px 0}figcaption p{font-size:14px;color:#526873}table{width:100%;border-collapse:collapse;font-size:14px}th,td{border:1px solid #d9e2e7;padding:10px;text-align:left;vertical-align:top}.table-wrap,.katex-display{overflow-x:auto}.katex-display{overflow-y:hidden;padding:10px 0}p[id^=ref-]{font-size:14px;overflow-wrap:anywhere}blockquote{color:#526873;border-left:3px solid #d9e2e7;padding-left:16px;margin-left:0}@media(max-width:700px){.page{margin:0;padding:22px 18px}p{font-size:16px}h1{font-size:30px}table{min-width:600px}}`;
const content = rendered.replace(/<table>/g, '<div class="table-wrap"><table>').replace(/<\/table>/g, '</table></div>');
const citationCss = 'a[href^="#ref-"]{font-size:.72em;vertical-align:super;white-space:nowrap;text-decoration:none;padding:0 2px}a[href^="#ref-"]::before{content:"["}a[href^="#ref-"]::after{content:"]"}';
const preview = `docs/drafts/${slug}-preview.html`;
await writeFile(preview, `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>声波与传播 · 本地预览</title><style>${katex}\n${css}\n${citationCss}</style></head><body><main class="page">${content}</main></body></html>`, 'utf8');
// Only this entry is refreshed; other unpublished work in the shared workspace is preserved.
const manifestPath = 'docs/research/wiki-evidence-map.json';
const wiki = JSON.parse(await readFile(manifestPath, 'utf8'));
const index = wiki.entries.findIndex(e => e.slug === slug);
if (index < 0) wiki.entries.push(stats); else wiki.entries[index] = stats;
wiki.relations = knowledgeRelations.length;
wiki.date = '2026-10-10';
await writeFile(manifestPath, JSON.stringify(wiki, null, 2)+'\n', 'utf8');
const researchDir = 'docs/research/sound-waves-2026-10-10';
await mkdir(researchDir, { recursive: true });
const report = { ...stats, figures, relationships_added: edges.length,
  preview, display_equations: (rendered.match(/class="katex-display"/g) || []).length,
  validation_scope: 'This entry: source IDs, citation numbering, existing links, assets, math rendering, relations and learning path. Not a successful full-site build or scientific review.' };
await writeFile(`${researchDir}/verification.json`, JSON.stringify(report, null, 2)+'\n', 'utf8');
console.log(JSON.stringify(report, null, 2));
