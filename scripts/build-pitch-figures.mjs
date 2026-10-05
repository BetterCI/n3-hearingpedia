import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
// Original vector figures. Explanatory prose is kept in external captions.
const out=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../public/figures/pitch');
await fs.mkdir(out,{recursive:true});
const sharp=process.argv.includes('--png')?(await import('sharp')).default:null;
const C={ink:'#202020',muted:'#555555',blue:'#0072b2',orange:'#d55e00',teal:'#00846b',line:'#cccccc',white:'#ffffff'};
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
let items=[];
const put=s=>items.push(s);
const txt=(x,y,s,size=22,color=C.ink,anchor='start',weight=400)=>put(`<text x="${x}" y="${y}" font-size="${size}" fill="${color}" text-anchor="${anchor}" font-weight="${weight}">${esc(s)}</text>`);
const line=(x1,y1,x2,y2,color=C.line,w=1.5,dash='')=>put(`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="${w}" ${dash?`stroke-dasharray="${dash}"`:''}/>`);
const rect=(x,y,w,h,fill=C.white,stroke=C.ink)=>put(`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}" stroke="${stroke}" stroke-width="1.5"/>`);
const circle=(x,y,r,fill=C.white,stroke=C.ink,w=1.5)=>put(`<circle cx="${x}" cy="${y}" r="${r}" fill="${fill}" stroke="${stroke}" stroke-width="${w}"/>`);
const curve=(pts,color=C.blue,w=2,dash='')=>put(`<path d="${pts.map((p,i)=>`${i?'L':'M'}${p[0].toFixed(2)},${p[1].toFixed(2)}`).join(' ')}" fill="none" stroke="${color}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round" ${dash?`stroke-dasharray="${dash}"`:''}/>`);
const arrow=(x1,y1,x2,y2,color=C.muted)=>put(`<path d="M${x1},${y1} L${x2},${y2}" fill="none" stroke="${color}" stroke-width="1.8" marker-end="url(#arrow)"/>`);
const panel=(x,y,letter,title)=>{txt(x,y,`(${letter})`,25,C.ink,'start',700);txt(x+49,y,title,24);};
const vertical=(x,y,s,size=21)=>put(`<text x="${x}" y="${y}" font-size="${size}" text-anchor="middle" transform="rotate(-90 ${x} ${y})" fill="${C.ink}">${esc(s)}</text>`);
const samples=(n,f)=>Array.from({length:n},(_,i)=>f(i/(n-1)));
const files=[];
const start=()=>{items=[];};
async function save(name,title,desc,h){
  const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="${h}" viewBox="0 0 1400 ${h}" role="img" aria-labelledby="title desc"><title id="title">${esc(title)}</title><desc id="desc">${esc(desc)}</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="${C.muted}"/></marker></defs><rect width="1400" height="${h}" fill="white"/><g font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif">${items.join('\n')}</g></svg>`;
  await fs.writeFile(path.join(out,name+'.svg'),svg);
  if(sharp)await sharp(Buffer.from(svg)).png().toFile(path.join(out,name+'.png'));
  files.push({name,title,width:1400,height:h});
}
function person(x,y,color=C.muted,scale=1){
  circle(x,y,16*scale,C.white,C.ink,1.8);
  put(`<path d="M${x-27*scale},${y+65*scale} L${x-27*scale},${y+41*scale} Q${x-27*scale},${y+23*scale} ${x},${y+23*scale} Q${x+27*scale},${y+23*scale} ${x+27*scale},${y+41*scale} L${x+27*scale},${y+65*scale}" fill="${color}" fill-opacity="0.15" stroke="${C.ink}" stroke-width="1.8"/>`);
}
function note(x,y,color=C.ink,r=7){put(`<ellipse cx="${x}" cy="${y}" rx="${r}" ry="${r*.65}" transform="rotate(-20 ${x} ${y})" fill="${color}"/>`);line(x+r*.8,y,x+r*.8,y-27,color,1.8);}
function axes(x,y,w,h,max,label,ticks,mode='wave'){
  line(x,y+h,x+w,y+h,C.ink);line(x,y,x,y+h,C.ink);
  ticks.forEach(v=>{const xx=x+v/max*w;line(xx,y+h,xx,y+h+5,C.ink);txt(xx,y+h+30,String(v),20,C.ink,'middle');});
  (mode==='wave'?[[1,'1'],[0,'0'],[-1,'−1']]:[[1,'1'],[0,'0']]).forEach(([v,label])=>{const yy=mode==='wave'?y+h/2-v*h/2:y+h-v*h;line(x-5,yy,x,yy,C.ink);txt(x-13,yy+7,label,19,C.ink,'end');});
  if(mode==='wave')line(x,y+h/2,x+w,y+h/2,C.line,1,'4 5');
  txt(x+w/2,y+h+63,label,21,C.ink,'middle');
}

// 1. Line-drawn everyday scenes and schematic contours.
start();panel(47,38,'a','音乐旋律');panel(740,38,'b','普通话汉语声调');panel(47,401,'c','语音语调');panel(740,401,'d','鸡尾酒会');
person(132,128,C.muted,1.1);rect(79,206,196,28);
for(let i=1;i<14;i++)line(79+i*14,206,79+i*14,234,C.ink,1);
const melody=[[326,180],[383,126],[440,146],[498,95],[556,128]];
curve(melody,C.blue,1.7);melody.forEach(p=>note(...p,C.blue));arrow(307,227,611,227);txt(462,260,'音符次序',20,C.ink,'middle');vertical(293,159,'相对音高',20);txt(99,303,'旋律轮廓与音程关系',22);
const toneYs=[[.85,.85,.85,.85],[.17,.35,.60,.9],[.55,.14,.11,.56],[.92,.68,.37,.12]];
toneYs.forEach((values,i)=>{const x=782+i*141;txt(x+46,100,['妈 mā','麻 má','马 mǎ','骂 mà'][i],23,C.ink,'middle');line(x,232,x+92,232,C.ink,1);line(x,122,x,232,C.ink,1);curve(values.map((v,j)=>[x+j*92/3,224-v*99]),C.blue,2.5);txt(x+46,269,['一声','二声','三声','四声'][i],20,C.ink,'middle');});
vertical(756,180,'相对音高',20);txt(1076,307,'归一化时间',20,C.ink,'middle');
person(126,496,C.muted,.95);txt(213,462,'你来了。',23);txt(213,578,'你来了？',23);line(215,527,600,527,C.ink,1);line(215,644,600,644,C.ink,1);curve([[225,492],[345,492],[461,501],[574,519]],C.ink,2);curve([[225,622],[345,622],[461,610],[574,578]],C.blue,2);txt(218,692,'时间',20);txt(604,511,'陈述',20);txt(604,630,'疑问',20);
person(810,501,C.muted,.95);person(1006,488,C.muted,.95);person(1204,512,C.blue,.95);txt(801,622,'说话者 1',20,C.ink,'middle');txt(1015,622,'说话者 2',20,C.ink,'middle');txt(1210,622,'目标说话者',20,C.blue,'middle');curve([[777,567],[800,556],[826,570],[849,548],[874,564]],C.muted,1.7,'5 4');curve([[964,563],[991,554],[1014,561],[1039,550],[1063,558]],C.muted,1.7,'2 4');curve([[1149,576],[1174,550],[1199,565],[1224,539],[1250,551],[1278,535]],C.blue,2.5);txt(771,689,'音高线索与音色、空间、语义及注意共同作用',20);
await save('01-everyday-scenes','日常聆听中的音高','四个分面：音乐旋律、普通话汉语声调、语音语调、多人交谈。线描人物与音高曲线均为示意。',730);

// 2. Mathematical waveforms and exact line spectra.
const signal=(harm,t)=>harm.reduce((a,n)=>a+Math.sin(2*Math.PI*n*200*t),0)/harm.length;
start();
for(let row=0;row<2;row++){
  const offset=row*353,color=row?C.orange:C.blue,harm=row?[2,3,4]:[1,2,3,4];panel(50,36+offset,row?'c':'a',row?'缺失基频：波形':'保留基频：波形');panel(770,36+offset,row?'d':'b',row?'缺失基频：频谱':'保留基频：频谱');
  const x=125,y=108+offset,w=500,h=154;axes(x,y,w,h,15,'时间 / ms',[0,5,10,15]);vertical(64,y+h/2,'归一化幅度');curve(samples(1501,v=>[x+v*w,y+h/2-signal(harm,v*.015)*h/2]),color,2);
  const p1=x+w/3,p2=x+w*2/3;line(p1,y-14,p2,y-14,C.ink);line(p1,y-18,p1,y-10,C.ink);line(p2,y-18,p2,y-10,C.ink);txt((p1+p2)/2,y-29,'5 ms',21,C.ink,'middle');
  const fx=841,fy=y,fw=489;axes(fx,fy,fw,h,1000,'频率 / Hz',[0,200,400,600,800,1000],'amplitude');vertical(776,fy+h/2,'分量幅度 / 相对值');harm.forEach(n=>{const xx=fx+n*200/1000*fw;line(xx,fy+h,xx,fy,color,2.5);circle(xx,fy,3,color,color);});
  if(row){const xx=fx+200/1000*fw;line(xx,fy+h,xx,fy+15,C.muted,1.3,'5 5');rect(xx-31,fy+64,62,27,C.white,'none');txt(xx,fy+85,'缺失',20,C.muted,'middle');}
}
await save('02-missing-fundamental','缺失基频与共同周期','保留200、400、600、800Hz与仅保留400、600、800Hz的波形和频谱。两组最短周期均为5毫秒。',707);

// 3. Gaussian amplitude filters are illustrative, not measured auditory filters.
start();
for(let row=0;row<2;row++){
  const offset=row*369,color=row?C.orange:C.blue,harm=row?[12,13,14]:[2,3,4],center=row?2600:600,bw=row?650:100,sigma=bw/Math.sqrt(8*Math.log(2));
  const weight=harm.map(n=>Math.exp(-.5*((n*200-center)/sigma)**2)),norm=weight.reduce((a,b)=>a+b,0);panel(48,36+offset,row?'c':'a',row?'高阶谐波与宽滤波器':'低阶谐波与窄滤波器');panel(768,36+offset,row?'d':'b',`中心 ${center} Hz 的输出`);
  const x=125,y=112+offset,w=500,h=157,min=row?2000:0,max=row?3200:1200;axes(x,y,w,h,max-min,'频率 / Hz',[],'amplitude');vertical(62,y+h/2,'增益 / 相对值');
  [min,min+400,min+800,max].forEach(f=>{const xx=x+(f-min)/(max-min)*w;line(xx,y+h,xx,y+h+5,C.ink);txt(xx,y+h+30,String(f),20,C.ink,'middle');});harm.forEach(n=>{const xx=x+(n*200-min)/(max-min)*w;line(xx,y+h,xx,y,C.ink,1.8);});
  (row?[center]:harm.map(n=>n*200)).forEach(cf=>curve(samples(501,v=>[x+v*w,y+h-Math.exp(-.5*((min+v*(max-min)-cf)/sigma)**2)*h]),C.teal,cf===center?2.5:1.7,cf===center?'':'4 4'));txt(x,y-18,`半高全宽 ${bw} Hz`,20,C.teal);
  const p1=x+(harm[0]*200-min)/(max-min)*w,p2=x+(harm[1]*200-min)/(max-min)*w;line(p1,y-39,p2,y-39,C.ink);txt((p1+p2)/2,y-48,'200 Hz',20,C.ink,'middle');
  const tx=841,ty=y,tw=489,th=h;axes(tx,ty,tw,th,15,'时间 / ms',[0,5,10,15]);vertical(776,ty+th/2,'归一化幅度');
  const wave=t=>harm.reduce((a,n,i)=>a+weight[i]*Math.sin(2*Math.PI*n*200*t),0)/norm;
  const envelope=t=>Math.hypot(harm.reduce((a,n,i)=>a+weight[i]*Math.cos(2*Math.PI*n*200*t),0),harm.reduce((a,n,i)=>a+weight[i]*Math.sin(2*Math.PI*n*200*t),0))/norm;
  curve(samples(2001,v=>[tx+v*tw,ty+th/2-wave(v*.015)*th/2]),color,1.6);curve(samples(701,v=>[tx+v*tw,ty+th/2-envelope(v*.015)*th/2]),C.teal,2.6,'7 4');
}
line(132,741,185,741,C.ink,1.8);txt(198,748,'谐波分量',20);line(421,741,474,741,C.teal,2.5);txt(488,748,'滤波器增益',20);line(764,741,817,741,C.blue,2);txt(831,748,'输出波形',20);line(1051,741,1104,741,C.teal,2.5,'7 4');txt(1118,748,'输出包络',20);
await save('03-harmonic-resolvability','谐波可分辨性示意','低阶与高阶谐波的间距均为200Hz，高斯幅度滤波器带宽100/650Hz。中心通道输出及解析包络为数学模型。',784);

// 4. Parallel candidate explanations; arrows are not established causal pathways.
start();txt(700,36,'输入：200、400、600、800 Hz 谐波复合音',24,C.ink,'middle');arrow(544,55,345,106);arrow(857,55,1070,106);panel(48,140,'a','位置相关线索');panel(768,140,'b','时域相关线索');
const px=127,py=213,pw=498,ph=165;axes(px,py,pw,ph,1000,'频率 / Hz',[0,200,400,600,800,1000],'amplitude');vertical(62,py+ph/2,'示意响应 / 相对值');curve(samples(701,v=>[px+v*pw,py+ph-[200,400,600,800].reduce((a,f)=>a+Math.exp(-.5*((v*1000-f)/42)**2),0)*ph]),C.blue,2.4);
const spikeSets=[[.1,5.2,10.1,15.3],[.2,10.3,15.1],[5.3,10.2],[.1,5.1,15.2]];
spikeSets.forEach((times,i)=>{const yy=236+i*46;line(861,yy,1322,yy,C.line);txt(839,yy+7,String(i+1),20,C.ink,'end');times.forEach(t=>line(861+t/20*461,yy,861+t/20*461,yy-28,C.orange,2));});vertical(786,305,'合成放电序列');[0,5,10,15,20].forEach(t=>txt(861+t/20*461,416,String(t),20,C.ink,'middle'));txt(1091,449,'时间 / ms',21,C.ink,'middle');txt(373,497,'候选计算：响应峰之间的关系',22,C.blue,'middle');txt(1085,497,'候选计算：重复规律与放电间隔',22,C.orange,'middle');arrow(373,520,595,587);arrow(1085,520,813,587);txt(700,625,'音高判断：可能联合利用位置与时域信息',24,C.ink,'middle');
await save('04-place-time-candidates','位置与时域的候选解释','同一复合音的示意位置分布、合成放电事件，以及并行的候选音高计算。箭头为解释路径。',667);

// 5. Five task schematics, with no fixed hierarchy.
start();panel(48,38,'a','差异辨别');panel(518,38,'b','高低判断');panel(981,38,'c','音高排序');
for(let j=0;j<3;j++){const x=91+j*128;for(let k=0;k<2;k++)curve(samples(101,v=>[x+k*48+v*39,151-Math.sin(2*Math.PI*v*(j===2&&k===1?3:2))*22]),j===2&&k===1?C.orange:C.ink,1.5);txt(x+44,209,['甲','乙','丙'][j],21,C.ink,'middle');}txt(257,261,'判断哪一组与其余不同',21,C.ink,'middle');
line(572,213,891,213,C.ink);line(572,213,572,81,C.ink);txt(731,257,'第一声 → 第二声',21,C.ink,'middle');vertical(536,144,'相对音高',19);line(600,166,681,166,C.ink,2.6);line(785,115,866,115,C.blue,2.6);arrow(697,166,768,115);
line(1029,213,1341,213,C.ink);line(1029,213,1029,81,C.ink);vertical(992,144,'相对音高',19);[174,119,147,88].forEach((y,j)=>{circle(1065+j*78,y,6,C.ink);txt(1065+j*78,245,['甲','乙','丙','丁'][j],21,C.ink,'middle');});
panel(48,343,'d','音高匹配');panel(769,343,'e','旋律与音程');line(140,545,625,545,C.ink);line(140,545,140,393,C.ink);vertical(91,472,'相对音高',20);line(181,458,277,458,C.ink,2.5);line(427,416,519,416,C.orange,2.5);line(427,458,519,458,C.orange,2,'5 4');arrow(551,419,551,455);txt(230,584,'参照音',21,C.ink,'middle');txt(473,584,'可调比较音',21,C.orange,'middle');
const ys=[506,450,478,414,472];line(854,545,1309,545,C.ink);line(854,545,854,391,C.ink);vertical(803,472,'相对音高',20);curve(ys.map((y,j)=>[882+j*99,y]),C.blue,1.4);ys.forEach((y,j)=>note(882+j*99,y,C.blue));txt(1082,584,'音符次序',21,C.ink,'middle');
await save('05-pitch-tasks','音高任务示意','辨别、高低判断、排序、匹配、旋律与音程五种任务并列示意，没有难度顺序。',638);

// 6. Pulse events, not actual biphasic current waveforms.
start();
function electrodogram(x,y,w,h,ch,rate,am,color){
  const step=h/6;for(let c=1;c<=5;c++){const yy=y+c*step;line(x,yy,x+w,yy,C.line,1);txt(x-15,yy+6,String(c),19,C.ink,'end');}
  for(let k=0;k<rate*.1;k++){const t=k/rate,yy=y+ch*step,amp=am?.65+.3*Math.cos(2*Math.PI*am*t):.8;line(x+t/.1*w,yy,x+t/.1*w,yy-amp*step*.82,color,am?1.4:2);}
  if(am)curve(samples(501,v=>[x+v*w,y+ch*step-(.65+.3*Math.cos(2*Math.PI*am*v*.1))*step*.82]),C.ink,1.6,'5 3');
  [0,25,50,75,100].forEach(t=>{const xx=x+t/100*w;line(xx,y+h,xx,y+h+4,C.ink);txt(xx,y+h+28,String(t),20,C.ink,'middle');});line(x,y+h,x+w,y+h,C.ink);txt(x+w/2,y+h+60,'时间 / ms',21,C.ink,'middle');vertical(x-64,y+h/2,'通道序号',21);
}
const configs=[['刺激位置','通道 2；100 脉冲/秒','通道 4；100 脉冲/秒',[2,100,0],[4,100,0]],['脉冲率','100 脉冲/秒','200 脉冲/秒',[3,100,0],[3,200,0]],['振幅调制频率','载体 1000 脉冲/秒；调制 50 Hz','载体 1000 脉冲/秒；调制 100 Hz',[3,1000,50],[3,1000,100]]];
configs.forEach((c,i)=>{const oy=i*293;panel(49,35+oy,['a','b','c'][i],c[0]);txt(125,78+oy,c[1],21,C.blue);txt(846,78+oy,c[2],21,C.orange);electrodogram(125,95+oy,500,125,...c[3],C.blue);electrodogram(846,95+oy,484,125,...c[4],C.orange);});
await save('06-ci-pitch-parameters','人工耳蜗刺激参数示意','成对比较位置、100/200脉冲每秒、载体1000脉冲每秒下50/100Hz振幅调制。任意通道编号、相对幅度、示意事件。',891);

// 7. Pitch helix: azimuth = pitch class; axial height = semitone index.
start();panel(48,36,'a','音高螺旋');panel(889,36,'b','音级圆环');
const cx=405,rx=226,ry=87,base=683,step=21;
const point=n=>[cx+rx*Math.cos(n*Math.PI/6),base-step*n-ry*Math.sin(n*Math.PI/6)];
for(const n of [0,12,24])curve(samples(181,v=>[cx+rx*Math.cos(v*2*Math.PI),base-step*n-ry*Math.sin(v*2*Math.PI)]),C.line,1,'4 5');line(cx-rx,base+13,cx-rx,base-24*step-13,C.line,1,'4 5');line(cx+rx,base+13,cx+rx,base-24*step-13,C.line,1,'4 5');arrow(97,720,97,96);vertical(58,407,'音高高低（每级对应一个半音）',22);
for(let n=0;n<24;n+=.10)curve([point(n),point(Math.min(n+.10,24))],Math.sin((n+.05)*Math.PI/6)<0?C.blue:C.muted,2.4);
const pitchClasses=['C','升C','D','升D','E','F','升F','G','升G','A','升A','B'];
for(let n=0;n<=24;n++){const[x,y]=point(n);note(x,y,n%12===0?C.blue:C.ink,n%12===0?9:5);if(n%12===0){line(x+15,y,x+42,y,C.blue);txt(x+54,y+7,`C${4+n/12}`,25,C.blue);}}
line(743,base,743,base-12*step,C.ink);line(736,base,750,base,C.ink);line(736,base-12*step,750,base-12*step,C.ink);txt(767,557,'一个八度',21);txt(767,587,'12 半音',21);txt(420,817,'同一音级在不同八度中对齐',21,C.ink,'middle');
const rcx=1119,rcy=380,rr=158;circle(rcx,rcy,rr,C.white,C.line,1.4);
for(let n=0;n<12;n++){const t=n*Math.PI/6,x=rcx+rr*Math.cos(t),y=rcy-rr*Math.sin(t);circle(x,y,n===0?7:4,n===0?C.blue:C.ink,n===0?C.blue:C.ink);txt(rcx+(rr+38)*Math.cos(t),rcy-(rr+38)*Math.sin(t)+7,pitchClasses[n],n===0?26:22,n===0?C.blue:C.ink,'middle');}
curve(samples(50,v=>{const t=.06+v*.38;return[rcx+117*Math.cos(t),rcy-117*Math.sin(t)]}),C.muted,1.8);const a=.44;arrow(rcx+117*Math.cos(a-.08),rcy-117*Math.sin(a-.08),rcx+117*Math.cos(a),rcy-117*Math.sin(a));txt(rcx,rcy-9,'十二平均律',22,C.ink,'middle');txt(rcx,rcy+28,'十二个音级',22,C.ink,'middle');txt(rcx,660,'圆周角度表示音级',22,C.ink,'middle');txt(rcx,701,'C4、C5、C6 对应同一个 C 音级',20,C.blue,'middle');
await save('07-pitch-helix','音高螺旋与音级圆环','每圈12半音、每圈一个八度；C4、C5、C6竖直对齐。旁边圆环显示十二平均律的十二个音级。概念几何示意。',849);

const checks={fullPeriod5ms:Math.max(...samples(401,v=>Math.abs(signal([1,2,3,4],v*.015)-signal([1,2,3,4],v*.015+.005)))),missingPeriod5ms:Math.max(...samples(401,v=>Math.abs(signal([2,3,4],v*.015)-signal([2,3,4],v*.015+.005)))),lowHarmonicSpacing:[200,200],highHarmonicSpacing:[200,200],ciEventCounts100ms:[10,20,100],gaussianFwhmHz:[100,650],helixOctaveSemitones:12,helixCAlignmentError:Math.max(Math.abs(point(0)[0]-point(12)[0]),Math.abs(point(0)[0]-point(24)[0])),figureCount:files.length,style:'White background; lettered panels; no decorative headers, cards, or prose banners.'};
if(checks.fullPeriod5ms>1e-12||checks.missingPeriod5ms>1e-12||checks.helixCAlignmentError>1e-12||files.length!==7)throw Error('Figure numeric verification failed');
await fs.writeFile(path.resolve(out,'../../../docs/research/pitch-figure-checks.json'),JSON.stringify({files,checks},null,2)+'\n');
if(sharp){
const rowHeights=Array.from({length:Math.ceil(files.length/2)},(_,i)=>Math.ceil(Math.max(...files.slice(i*2,i*2+2).map(f=>f.height))*650/1400)+55);
const composites=await Promise.all(files.map(async(f,i)=>({input:await sharp(path.join(out,f.name+'.png')).resize({width:650}).toBuffer(),left:25+(i%2)*700,top:25+rowHeights.slice(0,Math.floor(i/2)).reduce((a,b)=>a+b,0)})));
await sharp({create:{width:1400,height:rowHeights.reduce((a,b)=>a+b,0),channels:4,background:'#f4f4f4'}}).composite(composites).png().toFile(path.join(out,'overview.png'));
}
console.log(JSON.stringify({figures:files.length,checks,output:out},null,2));
