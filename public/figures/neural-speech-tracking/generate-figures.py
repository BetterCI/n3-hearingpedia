from pathlib import Path
import numpy as np,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy.signal import butter,sosfiltfilt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
C=['#276a8c','#b75c3c','#59785b'];report={};rng=np.random.default_rng(261007)
def save(fig,name):
 fig.savefig(ROOT/(name+'.svg'),bbox_inches='tight');fig.savefig(ROOT/(name+'.png'),bbox_inches='tight');plt.close(fig)
def clean(ax):ax.grid(alpha=.15);ax.set_axisbelow(True)
fs=8000;t=np.arange(0,2,1/fs);env=.15+.65*(.5+.5*np.sin(2*np.pi*2.4*t))**2;wave=env*np.sin(2*np.pi*180*t)
neurot=np.arange(0,2,.01);sim=np.interp(np.maximum(neurot-.12,0),t,env)-.3+.12*rng.normal(size=len(neurot))
fig,axs=plt.subplots(3,1,figsize=(9.2,6.5),layout='constrained')
axs[0].plot(t,wave,color=C[0],lw=.55);axs[0].plot(t,env,color=C[1],lw=1.5,label='已知合成包络');axs[0].plot(t,-env,color=C[1],lw=1.2);axs[0].set(ylim=(-1,1),ylabel='相对幅度',title='A  合成声学波形及包络');axs[0].legend(fontsize=9,loc='upper right')
axs[1].plot(t,env,color=C[1],lw=1.7);axs[1].set(ylim=(0,1),ylabel='包络（相对单位）',title='B  作为模型输入的包络特征')
axs[2].plot(neurot,sim,color=C[2],lw=1.1);axs[2].set(ylabel='模拟响应（任意单位）',xlabel='时间 / s',title='C  带延迟和噪声的模拟记录：不是波形复制')
for ax in axs:ax.set_xlim(0,2);clean(ax)
save(fig,'01-signal-feature-response');report['waveform']={'synthetic_not_speech_recording':True,'max_abs':float(abs(wave).max()),'known_envelope_max':float(env.max()),'simulated_delay_s':.12}
fig,axs=plt.subplots(2,1,figsize=(9.2,4.7),layout='constrained')
for ax,labels,title in [(axs[0],['言语特征\n包络／频谱等','前向编码模型\n特征及延迟 → 响应','预测神经记录\n与实测响应比较'],'A  前向编码'),(axs[1],['多通道神经记录\n及时间延迟','后向重建模型\n响应 → 指定特征','重建言语特征\n与真实／候选特征比较'],'B  后向重建')]:
 ax.set(xlim=(0,10),ylim=(0,2));ax.axis('off');ax.set_title(title,loc='left',fontsize=12)
 for x,label in zip([.15,3.6,7.1],labels):
  ax.add_patch(Rectangle((x,.45),2.7,.95,fill=False,lw=1,edgecolor='#617480'));ax.text(x+1.35,.925,label,ha='center',va='center',fontsize=10)
 for x in [2.85,6.3]:ax.annotate('',(x+.65,.925),(x,.925),arrowprops={'arrowstyle':'->','lw':1.1,'color':'#617480'})
save(fig,'02-forward-backward');report['directions']={'schematic':True,'backward_weights_not_generators':True}
fs=50;t=np.arange(0,90,1/fs);x=sosfiltfilt(butter(3,7,fs=fs,output='sos'),rng.normal(size=len(t)));x=(x-x.mean())/x.std();lags=np.arange(26);tau=lags/fs
h=-.2*np.exp(-.5*((tau-.10)/.035)**2)+.3*np.exp(-.5*((tau-.23)/.055)**2)
X=np.stack([x[25-k:len(x)-k] for k in lags],axis=1);tt=t[25:];signal=X@h;y=signal+rng.normal(size=len(signal))*.7*signal.std()
train=np.flatnonzero(tt<59.5);test=np.flatnonzero(tt>=60.5);lambdas=np.logspace(-4,2,13);scores=[]
def fit(ids,lam):return np.linalg.solve(X[ids].T@X[ids]/len(ids)+lam*np.eye(26),X[ids].T@y[ids]/len(ids))
for lam in lambdas:
 rs=[]
 for lo,hi in [(0,20),(20,40),(40,59.5)]:
  val=train[(tt[train]>=lo+.5)&(tt[train]<hi-.5)];sub=train[(tt[train]<lo-.5)|(tt[train]>=hi+.5)]
  rs.append(float(np.corrcoef(X[val]@fit(sub,lam),y[val])[0,1]))
 scores.append(np.mean(rs))
lam=float(lambdas[np.argmax(scores)]);hh=fit(train,lam);pred=X[test]@hh;r=float(np.corrcoef(pred,y[test])[0,1])
fig,axs=plt.subplots(1,2,figsize=(10,4.8),gridspec_kw={'width_ratios':[1,1.5]},layout='constrained')
axs[0].plot(tau*1000,h,'--',color='#737d84',lw=2,label='生成数据的已知权重');axs[0].plot(tau*1000,hh,color=C[0],lw=2,label='训练数据估计');axs[0].axhline(0,color='#a4afb5',ls=':');axs[0].set(xlabel='延迟 / ms',ylabel='模型权重（任意单位）',title='A  合成时域响应函数');axs[0].legend(fontsize=9)
axs[1].plot(tt[test],y[test],color='#9ba7ad',lw=.8,label='含噪模拟记录');axs[1].plot(tt[test],pred,color=C[0],lw=1.4,label='独立数据预测');axs[1].set(xlim=(65,69),xlabel='记录时间 / s',ylabel='模拟响应（任意单位）',title=f'B  留出数据：全测试段相关 r = {r:.2f}');axs[1].legend(fontsize=9)
for ax in axs:clean(ax)
save(fig,'03-trf-heldout');report['ridge']={'synthetic':True,'fs_Hz':fs,'lags_s':[0,.5],'train_max_s':float(tt[train].max()),'test_min_s':float(tt[test].min()),'inner_validation':'three contiguous folds with 0.5 s guard','lambda_candidates':lambdas.tolist(),'selected_lambda':lam,'test_correlation':r,'coefficient_rmse':float(np.sqrt(np.mean((hh-h)**2))),'test_display_s':[65,69],'full_test_duration_s':float(len(test)/fs)}
fs=50;t=np.arange(0,30,1/fs);sos=butter(3,4,fs=fs,output='sos')
def lowpass_noise():return sosfiltfilt(sos,rng.normal(size=len(t)+4*fs))[2*fs:-2*fs]
a=lowpass_noise();b=lowpass_noise();a=(a-a.mean())/a.std();b=(b-b.mean())/b.std();rec=.8*a+.08*b+.8*lowpass_noise();rec=(rec-rec.mean())/rec.std();ra=float(np.corrcoef(rec,a)[0,1]);rb=float(np.corrcoef(rec,b)[0,1])
fig,axs=plt.subplots(1,2,figsize=(10,4.4),gridspec_kw={'width_ratios':[2.6,1]},layout='constrained')
for z,c,label in [(a,C[0],'候选 A'),(b,C[1],'候选 B'),(rec,C[2],'合成重建特征')]:axs[0].plot(t,z,color=c,lw=1.2,label=label)
axs[0].set(xlim=(0,4),xlabel='时间 / s',ylabel='标准化特征值',title='A  两个候选与模拟重建');axs[0].legend(fontsize=9,loc='upper right')
axs[1].bar(['A','B'],[ra,rb],color=C[:2],width=.5);axs[1].set(ylim=(-.15,1.05),ylabel='皮尔逊相关系数',title='B  全 30 s 的相关')
for i,v in enumerate([ra,rb]):axs[1].text(i,max(v,0)+.04,f'{v:.2f}',ha='center')
for ax in axs:clean(ax)
save(fig,'04-attention-candidates');report['attention']={'synthetic_linear_mixture_not_EEG_decoding':True,'r_A':ra,'r_B':rb,'duration_s':30,'standardized_not_waveform':True}
fig,axs=plt.subplots(2,1,figsize=(9.3,5.1),layout='constrained')
for ax,grouped in zip(axs,[False,True]):
 for trial in range(4):
  for seg in range(6):
   test=trial==3 if grouped else seg%3==2;ax.add_patch(Rectangle((trial*7+seg,.2),.86,.65,facecolor=C[1] if test else C[0]))
  ax.text(trial*7+2.9,1.08,f'完整试次 {trial+1}',ha='center',fontsize=10)
 ax.set(xlim=(-.3,27),ylim=(0,1.5),xticks=[],yticks=[],title='B  按完整试次划分：测试试次未参与训练' if grouped else 'A  同试次片段混入训练和测试：可能共享特征与噪声');ax.set_xlabel('蓝：训练；橙：测试。推广到新听者时，还需按听者划分。',fontsize=10)
save(fig,'05-validation');report['validation']={'schematic':True,'held_out_trial_not_held_out_person':True,'nonoverlap_not_independence':True}
assert report['waveform']['max_abs']<=1 and report['ridge']['train_max_s']<report['ridge']['test_min_s']
assert -1<=ra<=1 and -1<=rb<=1
(ROOT/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report['ridge'],ensure_ascii=False,indent=2))
