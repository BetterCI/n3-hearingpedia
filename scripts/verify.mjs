import { readFile, readdir, stat } from 'node:fs/promises';
import { resolve, relative, join, sep } from 'node:path';
import assert from 'node:assert/strict';

const root = resolve('dist');
const base = (process.env.BASE_PATH || '/n3-hearingpedia').replace(/\/$/, '');
async function walk(folder) {
  const entries = await readdir(folder, { withFileTypes: true });
  return (await Promise.all(entries.map(e => e.isDirectory() ? walk(join(folder,e.name)) : join(folder,e.name)))).flat();
}
const htmlFiles=(await walk(root)).filter(p=>p.endsWith('.html'));
const conceptFiles=(await readdir('src/content/concepts')).filter(p=>p.endsWith('.md'));
const expectedConcepts=conceptFiles.length;
assert(htmlFiles.length>=expectedConcepts+22,'Expected core pages, 12 domains, and all concepts');
const cache=new Map(await Promise.all(htmlFiles.map(async p=>[p,await readFile(p,'utf8')])));
for(const file of conceptFiles)assert(cache.has(join(root,'concepts',file.slice(0,-3),'index.html')),'Missing concept route: '+file);
const batch=JSON.parse(await readFile('docs/research/second-batch-catalog.json','utf8'));
for(const e of batch.entries){
  assert(conceptFiles.includes(e.slug+'.md'),'Selected concept not written: '+e.slug);
  const html=cache.get(join(root,'concepts',e.slug,'index.html'));
  assert(html.includes('Draft · 待审阅') && html.includes('尚未经过成员科学审阅'),'Incorrect review status: '+e.slug);
  for(const id of e.reference_ids)assert(html.includes('id="ref-'+id+'"'),'Missing selected reference: '+e.slug+' / '+id);
}
const errors=[];
let checkedLinks=0, equations=0;
for(const [file,html] of cache) {
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
  if(file.includes(sep+'concepts'+sep)) {
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
console.log(JSON.stringify({pages:htmlFiles.length,checkedInternalLinks:checkedLinks,equations,searchableConcepts:entry.languages['zh-cn'].page_count,batch2Concepts:batch.entries.length,brokenLinks:0},null,2));
