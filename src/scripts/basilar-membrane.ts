import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const root=document.querySelector<HTMLElement>('#bm-lab')!;
const el=<T extends HTMLElement>(id:string)=>document.getElementById(`bm-${id}`) as T;
const message=el('message'), state=el('state'), host=el('scene');
const player=el<HTMLAudioElement>('player'), frequency=el<HTMLInputElement>('frequency');
const listen=el<HTMLInputElement>('listen'), stopButton=el<HTMLButtonElement>('stop');
let ctx:AudioContext|undefined, bank:AudioWorkletNode|undefined, sink:GainNode|undefined, monitor:GainNode|undefined;
let mediaSource:MediaElementAudioSourceNode|undefined, stream:MediaStream|undefined;
let input:AudioNode|undefined, oscillators:OscillatorNode[]=[], objectURL:string|undefined;
let mode='idle', generation=0, frozen=false, disposed=false, preparing=false;
let values=new Float32Array(96), envelope=new Float32Array(96);
const cf=(i:number)=>165.4*(10**(2.1*(1-i/95))-.88);
const hz=()=>Math.round(10**Number(frequency.value));
const format=(n:number)=>n>=1000?`${(n/1000).toFixed(1)} kHz`:`${Math.round(n)} Hz`;

async function setup(){
  if(!window.AudioContext || !window.AudioWorkletNode) throw new Error('当前浏览器不支持 AudioWorklet，请使用新版 Chrome、Edge、Firefox 或 Safari。');
  if(!ctx){
    const next=new AudioContext();ctx=next;
    try{
      await next.audioWorklet.addModule(root.dataset.worklet!);
      bank=new AudioWorkletNode(next,'basilar-bank');
      sink=next.createGain();sink.gain.value=0;bank.connect(sink).connect(next.destination);
      monitor=next.createGain();monitor.gain.value=0;monitor.connect(next.destination);
      bank.port.onmessage=bankHandler;
    }catch(error){await next.close();ctx=undefined;throw error;}
  }
  await ctx.resume();
}
function clearInput(){
  player.pause();player.hidden=true;
  input?.disconnect();input=undefined;
  oscillators.forEach(o=>{o.stop();o.disconnect();});oscillators=[];
  stream?.getTracks().forEach(t=>t.stop());stream=undefined;
  if(objectURL){URL.revokeObjectURL(objectURL);objectURL=undefined;player.removeAttribute('src');player.load();}
  if(monitor)monitor.gain.value=0;
  bank?.disconnect();bank?.port.close();bank=undefined;
  values.fill(0);envelope.fill(0);mode='idle';
  el('peak').textContent='—';el('rms').textContent='—';stopButton.disabled=true;
}
function resetBank(){
  if(!ctx||!sink)return;
  const previous=bank;
  bank=new AudioWorkletNode(ctx,'basilar-bank');bank.connect(sink);
  // New source gets a fresh bank so previous filter states cannot leak.
  bank.port.onmessage=bankHandler;
  previous?.disconnect();previous?.port.close();
}
function bankHandler({data}:MessageEvent){
  if(mode==='idle'||frozen||disposed)return;
  values=Float32Array.from(data.values);envelope=Float32Array.from(data.envelope);
  let peak=0;for(let i=1;i<96;i++)if(envelope[i]>envelope[peak])peak=i;
  el('peak').textContent=envelope[peak]>1e-7?`${format(Math.min(cf(peak),data.sampleRate*.45))} · 距蜗底 ${(peak/95*100).toFixed(0)}%`:'—（静音）';
  el('rms').textContent=envelope[peak]>1e-7?`${(20*Math.log10(envelope[peak])).toFixed(1)} dB re 1`:'—';
  el('rate').textContent=`${data.sampleRate/1000} kHz`;
}
function connect(node:AudioNode){input=node;node.connect(bank!);if(mode!=='mic')node.connect(monitor!);stopButton.disabled=false;}
function updateMonitor(){if(monitor)monitor.gain.setTargetAtTime(listen.checked&&mode!=='mic'?.3:0,ctx!.currentTime,.02);}
async function start(kind:string,file?:File){
  if(preparing)return;
  preparing=true;const token=++generation;
  clearInput();stopButton.disabled=false;state.textContent='正在准备声音…';
  try{
    await setup();if(token!==generation||disposed)return;
    resetBank();mode=kind;frozen=false;el('freeze').textContent='冻结画面';
    if(kind==='mic'){
      if(!navigator.mediaDevices?.getUserMedia)throw new Error('麦克风需要 HTTPS 或 localhost，以及支持录音的浏览器。');
      const acquired=await navigator.mediaDevices.getUserMedia({audio:{echoCancellation:false,noiseSuppression:false,autoGainControl:false}});
      if(token!==generation||disposed){acquired.getTracks().forEach(t=>t.stop());return;}
      stream=acquired;connect(ctx!.createMediaStreamSource(acquired));
      acquired.getAudioTracks().forEach(t=>t.addEventListener('ended',()=>{if(mode==='mic'){generation++;clearInput();state.textContent='麦克风已断开';}}));
      message.textContent='麦克风正在分析；始终不回放。系统仍可能施加设备增益，读数不是校准声压级。';
    }else if(kind==='file'){
      if(!file)throw new Error('请选择一个音频文件。');
      objectURL=URL.createObjectURL(file);player.src=objectURL;player.hidden=false;
      mediaSource??=ctx!.createMediaElementSource(player);connect(mediaSource);
      updateMonitor();await player.play();
      message.textContent=`正在分析：${file.name}。可暂停、拖动和重播；勾选「播放声音」可开启回放。`;
    }else{
      const mix=ctx!.createGain();mix.gain.value=.15;connect(mix);
      for(const f of(kind==='dual'?[500,3000]:[hz()])){
        const o=ctx!.createOscillator();o.frequency.value=f;o.connect(mix);o.start();oscillators.push(o);
      }
      message.textContent=kind==='dual'?'双音：500 Hz + 3000 Hz，幅度各为 0.15。该线性模型不产生双音抑制或失真产物。':'移动频率滑块，观察响应峰位置。输出幅度 0.15；显示放大不改变播放音量。';
    }
    updateMonitor();state.textContent=kind==='mic'?'实时输入 / 麦克风':kind==='file'?'本地音频 / 正在分析':kind==='dual'?'双音 / 500 + 3000 Hz':`纯音 / ${hz()} Hz`;
  }catch(error){if(token===generation){clearInput();state.textContent='输入未启动';const name=error instanceof DOMException?error.name:'';message.textContent=name==='NotAllowedError'?'浏览器未允许麦克风或声音播放。请检查站点权限，或使用纯音演示。':`无法载入声音：${error instanceof Error?error.message:String(error)} 可尝试 WAV、MP3 或其他浏览器支持的格式。`;}}
  finally{preparing=false;}
}
el('tone').onclick=()=>void start('tone');el('dual').onclick=()=>void start('dual');el('mic').onclick=()=>void start('mic');
el<HTMLInputElement>('file').onchange=e=>{const file=(e.target as HTMLInputElement).files?.[0];if(file)void start('file',file);(e.target as HTMLInputElement).value='';};
stopButton.onclick=()=>{generation++;clearInput();state.textContent='已停止 · 麦克风已释放';};
listen.onchange=updateMonitor;
player.addEventListener('pause',()=>{if(mode==='file')state.textContent=player.ended?'音频结束 / 可重播':'音频已暂停';});
player.addEventListener('play',()=>{if(mode==='file')state.textContent='本地音频 / 正在分析';});
player.addEventListener('error',()=>{if(mode==='file'){generation++;clearInput();state.textContent='音频格式不支持';message.textContent='此文件无法解码。请尝试 WAV、MP3，或当前浏览器支持的其他音频格式。';}});
frequency.oninput=()=>{el('freq-value').textContent=`${hz()} Hz`;if(mode==='tone'){oscillators[0]?.frequency.setTargetAtTime(hz(),ctx!.currentTime,.03);state.textContent=`纯音 / ${hz()} Hz`;}};
el<HTMLInputElement>('gain').oninput=e=>el('gain-value').textContent=`${(e.target as HTMLInputElement).value}×`;
el('freeze').onclick=()=>{frozen=!frozen;el('freeze').textContent=frozen?'恢复画面':'冻结画面';message.textContent=frozen?'画面已冻结，声音输入继续；停止输入可释放麦克风。':'画面已恢复。瞬时响应经屏幕抽样，闪动不代表真实声学周期。';};
el('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.querySelector('.instrument')!.requestFullscreen();}catch{message.textContent='当前浏览器不支持此全屏操作。';}};

try{
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.append(renderer.domElement);
  const scene=new THREE.Scene(), camera=new THREE.PerspectiveCamera(40,1,.1,100);
  const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.minDistance=6;controls.maxDistance=60;
  function reset(){const fit=Math.max(1,1.6/(host.clientWidth/host.clientHeight));camera.position.set(0,6*fit,10*fit);controls.target.set(0,0,0);controls.update();}reset();el('reset').onclick=reset;
  const geo=new THREE.PlaneGeometry(12,1,95,12);geo.rotateX(-Math.PI/2);
  const positions=geo.attributes.position as THREE.BufferAttribute, colors=new Float32Array(positions.count*3);
  geo.setAttribute('color',new THREE.BufferAttribute(colors,3));
  const membrane=new THREE.Mesh(geo,new THREE.MeshStandardMaterial({vertexColors:true,side:THREE.DoubleSide,metalness:.12,roughness:.6}));scene.add(membrane);
  const wire=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:0xb2fff0,wireframe:true,transparent:true,opacity:.13}));scene.add(wire);
  scene.add(new THREE.AmbientLight(0xc8e9ff,2));const light=new THREE.DirectionalLight(0xffffff,3);light.position.set(-4,8,4);scene.add(light);
  const grid=new THREE.GridHelper(16,32,0x345565,0x19394c);grid.position.y=-.08;scene.add(grid);
  const lineGeo=new THREE.BufferGeometry().setFromPoints(Array.from({length:96},(_,i)=>new THREE.Vector3(i/95*12-6,0,-1.25)));
  const line=new THREE.Line(lineGeo,new THREE.LineBasicMaterial({color:0xffce82}));scene.add(line);
  const label=(text:string,x:number)=>{const c=document.createElement('canvas');c.width=256;c.height=64;const g=c.getContext('2d')!;g.font='32px "Microsoft YaHei",sans-serif';g.fillStyle='#c9e6f2';g.textAlign='center';g.fillText(text,128,42);const texture=new THREE.CanvasTexture(c);const sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:texture,transparent:true,depthTest:false}));sprite.position.set(x,-.1,1.9);sprite.scale.set(2.4,.6,1);scene.add(sprite);};
  for(const f of[16000,8000,3000,1000,250,60]){const x=1-Math.log10(f/165.4+.88)/2.1;label(format(f),x*12-6);}
  const resize=new ResizeObserver(()=>{renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();});resize.observe(host);
  host.addEventListener('keydown',e=>{const moves:Record<string,[number,number]>={ArrowLeft:[-.5,0],ArrowRight:[.5,0],ArrowUp:[0,.5],ArrowDown:[0,-.5]};if(moves[e.key]){e.preventDefault();camera.position.x+=moves[e.key][0];camera.position.y+=moves[e.key][1];}if(e.key==='+'||e.key==='=')camera.position.multiplyScalar(.9);if(e.key==='-')camera.position.multiplyScalar(1.1);controls.update();});
  const color=new THREE.Color();let raf=0;
  function draw(){
    if(disposed)return;raf=requestAnimationFrame(draw);controls.update();
    const gain=Number(el<HTMLInputElement>('gain').value), env=el<HTMLSelectElement>('view').value==='envelope';
    for(let j=0;j<=12;j++)for(let i=0;i<96;i++){
      const index=j*96+i, x=i/95, radial=j/12;
      positions.setY(index,Math.tanh((env?envelope[i]:values[i])*gain)*1.8*Math.sin(radial*Math.PI));
      positions.setZ(index,(radial-.5)*(.35+1.8*x));
      color.setHSL(.52-Math.min(.48,envelope[i]*gain*.4),.7,.35+Math.min(.25,envelope[i]*gain*.15));
      colors.set([color.r,color.g,color.b],index*3);
    }
    const lp=lineGeo.attributes.position as THREE.BufferAttribute;
    for(let i=0;i<96;i++)lp.setY(i,Math.tanh(envelope[i]*gain)*1.8+.03);
    lp.needsUpdate=true;positions.needsUpdate=true;geo.attributes.color.needsUpdate=true;geo.computeVertexNormals();renderer.render(scene,camera);
  }draw();
  window.addEventListener('pagehide',()=>{disposed=true;generation++;clearInput();void ctx?.close();cancelAnimationFrame(raf);resize.disconnect();controls.dispose();renderer.dispose();geo.dispose();lineGeo.dispose();},{once:true});
  renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();generation++;clearInput();state.textContent='三维绘图已中断，请刷新页面';});
}catch{message.textContent='三维视图需要支持 WebGL 的浏览器与显卡。请启用硬件加速后刷新；可返回词条查看静态图。';state.textContent='三维视图不可用';for(const id of['tone','dual','mic','file'])el<HTMLInputElement>(id).disabled=true;}

window.addEventListener('pageshow', e=>{if(e.persisted)location.reload();});
