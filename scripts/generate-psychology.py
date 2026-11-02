"""Original psychology teaching figures. Source figures are not reused."""
from pathlib import Path
import importlib.util,sys,json
sys.dont_write_bytecode=True
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.stats import norm
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('models',ROOT/'public/code/psychology/experiments.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
FIG=ROOT/'public/figures/psychology';PRE=ROOT/'artifacts/psychology/figures';REC=ROOT/'docs/research/psychology-2026-11-02'
for p in [FIG,PRE,REC]:p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,'svg.fonttype':'path','svg.hashsalt':'psychology-course','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False})
B,G,R,P,M='#22658c','#31755e','#b44e37','#79639d','#61727d'
def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创心理学教学图 · 示意关系或指定模型，非参与者实测',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.065,1,.90),w_pad=3,h_pad=2)
    path=FIG/(name+'.svg');fig.savefig(path,metadata={'Date':None},facecolor='white')
    path.write_text('\n'.join(s.rstrip() for s in path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/(name+'.png'),dpi=100,facecolor='white');plt.close(fig)
def box(ax,x,y,w,h,text,col=B,fs=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.09',fc=col+'12',ec=col,lw=1.6))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=col)
def arrow(ax,start,end,col=M):ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',lw=1.7,color=col))
# 1 Research logic, deliberately not a neural architecture.
fig,ax=plt.subplots(figsize=(14,5.5));ax.set(xlim=(0,14),ylim=(0,5));ax.axis('off')
for x,y,txt,col in [(.5,3.1,'构念与假设\n例如：选择目标信息',P),(5,3.1,'操作与设计\n任务、材料、对照',B),(9.5,3.1,'可观察指标\n选择、时间、报告',G),(9.5,.7,'模型与预测\n能区分哪些机制？',P),(5,.7,'替代解释与情境\n测量、样本、混杂',R),(.5,.7,'有限结论与新问题\n修订并再次检验',B)]:box(ax,x,y,3.8,1.2,txt,col)
for a,b in [((4.3,3.7),(4.9,3.7)),((8.8,3.7),(9.4,3.7)),((11.4,3.0),(11.4,2.0)),((9.4,1.3),(8.9,1.3)),((4.9,1.3),(4.4,1.3)),((2.4,2.0),(2.4,3.0))]:arrow(ax,a,b)
fig.suptitle('心理学解释：从抽象问题到可检验的证据',fontsize=18,fontweight='bold');save(fig,'research-chain')
# 2 Perfect correlation under a systematic shift.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(20,80,21)
ax[0].scatter(x,x+12,color=B,label='指定21对分数：Y=X+12');ax[0].plot([15,100],[15,100],ls='--',color=M,label='完全一致：Y=X')
ax[0].set(xlabel='第一次分数 X',ylabel='第二次分数 Y',xlim=(15,100),ylim=(15,100),title='（a）r=1，但每次都偏移12分');ax[0].legend(fontsize=10)
ax[1].bar(['真分数方差','误差方差'],[100,25],color=[B,R],width=.55)
for i,v in enumerate([100,25]):ax[1].text(i,v+3,str(v),ha='center')
ax[1].set(ylabel='方差 / 分²',ylim=(0,125),title='（b）简单经典模型：信度100/125=0.8')
fig.suptitle('信度、绝对一致与效度不能合为一个指标',fontsize=18,fontweight='bold');save(fig,'measurement')
# 3 Simpson reversal: exact invented counts, not a treatment estimate.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ok,n,rate,pooled=m.simpson();xx=np.arange(2)
for i,col in enumerate([B,R]):
    bars=ax[0].bar(xx+(i-.5)*.3,rate[i],.3,color=col,label='方案'+['A','B'][i])
    for j,b in enumerate(bars):ax[0].text(b.get_x()+b.get_width()/2,b.get_height()+.025,f'{ok[i,j]}/{n[i,j]}',ha='center',fontsize=11)
ax[0].set(xticks=xx,xticklabels=['安静','噪声'],ylabel='成功比例',ylim=(0,1.15),title='（a）每个情境内B均更高');ax[0].legend()
for i,col in enumerate([B,R]):
    vals=[pooled[i],rate[i].mean()];bars=ax[1].bar(xx+(i-.5)*.3,vals,.3,color=col,label='方案'+['A','B'][i])
    for v,b in zip(vals,bars):ax[1].text(b.get_x()+b.get_width()/2,v+.025,f'{100*v:g}%',ha='center')
ax[1].set(xticks=xx,xticklabels=['按原样本合并','情境各占50%'],ylabel='成功比例',ylim=(0,1.15),title='（b）总体结果随构成改变');ax[1].legend()
fig.suptitle('分母和情境构成决定总体比较的含义',fontsize=18,fontweight='bold');save(fig,'confounding')
# 4 Psychometric and response criterion.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));x=np.linspace(-3,13,801);theta=m.threshold()
ax[0].plot(x,m.psychometric(x),color=B,lw=2);ax[0].axhline(.5,color=M,ls=':',label='下限0.50');ax[0].axhline(.98,color=R,ls=':',label='上限0.98')
ax[0].plot([theta,theta], [.48,.75],ls='--',color=G);ax[0].plot([-3,theta],[.75,.75],ls='--',color=G,label=f'75%阈值≈{theta:.4f}')
ax[0].scatter([5],[.74],color=P,label='α=5，p=0.74',zorder=3);ax[0].set(xlabel='刺激量 / 教学单位',ylabel='二选一正确率',ylim=(.48,1.02),title='（a）阈值取决于函数与准则');ax[0].legend(fontsize=9,loc='lower right')
k=np.linspace(-2,3.5,601);H,F,_,_=m.detection(k)
ax[1].plot(k,H,color=B,lw=2,label='命中 H');ax[1].plot(k,F,color=R,lw=2,label='虚警 F')
for kk in [0,.75,1.5]:
    h,f,_,_=m.detection(kk);ax[1].scatter([kk,kk],[h,f],color=[B,R],s=25);ax[1].axvline(kk,color=M,ls=':',lw=.8)
ax[1].set(xlabel='回答“有”的证据判据 k',ylabel='条件反应概率',ylim=(-.03,1.03),title='（b）d′固定1.5，H与F随k一起变化');ax[1].legend()
fig.suptitle('感觉信息与回答规则需要分别检查',fontsize=18,fontweight='bold');save(fig,'perception-decision')
# 5 Functional diagram and a toy retention curve.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ax[0].set(xlim=(0,10),ylim=(0,5));ax[0].axis('off')
for x,y,txt,col in [(.3,3.0,'选择与编码',B),(5.7,3.0,'保持与变化',P),(5.7,.7,'线索与提取',G),(.3,.7,'任务回答',R)]:box(ax[0],x,y,3.5,1.0,txt,col,12)
arrow(ax[0],(3.9,3.5),(5.6,3.5));arrow(ax[0],(7.45,2.9),(7.45,1.8));arrow(ax[0],(5.6,1.2),(3.9,1.2));ax[0].text(4.9,4.65,'目标、语境、已有知识',ha='center',color=M,fontsize=12)
t=np.linspace(0,10,501);ax[1].plot(t,m.retention(t),color=B,lw=2);ax[1].axhline(.15,color=R,ls='--',label='指定下渐近线0.15')
ax[1].set(xlabel='时间 / 天',ylabel='指定模型的提取成功概率',ylim=(0,1.05),title='（b）p(t)=0.15+0.85exp(−t/2)');ax[1].legend()
fig.suptitle('选择、保持与提取：没有统一的记忆读数',fontsize=18,fontweight='bold');save(fig,'attention-memory')
# 6 Simultaneous prediction-error updates.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));h=m.rw_compound();n=np.arange(len(h))
ax[0].plot(n,h[:,0],color=B,lw=2,label='A');ax[0].plot(n,h[:,1],color=R,lw=2,label='B');ax[0].axvline(20,color=M,ls='--',label='从A+改为AB+')
ax[0].set(xlabel='训练试次（含起始状态0）',ylabel='模型联结强度',ylim=(-.03,1.08),title='（a）先20次A+，再15次AB+');ax[0].legend()
vals=[m.rw_compound(0,15)[-1,1],h[-1,1]];ax[1].bar(['无预训练\n15次AB+','20次A+预训练\n15次AB+'],vals,color=[G,R],width=.55)
for i,v in enumerate(vals):ax[1].text(i,v+.018,f'{v:.6f}',ha='center')
ax[1].set(ylabel='B的最终联结强度',ylim=(0,.61),title='（b）已被预测的结果留下很小的新误差')
fig.suptitle('预测误差模型中的线索竞争',fontsize=18,fontweight='bold');save(fig,'prediction-error')
# 7 Bayes counts and exact symmetric drift diffusion outputs.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ax[0].axis('off')
table=ax[0].table(cellText=[['80','20','100'],['180','720','900'],['260','740','1000']],rowLabels=['A类','非A类','合计'],colLabels=['有线索','无线索','合计'],cellLoc='center',loc='center',bbox=[.12,.35,.85,.43]);table.auto_set_font_size(False);table.set_fontsize(13)
for (r,c),cell in table.get_celld().items():cell.set_edgecolor('#d9e1e5');cell.set_facecolor('#eef3f6' if r==0 or c==-1 else 'white')
ax[0].text(.53,.15,'P(A | 有线索) = 80 / 260 ≈ 30.77%',transform=ax[0].transAxes,ha='center',color=B,fontsize=13);ax[0].set_title('（a）先验10%，命中80%，虚警20%')
a=np.linspace(.2,2.2,501);p,rt=m.diffusion_decision(a);a2=ax[1].twinx();a2.spines['right'].set_visible(True)
l1=ax[1].plot(a,p,color=B,lw=2,label='正确率');l2=a2.plot(a,rt,color=R,lw=2,label='平均总反应时间')
aa=np.array([.5,1.,2.]);pp,tt=m.diffusion_decision(aa);ax[1].scatter(aa,pp,color=B);a2.scatter(aa,tt,color=R)
ax[1].set(xlabel='边界距离 a / 证据单位',ylabel='正确率',ylim=(.5,1.02),title='（b）固定v=s=1，t₀=0.3秒');a2.set(ylabel='平均总反应时间 / 秒',ylim=(0,2.8));ax[1].legend(l1+l2,[l.get_label() for l in l1+l2],loc='lower right',fontsize=10)
fig.suptitle('概率方向与决策策略都影响结论',fontsize=18,fontweight='bold');save(fig,'judgment')
# 8 Not an exclusive or serial emotion theory.
fig,ax=plt.subplots(figsize=(14,5.5));ax.set(xlim=(0,14),ylim=(0,5));ax.axis('off')
for x,y,w,h,txt,col in [(.5,3.1,2.5,1.05,'声音或事件',B),(4.,3.1,2.5,1.05,'评价与意义',P),(8.,3.1,2.5,1.05,'主观体验',R),(8.,.8,2.5,1.05,'身体反应',G),(11.4,1.9,2.1,1.1,'行动与表达',B),(4.,.8,2.5,1.05,'目标与成本',P)]:box(ax,x,y,w,h,txt,col,13)
for a,b in [((3.1,3.63),(3.9,3.63)),((6.6,3.63),(7.9,3.63)),((6.5,3.05),(7.9,1.7)),((9.25,3.0),(9.25,2.0)),((10.6,3.55),(11.5,2.8)),((10.6,1.45),(11.5,2.05)),((5.25,1.95),(5.25,3.0))]:arrow(ax,a,b)
ax.text(1.75,1.35,'经验、关系与文化\n参与解释和表达',ha='center',va='center',color=M,fontsize=13)
fig.suptitle('情绪与动机：体验、身体和情境共同进入问题',fontsize=18,fontweight='bold');save(fig,'emotion-context')
# 9 Cohort example and mathematical overlap.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));ages1=np.array([40,50,60]);ages2=np.array([60,70,80]);y1=np.array([80,78,76]);y2=np.array([66,64,62])
ax[0].plot(ages1,y1,'o-',color=B,lw=2,label='队列1纵向');ax[0].plot(ages2,y2,'o-',color=G,lw=2,label='队列2纵向');ax[0].plot([40,60],[80,66],'--',color=R,label='同一日历起点的横断比较')
ax[0].set(xlabel='年龄 / 岁',ylabel='虚构任务分数',ylim=(57,85),title='（a）横断差14分，各队列20年变4分');ax[0].legend(fontsize=9)
x=np.linspace(-4,4.5,1001);p1,p2=norm.pdf(x),norm.pdf(x-.5);ax[1].plot(x,p1,color=B,label='均值0，SD=1');ax[1].plot(x,p2,color=R,label='均值0.5，SD=1');ax[1].fill_between(x,0,np.minimum(p1,p2),color=P,alpha=.25,label=f'重叠{100*m.overlap():.2f}%')
ax[1].set(xlabel='指定标准化变量',ylabel='概率密度',title='（b）有均值差，仍有大量分布重叠');ax[1].legend(fontsize=10)
fig.suptitle('年龄差异不等于个体变化，组均值不代表每个人',fontsize=18,fontweight='bold');save(fig,'development-differences')
# 10 Exact variance of a balanced exchangeable hierarchy.
fig,ax=plt.subplots(1,2,figsize=(14,5.5));n=np.arange(10,101);se,naive=m.clustered_se(n)
ax[0].plot(n,se,color=B,lw=2,label='保留同人相关ρ=0.2');ax[0].plot(n,naive,color=R,lw=2,label='误当所有记录独立');ax[0].scatter([50,50],m.clustered_se(50),color=[B,R])
ax[0].set(xlabel='独立参与者数 n',ylabel='总均值标准误 / 指定单位',title='（a）每人20次，单次方差1');ax[0].legend()
mm=np.arange(1,201)
for rho,col in [(.2,B),(0,G)]:ax[1].plot(mm,np.sqrt((rho+(1-rho)/mm)/50),color=col,lw=2,label=f'同人相关ρ={rho:g}')
ax[1].axhline(np.sqrt(.2/50),color=M,ls=':',label='ρ=0.2时m→∞的极限');ax[1].set(xlabel='每人重复次数 m',ylabel='总均值标准误 / 指定单位',title='（b）固定50人，增加重复的收益有限');ax[1].legend(fontsize=9)
fig.suptitle('重复次数与独立参与者数不能互换',fontsize=18,fontweight='bold');save(fig,'uncertainty')
rh=m.rw_compound()
calc=dict(psychometric_threshold_75=m.threshold(),psychometric_at_alpha=float(m.psychometric(5)),detection=[dict(k=k,H=float(m.detection(k)[0]),F=float(m.detection(k)[1]),dprime=float(m.detection(k)[2]),c=float(m.detection(k)[3])) for k in [0.,.75,1.5]],simpson=dict(within=rate.tolist(),pooled=pooled.tolist(),equal_weight=rate.mean(1).tolist()),rw_after_pretraining=float(rh[20,0]),rw_final=rh[-1].tolist(),rw_no_pretraining=m.rw_compound(0,15)[-1].tolist(),bayes_posterior=m.posterior(),ddm=dict(a=aa.tolist(),correct=pp.tolist(),mean_total_RT_s=tt.tolist()),overlap=m.overlap(),cluster_se=list(map(float,m.clustered_se(50))),design_effect=4.8,variance_equivalent_sample_size=1000/4.8)
(REC/'calculations.json').write_text(json.dumps(calc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Repo-native course sketch: person observing information and choosing an answer.
sketch='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180" role="img" aria-labelledby="title desc"><title id="title">心理学：观察、思考与选择</title><desc id="desc">人物侧面轮廓内连接着信息节点，眼前有不同图形和两个选择框，体现对心理与行为的研究。</desc><rect width="320" height="180" fill="#f4f0e5"/><g fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M99 158v-24c-22-9-38-29-38-55 0-35 29-57 62-57 31 0 52 20 54 46l14 24-15 7v21c0 10-10 15-27 15v23" stroke="#61727d" stroke-width="2"/><path d="M78 159h92" stroke="#61727d" stroke-width="1.8"/><circle cx="157" cy="73" r="3" fill="#61727d" stroke="#61727d"/><path d="M91 62l31-12 19 37-33 24-17-49m31-12-14 61m33-24-50-25" stroke="#79639d" stroke-width="1.7"/><g fill="#f4f0e5" stroke="#79639d" stroke-width="2"><circle cx="91" cy="62" r="5"/><circle cx="122" cy="50" r="5"/><circle cx="141" cy="87" r="5"/><circle cx="108" cy="111" r="5"/></g><path d="M191 78l31-20m-25 35h27" stroke="#b44e37" stroke-width="1.6" stroke-dasharray="4 5"/><circle cx="242" cy="47" r="11" stroke="#22658c" stroke-width="2"/><path d="m269 37 12 21h-24z" stroke="#31755e" stroke-width="2"/><rect x="224" y="87" width="31" height="25" rx="5" stroke="#22658c" stroke-width="2"/><rect x="267" y="87" width="31" height="25" rx="5" stroke="#61727d" stroke-width="1.6"/><path d="m232 99 5 5 10-12m-32 41h78" stroke="#31755e" stroke-width="2"/></g></svg>'''
(ROOT/'public/figures/foundation-courses/psychology.svg').write_text(sketch+'\n',encoding='utf-8')
print(json.dumps(dict(figures=10,calculations=calc),ensure_ascii=False))
