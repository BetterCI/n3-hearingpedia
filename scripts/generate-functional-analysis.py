"""Original vector teaching figures from specified mathematical models."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/functional-analysis/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
FIG=ROOT/'public/figures/functional-analysis';PRE=ROOT/'artifacts/functional-analysis/figures';REC=ROOT/'docs/research/functional-analysis-2026-11-02'
for d in [FIG,PRE,REC]:d.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'functional-analysis-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创泛函分析教学图 · 指定数学模型，非器件或人体实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    out=FIG/(name+'.svg');fig.savefig(out,metadata={'Date':None},facecolor='white')
    out.write_text('\n'.join(s.rstrip() for s in out.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
t=np.linspace(0,1,2001)
# 1 Unit balls and dimension dependence.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));a=np.linspace(0,2*np.pi,1001);xy=np.array([np.cos(a),np.sin(a)])
for p,col,label in [(1,R,'一范数'),(2,B,'二范数'),(np.inf,G,'无穷范数')]:
    norm=np.max(abs(xy),axis=0) if p==np.inf else np.sum(abs(xy)**p,axis=0)**(1/p)
    q=xy/norm;ax[0].plot(q[0],q[1],color=col,label=label,lw=2)
ax[0].set(aspect='equal',xlabel='x₁',ylabel='x₂',title='（a）二维单位球：不同大小定义');ax[0].legend(fontsize=10)
N=np.arange(1,101);ax[1].plot(N,np.sqrt(N),color=B,lw=2,label='全1向量：二范数 / 最大范数')
ax[1].set(xlabel='维数 N',ylabel='范数比值',title='（b）比较常数可以随维数增长');ax[1].legend(fontsize=10)
fig.suptitle('范数塑造空间的几何与收敛',fontsize=18,fontweight='bold');save(fig,'norm-geometry')
# 2 Incomplete continuous subspace and L2 spike counterexample.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
ax[0].plot(t,(t>.5).astype(float),'--',color=M,label='阶跃极限',lw=2)
for n,col in [(4,R),(8,G),(32,B)]:ax[0].plot(t,model.ramp(t,n),color=col,label=f'n={n}',lw=1.8)
for n,col in [(4,R),(16,G),(64,B)]:ax[1].plot(t,model.spike(t,n),color=col,label=f'n={n}，L²范数²={2/(3*n):.4f}',lw=1.8)
for aa in ax:aa.set(xlabel='归一化时间 t',ylabel='函数值',ylim=(-.05,1.12));aa.legend(fontsize=10)
ax[0].set_title('（a）连续函数在L²中逼近阶跃');ax[1].set_title('（b）范数趋零，峰高仍为1')
fig.suptitle('均方接近与逐点接近需要区分',fontsize=18,fontweight='bold');save(fig,'convergence-and-spikes')
# 3 Orthogonal projection.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
f=model.signal(t);p=model.projection(t)
for val,col,label in [(f,M,'原函数 f'),(p,B,'投影 p'),(f-p,R,'残差 f−p')]:ax[0].plot(t,val,color=col,label=label,lw=1.8)
ax[0].set(xlabel='归一化时间 t',ylabel='函数值',title='（a）三项函数投影到两项子空间');ax[0].legend(fontsize=10)
ax[1].bar(['原函数','投影','残差'],[.6,.58,.02],color=[M,B,R],width=.55)
for i,y in enumerate([.6,.58,.02]):ax[1].text(i,y+.015,f'{y:.2f}',ha='center')
ax[1].set(ylabel='L²平方范数',ylim=(0,.72),title='（b）0.60 = 0.58 + 0.02')
fig.suptitle('最佳近似的残差正交于整个允许子空间',fontsize=18,fontweight='bold');save(fig,'orthogonal-projection')
# 4 Square summability and error tails.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));n=np.arange(1,1001);tail=np.pi**2/6-np.cumsum(1/n**2)
ax[0].loglog(n,1/n,color=B,label='系数 |cₙ|=1/n',lw=2);ax[0].loglog(n,1/n**2,color=G,label='平方 |cₙ|²=1/n²',lw=2)
ax[0].set(xlabel='序号 n',ylabel='系数或平方',title='（a）平方可和不等于绝对可和');ax[0].legend(fontsize=10)
ax[1].loglog(n,tail,color=B,lw=2,label='无限平方尾和')
ax[1].loglog(n,1/n,'--',color=M,label='1/N参考');ax[1].set(xlabel='保留项数 N',ylabel='投影误差平方',title='（b）完整正交基下由尾和给误差');ax[1].legend(fontsize=10)
fig.suptitle('正交展开：完备性与尾部误差',fontsize=18,fontweight='bold');save(fig,'basis-and-tails')
# 5 Derivative and graph norms.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for n,col in [(1,B),(4,G),(12,R)]:ax[0].plot(t,np.sqrt(2)*np.sin(n*np.pi*t),color=col,label=f'n={n}',lw=1.6)
ax[0].set(xlabel='归一化坐标 t',ylabel='eₙ(t)',title='（a）各输入的L²范数都为1');ax[0].legend(fontsize=10)
n=np.arange(1,41)
ax[1].plot(n,np.ones_like(n),color=M,label='输入L²范数')
ax[1].plot(n,n*np.pi,color=R,label='导数L²范数 nπ',lw=2)
ax[1].plot(n,np.sqrt(1+(n*np.pi)**2),'--',color=B,label='图范数 √(1+n²π²)',lw=2)
ax[1].set(xlabel='模态序号 n',ylabel='范数',title='（b）图范数同时控制函数和导数');ax[1].legend(fontsize=9)
fig.suptitle('定义域与范数决定求导是否有界',fontsize=18,fontweight='bold');save(fig,'derivative-and-domain')
# 6 Averaging functionals.
fig,ax=plt.subplots(1,2,figsize=(14,5.5))
for eps,col in [(.5,R),(.2,G),(.05,B)]:
    val=((t>=.5-eps/2)&(t<=.5+eps/2))/eps
    ax[0].plot(t,val,color=col,label=f'窗宽 ε={eps:g}',lw=1.8)
ax[0].set(xlabel='归一化时间 t',ylabel='平均窗 gε(t)',title='（a）每个窗积分为1');ax[0].legend(fontsize=10)
eps=np.logspace(-3,0,301);ax[1].loglog(eps,1/np.sqrt(eps),color=B,lw=2)
ax[1].set(xlabel='窗宽 ε',ylabel='泛函范数 ε⁻¹ᐟ²',title='（b）窄窗平均的L²增益界增加')
fig.suptitle('连续线性泛函：测量必须说明窗口和空间',fontsize=18,fontweight='bold');save(fig,'window-functionals')
# 7 Weak versus strong.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));matrix=np.zeros((6,14))
for i,n in enumerate([1,3,5,7,10,14]):matrix[i,n-1]=1
ax[0].imshow(matrix,aspect='auto',cmap='Blues',vmin=0,vmax=1,extent=[.5,14.5,6.5,.5])
ax[0].set(xlabel='坐标序号',ylabel='选取的序列元素',yticks=np.arange(1,7),yticklabels=['e₁','e₃','e₅','e₇','e₁₀','e₁₄'],title='（a）非零分量移向后续坐标')
n=np.arange(1,61);ax[1].plot(n,np.ones_like(n),color=R,label='二范数始终为1',lw=2);ax[1].plot(n,1/n,color=B,label='固定读数：gₙ=1/n',lw=2)
ax[1].set(xlabel='序号 n',ylabel='范数或读数绝对值',title='（b）弱趋零不要求范数趋零');ax[1].legend(fontsize=10)
fig.suptitle('固定读数趋零，不代表向量范数趋零',fontsize=18,fontweight='bold');save(fig,'weak-and-strong')
# 8 Compact Green eigenvalues and approximate spectrum.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));n=np.arange(1,61)
ax[0].loglog(n,1/(n*np.pi)**2,'o-',color=B,ms=3,label='λₙ=1/(nπ)²')
ax[0].set(xlabel='模态序号 n',ylabel='Green算子特征值',title='（a）非零谱向0聚集，0不是特征值');ax[0].legend(fontsize=10)
for eps,col in [(.2,R),(.1,G),(.04,B)]:
    val=((t>=.5-eps)&(t<=.5+eps))/np.sqrt(2*eps)
    ax[1].plot(t,val,color=col,label=f'ε={eps:g}，残差={eps/np.sqrt(3):.3f}',lw=1.8)
ax[1].set(xlabel='归一化坐标 t',ylabel='归一化窄窗 fε(t)',title='（b）乘法M=t：λ=0.5的近似特征向量');ax[1].legend(fontsize=9)
fig.suptitle('谱不只包含真正的特征值',fontsize=18,fontweight='bold');save(fig,'compact-and-spectrum')
# 9 Galerkin and energy error identity.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ax[0].plot(t,t*(1-t)/2,'--',color=M,label='精确弱解',lw=2)
for m,col in [(4,R),(8,G),(16,B)]:
    data=model.galerkin(m);ax[0].plot(data['x'],data['u'],'o-',ms=3,color=col,label=f'{m}单元')
ax[0].set(xlabel='归一化位置 x',ylabel='u(x)',title='（a）分段线性Galerkin近似');ax[0].legend(fontsize=10)
ms=np.array([4,8,16,32,64]);d=[model.galerkin(int(m)) for m in ms];jd=np.array([x['J']-x['J_exact'] for x in d]);ee=np.array([x['energy_error2']/2 for x in d])
ax[1].loglog(ms,jd,'o-',color=B,label='泛函差 J(uₕ)−J(u)');ax[1].loglog(ms,ee,'x',color=R,ms=9,label='能量误差平方的一半')
ax[1].set(xlabel='单元数',ylabel='泛函差或半能量误差',title='（b）两种计算一致，误差按二阶下降');ax[1].legend(fontsize=9)
fig.suptitle('适当空间中的弱解与最优近似',fontsize=18,fontweight='bold');save(fig,'variational-problem')
# 10 Regularization errors and spectral gains.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));data=model.regularization();n=data['n']
ax[0].semilogy(n,np.abs(data['raw']-data['truth'])+1e-16,color=R,label='直接反演的系数误差',lw=1.6)
ax[0].semilogy(n,np.abs(data['estimate']-data['truth'])+1e-16,color=B,label='α=10⁻⁴的系数误差',lw=1.8)
ax[0].set(xlabel='系数序号 n',ylabel='绝对误差（对数轴）',title='（a）相同确定性数据扰动，范数δ=0.001');ax[0].legend(fontsize=9)
s=np.logspace(-5,0,600);alpha=1e-4
ax[1].loglog(s,1/s,color=R,label='直接逆增益 1/σ',lw=2)
ax[1].loglog(s,s/(s*s+alpha),color=B,label='Tikhonov增益',lw=2);ax[1].axhline(1/(2*np.sqrt(alpha)),color=M,ls='--',label='上界 1/(2√α)=50')
ax[1].set(xlabel='奇异值 σ',ylabel='数据到系数的增益',title='（b）控制放大同时引入偏差');ax[1].legend(fontsize=9)
fig.suptitle('正则化的条件与代价：偏差和误差放大一起看',fontsize=18,fontweight='bold');save(fig,'regularization')
# Course sketch: an infinite sequence of orthogonal axes, projection and space boundary.
thumb=ROOT/'public/figures/foundation-courses/functional-analysis.svg'
thumb.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="320" height="180" viewBox="0 0 320 180"><rect width="320" height="180" fill="#f2f0f7"/><g fill="none" stroke="#7c7091" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="111" cy="94" rx="70" ry="48" transform="rotate(-14 111 94)"/><path d="M62 127l75-21 40 20M137 106l-11-66M137 106l-44-40M137 106l34-37M137 106l51-4" opacity=".75"/><path d="M137 106l-10-38" stroke="#437b91" stroke-width="3"/><path d="M127 68l25 39" stroke-dasharray="4 4"/></g><g fill="none" stroke="#437b91" stroke-width="2"><path d="M213 61q11-24 22 0t22 0M213 89q7-21 14 0t14 0t14 0M213 117q5-17 10 0t10 0t10 0t10 0"/></g><g fill="#8d819b"><circle cx="277" cy="144" r="2"/><circle cx="285" cy="144" r="2"/><circle cx="293" cy="144" r="2"/></g></svg>\n',encoding='utf-8')
(REC/'calculations.json').write_text(json.dumps(model.summary(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,summary=model.summary()),ensure_ascii=True))
