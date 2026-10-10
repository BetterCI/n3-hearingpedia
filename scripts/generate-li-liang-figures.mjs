import {mkdir,writeFile} from 'node:fs/promises';
const out='public/figures/li-liang';await mkdir(out,{recursive:true});
const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
const txt=(x,y,s,size=22,color='#26334b')=>`<text x="${x}" y="${y}" font-size="${size}" fill="${color}">${escape(s)}</text>`;
const rect=(x,y,w,h,c='#f4f7fc')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="14" fill="${c}" stroke="#d9e2ef"/>`;
const start=(h,title)=>`<svg xmlns="http://www.w3.org/2000/svg" width="960" height="${h}" viewBox="0 0 960 ${h}" role="img"><title>${title}</title><rect width="960" height="${h}" fill="white"/><g font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif">`;
let s=start(480,'三种范式：操纵、任务与指标');s+=txt(35,48,'三种任务，三类指标',30)+txt(35,80,'范式概念对照｜不表示同一实验装置或相同刺激参数',18,'#66758a');
const cards=[['语音去掩蔽','操纵：目标与干扰声像','任务：复述目标语句','指标：关键词识别表现','问题：是否更容易选出目标？'],['短暂声学信息保留','操纵：双耳关系与延迟','任务：检测相关性中断','指标：任务阈值（毫秒）','问题：能否跨时间比较输入？'],['前脉冲抑制','操纵：学习、分离、干预','任务：记录动物惊跳反应','指标：相对抑制比例','问题：门控怎样受到调节？']];
cards.forEach((a,i)=>{const x=35+i*300;s+=rect(x,112,280,305);s+=txt(x+18,155,a[0],24,'#315bc6');a.slice(1).forEach((v,j)=>s+=txt(x+18,205+j*52,v,j===3?17:19));});s+=txt(35,452,'识别率、检测阈值与惊跳抑制不能互相替代。',20);await writeFile(out+'/three-paradigms.svg',s+'</g></svg>');
s=start(550,'反射延迟的指数下降模型教学示例');s+=txt(35,45,'时间常数怎样改变曲线？',30)+txt(35,77,'教学模型｜假设参数｜非论文实测数据',20,'#aa4b21');
const X=d=>105+d*11.8,Y=p=>440-(p-20)*4.8;
for(const p of [20,40,60,80]){s+=`<path d="M105 ${Y(p)}H860" stroke="#e3e8f1"/>`;s+=txt(58,Y(p)+7,String(p),18);}
s+='<path d="M105 112V440H860" fill="none" stroke="#55657c" stroke-width="2"/>';
for(const d of [0,16,32,48,64])s+=txt(X(d)-10,470,String(d),18);
s+=txt(350,508,'模拟反射延迟 d（ms）',22)+txt(105,108,'识别正确率（%）',19);
for(const [tau,color] of [[16,'#305ec8'],[32,'#ba6a21']]){const pts=Array.from({length:129},(_,i)=>{const d=i/2,p=30+50*Math.exp(-d/tau);return `${X(d)},${Y(p)}`}).join(' ');s+=`<polyline points="${pts}" fill="none" stroke="${color}" stroke-width="3.5"/>`;const p=30+50*Math.exp(-32/tau);s+=`<circle cx="${X(32)}" cy="${Y(p)}" r="5" fill="${color}"/>`;s+=txt(X(32)+12,Y(p)+(tau===16?24:-12),p.toFixed(1)+'%',20,color);}
s+=rect(555,120,290,105,'#fff');s+=txt(575,151,'共同基线：30%',20)+txt(575,180,'可下降部分：50个百分点',20)+txt(575,209,'τ = 16 ms（蓝） / 32 ms（橙）',18);s+=txt(35,540,'两条曲线由 p(d) = 30 + 50 exp(−d/τ) 计算，无人群比较或显著性含义。',18);await writeFile(out+'/delay-model.svg',s+'</g></svg>');
s=start(500,'不同研究方法的证据范围');s+=txt(35,45,'方法不同，能回答的问题也不同',29)+txt(35,77,'阅读证据时，保留任务、对象与解释层次',19,'#66758a');
const rows=[['行为操纵','改变声音条件 → 比较任务表现','支持条件作用，不能独自定位脑区'],['跨任务相关','同一听者的不同指标相互联系','提示联系，不证明唯一因果链'],['神经记录','观察响应与声音、行为的关系','响应变化不自动等于识别改善'],['可逆干预','改变局部功能，再看反应与恢复','支持功能依赖，仍需网络与基线对照'],['临床比较','疾病或手术背景下比较表现','需要控制可听度和其他背景差异']];
rows.forEach((a,i)=>{const y=100+i*72;s+=rect(35,y,890,63);s+=txt(53,y+39,a[0],22,'#315bc6')+txt(225,y+25,a[1],19)+txt(225,y+50,a[2],18,'#66758a');});s+=txt(35,482,'这是方法阅读图，不是把研究排成统一的证据强弱分数。',19);await writeFile(out+'/evidence-levels.svg',s+'</g></svg>');
console.log({figures:3,exampleAt32ms:{tau16:30+50*Math.exp(-2),tau32:30+50*Math.exp(-1)}});
