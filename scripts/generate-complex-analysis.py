"""Original complex-analysis teaching figures and coherent-tone audio."""
from pathlib import Path
import json
import wave
import numpy as np
import scipy
from scipy import signal, integrate
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
FIG=ROOT/'public/figures/complex-analysis'
AUDIO=ROOT/'public/audio/complex-analysis'
REC=ROOT/'docs/research/complex-analysis-2026-11-02'
PRE=ROOT/'artifacts/complex-analysis/figures'
for p in (FIG,AUDIO,REC,PRE): p.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'svg.fonttype':'path',
 'svg.hashsalt':'complex-analysis-acoustics','axes.unicode_minus':False,
 'axes.spines.top':False,'axes.spines.right':False})
B,R,G,M='#22658c','#b44e37','#31755e','#61727d'

def save(fig,name):
    fig.text(.5,.012,'n³ Hearingpedia · 原创复变函数与声学教学计算 · 非实测数据',ha='center',fontsize=10,color=M)
    fig.tight_layout(rect=(0,.045,1,.94),w_pad=3,h_pad=2)
    p=FIG/f'{name}.svg'
    fig.savefig(p,metadata={'Date':None},facecolor='white')
    p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(PRE/f'{name}.png',dpi=110,facecolor='white')
    plt.close(fig)

angle=np.linspace(0,2*np.pi,500)
P=.02*np.exp(1j*np.pi/3)
fig,ax=plt.subplots(1,2,figsize=(14,6.5))
ax[0].plot(.02*np.cos(angle),.02*np.sin(angle),'--',color=M)
ax[0].annotate('',xy=(P.real,P.imag),xytext=(0,0),arrowprops={'arrowstyle':'->','color':B,'lw':2})
ax[0].plot([P.real,P.real],[0,P.imag],':',color=G)
ax[0].plot([0,P.real],[P.imag,P.imag],':',color=G)
ax[0].text(.001,.003,'相位 π/3',fontsize=11)
ax[0].set(xlabel='实部（Pa）',ylabel='虚部（Pa）',title='（a）峰值相量 P = 0.02 exp(jπ/3)',xlim=(-.025,.025),ylim=(-.025,.025))
ax[0].set_aspect('equal')
t=np.linspace(0,.002,1000)
ax[1].plot(t*1000,np.real(P*np.exp(1j*2*np.pi*1000*t)),color=B)
ax[1].axhline(0,color=M,lw=.7)
ax[1].set(xlabel='时间（ms）',ylabel='实际声压 p(t)（Pa）',title='（b）乘旋转因子后取实部，得到 1000 Hz 波形')
fig.suptitle('一个复数同时保存同频声音的幅值与初相位',fontsize=18,fontweight='bold')
save(fig,'phasor-and-wave')

phases=[0,2*np.pi/3,np.pi]
sums=[.2*(1+np.exp(1j*p)) for p in phases]
fig,axes=plt.subplots(2,3,figsize=(14,8))
tt=np.linspace(0,.002,800)
for i,(phase,total) in enumerate(zip(phases,sums)):
    a,b=.2,.2*np.exp(1j*phase)
    for start,end,color in [(0,a,B),(a,total,G),(0,total,R)]:
        axes[0,i].annotate('',xy=(np.real(end),np.imag(end)),xytext=(np.real(start),np.imag(start)),
            arrowprops={'arrowstyle':'->','color':color,'lw':2})
    axes[0,i].axhline(0,color=M,lw=.6);axes[0,i].axvline(0,color=M,lw=.6)
    axes[0,i].set(xlim=(-.25,.45),ylim=(-.25,.3),xlabel='实部',ylabel='虚部',
        title=f'相位差 {round(phase*180/np.pi)}°；合成幅值 {abs(total):.1f}')
    axes[0,i].set_aspect('equal')
    axes[1,i].plot(tt*1000,.2*np.cos(2*np.pi*1000*tt),color=B,alpha=.5,label='分量 1')
    axes[1,i].plot(tt*1000,.2*np.cos(2*np.pi*1000*tt+phase),'--',color=G,alpha=.7,label='分量 2')
    axes[1,i].plot(tt*1000,np.real(total*np.exp(1j*2*np.pi*1000*tt)),color=R,label='叠加')
    axes[1,i].set(ylim=(-.45,.45),xlabel='时间（ms）',ylabel='无量纲幅值')
axes[1,0].legend(frameon=False,fontsize=9)
fig.suptitle('同频相干叠加：相位差会改变合成幅值',fontsize=18,fontweight='bold')
save(fig,'coherent-interference')

fig,axes=plt.subplots(1,3,figsize=(14,6))
hs=np.geomspace(.6,.002,16)
z0=1+1j
for step,color,label in [(hs,B,'沿实轴'),(1j*hs,R,'沿虚轴')]:
    quotient=((z0+step)**2-z0**2)/step
    axes[0].plot(quotient.real,quotient.imag,'o-',ms=4,color=color,label=label)
axes[0].scatter([2],[2],marker='x',s=90,color=G)
axes[0].set(title='（a）f(z)=z²，z0=1+j',xlabel='差商实部',ylabel='差商虚部')
axes[0].legend(frameon=False,fontsize=10)
axes[1].scatter([1,-1],[0,0],s=70,c=[B,R])
axes[1].text(.85,.12,'沿实轴：1',ha='right',fontsize=10)
axes[1].text(-.85,-.2,'沿虚轴：−1',fontsize=10)
axes[1].set(title='（b）f(z)=共轭 z：方向不同',xlim=(-1.5,1.5),ylim=(-.8,.8),xlabel='差商实部',ylabel='差商虚部')
axes[2].plot(hs,np.zeros_like(hs),'o-',color=B,label='沿实轴')
axes[2].plot(np.zeros_like(hs),-hs,'s--',color=R,label='沿虚轴')
axes[2].scatter([0],[0],marker='x',s=90,color=G)
axes[2].set(title='（c）f(z)=|z|²，仅 z0=0 可导',xlabel='差商实部',ylabel='差商虚部')
axes[2].legend(frameon=False,fontsize=10)
fig.suptitle('复导数必须对所有趋近方向给出同一个极限',fontsize=18,fontweight='bold')
save(fig,'complex-derivative')

f=np.linspace(0,2000,2001)
delay=.003
response=np.exp(-1j*2*np.pi*f*delay)
fig,axes=plt.subplots(2,1,figsize=(14,7.5),sharex=True)
axes[0].plot(f,np.angle(response)/np.pi,color=B)
axes[0].set(ylabel='主值相位 / π',ylim=(-1.15,1.15),title='（a）主值相位限制在约 −π 到 π，出现跳变')
axes[1].plot(f,-2*f*delay,color=G,label='已知连续相位：−2πfτ')
axes[1].plot(f[::50],np.unwrap(np.angle(response))[::50]/np.pi,'o',ms=3,color=R,label='稠密采样后展开')
axes[1].set(xlabel='频率（Hz）',ylabel='连续相位 / π',title='（b）同一个 3 ms 延迟，连续相位保留绕圈数')
axes[1].legend(frameon=False,fontsize=10)
fig.suptitle('对数与相位需要选分支，主值跳变不等于系统突变',fontsize=18,fontweight='bold')
save(fig,'log-and-phase')

fig,axes=plt.subplots(1,2,figsize=(14,6.5))
contour_records=[]
for ax,a in zip(axes,[.5,1.5]):
    circle=np.exp(1j*angle)
    ax.plot(circle.real,circle.imag,color=B)
    ax.annotate('',xy=(np.cos(.55),np.sin(.55)),xytext=(1,0),arrowprops={'arrowstyle':'->','color':B})
    ax.scatter([a],[0],marker='x',s=110,color=R,label=f'极点 a={a}')
    ax.set_aspect('equal');ax.axhline(0,color=M,lw=.6);ax.axvline(0,color=M,lw=.6)
    ax.set(xlim=(-1.3,1.9),ylim=(-1.3,1.3),xlabel='Re z',ylabel='Im z',
        title='（a）极点在内：积分 = 2πj' if a<1 else '（b）极点在外：积分 = 0')
    ax.legend(frameon=False)
    theta=2*np.pi*np.arange(4096)/4096
    zz=np.exp(1j*theta)
    value=np.mean(1/(zz-a)*1j*zz)*2*np.pi
    contour_records.append([float(value.real),float(value.imag)])
fig.suptitle('同一条逆时针圆周，积分还取决于内部是否有奇点',fontsize=18,fontweight='bold')
save(fig,'contours-and-poles')

a=.8
fig,axes=plt.subplots(1,2,figsize=(14,6.5))
grid=np.linspace(-1.5,1.5,400)
gx,gy=np.meshgrid(grid,grid)
axes[0].contourf(gx,gy,(gx*gx+gy*gy>a*a).astype(int),levels=[.5,1.5],colors=['#e4eff5'])
axes[0].plot(a*np.cos(angle),a*np.sin(angle),'--',color=R,label='极点模长 0.8：ROC 边界')
axes[0].plot(np.cos(angle),np.sin(angle),color=G,label='单位圆：频率响应取值位置')
axes[0].scatter([a],[0],marker='x',s=100,color=R)
axes[0].set_aspect('equal');axes[0].set(xlabel='Re z',ylabel='Im z',title='（a）因果序列的收敛域：|z| > 0.8')
axes[0].legend(frameon=False,fontsize=9,loc='lower left')
terms=np.arange(1,41)
for z,col,style in [(1.,B,'-'),(.9,G,'--'),(.6,R,':')]:
    q=a/z
    errors=np.abs(q**terms/(1-q))
    axes[1].semilogy(terms,errors,style,color=col,label=f'z={z}，|a/z|={q:.3f}')
axes[1].set(xlabel='外部级数截取项数 M',ylabel='截断和与有理式的绝对差',title='（b）收敛域之外，增加项数可能越算越远')
axes[1].legend(frameon=False,fontsize=10)
fig.suptitle('同一个有理式，必须连同收敛域解释它代表的序列',fontsize=18,fontweight='bold')
save(fig,'series-and-roc')

fs=16000
theta0=2*np.pi*1000/fs
nn=np.arange(600)
ff=np.linspace(0,2500,20001)
resonators=[]
fig,axes=plt.subplots(1,3,figsize=(14,6))
axes[0].plot(np.cos(angle),np.sin(angle),'--',color=M)
for r,col,style in [(.95,B,'-'),(.995,R,'--')]:
    poles=r*np.exp(1j*np.array([theta0,-theta0]))
    axes[0].scatter(poles.real,poles.imag,marker='x',s=80,color=col,label=f'r={r}')
    impulse=r**nn*np.sin((nn+1)*theta0)/np.sin(theta0)
    w,H=signal.freqz([1],[1,-2*r*np.cos(theta0),r*r],worN=ff,fs=fs)
    axes[1].plot(ff,20*np.log10(np.abs(H)),style,color=col,label=f'r={r}')
    axes[2].plot(nn/fs*1000,r**nn,style,color=col,label=f'r={r}')
    fpeak=fs/(2*np.pi)*np.arccos((1+r*r)/(2*r)*np.cos(theta0))
    resonators.append({'r':r,'time_constant_ms':float(-1000/(fs*np.log(r))),'peak_Hz':float(fpeak),
        'peak_gain':float(abs(1/(1-2*r*np.cos(theta0)*np.exp(-1j*2*np.pi*fpeak/fs)+r*r*np.exp(-2j*2*np.pi*fpeak/fs))))})
axes[0].set_aspect('equal');axes[0].set(xlim=(.8,1.05),ylim=(-.48,.48),xlabel='Re z',ylabel='Im z',title='（a）同角度，极点更近单位圆')
axes[1].set(xlim=(600,1400),xlabel='频率（Hz）',ylabel='幅度增益（dB）',title='（b）保持分子为1，峰更高更窄')
axes[2].set(xlabel='时间（ms）',ylabel='模态衰减因子 rⁿ',title='（c）这里只比较衰减因子')
for ax in axes: ax.legend(frameon=False,fontsize=9)
fig.suptitle('复极点的角度联系振荡，模长联系衰减',fontsize=18,fontweight='bold')
save(fig,'poles-and-resonance')

fig,axes=plt.subplots(1,2,figsize=(14,6.5))
semi=np.linspace(0,np.pi,500)
axes[0].plot([-3,3],[0,0],color=B)
axes[0].plot(3*np.cos(semi),3*np.sin(semi),color=B)
axes[0].scatter([0,0],[1,-1],marker='x',s=90,color=R)
axes[0].annotate('上半平面极点 j\n留数 = 1/(2j)',(0,1),(.4,1.4),fontsize=11)
axes[0].set_aspect('equal');axes[0].set(xlim=(-3.5,3.5),ylim=(-1.5,3.5),xlabel='Re w',ylabel='Im w',title='（a）积分核 1/(1+w²)，半圆半径趋于无穷')
u=np.linspace(0,5,1000)
power=1/(1+u*u)
axes[1].plot(u,power,color=B)
axes[1].fill_between(u,0,power,where=u<=1,color=G,alpha=.3,label='0 到 1 的面积 π/4')
axes[1].axvline(1,color=M,ls='--')
axes[1].set(xlabel='归一化角频率 u = Ω/ωc',ylabel='一阶低通平方幅度 |H|²',title='（b）0 到无穷的总面积 π/2；图仅画到5')
axes[1].legend(frameon=False,fontsize=10)
fig.suptitle('用留数计算实积分，再解释低通响应的面积',fontsize=18,fontweight='bold')
save(fig,'residue-and-bandwidth')

# Coherent same-frequency tone sums, common gain and common ramp.
duration=.7
time=np.arange(round(fs*duration))/fs
ramp=np.ones(len(time));edge=round(.01*fs)
ramp[:edge]=np.linspace(0,1,edge);ramp[-edge:]=np.linspace(1,0,edge)
audio=[]
for phase,name in zip(phases,['phase-0','phase-120','phase-180']):
    values=.2*np.cos(2*np.pi*1000*time)+.2*np.cos(2*np.pi*1000*time+phase)
    played=.6*ramp*values
    assert np.max(np.abs(played))<1
    pcm=np.rint(32767*played).astype('<i2')
    with wave.open(str(AUDIO/f'{name}.wav'),'wb') as f:
        f.setparams((1,2,fs,len(pcm),'NONE','not compressed'));f.writeframes(pcm.tobytes())
    audio.append({'name':name,'phase_degrees':float(phase*180/np.pi),
        'amplitude_before_playback':float(abs(.2*(1+np.exp(1j*phase)))),'peak_pcm':int(np.max(np.abs(pcm.astype(int))))})

P=.02+0j
V=.0001*np.exp(-1j*np.pi/3)
impedance=P/V
intensity=.5*np.real(P*np.conj(V))
record={'nature':'original analytic/synthetic teaching examples; no measured hearing or device data',
 'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},
 'phasor':{'amplitude_Pa':.02,'phase_rad':float(np.pi/3),'real_Pa':.01,'imag_Pa':float(.01*np.sqrt(3))},
 'specific_impedance':{'real_Pa_s_per_m':float(impedance.real),'imag_Pa_s_per_m':float(impedance.imag),
     'mean_intensity_W_per_m2':float(intensity),'pressure_peak_Pa':.02,'velocity_peak_m_per_s':.0001,'velocity_phase_rad':float(-np.pi/3)},
 'contours':contour_records,'series':{'a':.8,'M':8,'at_z_1_partial_sum':float(sum(.8**n for n in range(8))),
     'at_z_1_exact':5.,'at_z_1_absolute_tail':float(.8**8/.2)},
 'resonators':resonators,'resonator_fs_Hz':fs,'resonator_pole_angle_rad':float(theta0),
 'analog_lowpass':{'fc_Hz':1000,'omega_c_per_s':float(2000*np.pi),'time_constant_ms':float(1/(2*np.pi)),
     'gain_at_fc':float(1/np.sqrt(2)),'phase_at_fc_rad':float(-np.pi/4),'one_sided_square_response_area_Hz':float(500*np.pi)},
 'delay_s':delay,'audio':{'fs_Hz':fs,'duration_s':duration,'ramp_ms':10,'common_gain':.6,'individual_normalization':False,'files':audio}}
(REC/'calculations.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False,indent=2))
