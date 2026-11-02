"""Original numerical-analysis figures, explicit models and raster previews."""
from pathlib import Path
import sys,importlib.util,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/numerical-analysis/experiments.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/numerical-analysis';PRE=ROOT/'artifacts/numerical-analysis/figures';REC=ROOT/'docs/research/numerical-analysis-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'numerical-analysis','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创数值分析教学图 · 指定计算模型，非听者或器件实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    p=FIG/(name+'.svg');fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
# 1 Cancellation vs a dedicated elementary function.
x,a,b,ea,eb=m.cancellation();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
ax[0].semilogx(x,a/x,color=R,lw=1.7,label='log(1+x) / x');ax[0].semilogx(x,b/x,color=B,lw=1.8,label='log1p(x) / x')
ax[0].set(xlabel='x／无量纲',ylabel='计算输出 / x',title='（a）小x处，直接公式可能先丢掉x',ylim=(-.08,2.05));ax[0].legend(fontsize=10)
ax[1].loglog(x,np.maximum(ea,1e-20),color=R,lw=1.7,label='直接公式');ax[1].loglog(x,np.maximum(eb,1e-20),color=B,lw=1.7,label='log1p')
ax[1].set(xlabel='x／无量纲',ylabel='相对误差',title='（b）80位Decimal参考，同一输入');ax[1].legend(fontsize=10)
fig.suptitle('有限精度：代数等价不保证数值表现相同',fontsize=18,fontweight='bold');save(fig,'cancellation')
# 2 Small residual but large forward error.
d=m.condition_demo();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for key,col,label in [('forward',R,'相对解误差 ≈ 0.707'),('relative_residual',B,'相对残差'),('scaled_residual',G,'归一化残差 η')]:
    ax[0].loglog(d['delta'],d[key],color=col,lw=2,label=label)
ax[0].set(xlabel='小参数 δ',ylabel='相对量／无量纲',title='（a）A=diag(1,δ)，近似解(1,0)');ax[0].legend(fontsize=9)
theta=np.linspace(0,2*np.pi,1001);ax[1].plot(np.cos(theta),np.sin(theta),color=B,lw=2,label='输入单位圆')
ax[1].plot(np.cos(theta),.15*np.sin(theta),color=R,lw=2,label='A作用后：δ=0.15')
ax[1].axhline(0,color=M,lw=.5);ax[1].axvline(0,color=M,lw=.5);ax[1].set(aspect='equal',xlabel='第一坐标',ylabel='第二坐标',title='（b）不同方向的放大不同');ax[1].legend(fontsize=9)
fig.suptitle('小残差需要结合条件性解释',fontsize=18,fontweight='bold');save(fig,'conditioning-residual')
# 3 Weakly identifiable coefficients in a deliberately almost-collinear tone basis.
d=m.least_squares();fig,ax=plt.subplots(1,2,figsize=(14,5.5));sel=d['t']<=.004
ax[0].plot(d['t'][sel]*1000,d['A'][sel,0],color=B,lw=2,label='1000 Hz')
ax[0].plot(d['t'][sel]*1000,d['A'][sel,1],color=R,lw=1.6,ls='--',label='1000.0001 Hz')
ax[0].set(xlabel='时间 / ms',ylabel='基函数／无量纲',title='（a）16 ms记录，只放大前4 ms');ax[0].legend(fontsize=10)
loc=np.arange(2);width=.24
for offset,key,col,label in [(-width,'true',M,'指定真值'),(0,'perturbed',R,'小扰动后的QR'),(width,'ridge',G,'正则化 λ=10⁻⁴')]:
    ax[1].bar(loc+offset,d[key],width,color=col,alpha=.85,label=label)
ax[1].axhline(0,color=M,lw=.7);ax[1].set(xticks=loc,xticklabels=['第一项系数','第二项系数'],ylabel='系数 / Pa',title='（b）输出扰动范数仅10⁻⁴ Pa');ax[1].legend(fontsize=9)
fig.suptitle('拟合输出接近，不保证系数已可靠辨认',fontsize=18,fontweight='bold');save(fig,'least-squares')
# 4 Local Newton convergence vs an exact two-cycle.
d=m.roots();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for key,col,label in [('bisection',M,'二分法'),('fixed',G,'固定点 cos x'),('newton',B,'Newton')]:
    vals=d[key];ax[0].semilogy(np.arange(len(vals)),np.maximum(abs(vals-d['root']),1e-16),color=col,lw=1.8,marker='o',ms=2.5,label=label)
ax[0].set(xlabel='各方法的序列索引',ylabel='相对参考根的绝对差',title='（a）cos x−x：不同收敛行为');ax[0].legend(fontsize=10)
x=np.linspace(-2.05,1.4,1001);ax[1].plot(x,x**3-2*x+2,color=B,lw=2,label='x³−2x+2')
tt=np.linspace(-.15,1.2,100);ax[1].plot(tt,2-2*tt,color=R,ls='--',lw=1.7,label='x=0处切线');ax[1].plot(tt,tt,color=G,ls=':',lw=2,label='x=1处切线')
ax[1].scatter([0,1],[2,1],color=[R,G],zorder=4);ax[1].scatter([0,1],[0,0],color=[G,R],marker='x',s=50,zorder=4)
ax[1].axhline(0,color=M,lw=.7);ax[1].set(ylim=(-3,4),xlabel='x／无量纲',ylabel='函数值',title='（b）Newton初值0：0 → 1 → 0');ax[1].legend(fontsize=9,loc='lower right')
fig.suptitle('Newton的快速性不能当作全局收敛保证',fontsize=18,fontweight='bold');save(fig,'root-iteration')
# 5 Runge phenomenon, analytic barycentric weights, complete common scale.
x=np.linspace(-1,1,10001);truth=1/(1+25*x*x);fig,ax=plt.subplots(1,2,figsize=(14,5.5))
ax[0].plot(x,truth,color=M,lw=2,label='Runge函数')
for cheb,col,label in [(False,R,'20次等距插值'),(True,B,'20次Chebyshev–Lobatto')]:
    _,_,p=m.runge(20,cheb);ax[0].plot(x,p(x),color=col,lw=1.5,label=label)
ax[0].set(xlabel='x／无量纲',ylabel='函数值',title='（a）相同次数，共用完整纵轴');ax[0].legend(fontsize=8)
rows=m.runge_errors()
for key,col,label in [('equally_spaced',R,'等距节点'),('Chebyshev_Lobatto',B,'Chebyshev–Lobatto节点')]:
    ax[1].semilogy([r['degree'] for r in rows],[r[key] for r in rows],color=col,lw=2,marker='o',ms=4,label=label)
ax[1].set(xlabel='插值次数 n',ylabel='10001点检验网格最大绝对误差',title='（b）次数增加可能使误差变大');ax[1].legend(fontsize=9)
fig.suptitle('插值：节点设计与求值算法分别检查',fontsize=18,fontweight='bold');save(fig,'interpolation-nodes')
# 6 Shape constraints and smoothness.
x,y,z,cs,pc=m.splines();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for fn,col,label in [(cs,R,'自然三次样条 C²'),(pc,B,'PCHIP C¹')]:
    ax[0].plot(z,fn(z),color=col,lw=2,label=label);ax[1].plot(z,fn(z,1),color=col,lw=2,label=label)
ax[0].scatter(x,y,color='black',s=35,zorder=4,label='四个单调非负节点')
for a in ax:a.axhline(0,color=M,lw=.7,ls='--');a.set_xlabel('x／无量纲');a.legend(fontsize=9)
ax[0].set(ylabel='插值值',title='（a）自然样条出现负值与局部下降')
ax[1].set(ylabel='一阶导数',title='（b）导数为负，表示该区间下降')
fig.suptitle('更光滑不自动满足所需形状约束',fontsize=18,fontweight='bold');save(fig,'spline-shape')
# 7 A narrow peak that defeats both coarse grids and an uninformed adaptive call.
d=m.narrow_integral();f=d['function'];fig,ax=plt.subplots(1,2,figsize=(14,5.5));xx=np.linspace(.34,.4,3001);coarse=np.arange(17)/16
ax[0].plot(xx,f(xx),color=B,lw=2,label='指定窄峰');ax[0].scatter(coarse,f(coarse),color=R,s=38,label='16区间网格样点',zorder=4)
ax[0].set(xlim=(.34,.4),xlabel='x／无量纲',ylabel='g(x)',title='（a）局部放大：粗网格未分辨峰');ax[0].legend(fontsize=9)
ax[1].semilogx([r['intervals'] for r in d['rows']],[r['value'] for r in d['rows']],base=2,color=B,lw=2,marker='o',label='复合梯形积分')
ax[1].axhline(d['exact'],color=M,ls='--',label='解析参考 ≈ 0.00177245')
ax[1].set(xlabel='等宽小区间数 N',ylabel='积分值／无量纲',title='（b）分辨峰之后才可靠');ax[1].legend(fontsize=9,loc='lower right')
fig.suptitle('误差估计与网格比较，也可能共同漏掉局部结构',fontsize=18,fontweight='bold');save(fig,'narrow-quadrature')
# 8 Stiffness: seconds are used in the ODE; omega=1 rad/s and a=1000/s.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));fine=np.linspace(0,.03,2001)
ax[0].plot(fine*1000,np.cos(fine)-np.exp(-1000*fine),color=M,lw=2.5,label='解析解')
for h,implicit,col,label in [(.001,False,B,'显式Euler 1 ms'),(.01,True,G,'隐式Euler 10 ms')]:
    t,y=m.stiff_euler(h,implicit);sel=t<=.03+1e-12;ax[0].plot(t[sel]*1000,y[sel],color=col,lw=1.5,marker='o',ms=4,label=label)
ax[0].set(xlabel='时间 / ms',ylabel='输出／无量纲',title='（a）起始1 ms暂态需要足够时间分辨');ax[0].legend(fontsize=9)
for h,implicit,col,label in [(.001,False,B,'显式Euler 1 ms'),(.01,True,G,'隐式Euler 10 ms'),(.01,False,R,'显式Euler 10 ms')]:
    t,y=m.stiff_euler(h,implicit);err=abs(y-(np.cos(t)-np.exp(-1000*t)))
    ax[1].semilogy(t,np.maximum(err,1e-16),color=col,lw=1.5,label=label)
ax[1].set(xlabel='时间 / s',ylabel='绝对误差／对数轴',title='（b）数值增长不来自原模型');ax[1].legend(fontsize=9,loc='center left')
fig.suptitle('刚性：稳定性限制与精度要求不一定一致',fontsize=18,fontweight='bold');save(fig,'stiff-integration')
# 9 Known exact BVP and asymptotic second order.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x,y,err,res=m.bvp(16);fine=np.linspace(0,1,1001)
ax[0].plot(fine,np.sin(np.pi*fine),color=M,lw=2.5,label='解析 sin(πx)')
ax[0].plot(np.r_[0,x,1],np.r_[0,y,0],color=B,lw=1.4,marker='o',ms=4,label='16区间差分解')
ax[0].set(xlabel='x／无量纲',ylabel='u／无量纲',title='（a）零端值与内部离散一起定义问题');ax[0].legend(fontsize=9)
Ns=np.array([16,32,64,128]);hs=1/Ns;errors=np.array([m.bvp(int(n))[2] for n in Ns])
ax[1].loglog(hs,errors,color=B,lw=2,marker='o',label='网格最大绝对误差');ax[1].loglog(hs,np.pi**2/12*hs**2,color=R,ls='--',label='π²h²/12参考趋势')
ax[1].set(xlabel='网格间隔 h／无量纲',ylabel='最大绝对误差',title='（b）加密一倍，误差约降至1/4');ax[1].legend(fontsize=9)
fig.suptitle('解准离散方程，还要检查连续离散误差',fontsize=18,fontweight='bold');save(fig,'boundary-grid')
# 10 Euclidean residuals may be nonmonotone; both final errors shown.
A,b,rows=m.cg_demo();fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for row,col in zip(rows,[R,B]):
    ax[0].semilogy(np.arange(1,row['iterations']+1),row['residual'],color=col,lw=1.1,label=row['name']+f"：{row['iterations']}步")
ax[0].axhline(1e-10,color=M,ls='--',lw=1,label='相对残差停止阈值')
ax[0].set(xlabel='迭代次数',ylabel='‖b−Axₖ‖₂ / ‖b‖₂',title='（a）80维正定系统，float64');ax[0].legend(fontsize=9)
loc=np.arange(2)
for offset,key,col,label in [(-.17,'final_relative_residual',G,'最终相对残差'),(.17,'relative_forward_error',P,'相对真解误差')]:
    ax[1].bar(loc+offset,[r[key] for r in rows],.34,color=col,label=label)
ax[1].set_yscale('log');ax[1].set(xticks=loc,xticklabels=['CG','Jacobi预条件CG'],ylabel='相对量／对数轴',title='（b）同时核对已知真解');ax[1].legend(fontsize=9)
fig.suptitle('预条件迭代：矩阵性质、停止规则与真实误差一起报告',fontsize=18,fontweight='bold');save(fig,'preconditioned-cg')
(REC/'calculations.json').write_text(json.dumps(m.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sketch=ROOT/'public/figures/foundation-courses/numerical-analysis.svg'
sketch.write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180" role="img" aria-labelledby="t d">
<title id="t">数值分析简笔画</title><desc id="d">左侧离散网格上的折线近似，右侧包含同一目标点的区间逐步缩小。</desc>
<rect width="320" height="180" fill="#f3f1f8"/>
<g fill="none" stroke="#79639d" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
<path d="M22 132h117M29 137V35M34 121L54 94L74 74L94 61L114 54L134 50"/>
<path d="M186 66h116m-116-7v14m116-14v14M207 93h78m-78-7v14m78-14v14M232 120h35m-35-7v14m35-14v14"/>
<path d="M251 45v91" stroke="#31755e" stroke-dasharray="4 5"/>
</g><g fill="#79639d"><circle cx="34" cy="121" r="3"/><circle cx="54" cy="94" r="3"/><circle cx="74" cy="74" r="3"/><circle cx="94" cy="61" r="3"/><circle cx="114" cy="54" r="3"/><circle cx="134" cy="50" r="3"/></g>
<g font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#61727d" text-anchor="middle"><text x="83" y="158">网格近似</text><text x="245" y="158">迭代收敛</text></g></svg>
''',encoding='utf-8')
