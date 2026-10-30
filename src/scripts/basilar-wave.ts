// Comparison branch: analytic steady-state response of the original biquads.
// The time phase is intentionally slowed; the frequency response is not rescaled.
import {coupledWaveResponse} from '../lib/basilar-coupled-model.ts';
export function waveResponse(frequency:number, count=1201, fs=48000) {
  const omega=2*Math.PI*frequency/fs;
  const z1r=Math.cos(omega), z1i=-Math.sin(omega);
  const z2r=Math.cos(2*omega), z2i=-Math.sin(2*omega);
  return Array.from({length:count},(_,i)=>{
    const x=i/(count-1), cf=165.4*(10**(2.1*(1-x))-.88);
    const w=2*Math.PI*Math.min(cf,fs*.45)/fs, alpha=Math.sin(w)/10;
    const b0=alpha/(1+alpha), a1=-2*Math.cos(w)/(1+alpha), a2=(1-alpha)/(1+alpha);
    const nr=b0*(1-z2r), ni=-b0*z2i;
    const dr=1+a1*z1r+a2*z2r, di=a1*z1i+a2*z2i, denominator=dr*dr+di*di;
    const hr=(nr*dr+ni*di)/denominator, hi=(ni*dr-nr*di)/denominator;
    const delay=Math.round(fs*(.0003+.006*x*x))/fs, angle=-omega*fs*delay;
    return {x, re:hr*Math.cos(angle)-hi*Math.sin(angle), im:hr*Math.sin(angle)+hi*Math.cos(angle), amplitude:Math.hypot(hr,hi)};
  });
}

export function initBasilarWave(){
  document.querySelectorAll<HTMLElement>('[data-basilar-wave]').forEach(root=>{
    if(root.dataset.initialized)return;
    if(!root.querySelector('[data-wave-model]')||!root.querySelector('[data-wave-controls]')||!root.querySelector('canvas'))return;
    root.dataset.initialized='true';
    const canvas=root.querySelector<HTMLCanvasElement>('canvas')!, ctx=canvas.getContext('2d');
    if(!ctx)return;
    const slider=root.querySelector<HTMLInputElement>('[data-wave-slider]')!;
    const number=root.querySelector<HTMLInputElement>('[data-wave-frequency]')!;
    const speed=root.querySelector<HTMLSelectElement>('[data-wave-speed]')!;
    const model=root.querySelector<HTMLSelectElement>('[data-wave-model]')!;
    const pause=root.querySelector<HTMLButtonElement>('[data-wave-pause]')!;
    const status=root.querySelector<HTMLElement>('[data-wave-status]')!;
    let frequency=1000, response=coupledWaveResponse(frequency), phase=0, playing=!matchMedia('(prefers-reduced-motion: reduce)').matches;
    let visible=false, last=0, frame=0, width=900, height=430, disposed=false;
    const peakPosition=(f:number)=>1-Math.log10(f/165.4+.88)/2.1;
    function updateStatus(){
      pause.textContent=playing?'暂停动画':'播放动画';pause.setAttribute('aria-pressed',String(!playing));
      const cycles=Number(speed.value);
      const peak=response.reduce((a,b)=>a.amplitude>b.amplitude?a:b);
      status.textContent=`${frequency} Hz · 计算峰位：距蜗底 ${(peak.x*100).toFixed(1)}%（Greenwood 参考 ${(peakPosition(frequency)*100).toFixed(1)}%）· ${playing?'慢动作':'已暂停'}：${cycles} 周期/秒（约 1/${Math.round(frequency/cycles)} 速度）· ${model.value==='coupled'?'一维被动耦合 · 各频率峰值归一化':'并联滤波器 · 非真实行波包络'} · 无声`;
      canvas.setAttribute('aria-label',`${frequency} Hz 的空间响应：青色波形随时间振动，橙色振幅包络固定，计算峰位在距蜗底 ${(peak.x*100).toFixed(1)}%。`);
    }
    function draw(){
      const g=ctx!;g.clearRect(0,0,width,height);g.fillStyle='#fff';g.fillRect(0,0,width,height);
      const small=width<560, left=small?48:68, right=width-20, top=small?75:58, bottom=height-54;
      const X=(x:number)=>left+x*(right-left), Y=(y:number)=>top+(1.2-y)/2.4*(bottom-top);
      g.font=`${small?11:13}px "Microsoft YaHei", sans-serif`;g.textAlign='center';g.lineWidth=1;
      for(let tick=0;tick<=100;tick+=20){g.strokeStyle='#e3eaed';g.beginPath();g.moveTo(X(tick/100),top);g.lineTo(X(tick/100),bottom);g.stroke();g.fillStyle='#526370';g.fillText(String(tick),X(tick/100),bottom+21);}
      for(const tick of[-1,-.5,0,.5,1]){g.strokeStyle=tick===0?'#9bafb9':'#e3eaed';g.beginPath();g.moveTo(left,Y(tick));g.lineTo(right,Y(tick));g.stroke();g.textAlign='right';g.fillStyle='#526370';g.fillText(String(tick),left-9,Y(tick)+4);}
      function curve(value:(point:typeof response[number])=>number,color:string,dashed=false){g.beginPath();g.strokeStyle=color;g.lineWidth=2;g.setLineDash(dashed?[6,5]:[]);response.forEach((p,i)=>{if(i===0)g.moveTo(X(p.x),Y(value(p)));else g.lineTo(X(p.x),Y(value(p)));});g.stroke();g.setLineDash([]);}
      curve(p=>p.amplitude,'#d67832');curve(p=>-p.amplitude,'#d67832',true);
      curve(p=>p.re*Math.cos(phase)-p.im*Math.sin(phase),'#167d94');
      g.fillStyle='#213d49';g.textAlign='left';g.font=`${small?12:15}px "Microsoft YaHei",sans-serif`;g.fillText(`${frequency} Hz：运动的波形，固定的振幅包络`,left,24);
      function key(x:number,y:number,color:string,text:string){g.strokeStyle=color;g.lineWidth=3;g.beginPath();g.moveTo(x,y);g.lineTo(x+22,y);g.stroke();g.fillStyle='#526370';g.font='11px "Microsoft YaHei",sans-serif';g.fillText(text,x+29,y+4);}
      key(left,small?44:42,'#167d94','瞬时响应');key(left+(small?0:140),small?62:42,'#d67832','正弦振幅包络（±）');
      g.font=`${small?11:12}px "Microsoft YaHei",sans-serif`;g.textAlign='center';g.fillStyle='#526370';g.fillText('距蜗底的全长比例（%）  蜗底 → 蜗顶',(left+right)/2,height-12);
      g.save();g.translate(small?13:18,(top+bottom)/2);g.rotate(-Math.PI/2);g.fillText(model.value==='coupled'?'相对位移（逐频峰值归一化）':'滤波响应（任意单位）',0,0);g.restore();
    }
    function tick(now:number){
      frame=0;if(disposed)return;
      if(last)phase=(phase+Math.min((now-last)/1000,.1)*2*Math.PI*Number(speed.value))%(2*Math.PI);
      last=now;draw();schedule();
    }
    function schedule(){if(playing&&visible&&!document.hidden&&!frame&&!disposed)frame=requestAnimationFrame(tick);}
    function halt(){cancelAnimationFrame(frame);frame=0;last=0;}
    function setFrequency(value:number){
      frequency=Math.max(60,Math.min(16000,Math.round(value)));number.value=String(frequency);slider.value=String(Math.log10(frequency));
      response=model.value==='coupled'?coupledWaveResponse(frequency):waveResponse(frequency);updateStatus();draw();
    }
    slider.addEventListener('input',()=>setFrequency(10**Number(slider.value)));
    number.addEventListener('input',()=>{if(Number.isFinite(number.valueAsNumber)&&number.valueAsNumber>=60&&number.valueAsNumber<=16000)setFrequency(number.valueAsNumber);});
    number.addEventListener('change',()=>{if(number.value.trim()&&Number.isFinite(number.valueAsNumber))setFrequency(number.valueAsNumber);else number.value=String(frequency);});
    pause.addEventListener('click',()=>{playing=!playing;halt();updateStatus();schedule();});
    speed.addEventListener('change',()=>{last=0;updateStatus();});
    model.addEventListener('change',()=>setFrequency(frequency));
    root.querySelectorAll<HTMLButtonElement>('[data-wave-preset]').forEach(button=>button.addEventListener('click',()=>setFrequency(Number(button.dataset.wavePreset))));
    const resize=new ResizeObserver(()=>{const rect=canvas.getBoundingClientRect();width=rect.width;height=width<560?330:430;canvas.style.height=`${height}px`;const ratio=Math.min(devicePixelRatio,2);canvas.width=Math.round(width*ratio);canvas.height=Math.round(height*ratio);ctx.setTransform(ratio,0,0,ratio,0,0);draw();});
    const observer=new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(visible)schedule();else halt();});
    const onVisibility=()=>{if(document.hidden)halt();else schedule();};document.addEventListener('visibilitychange',onVisibility);
    root.querySelector<HTMLElement>('[data-wave-controls]')!.hidden=false;
    root.querySelector<HTMLElement>('[data-wave-fallback]')!.hidden=true;
    resize.observe(canvas);observer.observe(root);updateStatus();draw();
    window.addEventListener('pagehide',()=>{disposed=true;halt();resize.disconnect();observer.disconnect();document.removeEventListener('visibilitychange',onVisibility);},{once:true});
    window.addEventListener('pageshow',e=>{if(e.persisted){disposed=false;resize.observe(canvas);observer.observe(root);document.addEventListener('visibilitychange',onVisibility);schedule();}});
  });
}
