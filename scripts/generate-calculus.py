"""Generate original scientific SVG figures, PNG previews and a native course sketch."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/calculus/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/calculus';PRE=ROOT/'artifacts/calculus/figures';REC=ROOT/'docs/research/calculus-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'calculus','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创微积分教学图 · 指定函数与模型，非听者或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Formal limit and a changed point value.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(.5,1.5,1001)
ax[0].axhspan(.7,1.3,color=G,alpha=.12,label='输出误差带：1±0.3')
ax[0].axvspan(.9,1.1,color=P,alpha=.16,label='输入邻域：1±0.1')
ax[0].plot(x,x*x,color=B,lw=2,label='f(x)=x²');ax[0].scatter([1],[1],color=B,zorder=4)
ax[0].set(title='（a）ε=0.3，δ=0.1满足要求',xlabel='输入 x／无量纲',ylabel='输出 f(x)／无量纲',xlim=(.5,1.5),ylim=(.2,2.4));ax[0].legend(fontsize=9)
ax[1].plot(x,x*x,color=B,lw=2);ax[1].scatter([1],[1],facecolors='white',edgecolors=B,s=70,zorder=4,label='附近趋于1，此点未取')
ax[1].scatter([1],[1.6],color=R,s=50,zorder=5,label='实际f(1)=1.6');ax[1].set(title='（b）只改点值：极限仍为1，但不连续',xlabel='输入 x／无量纲',ylabel='输出 f(x)／无量纲',xlim=(.5,1.5),ylim=(.2,2.4));ax[1].legend(fontsize=9)
fig.suptitle('极限看附近的行为，连续还要等于点值',fontsize=18,fontweight='bold');save(fig,'limit-continuity')
# 2 Gaussian pulse secants and derivative, all time computations in seconds.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(-.006,.008,1201);a,hs,slopes,true=m.secants()
ax[0].plot(t*1000,m.pulse(t),color=B,lw=2,label='p(t)／Pa')
tt=np.linspace(.0005,.005,101)
for h,s,col in zip(hs[:3],slopes[:3],[G,P,R]):
    ax[0].plot(np.array([a,a+h])*1000,[m.pulse(a),m.pulse(a+h)],color=col,lw=2,label=f'割线 h={h*1000:g} ms')
ax[0].plot(tt*1000,m.pulse(a)+true*(tt-a),color=M,ls='--',lw=1.8,label='切线')
ax[0].scatter([a*1000],[m.pulse(a)],color='black',s=30,zorder=5)
ax[0].set(xlim=(-2,6),ylim=(-.3,1.1),xlabel='时间 / ms',ylabel='声压 / Pa',title='（a）2 ms处，右侧割线趋近切线');ax[0].legend(fontsize=9)
ax[1].plot(t*1000,m.pulse_derivative(t),color=B,lw=2);ax[1].axhline(0,color=M,lw=.7);ax[1].scatter([2],[true],color=R,zorder=4,label=f'2 ms：{true:.2f} Pa/s')
ax[1].set(xlabel='时间 / ms',ylabel='声压变化率 / Pa·s⁻¹',title='（b）先上升后下降，峰顶导数为0');ax[1].legend(fontsize=10)
fig.suptitle('导数：差商的极限与局部变化率',fontsize=18,fontweight='bold');save(fig,'derivative-pulse')
# 3 Taylor and remainder.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));u=np.linspace(0,1,501);exact=np.exp(-u)
ax[0].plot(u,exact,color=M,lw=3,label='e⁻ᵘ')
for degree,col in [(1,R),(2,G),(4,B)]:
    value=m.taylor(u,degree);ax[0].plot(u,value,color=col,lw=1.7,label=f'{degree}阶多项式')
    ax[1].semilogy(u,np.maximum(abs(value-exact),1e-15),color=col,lw=1.7,label=f'{degree}阶绝对误差')
ax[1].semilogy(u,np.maximum(u*u/2,1e-15),color=M,ls='--',lw=1.5,label='一阶余项界 u²/2')
ax[0].set(xlabel='u／无量纲',ylabel='函数值／无量纲',title='（a）展开中心0，越远不一定越准确');ax[0].legend(fontsize=9)
ax[1].set(xlabel='u／无量纲',ylabel='绝对误差／无量纲',title='（b）阶数与余项界一同报告',ylim=(1e-15,1));ax[1].legend(fontsize=9)
fig.suptitle('Taylor近似不是没有误差的等式',fontsize=18,fontweight='bold');save(fig,'taylor-remainder')
# 4 Midpoint Riemann rectangles.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));xx=np.linspace(0,1,1001)
for a,N,lab in [(ax[0],4,'a'),(ax[1],16,'b')]:
    for k in range(N):a.add_patch(Rectangle((k/N,0),1/N,((k+.5)/N)**2,fc=B+'22',ec=B,lw=.8))
    a.plot(xx,xx*xx,color=R,lw=2,label='x²');a.set(xlim=(0,1),ylim=(0,1.06),xlabel='x／无量纲',ylabel='函数高度／无量纲',title=f'（{lab}）N={N}，中点和={m.riemann(N):.8f}')
    a.legend(loc='upper left');a.text(.03,.8,'精确积分 = 1/3',transform=a.transAxes,color=M)
fig.suptitle('Riemann和：高度乘宽度，再取网格极限',fontsize=18,fontweight='bold');save(fig,'riemann-sums')
# 5 Signed accumulation; physical pressure and time units.
d=m.cycle();t=d['t'];p=d['p'];fig,ax=plt.subplots(1,2,figsize=(14,5.5))
ax[0].plot(t*1000,p,color=B,lw=2);ax[0].fill_between(t*1000,p,0,where=p>=0,color=G,alpha=.25);ax[0].fill_between(t*1000,p,0,where=p<0,color=R,alpha=.25)
ax[0].axhline(0,color=M,lw=.7);ax[0].set(xlabel='时间 / ms',ylabel='声压 / Pa',title='（a）一周期：正负净累积抵消')
ax[1].plot(t*1000,d['signed'],color=P,lw=2);ax[1].set(xlabel='积分上限 t / ms',ylabel='净累积 F(t) / Pa·s',title='（b）F′(t)=p(t)，终点回到0')
ax[1].ticklabel_format(axis='y',style='sci',scilimits=(0,0))
fig.suptitle('微积分基本定理：累积函数的导数是被积函数',fontsize=18,fontweight='bold');save(fig,'cumulative-cycle')
# 6 Divergence cannot be inferred only from a finite plot.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));Rr=np.logspace(0,3,1000);n=np.arange(1,1001)
ax[0].semilogx(Rr,np.log(Rr),color=R,lw=2,label='∫₁ᴿ 1/x dx = ln R');ax[0].semilogx(Rr,1-1/Rr,color=B,lw=2,label='∫₁ᴿ 1/x² dx = 1−1/R')
ax[0].set(xlabel='截断上限 R／无量纲',ylabel='截断积分／无量纲',title='（a）尾部都趋零，累积行为不同');ax[0].legend(fontsize=9)
ax[1].semilogx(n,np.cumsum(1/n),color=R,lw=2,label='Σ₁ᴺ 1/n');ax[1].semilogx(n,np.cumsum(1/n**2),color=B,lw=2,label='Σ₁ᴺ 1/n²')
ax[1].set(xlabel='项数 N',ylabel='部分和／无量纲',title='（b）单项趋零不是级数收敛的充分条件');ax[1].legend(fontsize=10)
fig.suptitle('反常积分与级数：各自定义累积极限',fontsize=18,fontweight='bold');save(fig,'convergence')
# 7 Multivariable differential and counterexample.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));aa=np.linspace(-1,3,401);bb=np.linspace(-2,2,401);A,Bb=np.meshgrid(aa,bb)
cs=ax[0].contour(A,Bb,m.objective(A,Bb),levels=[.5,1,2,4,6.25,10,15],colors=B,linewidths=1);ax[0].clabel(cs,fontsize=8)
g=m.objective_gradient(2,.25);ax[0].scatter([1,2],[-.5,.25],color=[G,R],s=40,zorder=4)
ax[0].annotate('',xy=np.array([2,.25])+.16*g,xytext=(2,.25),arrowprops={'arrowstyle':'->','color':R,'lw':2.2})
ax[0].text(1,-.7,'最小值',ha='center',color=G);ax[0].text(2.05,1.4,'∇L=(2,6)\n箭头缩短显示',color=R,fontsize=10)
ax[0].set(aspect='equal',xlabel='参数 a／无量纲',ylabel='参数 b／无量纲',title='（a）等高线与指定点的梯度')
v=np.r_[np.linspace(-1,-.001,500),np.nan,np.linspace(.001,1,500)]
ax[1].plot(v,m.partial_counterexample(v,0),color=B,lw=2,label='沿x轴或y轴');ax[1].plot(v,m.partial_counterexample(v,v),color=R,lw=2,label='沿y=x')
ax[1].scatter([0],[.5],facecolors='white',edgecolors=R,s=70,zorder=4);ax[1].scatter([0],[0],color='black',s=35,zorder=4,label='原点值0')
ax[1].set(xlabel='路径参数／无量纲',ylabel='F值／无量纲',ylim=(-.1,.7),title='（b）两个偏导为0，原点仍不连续');ax[1].legend(fontsize=10)
fig.suptitle('偏导存在，不等于所有方向共享线性近似',fontsize=18,fontweight='bold');save(fig,'multivariable')
# 8 Polar Jacobian and radial mass, no normalization as probability.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));q=np.linspace(-3,3,401);xx,yy=np.meshgrid(q,q);rr=np.hypot(xx,yy);field=np.ma.masked_where(rr>3,np.exp(-rr*rr/2))
im=ax[0].imshow(field,extent=(-3,3,-3,3),origin='lower',cmap='viridis',vmin=0,vmax=1,interpolation='nearest')
for radius in np.arange(.5,3.01,.5):ax[0].add_patch(Circle((0,0),radius,fill=False,color='white',alpha=.7,lw=.9))
ax[0].set(aspect='equal',xlabel='x／无量纲',ylabel='y／无量纲',title='（a）等宽圆环的面积并不相等');fig.colorbar(im,ax=ax[0],label='q／无量纲')
r=np.linspace(0,3,501)
ax[1].plot(r,np.exp(-r*r/2),color=B,lw=2,label='局部值 q(r)');ax[1].plot(r,2*np.pi*r*np.exp(-r*r/2),color=R,lw=2,label='圆环密度 2πr q(r)')
ax[1].set(xlabel='半径 r／无量纲',ylabel='值／无量纲',title='（b）∫₀³ 2πr q(r)dr ≈ 6.21339');ax[1].legend(fontsize=10)
fig.suptitle('极坐标积分：函数值必须乘局部面积因子',fontsize=18,fontweight='bold');save(fig,'polar-integral')
# 9 Initial state and forward Euler stability.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));t=np.linspace(0,.03,601)
for y0,col in [(0,B),(.4,R)]:ax[0].plot(t*1000,m.decay_step(t,y0),color=col,lw=2,label=f'y(0)={y0}')
ax[0].axvline(5,color=M,ls=':',label='一个时间常数5 ms');ax[0].set(xlabel='时间 / ms',ylabel='输出／无量纲',title='（a）同一方程，不同初值');ax[0].legend(fontsize=10)
tt=np.linspace(0,.064,1001);ax[1].plot(tt*1000,m.decay_step(tt),color=M,lw=2,ls='--',label='解析解')
for h,col in [(.001,B),(.008,G),(.012,R)]:
    te,ye=m.euler(h);ax[1].plot(te*1000,ye,color=col,marker='o',ms=3,lw=1.5,label=f'Euler h={h*1000:g} ms')
ax[1].set(xlabel='时间 / ms',ylabel='输出／无量纲',title='（b）τ=5 ms，稳定条件0<h<10 ms');ax[1].legend(fontsize=9)
fig.suptitle('模型的稳定性，与数值格式的稳定性分别判断',fontsize=18,fontweight='bold');save(fig,'ode-initial-state')
# 10 Truncation/rounding and independent additive noise.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));h,forward,central=m.difference_errors()
ax[0].loglog(h,np.maximum(forward,1e-16),color=R,lw=1.5,label='前向差分');ax[0].loglog(h,np.maximum(central,1e-16),color=B,lw=1.5,label='中心差分')
ax[0].set(xlabel='步长 h／无量纲',ylabel='对e¹的绝对误差',title='（a）float64：截断与舍入共同影响');ax[0].legend(fontsize=10)
sigma,h,observed,theory=m.noise_difference();ax[1].loglog(h,theory,color=P,lw=2,label='理论 σ/(√2h)');ax[1].scatter(h,observed,color=G,s=35,label='100000对噪声复算',zorder=4)
ax[1].set(xlabel='步长 h／无量纲',ylabel='中心差分噪声标准差',title='（b）两样值独立噪声，σ=10⁻⁶');ax[1].legend(fontsize=10)
fig.suptitle('数值求导：步长越小并不总越可靠',fontsize=18,fontweight='bold');save(fig,'numerical-differentiation')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sketch=ROOT/'public/figures/foundation-courses/calculus.svg'
sketch.write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180" role="img" aria-labelledby="t d">
<title id="t">微积分简笔画</title><desc id="d">左侧用曲线和切线表现导数，右侧用小矩形与阴影面积表现积分。</desc>
<rect width="320" height="180" fill="#f3f1f8"/>
<g stroke="#79639d" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M26 130h112M33 135V36M38 121q34-62 91-67"/><path d="M44 98.10L127 36.99"/><circle cx="77.75" cy="73.25" r="3" fill="#79639d"/>
<path d="M181 130h115M188 135V36"/><path d="M195 130V104h18v26m0 0V81h18v49m0 0V66h18v64m0 0V58h18v72m0 0V54h18v76" fill="#79639d" fill-opacity=".12"/><path d="M195 119q35-66 91-66" stroke="#31755e"/></g>
<g fill="#61727d" font-family="serif" font-size="18" text-anchor="middle"><text x="84" y="159">f′(x)</text><text x="243" y="159">∫ f(x) dx</text></g></svg>
''',encoding='utf-8')
