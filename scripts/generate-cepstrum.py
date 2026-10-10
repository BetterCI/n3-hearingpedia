"""Original, reproducible cepstrum illustrations; no human or clinical data."""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
OUT=Path(__file__).resolve().parents[1]/'public/figures/cepstrum'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'svg.fonttype':'path','font.size':11})
B,O,G='#287da8','#d77537','#438872'
FS,N,P=16000,8000,80
freq=np.fft.rfftfreq(N,1/FS);omega=2*np.pi*freq/FS
q=np.arange(N)/FS
def cep(Z):
    assert np.all(np.abs(Z)>0)
    return np.fft.irfft(np.log(np.abs(Z)),n=N)
def save(fig,name,footer):
    fig.text(.5,.012,footer,ha='center',fontsize=10,color='#566774')
    fig.tight_layout(rect=(0,.065,1,.95))
    fig.savefig(OUT/(name+'.png'),dpi=150,facecolor='white')
    file=OUT/(name+'.svg');fig.savefig(file,facecolor='white')
    file.write_text('\n'.join(s.rstrip() for s in file.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)
def dbshape(Z):
    a=20*np.log10(np.abs(Z));return a-a.mean()
def grid(ax): ax.grid(alpha=.18)

rng=np.random.default_rng(20261010)
excitation=.02*rng.normal(size=N);excitation[::P]+=1
E=np.fft.rfft(excitation)
H=np.ones_like(E,dtype=complex)
resonances=[(700,80),(1200,100),(2500,150)]
for fc,bw in resonances:
    radius=np.exp(-np.pi*bw/FS);angle=2*np.pi*fc/FS
    H/=1-2*radius*np.cos(angle)*np.exp(-1j*omega)+radius**2*np.exp(-2j*omega)
X=E*H;x=np.fft.irfft(X,n=N)
cE,cH,cX=map(cep,[E,H,X])
err_add=float(np.max(abs(cX-cE-cH)));assert err_add<1e-12
cg=cep(3*X)-cX
assert abs(cg[0]-np.log(3))<1e-12 and np.max(abs(cg[1:]))<1e-12
fig,ax=plt.subplots(3,1,figsize=(12,9))
show=np.arange(640)
ax[0].plot(show/FS*1000,x[show]/np.max(abs(x)),color=B,lw=.9)
ax[0].set(xlabel='原波形时间 / ms',ylabel='相对幅度',title='A  合成波形（仅显示前 40 ms；计算记录长 500 ms）')
mask=freq<=4000
ax[1].plot(freq[mask],dbshape(X)[mask],color=B,lw=.6,label='合成声的对数幅度谱')
ax[1].plot(freq[mask],dbshape(H)[mask],color=O,lw=1.6,label='已知滤波器的谱形')
ax[1].set(xlabel='频率 / Hz',ylabel='去均值谱形 / dB',title='B  谐波间隔约 200 Hz，宽尺度谱形由滤波器塑造');ax[1].legend()
cut=(q>=.0005)&(q<=.02)
ax[2].plot(q[cut]*1000,cX[cut],color=B,lw=1,label='合成声实倒谱')
ax[2].plot(q[cut]*1000,cH[cut],color=O,lw=1,label='已知滤波器实倒谱')
ax[2].axvline(5,color=G,ls='--',label='脉冲重复间隔 5 ms')
ax[2].set(xlabel='倒频率 / ms（不是原波形时间）',ylabel='自然对数倒谱系数',title='C  谱中的间隔，转为倒谱中的周期线索（显示 0.5–20 ms）');ax[2].legend()
for a in ax:grid(a)
save(fig,'01-spectrum-to-cepstrum','16 kHz；200 Hz 脉冲列加固定随机背景，经三组共轭极点滤波。周期 DFT 合成，无窗；不是自然语音。')

fig,axs=plt.subplots(3,1,figsize=(12,9),sharex=True)
for ax,seconds in zip(axs,[.001,.0025,.007]):
    distance=np.minimum(np.arange(N),N-np.arange(N))/FS
    cl=cX*(distance<=seconds)
    smoothed=np.exp(np.fft.rfft(cl).real)
    ax.plot(freq[mask],dbshape(X)[mask],color='#a5bbc7',lw=.5,label='原对数幅度谱')
    ax.plot(freq[mask],dbshape(smoothed)[mask],color=B,lw=1.5,label='低倒频率截断后的谱形')
    ax.plot(freq[mask],dbshape(H)[mask],color=O,ls='--',lw=1.3,label='已知滤波器（仅作比较）')
    ax.set(title=f'对称保留 |q| ≤ {seconds*1000:g} ms',ylabel='去均值谱形 / dB',ylim=(-65,85))
    grid(ax)
axs[0].legend(ncol=3,fontsize=10);axs[-1].set_xlabel('频率 / Hz')
save(fig,'02-lifter-envelope','矩形 lifter 的截止点由示例选择。7 ms 已包含 5 ms 周期峰；截断结果不等于精确声道反演。')

N2,D,alpha=8192,128,.5
w=2*np.pi*np.fft.rfftfreq(N2)
He=1+alpha*np.exp(-1j*w*D)
ce=np.fft.irfft(np.log(abs(He)),n=N2)
analytic=[(-1)**(r+1)*alpha**r/(2*r) for r in range(1,5)]
err_echo=float(max(abs(ce[r*D]-analytic[r-1]) for r in range(1,5)))
assert err_echo<1e-12
fig,ax=plt.subplots(3,1,figsize=(12,8))
ax[0].stem([0,8],[1,.5],basefmt=' ',linefmt=B,markerfmt='o')
ax[0].set(xlim=(-1,13),xlabel='脉冲响应时间 / ms',ylabel='回声模型系数',title='A  直接声 + 0.5 倍、延迟 8 ms 的副本')
fe=np.fft.rfftfreq(N2,1/FS);ix=fe<=1000
ax[1].plot(fe[ix],20*np.log10(abs(He[ix])),color=B)
ax[1].set(xlabel='频率 / Hz',ylabel='传递函数幅度 / dB',title='B  梳状起伏间隔 125 Hz = 1 / 8 ms')
qs=np.arange(N2)/FS;ix=(qs>0)&(qs<=.04)
ax[2].plot(qs[ix]*1000,ce[ix],color=B,lw=.8)
ax[2].scatter(np.arange(1,5)*8,analytic,color=O,zorder=3)
ax[2].set(xlabel='倒频率 / ms',ylabel='实倒谱系数',title='C  8 ms 及整数倍处有系数；实倒谱的系数可为负')
for a in ax:grid(a)
save(fig,'03-echo','仅计算已知回声滤波器 h 的倒谱。实际录音还含声源倒谱；峰不能自动归因于基频或房间。')

M=4096;a=.6
w2=2*np.pi*np.fft.fftfreq(M)
hmin=np.zeros(M);hmin[:2]=[1,-a]
hmax=np.zeros(M);hmax[:2]=[-a,1]
Fmin,Fmax=np.fft.fft(hmin),np.fft.fft(hmax)
realmin=np.fft.ifft(np.log(abs(Fmin))).real
realmax=np.fft.ifft(np.log(abs(Fmax))).real
cm=np.fft.ifft(np.log(1-a*np.exp(-1j*w2))).real
ca=np.fft.ifft(np.log(1-a*np.exp(1j*w2))).real
err_phase=float(np.max(abs(realmin-realmax)));assert err_phase<1e-12
reconmin=np.fft.ifft(np.exp(np.fft.fft(cm))).real
reconmax=np.fft.ifft(np.exp(np.fft.fft(ca))*np.exp(-1j*w2)).real
err_recon=float(max(np.max(abs(reconmin-hmin)),np.max(abs(reconmax-hmax))))
assert err_recon<1e-12
fig,ax=plt.subplots(2,2,figsize=(12,8))
ax[0,0].bar(np.array([0,1])-.14,hmin[:2],width=.28,color=B,label='最小相位 FIR')
ax[0,0].bar(np.array([0,1])+.14,hmax[:2],width=.28,color=O,label='时间反转 FIR')
ax[0,0].set(xlabel='原序列样本 n',ylabel='系数',title='A  两个不同的序列');ax[0,0].legend()
k=np.arange(M//2+1);f=k/M
ax[0,1].plot(f,20*np.log10(abs(Fmin[k])),color=B,label='最小相位')
ax[0,1].plot(f,20*np.log10(abs(Fmax[k])),color=O,ls='--',label='时间反转')
ax[0,1].set(xlabel='归一化频率 / 周期每样本',ylabel='幅度 / dB',title='B  幅度谱完全相同');ax[0,1].legend()
indices=np.arange(-12,13);take=indices%M
ax[1,0].plot(indices,realmin[take],'-o',color=B,label='最小相位实倒谱')
ax[1,0].plot(indices,realmax[take],'--',color=O,label='时间反转实倒谱')
ax[1,0].set(xlabel='带符号倒谱样本 m',ylabel='实倒谱系数',title='C  实倒谱无法区分这两个序列');ax[1,0].legend(fontsize=10)
ax[1,1].plot(indices,cm[take],'-o',color=B,label='最小相位复倒谱')
ax[1,1].plot(indices,ca[take],'-s',color=O,label='反转序列：移除 1 样本延迟后')
ax[1,1].set(xlabel='带符号倒谱样本 m',ylabel='复倒谱系数（此处为实数）',title='D  保留相位信息后，系数分布不同');ax[1,1].legend(fontsize=9)
for a0 in ax.flat:grid(a0)
save(fig,'04-phase-and-inversion','解析例使用已知对数分支，并单独记录反转序列的 1 样本延迟；不是任意语音的通用相位展开算法。')

record={'nature':'original synthetic teaching examples; not measured speech or clinical results',
 'numpy_version':np.__version__,'matplotlib_version':matplotlib.__version__,
 'source_filter':{'fs_hz':FS,'dft_samples':N,'record_seconds':N/FS,'pulse_interval_samples':P,'nominal_repetition_hz':FS/P,'noise_sd':.02,'rng_seed':20261010,'resonances_hz_bandwidth_hz':resonances,'window':'none; periodic DFT model','lifter_cutoffs_ms':[1,2.5,7],'max_cepstral_additivity_error':err_add,'gain_c0_shift':float(cg[0]),'gain_nonzero_cepstrum_max_error':float(np.max(abs(cg[1:]))),'spectral_floor':'none: all computed bins verified nonzero'},
 'echo':{'fs_hz':FS,'dft_samples':N2,'delay_samples':D,'delay_ms':D/FS*1000,'amplitude':alpha,'first_four_positive_quefrency_coefficients':analytic,'analytic_max_error':err_echo},
 'phase':{'dft_samples':M,'minimum_phase_fir':[1,-.6],'reversed_fir':[-.6,1],'removed_delay_samples':1,'real_cepstrum_max_difference':err_phase,'complex_cepstrum_inverse_max_error':err_recon,'scope':'known analytic branches only'},
 'quefrency_spacing_seconds':1/FS}
(OUT/'parameters.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
