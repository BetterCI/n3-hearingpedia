"""Original teaching plots and calculations, not clinical norms or a fitting algorithm."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/drafts/assets/real-ear-measurement';OUT.mkdir(parents=True,exist_ok=True)
RESEARCH=ROOT/'docs/research/real-ear-2026-10-11';RESEARCH.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name(),'svg.fonttype':'path','axes.unicode_minus':False,'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.titlepad':14})
P,T,G,O='#6952b4','#267f80','#667085','#b66a2c'
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'));fig.savefig(OUT/(name+'.png'),dpi=150);plt.close(fig)
def foot(fig,text):fig.text(.055,.025,text,fontsize=9,color=G)
def frequencies(ax,fs):
 ax.set_xscale('log');ax.set_xticks(fs,labels=[str(int(f)) for f in fs]);ax.tick_params(axis='x',labelsize=9);ax.set_xlabel('频率（Hz，对数轴）')

# Pure-tone linear teaching curves, reference input 65 dB SPL at each frequency.
f=np.array([250,500,1000,2000,3000,4000,6000]);reug=np.array([0,1,3,9,15,10,5]);reag=np.array([8,13,20,24,26,24,18]);reig=reag-reug
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.065,right=.97,top=.82,bottom=.24,wspace=.27)
ax[0].plot(f,np.full(len(f),65),color=G,ls=':',label='参考输入：65 dB SPL')
ax[0].plot(f,65+reug,'o-',color=T,label='REUR：未戴助听器')
ax[0].plot(f,65+reag,'o-',color=P,label='REAR：助听器开启')
ax[0].set(title='响应：测量点的绝对声压级',ylabel='声压级（dB SPL）',ylim=(60,102));ax[0].legend(frameon=False,fontsize=10)
ax[1].plot(f,reug,'o-',color=T,label='REUG = REUR − 输入')
ax[1].plot(f,reag,'o-',color=P,label='REAG = REAR − 输入')
ax[1].plot(f,reig,'s--',color=O,label='REIG = REAG − REUG')
ax[1].set(title='增益：不同参照下的声级差',ylabel='增益（dB）',ylim=(-1,36));ax[1].legend(frameon=False,fontsize=10)
for a in ax:frequencies(a,f)
foot(fig,'原创线性教学响应；逐个频率的纯音输入均为65 dB SPL，不能当作宽带言语各频带的输入。\n2 kHz例子：REUR=74，REAR=89 dB SPL；REUG=9，REAG=24，REIG=15 dB。非人群常模。')
save(fig,'01-responses-and-gains')

# Lossless uniform tube and real positive load reflection coefficient, near drum.
c,r=343.,.8
def pressure_ratio(f,d):
 k=2*np.pi*np.asarray(f)/c
 return np.abs(np.exp(1j*k*d)+r*np.exp(-1j*k*d))/(1+r)
fs=np.geomspace(125,10000,1200);distances=[.005,.010,.015]
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.065,right=.97,top=.82,bottom=.24,wspace=.3)
for d,color,ls in zip(distances,[P,T,G],['-','--',':']):ax[0].plot(fs,20*np.log10(pressure_ratio(fs,d)),color=color,ls=ls,lw=2,label=f'd = {int(d*1000)} mm')
ax[0].set(title='同一负载：位置改变测得的总声压',ylabel='相对负载表面声级（dB）',ylim=(-22,2));ax[0].legend(frameon=False)
frequencies(ax[0],[125,250,500,1000,2000,4000,8000,10000])
ax[0].set_xticklabels(['125','250','500','1k','2k','4k','8k','10k'])
ds=np.linspace(0,.025,600);fr=6000;node=c/(4*fr)
ax[1].plot(ds*1000,20*np.log10(pressure_ratio(fr,ds)),color=P,lw=2)
ax[1].axvline(node*1000,color=T,ls='--');ax[1].text(1.5,-16,'6 kHz下\n低谷约14.3 mm',color=T,fontsize=10)
ax[1].set(title='固定6 kHz：总声压沿管道变化',xlabel='距负载表面的距离 d（mm）',ylabel='相对负载表面声级（dB）',ylim=(-22,2),xlim=(0,25))
foot(fig,'原创一维无损管道：p(d)=p+ [exp(jkd)+r exp(−jkd)]，r=0.8，c=343 m/s，负载表面d=0。\n曲线仅说明相干反射；不模拟真实耳道，也不提供临床探管插入距离或安全位置。')
save(fig,'02-probe-position')

# Sampled third-octave-band speech-like levels, not actual ISTS or NAL/DSL targets.
fb=np.array([250,500,1000,2000,4000,6000]);offset=np.array([-10,-11,-16,-21,-26,-30]);gain65=np.array([12,18,27,34,42,44]);threshold=np.array([38,44,49,57,66,70])
errors={55:np.array([-1,-1,-3,-5,-7,-6]),65:np.array([0,-1,-2,-4,-6,-5]),75:np.array([1,0,-1,-2,-4,-3])}
fig,ax=plt.subplots(1,3,figsize=(12.8,5.5));fig.subplots_adjust(left=.06,right=.98,top=.82,bottom=.28,wspace=.22)
speech={}
for a,L in zip(ax,[55,65,75]):
 target=L+offset+gain65+(65-L)/2;measured=target+errors[L]
 speech[str(L)]={'target_band_spl':target.tolist(),'measured_band_spl':measured.tolist(),'error_db':errors[L].tolist()}
 a.plot(fb,target,'o--',color=G,label='教学目标');a.plot(fb,measured,'o-',color=P,label='教学测得响应')
 a.plot(fb,threshold,':',color=T,label='已转换的听阈');a.set(title=f'输入总声级 {L} dB SPL',ylim=(30,100));frequencies(a,fb)
 a.set_ylabel('采样频带声级（dB SPL）' if L==55 else '');a.legend(frameon=False,fontsize=8,loc='upper left')
foot(fig,'原创言语样频谱，仅绘六个三分之一倍频程频带：频带输入=总声级+所列频谱偏移；其余频带未画。\n目标增益随输入每增20 dB减少10 dB，各频带压缩比为2；听阈和目标均为假设，非NAL、DSL或ISTS数据。\n平均频谱高于听阈不等于言语全部时刻都可听；本图没有绘制百分位或不舒适级。')
save(fig,'03-multiple-input-levels')

# Matched transducer and coupling hypothetical transforms at 1 kHz.
recd=np.array([5,12]);coupler=80;ear=coupler+recd;target=92;required=target-recd
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.065,right=.97,top=.81,bottom=.25,wspace=.3)
x=np.arange(2);names=['声学条件P\nRECD = 5 dB','声学条件Q\nRECD = 12 dB']
ax[0].bar(x,ear,color=[P,T],width=.45);ax[0].axhline(coupler,color=G,ls='--',label='相同耦合腔响应：80 dB SPL')
for a,v in zip(x,ear):ax[0].text(a,v+1,f'{v} dB SPL',ha='center',fontsize=11)
ax[0].set(title='耦合腔 → 耳内：加上相容RECD',ylabel='声压级（dB SPL）',ylim=(0,110),xticks=x,xticklabels=names);ax[0].legend(frameon=False,fontsize=9,loc='upper left')
ax[1].bar(x,required,color=[P,T],width=.45);ax[1].axhline(target,color=G,ls='--',label='相同耳内目标：92 dB SPL')
for a,v in zip(x,required):ax[1].text(a,v-7,f'{v} dB SPL',ha='center',fontsize=11,color='white')
ax[1].set(title='耳内目标 → 耦合腔：减去相容RECD',ylabel='耦合腔目标（dB SPL）',ylim=(0,110),xticks=x,xticklabels=names);ax[1].legend(frameon=False,fontsize=9,loc='upper left')
foot(fig,'原创1 kHz教学算例；假设声源、耦合腔、耳塞与相关修正相容。P/Q不是成人/儿童常模。\n这里只表示声压级转换，不表示传声功率、舒适度或听力改善；真实RECD是频率相关曲线。')
save(fig,'04-recd-transform')

calc={'scope':'Original teaching assumptions; no clinical norms, actual prescriptive targets or patient data','response_at_2khz':{'input_spl':65,'REUR_spl':74,'REAR_spl':89,'REUG_db':9,'REAG_db':24,'REIG_db':15},'wave':{'reflection_coefficient':r,'sound_speed_m_s':c,'first_minimum_6khz_distance_mm':node*1000,'minimum_relative_level_db':float(20*np.log10((1-r)/(1+r)))},'speech':{'frequencies_hz':fb.tolist(),'band_input_offsets_db':offset.tolist(),'gain_at_65_db':gain65.tolist(),'assumed_threshold_band_spl':threshold.tolist(),'curves':speech,'compression_ratio':2,'shown_input_energy_fraction':float(np.sum(10.**(offset/10)))},'recd':{'frequency_hz':1000,'recd_db':recd.tolist(),'coupler_spl':coupler,'ear_spl':ear.tolist(),'ear_target_spl':target,'required_coupler_spl':required.tolist(),'threshold_hl':45,'coupler_reference_threshold_spl':7,'converted_ear_threshold_spl':(45+7+recd).tolist()},'error_example':{'errors_db':[-2,-4,-6,-8],'rms_db':float(np.sqrt(30)),'mean_signed_db':-5,'max_absolute_db':8,'alternating_errors_db':[-6,6,-6,6],'alternating_mean_db':0,'alternating_rms_db':6},'compression_example':{'input_spl':[55,65,75],'output_spl':[78,83,88],'gain_db':[23,18,13],'compression_ratio':2}}
assert 0 < np.sum(10.**(offset/10)) < 1  # Unplotted bands carry the remaining input energy.
assert np.all(pressure_ratio(fs,.015)>0)
assert np.allclose(ear,[85,92]) and np.allclose(required,[87,80])
(RESEARCH/'calculations.json').write_text(json.dumps(calc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('4 original SVG/PNG figures and calculations generated')
