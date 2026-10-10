"""Original analytic/synthetic teaching figures; no measured participant data."""
from pathlib import Path
import json
import shutil
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/spectrum-and-power-spectral-density'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,
                     'svg.fonttype':'path','font.size':11})
FS=8000
BLUE,ORANGE,GREEN='#287da8','#d77537','#438872'
records={'nature':'original analytic and seeded synthetic teaching calculations, not measured data',
         'numpy_version':np.__version__,'scipy_version':scipy.__version__,'fs_hz':FS,'seed':20261010}

def save(fig,name,footer):
    fig.text(.5,.017,footer,ha='center',fontsize=10,color='#566774')
    fig.tight_layout(rect=(0,.075,1,.94))
    fig.savefig(OUT/(name+'.svg'),facecolor='white')
    svg_path=OUT/(name+'.svg')
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(OUT/(name+'.png'),dpi=160,facecolor='white')
    plt.close(fig)

def estimate(x,w,nfft=None):
    nfft=len(x) if nfft is None else nfft
    z=np.fft.rfft(x*w,nfft)
    factor=np.full(len(z),2.);factor[0]=1
    if nfft%2==0: factor[-1]=1
    f=np.fft.rfftfreq(nfft,1/FS)
    psd=factor*abs(z)**2/(FS*np.sum(w*w))
    spectrum=factor*abs(z)**2/abs(np.sum(w))**2
    enbw=FS*np.sum(w*w)/abs(np.sum(w))**2
    assert np.allclose(spectrum,psd*enbw)
    assert np.isclose(np.sum(psd)*FS/nfft,np.sum((x*w)**2)/np.sum(w*w))
    return f,psd,spectrum,enbw

fig,ax=plt.subplots(2,2,figsize=(12,7),sharex=True)
tone_records=[]
for i,n in enumerate([2000,8000]):
    t=np.arange(n)/FS;x=.2*np.cos(2*np.pi*1000*t)
    f,p,s,b=estimate(x,np.ones(n));amp=np.sqrt(2*s)
    amp[0]=np.sqrt(s[0]);amp[-1]=np.sqrt(s[-1])
    select=(f>=970)&(f<=1030)
    ax[i,0].stem(f[select],amp[select],linefmt=BLUE,markerfmt='o',basefmt=' ')
    ax[i,1].stem(f[select],p[select],linefmt=ORANGE,markerfmt='o',basefmt=' ')
    ax[i,0].set(title=f'（{"a" if i==0 else "c"}）T={n/FS:g} s：峰值幅度谱',ylabel='幅度（Pa，峰值）',ylim=(0,.23))
    ax[i,1].set(title=f'（{"b" if i==0 else "d"}）T={n/FS:g} s：单侧 PSD',ylabel='PSD（Pa²/Hz）',ylim=(0,.023))
    ax[i,0].text(973,.185,'1000 Hz：0.2 Pa',fontsize=10)
    ax[i,1].text(972,.0205,f'峰高 {p.max():g}\n积分 0.02 Pa²\nΔf={FS/n:g} Hz',fontsize=10,va='top')
    for a in ax[i]: a.grid(alpha=.2);a.set_xlim(970,1030)
    assert np.isclose(p.max(),.02/(FS/n))
    assert np.isclose(amp.max(),.2)
    tone_records.append({'N':n,'duration_seconds':n/FS,'df_hz':FS/n,'psd_peak':float(p.max()),'psd_integral':float(p.sum()*FS/n),'amplitude_peak':float(amp.max())})
for a in ax[-1]: a.set_xlabel('频率（Hz）')
fig.suptitle('同一个纯音：记录更长，PSD 峰更高，积分不变',fontsize=18)
save(fig,'01-tone-scaling','原创解析计算｜矩形窗、整周期、无零填充｜RMS²=0.02 Pa²｜谱图只显示 970–1030 Hz')
records['tone']=tone_records

rng=np.random.default_rng(20261010)
S0=1e-6;x=rng.normal(0,np.sqrt(S0*FS/2),FS*16)
fig,ax=plt.subplots(1,2,figsize=(12,5))
noise_records=[]
for n,color in [(1000,BLUE),(4000,ORANGE)]:
    w=signal.windows.hann(n,sym=False)
    f,p=signal.welch(x,FS,window=w,nperseg=n,noverlap=n//2,nfft=n,detrend=False,scaling='density')
    _,s=signal.welch(x,FS,window=w,nperseg=n,noverlap=n//2,nfft=n,detrend=False,scaling='spectrum')
    b=FS*np.sum(w*w)/np.sum(w)**2
    assert np.allclose(s,p*b)
    ax[0].plot(f,p*1e6,color=color,lw=.9,label=f'N={n}，Δf={FS/n:g} Hz')
    ax[1].plot(f,s*1e6,color=color,lw=.9,label=f'N={n}，ENBW={b:g} Hz')
    noise_records.append({'segment_length':n,'df_hz':FS/n,'enbw_hz':float(b),'segments':1+(len(x)-n)//(n//2),
                          'mean_psd_100_3900':float(np.mean(p[(f>=100)&(f<=3900)])),
                          'expected_spectrum_noise_interior':float(S0*b)})
ax[0].axhline(1,color=GREEN,ls='--',label='理论单侧密度 1 × 10^-6')
ax[1].axhline(12,color=BLUE,ls='--',alpha=.5);ax[1].axhline(3,color=ORANGE,ls='--',alpha=.5)
ax[0].set(title='（a）密度标度：平均噪声底约保持不变',ylabel='PSD（10^-6 Pa²/Hz）',ylim=(0,2))
ax[1].set(title='（b）spectrum 标度：噪声随 ENBW 改变',ylabel='spectrum（10^-6 Pa²）',ylim=(0,22))
for a in ax: a.set(xlabel='频率（Hz）',xlim=(100,3900));a.grid(alpha=.2);a.legend(fontsize=9)
fig.suptitle('同一白噪声：密度与“每个分析带的功率”不同',fontsize=18)
save(fig,'02-noise-bandwidth','原创随机合成｜16 s、8 kHz｜周期 Hann、50% 重叠、无去均值｜虚线为模型期望')
records['noise']=noise_records

rho=.8;innovation=.04;N=FS*2;L=2000;K=15;trials=160
def ar1():
    return signal.lfilter([1],[1,-rho],rng.normal(0,innovation,N+FS))[FS:]
y=ar1();window_full=signal.windows.hann(N,sym=False);window_short=signal.windows.hann(L,sym=False)
fp,pp=signal.periodogram(y,FS,window=window_full,detrend=False,scaling='density')
fw,pw=signal.welch(y,FS,window=window_short,nperseg=L,noverlap=L//2,detrend=False,scaling='density')
def theory(f): return 2*innovation**2/FS/abs(1-rho*np.exp(-2j*np.pi*f/FS))**2
point=800;truth=float(theory(point));vp=[];vw=[]
for _ in range(trials):
    z=ar1()
    _,a=signal.periodogram(z,FS,window=window_full,detrend=False,scaling='density')
    _,b=signal.welch(z,FS,window=window_short,nperseg=L,noverlap=L//2,detrend=False,scaling='density')
    vp.append(a[np.argmin(abs(fp-point))]/truth);vw.append(b[np.argmin(abs(fw-point))]/truth)
fig,ax=plt.subplots(1,2,figsize=(12,5))
ax[0].semilogy(fp,pp,color=BLUE,lw=.65,alpha=.7,label='整段周期图：2 s')
ax[0].semilogy(fw,pw,color=ORANGE,lw=1.2,label='Welch：0.25 s × 15 段')
ax[0].semilogy(fw[1:-1],theory(fw[1:-1]),color=GREEN,ls='--',label='AR(1) 理论 PSD')
ax[0].set(title='（a）同一条记录的两种估计',xlabel='频率（Hz）',ylabel='PSD（Pa²/Hz）',xlim=(40,2000),ylim=(1e-9,6e-5))
bins=np.linspace(0,5,35)
ax[1].hist(vp,bins=bins,density=True,color=BLUE,alpha=.55,label='整段周期图')
ax[1].hist(vw,bins=bins,density=True,color=ORANGE,alpha=.6,label='Welch')
ax[1].axvline(1,color=GREEN,ls='--',label='理论值')
ax[1].set(title='（b）160 条独立记录：800 Hz 的估计',xlabel='估计值 / 理论 PSD（无量纲）',ylabel='概率密度',xlim=(0,5))
for a in ax:a.grid(alpha=.2);a.legend(fontsize=9)
fig.suptitle('Welch 平均减小随机波动，频率分辨仍由段长约束',fontsize=18)
save(fig,'03-estimation-variance','原创 AR(1) 合成｜ρ=0.8、创新标准差 0.04 Pa｜2 s、8 kHz、周期 Hann、50% 重叠｜不是听者实验')
records['variance']={'rho':rho,'innovation_sd_pa':innovation,'samples':N,'segment_length':L,'segments':K,'trials':trials,'point_hz':point,'theoretical_psd':truth,
                     'periodogram_mean_ratio':float(np.mean(vp)),'welch_mean_ratio':float(np.mean(vw)),
                     'periodogram_cv':float(np.std(vp,ddof=1)/np.mean(vp)),'welch_cv':float(np.std(vw,ddof=1)/np.mean(vw))}

edges=np.array([100,200,400,800,1600,3200]);f=np.geomspace(100,3200,800)
white=1e-6*np.ones_like(f);pink=1e-3/f
white_band=1e-6*np.diff(edges);pink_band=1e-3*np.log(edges[1:]/edges[:-1])
fig,ax=plt.subplots(1,2,figsize=(12,5))
ax[0].loglog(f,white,color=BLUE,label='白：S(f)=10^-6 Pa²/Hz')
ax[0].loglog(f,pink,color=ORANGE,label='粉红：S(f)=10^-3/f')
for e in edges:ax[0].axvline(e,color='#91a5ae',lw=.6,ls=':')
ax[0].set(title='（a）按 Hz 表示的理论密度',xlabel='频率（Hz，对数轴）',ylabel='PSD（Pa²/Hz）')
locations=np.arange(5)
ax[1].bar(locations-.18,white_band*1e3,width=.36,color=BLUE,label='白噪声')
ax[1].bar(locations+.18,pink_band*1e3,width=.36,color=ORANGE,label='粉红噪声')
ax[1].set(xticks=locations,xticklabels=['100–200','200–400','400–800','800–1600','1600–3200'],title='（b）每个倍频程的均方值积分',xlabel='频带（Hz）',ylabel='频带均方声压（10^-3 Pa²）')
ax[1].tick_params(axis='x',labelsize=9)
for a in ax:a.grid(alpha=.2);a.legend(fontsize=9)
fig.suptitle('横轴改成对数，不会把“每 Hz”自动变成“每倍频程”',fontsize=18)
save(fig,'04-band-integration','原创带限理论模型｜仅定义 100–3200 Hz｜柱高由 ∫S(f)df 计算，不是对 dB 值求和')
records['bands']={'edges_hz':edges.tolist(),'white_pa2':white_band.tolist(),'pink_pa2':pink_band.tolist(),
                  'white_100_200_spl_db':float(10*np.log10(white_band[0]/(20e-6)**2)),
                  'white_100_300_spl_db':float(10*np.log10(2*white_band[0]/(20e-6)**2))}
assert np.allclose(pink_band,pink_band[0]) and np.allclose(white_band[1:]/white_band[:-1],2)

# Independent checks: odd/even FFT endpoints, zero padding, window-weighted Parseval and SciPy agreement.
for n in [1000,1001]:
    z=rng.normal(size=n);w=signal.windows.hann(n,sym=False)
    for nfft in [n,4*n,4*n+1]:
        f,p,s,enbw=estimate(z,w,nfft)
        ff,ps=signal.periodogram(z,FS,window=w,nfft=nfft,detrend=False,scaling='density')
        assert np.allclose(f,ff) and np.allclose(p,ps)
records['checks']={'odd_even_and_zero_padding_parseval':'passed','scipy_periodogram_agreement':'passed','spectrum_density_enbw':'passed',
                   'tone_amplitude_and_area':'passed','octave_band_integrals':'passed'}
(OUT/'parameters.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
shutil.copyfile(__file__,OUT/'generate-spectrum-psd.py')
print(json.dumps(records,ensure_ascii=False,indent=2))
