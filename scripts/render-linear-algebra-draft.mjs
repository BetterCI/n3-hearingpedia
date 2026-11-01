import { readFile, writeFile, mkdir, access } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { createMarkdownProcessor } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { references } from '../src/data/references.ts';
import { knowledgeRelations } from '../src/data/relations.ts';
import { learningPaths } from '../src/data/paths.ts';

const slug = 'linear-algebra';
const record = 'docs/research/linear-algebra-2026-11-01';
const source = (await readFile(`src/content/concepts/${slug}.md`, 'utf8')).replaceAll('\r\n', '\n');
const body = source.split('\n---\n').slice(1).join('\n---\n');
const ids = JSON.parse(source.match(/^references: (.+)$/m)[1]);
const cited = [...body.matchAll(/\[(\d+)\]\(#ref-([^\s)]+)\)/g)];
for (const c of cited) assert.equal(ids[Number(c[1]) - 1], c[2]);
for (const id of ids) assert(references[id] && cited.some(c => c[2] === id), id);
const links = [...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\/\)/g)].map(m => m[1]))];
for (const target of links) await access(`src/content/concepts/${target}.md`);
const edges = knowledgeRelations.filter(r => r.source === slug || r.target === slug);
for (const edge of edges) {
  await access(`src/content/concepts/${edge.source}.md`);
  await access(`src/content/concepts/${edge.target}.md`);
}
assert(learningPaths.some(p => p.slugs.includes(slug)));
const depth = source.match(/^depth: (.+)$/m)[1].replaceAll('"', '');
assert.equal(depth, 'in-depth');
// Export each displayed experiment as an independent executable example.
const snippets = [...body.matchAll(/```python\n([\s\S]*?)\n```/g)];
assert.equal(snippets.length, 3);
for (const [i, snippet] of snippets.entries()) await writeFile(`${record}/example-${i+1}.py`, snippet[1] + '\n', 'utf8');
await writeFile(`${record}/example.py`, 'from pathlib import Path\nimport runpy\nfor name in ("example-1.py", "example-2.py", "example-3.py"):\n    print(name)\n    runpy.run_path(str(Path(__file__).with_name(name)), run_name="__main__")\n', 'utf8');
const esc = s => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const bibliography = ids.map((id, i) => {
  const r = references[id];
  return `<p id="ref-${id}">[${i + 1}] ${esc(r.authors)} (${esc(r.year)}). <a href="${esc(r.url)}">${esc(r.title)}</a>. ${esc(r.publication)}。${esc(r.supports)}</p>`;
}).join('\n');
const processor = await createMarkdownProcessor({remarkPlugins: [remarkMath], rehypePlugins: [[rehypeKatex, {throwOnError: true}]]});
let html = (await processor.render(`# 线性代数\n\n> Linear Algebra · 基础课程 · 深度词条 · 2026-11-01 · Draft，待专业审阅\n\n${body}\n\n## 参考文献与核验范围\n\n${bibliography}`)).code;
assert(!html.includes('katex-error'));
for (const id of ids) assert(html.includes(`id="ref-${id}"`));
html = html.replaceAll('<table>', '<div class="table-wrap"><table>').replaceAll('</table>', '</table></div>');
// Self-contained artifact: formulas, fonts and figure work offline.
const mediaPaths = [...new Set([...html.matchAll(/src="(\/n3-hearingpedia\/(?:figures|audio)\/linear-algebra\/[^\"]+)"/g)].map(m=>m[1]))];
assert.equal(mediaPaths.filter(path=>path.endsWith('.svg')).length, 6);
assert.equal(mediaPaths.filter(path=>path.endsWith('.wav')).length, 4);
for (const path of mediaPaths) {
  const data = await readFile('public' + path.replace('/n3-hearingpedia', ''));
  const mime = path.endsWith('.svg') ? 'image/svg+xml' : 'audio/wav';
  html = html.replaceAll(path, `data:${mime};base64,${data.toString('base64')}`);
}
html = html.replaceAll(/href="\.\.\/([^/]+)\/"/g, 'href="https://betterci.github.io/n3-hearingpedia/concepts/$1/"');
const experimentCode = await readFile('public/code/linear-algebra/experiments.py');
html = html.replaceAll('/n3-hearingpedia/code/linear-algebra/experiments.py', `data:text/x-python;base64,${experimentCode.toString('base64')}`);
let katex = await readFile('node_modules/katex/dist/katex.min.css', 'utf8');
const fonts = [...new Set([...katex.matchAll(/url\((fonts\/[^)]+)\)/g)].map(m => m[1]))];
for (const font of fonts) {
  const ext = font.split('.').at(-1);
  const data = (await readFile(`node_modules/katex/dist/${font}`)).toString('base64');
  katex = katex.replaceAll(`url(${font})`, `url(data:font/${ext};base64,${data})`);
}
const css = `*{box-sizing:border-box}body{margin:0;background:#f4f7f8;color:#253743;font-family:"Microsoft YaHei",system-ui,sans-serif;line-height:1.95}.page{max-width:1040px;margin:24px auto;padding:36px 52px;background:white}h1{font-size:36px}h2{margin-top:40px;border-bottom:1px solid #d9e2e7;padding-bottom:8px}h3{margin-top:26px}p{font-size:17px}a{color:#22658c}img{display:block;max-width:100%;width:100%;height:auto}figure{margin:28px 0}figcaption{font-size:14px;color:#526370}.table-wrap{overflow:auto}table{border-collapse:collapse;min-width:640px;width:100%;font-size:14px}th,td{border:1px solid #d9e2e7;padding:10px 12px;text-align:left;vertical-align:top}th{background:#edf4f7}blockquote{margin:0;border-left:4px solid #22658c;padding:1px 18px;background:#edf4f7}pre{padding:18px;overflow:auto;line-height:1.65;font-size:13px}code{font-family:Consolas,monospace}.katex-display{overflow-x:auto;overflow-y:hidden;padding:6px 0}details{border:1px solid #c7d5db;border-radius:6px;padding:14px 18px}summary{cursor:pointer;color:#22658c}@media(max-width:700px){.page{margin:0;padding:24px 20px}p{font-size:16px}h1{font-size:30px}figure{margin:20px 0}}`;
await mkdir('docs/drafts', {recursive: true});
await writeFile('docs/drafts/linear-algebra-preview.html', `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>线性代数 · 听觉技术研究的基础课程</title><style>${katex}\n${css}</style></head><body><main class="page">${html}</main></body></html>`, 'utf8');
const report = {slug, depth, executable_examples: snippets.length, preview: 'docs/drafts/linear-algebra-preview.html', numbered_citations: cited.length,
  reference_count: ids.length, local_concept_links: links, relationship_count: edges.length,
  display_equations: (html.match(/class="katex-display"/g) || []).length,
  math_rendering: 'passed with throwOnError', assets: 'embedded SVG figures, WAV audio and KaTeX fonts', media_paths: mediaPaths,
  validation_scope: 'Entry citations, media, math and links checked here. Publication build and scientific audit are recorded in scientific-audit.md.'};
await writeFile(`${record}/entry-verification.json`, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify(report, null, 2));
