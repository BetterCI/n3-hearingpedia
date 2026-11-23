"""Original teaching figures; run with Python, NumPy, SciPy and Matplotlib."""
from pathlib import Path
import json
import numpy as np
import scipy
from scipy import signal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
font = Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font))
plt.rcParams.update({'font.family': 'Microsoft YaHei' if font.exists() else 'sans-serif',
                     'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False,
                     'svg.fonttype': 'path', 'figure.facecolor': 'white', 'axes.unicode_minus': False})
rng = np.random.default_rng(20261123)
blue, orange = '#176b9b', '#bb5426'
def canvas():
    return plt.subplots(2, 1, figsize=(9, 8), layout='constrained')
def save(fig, name):
    for ax in fig.axes:
        ax.grid(alpha=.18)
    fig.savefig(OUT / (name+'.svg'))
    fig.savefig(OUT / (name+'.png'), dpi=150)
    plt.close(fig)

fs=1000
x=rng.standard_normal(4096)
y=np.r_[np.zeros(12),x[:-12]]
xc=x-x.mean(); yc=y-y.mean()
cc=signal.correlate(yc,xc)/np.linalg.norm(xc)/np.linalg.norm(yc)
lags=signal.correlation_lags(len(y),len(x))
peak=int(lags[np.argmax(cc)])
assert peak==12
fig,ax=canvas()
keep=abs(lags)<=60
ax[0].plot(lags[keep],cc[keep],color=blue)
ax[0].axvline(12,color=orange,ls='--',label='已知延迟：+12 ms')
ax[0].set(title='宽带信号：零延迟相关低，移位后峰值清晰',xlabel='延迟 / ms',ylabel='归一化互相关')
ax[0].legend()
t=np.linspace(-120,120,1201)
ax[1].plot(t,np.cos(2*np.pi*(t-12)/50),color=blue)
ax[1].set(title='周期信号：相隔一个周期出现等价峰',xlabel='延迟 / ms',ylabel='理论归一化互相关')
save(fig,'delay')

x=rng.standard_normal(262144)
b,a=signal.butter(3,100,fs=fs)
y=signal.lfilter(b,a,x)+.5*rng.standard_normal(len(x))
params=dict(fs=fs,window='hann',nperseg=2048,noverlap=1024,detrend='constant')
f,c=signal.coherence(x,y,**params)
_,h=signal.freqz(b,a,worN=f,fs=fs)
theory=abs(h)**2/(abs(h)**2+.25)
error=float(np.mean(abs(c[1:]-theory[1:])))
assert error<.04
yd=np.r_[np.zeros(12),x[:-12]]
_,sxy=signal.csd(x,yd,**params)
phase=np.unwrap(np.angle(sxy))
fit=(f>10)&(f<300)
delay=-np.polyfit(f[fit],phase[fit],1)[0]/(2*np.pi)
assert abs(delay-.012)<.0001
fig,ax=canvas()
ax[0].plot(f,c,color=blue,label='Welch估计')
ax[0].plot(f,theory,color=orange,ls='--',label='理论：信噪比 /（1 + 信噪比）')
ax[0].set(xlim=(0,500),ylim=(0,1.05),title='低通系统加输出噪声：相干取决于频率',xlabel='频率 / Hz',ylabel='平方相干')
ax[0].legend()
ax[1].plot(f[fit],phase[fit],color=blue,label='估计互谱相位')
ax[1].plot(f[fit],-2*np.pi*f[fit]*.012,color=orange,ls='--',label='理论：−2π f × 0.012 s')
ax[1].set(title='单独的纯延迟模型：相位斜率保留延迟信息',xlabel='频率 / Hz',ylabel='解缠相位 / rad')
ax[1].legend()
save(fig,'filter')

x=rng.standard_normal(65536); y=rng.standard_normal(65536)
xx=np.fft.rfft(x); yy=np.fft.rfft(y)
single=abs(np.conj(xx)*yy)**2/(abs(xx)**2*abs(yy)**2)
assert np.allclose(single,1)
p=dict(fs=fs,window='hann',nperseg=1024,noverlap=512,detrend='constant')
f,c=signal.coherence(x,y,**p)
assert c.mean()<.03
fig,ax=canvas()
ax[0].plot(np.fft.rfftfreq(len(x),1/fs),single,color=orange)
ax[0].set(title='错误的单段比值：独立噪声也恒为1',ylim=(0,1.08),xlabel='频率 / Hz',ylabel='平方相干')
ax[1].plot(f,c,color=blue)
ax[1].set(title='多段复谱平均：估计接近零，但不恰好等于零',ylim=(0,1.08),xlabel='频率 / Hz',ylabel='平方相干')
save(fig,'averaging')
independent_mean=float(c.mean())

v=np.linspace(-3,3,401)
square_r=float(np.corrcoef(v,v*v)[0,1])
assert abs(square_r)<1e-12
assert np.isclose(np.corrcoef(v,2*v+5)[0,1],1)
assert np.isclose(np.corrcoef(v,-v)[0,1],-1)
x=rng.standard_normal(65536); y=x*x; y-=y.mean()
f,c=signal.coherence(x,y,**p)
assert c.mean()<.03
fig,ax=canvas()
ax[0].scatter(v[::4],v[::4]**2,s=14,color=blue)
ax[0].set(title='确定性平方关系：成对对称样本的相关为零',xlabel='输入 x / 归一化量',ylabel='输出 y = x²')
ax[1].plot(f,c,color=blue)
ax[1].set(title='高斯白噪声及其中心化平方：相干估计接近零',ylim=(0,1.08),xlabel='频率 / Hz',ylabel='平方相干')
save(fig,'nonlinear')
result={'seed':20261123,'numpy':np.__version__,'scipy':scipy.__version__,
        'lag_peak_samples':peak,'zero_lag_r':float(np.corrcoef(xc,yc)[0,1]),
        'linear_filter_coherence_mean_absolute_error':error,
        'estimated_delay_seconds':float(delay),'single_fft_max_error':float(max(abs(single-1))),
        'independent_noise_mean_coherence':independent_mean,'symmetric_square_pearson_r':square_r,
        'gaussian_square_mean_coherence':float(c.mean()),'assertions':'passed',
        'note':'Synthetic demonstration, not experimental evidence or a significance test.'}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
