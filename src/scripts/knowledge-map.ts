import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { brainNodePositions, createBrainScaffold } from './brain-layout';

interface AtlasNode { id:string; title:string; english:string; aliases:string[]; summary:string; kind:string; area:string; url:string; }
interface AtlasEdge { source:string; target:string; type:string; note:string; }
interface AtlasArea { id:string; title:string; english:string; color:string; }
interface AtlasType { label:string; outgoing:string; incoming:string; directional:boolean; }
interface AtlasData { nodes:AtlasNode[]; edges:AtlasEdge[]; areas:AtlasArea[]; types:Record<string,AtlasType>; }
interface NodeView { data:AtlasNode; mesh:THREE.Mesh<THREE.SphereGeometry,THREE.MeshBasicMaterial>; halo:THREE.Sprite; label:HTMLButtonElement; position:THREE.Vector3; }
interface EdgeView { data:AtlasEdge; curve:THREE.QuadraticBezierCurve3; line:THREE.Line<THREE.BufferGeometry,THREE.LineBasicMaterial>; particle:THREE.Sprite; }

export function initKnowledgeMap() {
  const dataElement=document.querySelector('#atlas-data');
  const stage=document.querySelector<HTMLElement>('#atlas-stage');
  if(!dataElement?.textContent||!stage)return;
  const data:AtlasData=JSON.parse(dataElement.textContent);
  const host=document.querySelector<HTMLElement>('#atlas-canvas-host')!;
  const labels=document.querySelector<HTMLElement>('#atlas-labels')!;
  const status=document.querySelector<HTMLElement>('#atlas-status')!;
  const query=document.querySelector<HTMLInputElement>('#atlas-query')!;
  const areaSelect=document.querySelector<HTMLSelectElement>('#atlas-area')!;
  const relationSelect=document.querySelector<HTMLSelectElement>('#atlas-relation')!;
  const motionButton=document.querySelector<HTMLButtonElement>('#atlas-motion')!;
  const labelButton=document.querySelector<HTMLButtonElement>('#atlas-label-toggle')!;
  const atlas=document.querySelector<HTMLElement>('.atlas')!;
  const fullscreenButton=document.querySelector<HTMLButtonElement>('#atlas-fullscreen')!;
  let pageFullscreen=false, wasFullscreen=false;
  function syncFullscreen(){
    const active=document.fullscreenElement===atlas||pageFullscreen;
    atlas.classList.toggle('is-expanded',pageFullscreen);
    document.documentElement.classList.toggle('atlas-fullscreen-open',pageFullscreen);
    fullscreenButton.textContent=active?'退出全屏':'⛶ 全屏';
    fullscreenButton.setAttribute('aria-label',active?'退出地图全屏':'进入地图全屏');
    fullscreenButton.setAttribute('aria-pressed',String(active));
    if(wasFullscreen&&!active)fullscreenButton.focus({preventScroll:true});
    wasFullscreen=active;
  }
  async function toggleFullscreen(){
    fullscreenButton.disabled=true;
    try{
      if(document.fullscreenElement===atlas)await document.exitFullscreen();
      else if(pageFullscreen)pageFullscreen=false;
      else if(document.fullscreenEnabled&&atlas.requestFullscreen){
        try{await atlas.requestFullscreen();}catch{pageFullscreen=true;}
      }else pageFullscreen=true;
    }catch{status.textContent='未能切换全屏，请重试或按 Esc 返回。';}
    finally{fullscreenButton.disabled=false;syncFullscreen();}
  }
  function fullscreenEscape(event:KeyboardEvent){
    if(event.key==='Escape'&&pageFullscreen){event.preventDefault();pageFullscreen=false;syncFullscreen();}
    else if(event.key==='Escape'&&document.fullscreenElement===atlas){event.preventDefault();void toggleFullscreen();}
  }
  fullscreenButton.addEventListener('click',toggleFullscreen);
  document.addEventListener('fullscreenchange',syncFullscreen);
  document.addEventListener('keydown',fullscreenEscape);
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  let motion=!reduced.matches, showLabels=true, selected:string|null=null;
  let width=1,height=1,visible=true,frame=0,lastTime=0,elapsed=0;
  let renderer:THREE.WebGLRenderer|null=null, ctx:CanvasRenderingContext2D|null=null;
  let canvas=document.createElement('canvas');
  canvas.setAttribute('aria-label','可旋转与缩放的三维知识网络');
  canvas.style.cssText='width:100%;height:100%;display:block;touch-action:none';
  try { renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:true,powerPreference:'low-power'});renderer.setPixelRatio(Math.min(devicePixelRatio,1.7)); }
  catch { canvas=document.createElement('canvas');canvas.style.cssText='width:100%;height:100%;display:block;touch-action:none';canvas.setAttribute('aria-label','兼容模式的三维知识网络');ctx=canvas.getContext('2d'); }
  host.append(canvas);
  if(!renderer&&!ctx){stage.dataset.state='unavailable';status.textContent='当前浏览器未能显示地图；下方目录和关系清单仍可阅读。';return;}
  stage.dataset.state=renderer?'webgl':'compatible';
  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(43,1,1,1600);
  camera.position.set(12,40,470);
  const controls=new OrbitControls(camera,canvas);
  controls.enableDamping=true;controls.dampingFactor=.075;controls.autoRotate=motion;controls.autoRotateSpeed=.42;
  controls.minDistance=150;controls.maxDistance=1100;controls.enablePan=false;controls.rotateSpeed=.55;controls.zoomSpeed=.7;
  controls.saveState();
  const brain=createBrainScaffold();
  for(const trace of brain.lines)scene.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(trace.points),new THREE.LineBasicMaterial({color:'#89bdd4',transparent:true,opacity:trace.opacity,depthWrite:false})));
  scene.add(new THREE.Points(new THREE.BufferGeometry().setFromPoints(brain.points),new THREE.PointsMaterial({color:'#89bdd4',size:1.1,transparent:true,opacity:.24,sizeAttenuation:false,depthWrite:false})));
  const areaById=Object.fromEntries(data.areas.map(a=>[a.id,a]));
  const byId=Object.fromEntries(data.nodes.map(n=>[n.id,n]));
  const degree=Object.fromEntries(data.nodes.map(n=>[n.id,data.edges.filter(e=>e.source===n.id||e.target===n.id).length]));
  const glowCanvas=document.createElement('canvas');glowCanvas.width=128;glowCanvas.height=128;
  const gc=glowCanvas.getContext('2d')!;const gradient=gc.createRadialGradient(64,64,1,64,64,64);
  gradient.addColorStop(0,'rgba(255,255,255,1)');gradient.addColorStop(.17,'rgba(255,255,255,.5)');gradient.addColorStop(.45,'rgba(255,255,255,.12)');gradient.addColorStop(1,'rgba(255,255,255,0)');gc.fillStyle=gradient;gc.fillRect(0,0,128,128);
  const glow=new THREE.CanvasTexture(glowCanvas);
  const positions=brainNodePositions(data.nodes.length);
  const layoutNodes=data.areas.flatMap(area=>data.nodes.filter(n=>n.area===area.id));
  const positionById=Object.fromEntries(layoutNodes.map((n,i)=>[n.id,positions[i]]));
  const nodeViews:NodeView[]=data.nodes.map(n=>{
    const position=positionById[n.id];
    const material=new THREE.MeshBasicMaterial({color:areaById[n.area].color,transparent:true,opacity:.96});
    const mesh=new THREE.Mesh(new THREE.SphereGeometry(3+Math.sqrt(degree[n.id])*.35,16,12),material);mesh.position.copy(position);mesh.userData.id=n.id;scene.add(mesh);
    const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glow,color:areaById[n.area].color,transparent:true,opacity:.57,blending:THREE.AdditiveBlending,depthWrite:false}));halo.position.copy(position);halo.scale.setScalar(24);scene.add(halo);
    const label=document.createElement('button');label.type='button';label.className='atlas-node-label';label.textContent=n.title;label.setAttribute('aria-label','选择 '+n.title);label.style.setProperty('--node-color',areaById[n.area].color);labels.append(label);label.addEventListener('click',()=>select(n.id));
    return {data:n,mesh,halo,label,position};
  });
  const viewById=Object.fromEntries(nodeViews.map(n=>[n.data.id,n]));
  const edgeViews:EdgeView[]=data.edges.map((e,i)=>{
    const a=viewById[e.source].position,b=viewById[e.target].position;
    const mid=a.clone().add(b).multiplyScalar(.5);mid.z-=15+Math.sin(i*1.91)*17;
    const curve=new THREE.QuadraticBezierCurve3(a.clone(),mid,b.clone());
    const line=new THREE.Line(new THREE.BufferGeometry().setFromPoints(curve.getPoints(32)),new THREE.LineBasicMaterial({color:areaById[byId[e.source].area].color,transparent:true,opacity:.17,depthWrite:false}));scene.add(line);
    const particle=new THREE.Sprite(new THREE.SpriteMaterial({map:glow,color:'#d9f2ff',transparent:true,opacity:.72,blending:THREE.AdditiveBlending,depthWrite:false}));particle.scale.setScalar(6);scene.add(particle);
    return {data:e,curve,line,particle};
  });
  const stars=Array.from({length:300},(_,i)=>{const a=i*2.399963,b=Math.acos(1-2*(i+.5)/300),r=350+(i%7)*38;return new THREE.Vector3(r*Math.sin(b)*Math.cos(a),r*Math.cos(b),r*Math.sin(b)*Math.sin(a));});
  const starsGeometry=new THREE.BufferGeometry().setFromPoints(stars);
  const starPoints=new THREE.Points(starsGeometry,new THREE.PointsMaterial({color:'#82b0d0',size:1.15,transparent:true,opacity:.32,sizeAttenuation:false}));scene.add(starPoints);
  const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();let pointerDown:[number,number]|null=null;
  const matches=(n:AtlasNode)=>!areaSelect.value||n.area===areaSelect.value;
  const relevantEdges=()=>data.edges.filter(e=>(!relationSelect.value||e.type===relationSelect.value)&&(!areaSelect.value||matches(byId[e.source])||matches(byId[e.target])));
  const neighbors=()=>new Set(relevantEdges().filter(e=>e.source===selected||e.target===selected).flatMap(e=>[e.source,e.target]));
  function applyStyles(){
    const linked=neighbors();
    nodeViews.forEach(n=>{const active=matches(n.data)&&(!selected||linked.has(n.data.id)||n.data.id===selected);n.mesh.material.opacity=active?.96:.1;(n.halo.material as THREE.SpriteMaterial).opacity=active?.55:.06;n.halo.scale.setScalar(n.data.id===selected?39:24);n.label.classList.toggle('is-selected',n.data.id===selected);n.label.classList.toggle('is-dimmed',!active);});
    edgeViews.forEach(e=>{const active=(!relationSelect.value||e.data.type===relationSelect.value)&&(!areaSelect.value||matches(byId[e.data.source])||matches(byId[e.data.target]))&&(!selected||e.data.source===selected||e.data.target===selected);e.line.material.opacity=active?(selected?.58:.12):.018;e.particle.visible=motion&&active;});
    document.querySelectorAll<HTMLButtonElement>('[data-area-chip]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.areaChip===areaSelect.value)));
    status.textContent=(renderer?'':'兼容模式 · ')+(selected?byId[selected].title+' · ':'')+data.nodes.filter(matches).length+' 个概念 · '+relevantEdges().length+' 条关联';
  }
  function select(id:string|null){
    selected=id;const node=id?byId[id]:null;
    const setText=(selector:string,text:string)=>{document.querySelector<HTMLElement>(selector)!.textContent=text;};
    setText('#atlas-detail-area',node?areaById[node.area].title:'从一个概念开始');setText('#atlas-detail-title',node?.title||'探索听觉科学');setText('#atlas-detail-english',node?.english||'Sound → Perception → Technology');setText('#atlas-detail-kind',node?.kind||'六个知识层面');setText('#atlas-detail-summary',node?.summary||'点击节点或定位概念，查看明确的知识关系。');
    const link=document.querySelector<HTMLAnchorElement>('#atlas-detail-link')!;if(node){link.href=node.url;link.textContent='阅读完整词条 ↗';}else{link.href=new URL('../explore/',location.href).href;link.textContent='浏览百科词条 ↗';}
    const list=document.querySelector<HTMLUListElement>('#atlas-neighbors')!;list.replaceChildren();
    const edges=node?relevantEdges().filter(e=>e.source===id||e.target===id):[];
    setText('#atlas-neighbor-count',String(edges.length));
    for(const edge of edges){const incoming=edge.target===id,other=byId[incoming?edge.source:edge.target];const li=document.createElement('li'),button=document.createElement('button'),name=document.createElement('strong'),type=document.createElement('span'),note=document.createElement('small');button.type='button';name.textContent=other.title;type.textContent=incoming?data.types[edge.type].incoming:data.types[edge.type].outgoing;note.textContent=edge.note;button.append(name,type,note);button.addEventListener('click',()=>select(other.id));li.append(button);list.append(li);}
    if(!edges.length){const li=document.createElement('li');li.className='atlas-empty';li.textContent=node?'当前筛选下没有相邻关系。':'选中节点后，在这里逐条查看关系。';list.append(li);}
    document.querySelector<HTMLButtonElement>('#atlas-clear')!.hidden=!node;
    applyStyles();
  }
  function find(){const term=query.value.trim().toLocaleLowerCase();if(!term){select(null);return;}const node=data.nodes.find(n=>[n.title,n.english,n.id,...n.aliases].some(s=>s.toLocaleLowerCase()===term))||data.nodes.find(n=>(n.title+' '+n.english+' '+n.aliases.join(' ')).toLocaleLowerCase().includes(term));if(node){areaSelect.value='';select(node.id);controls.autoRotate=false;}else status.textContent='未找到该概念。可从建议列表或下方目录选择。';}
  document.querySelector('#atlas-find')!.addEventListener('click',find);query.addEventListener('keydown',e=>{if(e.key==='Enter')find();});query.addEventListener('change',find);
  areaSelect.addEventListener('change',()=>select(selected));relationSelect.addEventListener('change',()=>select(selected));
  document.querySelectorAll<HTMLButtonElement>('[data-area-chip]').forEach(b=>b.addEventListener('click',()=>{areaSelect.value=areaSelect.value===b.dataset.areaChip?'':b.dataset.areaChip!;select(selected);}));
  document.querySelector('#atlas-clear')!.addEventListener('click',()=>{query.value='';select(null);});
  document.querySelector('#atlas-reset')!.addEventListener('click',()=>{controls.reset();resize();controls.autoRotate=motion;});
  document.querySelector('#atlas-rotate-left')!.addEventListener('click',()=>controls.rotateLeft(Math.PI/8));
  document.querySelector('#atlas-zoom-in')!.addEventListener('click',()=>controls.dollyIn(1.2));
  document.querySelector('#atlas-zoom-out')!.addEventListener('click',()=>controls.dollyOut(1.2));
  function setMotion(value:boolean){motion=value;controls.autoRotate=value;motionButton.textContent=value?'暂停动效':'开启动效';motionButton.setAttribute('aria-pressed',String(value));applyStyles();}
  motionButton.addEventListener('click',()=>setMotion(!motion));reduced.addEventListener('change',()=>{if(reduced.matches)setMotion(false);});
  labelButton.addEventListener('click',()=>{showLabels=!showLabels;labelButton.setAttribute('aria-pressed',String(showLabels));});
  canvas.addEventListener('pointerdown',e=>{pointerDown=[e.clientX,e.clientY];});
  canvas.addEventListener('pointerup',e=>{if(!pointerDown||Math.hypot(e.clientX-pointerDown[0],e.clientY-pointerDown[1])>6){pointerDown=null;return;}pointerDown=null;const rect=canvas.getBoundingClientRect();pointer.set((e.clientX-rect.left)/rect.width*2-1,-(e.clientY-rect.top)/rect.height*2+1);raycaster.setFromCamera(pointer,camera);const hit=raycaster.intersectObjects(nodeViews.map(n=>n.mesh))[0];if(hit)select(hit.object.userData.id);});
  canvas.addEventListener('pointermove',e=>{const rect=canvas.getBoundingClientRect();pointer.set((e.clientX-rect.left)/rect.width*2-1,-(e.clientY-rect.top)/rect.height*2+1);raycaster.setFromCamera(pointer,camera);canvas.style.cursor=raycaster.intersectObjects(nodeViews.map(n=>n.mesh)).length?'pointer':'grab';});
  function resize(){width=stage!.clientWidth;height=stage!.clientHeight;camera.aspect=width/height;camera.updateProjectionMatrix();if(renderer)renderer.setSize(width,height,false);else{const ratio=Math.min(devicePixelRatio,1.7);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);ctx!.setTransform(ratio,0,0,ratio,0,0);}const fit=Math.min(1050,Math.max(470,400/(2*Math.tan(THREE.MathUtils.degToRad(camera.fov/2))*camera.aspect)));if(width<500&&controls.getDistance()<fit){camera.position.set(10,45,fit);controls.update();}}
  const observer=new ResizeObserver(resize);observer.observe(stage);resize();
  const projector=new THREE.Vector3();
  const project=(p:THREE.Vector3)=>{projector.copy(p).project(camera);return {x:(projector.x*.5+.5)*width,y:(-projector.y*.5+.5)*height,z:projector.z};};
  function layoutLabels(){const occupied:{x:number;y:number;w:number;h:number}[]=[];const linked=neighbors();const ordered=[...nodeViews].sort((a,b)=>(b.data.id===selected?1000:linked.has(b.data.id)?100:degree[b.data.id])-(a.data.id===selected?1000:linked.has(a.data.id)?100:degree[a.data.id]));for(const n of ordered){const p=project(n.position);const w=Math.min(n.label.textContent!.length*12+18,width<500?150:195),h=25,x=p.x+9+w<width-6?p.x+9:p.x-w-9,y=p.y-12;const valid=p.z<1&&p.z>0&&p.x>5&&p.x<width-5&&x>5&&x+w<width-6&&y>45&&y+h<height-100;const collision=occupied.some(b=>x<b.x+b.w+5&&x+w+5>b.x&&y<b.y+b.h+3&&y+h+3>b.y);const active=matches(n.data)&&(!selected||linked.has(n.data.id)||n.data.id===selected);const show=showLabels&&valid&&active&&(!collision||n.data.id===selected);n.label.hidden=!show;if(show){n.label.style.transform='translate('+x+'px,'+y+'px)';occupied.push({x,y,w,h});}}}
  function drawCompatible(){const c=ctx!;c.clearRect(0,0,width,height);
    c.strokeStyle='#89bdd4';c.lineWidth=.8;
    for(const trace of brain.lines){c.globalAlpha=trace.opacity;c.beginPath();trace.points.forEach((point,i)=>{const p=project(point);if(i===0)c.moveTo(p.x,p.y);else c.lineTo(p.x,p.y);});c.stroke();}
    c.fillStyle='#89bdd4';c.globalAlpha=.24;
    for(const point of brain.points){const p=project(point);if(p.z>0&&p.z<1)c.fillRect(p.x,p.y,1.1,1.1);}
    c.globalAlpha=1;for(const star of stars){const p=project(star);if(p.z>0&&p.z<1){c.fillStyle='rgba(138,183,216,.3)';c.fillRect(p.x,p.y,1.2,1.2);}}for(const edge of edgeViews){if(edge.line.material.opacity<.04)continue;c.strokeStyle=areaById[byId[edge.data.source].area].color;c.globalAlpha=edge.line.material.opacity;c.lineWidth=selected?1.2:.7;c.beginPath();edge.curve.getPoints(24).forEach((p,i)=>{const q=project(p);if(i===0)c.moveTo(q.x,q.y);else c.lineTo(q.x,q.y);});c.stroke();if(edge.particle.visible){const p=project(edge.particle.position);c.globalAlpha=.85;c.fillStyle='#c6eaff';c.beginPath();c.arc(p.x,p.y,1.3,0,Math.PI*2);c.fill();}}for(const n of [...nodeViews].sort((a,b)=>project(b.position).z-project(a.position).z)){const p=project(n.position);if(p.z<0||p.z>1)continue;const r=4.4*(470/controls.getDistance()),color=areaById[n.data.area].color;c.globalAlpha=n.mesh.material.opacity;c.shadowBlur=n.data.id===selected?24:14;c.shadowColor=color;c.fillStyle=color;c.beginPath();c.arc(p.x,p.y,r,0,Math.PI*2);c.fill();c.shadowBlur=0;}c.globalAlpha=1;}
  function tick(time:number){frame=requestAnimationFrame(tick);if(!visible||document.hidden)return;if(time-lastTime<30)return;const delta=Math.min((time-lastTime)/1000,.08);lastTime=time;if(motion)elapsed+=delta;controls.update(delta);scene.updateMatrixWorld();camera.updateMatrixWorld();edgeViews.forEach((e,i)=>e.particle.position.copy(e.curve.getPoint((elapsed*.065+i*.137)%1)));nodeViews.forEach((n,i)=>{if(motion)n.halo.scale.setScalar((n.data.id===selected?39:24)+Math.sin(elapsed*1.1+i)*1.6);});if(renderer)renderer.render(scene,camera);else drawCompatible();layoutLabels();}
  const intersection=new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;});intersection.observe(stage);
  setMotion(motion);select(new URLSearchParams(location.search).get('concept')&&byId[new URLSearchParams(location.search).get('concept')!] ? new URLSearchParams(location.search).get('concept'):null);
  frame=requestAnimationFrame(tick);
  window.addEventListener('pagehide',(event)=>{if(event.persisted)return;document.removeEventListener('fullscreenchange',syncFullscreen);document.removeEventListener('keydown',fullscreenEscape);document.documentElement.classList.remove('atlas-fullscreen-open');cancelAnimationFrame(frame);observer.disconnect();intersection.disconnect();controls.dispose();scene.traverse(object=>{const obj=object as THREE.Mesh;if(obj.geometry)obj.geometry.dispose();if(obj.material){for(const material of Array.isArray(obj.material)?obj.material:[obj.material])material.dispose();}});glow.dispose();renderer?.dispose();});
}
