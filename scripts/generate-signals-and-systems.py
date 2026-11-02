"""Create independent SVG teaching figures and raster previews, no source art copied."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('m',ROOT/'public/code/signals-and-systems/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/signals-and-systems';PRE=ROOT/'artifacts/signals-and-systems/figures';REC=ROOT/'docs/research/signals-and-systems-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'signals-and-systems','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创信号与系统教学图 · 指定理想模型，非生理或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def stem(ax,x,y,col=B,label=None):
    a,b,c=ax.stem(x,y,basefmt=' ',label=label);plt.setp(a,color=col,markersize=4);plt.setp(b,color=col,linewidth=1.2)
# 1 Coordinates.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(-.003,.005,1201)
for xx,label,col in [(m.pulse(t),'x(t)',B),(m.pulse(t-.002),'x(t−2 ms)',G),(m.pulse(2*t),'x(2t)',R)]:
    ax[0].plot(t*1000,xx,label=label,color=col,lw=2)
ax[0].set(xlabel='时间 / ms',ylabel='无单位幅度',title='（a）延迟与时间压缩');ax[0].legend()
n=np.arange(-16,33);stem(ax[1],n,m.pulse(n/8000));ax[1].set(xlabel='整数样本索引 n',ylabel='无单位样值',title='（b）8 kHz采样，Ts=0.125 ms')
fig.suptitle('同一脉冲：横轴、索引与变换规则',fontsize=18,fontweight='bold');save(fig,'signal-coordinates')
# 2 Superposition.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x1=.6*m.pulse(t);x2=.6*m.pulse(t-.0004);clip=lambda x:np.clip(x,-.7,.7)
for a,T,title in [(ax[0],lambda x:2*x,'（a）固定增益2：满足叠加'),(ax[1],clip,'（b）±0.7限幅：不满足叠加')]:
    a.plot(t*1000,T(x1+x2),color=B,lw=2.5,label='T{x1+x2}');a.plot(t*1000,T(x1)+T(x2),color=R,ls='--',lw=2,label='T{x1}+T{x2}')
    a.set(xlabel='时间 / ms',ylabel='无单位输出',title=title);a.legend()
fig.suptitle('线性要检验处理次序，不能只看曲线外形',fontsize=18,fontweight='bold');save(fig,'system-properties')
# 3 Echo impulse and full convolution.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));fs,x,h,y=m.echo();stem(ax[0],np.array([0,40,96])/fs*1000,h[[0,40,96]])
ax[0].axhline(0,color=M,lw=.6);ax[0].set(xlabel='延迟 / ms',ylabel='通路系数',title='（a）三个离散冲激，fs=8 kHz')
ax[1].plot(np.arange(len(x))/fs*1000,x,color=M,ls='--',label='输入',lw=2)
ax[1].plot(np.arange(len(y))/fs*1000,y,color=B,label='完整卷积输出',lw=2)
ax[1].set(xlabel='时间 / ms',ylabel='无单位幅度',title='（b）延迟副本相加，保留尾部');ax[1].legend()
fig.suptitle('卷积：每个样本激起同一通路的移位响应',fontsize=18,fontweight='bold');save(fig,'convolution-echo')
# 4 Initial state and unit impulse.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));tt=np.linspace(0,.03,901);zs,zi,total=m.initial(tt)
for yy,col,label,ls in [(total,B,'全响应','-'),(zs,G,'零状态响应','--'),(zi,R,'零输入响应',':')]:ax[0].plot(tt*1000,yy,color=col,label=label,ls=ls,lw=2)
ax[0].set(xlabel='时间 / ms',ylabel='无单位输出',title='（a）τ0=5 ms，y(0)=0.5');ax[0].legend()
ax[1].plot(tt*1000,zs,color=G,lw=2,label='阶跃响应');ax[1].set(xlabel='时间 / ms',ylabel='阶跃响应 / 无单位',title='（b）冲激与阶跃的单位不同')
other=ax[1].twinx();other.plot(tt*1000,np.exp(-tt/.005)/.005,color=P,lw=2,label='冲激响应');other.set_ylabel('冲激响应 / s⁻¹',color=P);other.spines['right'].set_visible(True)
ax[1].legend(loc='center right');other.legend(loc='lower right')
fig.suptitle('初始记忆与输入作用需要分开计算',fontsize=18,fontweight='bold');save(fig,'initial-state')
# 5 Fourier square-wave approximations.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for a,xx,title in [(ax[0],np.linspace(-1,1,2001),'（a）两个完整周期'),(ax[1],np.linspace(-.15,.15,1401),'（b）同一跳变的局部放大')]:
    a.plot(xx,np.sign(np.sin(2*np.pi*xx)),color=M,ls=':',label='±1方波')
    for last,col in [(1,G),(5,P),(21,B)]:a.plot(xx,m.square_series(xx,last),color=col,label=f'最高谐波 {last}',lw=1.8)
    a.set(xlabel='时间 / 周期',ylabel='无单位幅度',title=title,ylim=(-1.4,1.4));a.legend(fontsize=9)
fig.suptitle('傅里叶级数：截断、跳变与Gibbs过冲',fontsize=18,fontweight='bold');save(fig,'fourier-series')
# 6 Frequency response and group delay.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));f=np.logspace(0,4,1001);tau=1/(2*np.pi*200);H=m.lowpass(2*np.pi*f,tau)
ax[0].semilogx(f,20*np.log10(abs(H)),color=B,lw=2);ax[0].scatter([200],[-10*np.log10(2)],color=R,zorder=3);ax[0].axvline(200,color=M,ls='--');ax[0].set(xlabel='频率 / Hz',ylabel='幅度增益 / dB',title='（a）截止200 Hz，约−3.01 dB')
ax[1].semilogx(f,1000*tau/(1+(2*np.pi*f*tau)**2),color=B,lw=2,label='一阶低通');ax[1].axhline(2,color=R,ls='--',label='2 ms纯延迟')
ax[1].set(xlabel='频率 / Hz',ylabel='群延迟 / ms',title='（b）随频率变化与恒定延迟');ax[1].legend()
fig.suptitle('一阶低通与纯延迟：增益和时间作用分别判断',fontsize=18,fontweight='bold');save(fig,'frequency-response')
# 7 DTFT and DFT sample grids; both normalized by original N.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));seq=m.record_sequence();fc=np.linspace(0,.25,2001);dense=abs(m.dtft(seq,fc))/32
for a,L in zip(ax,[32,128]):
    ff=np.arange(L)/L;sel=ff<=.25
    a.plot(fc,dense,color=M,lw=1.6,label='同一32点记录的DTFT');stem(a,ff[sel],abs(np.fft.fft(seq,L)[sel])/32,B,label=f'{L}点DFT取样')
    a.set(xlabel='归一化频率 / 周每样本',ylabel='幅度 / 原始长度32',title=f'（{"a" if L==32 else "b"}）DFT长度{L}',ylim=(-.02,1.08));a.legend(fontsize=9)
fig.suptitle('补零改变取样密度，不改变原记录的谱形状',fontsize=18,fontweight='bold');save(fig,'dtft-dft')
# 8 ROC regions for the same algebraic Z expression.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));grid=np.linspace(-1.6,1.6,501);xx,yy=np.meshgrid(grid,grid);rad=np.hypot(xx,yy)
for a,outside,title in [(ax[0],True,'（a）因果：|z|>0.8，包含单位圆'),(ax[1],False,'（b）反因果：|z|<0.8，不含单位圆')]:
    mask=rad>.8 if outside else rad<.8
    a.contourf(xx,yy,mask.astype(int),levels=[-.5,.5,1.5],colors=['white','#dcecf5'])
    a.add_patch(Circle((0,0),.8,fill=False,color=R,lw=1.6,label='ROC边界（不含）'))
    a.add_patch(Circle((0,0),1,fill=False,color=M,ls='--',lw=1.5,label='单位圆'))
    a.scatter([.8],[0],marker='x',s=65,color=R,zorder=4,label='极点0.8')
    a.axhline(0,color=M,lw=.5);a.axvline(0,color=M,lw=.5);a.set(aspect='equal',xlim=(-1.6,1.6),ylim=(-1.6,1.6),xlabel='Re z',ylabel='Im z',title=title);a.legend(fontsize=8,loc='lower left')
fig.suptitle('同一个X(z)=1/(1−0.8z⁻¹)，还须给出ROC',fontsize=18,fontweight='bold');save(fig,'region-of-convergence')
# 9 Time aliasing and independent midrise amplitude quantization.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));tt=np.linspace(0,.001,1601);ts=np.arange(9)/8000
ax[0].plot(tt*1000,np.cos(2*np.pi*6000*tt),color=R,lw=1.6,label='6 kHz连续余弦');ax[0].plot(tt*1000,np.cos(2*np.pi*2000*tt),color=B,lw=1.6,label='2 kHz连续余弦')
ax[0].scatter(ts*1000,np.cos(2*np.pi*2000*ts),color='black',s=25,zorder=4,label='共同样本，fs=8 kHz')
ax[0].set(xlabel='时间 / ms',ylabel='无单位幅度',title='（a）两个不同连续信号给出相同样本');ax[0].legend(fontsize=9)
xx=np.linspace(-1,1,2001);ax[1].plot(xx,xx,color=M,ls='--',label='未量化');ax[1].plot(xx,m.quantize(xx),color=G,lw=2,label='八级中升量化')
ax[1].set(xlabel='无单位输入',ylabel='量化输出',title='（b）独立幅度示例：Δ=0.25');ax[1].legend()
fig.suptitle('时间混叠与幅度量化分别检查',fontsize=18,fontweight='bold');save(fig,'sampling-quantization')
# 10 Delayed feedback diagram and response envelope.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));a=ax[0];a.set(xlim=(0,10),ylim=(0,6));a.axis('off')
a.text(.5,4,'x[n]',ha='center',fontsize=14);a.add_patch(Circle((3,4),.4,fill=False,color=B,lw=2));a.text(3,4,'+',ha='center',va='center',fontsize=18);a.text(8.7,4.35,'y[n]',fontsize=14)
for start,end in [((1.2,4),(2.6,4)),((3.4,4),(8.7,4)),((8,4),(8,1.5)),((8,1.5),(6.8,1.5)),((4.8,1.5),(3,1.5)),((3,1.5),(3,3.6))]:
    a.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color=B,lw=2))
a.add_patch(FancyBboxPatch((4.8,.9),2,1.2,boxstyle='round,pad=.05',facecolor='#edf2f7',edgecolor=B,lw=1.5));a.text(5.8,1.5,'k × 延迟1样本',ha='center',va='center',fontsize=11)
a.text(2.45,3.25,'−',color=R,fontsize=19);a.text(5,.15,'y[n] = x[n] − k y[n−1]',ha='center',fontsize=13);a.set_title('（a）反馈支路含一个样本延迟')
n=np.arange(60)
for k,col in [(.5,B),(1.05,R)]:ax[1].semilogy(n,abs(m.feedback(k)),color=col,lw=2,label=f'k={k:g}，极点−{k:g}')
ax[1].set(xlabel='样本索引 n',ylabel='冲激响应绝对值（对数）',title='（b）衰减或增长由闭环极点决定');ax[1].legend(fontsize=9)
fig.suptitle('负反馈结构不自动保证稳定',fontsize=18,fontweight='bold');save(fig,'feedback-stability')
thumb=ROOT/'public/figures/foundation-courses/signals-and-systems.svg'
thumb.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180"><rect width="320" height="180" fill="#f2f0f7"/><g fill="none" stroke="#7c7091" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 87h12q8 0 13-27t12 0q5 27 14 27h10M83 87h15m-5-5 5 5-5 5"/><rect x="103" y="59" width="83" height="56" rx="9"/><path d="M118 101h54M121 97V75m9 22V68m9 29V81m9 16V87m9 10V91m32-4h15m-5-5 5 5-5 5"/></g><path d="M210 104h9q6 0 10-29t10 0q4 29 10 29h6q5 0 9-17t8 0q4 17 10 17h17" fill="none" stroke="#437b91" stroke-width="2.5" stroke-linecap="round"/><path d="M104 137h82m-63-7 17 7-17 7" fill="none" stroke="#b58258" stroke-width="2" stroke-linecap="round"/></svg>\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(m.summary(),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,summary=m.summary())))
