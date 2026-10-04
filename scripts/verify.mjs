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
assert(htmlFiles.length>=30,'Expected core pages, 12 domains, and 8 concepts');
const cache=new Map(await Promise.all(htmlFiles.map(async p=>[p,await readFile(p,'utf8')])));
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
assert(entry.languages['zh-cn']?.page_count===8,'Expected 8 searchable concepts');
assert(equations>=8,'Expected rendered concept equations');
if(errors.length) { console.error(errors.join('\n'));process.exit(1); }
console.log(JSON.stringify({pages:htmlFiles.length,checkedInternalLinks:checkedLinks,equations,searchableConcepts:entry.languages['zh-cn'].page_count,brokenLinks:0},null,2));
