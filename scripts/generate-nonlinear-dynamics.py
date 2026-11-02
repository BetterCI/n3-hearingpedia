"""Ten original scientific SVGs and a native course sketch."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
from scipy.signal import welch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];spec=importlib.util.spec_from_file_location('nd',ROOT/'public/code/nonlinear-dynamics/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/nonlinear-dynamics';PRE=ROOT/'artifacts/nonlinear-dynamics/figures';REC=ROOT/'docs/research/nonlinear-dynamics-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'nonlinear-dynamics-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创非线性动力学教学图 · 归一化指定模型，非听觉/生理/器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2);path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white');path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Exact scalar gradient model: no oscillations.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(-1.7,1.7,600);axes[0].plot(x,x**4/4-x*x/2,color=B,lw=2);axes[0].scatter([-1,0,1],[-.25,0,-.25],color=[G,R,G],s=60,zorder=3);axes[0].set(xlabel='状态 x',ylabel='V(x)',title='（a）x′=−V′：两个势阱与中间不稳定平衡')
t=np.linspace(0,6,501)
for x0 in [-1.5,-.4,.4,1.5]:
    s=m.solve(lambda t,x:x-x**3,(0,6),[x0],t_eval=t);axes[1].plot(t,s.y[0],color=G if x0<0 else P,lw=1.8)
axes[1].axhline(0,color=R,ls=':');axes[1].set(xlabel='归一化时间 τ',ylabel='状态 x',title='（b）符号不同的初值进入不同吸引域')
fig.suptitle('非线性允许多稳态：局部稳定不等于唯一最终状态',fontsize=18,fontweight='bold');save(fig,'basins-potential')
# 2 Static equilibrium branch and ghost passage: parameter, not time, on left.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(-1.45,1.45,1501);h=x**3-x;stable=abs(x)>1/np.sqrt(3)
axes[0].plot(np.where(stable,h,np.nan),x,color=G,lw=2,label='稳定分支');axes[0].plot(np.where(~stable,h,np.nan),x,color=R,ls='--',lw=2,label='不稳定分支');hc=2/(3*np.sqrt(3))
for v in [-hc,hc]:axes[0].axvline(v,color=M,ls=':',lw=1)
axes[0].set(xlim=(-.65,.65),xlabel='固定参数 h（不是时间）',ylabel='平衡 x*',title='（a）x′=h+x−x³；准静态折叠与滞后条件');axes[0].legend()
eps=np.geomspace(.001,.3,200);exact=2*np.arctan(1/np.sqrt(eps))/np.sqrt(eps);axes[1].loglog(eps,exact,color=B,label='精确过境时间');axes[1].loglog(eps,np.pi/np.sqrt(eps),color=P,ls='--',label='ε→0⁺渐近式π/√ε');axes[1].set(xlabel='参数 ε>0',ylabel='从−1到1的时间',title='（b）另一个模型x′=ε+x²：平衡消失后的瓶颈');axes[1].legend()
fig.suptitle('鞍结附近：静态分支、缓慢通过与动态扫参要区分',fontsize=18,fontweight='bold');save(fig,'folds-bottleneck')
# 3 Stable Hopf limit cycle and critical forced response.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(0,15,2001)
for r0,col in [(.12,B),(.8,P)]:
    r=m.hopf_radial(t,r0);axes[0].plot(r*np.cos(2*np.pi*t),r*np.sin(2*np.pi*t),color=col,lw=1,alpha=.8)
phi=np.linspace(0,2*np.pi,501);axes[0].plot(np.sqrt(.2)*np.cos(phi),np.sqrt(.2)*np.sin(phi),color=G,lw=2);axes[0].set(xlabel='x',ylabel='y',aspect='equal',title='（a）μ=0.2：半径√μ的吸引极限环')
F=np.geomspace(1e-6,1,250)
for mu,col in [(0,G),(-.2,B)]:
    radii=[next(r.real for r in np.roots([1,0,-mu,-f]) if abs(r.imag)<1e-8 and r.real>0) for f in F];axes[1].loglog(F,radii,color=col,lw=2,label=f'μ={mu:g}')
axes[1].set(xlabel='共振驱动幅度 F',ylabel='锁定解幅度 r',title='（b）c=0、精确共振；r³−μr=F');axes[1].legend()
fig.suptitle('超临界Hopf与临界压缩：同一正规形的不同问题',fontsize=18,fontweight='bold');save(fig,'hopf-critical-response')
# 4 Quintic stabilization is explicit; no claim pure cubic yields stable large cycle.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));mu=np.linspace(-.25,.15,401);disc=np.sqrt(1+4*mu);upper=np.sqrt((1+disc)/2);lower=np.sqrt(np.maximum((1-disc)/2,0));axes[0].plot(mu,upper,color=G,lw=2,label='稳定大环');mask=mu<0;axes[0].plot(mu[mask],lower[mask],color=R,ls='--',label='不稳定小环');axes[0].plot([-.32,0],[0,0],color=B,lw=2,label='稳定原点');axes[0].plot([0,.15],[0,0],color=R,ls='--');axes[0].axvline(-.25,color=M,ls=':');axes[0].axvline(0,color=M,ls=':');axes[0].set(xlabel='参数 μ',ylabel='周期轨道半径 / 原点',title='（a）−1/4<μ<0：原点与大环共存');axes[0].legend(fontsize=9)
t=np.linspace(0,35,1501)
for r0,col in [(.25,B),(.55,P),(1.1,G)]:
    s=m.solve(lambda t,r:r*(-.15+r*r-r**4),(0,35),[r0],t_eval=t);axes[1].plot(t,s.y[0],color=col,label=f'r₀={r0}')
for r in m.subcritical_radii(-.15):axes[1].axhline(r,color=M,ls=':',lw=.8)
axes[1].set(xlabel='归一化时间 τ',ylabel='r',title='（b）μ=−0.15：不稳定环分隔吸引域');axes[1].legend(fontsize=10)
fig.suptitle('亚临界Hopf需要交代全局饱和：这里显式加入−r⁵',fontsize=18,fontweight='bold');save(fig,'subcritical-hysteresis')
# 5 Van der Pol, aligned time segments for qualitative waveform shape.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));vdp=m.vdp_example()
for (mu,s),col in zip(vdp.items(),[B,R]):
    axes[0].plot(s.t-160,s.y[0],color=col,label=f'μ={mu:g}');axes[1].plot(s.y[0],s.y[1],color=col,label=f'μ={mu:g}')
axes[0].set(xlabel='暂态之后的时间 τ−160',ylabel='x',xlim=(0,28),title='（a）小μ近似正弦，大μ慢快交替');axes[1].set(xlabel='x',ylabel='v=x′',title='（b）同一方程的不同参数');axes[0].legend();axes[1].legend()
fig.suptitle('Van der Pol振荡：负阻尼输入与大幅度耗散共同作用',fontsize=18,fontweight='bold');save(fig,'van-der-pol')
# 6 First harmonic balance, do not label stability from real roots alone.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));amps=np.linspace(0,.7,300)
for alpha,col,label in [(1,B,'硬化 α=1'),(0,M,'线性 α=0'),(-1,P,'软化 α=−1（局部）')]:axes[0].plot(amps,np.sqrt(1+.75*alpha*amps**2),color=col,label=label)
axes[0].set(xlabel='近似基波幅度 A',ylabel='近似自由振荡角频率',title='（a）一阶近似骨干线；小振幅解释');axes[0].legend(fontsize=9)
om=np.linspace(.7,1.65,1200);xx=[];yy=[]
for w in om:
    for a in m.duffing_candidates(w):xx.append(w);yy.append(a)
axes[1].scatter(xx,yy,color=G,s=3);axes[1].set(xlabel='驱动角频率 Ω',ylabel='候选基波幅度 A',title='（b）ζ=0.05、α=1、F=0.2：谐波平衡根')
fig.suptitle('Duffing幅频弯曲：候选代数分支不是精确解或稳定性证书',fontsize=18,fontweight='bold');save(fig,'duffing-balance')
# 7 Phase locking in an explicitly chosen reduced model.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));K=np.linspace(0,2,300);axes[0].fill_betweenx(K,-K,K,color=G+'25');axes[0].plot(K,K,color=G);axes[0].plot(-K,K,color=G);axes[0].scatter([.4,1.3],[1,1],color=[B,R],s=55);axes[0].set(xlabel='失谐 Δ',ylabel='耦合 K≥0',title='（a）ψ′=Δ−K sinψ：|Δ|<K的稳定锁定区')
t,out=m.adler_example()
for (delta,s),col in zip(out.items(),[B,R]):axes[1].plot(t,s.y[0],color=col,label=f'Δ={delta:g}, K=1')
axes[1].set(xlabel='归一化时间 τ',ylabel='展开相位差 ψ / rad',title='（b）锁定与持续相位滑移');axes[1].legend()
fig.suptitle('同步不是必须零相位差：锁定边界依赖具体相位模型',fontsize=18,fontweight='bold');save(fig,'phase-locking')
# 8 Bifurcation sampling is numerical, not proof of every parameter's limiting set.
r,samples,exponents=m.logistic_bifurcation();fig,axes=plt.subplots(2,1,figsize=(14,7.5),gridspec_kw={'height_ratios':[2,1]});axes[0].plot(np.tile(r,128),samples[-128:].ravel(),',',color=B,alpha=.3,rasterized=True);axes[0].set(ylabel='暂态后xₙ',title='（a）1000个r；舍弃1600步，再绘最后128步')
axes[1].plot(r,exponents,color=R,lw=.7);axes[1].axhline(0,color=M,lw=.8);axes[1].set(xlabel='参数 r（不是时间）',ylabel='有限步平均log|f′|',ylim=(-2,1),title='（b）400步导数平均；尖谷截于−2，不作无穷时判定')
fig.suptitle('Logistic映射：倍周期、窗口与非均匀的参数结构',fontsize=18,fontweight='bold');save(fig,'logistic-chaos')
# 9 One recorded finite-time Lorenz QR run, not a theorem proof.
qr=m.lorenz_qr();(REC/'lorenz-qr.json').write_text(json.dumps(qr,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
s=m.solve(m.lorenz,(0,65),[1.,1.,1.],t_eval=np.linspace(25,65,5001),max_step=.02);fig=plt.figure(figsize=(14,5.5));ax=fig.add_subplot(121,projection='3d');ax.plot(*s.y,color=B,lw=.45);ax.set(xlabel='x',ylabel='y',zlabel='z',title='（a）σ=10、ρ=28、β=8/3；舍弃前25时间单位')
ax=fig.add_subplot(122);history=np.asarray(qr['history']);times=np.asarray(qr['times'])
for i,(col,label) in enumerate([(R,'λ₁'),(G,'λ₂'),(B,'λ₃')]):ax.plot(times,history[:,i],color=col,label=label)
ax.axhline(0,color=M,lw=.7);ax.set(xlabel='累计变分时间 T',ylabel='有限时间指数 / τ',ylim=(-16,3),title='（b）变分方程+QR，预热30、累计240');ax.legend()
fig.suptitle('Lorenz：轨道几何与切向伸长率提供不同层次的数值信息',fontsize=18,fontweight='bold');save(fig,'lorenz-exponents')
# 10 Deterministic nonlinear map and stochastic sequence both have broad spectra.
data=m.logistic_series();noise=np.random.default_rng(20261102).normal(size=len(data));fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for v,col,label,offset in [(data,B,'Logistic r=4',0),(noise,R,'独立高斯随机序列',4)]:
    z=(v-v.mean())/v.std();axes[0].plot(np.arange(160),z[:160]+offset,color=col,lw=.8,label=label);f,p=welch(z,fs=1.,nperseg=512);axes[1].semilogy(f,p,color=col,label=label)
axes[0].set(xlabel='离散步 n',ylabel='标准化值（红线纵向平移4）',title='（a）来源不同，都可呈现不规则波形');axes[1].set(xlabel='频率 / cycles per step',ylabel='Welch PSD（标准化序列）',title='（b）宽谱不是确定性混沌的充分条件');axes[0].legend(fontsize=9);axes[1].legend(fontsize=9)
fig.suptitle('从模型到数据：非线性、随机性和混沌必须分别检验',fontsize=18,fontweight='bold');save(fig,'data-evidence')
# Native course thumbnail: bifurcating branch plus phase orbit, without copied artwork.
fig,ax=plt.subplots(figsize=(6.4,3.6));ax.axis('off');ax.set(xlim=(-2,3),ylim=(-1.6,1.8));q=np.linspace(0,1.6,200);ax.plot([-1.6,0],[0,0],color=B,lw=2);ax.plot([0,1.6],[0,0],color=R,ls='--',lw=1.5);ax.plot(q,np.sqrt(q),color=G,lw=2);ax.plot(q,-np.sqrt(q),color=G,lw=2);phi=np.linspace(0,2*np.pi,500);ax.plot(2.2+.5*np.cos(phi),.7*np.sin(phi),color=P,lw=2);ax.text(-1.7,1.5,'非线性动力学',fontsize=18,fontweight='bold',color=B);fig.tight_layout();path=ROOT/'public/figures/foundation-courses/nonlinear-dynamics.svg';fig.savefig(path,metadata={'Date':None},transparent=True);path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8');plt.close(fig)
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(dict(summary=m.summary(),lorenz_exponents=qr['exponents']),ensure_ascii=False))
