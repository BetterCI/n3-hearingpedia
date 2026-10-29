"""Reproducible analytic teaching figures, not experimental observations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT/'docs/research/wave-and-helmholtz-2026-10-29'
RESEARCH.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':12,
    'svg.fonttype':'path','axes.unicode_minus':False, 'axes.spines.top':False,
    'axes.spines.right':False, 'svg.hashsalt':'wave-helmholtz-2026', 'savefig.dpi':140})
BLUE, ORANGE, GREEN = '#22658c','#b45b36','#397a66'
manifest=[]
def panels(height=4.6):
    fig,axs=plt.subplots(1,2,figsize=(12,height),layout='constrained')
    for ax in axs: ax.grid(alpha=.18)
    return fig,axs
def save(fig,slug,name,params):
    out=ROOT/'public/figures'/slug
    out.mkdir(parents=True, exist_ok=True)
    for ext in ['svg','png']:
        fig.savefig(out/(name+'.'+ext), facecolor='white', metadata={'Date':None} if ext=='svg' else None)
    svg = out/(name+'.svg')
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text('utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)
    manifest.append({'entry':slug,'svg':name+'.svg','png':name+'.png','nature':'原创解析教学图，非实测','parameters':params})

c=343.; sigma=.04; t=.0004
x=np.linspace(-.3,.3,1501)
g=lambda z:np.exp(-z*z/(2*sigma*sigma))
fig,axs=panels()
for ax in axs:
    ax.plot(x,g(x),color='gray',ls=':',label='t＝0 ms')
    ax.set(xlabel='位置 x（m）',ylabel='声压 p（Pa）',ylim=(-.05,1.15))
axs[0].plot(x,.5*(g(x-c*t)+g(x+c*t)),color=BLUE,label='t＝0.4 ms')
axs[1].plot(x,g(x-c*t),color=ORANGE,label='t＝0.4 ms')
axs[0].set_title('（a）初始时间导数为零：双向分裂')
axs[1].set_title('（b）右行初始条件：单向平移')
for ax in axs: ax.legend(loc='upper right',fontsize=10)
save(fig,'wave-equation','01-initial-data',{'c_m_s':c,'sigma_m':sigma,'t_s':t,'amplitude_Pa':1})

x=np.linspace(-.3,0,1201); a=.1
incident=g(x-a); mirror=g(x+a)
fig,axs=panels()
for ax,R,title in zip(axs,[1,-1],['（a）刚壁：压力反射系数 +1','（b）压力释放面：压力反射系数 −1']):
    ax.plot(x,incident,ls='--',color=BLUE,label='入射分量')
    ax.plot(x,R*mirror,ls=':',color=ORANGE,label='反射分量')
    ax.plot(x,incident+R*mirror,color=GREEN,label='总声压')
    ax.axvline(0,color='black',lw=2)
    ax.set(title=title,xlabel='位置 x（m）',ylabel='声压 p（Pa）',ylim=(-1.15,1.15))
    ax.legend(fontsize=10,loc='upper left')
assert abs(g(-a)-g(a))<1e-15
save(fig,'wave-equation','02-reflection',{'boundary_m':0,'incident_virtual_center_m':a,'sigma_m':sigma,'R':[1,-1]})

fig,ax=plt.subplots(figsize=(12,4.6),layout='constrained')
N=np.linspace(2.1,30,600)
for C,col,ls in [(0.5,BLUE,'-'),(.9,ORANGE,'--'),(1.,GREEN,':')]:
    ratio=N/(np.pi*C)*np.arcsin(C*np.sin(np.pi/N))
    ax.plot(N,ratio,color=col,ls=ls,label=f'C＝{C:.1f}')
    if C==1: assert np.max(np.abs(ratio-1))<1e-14
ax.set(xlabel='每波长网格点数 λ / Δx',ylabel='数值相速度 / 真实声速',ylim=(.65,1.025),title='一维中心差分：稳定条件以内的数值色散')
ax.grid(alpha=.18); ax.legend()
save(fig,'wave-equation','03-dispersion',{'C':[.5,.9,1.],'points_per_wavelength':[2.1,30],'model':'1D second-order centered difference'})

x=np.linspace(0,2*c/1000,1001); k=2*np.pi*1000/c
fig,axs=panels(5)
for ax,P,title in zip(axs,[np.exp(-1j*k*x),np.cos(k*x).astype(complex)],['（a）右行波','（b）等幅反向波组成的驻波']):
    ax.plot(x,np.real(P),color=BLUE,label='t＝0')
    ax.plot(x,np.real(1j*P),color=ORANGE,ls='--',label='t＝T/4')
    ax.plot(x,np.abs(P),color='gray',ls=':',label='相量幅度 |P|')
    ax.set(title=title,xlabel='位置 x（m）',ylabel='声压（Pa）',ylim=(-1.2,1.4)); ax.legend(fontsize=10)
save(fig,'helmholtz-equation','01-phasor',{'f_Hz':1000,'c_m_s':c,'travelling_peak_Pa':1,'standing_each_wave_Pa':.5})

L=.1; x=np.linspace(0,L,1001)
fig,axs=panels(5)
for ax,closed,title in zip(axs,[True,False],['（a）两端刚壁','（b）左端刚壁、右端压力释放']):
    for n,col in zip(range(1,4),[BLUE,ORANGE,GREEN]):
        kn=n*np.pi/L if closed else (2*n-1)*np.pi/(2*L)
        f=kn*c/(2*np.pi); offset=(3-n)*2.8
        ax.axhline(offset,color='gray',lw=.5,alpha=.3)
        ax.plot(x,np.cos(kn*x)+offset,color=col)
        ax.text(.006,offset+1.18,f'n＝{n}，{f:g} Hz',color=col,fontsize=11)
    ax.set(title=title,xlabel='位置 x（m）',ylabel='归一化压力模态（竖直错开）',yticks=[],ylim=(-1.25,7.5))
    ax.axvline(0,color='black',lw=2); ax.axvline(L,color='black',ls='-' if closed else '--',lw=2)
save(fig,'helmholtz-equation','02-modes',{'L_m':L,'c_m_s':c,'normalization':'each mode peak normalized to 1, vertically offset'})

rho=1.2; f=2000; k=2*np.pi*f/c; R=.5
P=np.exp(-1j*k*x)+R*np.exp(-2j*k*L)*np.exp(1j*k*x)
V=(np.exp(-1j*k*x)-R*np.exp(-2j*k*L)*np.exp(1j*k*x))/(rho*c)
I=.5*np.real(P*np.conj(V)); Iinc=1/(2*rho*c)
assert abs(P[-1]/V[-1]-3*rho*c)<1e-10
assert np.max(np.abs(I/Iinc-.75))<1e-14
fig,axs=panels()
axs[0].plot(x,np.ones_like(x),color=BLUE,ls='--',label='入射幅度')
axs[0].plot(x,np.abs(P),color=ORANGE,label='总声压幅度')
axs[0].set(title='（a）局部压力幅度随位置起伏',xlabel='位置 x（m）',ylabel='峰值声压幅度（Pa）',ylim=(0,1.65)); axs[0].legend()
axs[1].plot(x,I/Iinc,color=GREEN)
axs[1].set(title='（b）净平均能流保持不变',xlabel='位置 x（m）',ylabel='净声强 / 入射声强',ylim=(0,1.1))
save(fig,'helmholtz-equation','03-impedance-tube',{'rho_kg_m3':rho,'c_m_s':c,'f_Hz':f,'L_m':L,'R':R,'incident_peak_Pa':1,'Zs_Pa_s_m':3*rho*c})

(RESEARCH/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checks={'boundary_impedance_abs_error':float(abs(P[-1]/V[-1]-3*rho*c)), 'net_flux_relative_error':float(np.max(np.abs(I/Iinc-.75))), 'delay_s':.343/c,'samples_at_48kHz':.343/c*48000,'SPL_for_1_Pa_peak':float(20*np.log10(1/np.sqrt(2)/20e-6)), 'figures':len(manifest)}
(RESEARCH/'numerical-checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,indent=2))
