"""Reproducible control figures and native course SVG sketch."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Circle
from scipy import signal
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ctmodels',ROOT/'public/code/control-theory/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/control-theory';PRE=ROOT/'artifacts/control-theory/figures';REC=ROOT/'docs/research/control-theory-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'control-theory','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def canvas(title):
    fig,ax=plt.subplots(1,2,figsize=(14,5.5));fig.suptitle(title,fontsize=18,fontweight='bold');return fig,ax
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创控制理论教学图 · 归一化指定模型，非听者或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(l.rstrip() for l in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Negative-feedback architecture and a deliberately imperfect P controller.
fig,ax=canvas('反馈改变闭环动态；比例反馈仍会留下稳态误差')
a=ax[0];a.set(xlim=(0,10),ylim=(0,5));a.axis('off')
def arrow(start,end):a.annotate('',end,start,arrowprops={'arrowstyle':'->','color':M,'lw':1.8})
for cx,label in [(3.8,'控制器 C'),(6.8,'对象 P')]:
    a.add_patch(FancyBboxPatch((cx-1,2.4),2,1,boxstyle='round,pad=.05',facecolor='#eef3f4',edgecolor=B,lw=1.6));a.text(cx,2.9,label,ha='center',va='center')
a.add_patch(Circle((1.6,2.9),.28,fill=False,edgecolor=M,lw=1.5));a.text(1.6,2.9,'+',ha='center',va='center')
arrow((.1,2.9),(1.3,2.9));a.text(.25,3.3,'参考 r')
arrow((1.9,2.9),(2.7,2.9));a.text(2.1,3.2,'e')
arrow((4.9,2.9),(5.7,2.9));a.text(5,3.2,'u')
arrow((7.9,2.9),(9.8,2.9));a.text(8.8,3.25,'输出 y')
a.plot([8.5,8.5,1.6],[2.9,1,1],color=M,lw=1.8);arrow((1.6,1),(1.6,2.6));a.text(1.25,2.2,'−',fontsize=16)
a.text(5.2,.4,'单位测量反馈：e=r−y（此图未画噪声与扰动）',ha='center',fontsize=10)
a.set_title('（a）误差经控制器再次作用于对象')
t=np.linspace(0,8,801);op,cl=m.proportional(t)
ax[1].plot(t,op,color=R,lw=2,label='开环 u=r');ax[1].plot(t,cl,color=B,lw=2,label='反馈 u=4(r−y)')
ax[1].axhline(1,color=M,ls=':',label='参考 r=1');ax[1].axvline(3,color=G,ls='--',label='对象输入扰动 +0.3')
ax[1].set(xlabel='归一化时间 τ=t/T₀，T₀=1 s',ylabel='归一化输出 y',title='（b）对象 y′=−y+u+d');ax[1].legend(fontsize=9)
save(fig,'feedback-architecture')
# 2 Damping and hidden unstable state.
fig,ax=canvas('响应形状与内部稳定性要分别判断')
t=np.linspace(0,8,801)
for z,col in [(.2,R),(.7,B),(1.2,G)]:
    _,y=signal.step(([4.],[1.,4*z,4.]),T=t);ax[0].plot(t,y,color=col,lw=2,label=f'ζ={z}')
ax[0].axhline(1,color=M,lw=.7,ls=':');ax[0].set(xlabel='τ',ylabel='单位阶跃输出',title='（a）ωₙ=2，不同阻尼比');ax[0].legend()
ax[1].semilogy(t,np.exp(-t),color=B,lw=2,label='可见输出 y=x₁=e⁻ᵗ')
ax[1].semilogy(t,.02*np.exp(t),color=R,lw=2,label='不可见状态 x₂=0.02eᵗ')
ax[1].set(xlabel='τ',ylabel='状态或输出幅值',title='（b）A=diag(−1,+1)，C=(1,0)');ax[1].legend(fontsize=9)
save(fig,'response-internal-stability')
# 3 Root locus and instability from excessive positive gain.
fig,ax=canvas('负反馈并非必然稳定：本例只有 0<K<6 稳定')
ks=np.linspace(.001,12,600);roots=np.array([np.sort_complex(np.roots([1,3,2,k])) for k in ks])
for j in range(3):ax[0].plot(roots[:,j].real,roots[:,j].imag,color=B,alpha=.7,lw=1.5)
for k,col in [(2,G),(6,M),(8,R)]:
    r=np.roots([1,3,2,k]);ax[0].scatter(r.real,r.imag,color=col,s=35,label=f'K={k}',zorder=3)
ax[0].axvline(0,color=R,ls='--',lw=1);ax[0].set(xlabel='极点实部',ylabel='极点虚部',title='（a）特征式 s³+3s²+2s+K');ax[0].legend(fontsize=9)
t=np.linspace(0,25,1251)
for k,col in [(2,G),(5,B),(8,R)]:ax[1].plot(t,m.root_response(k,t),color=col,label=f'K={k}')
ax[1].axhline(1,color=M,ls=':',lw=.8);ax[1].set(xlabel='τ',ylabel='闭环单位阶跃输出',title='（b）K=8出现增幅振荡');ax[1].legend(fontsize=9)
save(fig,'root-locus-gain')
# 4 Frequency margins with an exact pure delay, no Pade approximation.
fig=plt.figure(figsize=(14,5.5));gs=fig.add_gridspec(2,2);a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[1,0]);c=fig.add_subplot(gs[:,1])
fig.suptitle('频率裕度说明距离临界还有多远；时延消耗相位',fontsize=18,fontweight='bold')
w=np.logspace(-2,2,1200);margin=m.margins();wc=margin['crossover']
a.semilogx(w,20*np.log10(np.abs(m.loop(w))),color=B);a.axhline(0,color=M,ls=':');a.axvline(wc,color=G,ls='--')
a.set(ylabel='环路幅值 / dB',title='（a）L₀=4/[(s+1)(s+2)]，ωc≈%.3f'%wc)
for delay,col in [(0,B),(1.5,R)]:
    phase=-np.rad2deg(np.arctan(w)+np.arctan(w/2)+delay*w)
    b.semilogx(w,phase,color=col,label=f'纯时延 θ={delay}')
b.axhline(-180,color=M,ls=':');b.axvline(wc,color=G,ls='--');b.set(xlabel='归一化角频率 ω',ylabel='展开相位 / 度',ylim=(-320,5));b.legend(fontsize=9)
ww=np.r_[-np.logspace(3,-4,3000),0,np.logspace(-4,3,3000)]
for delay,col in [(0,B),(1.5,R)]:
    z=m.loop(ww,delay);c.plot(z.real,z.imag,color=col,lw=1.5,label=f'θ={delay}')
c.plot(-1,0,'x',color=M,ms=10);c.annotate('临界点 −1',(-1,0),xytext=(-1.65,.4),arrowprops={'arrowstyle':'->','color':M},fontsize=10)
c.set(xlabel='Re L(jω)',ylabel='Im L(jω)',title='（b）正负频率轨迹均绘出',xlim=(-1.9,2.2),ylim=(-1.9,1.9),aspect='equal');c.legend(fontsize=9)
save(fig,'frequency-delay')
# 5 Sensitivity functions, exact identity S+T=1.
fig,ax=canvas('抗扰、跟踪与测量噪声受到同一环路约束')
w=np.logspace(-2,2,3000)
for delay,col in [(0,B),(1.,R)]:
    l=m.loop(w,delay);s=1/(1+l);tt=l/(1+l)
    ax[0].loglog(w,abs(s),color=col,lw=2,label=f'θ={delay}')
    ax[1].loglog(w,abs(tt),color=col,lw=2,label=f'θ={delay}')
for a in ax:a.axhline(1,color=M,ls=':',lw=.8);a.set(xlabel='归一化角频率 ω');a.legend(fontsize=10)
ax[0].set(ylabel='|S(jω)|',title='（a）S=1/(1+L)：灵敏度')
ax[1].set(ylabel='|T(jω)|',title='（b）T=L/(1+L)：互补灵敏度')
save(fig,'sensitivity-tradeoff')
# 6 Windup and back calculation.
fig,ax=canvas('执行器已饱和，积分器仍可能继续累积')
for anti,col,label in [(False,R,'无抗饱和'),(True,B,'反算抗饱和')]:
    d=m.windup(anti);ax[0].plot(d['t'],d['y'],color=col,lw=2,label=label)
    ax[1].plot(d['t'],d['command'],color=col,label=label+'：命令 uc')
    ax[1].plot(d['t'],d['actual'],color=col,ls='--',alpha=.7,label=label+'：实际 u')
ax[0].plot(d['t'],d['reference'],color=M,ls=':',label='参考：2 → 0.5')
ax[0].set(xlabel='τ',ylabel='输出与参考',title='（a）前5时间单位的参考不可实现');ax[0].legend(fontsize=9)
ax[1].axhline(1,color=G,ls=':',lw=.8);ax[1].axhline(-1,color=G,ls=':',lw=.8)
ax[1].set(xlabel='τ',ylabel='归一化控制量',title='（b）实际输入限制在[−1,1]');ax[1].legend(fontsize=8)
save(fig,'integrator-windup')
# 7 Full-state pole placement.
fig,ax=canvas('状态反馈改变内部极点；可控性限定能改变哪些模态')
t=np.linspace(0,8,801);d=m.state_feedback(t)
ax[0].plot(t,d['opened'][:,0],color=M,label='开环自由响应');ax[0].plot(t,d['closed'][:,0],color=B,lw=2,label='状态反馈 K=(4,4.4)')
ax[0].set(xlabel='τ',ylabel='归一化位置 x₁',title='（a）初态(1,0)，参考为0');ax[0].legend(fontsize=9)
ax[1].plot(t,d['control'],color=R,lw=2);ax[1].axhline(0,color=M,lw=.5);ax[1].set(xlabel='τ',ylabel='控制输入 u=−Kx',title='（b）极点由−0.3±j1.382变为−2、−3')
save(fig,'state-feedback')
# 8 Observer rate versus noise transfer; no stochastic claims.
fig,ax=canvas('观测器更快，并不意味着含噪估计总是更好')
t=np.linspace(0,3,601);w=np.logspace(-2,3,1500)
for poles,col,label in [((-4.,-5.),B,'极点 −4、−5'),((-12.,-15.),R,'极点 −12、−15')]:
    d=m.observer(t,poles);ax[0].semilogy(t,d['norm'],color=col,lw=2,label=label)
    ax[1].loglog(w,m.observer_noise(w,poles),color=col,lw=2,label=label)
ax[0].set(xlabel='τ',ylabel='无噪声误差 ‖x−x̂‖₂',title='（a）相同初始估计误差(1,0)');ax[0].legend(fontsize=9)
ax[1].set(xlabel='归一化角频率 ω',ylabel='|x̂₂ / n|：测量噪声通路',title='（b）位置测量噪声进入速度估计');ax[1].legend(fontsize=9)
save(fig,'observer-noise')
# 9 LQR effort tradeoff on a normalized spring-damper, not the textbook double integrator.
fig,ax=canvas('LQR优化的是指定代价：改变输入权重会改变动作')
t=np.linspace(0,8,801)
for r,col in [(.1,R),(1.,B),(10.,G)]:
    d=m.lqr(r,t);ax[0].plot(t,d['x'][:,0],color=col,lw=2,label=f'R={r:g}')
    ax[1].plot(t,d['control'],color=col,lw=2,label=f'R={r:g}')
ax[0].set(xlabel='τ',ylabel='归一化位置 x₁',title='（a）Q=I，初态(1,0)');ax[0].legend()
ax[1].set(xlabel='τ',ylabel='控制输入 u',title='（b）无输入硬约束的最优反馈');ax[1].legend()
save(fig,'lqr-effort')
# 10 Sampling a plant and holding feedback differs from sampling continuous feedback.
fig,ax=canvas('连续闭环稳定，不保证同一增益的数字实现稳定')
for h,col in [(.1,G),(.4,B),(.6,R)]:
    a=m.sampled(h)['pole'];k=np.arange(int(5/h)+1);x=a**k
    ax[0].plot(k*h,x,'o-',color=col,ms=3,label=f'h={h}，离散极点={a:.3f}')
ax[0].set(xlabel='τ=k h（只画采样时刻）',ylabel='xₖ，初值1',title='（a）对象x′=−x+u，uₖ=−4xₖ');ax[0].legend(fontsize=9)
h=np.linspace(.001,1,600);ax[1].plot(h,5*np.exp(-h)-4,color=R,lw=2,label='对象ZOH后闭环：5e⁻ʰ−4')
ax[1].plot(h,np.exp(-5*h),color=B,ls='--',lw=2,label='连续闭环的采样：e⁻⁵ʰ')
ax[1].axhline(-1,color=M,ls=':');ax[1].axhline(1,color=M,ls=':');ax[1].axvline(np.log(5/3),color=G,ls='--',label='临界 h=ln(5/3)')
ax[1].set(xlabel='归一化采样间隔 h=Tₛ/T₀',ylabel='离散极点',title='（b）两个运算的先后顺序不同');ax[1].legend(fontsize=9)
save(fig,'sampled-feedback')
sketch='''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="200" viewBox="0 0 320 200" role="img" aria-labelledby="title desc"><title id="title">控制理论：闭合的反馈回路与受控响应</title><desc id="desc">误差节点、控制器、对象与返回箭头组成反馈环，下方曲线从振荡逐渐接近虚线目标。</desc><rect width="320" height="200" rx="18" fill="#f6f1e7"/><g fill="none" stroke="#537586" stroke-width="2.5"><circle cx="48" cy="58" r="12"/><rect x="86" y="39" width="65" height="38" rx="6"/><rect x="190" y="39" width="65" height="38" rx="6"/><path d="M17 58H36M60 58H86M151 58H190M255 58H296M276 58V102H48V70"/><path d="M78 53L86 58L78 63M182 53L190 58L182 63M288 53L296 58L288 63M43 78L48 70L53 78"/></g><path d="M42 58H54M48 52V64M26 82H36" stroke="#b44e37" stroke-width="2"/><path d="M108 65L119 51L130 65M210 58H235" stroke="#31755e" stroke-width="2.5" fill="none"/><path d="M32 151H290" stroke="#a7a38d" stroke-width="2" stroke-dasharray="6 5"/><path d="M32 181C55 175 61 122 83 131S111 170 132 158S160 142 181 148S207 155 228 151S264 150 290 151" stroke="#b44e37" stroke-width="3" fill="none"/></svg>'''
(ROOT/'public/figures/foundation-courses/control-theory.svg').write_text(sketch+'\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print('Generated 10 scientific SVGs/PNG previews, 1 course sketch and calculations.')
