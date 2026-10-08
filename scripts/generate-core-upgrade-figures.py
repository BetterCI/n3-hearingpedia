"""Transparent synthetic figures for the 2026-10-09 local editorial batch.

No participant data, anatomy, clinical normal limits, or full auditory models.
One shared peak scale keeps all sound waveform figures within [-1, 1].
"""
from pathlib import Path
import shutil,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import correlate,correlation_lags,lfilter

ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':10,
 'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path',
 'axes.unicode_minus':False,'figure.dpi':150,'savefig.dpi':150})
C=['#215e83','#b75637','#457665','#8264a0'];rng=np.random.default_rng(20261009)
manifest=[]
def panel(n=1,w=9,h=3.5,rows=1):
 f,a=plt.subplots(rows,n,figsize=(w,h),layout='constrained',squeeze=False)
 return f,a.ravel()
def save(f,slug,name,parameters):
 d=ROOT/'public/figures'/slug;d.mkdir(parents=True,exist_ok=True)
 local=ROOT/'docs/drafts/assets'/slug;local.mkdir(parents=True,exist_ok=True)
 for ext in ['svg','png']:
  p=d/(name+'.'+ext);f.savefig(p,bbox_inches='tight',facecolor='white')
  if ext=='svg':
   p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
  shutil.copy2(p,local/p.name)
 plt.close(f);manifest.append({'slug':slug,'file':name+'.svg','source':'Original mathematical/synthetic illustration; no participant data','parameters':parameters})
def waveax(a):a.set_ylim(-1.08,1.08);a.set_ylabel('相对幅度');a.set_xlabel('时间 (ms)')

# Standard articles: one substantive new figure each.
s='amplitude-modulation';f,a=panel(2,h=3.6);t=np.arange(0,.15,1/48000)
for m,c in zip([.2,.8],C):
 x=(1+m*np.cos(2*np.pi*20*t))*np.cos(2*np.pi*400*t)/1.8
 assert np.max(np.abs(x))<=1.00001
 a[0].plot(t*1000,x,color=c,lw=.65,alpha=.75,label=f'm = {m}')
 a[1].stem([380,400,420],[m/2,1,m/2],linefmt=c,markerfmt='o',basefmt=' ')
a[0].legend();waveax(a[0]);a[1].set(xlabel='频率 (Hz)',ylabel='相对线幅度',xlim=(370,430),ylim=(0,1.12))
save(f,s,'am-spectrum',{'carrier_Hz':400,'modulation_Hz':20,'depths':[.2,.8],'shared_peak_scale':1.8})
s='atomic-speech-model';f,a=panel(2)
for ax,concentrated in zip(a,[False,True]):
 times=np.linspace(.06,.96,30) if not concentrated else np.linspace(.06,.4,30)
 bands=np.arange(30)%8 if not concentrated else np.arange(30)%3
 sc=ax.scatter(times,bands+1,c=np.linspace(.3,1,30),cmap='viridis',vmin=0,vmax=1,s=45)
 ax.set(xlabel='时间 (s)',ylabel='分析带序号',xlim=(0,1),ylim=(.5,8.5))
 ax.set_title('分散事件' if not concentrated else '集中事件')
f.colorbar(sc,ax=a.tolist(),label='示例权重',shrink=.7)
save(f,s,'atomic-events',{'events_each':30,'bands':8,'not_original_ASM_stimulus':True})
s='auditory-plasticity';f,a=panel();t=np.linspace(0,10,100)
for y,label,c in [(40+40*(1-np.exp(-t/2)),'训练材料',C[0]),(40+20*(1-np.exp(-t/3)),'新材料',C[1])]:a[0].plot(t,y,c=c,label=label)
a[0].plot([10,14,18],[80,74,70],c=C[0],ls='--',label='保持复测')
a[0].axvline(10,c='#888',ls=':',label='训练结束');a[0].set(xlabel='示例时间单位',ylabel='示例正确率 (%)',ylim=(0,100));a[0].legend()
save(f,s,'plasticity-curves',{'synthetic_learning_curves':True,'no_prescribed_training_dose':True})
s='binaural-integration';f,a=panel(2)
for ax,vals,title in zip(a,[[40,75,76,85],[35,40,65,85]],['接近较好单耳','互补信息被利用，仍有整合代价']):
 ax.bar(np.arange(4),vals,color=[C[0],C[1],C[2],C[3]]);ax.set_xticks(np.arange(4),['左耳','右耳','双耳','完整同耳']);ax.set(ylim=(0,100),ylabel='示例正确率 (%)');ax.set_title(title,fontsize=11)
save(f,s,'binaural-baselines',{'fictional_percentages':[[40,75,76,85],[35,40,65,85]]})
s='binaural-intelligibility-level-difference';f,a=panel();x=np.arange(3);n0=np.array([-4,0,-6]);npi=np.array([-9,-5,-7])
for i in x:a[0].plot([i-.12,i+.12],[n0[i],npi[i]],c='#8a969e',lw=1.5)
a[0].scatter(x-.12,n0,c=C[0],label='同相');a[0].scatter(x+.12,npi,c=C[1],label='反相');a[0].set_xticks(x,['A','B','C']);a[0].set(ylabel='示例 SRT (dB SNR)',xlabel='假设听者',ylim=(-11,2));a[0].legend()
save(f,s,'bild-paired',{'diotic':n0.tolist(),'antiphasic':npi.tolist(),'BILD_direction':'diotic minus antiphasic'})
s='channel-interaction';f,a=panel(2);idx=np.arange(8)
for ax,width in zip(a,[.45,1.3]):
 W=np.exp(-((idx[:,None]-idx[None,:])/width)**2/2);W/=W.sum(axis=0)
 im=ax.imshow(W,cmap='Blues',vmin=0,vmax=1,origin='lower',interpolation='nearest');ax.set(xlabel='输入通道',ylabel='输出位置');ax.set_title(f'扩散参数 {width}')
f.colorbar(im,ax=a.tolist(),label='归一化权重',shrink=.75)
save(f,s,'channel-mixing',{'channels':8,'Gaussian_widths':[.45,1.3],'column_normalized':True})
s='cochlear-synaptopathy';f,a=panel();N=np.arange(1,101)
for sync,c in zip([1,.6,.3],C):a[0].plot(N,N/100*sync,c=c,label=f'同步权重 {sync}')
a[0].set(xlabel='示例连接数',ylabel='归一化群体响应');a[0].legend()
save(f,s,'synapse-evidence',{'linear_teaching_model':'response = N/100 * synchrony','not_diagnostic':True})
s='confusion-matrix';f,a=panel(2);M1=np.eye(4)*.7
for i in range(4):M1[i,(i+1)%4]=.3
M2=np.eye(4)*.6+np.ones((4,4))*.1
for ax,M,title in zip(a,[M1,M2],['集中混淆','分散混淆']):
 im=ax.imshow(M,cmap='Blues',vmin=0,vmax=1);ax.set_xticks(range(4),list('ABCD'));ax.set_yticks(range(4),list('ABCD'));ax.set(xlabel='反应类别',ylabel='刺激类别');ax.set_title(title)
 for i in range(4):
  for j in range(4):ax.text(j,i,f'{M[i,j]*100:.0f}%',ha='center',va='center',color='white' if M[i,j]>.5 else '#243b4a')
f.colorbar(im,ax=a.tolist(),label='行比例',shrink=.75)
save(f,s,'confusion-patterns',{'matrix1':M1.tolist(),'matrix2':M2.tolist(),'row_sums':1})
s='f0-in-tfs';f,a=panel(1,rows=3,h=6);t=np.linspace(0,.12,3000);q=(1+np.cos(2*np.pi*110*t))/2
a[0].plot(t*1000,q,c=C[2]);a[0].set_ylabel('共同因子')
for i,ax in enumerate(a[1:]):
 E=.65+.2*np.cos(2*np.pi*(6+i*2)*t+i)
 ax.plot(t*1000,E,c='#788792',label='输入包络');ax.plot(t*1000,E*q,c=C[i],label='调制后');ax.set_ylim(0,1);ax.set_ylabel(f'带 {i+1} 相对幅度');ax.legend(loc='upper right',fontsize=9)
a[-1].set_xlabel('时间 (ms)');save(f,s,'f0intfs-modulation',{'ideal_factor_Hz':110,'not_full_F0inTFS_algorithm':True})
s='get-vocoder';f,a=panel(1,rows=2,h=5);t=np.arange(0,.035,1/48000);ts=np.arange(.003,.033,.005)
ys=[]
for sigma in [.0005,.002]:ys.append(sum(np.exp(-(t-t0)**2/(2*sigma**2))*np.cos(2*np.pi*1000*(t-t0)) for t0 in ts))
scale=max(max(abs(y)) for y in ys)
for ax,y,sigma in zip(a,ys,[.5,2]):ax.plot(t*1000,y/scale,c=C[0],lw=.8);waveax(ax);ax.set_title(f'幅度包络标准差 {sigma} ms')
save(f,s,'get-overlap',{'carrier_Hz':1000,'interval_ms':5,'sigmas_ms':[.5,2],'shared_scale':float(scale)})
s='mandarin-lexical-tone';f,a=panel(1,rows=2,h=5);t=np.linspace(0,1,500)
for c,ls in zip(C,['-','--']):a[0].plot(t,140+90*t,c=c,ls=ls,lw=2)
a[0].set(xlabel='归一化音节时间',ylabel='示例基频 (Hz)',title='两条件基频相同')
a[1].plot(t,.3+.6*t,c=C[0],label='幅度上升');a[1].plot(t,.9-.6*t,c=C[1],ls='--',label='幅度下降');a[1].set(xlabel='归一化音节时间',ylabel='相对包络',ylim=(0,1));a[1].legend()
save(f,s,'tone-cue-control',{'F0_range_Hz':[140,230],'not_DiTone_material':True})
s='n-of-m-coding';f,a=panel();v=np.array([.2,.35,.85,.65,.15,.4,.93,.5,.28,.75,.12,.3]);sel=np.argsort(v)[-4:]
a[0].bar(np.arange(12)+1,v,color=[C[0] if i in sel else '#d0dce3' for i in range(12)]);a[0].set(xlabel='候选分析通道',ylabel='示例选择量',ylim=(0,1.1));a[0].set_xticks(range(1,13))
save(f,s,'maxima-selection',{'m':12,'n':4,'selected_one_based':(sel+1).tolist()})
s='noise-induced-hearing-loss';f,a=panel();L=np.arange(0,19,3);T=2**(-L/3)
a[0].plot(L,T,'o-',c=C[0]);a[0].set(xlabel='相对声级增加 (dB)',ylabel='等声能所需的相对时长',yscale='log',ylim=(.01,1.2));a[0].set_xticks(L);a[0].set_yticks(T,[f'1/{int(1/v)}' if v<1 else '1' for v in T]);a[0].grid(alpha=.15)
save(f,s,'noise-energy',{'equal_energy_only':True,'not_safety_limit':True,'relative_levels_dB':L.tolist()})
s='temporal-limits-encoder';f,a=panel();orig=np.array([1000,1200]);sh=orig-800;stretch=orig/5
for x,y,c in zip([0,1,2],[orig,sh,stretch],C):
 a[0].scatter([x,x],y,c=c,s=60);a[0].plot([x,x],y,c=c,lw=2)
 for k,yy in enumerate(y):a[0].text(x+.07+(0.18 if x==2 and k else 0),yy,f'{yy:g} Hz',va='center',fontsize=9)
for i in range(2):a[0].plot([0,1], [orig[i],sh[i]],c='#adb8bd',ls='--');a[0].plot([0,2],[orig[i],stretch[i]],c='#d5dce0',ls=':')
a[0].set_xticks([0,1,2],['原始分量','共同下移 800 Hz','时间拉长五倍']);a[0].set(ylabel='频率 (Hz)',xlim=(-.3,2.65),ylim=(100,1350))
save(f,s,'tle-translation',{'original_Hz':orig.tolist(),'shift_Hz':800,'time_scale':5,'not_full_TLE_algorithm':True})
s='zodiac-in-noise';f,a=panel();x=np.linspace(-20,0,300)
for slope,c in zip([.35,.85],C):y=1/12+(1-1/12)/(1+np.exp(-slope*(x+10)));a[0].plot(x,y,c=c,label=f'斜率参数 {slope}')
a[0].axhline(1/12,c='#888',ls=':');a[0].set(xlabel='示例信噪比 (dB)',ylabel='单项目示例正确率',ylim=(0,1.03));a[0].legend()
save(f,s,'zin-psychometric',{'guess_floor':1/12,'not_official_ZIN_scoring':True,'center_dB':-10})

# Interaural time difference: delay signs checked against analytic definition.
s='interaural-time-difference';f,a=panel();deg=np.linspace(-90,90,181);th=np.deg2rad(deg);tau=.0875/343*(th+np.sin(th))*1e6
a[0].plot(deg,tau,c=C[0]);a[0].axhline(0,c='#aaa',lw=.7);a[0].axvline(0,c='#aaa',lw=.7);a[0].set(xlabel='方位角 (度，向左为正)',ylabel='右耳减左耳时间 (μs)');a[0].text(15,70,'正值：左耳先到',color=C[0]);a[0].text(-85,-85,'负值：右耳先到',color=C[1])
save(f,s,'itd-geometry',{'sphere_radius_m':.0875,'sound_speed_m_s':343,'high_frequency_geometry_only':True})
f,a=panel(1,rows=2,h=6);t=np.arange(0,.006,1/48000);tau=.0002
a[0].plot(t*1000,np.cos(2*np.pi*500*t),c=C[0],label='左耳');a[0].plot(t*1000,np.cos(2*np.pi*500*(t-tau)),c=C[1],ls='--',label='右耳');waveax(a[0]);a[0].legend()
freq=np.linspace(0,5000,1000);raw=360*freq*tau;wrapped=(raw+180)%360-180
a[1].plot(freq,raw,c=C[0],label='未取模');a[1].plot(freq,wrapped,c=C[1],label='[-180°, 180°)');a[1].set(xlabel='频率 (Hz)',ylabel='左相位减右相位 (度)');a[1].legend()
save(f,s,'itd-phase',{'time_difference_us':200,'wave_carrier_Hz':500,'sign':'left phase minus right'})
f,a=panel(2,h=4);t=np.arange(0,.08,1/48000);tau=.003;E=lambda z:(1+.9*np.cos(2*np.pi*20*z))/1.9
L=E(t)*np.cos(2*np.pi*300*t)
for ax,R,title in zip(a,[E(t-tau)*np.cos(2*np.pi*300*t),E(t-tau)*np.cos(2*np.pi*300*(t-tau))],['只延迟包络','整体波形延迟']):
 ax.plot(t*1000,L,c=C[0],lw=.6,label='左耳');ax.plot(t*1000,R,c=C[1],lw=.6,alpha=.8,label='右耳');ax.plot(t*1000,E(t),c=C[0],lw=1.2);ax.plot(t*1000,E(t-tau),c=C[1],ls='--',lw=1.2);waveax(ax);ax.set_title(title);ax.legend(fontsize=9)
save(f,s,'itd-envelope',{'carrier_Hz':300,'envelope_Hz':20,'delay_ms':3,'teaching_low_carrier':True})
f,a=panel(2);fs=48000;t=np.arange(0,.12,1/fs);lag_samples=10
for ax,L,title in zip(a,[np.cos(2*np.pi*500*t),rng.normal(size=len(t))],['周期纯音','宽带噪声']):
 R=np.r_[np.zeros(lag_samples),L[:-lag_samples]];cc=correlate(R,L,mode='full')/np.sqrt(np.dot(L,L)*np.dot(R,R));lags=correlation_lags(len(R),len(L))/fs*1000;keep=abs(lags)<=6
 ax.plot(lags[keep],cc[keep],c=C[0]);ax.axvline(lag_samples/fs*1000,c=C[1],ls='--');ax.set(xlabel='比较滞后 (ms)',ylabel='归一化互相关',title=title,ylim=(-1.05,1.05))
save(f,s,'itd-correlation',{'fs_Hz':fs,'delay_samples':10,'actual_delay_us':lag_samples/fs*1e6,'correlation':'right versus left; positive lag for delayed right'})
# Fifth figure already provided by combined wave / phase plot? Four markers in ITD.
# Add a distinct fractional-delay figure for publication and explicit text insertion.
f,a=panel();freq=np.linspace(0,3000,400)
for delay,c,label in zip([200,187.5,208.333333],C,['目标 200 μs','9 点：187.5 μs','10 点：208.3 μs']):a[0].plot(freq,360*freq*delay*1e-6,c=c,label=label)
a[0].set(xlabel='频率 (Hz)',ylabel='左相位减右相位 (度)');a[0].legend()
save(f,s,'itd-sampling',{'fs_Hz':48000,'delays_us':[200,187.5,208.333333],'no_fractional_delay_model_run':True})

# ABR: synthetic potentials in microvolts, not audio normalization.
s='auditory-brainstem-response';t=np.linspace(-1,12,2600)
def gauss(t,mu,width):return np.exp(-(t-mu)**2/(2*width**2))
def abr(t,shift=0,amp=1):return amp*(.16*gauss(t,1.7+shift,.14)-.09*gauss(t,2+shift,.16)+.2*gauss(t,3.8+shift,.2)-.12*gauss(t,4.25+shift,.2)+.34*gauss(t,5.5+shift,.27)-.2*gauss(t,6.1+shift,.28))
f,a=panel();y=abr(t);a[0].plot(t,y,c=C[0]);a[0].axvline(0,c='#999',ls=':')
for peak,label in zip([1.7,3.8,5.5],['I','III','V']):a[0].annotate(label,(peak,abr(np.array([peak]))[0]),xytext=(peak,.43),ha='center',arrowprops={'arrowstyle':'-','color':'#788792'})
a[0].annotate('',xy=(6.8,float(abr(np.array([5.5]))[0])),xytext=(6.8,float(abr(np.array([6.1]))[0])),arrowprops={'arrowstyle':'<->','color':C[1]});a[0].text(7.1,.07,'峰—谷幅度',color=C[1],fontsize=9)
a[0].set(xlabel='刺激基准后时间 (ms)',ylabel='合成电位 (μV)',ylim=(-.27,.5));save(f,s,'abr-waveform',{'synthetic_peaks_ms':[1.7,3.8,5.5],'not_normal_ranges':True})
f,a=panel(2);freq=np.array([.5,1,2,4,8]);travel=np.array([4.5,3.3,2.3,1.5,1]);input_comp=4.5-travel
for ax,inp,title in zip(a,[np.zeros(5),input_comp],['同时输入','提前低频的补偿输入']):
 ax.scatter(inp,freq,c=C[1],label='输入时刻');ax.scatter(inp+travel,freq,c=C[0],label='假设到达时刻')
 for z,b,d in zip(inp,freq,travel):ax.plot([z,z+d],[b,b],c='#aab8c0',lw=1)
 ax.set(xlabel='相对时间 (ms)',ylabel='频率 (kHz)',title=title,xlim=(-.3,5));ax.legend(fontsize=9)
save(f,s,'abr-chirp',{'frequencies_kHz':freq.tolist(),'assumed_travel_delays_ms':travel.tolist(),'not_commercial_chirp':True})
f,a=panel(2,h=4);base=abr(t);noise=rng.normal(0,.7,size=(256,len(t)));artifact=.15*gauss(t,.5,.1)
for n,c in zip([16,64,256],C):a[0].plot(t,base+noise[:n].mean(0),c=c,lw=.75,label=f'{n} 次平均')
a[0].plot(t,base+artifact,c=C[3],ls='--',label='含锁时伪迹的期望');a[0].set(xlabel='时间 (ms)',ylabel='电位 (μV)',xlim=(-1,9));a[0].legend(fontsize=8)
n=np.arange(1,300);a[1].plot(n,.7/np.sqrt(n),c=C[0]);a[1].set(xlabel='平均试次数',ylabel='理想独立噪声标准差 (μV)')
save(f,s,'abr-averaging',{'independent_noise_sd_uV':.7,'trials':256,'locked_artifact_in_expected_curve':True})
f,a=panel(1,rows=4,h=7)
for ax,level,amp,shift in zip(a,[60,40,30,20],[1,.7,.4,0],[0,.3,.65,1]):
 for c in C[:2]:ax.plot(t,abr(t,shift,amp)+rng.normal(0,.017,size=len(t)),c=c,lw=.55)
 ax.set(xlabel='时间 (ms)',ylabel='电位 (μV)',ylim=(-.3,.45),xlim=(0,10));ax.set_title(f'教学水平 {level} dB nHL',fontsize=10)
save(f,s,'abr-levels',{'levels_nHL_teaching':[60,40,30,20],'amplitudes':[1,.7,.4,0],'not_eHL_conversion':True})
f,a=panel(1,rows=3,h=6);neural=abr(t);cm=.18*gauss(t,1,.7)*np.sin(2*np.pi*1.5*t)
a[0].plot(t,neural+cm,c=C[0],label='正极性');a[0].plot(t,neural-cm,c=C[1],ls='--',label='反极性');a[0].legend(fontsize=9)
a[1].plot(t,neural,c=C[2]);a[1].set_title('理想半和：极性不变部分',fontsize=10)
a[2].plot(t,cm,c=C[3]);a[2].set_title('理想半差：极性反转部分',fontsize=10)
for ax in a:ax.set(xlabel='时间 (ms)',ylabel='合成电位 (μV)',xlim=(-1,9))
save(f,s,'abr-polarity',{'ideal_neural_invariant':True,'ideal_reversing_component':True,'not_diagnostic':True})

# EEG: voltage reference, timing, filtering, averaging, and dependent windows.
s='electroencephalography';f,a=panel(2,h=4);t=np.linspace(0,1,1200);common=5*np.sin(2*np.pi*2*t);X=np.array([common+3*np.sin(2*np.pi*9*t+p) for p in [0,1,2]]);Xavg=X-X.mean(axis=0)
assert np.allclose(X[0]-X[1],Xavg[0]-Xavg[1])
for ax,xx,title in zip(a,[X,Xavg],['共同参考记录','平均重参考']):
 for y,c,k in zip(xx,C,range(3)):ax.plot(t,y,c=c,lw=.8,label=f'通道 {k+1}')
 ax.set(xlabel='时间 (s)',ylabel='电位 (μV)',ylim=(-10,10),title=title);ax.legend(fontsize=8)
save(f,s,'eeg-reference',{'synthetic_channels':3,'pairwise_differences_preserved':True})
f,a=panel();t=np.linspace(-100,400,2000);base=5*gauss(t,120,18);fixed=5*gauss(t,140,18);shifts=rng.normal(20,25,1000);jitter=np.mean([5*gauss(t,120+x,18) for x in shifts],axis=0)
for y,c,label in zip([base,fixed,jitter],C,['无附加延迟','固定延迟 20 ms','均值 20 ms、标准差 25 ms 的抖动']):a[0].plot(t,y,c=c,label=label)
a[0].set(xlabel='触发后时间 (ms)',ylabel='平均电位 (μV)');a[0].legend(fontsize=9)
save(f,s,'eeg-jitter',{'true_peak_ms':120,'fixed_delay_ms':20,'jitter_mean_ms':20,'jitter_sd_ms':25})
f,a=panel();t=np.arange(-100,201);x=np.where(t>=0,np.exp(-t/35),0)*5;kernel=np.ones(31)/31;center=np.convolve(x,kernel,'same');causal=lfilter(kernel,[1],x)
for y,c,label in zip([x,center,causal],C,['原始瞬态','居中非因果平滑','因果平滑']):a[0].plot(t,y,c=c,label=label)
a[0].axvline(0,c='#999',ls=':');a[0].set(xlabel='真实起始后时间 (ms)',ylabel='合成电位 (μV)');a[0].legend()
save(f,s,'eeg-filter',{'smoothing_samples':31,'sample_interval_ms':1,'not_software_defaults':True})
f,a=panel(2,rows=2,h=6);t=np.linspace(0,1,1000);env=gauss(t,.5,.15);phase=rng.uniform(0,2*np.pi,100)
for j,ph,title in zip(range(2),[np.zeros(100),phase],['相位一致','随机相位']):
 X=np.array([5*env*np.sin(2*np.pi*10*t+p) for p in ph])
 for y in X[:6]:a[j].plot(t,y,alpha=.35,lw=.7)
 a[j].set(title=title,ylabel='单试次电位 (μV)',ylim=(-6,6));a[j+2].plot(t,X.mean(0),c=C[j]);a[j+2].set(xlabel='时间 (s)',ylabel='平均电位 (μV)',ylim=(-6,6))
save(f,s,'eeg-phase-power',{'frequency_Hz':10,'trials':100,'equal_single_trial_amplitude':True})
f,a=panel();phi=.95;lag=np.arange(0,101);a[0].plot(lag,phi**lag,c=C[0]);a[0].set(xlabel='窗口或观测间隔 (单位步长)',ylabel='示例序列相关',ylim=(0,1.05));a[0].axhline(0,c='#aaa',lw=.7)
save(f,s,'eeg-validation',{'theoretical_AR1_phi':phi,'not_model_accuracy':True})

out=ROOT/'docs/drafts/batch-figure-manifest.json';out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8')
from PIL import Image,ImageOps,ImageDraw
thumbs=[]
for r in manifest:
 p=ROOT/'docs/drafts/assets'/r['slug']/Path(r['file']).with_suffix('.png')
 im=Image.open(p).convert('RGB');im.thumbnail((650,420));canvas=Image.new('RGB',(680,465),'white');canvas.paste(im,((680-im.width)//2,35));ImageDraw.Draw(canvas).text((12,10),r['slug']+'/'+r['file'],fill='black');thumbs.append(canvas)
for start in range(0,len(thumbs),10):
 sheet=Image.new('RGB',(1360,465*5),'#dce3e8')
 for k,im in enumerate(thumbs[start:start+10]):sheet.paste(im,((k%2)*680,(k//2)*465))
 sheet.save(ROOT/'docs/drafts'/f'batch-figures-contact-{start//10+1}.png')
print(json.dumps({'figures':len(manifest),'slugs':len(set(r['slug'] for r in manifest))}))
