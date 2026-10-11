// Standalone draft render and validation; does not touch the active collection,
// relations, learning paths, site version or evidence map.
import { readFile, writeFile, mkdir, readdir, copyFile, access, cp } from 'node:fs/promises';
import assert from 'node:assert/strict';
import { createMarkdownProcessor, parseFrontmatter } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { references as siteReferences } from '../src/data/references.ts';
const slug = 'interaural-level-difference';
const researchDir = 'docs/research/ild-2026-10-11';
const source = (await readFile(`docs/drafts/${slug}.md`, 'utf8')).replaceAll('\r\n','\n');
const front = source.match(/^---\n([\s\S]+?)\n---\n/); assert(front);
const meta = parseFrontmatter(source).frontmatter;
const body = source.slice(front[0].length);
assert.equal(meta.status,'draft'); assert.equal(meta.depth,'in-depth');
assert.equal(meta.reviewer,null); assert.equal(meta.reviewed_at,null);
assert(meta.key_facts.every(f=>typeof f.label==='string' && typeof f.value==='string'));
const records = JSON.parse(await readFile(`${researchDir}/references.json`,'utf8'));
assert.equal(records.length,23);
const map = new Map(records.map(r=>[r.id,r]));
assert.equal(map.size,records.length);assert.deepEqual(meta.references,records.map(r=>r.id));
for (const r of records) {
  for (const field of ['title','authors','year','publication','url','access','supports']) assert(r[field],`${r.id}: ${field}`);
  assert(['fulltext','abstract','metadata','documentation'].includes(r.access));
  assert(new URL(r.url).protocol==='https:');
}
const duplicateDois=new Map();
for(const r of records){if(r.doi){const d=r.doi.toLowerCase();assert(!duplicateDois.has(d));duplicateDois.set(d,r.id);}}
const citationMatches = [...body.matchAll(/\[(\d+)\]\(#ref-([\w-]+)\)/g)];
const cited=new Set();for(const m of citationMatches){assert.equal(meta.references[Number(m[1])-1],m[2]);cited.add(m[2]);}
for(const id of meta.references) assert(cited.has(id),'Uncited reference '+id);
const links=[...new Set([...body.matchAll(/\]\(\.\.\/([^/]+)\//g)].map(m=>m[1]))];
for(const name of links) await access(`src/content/concepts/${name}.md`);
const images=[...body.matchAll(/<img src="([^"]+)"/g)].map(m=>m[1]);assert.equal(images.length,4);
for(const path of images) await access('docs/drafts/'+path);
const assets=`docs/drafts/assets/${slug}`;
await mkdir(`${assets}/fonts`,{recursive:true});
for(const name of await readdir('node_modules/katex/dist/fonts')) if(name.endsWith('.woff2')) await copyFile(`node_modules/katex/dist/fonts/${name}`,`${assets}/fonts/${name}`);
await copyFile('node_modules/katex/LICENSE', `${assets}/fonts/KaTeX-LICENSE.txt`);
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const labels={fulltext:'已读全文相关部分',abstract:'摘要核对',metadata:'元数据核对',documentation:'官方文档／讲义'};
const bibliography=records.map((r,i)=>`<li id="ref-${r.id}"><span class="reference-title"><a href="${escape(r.url)}">[${i+1}] ${escape(r.title)}</a></span><div class="reference-detail">${escape(r.authors)} (${escape(r.year)}). ${escape(r.publication)}.${r.doi?` DOI: ${escape(r.doi)}.`:''}</div><div class="source-scope">${labels[r.access]}：${escape(r.supports)}</div></li>`).join('\n');
const processor=await createMarkdownProcessor({remarkPlugins:[remarkMath],rehypePlugins:[[rehypeKatex,{throwOnError:true}]]});
const reviewBody=body.replace(/\]\(\.\.\/([^/]+)\/\)/g,'](https://betterci.github.io/n3-hearingpedia/concepts/$1/)');
const rendered=await processor.render(reviewBody);assert(!rendered.code.includes('katex-error'));
const headings=rendered.metadata.headings.filter(h=>h.depth===2);
const toc=headings.map(h=>`<a href="#${escape(h.slug)}">${escape(h.text)}</a>`).join('');
const globalCss=await readFile('src/styles/global.css','utf8');
const katex=(await readFile('node_modules/katex/dist/katex.min.css','utf8')).replaceAll('url(fonts/',`url(assets/${slug}/fonts/`);
const draftCss=`.draft-container{max-width:1180px;margin:0 auto;padding:30px 32px 60px}.draft-top{font-size:13px;color:var(--muted);margin-bottom:25px;display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap}.draft-top a{color:var(--accent)}.draft-content{min-width:0}.encyclopedia-figure{margin:28px 0;padding:12px;border:1px solid var(--line);border-radius:10px;background:#fff}.encyclopedia-figure img{margin:0;max-width:100%;width:100%;height:auto}.encyclopedia-figure figcaption{margin-top:10px;font-size:12px;line-height:1.8;color:var(--muted)}.prose a[href^="#ref-"]{font-size:.72em;vertical-align:super;text-decoration:none;padding:0 2px;white-space:nowrap}.prose a[href^="#ref-"]::before{content:"["}.prose a[href^="#ref-"]::after{content:"]"}.reference-list li{padding-left:0;overflow-wrap:anywhere;scroll-margin-top:24px}.reference-list li:before{display:none}.source-scope{font-size:11px}.draft-top a:focus-visible{outline-offset:3px}@media(max-width:760px){.draft-container{padding:22px 18px 40px}.article-shell{gap:26px}.encyclopedia-figure{padding:7px;margin-left:0;margin-right:0}.encyclopedia-figure figcaption{font-size:11px}.article-sidebar{grid-row:1}.article-sidebar nav{max-height:145px}.draft-top{margin-bottom:18px}}`;
const html=`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>${escape(meta.title)} · 待确认草稿</title><style>${globalCss}\n${katex}\n${draftCss}</style></head><body><main class="draft-container"><div class="draft-top"><a href="https://betterci.github.io/n3-hearingpedia/">n³ Hearingpedia</a><span>独立草稿预览 · 2026-10-11 · 未发布</span></div><div class="article-shell"><article class="draft-content"><header class="article-header"><span class="status-pill">待确认草稿</span><h1>${escape(meta.title)}</h1><p class="article-english">${escape(meta.english)}</p><p class="lead">${escape(meta.summary)}</p><div class="article-metadata"><span>深度词条 · AI 辅助编写</span><span>23 项来源 · 4 幅原创图</span><span>尚未专业审阅</span></div></header><div class="draft-notice">此页独立于正式网站，仅供作者审阅。正文、公式和图示待你确认后再整合发布；文献访问范围列于页末。</div><div class="prose">${rendered.code}</div><section class="references"><h2 id="references">参考文献与证据范围</h2><ol class="reference-list">${bibliography}</ol></section></article><aside class="article-sidebar"><div class="toc-label">本文目录</div><nav aria-label="本文目录">${toc}<a href="#references">参考文献与证据范围</a></nav><p class="sidebar-info">教学计算与图示均可复现。<br>文献核对：2026-10-11<br>状态：待确认，未发布。</p></aside></div></main></body></html>`;
const preview=`docs/drafts/${slug}-preview.html`;await writeFile(preview,html,'utf8');
const artifact='artifacts/ild-preview';await mkdir(artifact,{recursive:true});await cp(assets,`${artifact}/assets/${slug}`,{recursive:true});await writeFile(`${artifact}/index.html`,html,'utf8');
const pendingReuse=records.flatMap(r=>Object.entries(siteReferences).filter(([,s])=>(r.doi&&s.doi?.toLowerCase()===r.doi.toLowerCase()) || s.url===r.url).map(([id])=>({draft_id:r.id,existing_id:id})));
const report={title:meta.title,slug,status:'draft',published:false,professionally_reviewed:false,chinese_characters:(body.match(/[\u3400-\u9fff]/g)||[]).length,sections:headings.length,subsections:(body.match(/^### /gm)||[]).length,references:records.length,citation_occurrences:citationMatches.length,figures:images,internal_links:links,display_equations:(rendered.code.match(/class="katex-display"/g)||[]).length,existing_sources_for_reuse:pendingReuse,preview,verification:'Citation numbering and coverage, source records, existing concept targets, figure assets, frontmatter draft state, KaTeX rendering and independent teaching calculations. Active site not modified; this is not a scientific peer review.'};
assert(report.chinese_characters>=6000 && report.chinese_characters<=10000);assert.equal(headings.length,11);
await writeFile(`${researchDir}/verification.json`,JSON.stringify(report,null,2)+'\n','utf8');console.log(JSON.stringify(report,null,2));
