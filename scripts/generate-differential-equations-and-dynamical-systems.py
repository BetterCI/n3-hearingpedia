"""Generate original scientific plots, raster previews and course SVG."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[1];SLUG='differential-equations-and-dynamical-systems'
spec=importlib.util.spec_from_file_location('ddsmodels',ROOT/'public/code'/SLUG/'experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures'/SLUG;PRE=ROOT/'artifacts'/SLUG/'figures';REC=ROOT/'docs/research'/f'{SLUG}-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':SLUG,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def canvas(title):
    fig,ax=plt.subplots(1,2,figsize=(14,5.5));fig.suptitle(title,fontsize=18,fontweight='bold');return fig,ax
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创微分方程与动力系统教学图 · 指定归一化模型，非实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(l.rstrip() for l in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Slope field and initial conditions.
fig,ax=canvas('方程给变化率，初始条件选出一条演化')
tt,xx=np.meshgrid(np.linspace(0,6,19),np.linspace(-.05,1.6,16))
slope=1.2*xx*(1-xx);scale=np.sqrt(1+slope**2)
ax[0].quiver(tt,xx,1/scale,slope/scale,color=M,angles='xy',scale_units='xy',scale=5,width=.002)
t=np.linspace(0,6,501)
for x0,col in [(0,M),(.15,B),(.6,G),(1.4,R)]:
    y=m.logistic_flow(t,x0);ax[0].plot(t,y,color=col,lw=2)
    ax[1].plot(t,y,color=col,lw=2,label=f'x(0)={x0}')
ax[0].set(xlabel='归一化时间 τ',ylabel='状态 x',title='（a）方向场：x′=1.2x(1−x)',ylim=(-.05,1.6))
ax[1].axhline(1,color=M,ls=':',lw=.8);ax[1].set(xlabel='τ',ylabel='x(τ)',title='（b）正初值接近1，零解另行保留');ax[1].legend(fontsize=10)
save(fig,'slope-initial')
# 2 Continuous RHS need not give uniqueness; smooth RHS need not give global solutions.
fig,ax=canvas('局部存在、唯一与全时域存在是三件事')
t=np.linspace(0,3,601)
for c,col in [(0,R),(1,B),(2,G)]:
    ax[0].plot(t,np.maximum(t-c,0)**2,color=col,lw=2,label=f'等待时间 c={c}')
ax[0].plot(t,np.zeros_like(t),color=M,ls='--',label='始终为0')
ax[0].set(xlabel='τ',ylabel='x(τ)',title='（a）x′=2√|x|，x(0)=0：不唯一');ax[0].legend(fontsize=9)
t=np.linspace(0,.97,700);ax[1].plot(t,1/(1-t),color=R,lw=2,label='x=1/(1−τ)')
ax[1].axvline(1,color=M,ls='--',label='有限终点 τ=1')
ax[1].set(xlabel='τ（仅展示 τ<1）',ylabel='x(τ)',title='（b）x′=x²，x(0)=1：有限时间爆破',xlim=(0,1.05));ax[1].legend(fontsize=9)
save(fig,'existence-uniqueness')
# 3 Resonance and damping.
fig,ax=canvas('线性振动：阻尼、受迫频率与共振条件一起看')
t=np.linspace(0,30,1801);resonance=.1*t*np.sin(2*t)
ax[0].plot(t,resonance,color=R,lw=1.4,label='无阻尼，ω=ω₀=2')
ax[0].plot(t,m.oscillator(t,.1)[:,0],color=B,lw=1.4,label='阻尼比 ζ=0.1，同频强迫')
ax[0].set(xlabel='τ',ylabel='归一化位移 q',title='（a）q″+4ζq′+4q=0.4cos(2τ)');ax[0].legend(fontsize=9)
w=np.linspace(0,4,1000)
for z,col in [(.1,B),(.5,G)]:
    amp=.4/np.sqrt((4-w*w)**2+(4*z*w)**2)
    ax[1].plot(w,amp,color=col,lw=2,label=f'稳态幅值，ζ={z}')
ax[1].axvline(2,color=M,ls=':',label='无阻尼自然频率 ω₀=2')
ax[1].set(xlabel='强迫角频率 ω',ylabel='稳态位移幅值',title='（b）位移峰值一般不恰好在ω₀');ax[1].legend(fontsize=9)
save(fig,'forced-oscillation')
# 4 Four linear phase portraits, axes form part of the comparison.
fig,axes=plt.subplots(2,2,figsize=(14,9));fig.suptitle('相图展示状态怎样移动：结点、焦点、鞍点与中心',fontsize=18,fontweight='bold')
u,v=np.meshgrid(np.linspace(-2,2,23),np.linspace(-2,2,23))
labels={'node':'稳定结点：A=diag(−1,−2)','focus':'稳定焦点：A=[−0.2,−1;1,−0.2]','saddle':'鞍点：A=diag(1,−1)','center':'中心：A=[0,−1;1,0]'}
for ax,(name,A) in zip(axes.ravel(),m.linear_examples().items()):
    flow=A@np.array([u.ravel(),v.ravel()]);speed=np.hypot(*flow).reshape(u.shape)
    ax.streamplot(u[0],v[:,0],flow[0].reshape(u.shape),flow[1].reshape(u.shape),density=.8,color='#c2cbd0',linewidth=.7,arrowsize=.8)
    for x0,col in [([1.5,.6],B),([-.6,1.4],R),([1.1,-1.3],G)]:
        path=np.array([expm(A*t)@x0 for t in np.linspace(0,12,701)])
        path[np.any(abs(path)>2,axis=1)]=np.nan
        ax.plot(path[:,0],path[:,1],color=col,lw=2);ax.plot(*x0,'o',color=col,ms=4)
    ax.plot(0,0,'o',color=M,ms=4);ax.set(xlim=(-2,2),ylim=(-2,2),aspect='equal',xlabel='x₁',ylabel='x₂',title=labels[name])
save(fig,'linear-phase-portraits')
# 5 Energy and a family of closed curves, distinct from an isolated cycle.
fig,ax=canvas('守恒闭轨与耗散收敛：能量提供另一层解释')
t=np.linspace(0,20,1601)
for damp,col,label in [(0,M,'无阻尼 γ=0'),(.4,B,'阻尼 γ=0.4')]:
    d=m.pendulum(t,damp);x=d['state']
    ax[0].plot(x[:,0],x[:,1],color=col,lw=2,label=label)
    ax[1].plot(t,d['energy'],color=col,lw=2,label=label)
ax[0].plot(1.4,0,'o',color=R,label='共同初态(1.4,0)')
ax[0].set(xlabel='角度 θ / rad',ylabel='归一化角速度 v',title='（a）θ′=v，v′=−sinθ−γv');ax[0].legend(fontsize=9)
ax[1].set(xlabel='τ',ylabel='V=v²/2+1−cosθ',title='（b）V′=−γv²；初始V<2');ax[1].legend(fontsize=9)
save(fig,'pendulum-energy')
# 6 An exactly solvable radial normal form with orbital stability.
fig,ax=canvas('极限环吸引到一条闭合轨道，不是同一个固定点')
t=np.linspace(0,10,2501);angle=np.linspace(0,2*np.pi,501)
ax[0].plot(np.cos(angle),np.sin(angle),color=M,ls='--',label='极限环 r=1')
for r0,col in [(.2,B),(2.,R)]:
    xy=m.hopf(t,r0);ax[0].plot(xy[:,0],xy[:,1],color=col,lw=1.5,label=f'r(0)={r0}')
    ax[1].plot(t,m.hopf_radius(t,r0),color=col,lw=2,label=f'r(0)={r0}')
ax[0].plot(0,0,'o',color=P,ms=4);ax[0].set(xlabel='x',ylabel='y',aspect='equal',title='（a）μ=1，ω=2：内外均接近单位圆');ax[0].legend(fontsize=9)
ax[1].axhline(1,color=M,ls='--');ax[1].set(xlabel='τ',ylabel='半径 r',title='（b）r′=r−r³，角速度恒为2');ax[1].legend(fontsize=9)
save(fig,'limit-cycle-hopf')
# 7 One-dimensional bifurcation branches; parameter is not time.
fig,ax=canvas('参数变化可改变解的结构：分岔图不是时间曲线')
positive=np.linspace(.0001,1,500);negative=np.linspace(-1,0,300)
ax[0].plot(positive,np.sqrt(positive),color=B,lw=2,label='稳定平衡 +√μ')
ax[0].plot(positive,-np.sqrt(positive),color=R,ls='--',lw=2,label='不稳定平衡 −√μ')
ax[0].plot(0,0,'o',color=M);ax[0].set(xlabel='参数 μ',ylabel='平衡位置 x*',xlim=(-1,1),title='（a）鞍结：x′=μ−x²');ax[0].legend(fontsize=9)
ax[1].plot(negative,np.zeros_like(negative),color=B,lw=2,label='稳定分支')
ax[1].plot(positive,np.zeros_like(positive),color=R,ls='--',lw=2,label='不稳定分支')
ax[1].plot(positive,np.sqrt(positive),color=B,lw=2);ax[1].plot(positive,-np.sqrt(positive),color=B,lw=2)
ax[1].plot(0,0,'o',color=M);ax[1].set(xlabel='参数 μ',ylabel='平衡位置 x*',xlim=(-1,1),title='（b）超临界叉形：x′=μx−x³');ax[1].legend(fontsize=9)
save(fig,'bifurcation-branches')
# 8 Discrete noninvertible map: finite numerical diagram and pair separation.
fig,ax=canvas('离散映射也有动力系统：倍周期与初值敏感')
rates,values=m.map_bifurcation()
ax[0].scatter(np.tile(rates,values.shape[0]),values.ravel(),s=.12,color=B,alpha=.5,rasterized=True)
ax[0].set(xlabel='映射参数 r',ylabel='暂态后迭代值 xₙ',title='（a）xₙ₊₁=rxₙ(1−xₙ)，有限采样')
a=m.map_orbit(4.);b=m.map_orbit(4.,.123456789+1e-10)
ax[1].semilogy(np.arange(len(a)),np.maximum(abs(a-b),1e-16),color=R,lw=1.5)
ax[1].set(xlabel='迭代次数 n（不是连续时间）',ylabel='两初值序列之差 |δxₙ|',title='（b）r=4：差异增长后进入有界范围')
save(fig,'discrete-logistic-map')
# 9 Lorenz trajectory and finite-time sensitivity; no claim that the plot proves chaos.
fig=plt.figure(figsize=(14,5.5));a=fig.add_subplot(121,projection='3d');b=fig.add_subplot(122)
fig.suptitle('Lorenz系统：确定方程也可能限制长期逐点预测',fontsize=18,fontweight='bold')
t=np.linspace(0,45,4501);x=m.lorenz(t);xp=m.lorenz(t,1e-8);sel=(t>=5)&(t<=40)
a.plot(x[sel,0],x[sel,1],x[sel,2],color=B,lw=.6);a.set(xlabel='x',ylabel='y',zlabel='z',title='（a）σ=10，ρ=28，β=8/3');a.view_init(elev=24,azim=-57)
b.semilogy(t,np.maximum(np.linalg.norm(x-xp,axis=1),1e-16),color=R,lw=1.5)
b.set(xlabel='归一化时间 τ',ylabel='两轨道距离 ‖δx‖₂',title='（b）初值仅第一分量相差10⁻⁸')
save(fig,'lorenz-sensitivity')
# 10 Same displacement shape; different evolution law and energy.
fig,ax=canvas('偏微分方程还需要空间与边界：扩散和波动不同')
x=np.linspace(0,1,501);times=np.array([0,.2,.5,1.])
cols=[M,B,G,R]
for kind,a in [('heat',ax[0]),('wave',ax[1])]:
    fields=m.pde(x,times,kind)
    for t,f,col in zip(times,fields,cols):a.plot(x,f,color=col,lw=2,label=f'τ={t:g}')
    a.axhline(0,color=M,lw=.5);a.set(xlabel='归一化位置 ξ=x/L₀',ylabel='场 u(ξ,τ)');a.legend(fontsize=9)
ax[0].set(title='（a）热方程 uτ=0.08uξξ')
ax[1].set(title='（b）波动方程 uττ=uξξ，初速0')
save(fig,'pde-heat-wave')
sketch='''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="200" viewBox="0 0 320 200" role="img" aria-labelledby="title desc"><title id="title">微分方程与动力系统：相平面中的流与轨道</title><desc id="desc">简笔画用坐标、方向箭头和围绕平衡点盘旋的轨道表示微分方程生成的连续演化。</desc><rect width="320" height="200" rx="18" fill="#f6f1e7"/><g fill="none" stroke="#a7b3b5" stroke-width="1.7"><path d="M40 105H286M164 178V25"/><path d="M278 100L286 105L278 110M159 33L164 25L169 33"/></g><g fill="none" stroke="#537586" stroke-width="2"><path d="M59 66L72 54L68 63M241 54L258 62L248 62M270 143L257 157L259 148M88 168L72 159L82 159"/></g><path d="M72 47C223 8 298 159 184 170S76 88 142 64S226 117 187 134S139 108 157 94S188 101 174 111S160 105 165 101" fill="none" stroke="#b44e37" stroke-width="3"/><path d="M183 167L192 170L185 177M144 65L136 67L139 76" fill="none" stroke="#b44e37" stroke-width="2.5"/><circle cx="165" cy="103" r="4" fill="#31755e"/></svg>'''
(ROOT/'public/figures/foundation-courses'/f'{SLUG}.svg').write_text(sketch+'\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print('Generated 10 original scientific SVG/PNG pairs, 1 course sketch and calculations.')
