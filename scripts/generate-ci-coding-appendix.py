"""Original numerical teaching illustrations, not clinical device simulations."""
from pathlib import Path
import importlib.util
import json
import numpy as np
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/ci-coding'
OUT.mkdir(parents=True, exist_ok=True)
spec = importlib.util.spec_from_file_location('encoder', ROOT / 'public/code/ci-coding/teaching_encoder.py')
enc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(enc)
t, x, bands, env, edges, cis, ace = enc.demo()
enc.verify(cis, ace)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':11,
    'svg.fonttype':'path','svg.hashsalt':'ci-coding-appendix',
    'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
P,G,O,GRAY = '#7454a2','#227d83','#be6536','#c8c2d1'
names=[]

def save(fig,name):
    for ext in ('svg','png'):
        fig.savefig(OUT/(name+'.'+ext),facecolor='white',dpi=145,
                    metadata={'Date':None} if ext=='svg' else None)
    plt.close(fig)
    svg = OUT / (name + '.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines()) + '\n', encoding='utf-8')
    names.append(name)

def grid(ax):
    ax.grid(alpha=.18)
    ax.set_axisbelow(True)

# A: actual matrix slice and event rows, linked by selection time.
fig,axs=plt.subplots(1,2,figsize=(12,5.3),layout='constrained')
j=36; n=int(j*enc.FS/enc.RATE)
sl=env[:,n-10:n+11]
im=axs[0].imshow(sl,origin='lower',aspect='auto',cmap='viridis',extent=[n-10.5,n+10.5,-.5,7.5])
fig.colorbar(im,ax=axs[0],label='包络相对幅度',shrink=.8,pad=.02)
axs[0].axvline(n,color='white',ls='--',lw=2)
axs[0].set(xlabel='声音样本索引 n',ylabel='代码通道索引（0–7）',yticks=range(8),
    title=f'（a）包络数组 (8, 2880) 的局部切片\n第 j={j} 轮读取第 n={n} 列')
ev=ace[j*4:(j+1)*4]
rows=[[f'{r[0]*1000:.3f}',str(int(r[1])),f'{r[2]:.3f}'] for r in ev]
axs[1].axis('off')
tab=axs[1].table(cellText=rows,colLabels=['起点（ms）','通道索引','相对幅度'],loc='center',cellLoc='center')
tab.auto_set_font_size(False);tab.set_fontsize(12);tab.scale(1,2.2)
axs[1].set_title('（b）同一轮生成 4 行 ACE 候选事件\n图中电极标签 = 代码通道索引 + 1')
axs[1].text(.5,.08,'一列包络 → 选通道 → 多行事件\n矩阵列号与事件行号不是同一个索引',transform=axs[1].transAxes,ha='center',color=P)
save(fig,'05-array-to-events')

# B: actual frequency response, plus causal state preservation example.
fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
f=np.geomspace(100,9000,1800)
for i,(lo,hi) in enumerate(zip(edges[:-1],edges[1:])):
    sos=signal.butter(3,[lo,hi],btype='bandpass',fs=enc.FS,output='sos')
    _,h=signal.sosfreqz(sos,worN=f,fs=enc.FS)
    axs[0].semilogx(f,20*np.log10(np.maximum(abs(h),1e-8)),label=f'E{i+1}')
axs[0].set(xlim=(120,8500),ylim=(-50,3),xlabel='频率（Hz，对数轴）',ylabel='幅度响应（dB）',title='（a）8 个教学带通：相同频率比，不同 Hz 带宽')
axs[0].set_xticks([200,500,1000,2000,6000],labels=['200','500','1000','2000','6000'])
axs[0].legend(ncol=4,fontsize=8);grid(axs[0])
sos=signal.butter(3,edges[1:3],btype='bandpass',fs=enc.FS,output='sos')
xx=.2*np.sin(2*np.pi*420*t); cut=995
whole=signal.sosfilt(sos,xx)
first,state=signal.sosfilt(sos,xx[:cut],zi=np.zeros((len(sos),2)))
second,_=signal.sosfilt(sos,xx[cut:],zi=state)
kept=np.r_[first,second]
reset=np.r_[first,signal.sosfilt(sos,xx[cut:])]
assert np.max(abs(whole-kept))<1e-12
sel=(t>.036)&(t<.061)
axs[1].plot(t[sel]*1000,whole[sel],color=G,label='连续处理／保留状态（重合）')
axs[1].plot(t[sel]*1000,reset[sel],color=O,ls='--',label='第二块状态清零')
axs[1].axvline(t[cut]*1000,color='gray',ls=':')
axs[1].set(xlabel='时间（ms）',ylabel='相对幅度',title='（b）分块边界：清零状态会引入新的瞬态')
axs[1].legend(fontsize=9);grid(axs[1]);save(fig,'06-filterbank-state')

# C: actual causal rectifier + envelope filter and selection samples.
fig,axs=plt.subplots(3,1,figsize=(12,7),layout='constrained')
i=1;sel=(t>=.04)&(t<.065)
axs[0].plot(t[sel]*1000,bands[i,sel],color=P)
axs[0].set(title='（a）E2 对应分频波形：保留正负振荡',ylabel='带通幅度')
axs[1].plot(t[sel]*1000,np.abs(bands[i,sel]),color=GRAY,label='全波整流')
axs[1].plot(t[sel]*1000,env[i,sel],color=G,lw=2,label='200 Hz 因果低通后的包络')
axs[1].set(title='（b）整流后平滑：包络不是瞬时正弦峰值',ylabel='相对幅度');axs[1].legend(fontsize=9)
samples=np.arange(32,52)*30
axs[2].plot(t[sel]*1000,env[i,sel],color=G)
axs[2].scatter(t[samples]*1000,env[i,samples],color=O,zorder=4,label='每 30 个声音样本取一次')
axs[2].set(title='（c）800 轮/s 的包络读数：间隔 1.25 ms',xlabel='时间（ms）',ylabel='包络读数');axs[2].legend(fontsize=9)
for ax in axs: grid(ax)
save(fig,'07-envelope-sampling')

# D: exact input scale and numerical example.
fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
levels=np.linspace(-70,15,600); mapped=enc.compress(.25*10**(levels/20))
axs[0].plot(levels,mapped,color=P,lw=2);axs[0].axvspan(-70,-50,color=GRAY,alpha=.3);axs[0].axvspan(0,15,color=GRAY,alpha=.3)
axs[0].scatter([-20],[enc.compress(np.array([.025]))[0]],color=O,zorder=4)
axs[0].annotate('a=0.025 → −20 dB\nu=0.6 → g≈0.8425',xy=(-20,.84248),xytext=(-46,.4),arrowprops={'arrowstyle':'->'},fontsize=11)
axs[0].set(xlabel='相对固定参考幅度的声级（dB；非 dB SPL）',ylabel='输出相对幅度',title='（a）截断 + 压缩：两端会出现平台')
u=np.linspace(0,1,300)
for mu,color in [(1,GRAY),(5,G),(20,P)]:axs[1].plot(u,np.log1p(mu*u)/np.log1p(mu),color=color,label=f'μ={mu}')
axs[1].plot(u,u,'--',color=O,label='线性参照 g=u')
axs[1].set(xlabel='归一化输入 u',ylabel='压缩输出 g(u)',title='（b）曲线形状：低水平斜率更大');axs[1].legend(fontsize=9)
for ax in axs:grid(ax)
save(fig,'08-compression-example')

# E: selected order is place order, not rank order.
fig,axs=plt.subplots(1,3,figsize=(12,4.8),layout='constrained')
v=np.array([.2,.5,.8,.1]); chosen=enc.select_channels(v,2)
assert np.array_equal(chosen,[1,2])
axs[0].bar(np.arange(1,5),v,color=[GRAY,P,P,GRAY]);axs[0].set(xticks=range(1,5),ylim=(0,1),xlabel='教学电极 E1–E4',ylabel='选择特征 v',title='（a）原始特征：取最大的 2 个')
for k,a in enumerate(v):axs[0].text(k+1,a+.03,f'{a:.2f}',ha='center')
axs[1].axis('off');axs[1].set_title('（b）强弱排序与保留集合');axs[1].text(.5,.75,'强弱排序\nE3 > E2 > E1 > E4',ha='center',va='center',fontsize=14,color=P)
axs[1].annotate('',xy=(.5,.38),xytext=(.5,.58),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':2})
axs[1].text(.5,.2,'保留集合\n{E2, E3}',ha='center',va='center',fontsize=16,color=G)
for q,ch in enumerate(chosen):
    axs[2].broken_barh([(q*58,58)],(ch+.7,.6),facecolors=P if q==0 else G)
    axs[2].text(q*58+29,ch+1,f'第 {q+1} 个',ha='center',va='center',color='white',fontsize=9)
axs[2].set(yticks=range(1,5),yticklabels=['E1','E2','E3','E4'],ylim=(.5,4.5),xlim=(-10,150),xlabel='轮内时间（µs）',title='（c）按位置调度：E2 → E3')
grid(axs[0]);grid(axs[2]);save(fig,'09-ace-selection')

# F: time budget with explicit inactive remainder.
fig,axs=plt.subplots(2,1,figsize=(12,5.4),layout='constrained')
for ax,N,label in [(axs[0],8,'CIS：8 个事件，464 µs'),(axs[1],4,'ACE：4 个事件，232 µs')]:
    for q in range(N):
        ax.add_patch(Rectangle((q*58,0),58,.75,facecolor=plt.cm.viridis(q/8),edgecolor='white'))
        ax.text(q*58+29,.37,str(q+1),ha='center',va='center',color='white',fontsize=10)
    ax.axvspan(N*58,1250,color=GRAY,alpha=.25)
    ax.text((N*58+1250)/2,.37,f'本轮剩余 {1250-N*58} µs',ha='center',va='center')
    ax.axvline(1250,color=O,ls='--');ax.set(xlim=(0,1350),ylim=(-.2,1),yticks=[],xlabel='相对本轮起点的时间（µs）',title=label)
    ax.text(1250,.85,'下一轮',ha='center',color=O)
fig.suptitle('同一轮次率 800 轮/s → 周期均为 1250 µs；格内数字是发放次序',color=P)
save(fig,'10-cycle-budget')

# G: events expanded into signed pulses with a separate fine time grid.
fig,axs=plt.subplots(2,1,figsize=(12,5.5),layout='constrained')
us=np.arange(-10,140,.25);amp=.8
for ch,onset,color in [(1,0,P),(2,58,G)]:
    wave=enc.biphasic(us*1e-6,onset*1e-6,amp)
    axs[0].step(us,wave+3*(ch-1),where='post',color=color,lw=2,label=f'E{ch}（纵向错开）')
axs[0].set(yticks=[0,3],yticklabels=['E1 基线','E2 基线'],xlabel='轮内时间（µs）',title='（a）事件起点 0、58 µs → 展开后的两电极双相波形');axs[0].legend(fontsize=9)
wave=enc.biphasic(us*1e-6,0,amp)
axs[1].step(us,wave,where='post',color=P)
axs[1].fill_between(us,wave,where=wave>0,step='post',color=G,alpha=.3)
axs[1].fill_between(us,wave,where=wave<0,step='post',color=O,alpha=.3)
axs[1].text(12,1,'正相面积 +20',ha='center',fontsize=10)
axs[1].text(45,-1.1,'负相面积 −20',ha='center',fontsize=10)
axs[1].text(98,.3,'面积单位：\n相对幅度 × µs\n净值 = 0',ha='center',fontsize=10)
axs[1].set(xlim=(-10,140),ylim=(-1.4,1.4),xlabel='相对 E1 事件起点（µs）',ylabel='相对幅度',title='（b）单相宽 25 µs，间隔 8 µs；面积不是临床电荷')
for ax in axs:grid(ax)
save(fig,'11-events-to-pulses')

# H: linear interpolation and generic sequence delays, not commercial CSSS.
fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
sx=np.array([10,11]);sy=np.array([-.4,.6]);cross=10.4
axs[0].plot(sx,sy,'o-',color=G);axs[0].axhline(0,color=GRAY)
axs[0].scatter([cross],[0],color=O,zorder=4,s=90)
axs[0].annotate('λ=0.4 → n+λ=10.4\n不是直接取 n 或 n+1',xy=(cross,0),xytext=(10.05,.42),arrowprops={'arrowstyle':'->'},fontsize=10)
axs[0].set(xlim=(9.9,11.1),ylim=(-.6,.85),xticks=[10,10.4,11],xlabel='声音样本位置',ylabel='分频幅度',title='（a）上行零交叉的线性插值')
starts=np.array([0,3.33]);offsets=np.array([0,.3,.6])
for k,start in enumerate(starts):
    axs[1].axvline(start,color=O,ls=':')
    axs[1].eventplot([start+offsets],lineoffsets=[1],linelengths=.55,colors=[P])
    axs[1].text(start+.3,1.6,f'交叉 {k+1} → 一组事件',ha='center',fontsize=10)
axs[1].set(xlim=(-.35,4.4),ylim=(.3,2),yticks=[],xlabel='时间（ms）',title='（b）通用序列示例：延时 0、0.3、0.6 ms')
axs[1].text(.5,.1,'仅演示“一次触发 → 多个事件”\n非 FSP／FS4 参数或完整 CSSS',ha='center',transform=axs[1].transAxes,color=O,fontsize=11)
grid(axs[0]);save(fig,'12-crossing-sequence')

# I: electrode glyphs plus a deliberately generic field mixture.
fig,axs=plt.subplots(1,2,figsize=(12,5.5),layout='constrained')
alphas=[0,.25,.5,.75,1]
for row,alpha in enumerate(alphas):
    shares=enc.steering(1,alpha)
    for col,share in enumerate(shares):
        axs[0].scatter(col,row,s=400+900*share,color=P if col==0 else G,alpha=.8,edgecolors='white')
        axs[0].text(col,row,f'{share:.2f}',ha='center',va='center',color='white' if share>.1 else '#333333',fontsize=10)
axs[0].set(xticks=[0,1],xticklabels=['电极 E_i','电极 E_(i+1)'],yticks=range(5),yticklabels=[f'α={a:g}' for a in alphas],xlim=(-.5,1.5),ylim=(4.7,-.7),title='（a）权重扫描：圆大小随电流份额增大')
z=np.linspace(-1,2,600);g1=np.exp(-z*z/(2*.45**2));g2=np.exp(-(z-1)**2/(2*.45**2))
for alpha in [0,.5,1]:axs[1].plot(z,(1-alpha)*g1+alpha*g2,label=f'α={alpha:g}')
axs[1].axvline(0,color=GRAY,ls=':');axs[1].axvline(1,color=GRAY,ls=':')
axs[1].set(xlabel='教学空间坐标 z（非 mm）',ylabel='相对场响应',title='（b）假设高斯传递关系的线性叠加')
axs[1].legend(fontsize=9);grid(axs[1]);fig.suptitle('权重变化 ≠ 独立神经通道增加；右图不预测个体神经激活或音高',color=P,fontsize=13)
save(fig,'13-steering-fields')

# J: exact custom masking formula from appendix, and its selected set.
ell=np.array([60.,58.,40.,52.,40.,49.]);channels=np.arange(6)
theta=np.maximum(0,ell[0]-8*abs(channels));score=ell-theta;score[0]=-np.inf
next_ch=int(np.argmax(score));assert next_ch==5
fig,axs=plt.subplots(1,3,figsize=(12,5.2),layout='constrained')
axs[0].bar(channels+1,ell,color=[P,P,GRAY,GRAY,GRAY,GRAY])
axs[0].set(title='（a）只按强度选 2 个：E1、E2',ylabel='特征声级（相对 dB）',ylim=(0,70))
axs[1].bar(channels+1,ell,color=GRAY,label='特征声级')
axs[1].plot(channels+1,theta,'o-',color=O,label='E1 入选后的假设阈值')
axs[1].set(title='（b）已选 E1 → 更新掩蔽阈',ylim=(0,70));axs[1].legend(fontsize=9)
axs[2].bar(channels[1:]+1,score[1:],color=[P if c==next_ch else GRAY for c in channels[1:]])
for c in channels[1:]:axs[2].text(c+1,score[c]+1,f'{score[c]:.0f}',ha='center')
axs[2].set(title='（c）剩余得分最高：下一步选 E6',ylabel='声级 − 阈值（dB）',ylim=(-10,38))
for ax in axs:ax.set(xticks=range(1,7),xlabel='教学电极 E1–E6');grid(ax)
fig.suptitle('自定义掩蔽教学例：M(1,i)=max(0, 60−8|i−1|) dB；不是商用 MP3000',fontsize=12,color=P)
save(fig,'14-masking-selection')

# K: numeric consequences of changing N, actual per-electrode counts.
fig,axs=plt.subplots(1,2,figsize=(12,5.2),layout='constrained')
counts=np.bincount(ace[:,1].astype(int),minlength=8)
assert int(counts.sum())==384
axs[0].bar(np.arange(1,9)-.18,np.full(8,96),width=.36,color=GRAY,label='CIS：每电极 96')
axs[0].bar(np.arange(1,9)+.18,counts,width=.36,color=P,label='ACE：按入选次数变化')
axs[0].set(xticks=range(1,9),xlabel='教学电极 E1–E8',ylabel='120 ms 内候选事件数',title='（a）候选事件如何分配到每个电极');axs[0].legend(fontsize=9)
ns=np.array([2,4,8]);totals=[]
for nn in ns:
    events=enc.schedule(env,int(nn),fs=enc.FS,rate=enc.RATE)
    assert len(events)==96*nn
    totals.append(len(events))
axs[1].bar(ns,totals,width=.9,color=[G,P,O])
for nn,total in zip(ns,totals):axs[1].text(nn,total+14,str(total),ha='center')
axs[1].set(xticks=ns,ylim=(0,860),xlabel='每轮事件数 N（保持 r=800）',ylabel='总候选事件数',title='（b）固定输入：P=96N；不预测响度或功耗')
for ax in axs:grid(ax)
save(fig,'15-event-counts')

record={'figure_names':names,'figures':len(names),'state_max_error':float(np.max(abs(whole-kept))),
    'masking_selected_electrodes':[1,next_ch+1],'ace_counts':counts.tolist(),
    'amplitude_unit':'dimensionless; masking uses a separate relative dB teaching scale'}
rec=ROOT/'artifacts/ci-coding';rec.mkdir(parents=True,exist_ok=True)
(rec/'figure-checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
