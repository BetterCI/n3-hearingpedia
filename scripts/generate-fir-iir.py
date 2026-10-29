"""Reproducible teaching comparisons, not clinical or perceptual measurements."""
from pathlib import Path
import json
import numpy as np
import scipy
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'public/figures/fir-iir'
REC = ROOT/'docs/research/fir-iir-2026-10-29'
OUT.mkdir(parents=True, exist_ok=True)
REC.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path',
    'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'svg.hashsalt':'fir-iir'})
B,O,G='#22658c','#b45b36','#397a66'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),facecolor='white',metadata={'Date':None})
    fig.savefig(OUT/(name+'.png'),facecolor='white',dpi=140)
    plt.close(fig)

fs=16000
# Same pass/stop specification: <=1 dB loss to 2 kHz, >=60 dB rejection from 3 kHz.
nt,beta=signal.kaiserord(66,1000/(fs/2))
nt += (nt % 2 == 0)
h=signal.firwin(nt,2500,window=('kaiser',beta),fs=fs)
sos=signal.iirdesign(2000,3000,1,60,ftype='ellip',output='sos',fs=fs)
f=np.linspace(0,fs/2,65537)
_,hf=signal.freqz(h,worN=f,fs=fs)
_,hi=signal.sosfreqz(sos,worN=f,fs=fs)
def metrics(H):
    db=20*np.log10(np.maximum(abs(H),1e-15))
    return {'pass_min_db':float(db[f<=2000].min()),'pass_max_db':float(db[f<=2000].max()),
            'stop_rejection_db':float(-db[f>=3000].max())}
mf,mi=metrics(hf),metrics(hi)
assert mf['pass_min_db']>=-1 and mf['stop_rejection_db']>=60
assert mi['pass_min_db']>=-1.00001 and mi['stop_rejection_db']>=59.999
_,p,_=signal.sos2zpk(sos)
assert np.max(abs(p))<1
# Verify the streaming example against the same continuous zero-state system.
rng=np.random.default_rng(20261029)
stream_x=rng.standard_normal(4097)
state=np.zeros((len(sos),2));parts=[]
for start in range(0,len(stream_x),256):
    yy,state=signal.sosfilt(sos,stream_x[start:start+256],zi=state)
    parts.append(yy)
stream_error=float(np.max(abs(np.concatenate(parts)-signal.sosfilt(sos,stream_x))))
assert stream_error<1e-13
assert np.max(abs(h-h[::-1]))<1e-14
a=.6
wa=np.linspace(0,np.pi,2001)
_,ha=signal.freqz([a,1],[1,a],worN=wa)
assert np.max(abs(abs(ha)-1))<1e-14
fi=np.linspace(0,2000,2001)
_,hh=signal.sosfreqz(sos,worN=fi,fs=fs)
gdi=-np.gradient(np.unwrap(np.angle(hh)),2*np.pi*fi/fs)
fig,ax=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
for H,c,label in [(hf,B,f'FIR：{nt-1} 阶，{nt} 抽头'),(hi,O,f'IIR：{len(p)} 阶，{len(sos)} 个二阶节')]:
    ax[0].plot(f/1000,20*np.log10(np.maximum(abs(H),1e-8)),color=c,label=label)
ax[0].axvspan(2,3,color='#dddddd',alpha=.6,label='过渡带')
ax[0].axhline(-60,color='gray',ls='--',lw=1)
ax[0].set(xlabel='频率（kHz）',ylabel='幅度（dB）',ylim=(-100,3),title='（a）相同边界与容差，设计目标不含相位')
ax[0].legend(fontsize=10)
ax[1].plot(fi/1000,np.full_like(fi,(nt-1)/2/fs*1000),color=B,label='线性相位 FIR')
ax[1].plot(fi/1000,gdi/fs*1000,color=O,label='椭圆 IIR')
ax[1].set(xlabel='通带内频率（kHz）',ylabel='群延迟（ms）',title='（b）只在通带比较群延迟')
ax[1].legend()
for a in ax:a.grid(alpha=.18)
save(fig,'01-common-specification')

n=np.arange(161); delta=np.zeros(161);delta[0]=1
imp=signal.sosfilt(sos,delta)
fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
ax[0].stem(np.arange(nt),h,linefmt=B,markerfmt=' ',basefmt=' ')
ax[0].axvline((nt-1)/2,color=O,ls='--',label=f'对称中心：{(nt-1)/2:g} 样本')
ax[0].set(xlabel='样本 n',ylabel='单位脉冲输出',title='（a）FIR：有限支撑，与对称性分开判断',xlim=(0,160))
ax[0].legend(fontsize=10)
ax[1].plot(n,imp,color=O)
ax[1].set(xlabel='样本 n',ylabel='单位脉冲输出',title='（b）IIR：显示前 161 样本，尾部并未截断',xlim=(0,160))
for a in ax:a.grid(alpha=.18);a.set_ylim(-.15,.35)
save(fig,'02-impulse-responses')

fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
nn=np.arange(120)
for r,c in [(.5,B),(.95,O)]:
    ax[0].plot(nn,r**nn,color=c,label=f'r = {r}')
ax[0].set(xlabel='样本 n',ylabel='相对初始值的幅度',title='（a）稳定一阶极点：r 越大，衰减越慢')
ax[0].legend()
theta=np.linspace(0,2*np.pi,500)
ax[1].plot(np.cos(theta),np.sin(theta),color='gray',ls='--')
ax[1].scatter(p.real,p.imag,color=O,marker='x',s=70,label='共同算例的 IIR 极点')
ax[1].set(xlabel='实部',ylabel='虚部',title='（b）因果有理系统的稳定极点位于单位圆内',xlim=(-1.15,1.15),ylim=(-1.15,1.15),aspect='equal')
ax[1].legend(fontsize=10)
for a in ax:a.grid(alpha=.18)
save(fig,'03-poles-and-memory')

hm=signal.minimum_phase(h,half=False)
fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
ax[0].plot(np.arange(nt)/fs*1000,h,color=B,label='线性相位')
ax[0].plot(np.arange(len(hm))/fs*1000,hm,color=G,label='最小相位近似')
ax[0].set(xlabel='时间（ms）',ylabel='单位脉冲输出',title='（a）同长度 FIR 可有不同能量分布')
ax[0].legend()
_,hmf=signal.freqz(hm,worN=f,fs=fs)
ax[1].plot(f/1000,20*np.log10(np.maximum(abs(hf),1e-8)),color=B,label='线性相位')
ax[1].plot(f/1000,20*np.log10(np.maximum(abs(hmf),1e-8)),color=G,ls='--',label='half=False 转换结果')
ax[1].set(xlabel='频率（kHz）',ylabel='幅度（dB）',ylim=(-100,3),title='（b）数值转换近似保幅，仍须重新验收')
ax[1].legend()
for a in ax:a.grid(alpha=.18)
save(fig,'04-fir-phase-choice')

xx=np.zeros(1025);xx[512]=1
yy=signal.sosfilt(sos,xx)
zz=signal.sosfiltfilt(sos,xx)
tt=(np.arange(len(xx))-512)/fs*1000
fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
ax[0].plot(tt,yy,color=O,label='单向因果')
ax[0].plot(tt,zz,color=G,ls='--',label='前后向离线')
ax[0].axvline(0,color='gray',lw=1)
ax[0].set(xlabel='相对输入脉冲的时间（ms）',ylabel='输出幅度',xlim=(-5,12),title='（a）零相位处理可把响应扩散至事件之前')
ax[0].legend(fontsize=10)
ax[1].plot(f/1000,20*np.log10(np.maximum(abs(hi),1e-8)),color=O,label='单向：|H|')
ax[1].plot(f/1000,40*np.log10(np.maximum(abs(hi),1e-8)),color=G,ls='--',label='前后向：|H|²（内部稳态）')
ax[1].set(xlabel='频率（kHz）',ylabel='幅度（dB）',ylim=(-130,3),title='（b）前后向同时改变了幅度响应')
ax[1].legend(fontsize=10)
for a in ax:a.grid(alpha=.18)
save(fig,'05-offline-is-not-realtime')

report={'nature':'原创数值教学计算，非听觉实测或设备处方','numpy':np.__version__,'scipy':scipy.__version__,
    'fs_Hz':fs,'pass_edge_Hz':2000,'stop_edge_Hz':3000,'pass_loss_limit_db':1,'stop_limit_db':60,
    'fir':{'numtaps':nt,'order':nt-1,'kaiser_beta':float(beta),'kaiser_design_atten_db':66,'cutoff_Hz':2500,
           'delay_samples':(nt-1)/2,'delay_ms':(nt-1)/2/fs*1000,**mf},
    'iir':{'type':'ellip','order':len(p),'sections':len(sos),'max_pole_radius':float(max(abs(p))),
           'group_delay_ms_at_0_1000_2000Hz':[float(gdi[i]/fs*1000) for i in [0,1000,2000]],**mi},
    'one_pole_r095_to_minus60dB_samples':int(np.ceil(np.log(.001)/np.log(.95))),
    'streaming_random_seed':20261029,'streaming_max_absolute_error':stream_error,
    'figures':[f'{i:02d}-{name}.svg' for i,name in enumerate(['common-specification','impulse-responses','poles-and-memory','fir-phase-choice','offline-is-not-realtime'],1)],
    'fir_coefficients':h.tolist(),'iir_sos':sos.tolist()}
(REC/'figure-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['fir_coefficients','iir_sos']},ensure_ascii=False,indent=2))
