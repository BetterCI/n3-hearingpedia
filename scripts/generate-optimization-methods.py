"""Generate original, reproducible teaching plots and the native SVG course sketch."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('optmodels',ROOT/'public/code/optimization-methods/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/optimization-methods';PRE=ROOT/'artifacts/optimization-methods/figures';REC=ROOT/'docs/research/optimization-methods-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'optimization-methods','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def canvas(title):
    fig,ax=plt.subplots(1,2,figsize=(14,5.5))
    fig.suptitle(title,fontsize=18,fontweight='bold')
    return fig,ax
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创最优化教学图 · 指定数学模型，非听者或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(l.rstrip() for l in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Feasible set, projection and the global lower bound.
fig,ax=canvas('先写清可行域，再讨论“最小”')
x,y=np.meshgrid(np.linspace(-.2,2.6,200),np.linspace(-.2,2.3,200))
f=.5*((x-2)**2+(y-1)**2)
ax[0].contour(x,y,f,levels=[.25,.5,1,2],colors=B,alpha=.7)
ax[0].fill([0,2,0],[0,0,2],color=G,alpha=.17,label='x₁,x₂≥0，x₁+x₂≤2')
ax[0].plot([2,1.5],[1,.5],'o--',color=R,label='无约束(2,1) → 可行最优(1.5,0.5)')
ax[0].set(xlabel='x₁／无量纲',ylabel='x₂／无量纲',aspect='equal',title='（a）最近点在预算边界');ax[0].legend(fontsize=9,loc='upper right')
mu=np.linspace(0,1,300)
ax[1].plot(mu,mu-mu**2,color=B,lw=2,label='对偶下界 q(μ)=μ−μ²')
ax[1].axhline(.25,color=R,ls='--',label='可行点目标 p*=0.25')
ax[1].plot([.5],[.25],'o',color=G)
ax[1].set(xlabel='乘子 μ≥0',ylabel='无量纲目标或下界',title='（b）μ=0.5 时上下界相接');ax[1].legend(fontsize=10)
save(fig,'feasible-dual')
# 2 Stationary points are not all minima.
fig,ax=canvas('驻点只是候选：还要检查曲率和其他可行点')
z=np.linspace(-1.5,1.5,500);nc=m.nonconvex()
ax[0].plot(z,(z*z-1)**2+.3*z,color=B,lw=2)
ax[0].scatter(nc['roots'],nc['values'],color=[G,R,P],zorder=3)
for xx,yy,label in zip(nc['roots'],nc['values'],['全局极小','局部极大','另一局部极小']):
    ax[0].annotate(label,(xx,yy),xytext=(0,17),textcoords='offset points',ha='center',fontsize=10)
ax[0].set(xlabel='x／无量纲',ylabel='f(x)',title='（a）f(x)=(x²−1)²+0.3x',ylim=(-.5,2))
xx,yy=np.meshgrid(np.linspace(-1,1,180),np.linspace(-1,1,180))
ax[1].contour(xx,yy,xx*xx-yy*yy,levels=[-.8,-.3,0,.3,.8],colors=[R,R,M,B,B])
ax[1].plot(0,0,'o',color=P);ax[1].annotate('原点梯度为零\n沿x上升，沿y下降',(0,0),xytext=(.2,.35),arrowprops={'arrowstyle':'->','color':M})
ax[1].set(xlabel='x／无量纲',ylabel='y／无量纲',aspect='equal',title='（b）f(x,y)=x²−y² 的鞍点')
save(fig,'stationary-points')
# 3 Exact iteration factors.
fig,ax=canvas('梯度下降：方向正确，还需要合适的步长')
xx,yy=np.meshgrid(np.linspace(-.1,3.3,200),np.linspace(-1.2,1.2,200))
ax[0].contour(xx,yy,.5*(xx**2+20*yy**2),levels=[.2,.8,2,5,10,16],colors=M,alpha=.5)
for a,col in [(.05,G),(.09,B)]:
    path=m.gradient(a);ax[0].plot(path[:,0],path[:,1],'o-',color=col,ms=2,label=f'α={a}')
ax[0].set(xlabel='x₁',ylabel='x₂',title='（a）二次目标，H=diag(1,20)');ax[0].legend()
for a,col in [(.05,G),(.09,B),(.105,R)]:
    p=m.gradient(a);val=.5*(p[:,0]**2+20*p[:,1]**2)
    ax[1].semilogy(np.arange(len(val)),val,color=col,lw=2,label=f'α={a}')
ax[1].set(xlabel='迭代次数 k',ylabel='目标差 f(xₖ)−f*',title='（b）稳定区间 0<α<0.1');ax[1].legend()
save(fig,'gradient-step')
# 4 Newton solves a quadratic; an indefinite Hessian can send it uphill.
fig,ax=canvas('Newton方法使用曲率；负曲率需要保护')
gd=m.gradient(.05,20);ax[0].semilogy(np.arange(21),np.linalg.norm(gd,axis=1),color=B,label='梯度下降 α=0.05')
ax[0].scatter([0,1],[np.sqrt(10),1e-14],color=G,label='二次型Newton：1步到解')
ax[0].annotate('精确值为0；仅绘在10⁻¹⁴',(1,1e-14),xytext=(3,1e-11),fontsize=9)
ax[0].set(xlabel='迭代次数 k',ylabel='距最优点的2范数',title='（a）正定二次型的特例');ax[0].legend(fontsize=10)
z=np.linspace(-.05,.25,300);v=lambda t:(t*t-1)**2+.3*t
x0=.1;g=4*x0**3-4*x0+.3;h=12*x0*x0-4;p=-g/h
ax[1].plot(z,v(z),color=B,lw=2,label='真实目标')
ax[1].plot(z,v(x0)+g*(z-x0)+.5*h*(z-x0)**2,color=M,ls='--',label='局部二次近似')
ax[1].plot([x0,x0+p],[v(x0),v(x0+p)],'o-',color=R,label='负Hessian的Newton步')
ax[1].set(xlabel='x／无量纲',ylabel='f(x)',title='（b）x=0.1：该步反而升高目标');ax[1].legend(fontsize=9)
save(fig,'newton-curvature')
# 5 A normalized exponential response, not a measured room or neural response.
d=m.nonlinear_fit();fig,ax=canvas('非线性最小二乘：拟合输出和参数证据分开看')
ax[0].plot(d['u'],d['y'],'o',ms=4,color=M,label='指定教学数据')
ax[0].plot(d['u'],d['prediction'],color=B,lw=2,label='有界TRF拟合')
ax[0].plot(d['u'],np.exp(-2*d['u']),color=G,ls='--',label='生成基线 exp(−2u)')
ax[0].set(xlabel='归一化时间 u=t/T，T=1 s',ylabel='归一化响应',title='（a）a exp(−bu)，a,b为无量纲参数');ax[0].legend(fontsize=9)
ax[1].axhline(0,color=M,lw=.7);ax[1].plot(d['u'],d['residual'],'o-',ms=3,color=R)
ax[1].set(xlabel='u／无量纲',ylabel='模型−数据',title='（b）小残差仍可保留系统形状')
save(fig,'nonlinear-least-squares')
# 6 Active sets and sensitivity.
cs=np.linspace(.05,4,400);xs=np.array([m.budget_solution(c)[0] for c in cs]);mus=np.array([m.budget_solution(c)[1] for c in cs])
cost=.5*np.sum((xs-np.array([2,1]))**2,axis=1)
fig,ax=canvas('约束何时起作用：预算改变会切换活跃集')
for j,col in [(0,B),(1,G)]:ax[0].plot(cs,xs[:,j],color=col,lw=2,label=f'x{j+1}*')
for a in ax:a.axvline(1,color=M,ls=':',lw=1);a.axvline(3,color=M,ls=':',lw=1)
ax[0].set(xlabel='预算 c／无量纲',ylabel='最优坐标',title='（a）c=1、3 是切换点');ax[0].legend()
ax[1].plot(cs,cost,color=B,lw=2,label='最优值 v(c)')
ax[1].plot(cs,mus,color=R,ls='--',lw=2,label='预算乘子 μ(c)')
ax[1].set(xlabel='预算 c／无量纲',ylabel='v(c) 或 μ(c)',title='（b）本例可微，v′(c)=−μ(c)');ax[1].legend()
save(fig,'active-budget')
# 7 Finite penalty violates the constraint; barrier remains strictly inside.
rho=np.logspace(-1,4,300);tau=np.logspace(-4,1,300)
fig,ax=canvas('罚函数和障碍法：有限参数下求的是不同问题')
ax[0].semilogx(rho,(2+rho)/(1+rho),color=R,lw=2,label='二次罚函数解')
ax[0].axhline(1,color=G,ls='--',label='原问题可行最优 x*=1')
ax[0].set(xlabel='罚参数 ρ>0',ylabel='xρ',title='（a）任何有限ρ，xρ>1，仍违反约束');ax[0].legend(fontsize=10)
ax[1].semilogx(tau,(3-np.sqrt(1+4*tau))/2,color=B,lw=2,label='对数障碍解')
ax[1].axhline(1,color=G,ls='--',label='原问题边界')
ax[1].set(xlabel='障碍权重 τ>0（趋零时靠近边界）',ylabel='xτ',title='（b）障碍解始终满足 xτ<1');ax[1].legend(fontsize=10)
save(fig,'penalty-barrier')
# 8 L1 versus L2 and their different objectives.
fig,ax=canvas('不可导也能精确处理：L1近端映射是软阈值')
z=np.linspace(-1.5,1.5,400)
ax[0].plot(z,z,color=M,ls=':',label='不惩罚：x=z')
ax[0].plot(z,m.soft(z,.2),color=B,lw=2,label='L1：S₀.₂(z)')
ax[0].plot(z,z/1.2,color=R,lw=1.8,label='L2：z/1.2')
ax[0].set(xlabel='输入 z／无量纲',ylabel='一维最优 x',title='（a）L1有归零区间');ax[0].legend(fontsize=9)
b=np.array([1.2,.15,-.08]);loc=np.arange(3);w=.24
for off,v,col,label in [(-w,b,M,'输入b'),(0,m.soft(b,.2),B,'L1 λ=0.2'),(w,b/1.2,R,'L2 λ=0.2')]:ax[1].bar(loc+off,v,w,color=col,label=label)
ax[1].axhline(0,color=M,lw=.5);ax[1].set(xticks=loc,xticklabels=['第一项','第二项','第三项'],ylabel='系数／无量纲',title='（b）单位设计矩阵，两个明确目标');ax[1].legend(fontsize=9)
save(fig,'proximal-threshold')
# 9 The stochastic model has a closed-form second moment.
d=m.sgd();fig,ax=canvas('随机梯度：单次下降和平均收敛是不同问题')
ax[0].plot(d['k'],d['fixed_path'],color=R,alpha=.8,label='固定 α=0.1，1条轨迹')
ax[0].plot(d['k'],d['decreasing_path'],color=B,label='递减 αₖ=1/k，同一噪声')
ax[0].axhline(0,color=M,lw=.5);ax[0].set(xlabel='更新次数 k',ylabel='xₖ',title='（a）gₖ=xₖ+ξₖ，ξₖ独立取±1');ax[0].legend(fontsize=9)
for key,theory,col,label in [('fixed_mse','fixed_theory',R,'固定步长'),('decreasing_mse','decreasing_theory',B,'递减步长')]:
    ax[1].loglog(d['k'][1:],d[key][1:],color=col,alpha=.7,label=label+'：512次平均')
    ax[1].loglog(d['k'][1:],d[theory][1:],color=col,ls='--',lw=2,label=label+'：精确期望')
ax[1].set(xlabel='更新次数 k',ylabel='E[xₖ²] 的理论或样本均值',title='（b）固定步长均方平台 ≈0.05263');ax[1].legend(fontsize=9)
save(fig,'stochastic-gradient')
# 10 Scaling and absolute tolerance.
fig,ax=canvas('缩放与停止条件会改变“看起来已收敛”的判断')
k=np.arange(1001);raw=m.gradient(1e-4,1000,(1,1),(1,1e4))
ax[0].semilogy(k,np.maximum(np.linalg.norm(raw,axis=1)/np.sqrt(2),1e-14),color=R,label='原坐标GD：α=10⁻⁴')
ax[0].plot([0,1,1000],[1,1e-14,1e-14],color=G,label='z=(x₁,100x₂)：α=1')
ax[0].annotate('缩放后精确解误差0；绘图下限10⁻¹⁴',(130,1e-13),fontsize=9)
ax[0].set(xlabel='更新次数 k',ylabel='原坐标相对2范数误差',title='（a）H条件数从10⁴变为1');ax[0].legend(fontsize=9)
eps=np.array([1,1e-6,1e-12]);ax[1].semilogy(range(3),np.sqrt(2)*eps,'o-',color=B,label='同一点(1,1)的梯度范数')
ax[1].axhline(1e-8,color=R,ls='--',label='任意指定绝对阈值10⁻⁸')
ax[1].set(xticks=range(3),xticklabels=['1','10⁻⁶','10⁻¹²'],xlabel='目标乘数 ε；fε(x)=ε‖x‖²/2',ylabel='‖∇fε(1,1)‖₂',title='（b）最优点始终为0，误差始终√2');ax[1].legend(fontsize=9)
save(fig,'scaling-stopping')
sketch='''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="200" viewBox="0 0 320 200" role="img" aria-labelledby="title desc"><title id="title">最优化方法：等高线上的下降路径与可行边界</title><desc id="desc">简笔画用椭圆等高线、折线箭头和约束边界表示沿搜索路径接近一个可行最优点。</desc><rect width="320" height="200" rx="18" fill="#f6f1e7"/><g fill="none" stroke="#537586" stroke-width="2"><ellipse cx="182" cy="105" rx="105" ry="63" transform="rotate(-18 182 105)"/><ellipse cx="182" cy="105" rx="73" ry="43" transform="rotate(-18 182 105)"/><ellipse cx="182" cy="105" rx="37" ry="22" transform="rotate(-18 182 105)"/></g><path d="M52 169L252 43" stroke="#32765c" stroke-width="3" stroke-dasharray="7 5"/><path d="M61 58L125 135L144 82L169 115L181 104" stroke="#b44e37" stroke-width="3" fill="none" stroke-linejoin="round"/><path d="M171 104L181 104L180 114" stroke="#b44e37" stroke-width="3" fill="none"/><circle cx="181" cy="104" r="5" fill="#32765c"/><g fill="#b44e37"><circle cx="61" cy="58" r="3"/><circle cx="125" cy="135" r="3"/><circle cx="144" cy="82" r="3"/><circle cx="169" cy="115" r="3"/></g></svg>'''
(ROOT/'public/figures/foundation-courses/optimization-methods.svg').write_text(sketch+'\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2,default=m.serial)+'\n',encoding='utf-8')
print('Generated 10 original SVGs, 10 PNG previews, 1 course sketch and calculations.json.')
