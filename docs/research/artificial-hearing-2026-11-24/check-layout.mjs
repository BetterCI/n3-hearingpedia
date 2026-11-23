// Connect only to the isolated headless Chrome instance started for this entry.
import {writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
const targets=await (await fetch('http://127.0.0.1:9337/json/list')).json();
const target=targets.find(t=>t.type==='page');assert(target);
const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
let next=0;const pending=new Map();
ws.addEventListener('message',e=>{const m=JSON.parse(e.data);if(m.id){const p=pending.get(m.id);pending.delete(m.id);m.error?p.reject(m.error):p.resolve(m.result)}});
function send(method,params={}){return new Promise((resolve,reject)=>{const id=++next;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}))})}
async function evaluate(expression){return (await send('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true})).result.value}
const base='docs/research/artificial-hearing-2026-11-24/';
await send('Page.enable');await send('Runtime.enable');
const url=process.argv[2]||pathToFileURL(resolve('docs/drafts/artificial-hearing-preview.html')).href;
await send('Page.navigate',{url});
for(let i=0;i<100;i++){if(await evaluate('document.readyState === "complete"'))break;await new Promise(r=>setTimeout(r,100))}
await evaluate('document.fonts.ready.then(()=>true)');
await evaluate('Promise.all([...document.querySelectorAll("figure img")].map(i=>{i.loading="eager";return i.decode().then(()=>true)}))');
const checks=[];
for(const [name,width,height,mobile] of [['desktop',1440,1100,false],['mobile',390,844,true]]){
 await send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile});
 await evaluate('window.scrollTo({top:0,behavior:"instant"})');
 await new Promise(r=>setTimeout(r,200));
 const result=await evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,images:[...document.querySelectorAll("figure img")].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.getBoundingClientRect().width})),math:document.querySelectorAll(".katex").length,tables:document.querySelectorAll("table").length})');
 assert.equal(result.width,width);assert(result.scrollWidth<=width+1);assert(result.images.every(i=>i.loaded));assert(result.math>0);
 for(const [view,selector] of [['top','h1'],['figure','figure'],['formula','.katex-display']]){
  await evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'start',behavior:'instant'})`);
  await new Promise(r=>setTimeout(r,100));
  const {data}=await send('Page.captureScreenshot',{format:'png'});await writeFile(base+`layout-${name}-${view}.png`,Buffer.from(data,'base64'));
 }
 checks.push({name,...result});
}
await writeFile(base+'layout-validation.json',JSON.stringify({url,checks},null,2)+'\n');
console.log(JSON.stringify(checks,null,2));await send('Browser.close');ws.close();
