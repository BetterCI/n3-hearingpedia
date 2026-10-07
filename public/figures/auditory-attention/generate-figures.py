from pathlib import Path
import numpy as np,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.signal import butter,sosfiltfilt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':140})
C=['#276a8c','#b75c3c','#59785b'];reports={}
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight');plt.close(fig)
def clean(ax):ax.grid(alpha=.15);ax.set_axisbelow(True)
fs=16000;t=np.arange(0,1.2,1/fs)
ea=.12+.7*(.5+.5*np.sin(2*np.pi*3*t))**2
eb=.12+.7*(.5+.5*np.cos(2*np.pi*4.1*t+.3))**2
a=ea*np.sin(2*np.pi*210*t);b=eb*np.sin(2*np.pi*330*t);mix=(a+b)/2
fig,axs=plt.subplots(3,1,figsize=(9.3,6.9),layout='constrained')
for ax,s,title,c in zip(axs,[a,b,mix],['A  声源 A（合成载波）','B  声源 B（合成载波）','C  相同物理混合输入：可按指令关注 A 或 B'],C):
 ax.plot(t,s,color=c,lw=.5);ax.set(xlim=(0,1.2),ylim=(-1,1),ylabel='相对幅度',title=title);clean(ax)
axs[-1].set_xlabel('时间 / s');save(fig,'01-mixture-selection')
reports['mixture']={'fs':fs,'mix':'(A+B)/2','max_amplitude':float(max(abs(a).max(),abs(b).max(),abs(mix).max())),'synthetic_not_speech':True}
fig,axs=plt.subplots(2,1,figsize=(9.3,5.3),layout='constrained')
for ax,switch in zip(axs,[False,True]):
 for row in range(2):ax.broken_barh([(1,1.8),(4,1.8),(7,1.8)],(row+.1,.55),facecolors=C[row],alpha=.55)
 ax.set(xlim=(0,10),ylim=(0,2.3),yticks=[.4,1.4],yticklabels=['声源 A','声源 B'],title='B  切换目标：A → B' if switch else 'A  维持目标：A → A')
 for start,target in [(0,'A'),(3,'B' if switch else 'A'),(6,'B' if switch else 'A')]:
  ax.axvline(start+.2,color='#666',ls=':',lw=1);ax.text(start+.4,1.9,'关注 '+target,fontsize=11,color=C[0 if target=='A' else 1]);row=0 if target=='A' else 1;ax.plot([start+1,start+2.8],[row+.72,row+.72],color=C[row],lw=3)
 clean(ax)
axs[-1].set_xlabel('示意时间 / s');save(fig,'02-maintain-switch');reports['switch']={'schematic':True,'same_sounds_different_instruction':True}
rng=np.random.default_rng(241007);fs=100;t=np.arange(0,20,1/fs);sos=butter(3,5,fs=fs,output='sos')
e1=sosfiltfilt(sos,rng.normal(size=len(t)));e2=sosfiltfilt(sos,rng.normal(size=len(t)))
e1=(e1-e1.mean())/e1.std();e2=(e2-e2.mean())/e2.std();rec=.7*e1+.12*e2+.8*rng.normal(size=len(t));rec=sosfiltfilt(sos,rec)
rec=(rec-rec.mean())/rec.std();r1=float(np.corrcoef(rec,e1)[0,1]);r2=float(np.corrcoef(rec,e2)[0,1])
fig,axs=plt.subplots(1,2,figsize=(10,4.4),gridspec_kw={'width_ratios':[3,1]},layout='constrained')
for s,c,label in [(e1,C[0],'候选 A 包络'),(e2,C[1],'候选 B 包络'),(rec,C[2],'合成重建包络')]:axs[0].plot(t,s,color=c,lw=1.1,alpha=.85,label=label)
axs[0].set(xlim=(0,4),xlabel='时间 / s',ylabel='标准化特征值',title='A  候选特征与合成重建特征');axs[0].legend(fontsize=9)
axs[1].bar(['A','B'],[r1,r2],color=C[:2],width=.55);axs[1].set(ylim=(-.1,1),ylabel='皮尔逊相关系数',title='B  全 20 s 的相关')
for i,r in enumerate([r1,r2]):axs[1].text(i,r+.025,f'{r:.2f}',ha='center')
for ax in axs:clean(ax)
save(fig,'03-envelope-decision');reports['reconstruction']={'synthetic':True,'r_A':r1,'r_B':r2,'standardized_features_not_pressure':True}
t=np.arange(0,30,.01);state=np.where(t<10,1.,0.);fig,ax=plt.subplots(figsize=(9.2,4.4),layout='constrained');ax.plot(t,state,'--',color='#65727b',lw=1.5,label='理想目标标签：A → B')
for L,c in zip([2,8],C):
 y=np.where(t<10,1,np.maximum(0,1-(t-10)/L));ax.plot(t,y,color=c,lw=2,label=f'过去 {L} s 的矩形窗平均');ax.scatter([10+L/2],[.5],color=c,zorder=4)
ax.axhline(.5,color='#a6afb5',ls=':');ax.axvline(10,color='#a6afb5',ls=':');ax.set(xlim=(5,22),ylim=(-.08,1.08),xlabel='时间 / s',ylabel='窗内属于 A 的样本比例',title='历史窗口引起的过渡（理想标签模拟）');ax.legend(fontsize=10);clean(ax);save(fig,'04-window-delay');reports['window']={'switch_s':10,'window_s':[2,8],'decision_delay_at_half_s':[1,4],'not_neural_latency':True}
fig,axs=plt.subplots(2,1,figsize=(9.3,5.5),layout='constrained')
for ax,safe in zip(axs,[False,True]):
 for trial in range(4):
  for segment in range(6):
   test=(trial==3) if safe else (segment%3==2)
   x=trial*7+segment;ax.add_patch(Rectangle((x,.35),.86,.7,facecolor=C[1] if test else C[0]));
  ax.text(trial*7+2.9,1.18,f'试次 {trial+1}',ha='center',fontsize=10)
 ax.set(xlim=(-.3,27),ylim=(0,1.7),yticks=[],xticks=[],title='B  按完整试次划分：示例为留出试次 4' if safe else 'A  同试次片段分散到训练与测试：可能利用试次特征');ax.set_xlabel('橙：测试片段；蓝：训练片段')
save(fig,'05-validation');reports['validation']={'schematic':True,'nonoverlap_is_not_independence':True}
assert reports['mixture']['max_amplitude']<=1
(ROOT/'figure-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf8');print('5 figures generated; waveform amplitude <= 1')
