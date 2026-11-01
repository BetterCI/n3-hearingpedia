"""Generate original vector figures and PNG previews from specified mathematical models."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.special import jv,jn_zeros,eval_legendre
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/mathematical-physics-methods/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
FIG=ROOT/'public/figures/mathematical-physics-methods';PRE=ROOT/'artifacts/mathematical-physics-methods/figures';REC=ROOT/'docs/research/mathematical-physics-methods-2026-11-02'
for d in [FIG,PRE,REC]:d.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'mathematical-physics-methods','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创数学物理方法教学图 · 指定理想问题，非器件或人体实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    out=FIG/(name+'.svg');fig.savefig(out,metadata={'Date':None},facecolor='white')
    out.write_text('\n'.join(s.rstrip() for s in out.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
x=np.linspace(0,1,1001)
# 1 Reference problems and distinct spectra.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for row,(label,left,right) in enumerate([('零值端点','u(0)=0','u(L)=0'),('零导数端点',"u′(0)=0","u′(L)=0"),('混合端点','u(0)=0',"u′(L)=0")]):
    y=2-row;ax[0].plot([.15,.85],[y,y],color=M,lw=3);ax[0].scatter([.15,.85],[y,y],c=P,s=50,zorder=3)
    ax[0].text(.5,y+.18,label,ha='center',color=P);ax[0].text(.15,y-.22,left,ha='center');ax[0].text(.85,y-.22,right,ha='center')
ax[0].set(xlim=(0,1),ylim=(-.55,2.6),title='（a）未知量相同，端点约束可以不同');ax[0].axis('off')
for y,col,label in [(np.sin(np.pi*x),B,'零值：sin(πx/L)'),(np.cos(np.pi*x),G,'零导数：cos(πx/L)'),(np.sin(.5*np.pi*x),R,'混合：sin(πx/2L)')]:ax[1].plot(x,y,color=col,label=label,lw=2)
ax[1].axhline(0,color=M,lw=.7);ax[1].set(xlabel='x / L',ylabel='示例模态值',title='（b）边界不同，允许的空间波数不同');ax[1].legend(fontsize=10)
fig.suptitle('方程必须和定解条件一起给出',fontsize=18,fontweight='bold');save(fig,'problem-and-boundaries')
# 2 Eigenfunctions and Gram matrix.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
modes=np.sqrt(2)*np.sin(np.arange(1,4)[:,None]*np.pi*x)
for n,y,col in zip(range(1,4),modes,[B,G,R]):ax[0].plot(x,y,color=col,label=f'n={n}',lw=2)
ax[0].set(xlabel='x / L（L=1）',ylabel='归一化特征函数',title='（a）区间零值端点的前三阶');ax[0].legend()
gram=np.array([[np.trapz(f*g,x) for g in modes] for f in modes])
im=ax[1].imshow(gram,vmin=0,vmax=1,cmap='Blues')
for i in range(3):
    for j in range(3):ax[1].text(j,i,f'{gram[i,j]:.3f}',ha='center',va='center',color='white' if i==j else M)
ax[1].set(xticks=range(3),yticks=range(3),xticklabels=['1','2','3'],yticklabels=['1','2','3'],xlabel='模态 n',ylabel='模态 m',title='（b）积分内积矩阵，权重w=1')
fig.suptitle('把函数当作坐标轴：正交与归一化',fontsize=18,fontweight='bold');save(fig,'eigenfunctions')
# 3 Pluck expansion.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));n=np.arange(1,101);b=model.pluck_coeff(n)
ax[0].plot(x,model.pluck_shape(x)*1000,'--',color=M,label='指定三角初态',lw=2)
for N,col in [(3,R),(10,G),(50,B)]:ax[0].plot(x,(b[:N,None]*np.sin(n[:N,None]*np.pi*x)).sum(0)*1000,color=col,label=f'{N}项',lw=1.5)
ax[0].set(xlabel='位置 x / m',ylabel='初位移 / mm',title='（a）分段初态的正弦重建');ax[0].legend(fontsize=10)
ax[1].vlines(n[:20],0,b[:20]*1000,color=B);ax[1].scatter(n[:20],b[:20]*1000,color=B,s=25);ax[1].axhline(0,color=M,lw=.7)
ax[1].set(xlabel='模态序号 n',ylabel='有符号系数 bₙ / mm',xticks=[1,5,10,15,20],title='（b）a=0.3L，系数并非全为正')
fig.suptitle('被拨动的弦：形状投影成一组模态权重',fontsize=18,fontweight='bold');save(fig,'plucked-string')
# 4 Heat versus wave.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for t,col in [(0,M),(.2,B),(.6,G),(1,R)]:
    heat,wave=model.heat_wave(x,t)
    ax[0].plot(x,heat,color=col,label=f't={t:g} s',lw=1.8);ax[1].plot(x,wave,color=col,label=f't={t:g} s',lw=1.8)
for a in ax:a.set(xlabel='位置 / m',ylabel='归一化场值',ylim=(-1.2,1.2));a.legend(fontsize=10);a.axhline(0,color=M,lw=.5)
ax[0].set_title('（a）扩散：D=0.1 m²/s');ax[1].set_title('（b）无损波动：c=1 m/s')
fig.suptitle('相同初形状与空间模态，不同时间演化',fontsize=18,fontweight='bold');save(fig,'heat-and-wave')
# 5 Resonance amplitude and phase.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));r=np.linspace(0,2,1801)
for z,col in [(.03,B),(.2,G),(.8,R)]:
    H=1/(1-r*r+2j*z*r)
    ax[0].plot(r,abs(H),color=col,label=f'ζ={z:g}',lw=2)
    ax[1].plot(r,np.angle(H)*180/np.pi,color=col,label=f'ζ={z:g}',lw=2)
ax[0].set(xlabel='频率比 ω / ωₙ',ylabel='归一化位移幅值',title='（a）非零阻尼使峰值有限');ax[0].legend()
ax[1].set(xlabel='频率比 ω / ωₙ',ylabel='相位 / °',title='（b）采用 exp(jωt) 时间约定');ax[1].legend()
fig.suptitle('自然频率、响应峰与损耗需要分开判断',fontsize=18,fontweight='bold');save(fig,'modal-resonance')
# 6 Circular membrane.
fig,axes=plt.subplots(1,4,figsize=(14,5.5));g=np.linspace(-1,1,241);xx,yy=np.meshgrid(g,g);rr=np.hypot(xx,yy);theta=np.arctan2(yy,xx)
for ax,(m,n) in zip(axes,[(0,1),(1,1),(2,1),(0,2)]):
    root=jn_zeros(m,n)[-1];u=jv(m,root*rr)*np.cos(m*theta);u/=np.max(np.abs(u[rr<=1]));u=np.ma.masked_where(rr>1,u)
    ax.contourf(xx,yy,u,levels=np.linspace(-1,1,33),cmap='RdBu_r')
    if np.min(u)<-1e-5:ax.contour(xx,yy,u,levels=[0],colors='white',linewidths=1.3)
    ax.add_patch(Circle((0,0),1,fill=False,color=M,lw=1.5));ax.set(aspect='equal',xlim=(-1.05,1.05),ylim=(-1.05,1.05),title=f'm={m}, n={n}\n零点 {root:.5f}',xlabel='x / a');ax.set_yticks([-1,0,1]);ax.set_xticks([-1,0,1])
axes[0].set_ylabel('y / a')
fig.suptitle('圆膜的节径与节圆：Jₘ(κr) cos(mθ)',fontsize=18,fontweight='bold');save(fig,'circular-modes')
# 7 Legendre and angular polar display.
fig=plt.figure(figsize=(14,5.5));gs=fig.add_gridspec(1,5,width_ratios=[2.4,1,1,1,1]);left=fig.add_subplot(gs[0]);z=np.linspace(-1,1,600)
for ell,col in zip(range(4),[M,B,G,R]):left.plot(z,eval_legendre(ell,z),label=f'ℓ={ell}',color=col,lw=1.8)
left.set(xlabel='z',ylabel='Pℓ(z)',title='（a）勒让德多项式');left.legend(fontsize=9);angle=np.linspace(0,2*np.pi,1001)
for ell in range(4):
    ax=fig.add_subplot(gs[ell+1],projection='polar');val=eval_legendre(ell,np.cos(angle))
    ax.plot(angle,np.where(val>=0,abs(val),np.nan),color=B,lw=2);ax.plot(angle,np.where(val<0,abs(val),np.nan),color=R,lw=2)
    ax.set_theta_zero_location('N');ax.set_title(f'ℓ={ell}',pad=15);ax.set(ylim=(0,1.05),xticks=np.arange(0,2*np.pi,np.pi/2),yticks=[.5,1]);ax.set_yticklabels([]);ax.tick_params(labelsize=8)
fig.suptitle('轴对称角向因子：蓝为非负、红为负，半径为绝对值',fontsize=17,fontweight='bold');save(fig,'angular-modes')
# 8 Heat convolution of normalized Gaussian.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));space=np.linspace(-1.5,1.5,1001);k=np.linspace(-15,15,701)
for t,col in [(0,M),(.05,B),(.2,G),(.5,R)]:
    ax[0].plot(space,model.gaussian(space,t),color=col,label=f't={t:g} s',lw=2)
    ax[1].plot(k,np.exp(-.1*k*k*t),color=col,label=f't={t:g} s',lw=2)
ax[0].set(xlabel='位置 / m',ylabel='归一化密度 / m⁻¹',title='（a）总积分为1，方差增加');ax[0].legend(fontsize=10)
ax[1].set(xlabel='空间角波数 k / rad·m⁻¹',ylabel='扩散乘子 exp(−Dk²t)',title='（b）高波数衰减更快');ax[1].legend(fontsize=10)
fig.suptitle('热核与傅里叶变换：展宽与高频平滑是同一过程',fontsize=18,fontweight='bold');save(fig,'heat-kernel')
# 9 Green function and source integral.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for xi,col in [(.3,B),(.5,G),(.7,R)]:ax[0].plot(x,model.green(x,xi),color=col,label=f'ξ/L={xi:g}',lw=2)
ax[0].set(xlabel='x / L',ylabel='G / L',title='（a）G连续，源点斜率跳跃−1');ax[0].legend()
xx2=np.linspace(0,1,41);xi=np.linspace(0,1,10001)
integral=np.array([np.trapz(model.green(xx,xi),xi) for xx in xx2])
ax[1].plot(x,x*(1-x)/2,color=B,label='解析解 x(1−x)/2',lw=2);ax[1].scatter(xx2[::2],integral[::2],color=R,s=20,label='对单位源的核积分',zorder=3)
ax[1].set(xlabel='x / L',ylabel='u / (f₀L²)',title='（b）−u″=f₀，零端点');ax[1].legend(fontsize=10)
fig.suptitle('格林函数：把点源响应叠成分布源响应',fontsize=18,fontweight='bold');save(fig,'green-function')
# 10 Grid convergence and discrete phase velocity.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ms=np.array([10,20,40,80,160])
errors=np.pi**2-4*ms**2*np.sin(np.pi/(2*ms))**2
ax[0].loglog(ms,errors,'o-',color=B,label='第一特征值绝对误差');ax[0].loglog(ms,errors[0]*(ms[0]/ms)**2,'--',color=M,label='M⁻²参考线')
ax[0].set(xlabel='单元数 M',ylabel='|λ₁ʰ−π²|（L=1）',title='（a）空间中心差分二阶收敛');ax[0].legend(fontsize=9)
kh=np.linspace(.001,np.pi,1001)
for nu,col in [(.3,R),(.7,G),(1.,B)]:
    ratio=2*np.arcsin(nu*np.sin(kh/2))/(nu*kh);ax[1].plot(kh/np.pi,ratio,color=col,label=f'ν={nu:g}',lw=2)
ax[1].set(xlabel='归一化空间波数 kΔx / π',ylabel='数值相速度 / c',title='（b）稳定格式仍可能有色散');ax[1].legend()
fig.suptitle('网格与时间步：分别核对收敛、稳定与色散',fontsize=18,fontweight='bold');save(fig,'numerical-checks')
# Course line sketch: circular nodal pattern plus separated 1D basis.
thumb=ROOT/'public/figures/foundation-courses/mathematical-physics-methods.svg'
thumb.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180"><rect width="320" height="180" fill="#f2f0f7"/><g fill="none" stroke="#7c7091" stroke-width="2.2"><ellipse cx="106" cy="91" rx="65" ry="49"/><ellipse cx="106" cy="91" rx="31" ry="23" stroke-dasharray="4 4"/><path d="M41 91h130M106 42v98M54 63q52 30 104 0M54 119q52-30 104 0"/></g><g fill="none" stroke="#437b91" stroke-width="2.4"><path d="M204 63q16-33 32 0t32 0M204 91q8-23 16 0t16 0t16 0t16 0M204 119q16 30 32 0t32 0"/></g><path d="M194 44v99m0-2h89" stroke="#aaa1b5" fill="none" stroke-width="1.5"/></svg>\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(model.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,thumbnail=True,summary=model.summary()),ensure_ascii=True))
