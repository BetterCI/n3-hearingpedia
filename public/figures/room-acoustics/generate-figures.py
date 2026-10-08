from pathlib import Path
import json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','svg.fonttype':'path','font.size':10,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B='#285f83';O='#b9613b';G='#65727b';T='#347b70'
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight',dpi=160);plt.close(fig)
 p=ROOT/(name+'.svg');p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def arrow(ax,a,b,color):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':color,'lw':1.5})
# 图 1：平面镜像路径与同一几何条件下的到达时刻。
source=np.array([1.,1.]);receiver=np.array([6.,3.]);mirror=np.array([1.,-1.]);fraction=-mirror[1]/(receiver[1]-mirror[1]);reflection=mirror+fraction*(receiver-mirror)
direct=np.linalg.norm(receiver-source);reflected=np.linalg.norm(receiver-mirror);times=np.array([direct,reflected])/343*1000
fig,axs=plt.subplots(1,2,figsize=(10,4.3),layout='constrained');ax=axs[0];ax.add_patch(Rectangle((0,0),8,5,fill=False,edgecolor=G,lw=1.3));ax.scatter(*source,color=B);ax.scatter(*receiver,color=O);ax.text(*source+np.array([-.6,.3]),'声源');ax.text(*receiver+np.array([.15,.25]),'接收点')
arrow(ax,source,receiver,B);arrow(ax,source,reflection,T);arrow(ax,reflection,receiver,T);ax.scatter(*reflection,color=T,s=15);ax.text(3.7,2.5,'直达路径',color=B);ax.text(4,.45,'一次反射路径',color=T);ax.set(xlim=(-.3,8.3),ylim=(-.3,5.5),aspect='equal',xlabel='长度方向（m）',ylabel='宽度方向（m）')
ax=axs[1];ax.vlines(times,0,[1,.7],colors=[B,T],lw=2);ax.scatter(times,[1,.7],color=[B,T]);ax.text(times[0]-.3,1.06,'直达声',ha='right',color=B);ax.text(times[1]+.3,.77,'一次反射',ha='left',color=T);ax.set(xlim=(0,35),ylim=(0,1.22),xlabel='从发声时刻起的时间（ms）',ylabel='示意相对脉冲幅度');ax.text(2,.2,f'额外延迟 {times[1]-times[0]:.2f} ms',fontsize=10)
save(fig,'01-propagation-paths')
# 图 2：同一直接峰值下的合成脉冲响应；右图独立展示理想指数能量衰减。
fs=12000;t=np.arange(int(fs*1.6))/fs;rng=np.random.default_rng(20261009);carrier=rng.normal(size=t.size);carrier/=np.max(abs(carrier))
responses=[]
for rt in [.4,1.]:
 h=.22*carrier*np.exp(-np.log(1000)*t/rt);h[t<.03]=0
 for delay,amp in [(0,1),(.012,.45),(.025,-.3)]:h[round(delay*fs)]+=amp
 responses.append(h)
fig,axs=plt.subplots(2,2,figsize=(10,5.8),layout='constrained')
for row,(rt,h) in enumerate(zip([.4,1.],responses)):
 ax=axs[row,0];ax.plot(t,h,color=B if row==0 else O,lw=.6);ax.set(xlim=(-.01,1.2),ylim=(-1.05,1.05),xlabel='相对直达声到达的时间（s）',ylabel='相对幅度',title=f'合成响应：尾声衰减参数 {rt:.1f} s')
 ax=axs[row,1];ax.plot(t,-60*t/rt,color=B if row==0 else O,lw=2);ax.axhspan(-25,-5,color='#dce8ec',alpha=.7);ax.axhspan(-35,-25,color='#eadcd4',alpha=.6);ax.axhline(-60,color=G,lw=.7,ls=':');ax.set(xlim=(0,1.2),ylim=(-70,2),xlabel='衰减时间（s）',ylabel='归一化能量衰减级（dB）',title=f'独立理想曲线：60 dB 衰减用时 {rt:.1f} s');ax.text(.84,-14,'T20 拟合范围',fontsize=8);ax.text(.84,-31,'T30 追加范围',fontsize=8)
save(fig,'02-impulse-decay')
# 图 3：刚性矩形房间三个水平截面的有符号声压，不是声级或能量图。
L=np.array([5.,4.,2.8]);x=np.linspace(0,L[0],201);y=np.linspace(0,L[1],161);xx,yy=np.meshgrid(x,y);modes=[(1,0,0),(0,1,0),(1,1,0)];freqs=[]
fig,axs=plt.subplots(1,3,figsize=(10,3.8),layout='constrained')
for ax,n in zip(axs,modes):
 f=343/2*np.linalg.norm(np.array(n)/L);freqs.append(f);p=np.cos(n[0]*np.pi*xx/L[0])*np.cos(n[1]*np.pi*yy/L[1]);im=ax.imshow(p,origin='lower',extent=(0,L[0],0,L[1]),cmap='RdBu_r',vmin=-1,vmax=1,interpolation='nearest',aspect='equal');ax.contour(xx,yy,p,levels=[0],colors=[G],linewidths=.8);ax.set(aspect='equal',xlabel='x（m）',ylabel='y（m）',title=f'模态 {n}：{f:.1f} Hz')
fig.colorbar(im,ax=axs,shrink=.8,label='归一化瞬时声压（有正负）');save(fig,'03-room-modes')
# 图 4：同频不同阻尼的衰减与谐振器响应，峰值独立归一化以隔离衰减时间。
f0=63.;tt=np.linspace(0,1.2,15000);ff=np.linspace(45,81,1500);fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
for rt,color in [(.3,B),(.9,O)]:
 a=np.log(1000)/rt;sig=np.exp(-a*tt)*np.cos(2*np.pi*f0*tt);axs[0].plot(tt,sig,color=color,lw=.6,label=f'60 dB 衰减用时 {rt:.1f} s');response=1/np.sqrt(((2*np.pi*f0)**2-(2*np.pi*ff)**2)**2+(2*a*2*np.pi*ff)**2);response/=max(response);axs[1].plot(ff,20*np.log10(response),color=color,lw=1.8,label=f'阻尼参数对应 {rt:.1f} s')
axs[0].set(xlim=(-.01,1.2),ylim=(-1.05,1.05),xlabel='时间（s）',ylabel='归一化声压幅度');axs[1].set(xlim=(45,81),ylim=(-30,1),xlabel='频率（Hz）',ylabel='响应幅度级（dB，各曲线峰值归一化）')
for ax in axs:ax.legend(fontsize=8,loc='upper right')
save(fig,'04-modal-decay')
# 图 5：只含自由场直达声的教室距离例，不作为真实房间总声级预测。
fig,axs=plt.subplots(1,2,figsize=(10,4.7),layout='constrained');ax=axs[0];ax.add_patch(Rectangle((0,0),11,7,fill=False,edgecolor=G));src=np.array([1.,3.5]);ax.scatter(*src,color=O,marker='*',s=160);ax.text(.2,4.1,'教师位置',fontsize=9)
seats=np.array([(a,b) for a in [2.5,4.5,6.5,8.5,10] for b in [1.5,3.5,5.5]]);distances=np.linalg.norm(seats-src,axis=1);snr=60-20*np.log10(distances)-45;im=ax.scatter(seats[:,0],seats[:,1],c=snr,cmap='viridis',s=100,vmin=-5,vmax=15);fig.colorbar(im,ax=ax,shrink=.7,label='仅直达声的示意信噪比（dB）');ax.set(xlim=(-.3,11.3),ylim=(-.3,7.3),aspect='equal',xlabel='长度（m）',ylabel='宽度（m）')
ax=axs[1];r=np.linspace(1,10,200);levels=60-20*np.log10(r);ax.plot(r,levels,color=B,lw=2,label='自由场直达声示例');ax.axhline(45,color=O,ls='--',label='假设空间均匀背景噪声');ax.set(xlim=(1,10),ylim=(35,65),xlabel='声源—接收点距离（m）',ylabel='示意 A 计权声级（dB）');ax.legend(fontsize=8);ax.text(1.3,36.8,'未计反射、指向性、遮挡及设备处理',fontsize=8)
save(fig,'05-classroom-distance')
assert np.all(np.abs(responses)<=1);assert reflected>direct
assert np.allclose(freqs,[34.3,42.875,54.90679033598668],rtol=1e-10)
report={'figures':5,'data':'原创几何与数学演示；非实测房间或人类行为数据','soundSpeedMps':343,'pathArrivalMs':times.tolist(),'reflectionExtraDelayMs':float(times[1]-times[0]),'roomDimensionsM':L.tolist(),'modeFrequenciesHz':freqs,'relativeWaveformsWithinPlusMinusOne':True,'decayConventions':'声压幅度 exp(-ln(1000)t/T)；能量级 -60t/T','classroomExample':'1 m 直达声60 dBA；均匀噪声45 dBA；不含反射','seed':20261009}
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
