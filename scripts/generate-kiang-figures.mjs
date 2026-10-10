import {mkdir,writeFile} from 'node:fs/promises';
const out='public/figures/nelson-kiang';await mkdir(out,{recursive:true});
const text=(x,y,s,n=20,c='#26334b')=>`<text x="${x}" y="${y}" font-size="${n}" fill="${c}">${s}</text>`;
const start=(h,title)=>`<svg xmlns="http://www.w3.org/2000/svg" width="960" height="${h}" viewBox="0 0 960 ${h}" role="img"><title>${title}</title><rect width="960" height="${h}" fill="white"/><g font-family="Microsoft YaHei,Noto Sans CJK SC,sans-serif">`;
const line=(x,y,X,Y,c='#cad3e1',w=1)=>`<path d="M${x} ${y}L${X} ${Y}" stroke="${c}" stroke-width="${w}" fill="none"/>`;
const trials=[[5,7,30,70],[6,8,32,72],[5,9,31,75],[7,10,33,77]];
let s=start(590,'同一组教学脉冲的栅格与PSTH');s+=text(35,42,'先对齐事件，再统计时间响应',30)+text(35,75,'本站假设数据｜4次重复，每次100 ms｜非历史实验记录',19,'#a55425');
const X=t=>125+t*7.6;
trials.forEach((a,i)=>{let y=118+i*40;s+=text(35,y+8,'重复 '+(i+1),19)+line(125,y,X(100),y);a.forEach(t=>s+=line(X(t),y-12,X(t),y+12,'#315bc6',2));});
s+=line(125,98,125,260,'#a55425',2)+text(126,283,'0',18)+text(X(100)-15,283,'100 ms',18);
s+=text(35,325,'10 ms分箱',22,'#315bc6')+text(525,325,'20 ms分箱',22,'#b36825');
for(const [bin,offset,color] of [[10,35,'#315bc6'],[20,525,'#b36825']]){const counts=Array(100/bin).fill(0);trials.flat().forEach(t=>counts[Math.floor(t/bin)]++);const rates=counts.map(c=>c/(4*bin/1000));const width=370/counts.length;const y=r=>495-r*.75;
 s+=line(offset+40,350,offset+40,495,'#52647b')+line(offset+40,495,offset+410,495,'#52647b');
 rates.forEach((rate,j)=>s+=`<rect x="${offset+41+j*width}" y="${y(rate)}" width="${width-2}" height="${495-y(rate)}" fill="${color}"/>`);
 s+=text(offset+42,345,'spikes/s',17)+text(offset+37,518,'0',17)+text(offset+360,518,'100 ms',17)+text(offset+85,375,'峰值 '+Math.max(...rates)+' spikes/s',18,color);
 console.log({bin,counts,rates});
}
s+=text(35,555,'分箱改变峰值显示；总脉冲数仍为16，整个窗口平均率为40 spikes/s。',20)+text(35,582,'统计单位：同一单元的重复试验，不是把4根不同纤维合并。',18);await writeFile(out+'/psth.svg',s+'</g></svg>');
s=start(490,'相同平均率与不同相位分布的教学示例');s+=text(35,42,'平均率相同，时序仍可不同',30)+text(35,75,'本站假设数据｜每组8个脉冲，观察窗100 ms｜非论文实测数据',19,'#a55425');
for(const [phases,cx,title,color] of [[[0,0,0,0,0,0,0,0],260,'固定相位：VS = 1','#315bc6'],[Array.from({length:8},(_,i)=>i*Math.PI/4),700,'均匀相位：VS = 0','#b36825']]){const cy=245,r=110;s+=`<circle cx="${cx}" cy="${cy}" r="${r}" fill="#f5f7fb" stroke="#cbd5e5"/>`;
 for(let i=0;i<8;i++){const p=i*Math.PI/4;s+=line(cx,cy,cx+r*Math.cos(p),cy-r*Math.sin(p));}
 phases.forEach((p,i)=>{const radius=phases.every(v=>v===0)?r-5-i*6:r;s+=`<circle cx="${cx+radius*Math.cos(p)}" cy="${cy-radius*Math.sin(p)}" r="5" fill="${color}"/>`;});
 s+=text(cx-135,390,title,23,color)+text(cx-120,420,'平均率都为80 spikes/s',20);}
s+=text(35,464,'圆周表示刺激相位；固定相位的圆点沿半径错开，仅为避免重叠。',19);await writeFile(out+'/rate-and-timing.svg',s+'</g></svg>');
s=start(510,'神经编码研究的三种问题');s+=text(35,42,'从脉冲记录到听觉解释',30)+text(35,75,'本站原创阅读图｜三种问题需要不同证据',19,'#66758a');
const rows=[['记录中有什么？','调谐曲线、平均率、放电时序','单纤维生理数据；明确刺激与记录部位'],['这些线索能做什么？','区分频率、共振峰或时间变化','分析或解码模型；说明可用信息及假设'],['听者实际用了什么？','听觉任务、阈值与错误模式','行为检验及有针对性的操纵']];
rows.forEach((a,i)=>{const y=108+i*110;s+=`<rect x="35" y="${y}" width="890" height="96" rx="14" fill="#f5f7fb" stroke="#d8e1ed"/>`;s+=text(53,y+38,a[0],24,'#315bc6')+text(320,y+35,a[1],21)+text(320,y+70,a[2],19,'#66758a');});s+=text(35,475,'神经响应里存在可解码线索，不自动证明人脑采用了同一种解码方式。',20);await writeFile(out+'/coding-evidence.svg',s+'</g></svg>');

