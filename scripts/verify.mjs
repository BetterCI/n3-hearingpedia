/**
 * Validate built pages, citations, knowledge links, search and historical redirects.
 * Inputs: dist/, src/, docs/ and optional BASE_PATH. Output: a JSON check summary.
 * Side effects: local file reads only; assertions or broken links fail the process.
 * Usage: node scripts/verify.mjs after pnpm build.
 * Updated 2026-10-09: distinguish canonical articles from merged section redirects.
 * Copyright: Huali Zhou, zhouhuali224@gmail.com
 * School of Electronics and Information Engineering, Heyuan Polytechnic, Heyuan, Guangdong, China.
 */
import { readFile, readdir, stat } from 'node:fs/promises';
import { resolve, relative, join, sep } from 'node:path';
import assert from 'node:assert/strict';
import { knowledgeRelations, relationTypes, relationshipsFor } from '../src/data/relations.ts';
import { knowledgeAreas, kindLabels } from '../src/data/knowledge.ts';
import { learningPaths } from '../src/data/paths.ts';
import { references } from '../src/data/references.ts';
import { mergedConceptRedirects } from '../src/data/merged-concepts.ts';

const root = resolve('dist');
const base = (process.env.BASE_PATH || '/n3-hearingpedia').replace(/\/$/, '');
async function walk(folder) {
  const entries = await readdir(folder, { withFileTypes: true });
  return (await Promise.all(entries.map(e => e.isDirectory() ? walk(join(folder,e.name)) : join(folder,e.name)))).flat();
}
const htmlFiles=(await walk(root)).filter(p=>p.endsWith('.html'));
const conceptFiles=(await readdir('src/content/concepts')).filter(p=>p.endsWith('.md'));
const expectedConcepts=conceptFiles.length;
const conceptPages=new Set(conceptFiles.map(file=>join(root,'concepts',file.slice(0,-3),'index.html')));
assert(htmlFiles.length>=expectedConcepts+23,'Expected core pages, 13 domains, and all concepts');
const cache=new Map(await Promise.all(htmlFiles.map(async p=>[p,await readFile(p,'utf8')])));
for(const file of conceptFiles)assert(cache.has(join(root,'concepts',file.slice(0,-3),'index.html')),'Missing concept route: '+file);
for (const file of conceptFiles) {
  const slug = file.slice(0, -3);
  const concept = cache.get(join(root, 'concepts', slug, 'index.html'));
  const share = cache.get(join(root, 'share', slug, 'index.html'));
  assert(concept.includes(base + '/share/' + slug + '/'), 'Missing share link: ' + slug);
  assert(share?.includes('id="copy-share-image"') && share.includes('id="share-image"'), 'Missing share page: ' + slug);
  const encoded = share.match(/data-card="([^"]+)"/)[1];
  const card = JSON.parse(encoded.replaceAll('&quot;', '"').replaceAll('&#39;', "'").replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&amp;', '&'));
  const articleUrl = new URL(base + '/concepts/' + slug + '/', process.env.SITE_URL || 'https://betterci.github.io').href;
  assert.equal(card.articleUrl, articleUrl, 'Share QR must target the deployed article: ' + slug);
  assert(card.qrDataUrl.startsWith('data:image/png;base64,') && card.facts.length >= 2 && card.facts.length <= 4, 'Missing share content or QR: ' + slug);
  assert(!share.includes('data-pagefind-body'), 'Share page must not duplicate search results: ' + slug);
}
const batch=JSON.parse(await readFile('docs/research/second-batch-catalog.json','utf8'));
const wiki=JSON.parse(await readFile('docs/research/wiki-evidence-map.json','utf8'));
const monitor=JSON.parse(await readFile('docs/research/monitor-expansion-2026-10-04.json','utf8'));
assert(monitor.entries.length>=11&&monitor.entries.length===monitor.counts.new_terms,'Expected more than ten monitor-derived concepts');
assert(new Set(monitor.entries.map(e=>e.slug)).size===monitor.entries.length,'Duplicate monitor concept');
assert(monitor.sources.length===monitor.counts.selected_sources,'Monitor source count differs');
const windowStart=new Date(monitor.window.start+'T00:00:00+08:00');
const windowEnd=new Date(new Date(monitor.window.end+'T00:00:00+08:00').getTime()+24*60*60*1000);
for(const s of monitor.sources){
  assert(new Date(s.first_seen_at)>=windowStart&&new Date(s.first_seen_at)<windowEnd,'Source outside update window: '+s.id);
  assert(references[s.id]?.title===s.title&&references[s.id]?.access===s.access,'Source verification record differs: '+s.id);
  assert((references[s.id]?.publicationType||'journal-article')===s.publication_type,'Publication status differs: '+s.id);
}
for(const e of monitor.entries){
  assert(conceptFiles.includes(e.slug+'.md'),'Monitor concept not published: '+e.slug);
  const w=wiki.entries.find(w=>w.slug===e.slug);
  assert.deepEqual(w?.reference_ids,e.reference_ids,'Monitor bibliography differs: '+e.slug);
  for(const id of e.monitor_source_ids)assert(monitor.sources.some(s=>s.id===id)&&e.reference_ids.includes(id),'Missing monitor seed or direct citation: '+id);
  const html=cache.get(join(root,'concepts',e.slug,'index.html'));
  assert(html.includes('Draft · 待审阅')&&html.includes('尚未完成专业审阅'),'Monitor review status: '+e.slug);
  for(const id of e.reference_ids)if(references[id].publicationType==='preprint')assert(html.includes('预印本 · 未同行评审'),'Unlabelled preprint: '+e.slug);
}
assert(wiki.entries.length===expectedConcepts,'Wiki evidence record must cover every concept');
assert(new Set(wiki.entries.map(e=>e.slug)).size===expectedConcepts,'Duplicate concept evidence record');
for(const e of wiki.entries){
  const source=(await readFile('src/content/concepts/'+e.slug+'.md','utf8')).replaceAll('\r\n','\n');
  const body=source.split(/\n---\n/).slice(1).join('\n---\n');
  const chineseCharacters=(body.match(/[\u3400-\u9fff]/g)||[]).length;
  assert(chineseCharacters===e.chinese_characters,'Evidence record out of date: '+e.slug);
  assert(chineseCharacters>=1000,'Expected substantive mechanism, method, and example coverage: '+e.slug);
  assert(body.trimStart().startsWith('**'),'Expected unheaded encyclopedia lead: '+e.slug);
  assert((body.match(/^## /gm)||[]).length===e.sections&&e.sections>=4,'Expected encyclopedia sections: '+e.slug);
  assert((body.match(/^### /gm)||[]).length===e.subsections&&e.subsections>=3,'Expected explanatory subsections: '+e.slug);
  assert(knowledgeAreas.some(a=>a.id===e.knowledge_area)&&e.kind in kindLabels,'Invalid knowledge classification: '+e.slug);
  assert(source.includes('knowledge_area: "'+e.knowledge_area+'"')&&source.includes('kind: "'+e.kind+'"'),'Classification manifest out of date: '+e.slug);
  assert(!/课题组|组内|成员/.test(source),'Public concept should use general professional wording: '+e.slug);
  assert(!/\n## [^\n]+\n\s*(?=## |$)/.test(body),'Empty article section: '+e.slug);
  const html=cache.get(join(root,'concepts',e.slug,'index.html'));
  assert(html.includes('wiki-infobox')&&html.includes('参见与关联概念'),'Missing wiki navigation: '+e.slug);
  const citations=[...body.matchAll(/\[([^\]]+)\]\(#ref-([^\s)]+)/g)];
  assert(citations.length,'Missing inline sources: '+e.slug);
  for(const citation of citations)assert(/^\d+$/.test(citation[1])&&e.reference_ids[Number(citation[1])-1]===citation[2],'Incorrect numbered reference: '+e.slug+' / '+citation[2]);
  assert.deepEqual([...html.matchAll(/id="ref-([^"]+)"/g)].map(m=>m[1]),e.reference_ids,'Bibliography order and citation numbering differ: '+e.slug);
  for(const id of e.reference_ids)assert(html.includes('id="ref-'+id+'"'),'Missing depth reference: '+e.slug+' / '+id);
  for(const slug of e.wiki_links)assert(conceptFiles.includes(slug+'.md')&&body.includes('../'+slug+'/'),'Broken wiki cross-link: '+e.slug+' / '+slug);
  const illustration=source.match(/illustration:.*?"src":"([^"]+)"/);
  if(illustration)assert(html.includes(base+'/'+illustration[1]),'Teaching illustration missing: '+e.slug);
}
const ids=new Set(wiki.entries.map(e=>e.slug)),edgeKeys=new Set();
assert(wiki.relations===knowledgeRelations.length,'Relationship manifest out of date');
for(const r of knowledgeRelations){
  assert(ids.has(r.source)&&ids.has(r.target)&&r.source!==r.target,'Invalid relationship endpoint');
  assert(r.type in relationTypes&&r.note.trim(),'Missing relationship semantics');
  const pair=relationTypes[r.type].directional?[r.source,r.target]:[r.source,r.target].sort();
  const key=[...pair,r.type].join('|');assert(!edgeKeys.has(key),'Duplicate relationship: '+key);edgeKeys.add(key);
  if(r.type==='measured-by')assert(['test','metric'].includes(wiki.entries.find(e=>e.slug===r.target).kind),'Measurement target must be a test or metric');
  if(r.type==='analyzed-by')assert(wiki.entries.find(e=>e.slug===r.target).kind==='analysis','Analysis target must be an analysis method');
  for(const slug of [r.source,r.target]){
    const relation=relationshipsFor(slug).find(e=>e.source===r.source&&e.target===r.target&&e.type===r.type);
    assert(relation&&relation.neighbor!==slug,'Relationship must be traversable from both ends');
    const html=cache.get(join(root,'concepts',slug,'index.html'));
    assert(html.includes(base+'/concepts/'+relation.neighbor+'/')&&html.includes(relation.label),'Related concept missing from article: '+slug);
  }
}
for (const redirect of mergedConceptRedirects) {
  assert(!ids.has(redirect.slug) && ids.has(redirect.target), 'Invalid merged article redirect: '+redirect.slug);
  const targetHtml=cache.get(join(root,'concepts',redirect.target,'index.html'));
  assert(targetHtml.includes('id="'+redirect.anchor+'"'), 'Missing merged section anchor: '+redirect.slug);
  const redirectHtml=cache.get(join(root,'concepts',redirect.slug,'index.html'));
  const destination=base+'/concepts/'+redirect.target+'/#'+redirect.anchor;
  assert(redirectHtml && /http-equiv="refresh"/i.test(redirectHtml) && redirectHtml.includes(destination), 'Missing historical redirect: '+redirect.slug);
  assert(!redirectHtml.includes('data-pagefind-body'), 'Retired article must not be indexed: '+redirect.slug);
}
for(const slug of ids)assert(relationshipsFor(slug).length,'Orphan concept: '+slug);
function checkTypes(slug,ancestors=new Set()){
  assert(!ancestors.has(slug),'Cycle in subtype hierarchy: '+slug);
  const next=new Set([...ancestors,slug]);
  for(const r of knowledgeRelations.filter(r=>r.source===slug&&r.type==='subtype'))checkTypes(r.target,next);
}
for(const slug of ids)checkTypes(slug);
const pathIds=new Set(learningPaths.flatMap(p=>p.slugs));
for(const slug of pathIds)assert(ids.has(slug),'Broken learning path: '+slug);
for(const slug of ids)assert(pathIds.has(slug),'Concept absent from learning paths: '+slug);
const map=cache.get(join(root,'map','index.html'));
const payload=JSON.parse(map.match(/<script[^>]+id="atlas-data"[^>]*>([\s\S]*?)<\/script>/)[1]);
assert.deepEqual(new Set(payload.nodes.map(n=>n.id)),ids,'Map must contain all concepts');
assert.deepEqual(payload.edges,knowledgeRelations,'Map must use canonical relationship records');
assert(payload.areas.length===knowledgeAreas.length&&map.includes('atlas-canvas-host'),'Missing 3D map interface');
for(const e of batch.entries){
  assert(conceptFiles.includes(e.slug+'.md'),'Selected concept not written: '+e.slug);
  const html=cache.get(join(root,'concepts',e.slug,'index.html'));
  assert(html.includes('Draft · 待审阅') && html.includes('尚未完成专业审阅'),'Incorrect review status: '+e.slug);
  for(const id of e.reference_ids)assert(html.includes('id="ref-'+id+'"'),'Missing selected reference: '+e.slug+' / '+id);
}
const errors=[];
let checkedLinks=0, equations=0;
for(const [file,html] of cache) {
  assert(!/课题组|组内|尚未经过成员/.test(html),'Public site positioning: '+relative(root,file));
  assert(!html.includes('class="katex-error"'),'KaTeX render error in '+relative(root,file));
  for(const match of html.matchAll(/\b(?:href|src|action)=["']([^"']+)["']/g)) {
    const link=match[1].replaceAll('&amp;','&');
    if(/^(?:https?:|mailto:|tel:|data:|\/\/)/i.test(link))continue;
    const parsed=new URL(link,'https://local.invalid'+base+'/'+relative(root,file).split(sep).join('/'));
    let path=decodeURIComponent(parsed.pathname);
    if(base && !path.startsWith(base+'/') && path!==base) { errors.push(relative(root,file)+': missing base prefix '+link);continue; }
    path=base ? path.slice(base.length) : path;
    let target=resolve(root,'.'+path);
    if(target!==root&&!target.startsWith(root+sep)) {errors.push('Path outside output: '+link);continue;}
    try {if((await stat(target)).isDirectory())target=join(target,'index.html');await stat(target);}
    catch {errors.push(relative(root,file)+': missing target '+link);continue;}
    if(parsed.hash && target.endsWith('.html')) {
      const text=cache.get(target)||await readFile(target,'utf8');
      const anchor=decodeURIComponent(parsed.hash.slice(1));
      if(!text.includes('id="'+anchor+'"')&&!text.includes("id='"+anchor+"'"))errors.push(relative(root,file)+': missing anchor '+link);
    }
    checkedLinks++;
  }
  if(conceptPages.has(file)) {
    assert(html.includes('data-pagefind-body'),'Concept not indexed: '+file);
    assert(html.includes('参考文献与证据范围'),'Missing reference section: '+file);
    assert(html.includes('关联概念'),'Missing related section: '+file);
    equations+=(html.match(/class="katex-display"/g)||[]).length;
  }
}
const tonotopy=await readFile(join(root,'concepts/tonotopy/index.html'),'utf8');
assert(tonotopy.includes('频位映射关系'),'Tonotopy translation missing');
assert(!tonotopy.includes('音调拓扑'),'Unapproved Tonotopy translation');
const entry=JSON.parse(await readFile(join(root,'pagefind/pagefind-entry.json'),'utf8'));
assert(entry.languages['zh-cn']?.page_count===expectedConcepts,'Search index must contain every concept');
assert(cache.get(join(root,'concepts/amplitude-modulation/index.html')).includes('预印本 · 未同行评审'),'Preprint evidence must be labelled');
assert(equations>=8,'Expected rendered concept equations');
if(errors.length) { console.error(errors.join('\n'));process.exit(1); }
console.log(JSON.stringify({pages:htmlFiles.length,legacyRedirects:mergedConceptRedirects.length,checkedInternalLinks:checkedLinks,equations,searchableConcepts:entry.languages['zh-cn'].page_count,wikiConcepts:wiki.entries.length,knowledgeAreas:knowledgeAreas.length,typedRelationships:knowledgeRelations.length,wikiCrossLinks:wiki.entries.reduce((s,e)=>s+e.wiki_links.length,0),chineseCharacters:wiki.entries.reduce((s,e)=>s+e.chinese_characters,0),brokenLinks:0},null,2));
