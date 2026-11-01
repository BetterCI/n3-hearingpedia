"""Reproducible original course figures, not real auditory measurements."""
from pathlib import Path
import json,importlib.util
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Circle
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('ml_examples',ROOT/'public/code/machine-learning/experiments.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
FIG=ROOT/'public/figures/machine-learning';PRE=ROOT/'artifacts/machine-learning/figures';REC=ROOT/'docs/research/machine-learning-2026-11-02'
for p in (FIG,PRE,REC):p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':12,'svg.fonttype':'path','svg.hashsalt':'machine-learning-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,M,P='#22658c','#31755e','#b44e37','#61727d','#79639d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创机器学习教学图 · 指定模型或模拟数据，非实验测量',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.055,1,.90),w_pad=3,h_pad=3)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def box(ax,x,y,w,h,label,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=color,fc='#f7f9fc',lw=1.5))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=13,color=color)
def arrow(ax,a,b):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':M,'lw':1.6})

fig,ax=plt.subplots(figsize=(14,5.6));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
box(ax,.02,.58,.22,.25,'研究任务\n目标人群与部署条件')
box(ax,.39,.58,.22,.25,'训练数据与损失\n学习模型参数',P)
box(ax,.76,.58,.22,.25,'独立评价\n预测与不确定性',G)
box(ax,.26,.13,.48,.24,'验证集选择流程；测试集最后评价\n先按人、录音或时间划分，再拟合预处理',R)
arrow(ax,(.25,.70),(.38,.70));arrow(ax,(.62,.70),(.75,.70));arrow(ax,(.5,.57),(.5,.39))
fig.suptitle('机器学习的主线：问题、数据、目标与可推广的评价',fontsize=18,fontweight='bold');save(fig,'learning-loop')

rng=np.random.default_rng(20261102);x=np.linspace(-1,1,18);truth=lambda a:1+.7*a-.9*a*a
y=truth(x)+rng.normal(0,.25,len(x));grid=np.linspace(-1,1,800)
q,qw=np.polynomial.legendre.leggauss(64);degrees=list(range(1,15));train=[];risk=[]
for d in degrees:
    fit=np.polynomial.Polynomial.fit(x,y,d)
    train.append(float(np.mean((fit(x)-y)**2)));risk.append(float(np.sum(qw*(fit(q)-truth(q))**2)/2+.25**2))
fig,axes=plt.subplots(1,2,figsize=(14,6))
axes[0].scatter(x,y,color=M,label='18个模拟训练点');axes[0].plot(grid,truth(grid),'--',color='black',label='生成均值')
for d,c in [(1,B),(2,G),(12,R)]:axes[0].plot(grid,np.polynomial.Polynomial.fit(x,y,d)(grid),color=c,label=f'{d}次多项式')
axes[0].set(xlabel='无量纲输入 x',ylabel='无量纲响应 y',ylim=(-1.6,3.2),title='（a）相同训练点，不同函数类');axes[0].legend(fontsize=9)
axes[1].plot(degrees,train,'o-',color=B,label='训练MSE');axes[1].plot(degrees,risk,'s-',color=R,label='指定总体的期望MSE')
axes[1].axhline(.0625,ls='--',color=M,label='不可约噪声方差 0.0625');axes[1].set(xlabel='多项式次数',ylabel='均方损失（对数轴）',yscale='log',title='（b）总体风险用已知生成模型积分');axes[1].legend(fontsize=9)
fig.suptitle('拟合训练点更紧，不保证新样本误差更小',fontsize=18,fontweight='bold');save(fig,'fit-and-risk')

rd=model.ridge_example();xx=np.array([-2.,-1.,0.,1.,2.]);yy=np.array([-3.8,-2.2,.2,1.8,4.])
fig,axes=plt.subplots(1,2,figsize=(13,5.6));axes[0].scatter(xx,yy,color=M)
for w,c,label in [(rd['ols_slope'],B,'最小二乘：w = 1.96'),(rd['ridge_slope'],G,'岭回归：λ = 1，w = 1.3067')]:axes[0].plot(xx,w*xx,color=c,label=label)
axes[0].set(xlabel='已中心化特征 x',ylabel='已中心化目标 y',title='（a）截距不惩罚，系数向零收缩');axes[0].legend(fontsize=10)
lam=np.logspace(-3,2,300);axes[1].semilogx(lam,19.6/(10+5*lam),color=G,lw=2);axes[1].scatter([1],[19.6/15],color=R)
axes[1].set(xlabel='正则化系数 λ',ylabel='岭回归斜率 w',title='（b）损失取样本平均，惩罚为 λw²/2')
fig.suptitle('正则化改变优化目标，也依赖特征的尺度',fontsize=18,fontweight='bold');save(fig,'ridge-shrinkage')

from scipy.special import expit
z=np.linspace(-6,6,600);prob=np.linspace(.005,.995,500)
fig,axes=plt.subplots(1,2,figsize=(13,5.7));axes[0].plot(z,expit(z),color=B);axes[0].axhline(.5,color=M,ls='--');axes[0].axvline(0,color=M,ls=':')
axes[0].set(xlabel='线性得分 z = b + wᵀx',ylabel='正类概率 σ(z)',title='（a）概率与决策阈值是两件事')
axes[1].plot(prob,-np.log(prob),color=G,label='真实 y = 1：−log p');axes[1].plot(prob,-np.log1p(-prob),color=R,label='真实 y = 0：−log(1−p)')
axes[1].set(xlabel='预测正类概率 p',ylabel='单样本对数损失 / nat',title='（b）自信的错误受到较大惩罚');axes[1].legend(fontsize=10)
fig.suptitle('逻辑回归：从线性得分到条件概率与损失',fontsize=18,fontweight='bold');save(fig,'logistic-and-loss')

pc=model.pca_example();a=np.array(pc['data']);lab=np.array(pc['labels'])
fig,axes=plt.subplots(1,2,figsize=(13,5.8))
for c,marker,color in [(0,'o',B),(1,'^',R)]:
    mask=lab==c;axes[0].scatter(a[mask,0],a[mask,1],marker=marker,color=color,s=80,label=f'类别 {c}')
    axes[1].scatter(a[mask,0],np.zeros(mask.sum())+(.015 if c else -.015),marker=marker,color=color,s=80)
axes[0].arrow(-3.5,0,7,0,width=.003,color=M,length_includes_head=True);axes[0].set(xlim=(-4,4),ylim=(-.45,.45),xlabel='特征1：大尺度无关变化',ylabel='特征2：小尺度类别线索',title='（a）原始8点：类别由特征2符号决定');axes[0].legend(fontsize=10)
axes[1].set(xlim=(-4,4),ylim=(-.45,.45),xlabel='第一主成分得分',ylabel='仅为看清重叠而上下错开',title='（b）保留99.21%方差，却无法区分类别');axes[1].set_yticks([])
fig.suptitle('PCA最大化方差，不直接最大化类别可分性',fontsize=18,fontweight='bold');save(fig,'pca-and-labels')

fig,axes=plt.subplots(1,2,figsize=(13,5.8));ax=axes[0];ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
layers=[[(.1,.3),(.1,.7)],[(.5,.2),(.5,.5),(.5,.8)],[(.9,.5)]]
for first,second in zip(layers[:-1],layers[1:]):
    for a0 in first:
        for b0 in second:ax.plot([a0[0],b0[0]],[a0[1],b0[1]],color='#b9bdc9',lw=1)
for j,layer in enumerate(layers):
    for position in layer:ax.add_patch(Circle(position,.048,ec=[B,P,G][j],fc='white',lw=2))
ax.text(.1,.04,'输入 x',ha='center');ax.text(.5,.04,'非线性隐藏层',ha='center');ax.text(.9,.04,'输出',ha='center');ax.set_title('（a）节点与线表示函数和参数')
t=np.linspace(-2,2,400);axes[1].plot(t,np.maximum(0,t),color=G,lw=2,label='ReLU(z) = max(0,z)');axes[1].plot(t,t,color=M,ls='--',label='线性函数')
axes[1].set(xlabel='隐藏单元输入 z',ylabel='激活输出',title='（b）非线性使多层函数不再合并成单层');axes[1].legend(fontsize=10)
fig.suptitle('神经网络：组合可学习变换，再用链式法则计算梯度',fontsize=18,fontweight='bold');save(fig,'network-and-activation')

identity=model.identity_split_example();fig,axes=plt.subplots(1,2,figsize=(14,6))
row=np.tile([0,0,0,0,1,1],(8,1));group=np.vstack([np.zeros((4,6)),np.ones((4,6))])
from matplotlib.colors import ListedColormap
for i,(array,title) in enumerate([(row,'（a）每个身份：4条训练、2条测试'),(group,'（b）整组身份：训练与测试不相交')]):
    axes[i].imshow(array,cmap=ListedColormap(['#22658c','#d9b67a']),vmin=0,vmax=1,aspect='auto')
    axes[i].set(xticks=range(6),xticklabels=range(1,7),yticks=range(8),yticklabels=range(1,9),xlabel='同一身份的第几条重复',ylabel='身份（只画8个说明布局）',title=title)
    axes[i].set_xticks(np.arange(-.5,6),minor=True);axes[i].set_yticks(np.arange(-.5,8),minor=True);axes[i].grid(which='minor',color='white',lw=2);axes[i].tick_params(which='minor',bottom=False,left=False)
fig.suptitle('只记身份也能得高分：40身份×6重复，行内100%，新身份50%\n蓝色为训练；金色为测试。两种划分回答不同推广问题',fontsize=16,fontweight='bold');save(fig,'group-split')

met=model.metrics_example();fig,axes=plt.subplots(1,2,figsize=(14,5.8))
mat=np.array([[40,10],[95,855]]);axes[0].imshow(mat,cmap='Blues',vmin=0,vmax=855)
for i in range(2):
    for j in range(2):axes[0].text(j,i,str(mat[i,j]),ha='center',va='center',color='white' if mat[i,j]>500 else B,fontsize=24)
axes[0].set(xticks=[0,1],xticklabels=['预测正类','预测负类'],yticks=[0,1],yticklabels=['真实正类','真实负类'],title='（a）1000例：真实正类仅50例')
names=['准确率','精确率','召回率','平衡准确率','F1'];values=[met[k] for k in ['accuracy','precision','recall','balanced_accuracy','f1']]
axes[1].barh(names,values,color=[B,R,G,P,M]);axes[1].set(xlim=(0,1.08),xlabel='指标数值',title='（b）不同指标有不同分母')
for i,v in enumerate(values):axes[1].text(v+.015,i,f'{v:.3f}',va='center')
fig.suptitle('准确率89.5%时，预测为正的样本中仍只有29.6%为真',fontsize=18,fontweight='bold');save(fig,'confusion-and-metrics')

fig,axes=plt.subplots(1,2,figsize=(13,5.7))
axes[0].plot([0,1],[0,1],ls='--',color=M,label='理想校准参考');axes[0].scatter([.8,.95],[.8,.8],s=90,c=[G,R]);axes[0].plot([.8,.95],[.8,.8],color=M,ls=':')
axes[0].set(xlim=(0,1),ylim=(0,1),xlabel='同组预测正类概率',ylabel='组内实际正类比例',title='（a）100例中80例为正：同组常数预测');axes[0].legend(fontsize=10)
axes[1].bar([0,1],[met['brier_08'],met['brier_095']],color=[G,R]);axes[1].set(xticks=[0,1],xticklabels=['全报0.80','全报0.95'],ylabel='二分类Brier分数，越低越好',ylim=(0,.23),title='（b）相同80%准确率，概率质量不同')
for i,v in enumerate([met['brier_08'],met['brier_095']]):axes[1].text(i,v+.006,f'{v:.4f}',ha='center')
fig.suptitle('校准检查概率是否可信，排序与分类正确率不能替代它',fontsize=18,fontweight='bold');save(fig,'probability-calibration')

thumb=ROOT/'public/figures/foundation-courses/machine-learning.svg'
thumb.write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img"><title>机器学习：从样本点学习分类边界</title><rect width="320" height="180" fill="#f3f1f8"/><g fill="none" stroke="#716286" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M43 143V32M43 143H276"/><path d="M84 126C111 111 115 88 145 87S189 68 212 41" stroke-dasharray="6 5"/><path d="M244 36l7 7 14-15"/></g><g fill="none" stroke="#437b91" stroke-width="2.5"><circle cx="75" cy="61" r="6"/><circle cx="96" cy="91" r="6"/><circle cx="122" cy="56" r="6"/><circle cx="162" cy="49" r="6"/></g><g fill="none" stroke="#b58258" stroke-width="2.5" stroke-linecap="round"><path d="M131 116l10 10m0-10l-10 10M165 100l10 10m0-10l-10 10M210 108l10 10m0-10l-10 10M231 74l10 10m0-10l-10 10"/></g><path d="M261 133c5-4 5-13-1-17s-15-2-17 4 2 14 8 15m-7 3h14m-12 5h10" fill="none" stroke="#716286" stroke-width="2.2" stroke-linecap="round"/></svg>\n''',encoding='utf-8')
calculations={'ridge':rd,'logistic':model.logistic_example(),'pca':pc,'identity_split':identity,'metrics':met,
 'polynomial':{'seed':20261102,'x':x.tolist(),'y':y.tolist(),'degrees':degrees,'training_mse':train,'population_mse':risk,'noise_variance':.0625}}
(REC/'calculations.json').write_text(json.dumps(calculations,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(calculations,ensure_ascii=True,indent=2))
