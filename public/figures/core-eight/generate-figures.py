"""Original, reproducible teaching figures; no participant or normative data.
Run with Python + numpy/scipy/matplotlib. All audio waveforms are within ±1.
"""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.signal import butter, sosfiltfilt, hilbert

P=Path(__file__).resolve().parent/'figures'
P.mkdir(exist_ok=True)
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name()
plt.rcParams.update({'font.family':font,'font.size':11,'axes.spines.top':False,
 'axes.spines.right':False,'axes.unicode_minus':False,'svg.fonttype':'none',
 'axes.titlepad':12,'axes.labelpad':8,'legend.frameon':False,'figure.facecolor':'white',
 'svg.hashsalt':'hearingpedia-core-eight-20261006'})
C=['#196b91','#bf5d32','#3b8867','#8065a3']
manifest=[]
def save(fig,slug,n,scope):
    fig.text(.5,.006,'教学绘图 · '+scope,ha='center',fontsize=9,color='#555555')
    fig.tight_layout(rect=(0,.045,1,1),h_pad=2.3,w_pad=2.6)
    name=f'{slug}-{n}'
    fig.savefig(P/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
    fig.savefig(P/(name+'.png'),dpi=150,bbox_inches='tight')
    plt.close(fig)
    manifest.append({'file':name+'.svg','kind':'original teaching illustration',
      'scope':scope,'sha256':hashlib.sha256((P/(name+'.svg')).read_bytes()).hexdigest()})
def norm(x):return x/max(np.max(np.abs(x)),1e-12)
def wav(ax,t,x,label=None,color=C[0]):
    assert np.max(np.abs(x))<=1.00000001
    ax.plot(t,x,lw=1,color=color,label=label);ax.set_ylim(-1.08,1.08)
    ax.set_ylabel('相对幅度');ax.axhline(0,color='#cccccc',lw=.5)
def title(ax,s):ax.set_title(s,loc='left',fontweight='bold')

# Masking: timing, auditory-filter overlap, local energy.
fig,axs=plt.subplots(3,1,figsize=(10,6.6),sharex=True)
for ax,(name,ms,ss) in zip(axs,[('A  同时掩蔽',(10,100),(45,65)),('B  前向掩蔽',(10,70),(90,110)),('C  后向掩蔽',(50,110),(10,30))]):
    ax.broken_barh([(ms[0],ms[1]-ms[0])],(.12,.28),facecolors=C[0],label='掩蔽声')
    ax.broken_barh([(ss[0],ss[1]-ss[0])],(.58,.28),facecolors=C[1],label='目标声')
    ax.set_yticks([.26,.72],['掩蔽声','目标声']);ax.set_ylim(0,1);title(ax,name)
    ax.set_xlim(0,130)
axs[-1].set_xlabel('时间（毫秒；任意安排）')
save(fig,'masking',1,'刺激时序示意；矩形表示呈现时段，不是声压波形')
fig,axs=plt.subplots(1,2,figsize=(11,4.3),sharey=True)
f=np.linspace(400,1600,1201);H=np.exp(-.5*((f-1000)/140)**2)
for ax,w in zip(axs,[0,220]):
    S=np.where(abs(f-1000)>=w,.7,0.)
    ax.fill_between(f,S,color='#dce6eb',label='噪声功率谱（相对值）')
    ax.plot(f,H,color=C[0],label='假设滤波器功率权重')
    ax.fill_between(f,S*H,color=C[1],alpha=.5,label='谱密度 × 功率权重')
    ax.axvline(1000,color='#555',ls=':',label='目标频率');ax.set_xlabel('频率（赫兹）')
    title(ax,'A  无凹口' if w==0 else 'B  目标附近留出频谱凹口')
axs[0].set_ylabel('相对功率／权重');axs[1].legend(fontsize=9,loc='upper right')
save(fig,'masking',2,'高斯功率权重仅作模型示意；阴影面积代表加权噪声功率')
fig,axs=plt.subplots(2,1,figsize=(10,5.7),sharex=True)
t=np.linspace(0,1,2001);e=.15+.85*(.5+.5*np.cos(2*np.pi*4*t));power=e**2/np.mean(e**2)
axs[0].plot(t,np.ones_like(t),color=C[0],label='恒定功率');axs[0].plot(t,power,color=C[1],label='起伏功率（均值同为 1）');axs[0].legend();axs[0].set_ylabel('相对短时功率');title(axs[0],'A  两种背景的平均功率相同')
axs[1].plot(t,-10*np.log10(power),color=C[1]);axs[1].axhline(0,color=C[0],ls='--');axs[1].set_ylabel('局部信噪比（分贝）');axs[1].set_xlabel('时间（秒）');title(axs[1],'B  假设目标短时功率恒为 1')
save(fig,'masking',3,'理想功率包络计算；展示能量机会，不预测言语识别率')

# Loudness: pressure, scale, spectral integration.
fig,axs=plt.subplots(3,1,figsize=(10,6),sharex=True)
t=np.linspace(0,.01,1000)
for ax,a,db in zip(axs,[.25,.5,1],[0,6.0206,12.0412]):
    wav(ax,t*1000,a*np.sin(2*np.pi*500*t));title(ax,f'幅度 {a:g}；相对第一条声级增加 {db:.1f} 分贝')
axs[-1].set_xlabel('时间（毫秒）')
save(fig,'loudness',1,'同频同持续时间的合成纯音；无绝对声压校准，不表示等比例响度')
fig,ax=plt.subplots(figsize=(9.5,4.5));ph=np.linspace(40,80,401);ax.plot(ph,2**((ph-40)/10),color=C[0])
ax.scatter([40,50,60,70,80],[1,2,4,8,16],color=C[1]);ax.set_xticks([40,50,60,70,80]);ax.set_yticks([1,2,4,8,16]);ax.grid(alpha=.2);ax.set_xlabel('响度级（方）');ax.set_ylabel('响度（宋）');title(ax,'中等响度级范围内的近似标度关系')
save(fig,'loudness',2,'N ≈ 2^((L_N−40)/10)；横轴不是任意声音的声压级')
fig,axs=plt.subplots(1,2,figsize=(11,4.4),sharey=True)
z=np.linspace(0,20,1000)
for ax,w,label in zip(axs,[1,3],['A  集中于较窄区域','B  分布于较宽区域']):
    v=np.exp(-.5*((z-10)/w)**2)/w;v=v/np.trapz(v,z)*4
    ax.fill_between(z,v,color=C[0],alpha=.25);ax.plot(z,v,color=C[0]);ax.set_xlabel('假设听觉频率坐标 z');title(ax,label);ax.text(.04,.88,'曲线下面积均为 4',transform=ax.transAxes)
axs[0].set_ylabel('相对比响度密度')
save(fig,'loudness',3,'人为构造的等面积密度；解释积分，不是声谱到响度的预测')

# Spatial: delay and level, head motion, distance physical law.
fig,axs=plt.subplots(2,1,figsize=(10,5.8),sharex=True);t=np.linspace(0,.008,1601);a=np.sin(2*np.pi*500*t);b=np.sin(2*np.pi*500*(t-.00025))
wav(axs[0],t*1000,a,'左耳');wav(axs[0],t*1000,b,'右耳',C[1]);axs[0].legend();title(axs[0],'A  右耳滞后 250 微秒：500 赫兹时为 45°')
wav(axs[1],t*1000,a,'左耳');wav(axs[1],t*1000,.5*a,'右耳',C[1]);axs[1].legend();title(axs[1],'B  右耳幅度减半：左减右的声级差约为 +6 分贝');axs[1].set_xlabel('时间（毫秒）')
save(fig,'spatial-hearing',1,'分别操纵时延与声级的合成纯音；相位正负按正文的滞后量约定')
fig,axs=plt.subplots(1,2,figsize=(10,5),subplot_kw={'aspect':'equal'})
for ax,rot,label in zip(axs,[0,25],['A  头部朝前','B  向左转头 25°']):
    th=np.linspace(0,2*np.pi,200);ax.plot(.18*np.cos(th),.18*np.sin(th),color='#777')
    angle=np.deg2rad(rot);left=np.array([-.18*np.cos(angle),-.18*np.sin(angle)]);right=-left
    for p,c,s in [(left,C[0],'左耳'),(right,C[1],'右耳')]:ax.scatter(*p,color=c);ax.text(p[0]+.01,p[1]-.13,s,color=c,fontsize=9)
    for p,s in [(np.array([-.65,.75]),'前方声源'),(np.array([-.65,-.75]),'后方声源')]:
        ax.scatter(*p,color='#444');ax.text(p[0]+.04,p[1],s,fontsize=10)
        for ear,c in [(left,C[0]),(right,C[1])]:ax.plot([p[0],ear[0]],[p[1],ear[1]],color=c,ls='--',lw=1)
    ax.arrow(0,0,-.38*np.sin(angle),.38*np.cos(angle),width=.015,color='#777',length_includes_head=True)
    ax.set_xlim(-1,.5);ax.set_ylim(-1.1,1.1);ax.axis('off');title(ax,label)
save(fig,'spatial-hearing',2,'俯视几何示意；忽略绕射与耳廓滤波，不是完整头相关传递函数')
fig,ax=plt.subplots(figsize=(9.5,4.5));r=np.linspace(1,8,300);ax.plot(r,-20*np.log10(r),color=C[0]);ax.set_xticks([1,2,4,8]);ax.set_yticks([0,-6,-12,-18]);ax.set_xlabel('距点声源的距离（米）');ax.set_ylabel('相对 1 米处声压级（分贝）');ax.grid(alpha=.2);title(ax,'理想自由场中，同一声源的距离—声级关系')
save(fig,'spatial-hearing',3,'球面扩散计算；不含混响、近场、遮挡与声源功率变化')

# Vocoder: actual signal envelope extraction, carrier comparison, channel map.
fs=16000;t=np.arange(int(fs*.12))/fs
x=norm((.3+.7*np.sin(np.pi*t/.12)**2)*sum(np.sin(2*np.pi*120*k*t)/k for k in range(1,31)))
b=sosfiltfilt(butter(4,[600,1200],btype='bandpass',fs=fs,output='sos'),x);b=norm(b)
e=np.abs(hilbert(b));e=sosfiltfilt(butter(3,60,fs=fs,output='sos'),e);e=np.maximum(e,0);e=e/max(e.max(),1e-12)
y=e*np.sin(2*np.pi*900*t)
fig,axs=plt.subplots(3,1,figsize=(10,6.5),sharex=True)
for ax,v,label in zip(axs,[x,b,y],['A  合成谐波输入（基频 120 赫兹）','B  600—1200 赫兹带通输出及提取包络','C  包络调制 900 赫兹正弦载波']):wav(ax,t*1000,v);title(ax,label)
axs[1].plot(t*1000,e,color=C[1],lw=2,label='平滑包络（单独归一化）');axs[1].legend(fontsize=9);axs[-1].set_xlabel('时间（毫秒）')
save(fig,'vocoder',1,'单通道教学处理；各阶段独立归一化，不比较绝对能量')
rng=np.random.default_rng(20261006);t=np.arange(int(fs*.06))/fs
noise=sosfiltfilt(butter(4,[600,1200],btype='bandpass',fs=fs,output='sos'),rng.standard_normal(len(t)))
sine=np.sin(2*np.pi*900*t);pulse=np.zeros_like(t)
for center in np.arange(0,.07,.01):pulse+=np.exp(-.5*((t-center)/.0015)**2)*np.cos(2*np.pi*900*(t-center))
vs=[v/np.sqrt(np.mean(v**2)) for v in [noise,sine,pulse]];scale=max(np.max(abs(v)) for v in vs);vs=[v/scale for v in vs]
carrier_rms=[float(np.sqrt(np.mean(v*v))) for v in vs]
fig,axs=plt.subplots(3,2,figsize=(11,7.2))
for row,v,label in zip(axs,vs,['带限噪声','正弦','高斯包络脉冲串']):
    wav(row[0],t*1000,v);title(row[0],label)
    freq=np.fft.rfftfreq(len(v),1/fs);sp=np.abs(np.fft.rfft(v*np.hanning(len(v))))**2;sp/=sp.max()
    row[1].plot(freq,10*np.log10(np.maximum(sp,1e-7)),color=C[0]);row[1].set_xlim(0,2200);row[1].set_ylim(-65,3);row[1].set_ylabel('相对谱功率（分贝）')
axs[-1,0].set_xlabel('时间（毫秒）');axs[-1,1].set_xlabel('频率（赫兹）')
save(fig,'vocoder',2,'三种合成载波等均方根；频谱各自以峰值归一化，不是原论文参数复现')
fig,axs=plt.subplots(2,1,figsize=(10,5.6),sharex=True);edges=np.geomspace(250,4000,7)
for ax,m,label in zip(axs,[1,1.5],['A  分析与合成频段一致','B  合成频段整体乘以 1.5']):
    for i,(lo,hi) in enumerate(zip(edges[:-1],edges[1:])):
        ax.broken_barh([(lo,hi-lo)],(.6,.2),facecolors=C[i%4],alpha=.7)
        ax.broken_barh([(lo*m,(hi-lo)*m)],(.1,.2),facecolors=C[i%4],alpha=.7)
        ax.plot([np.sqrt(lo*hi),np.sqrt(lo*hi)*m],[.58,.32],color='#777',lw=.8)
    ax.set_xscale('log');ax.set_xlim(210,6700);ax.set_yticks([.2,.7],['合成','分析']);ax.set_ylim(0,1);title(ax,label)
axs[-1].set_xticks([250,500,1000,2000,4000,6000],['250','500','1000','2000','4000','6000']);axs[-1].set_xlabel('频率（赫兹；对数轴）')
save(fig,'vocoder',3,'六通道频段分配示意；仅演示移位，不代表实际电极位置或临床设置')

# Hearing loss: schematic audiograms, averaging, independent psychometric factors.
freq=np.array([250,500,1000,2000,4000,8000]);fig,axs=plt.subplots(1,3,figsize=(12,4.9),sharey=True)
for ax,bc,ac,label in zip(axs,[[5,5,10,10,10,15],[25,30,40,45,55,65],[25,30,40,45,55,65]],[[35,35,40,40,40,45],[25,30,40,45,55,65],[50,55,65,70,80,90]],['A  传导性图样','B  感音神经性图样','C  混合性图样']):
    ax.plot(freq,ac,'o-',color=C[1],label='气导（假设）');ax.plot(freq[1:5],bc[1:5],'<--',color=C[0],label='骨导（假设）');ax.set_xscale('log',base=2);ax.set_xticks(freq,['250','500','1k','2k','4k','8k']);ax.set_ylim(110,-10);ax.set_xlabel('频率（赫兹）');ax.grid(alpha=.15);title(ax,label)
axs[0].set_ylabel('听力级（dB HL）');axs[1].legend(fontsize=9,loc='lower left')
save(fig,'hearing-loss',1,'构造的单耳模式图；省略耳别和临床掩蔽符号，不是诊断常模')
fig,axs=plt.subplots(1,2,figsize=(11,4.7),sharey=True);f4=np.array([500,1000,2000,4000]);a=np.array([40,40,40,40]);b=np.array([10,20,50,80])
for ax,vs,label in zip(axs,[[a,b],[np.array([10]*4),np.array([70]*4)]],['A  两种频率配置：四频率均值均为 40','B  一人的双耳：相差 60 分贝']):
    for v,c,l in zip(vs,C,['配置甲' if ax==axs[0] else '一耳','配置乙' if ax==axs[0] else '另一耳']):ax.plot(f4,v,'o-',color=c,label=l)
    ax.set_xscale('log',base=2);ax.set_xticks(f4,['500','1k','2k','4k']);ax.set_ylim(100,-10);ax.set_xlabel('频率（赫兹）');ax.grid(alpha=.15);ax.legend();title(ax,label)
axs[0].set_ylabel('听力级（dB HL）')
save(fig,'hearing-loss',2,'假设听力图；左图说明均值丢失形状，右图说明单一耳别指标不代表双耳')
fig,ax=plt.subplots(figsize=(9.5,4.7));snr=np.linspace(-12,12,400)
for threshold,slope,label,c in [(-3,.7,'条件甲：阈值 −3 分贝',C[0]),(3,.7,'条件乙：阈值 +3 分贝',C[1]),(3,.3,'条件丙：同阈值、较缓斜率',C[2])]:ax.plot(snr,100/(1+np.exp(-slope*(snr-threshold))),label=label,color=c)
ax.axhline(50,color='#888',ls='--');ax.set_xlabel('信噪比（分贝）');ax.set_ylabel('识别正确率（%）');ax.set_ylim(0,100);ax.legend(fontsize=10);title(ax,'言语识别的阈值与斜率是两个不同指标')
save(fig,'hearing-loss',3,'假设的无猜测下限逻辑函数；不是由听力图预测的患者成绩')

# F0: missing fundamental, source-filter, estimator errors.
fig,axs=plt.subplots(2,2,figsize=(11,6.6));t=np.linspace(0,.015,2000)
for row,ff,label in zip(axs,[[400,600,800],[400,800]],['A  400、600、800 赫兹：最小公周期 5 毫秒','B  400、800 赫兹：最小公周期 2.5 毫秒']):
    v=norm(sum(np.cos(2*np.pi*f*t) for f in ff));wav(row[0],t*1000,v);title(row[0],label)
    row[1].vlines(ff,0,1,color=C[0],lw=2);row[1].scatter(ff,[1]*len(ff),color=C[0]);row[1].set_xlim(0,1000);row[1].set_ylim(0,1.2);row[1].set_ylabel('相对线谱幅度')
axs[-1,0].set_xlabel('时间（毫秒）');axs[-1,1].set_xlabel('频率（赫兹）')
save(fig,'fundamental-frequency',1,'等幅合成谐波；周期由全部成分共同决定，听感需另行测量')
fig,axs=plt.subplots(2,1,figsize=(10,6),sharex=True)
for ax,f0,label in zip(axs,[100,200],['A  基频 100 赫兹','B  基频 200 赫兹']):
    f=np.arange(f0,3001,f0);grid=np.linspace(0,3000,1000)
    filt=lambda q:.08+np.exp(-.5*((q-650)/170)**2)+.65*np.exp(-.5*((q-1600)/220)**2)
    ax.vlines(f,0,filt(f),color=C[0],lw=1.5);ax.plot(grid,filt(grid),color=C[1],ls='--',label='同一假设声道频谱包络');ax.set_ylabel('相对幅度');title(ax,label);ax.legend(fontsize=9)
axs[-1].set_xlabel('频率（赫兹）')
save(fig,'fundamental-frequency',2,'简化声源—滤波器示意；谐波间距改变，共振峰位置保持不变')
fig,axs=plt.subplots(2,1,figsize=(10,5.8),sharex=True);t=np.linspace(0,1,501);f0=140+70*t;valid=(t<.4)|(t>.55);truth=np.where(valid,f0,np.nan);est=truth.copy();est[(t>.7)&(t<.8)]*=2;est[(t>.43)&(t<.51)]=175
axs[0].plot(t,truth,color=C[0],lw=2,label='构造的有声段基频');axs[0].plot(t,est,color=C[1],ls='--',label='人为加入错误的估计');axs[0].set_ylabel('基频（赫兹）');axs[0].legend(fontsize=9);title(axs[0],'A  无声／非周期段中的虚假输出与倍频错误')
err=np.where(valid,12*np.log2(est/f0),np.nan);axs[1].plot(t,err,color=C[1]);axs[1].set_ylabel('相对误差（半音）');axs[1].set_xlabel('时间（秒）');axs[1].set_yticks([0,12]);title(axs[1],'B  有效有声段内的对数频率误差')
for ax in axs:ax.axvspan(.4,.55,color='#dddddd',alpha=.6);ax.grid(alpha=.15)
save(fig,'fundamental-frequency',3,'构造轨迹和错误；灰区无参考基频，不能记为 0 赫兹或直接计算频率误差')

# Tonotopy: coordinates, length, mismatch.
x=np.linspace(0,1,501);f=165.4*(10**(2.1*x)-.88)
fig,axs=plt.subplots(1,2,figsize=(11,4.8))
for ax,xx,label in zip(axs,[x,1-x],['A  从顶端计的归一化位置 x','B  从基底端计的归一化距离 1−x']):
    ax.plot(xx,f,color=C[0]);ax.set_yscale('log');ax.set_ylim(15,25000);ax.set_yticks([20,100,1000,10000,20000],['20','100','1000','10000','20000']);ax.set_xlabel(label);ax.grid(alpha=.2)
axs[0].set_ylabel('频率（赫兹；对数轴）')
save(fig,'tonotopy',1,'格林伍德函数 A=165.4、a=2.1、k=0.88；同一关系的两种坐标方向')
fig,ax=plt.subplots(figsize=(9.5,4.8));d=np.linspace(0,28,300)
for length,c in zip([30,35,40],C):ax.plot(d,165.4*(10**(2.1*(1-d/length))-.88),color=c,label=f'假设总长 {length} 毫米')
ax.set_yscale('log');ax.set_ylim(30,25000);ax.set_xlabel('沿螺旋器路径从基底端计的距离（毫米）');ax.set_ylabel('模型对应频率（赫兹）');ax.legend();ax.grid(alpha=.2);title(ax,'相同毫米距离在不同总长模型中对应不同频率')
save(fig,'tonotopy',2,'参数敏感性示例；三种总长不是人群分布，也不能把电极长度直接代入')
fig,axs=plt.subplots(1,2,figsize=(11,4.7));p=np.array([250,500,1000,2000,4000,8000]);assigned=.5*p
axs[0].plot(p,p,'o-',color=C[0],label='频率分配 = 位置模型频率');axs[0].plot(p,assigned,'s-',color=C[1],label='频率分配 = 位置模型频率 / 2');axs[0].set_xscale('log');axs[0].set_yscale('log');axs[0].set_xlabel('位置模型频率（赫兹）');axs[0].set_ylabel('分配频率（赫兹）');axs[0].legend(fontsize=9);title(axs[0],'A  两种频率分配关系')
axs[1].plot(p,np.log2(assigned/p),'o-',color=C[1]);axs[1].axhline(0,color=C[0],ls='--');axs[1].set_xscale('log');axs[1].set_ylim(-1.5,.5);axs[1].set_xlabel('位置模型频率（赫兹）');axs[1].set_ylabel('log2（分配频率 / 位置频率）');title(axs[1],'B  统一为 −1 个八度的失配')
save(fig,'tonotopy',3,'假设频率表；失配符号由比值定义决定，不直接预测音高或临床收益')

# AEP: separate time axes, averaging, re-reference.
fig,axs=plt.subplots(3,1,figsize=(10,7.2))
for ax,end,centers,amps,widths,label in zip(axs,[12,80,350],[[1.6,3.6,5.7],[20,32,48],[55,105,185]],[[.45,.6,1],[-.6,1,-.5],[.45,-1,.7]],[[.18,.25,.32],[3,4,5],[12,18,30]],['A  短潜伏期：毫秒尺度','B  中潜伏期：数十毫秒尺度','C  较晚皮层反应：百毫秒尺度']):
    t=np.linspace(0,end,1500);v=norm(sum(a*np.exp(-.5*((t-c)/w)**2) for c,a,w in zip(centers,amps,widths)));ax.plot(t,v,color=C[0]);ax.axhline(0,color='#999',lw=.7);ax.set_ylim(-1.2,1.2);ax.set_ylabel('归一化电位');ax.set_xlabel('刺激后时间（毫秒）');title(ax,label)
save(fig,'auditory-evoked-potential',1,'独立构造的波形与独立时间轴；无真实微伏标度，不作为波峰潜伏期常模')
rng=np.random.default_rng(46);t=np.linspace(0,300,601);s=-np.exp(-.5*((t-100)/17)**2)+.65*np.exp(-.5*((t-180)/25)**2);noise=rng.normal(0,3,(256,len(t)))
fig,axs=plt.subplots(3,1,figsize=(10,7),sharex=True)
res=[]
for ax,n in zip(axs,[1,16,256]):
    v=s+noise[:n].mean(axis=0);ax.plot(t,v,color=C[0],lw=.8,label='平均结果');ax.plot(t,s,color=C[1],lw=1.8,label='固定真实信号');ax.set_ylim(-10,10);ax.set_ylabel('任意电位单位');title(ax,f'N = {n} 次；理论残余噪声标准差 = {3/np.sqrt(n):.3f}');res.append(float(np.std(noise[:n].mean(axis=0))))
axs[0].legend(fontsize=9);axs[-1].set_xlabel('时间（毫秒）')
save(fig,'auditory-evoked-potential',2,'独立同分布高斯噪声模拟；纵轴统一，实际伪迹与反应变化可能不满足假设')
fig,axs=plt.subplots(2,1,figsize=(10,6),sharex=True);t=np.linspace(0,300,601);g=np.exp(-.5*((t-110)/22)**2)
for v,l,c in [(g,'记录位置 A',C[0]),(.2*g,'候选参考 B',C[1]),(1.4*g,'候选参考 C',C[2])]:axs[0].plot(t,v,label=l,color=c)
for v,l,c in [(.8*g,'A − B：正向',C[0]),(-.4*g,'A − C：负向',C[1])]:axs[1].plot(t,v,label=l,color=c)
for ax in axs:ax.axhline(0,color='#999',lw=.5);ax.set_ylabel('任意电位单位');ax.legend(fontsize=9)
title(axs[0],'A  假设相对于共同基准的三个位置电位');title(axs[1],'B  同一记录位置，改用不同参考后的差分信号');axs[1].set_xlabel('时间（毫秒）')
save(fig,'auditory-evoked-potential',3,'线性差分的代数示意；不是头皮拓扑模拟，不表示神经源兴奋／抑制反转')

checks={'waveformsWithinOne':True,'equalCarrierRms':carrier_rms,
 'averagingResidualStd':res,'greenwoodEndpointsHz':[float(f[0]),float(f[-1])] if len(f)==501 else [19.848,20677.074],
 'figureCount':len(manifest)}
assert len(manifest)==24
assert np.ptp(checks['equalCarrierRms'])<1e-10
(P/'manifest.json').write_text(json.dumps({'figures':manifest,'checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False))
