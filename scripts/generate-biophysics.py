"""Original scientific diagrams and parameter illustrations. No source images copied."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.stats import binom
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/biophysics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/biophysics';PRE=ROOT/'artifacts/biophysics/figures';REC=ROOT/'docs/research/biophysics-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'biophysics-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创生物物理学教学图 · 指定理想模型，非生理或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 States and thermal work scales.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));d=np.linspace(-6,6,601)
ax[0].plot(d,m.open_prob(d*m.kB*m.T),color=B,lw=2);ax[0].scatter([-2,0,2],m.open_prob(np.array([-2,0,2])*m.kB*m.T),color=R,zorder=3)
ax[0].set(xlabel='开态−闭态自由能差 / kBT',ylabel='开概率',title='（a）二状态局部平衡，T=310 K',ylim=(-.03,1.03))
work=np.array([.2*10,1*4,5*8,10*8])
ax[1].bar(['0.2 pN×10 nm','1 pN×4 nm','5 pN×8 nm','10 pN×8 nm'],work/(m.kB*m.T/1e-21),color=[G,B,P,R])
ax[1].axhline(1,color=M,ls='--',label='1 kBT');ax[1].tick_params(axis='x',labelsize=9)
ax[1].set(ylabel='指定机械功 / kBT',title='（b）力乘位移与热能比较');ax[1].legend()
fig.suptitle('热运动、能量差与状态概率',fontsize=18,fontweight='bold');save(fig,'energy-and-states')
# 2 Gaussian density and time scale.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(-80,80,1001)
for t,col in [(.1,B),(1,G),(5,R)]:ax[0].plot(x,m.diffusion(x,t),color=col,label=f't={t:g} s',lw=2)
ax[0].set(xlabel='位置 / µm',ylabel='一维概率密度 / µm⁻¹',title='（a）D=100 µm²/s，点初态');ax[0].legend()
L=np.logspace(0,2.5,301);ax[1].loglog(L,L*L/200,color=B,lw=2)
ax[1].scatter([10,100],[.5,50],color=R);ax[1].set(xlabel='长度尺度 L / µm',ylabel='L²/(2D) / s',title='（b）长度十倍，均方位移时间百倍')
fig.suptitle('扩散尺度：展宽与时间都要注明维数',fontsize=18,fontweight='bold');save(fig,'diffusion-scales')
# 3 Same Kd, distinct kinetics.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));c=np.logspace(-2,2,501);t=np.linspace(0,3,901)
ax[0].semilogx(c,c/(1+c),color=B,lw=2,label='三模型重合：Kd=1 µM');ax[0].set(xlabel='游离配体 / µM',ylabel='平衡占比',title='（a）相同Kd，平衡曲线相同');ax[0].legend()
for scale,col in [(.2,R),(1,G),(5,B)]:ax[1].plot(t,m.binding(t,scale),color=col,label=f'速率缩放 {scale:g}，τ={1/(3*scale):.3g} s',lw=2)
ax[1].set(xlabel='时间 / s',ylabel='占比 θ(t)',title='（b）c=2 µM，初始未结合');ax[1].legend(fontsize=9)
fig.suptitle('反应平衡与响应速度是两种信息',fontsize=18,fontweight='bold');save(fig,'binding-kinetics')
# 4 Potentials and GHK.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));vals=[m.nernst(1,140,5)*1000,m.nernst(1,12,145)*1000,m.nernst(-1,10,120)*1000]
ax[0].bar(['K⁺','Na⁺','Cl⁻'],vals,color=[B,R,G],width=.55);ax[0].axhline(0,color=M,lw=.7)
for i,v in enumerate(vals):ax[0].text(i,v+(4 if v>0 else -6),f'{v:.2f}',ha='center',va='bottom' if v>0 else 'top')
ax[0].set(ylabel='单离子平衡电位 / mV',ylim=(-115,90),title='（a）指定内外浓度，T=310 K')
ko=np.logspace(0,2,601);ax[1].semilogx(ko,m.nernst(1,140,ko)*1000,color=B,label='仅K⁺的Nernst',lw=2);ax[1].semilogx(ko,m.ghk(ko)*1000,color=P,label='三单价离子GHK',lw=2)
ax[1].set(xlabel='K⁺外浓度 / mM',ylabel='电位 / mV',title='（b）相对P：1 : 0.04 : 0.45');ax[1].legend(fontsize=10)
fig.suptitle('膜电位来自电与化学驱动力的组合',fontsize=18,fontweight='bold');save(fig,'electrochemical-potentials')
# 5 Membrane charge and branch current.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(0,.05,1001);V,cap,leak=m.passive(t)
ax[0].plot(t*1000,V*1000,color=B,lw=2);ax[0].axvline(10,color=M,ls='--',label='τ=10 ms');ax[0].axhline(-50,color=R,ls=':',label='终值−50 mV')
ax[0].set(xlabel='时间 / ms',ylabel='膜电位 / mV',title='（a）被动阶跃响应');ax[0].legend(fontsize=10)
ax[1].plot(t*1000,cap*1e12,color=P,label='电容充电 C·dV/dt',lw=2);ax[1].plot(t*1000,leak*1e12,color=G,label='向外漏电 gL(V−EL)',lw=2);ax[1].axhline(20,color=M,ls='--',label='向内注入20 pA')
ax[1].set(xlabel='时间 / ms',ylabel='电流 / pA',title='（b）充电＋漏电＝注入');ax[1].legend(fontsize=9)
fig.suptitle('电容、电导和驱动力必须一起进入守恒',fontsize=18,fontweight='bold');save(fig,'passive-membrane')
# 6 Probability and binomial fractions. Right panel is a fixed independent example.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(0,.04,601)
ax[0].plot(t*1000,m.gate(t),color=B,lw=2);ax[0].axhline(2/3,color=M,ls='--',label='p∞=2/3')
ax[0].set(xlabel='时间 / ms',ylabel='开概率',title='（a）α=100/s，β=50/s，p₀=0.2');ax[0].legend()
for N,col in [(100,R),(10000,B)]:
    low=max(0,int(.2*N-5*np.sqrt(.16*N)));high=min(N,int(.2*N+5*np.sqrt(.16*N)))
    n=np.arange(low,high+1);pmf=binom.pmf(n,N,.2)
    ax[1].plot(n/N,pmf*N,color=col,label=f'N={N}，比例SD={np.sqrt(.16/N):.3f}',lw=1.8)
ax[1].set(xlabel='开放比例 n/N',ylabel='概率质量 / 比例格宽',title='（b）另取稳态p=0.2，独立通道');ax[1].legend(fontsize=9)
fig.suptitle('通道数量决定涨落尺度，速率决定时间相关',fontsize=18,fontweight='bold');save(fig,'channel-kinetics')
# 7 Cable spatial transfer.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(0,.002,601)
for f,col in [(0,M),(10,G),(100,B)]:
    h=m.cable(x,f);ax[0].plot(x*1000,abs(h),color=col,label=f'{f} Hz',lw=2);ax[1].plot(x*1000,np.unwrap(np.angle(h))*180/np.pi,color=col,label=f'{f} Hz',lw=2)
ax[0].set(xlabel='距驱动端距离 / mm',ylabel='电压幅值 / 端点幅值',title='（a）高频沿空间衰减更强');ax[0].legend()
ax[1].set(xlabel='距驱动端距离 / mm',ylabel='相位 / °',title='（b）被动模型的空间相移');ax[1].legend()
fig.suptitle('电缆近似：λ约0.707 mm，τ=10 ms',fontsize=18,fontweight='bold');save(fig,'cable-filtering')
# 8 Overdamped mechanics, no generated noise trajectory.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));d=m.mechanics();t=np.linspace(0,.006,601)
ax[0].plot(t*1000,d['mean']*(1-np.exp(-t/d['tau']))*1e9,color=B,lw=2);ax[0].axhline(d['mean']*1e9,color=M,ls='--',label='平均终值20 nm')
ax[0].set(xlabel='时间 / ms',ylabel='平均位移 / nm',title='（a）0.2 pN恒力，τ≈0.942 ms');ax[0].legend()
xx=np.linspace(-80,80,901);sd=d['rms']*1e9;density=np.exp(-xx**2/(2*sd**2))/(np.sqrt(2*np.pi)*sd)
ax[1].plot(xx,density,color=G,lw=2,label=f'无外力平衡SD={sd:.2f} nm');ax[1].axvline(20,color=R,ls='--',label='恒力引起的均值位移20 nm')
ax[1].set(xlabel='无外力时相对平衡位置的位移 / nm',ylabel='概率密度 / nm⁻¹',title='（b）被动热平衡，k=10⁻⁵ N/m');ax[1].legend(fontsize=9)
fig.suptitle('响应与涨落：先说明平均、刚度和热平衡条件',fontsize=18,fontweight='bold');save(fig,'mechanics-and-noise')
# 9 Compartments and references.
fig,ax=plt.subplots(figsize=(14,5.5));ax.set(xlim=(0,14),ylim=(0,5));ax.axis('off')
for xy,w,h,fc,txt,col in [((.5,3.5),4.2,1.1,'#e8f1f6','内淋巴（指定）\nφendo = +80 mV',B),((.5,.4),4.2,1.1,'#edf4ef','外淋巴参考\nφperi = 0 mV',G),((6,1.6),4.2,1.8,'#f1edf7','毛细胞内部（指定）\nφin = −60 mV',P)]:
    ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=.12',facecolor=fc,edgecolor=col,lw=1.7))
    ax.text(xy[0]+w/2,xy[1]+h/2,txt,ha='center',va='center',fontsize=15,color=col)
ax.annotate('',xy=(6.1,3.05),xytext=(4.65,3.95),arrowprops=dict(arrowstyle='->',color=B,lw=2.5))
ax.text(8.25,4.2,'顶端跨膜：φin − φendo = −140 mV\nMET有效反转≈ +80 mV（对外淋巴）',ha='center',va='center',fontsize=12,color=B)
ax.annotate('',xy=(4.65,1.),xytext=(6.1,1.95),arrowprops=dict(arrowstyle='->',color=G,lw=2.5))
ax.text(8.5,.55,'基底侧跨膜：φin − φperi = −60 mV\n另设EK = −80 mV时，钾通路向外电流',ha='center',va='center',fontsize=12,color=G)
ax.text(12.15,2.5,'箭头仅示意\n本例阳离子\n驱动力方向',ha='center',va='center',fontsize=12,color=M)
fig.suptitle('同一细胞的两面，不同外部隔室与电压参考',fontsize=18,fontweight='bold');save(fig,'hair-cell-references')
# 10 Mechanical gating to graded voltage.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));xx=np.linspace(-80,100,901)
p,V=m.transduction(xx*1e-9);ax[0].plot(xx,p,color=B,lw=2);ax[0].axvline(10,color=M,ls='--',label='半开放10 nm')
ax[0].set(xlabel='设定位移 x / nm',ylabel='开概率 Po',title='（a）有效力0.3 pN，T=310 K');ax[0].legend()
for E,col in [(0,G),(.08,B)]:
    _,V=m.transduction(xx*1e-9,E);ax[1].plot(xx,V*1000,color=col,label=f'有效EMET = {E*1000:.0f} mV',lw=2)
ax[1].set(xlabel='设定位移 x / nm',ylabel='稳态胞内电位（对外淋巴）/ mV',title='（b）gK=20 nS，gMET最大10 nS');ax[1].legend(fontsize=10)
fig.suptitle('机械门控到受体电位：驱动力与负载共同决定',fontsize=18,fontweight='bold');save(fig,'transduction-chain')
thumb=ROOT/'public/figures/foundation-courses/biophysics.svg'
thumb.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180"><rect width="320" height="180" fill="#f2f0f7"/><g fill="none" stroke="#7c7091" stroke-width="2"><path d="M47 49q42-22 82 0t85 0M47 130q42 22 82 0t85 0"/><path d="M53 59v61m15-57v53m15-50v47m15-48v48m15-48v48m15-49v50m64-47v45m15-48v52"/></g><g fill="#f2f0f7" stroke="#437b91" stroke-width="2.4"><rect x="145" y="54" width="31" height="72" rx="9"/><path d="M154 60v60m13-60v60"/></g><g fill="#b58258"><circle cx="151" cy="30" r="5"/><circle cx="166" cy="16" r="4"/><circle cx="167" cy="145" r="5"/></g><path d="M243 52v80m0 0h48M246 126q9-54 40-56" fill="none" stroke="#437b91" stroke-width="2.3"/><path d="M237 92h11m-5-5v10" stroke="#7c7091" stroke-width="2"/></svg>\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,summary=m.summary()),ensure_ascii=True))
