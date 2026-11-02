"""Original code-native figures for the deep-learning course; no source images copied."""
from pathlib import Path
import importlib.util,sys,json,itertools
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,Circle
from scipy.special import expit
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/deep-learning/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/deep-learning';PRE=ROOT/'artifacts/deep-learning/figures';REC=ROOT/'docs/research/deep-learning-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'deep-learning-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创深度学习教学图 · 指定数学模型或模拟，非声音基准/参与者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.06,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def arrow(ax,a,b,col=M):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.5,color=col))
def box(ax,x,y,w,h,text,col=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',facecolor=col+'12',edgecolor=col,lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=col,fontsize=12)
# 1 Explicit XOR representation; not a trained deep-vs-shallow benchmark.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));ax=axes[0];ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
inputs=[(1,1.5),(1,3.5)];hidden=[(4,1),(4,2.5),(4,4)]
for a in inputs:
    for b in hidden:ax.plot([a[0]+.35,b[0]-.4],[a[1],b[1]],color=B,alpha=.35,lw=1.2)
for j,b in enumerate(hidden):
    arrow(ax,(b[0]+.4,b[1]),(7.1,2.5),P);ax.text(5.7,b[1]+.1,['+1','−2','+1'][j],color=P,ha='center',fontsize=12)
for (x,y),text in zip(inputs,['x₁','x₂']):ax.add_patch(Circle((x,y),.35,fc='#edf3f6',ec=B,lw=1.8));ax.text(x,y,text,ha='center',va='center',fontsize=13)
for (x,y),text in zip(hidden,['h₂','h₁','h₀']):ax.add_patch(Circle((x,y),.4,fc='#f1edf7',ec=P,lw=1.8));ax.text(x,y,text,ha='center',va='center',fontsize=13)
# The bottom-to-top labels h2/h1/h0 correspond to biases -2/-1/0.
ax.text(4,.28,'hⱼ=ReLU(s−j)\ns=x₁+x₂',ha='center',fontsize=11,color=M)
ax.add_patch(Circle((7.5,2.5),.4,fc='#edf4ef',ec=G,lw=1.8));ax.text(7.5,2.5,'r',ha='center',va='center',fontsize=14);arrow(ax,(7.95,2.5),(9.05,2.5),G);ax.text(9.2,2.5,'σ(8r−4)',ha='center',va='center',color=G,fontsize=12)
ax.set_title('（a）一层隐藏层：隔离非线性机制')
q=np.linspace(0,1,201);xx,yy=np.meshgrid(q,q);prob=expit(8*m.xor_representation(np.stack([xx,yy],-1))-4)
im=axes[1].imshow(prob,origin='lower',extent=(0,1,0,1),cmap='RdBu_r',vmin=0,vmax=1,aspect='auto');axes[1].contour(xx,yy,prob,levels=[.5],colors='white',linewidths=1)
for x,y,label in [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]:axes[1].scatter(x,y,c='white',edgecolor='black',s=65,zorder=3);axes[1].annotate(str(label),(x,y),xytext=(7 if x==0 else -14,8 if y==0 else -17),textcoords='offset points',fontweight='bold')
axes[1].set(xlabel='输入 x₁',ylabel='输入 x₂',xlim=(-.06,1.06),ylim=(-.06,1.06),title='（b）指定映射的类别1概率');fig.colorbar(im,ax=axes[1],label='概率')
fig.suptitle('非线性表示让简单输出层获得新的区分能力',fontsize=18,fontweight='bold');save(fig,'representation')
# 2 Computational graph and independent finite differences.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));ax=axes[0];ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
for x,y,text,col in [(.5,3.1,'Z₁=XW₁+b₁',B),(5.8,3.1,'H₁=tanh(Z₁)',P),(5.8,.65,'z=H₁v+c',G),(.5,.65,'平均二分类损失',R)]:box(ax,x,y,3.7,1.1,text,col)
for a,b in [((4.3,3.65),(5.6,3.65)),((7.65,3.0),(7.65,1.9)),((5.6,1.2),(4.3,1.2))]:arrow(ax,a,b,B)
arrow(ax,(2.35,1.9),(2.35,3.0),R);ax.text(4.9,2.4,'链式法则累积\n所有使用路径',ha='center',color=M,fontsize=11);ax.set_title('（a）前向产生数值，反向计算梯度')
theta=m.THETA_SMALL;loss,grad=m.binary_loss_grad(theta);eps=1e-5
fd=np.array([(m.binary_loss_grad(theta+eps*e)[0]-m.binary_loss_grad(theta-eps*e)[0])/(2*eps) for e in np.eye(9)])
axes[1].bar(np.arange(9),grad,color=B,alpha=.65,label='解析反向传播');axes[1].scatter(np.arange(9),fd,color=R,marker='x',s=55,label='独立中心差分',zorder=3)
axes[1].axhline(0,color=M,lw=.7);axes[1].set(xticks=np.arange(9),xticklabels=['w₁₁','w₁₂','w₂₁','w₂₂','b₁','b₂','v₁','v₂','c'],ylabel='平均损失对参数的变化率',title=f'（b）损失{loss:.6f}，最大差{np.max(abs(fd-grad)):.1e}');axes[1].legend(fontsize=10)
fig.suptitle('反向传播检查：形状、分母与共享路径都要正确',fontsize=18,fontweight='bold');save(fig,'backpropagation')
# 3 Forward second moment and scalar Jacobian products are explicitly separate models.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));depth=np.arange(31)
for gain,col,label in [(.5,R,'权重方差1/n'),(1,G,'权重方差2/n'),(2,B,'权重方差4/n')]:axes[0].semilogy(depth,gain**depth,color=col,lw=2,label=label)
axes[0].set(xlabel='层数 L',ylabel='理想输出二阶矩 / 初值',title='（a）指定ReLU递推：每层系数n·Var(W)/2');axes[0].legend(fontsize=10)
depth=np.arange(101)
for gain,col,label in [(.5,R,'局部系数0.5'),(1.01,G,'局部系数1.01'),(1.2,B,'局部系数1.2')]:axes[1].semilogy(depth,gain**depth,color=col,lw=2,label=label)
axes[1].set(xlabel='连乘次数 L',ylabel='标量梯度增益 aᴸ',title='（b）固定系数示例，不是实际网络测量');axes[1].legend(fontsize=10)
fig.suptitle('深层尺度：保持二阶矩与保持梯度是相关而不同的问题',fontsize=18,fontweight='bold');save(fig,'depth-stability')
# 4 Batch context versus feature context; dropout expectation versus nonlinear output.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));x=np.array([[1.,4.],[3.,8.],[5.,6.]]);changed=x.copy();changed[-1]=[50,60]
bn=[m.normalize(a,0)[0,0] for a in [x,changed]];ln=[m.normalize(a,1)[0,0] for a in [x,changed]];pos=np.arange(2)
axes[0].bar(pos-.16,bn,.32,color=B,label='按批次/每特征');axes[0].bar(pos+.16,ln,.32,color=P,label='每样本/两特征');axes[0].axhline(0,color=M,lw=.7)
axes[0].set(xticks=pos,xticklabels=['原批次','修改第3条样本'],ylabel='第1条样本第1特征归一化值',ylim=(-1.55,.1),title='（a）相同输入，统计轴决定是否受同伴影响');axes[0].legend(fontsize=9,loc='lower left')
drop_mean=[1.,float((expit(0)+expit(2))/2)];deterministic=[1.,float(expit(1))]
axes[1].bar(pos-.16,drop_mean,.32,color=R,label='随机训练输出的均值');axes[1].bar(pos+.16,deterministic,.32,color=G,label='不失活的确定计算')
for i,(a,b) in enumerate(zip(drop_mean,deterministic)):
    axes[1].text(i-.16,a+.025,f'{a:.4f}',ha='center',fontsize=10);axes[1].text(i+.16,b+.025,f'{b:.4f}',ha='center',fontsize=10)
axes[1].set(xticks=pos,xticklabels=['激活本身','再经过sigmoid'],ylabel='指定无量纲输出值',ylim=(0,1.28),title='（b）h=1、丢弃率0.5、倒置缩放');axes[1].legend(fontsize=9)
fig.suptitle('归一化的统计依赖与随机失活的期望边界',fontsize=18,fontweight='bold');save(fig,'normalization-dropout')
# 5 Time causality and exact receptive field.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));impulse=np.zeros(41);impulse[20]=1;kernel=np.array([.25,.5,.25]);causal=m.causal_xcorr(impulse,kernel);center=np.convolve(impulse,kernel,mode='same')
axes[0].step(np.arange(41),impulse,where='mid',color=M,label='输入脉冲',lw=1.5);axes[0].plot(np.arange(41),causal,'o-',color=B,label='因果左填充',ms=4);axes[0].plot(np.arange(41),center,'x--',color=R,label='居中窗口',ms=5);axes[0].axvline(20,color=M,ls=':',lw=.8)
axes[0].set(xlabel='离散输入/输出位置',ylabel='指定幅值',xlim=(16,25),ylim=(-.05,1.1),title='（a）未来脉冲能否改变较早的输出？');axes[0].legend(fontsize=10)
sizes=[p[0] for p in m.receptive_field()]
for i,(size,col) in enumerate(zip(sizes,[B,P,G])):
    lags=np.arange(-size+1,1);axes[1].plot([lags[0],0],[i,i],color=col,lw=2);axes[1].scatter(lags,np.full(len(lags),i),color=col,s=28);axes[1].text(.8,i,f'{size}点',va='center',color=col)
axes[1].set(xlabel='相对当前输出的输入位置',yticks=[0,1,2],yticklabels=['第1层，d=1','第2层，d=2','第3层，d=4'],xlim=(-15,3),ylim=(-.5,2.7),title='（b）三层核长3、步长1，范围增至15点')
fig.suptitle('局部共享不等于实时：必须检查索引与前视',fontsize=18,fontweight='bold');save(fig,'convolution-causality')
# 6 CTC exact path enumeration.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));axes[0].axis('off');ctc_p=np.tile([.4,.6],(3,1));path_rows=[]
for path in itertools.product([0,1],repeat=3):
    label=m.collapse_ctc(path);mass=np.prod([ctc_p[i,v] for i,v in enumerate(path)])
    path_rows.append([' '.join('a' if v else '□' for v in path),'a'*len(label) if label else '空串',f'{mass:.3f}'])
table=axes[0].table(cellText=path_rows,colLabels=['路径（□为空白）','折叠结果','路径概率'],cellLoc='center',loc='center',bbox=[.02,.03,.96,.92]);table.auto_set_font_size(False);table.set_fontsize(12)
for (r,c),cell in table.get_celld().items():cell.set_edgecolor('#dce3e8');cell.set_facecolor('#edf3f6' if r==0 else ('#edf4ef' if path_rows[r-1][1]=='a' else 'white'))
axes[0].set_title('（a）先合并相邻重复，再删空白')
totals=m.ctc_enumerate(ctc_p);values=[totals[()],totals[(1,)],totals[(1,1)]];axes[1].bar(['空串','a','aa'],values,color=[M,G,P],width=.58)
for i,v in enumerate(values):axes[1].text(i,v+.025,f'{v:.3f}',ha='center',fontsize=12)
axes[1].set(ylabel='所有相应路径的概率和',ylim=(0,.95),title='（b）目标串概率不是最大单路径概率')
fig.suptitle('CTC对齐：三帧、两符号的完整可复算例子',fontsize=18,fontweight='bold');save(fig,'ctc-alignment')
# 7 Attention masks and perturbing the future.
fig,axes=plt.subplots(1,3,figsize=(14,5.5));x=m.ATTENTION_X;changed=x.copy();changed[-1]=[6,-5];allow=np.tril(np.ones((4,4),bool))
full_out,full=m.attention(x,x,x);causal_out,causal_A=m.attention(x,x,x,allow)
for i,(a,title) in enumerate([(full,'（a）完整注意力'),(causal_A,'（b）非未来掩码')]):
    im=axes[i].imshow(a,cmap='Blues',vmin=0,vmax=1)
    for r in range(4):
        for c in range(4):axes[i].text(c,r,'×' if i==1 and c>r else f'{a[r,c]:.2f}',ha='center',va='center',color='white' if a[r,c]>.55 else M,fontsize=10)
    axes[i].set(xticks=range(4),xticklabels=range(1,5),yticks=range(4),yticklabels=range(1,5),xlabel='键位置',ylabel='查询位置',title=title)
changes=[np.max(abs(full_out[:3]-m.attention(changed,changed,changed)[0][:3])),np.max(abs(causal_out[:3]-m.attention(changed,changed,changed,allow)[0][:3]))]
axes[2].bar(['完整','非未来掩码'],changes,color=[R,G],width=.55)
for i,v in enumerate(changes):axes[2].text(i,v+.12,f'{v:.4f}',ha='center')
axes[2].set(ylabel='前3个输出的最大绝对变化',ylim=(0,6.3),title='（c）只修改第4个输入')
fig.suptitle('每行在允许的键中归一化；因果性要用依赖关系检查',fontsize=18,fontweight='bold');save(fig,'attention-masks')
# 8 Actual Markov forward diffusion chain; no generated reverse result.
time,states=m.diffusion_forward();fig,axes=plt.subplots(2,2,figsize=(14,8));bound=max(abs(v).max() for v in states.values())*1.07
for ax,(step,state),col in zip(axes.ravel(),states.items(),[B,G,P,R]):
    ax.plot(time,state,color=col,lw=1);ax.set(xlabel='归一化位置',ylabel='标准化模型幅值',ylim=(-bound,bound),title=f'步{step}，信号系数平方={(.98**step):.4f}')
fig.suptitle('扩散前向链：独立高斯增量逐步加入指定波形',fontsize=18,fontweight='bold');save(fig,'diffusion-forward')
# 9 One-hidden-layer mechanism isolation: no claim of universal U-shaped risk.
training=m.regression_training();r=training['records'];best=training['best_index'];fig,axes=plt.subplots(1,2,figsize=(14,5.5))
for j,col,label in [(1,B,'训练MSE'),(2,P,'验证MSE'),(3,G,'已知总体期望MSE')]:axes[0].semilogy(r[:,0],r[:,j],color=col,lw=1.7,label=label)
axes[0].axvline(r[best,0],color=R,ls='--',label='按验证选择');axes[0].set(xlabel='全批Adam更新步数',ylabel='平方误差 / 指定单位²',title='（a）验证选择不使用已知总体风险');axes[0].legend(fontsize=9)
pos=np.arange(2)
for j,col,label in [(1,B,'训练'),(2,P,'验证'),(3,G,'已知总体')]:
    values=r[[best,-1],j];bars=axes[1].bar(pos+(j-2)*.23,values,.23,color=col,label=label)
    for bar,v in zip(bars,values):axes[1].text(bar.get_x()+bar.get_width()/2,v+.003,f'{v:.4f}',ha='center',fontsize=9)
axes[1].set(xticks=pos,xticklabels=[f'选择的{int(r[best,0])}步','最终12000步'],ylabel='MSE',ylim=(0,.17),title='（b）更低训练误差不保证更低风险');axes[1].legend(fontsize=9)
fig.suptitle('一次指定训练：保留模型选择和独立推广的区别',fontsize=18,fontweight='bold');save(fig,'training-selection')
# 10 Exact expectation under a known Bernoulli population; not calibration on a test set.
fig,axes=plt.subplots(1,2,figsize=(14,5.5));temperatures=np.linspace(.5,10,601);prob,risk=m.calibration(temperatures);optimal=np.log(9)/np.log(1.5)
axes[0].plot(temperatures,prob,color=B,lw=2,label='预测类别1概率');axes[0].axhline(.6,color=G,ls='--',label='指定总体发生率0.6');axes[0].scatter([1,optimal],[.9,.6],color=R)
axes[0].set(xlabel='正温度 T',ylabel='概率',ylim=(.48,1.02),title='（a）固定logit=log9，排序保持');axes[0].legend(fontsize=10)
axes[1].plot(temperatures,risk,color=P,lw=2);axes[1].scatter([1,optimal],[m.calibration(1)[1],m.calibration(optimal)[1]],color=R)
axes[1].axvline(optimal,color=M,ls='--',label=f'T≈{optimal:.4f}');axes[1].set(xlabel='正温度 T',ylabel='精确期望对数损失 / nat',title='（b）真实P(Y=1)=0.6，非测试样本均值');axes[1].legend()
fig.suptitle('概率校准改变置信度，不必改变分类正确率',fontsize=18,fontweight='bold');save(fig,'calibration')
calc=dict(binary_network=dict(loss=loss,gradient=grad.tolist(),finite_difference_max_error=float(np.max(abs(fd-grad)))),XOR_probabilities=expit(8*m.xor_representation(np.array([[0,0],[0,1],[1,0],[1,1]]))-4).tolist(),normalization=dict(batchnorm_first_feature=bn,layernorm_first_feature=ln,dropout_mean=drop_mean,deterministic=deterministic),attention_prefix_change=changes,receptive_fields=sizes,ctc=dict(empty=totals[()],a=totals[(1,)],aa=totals[(1,1)]),diffusion_alpha_bar={str(t):.98**t for t in states},training=dict(selected_checkpoint=r[best].tolist(),final_checkpoint=r[-1].tolist(),seed=training['seed'],width=32,parameters=97,checkpoints=len(r)),temperature=dict(optimal=optimal,probability_before=float(m.calibration(1)[0]),probability_after=float(m.calibration(optimal)[0]),risk_before=float(m.calibration(1)[1]),risk_after=float(m.calibration(optimal)[1])))
(REC/'calculations.json').write_text(json.dumps(calc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(REC/'training-records.json').write_text(json.dumps(dict(columns=['step','training_MSE','validation_MSE','known_population_expected_MSE'],records=r.tolist(),selection='minimum validation_MSE over recorded checkpoints',known_population_not_used_for_selection=True),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
nodes=[(80,[48,90,132]),(130,[37,72,108,143]),(185,[48,90,132]),(240,[63,117])]
paths=[]
for (x1,ys1),(x2,ys2) in zip(nodes,nodes[1:]):
    for y1 in ys1:
        for y2 in ys2:paths.append(f'<path d="M{x1+5} {y1}L{x2-5} {y2}"/>')
circles=''.join(f'<circle cx="{x}" cy="{y}" r="5"/>' for x,ys in nodes for y in ys)
sketch='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img" aria-labelledby="title desc"><title id="title">深度学习：多层表示与反向学习</title><desc id="desc">波形输入经过多列连接的计算单元形成输出，底部回返箭头表示由损失计算梯度。</desc><rect width="320" height="180" fill="#f4f0e5"/><g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M15 90h7l5-24 6 49 7-65 7 82 6-42h14" stroke="#22658c" stroke-width="1.9"/><g stroke="#79639d" stroke-opacity=".45" stroke-width="1.2">'+''.join(paths)+'</g><g fill="#f4f0e5" stroke="#79639d" stroke-width="1.8">'+circles+'</g><path d="M247 63l24 20m-24 34 24-20" stroke="#31755e" stroke-width="1.6"/><path d="M279 113V79m10 34V61m10 52V92" stroke="#31755e" stroke-width="5"/><path d="M281 141c-28 27-166 30-203 2m0 0 10-1m-10 1 5 9" stroke="#b44e37" stroke-width="1.6"/></g></svg>'
(ROOT/'public/figures/foundation-courses/deep-learning.svg').write_text(sketch+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,network_loss=loss,gradient_max_error=calc['binary_network']['finite_difference_max_error'],selected=r[best].tolist(),final=r[-1].tolist()),ensure_ascii=False))
