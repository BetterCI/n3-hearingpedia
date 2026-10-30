"""Original educational figures; no experimental observations are reproduced."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

plt.rcParams.update({'font.family': 'Microsoft YaHei', 'svg.fonttype': 'none', 'font.size': 13,
                     'axes.spines.top': False, 'axes.spines.right': False})
out=Path('public/figures/basilar-membrane');out.mkdir(parents=True,exist_ok=True)
x=np.linspace(0,1,1200)
f=165.4*(10**(2.1*(1-x))-.88)
def save(fig,name):
    fig.savefig(out/f'{name}.svg',facecolor='white')
    svg=out/f'{name}.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(out/f'{name}.png',dpi=160,facecolor='white');plt.close(fig)
fig,ax=plt.subplots(figsize=(12,5.4),dpi=100)
ax.semilogy(x*100,f,color='#167d94',linewidth=3)
table=[]
for tone in [500,1000,3000]:
    place=1-np.log10(tone/165.4+.88)/2.1
    table.append({'frequency_hz':tone,'fraction_from_base':float(place),'distance_mm_if_L35':float(place*35)})
    ax.scatter(place*100,tone,s=60,color='#d67832',zorder=3)
    ax.annotate(f'{tone} Hz / {place*100:.1f}%',(place*100,tone),xytext=(10,12),textcoords='offset points',fontsize=12)
ax.set(xlabel='距蜗底的全长比例（%）   蜗底 → 蜗顶',ylabel='参考频率（Hz，对数刻度）',xlim=(0,100),ylim=(18,24000),title='基底膜频位参考：Greenwood 人耳函数')
ax.grid(alpha=.2);fig.subplots_adjust(left=.11,right=.97,bottom=.18,top=.88)
fig.text(.11,.04,'教学计算：A = 165.4 Hz，a = 2.1，k = 0.88；不是个体实测。',fontsize=11,color='#526370')
save(fig,'place-map')

# One-frequency steady state of the exact digital filters used by the lab.
fs=48000;Q=5;tone=1000;w=2*np.pi*f/fs;alpha=np.sin(w)/(2*Q)
b0=alpha/(1+alpha);a1=-2*np.cos(w)/(1+alpha);a2=(1-alpha)/(1+alpha)
z=np.exp(-1j*2*np.pi*tone/fs)
H=(b0-b0*z*z)/(1+a1*z+a2*z*z)
delay=np.round(fs*(.0003+.006*x*x))/fs
response=H*np.exp(-2j*np.pi*tone*delay)
fig,ax=plt.subplots(figsize=(12,5.4),dpi=100)
ax.plot(x*100,response.real,color='#167d94',label='某时刻的有符号响应')
ax.plot(x*100,np.abs(response),color='#d67832',linewidth=2,label='正弦振幅包络')
ax.plot(x*100,-np.abs(response),color='#d67832',linestyle='--',alpha=.5)
ax.set(xlabel='距蜗底的全长比例（%）',ylabel='相对响应（任意单位）',title='1000 Hz：一帧波形与空间包络回答不同问题',xlim=(0,100),ylim=(-1.15,1.3));ax.legend(loc='upper left',fontsize=11);ax.grid(alpha=.2)
fig.subplots_adjust(left=.11,right=.97,bottom=.20,top=.88)
fig.text(.11,.05,'数字滤波器教学计算：48 kHz，Q = 5，附加延迟 0.3 + 6x² ms；非耦合行波求解。',fontsize=10,color='#526370')
save(fig,'parallel-filter-envelope')

# Passive 1D pressure/partition coupling; independently solved with SciPy.
def coupled(frequency, count=1201):
    x=np.linspace(0,1,count); dx=.035/(count-1); omega=2*np.pi*frequency
    omega0=2*np.pi*165.4*(10**(2.1*(1-x))-.88)
    D=.3*(omega0**2-omega**2+2j*.05*omega0*omega)
    q=2*1000*omega**2/(.001*D)
    ab=np.zeros((3,count-2),complex)
    ab[0,1:]=1; ab[1,:]=-2+dx*dx*q[1:-1]; ab[2,:-1]=1
    rhs=np.zeros(count-2,complex); rhs[0]=-1
    pressure=np.r_[1,solve_banded((1,1),ab,rhs),0]
    y=pressure/D; y/=max(np.abs(y))
    return x,y
x,y=coupled(1000)
fig,ax=plt.subplots(figsize=(12,5.4),dpi=100)
ax.plot(x*100,y.real,color='#167d94',label='某时刻的有符号位移')
ax.plot(x*100,np.abs(y),color='#d67832',linewidth=2,label='正弦位移振幅包络')
ax.plot(x*100,-np.abs(y),color='#d67832',linestyle='--',alpha=.6)
ax.set(xlabel='距蜗底的全长比例（%）',ylabel='相对位移（逐频峰值归一化）',title='1000 Hz：一维被动耦合模型的非对称包络',xlim=(0,100),ylim=(-1.15,1.3))
ax.legend(loc='upper left',fontsize=11);ax.grid(alpha=.2)
fig.subplots_adjust(left=.11,right=.97,bottom=.20,top=.88)
fig.text(.11,.05,'教学参数：L = 35 mm，h = 1 mm，ρ = 1000 kg/m³，m = 0.3 kg/m²，ζ = 0.05；非活体拟合。',fontsize=10,color='#526370')
save(fig,'wave-and-envelope')
checks=[]
for frequency in [60,250,500,1000,3000,8000,16000]:
    xx,yy=coupled(frequency); A=np.abs(yy); peak=int(np.argmax(A)); half=np.where(A>=.5)[0]
    xf,yf=coupled(frequency,2401)
    checks.append({'frequency':frequency,'peak_fraction':float(xx[peak]),'basal_halfwidth_mm':float((peak-half[0])*.035/1200*1000),'apical_halfwidth_mm':float((half[-1]-peak)*.035/1200*1000),'fine_grid_peak_fraction':float(xf[np.argmax(np.abs(yf))]),'samples':[{'index':i,'re':float(yy[i].real),'im':float(yy[i].imag)} for i in [0,120,360,600,720,960,1200]]})
record=Path('docs/research/basilar-membrane-2026-10-30');record.mkdir(parents=True,exist_ok=True)
(record/'coupled-reference.json').write_text(json.dumps({'method':'independent scipy.linalg.solve_banded; peak-normalized; not experimental data','parameters':{'length_m':.035,'height_m':.001,'density_kg_m3':1000,'mass_kg_m2':.3,'damping_ratio':.05,'nodes':1201,'boundary':'p(0)=1 Pa, p(L)=0'},'checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')

fig,axes=plt.subplots(1,2,figsize=(12,5.4),dpi=100)
for ax in axes:ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
for ax,title,labels in [(axes[0],'记录机械响应',['已知声压与参考相位','基底膜 / 网状板 / 盖膜','位移或速度 → 传递函数']),
                         (axes[1],'解释感觉结果',['机械电转导与相对运动','受体电位 → 突触 → 神经','行为任务：检测、分辨、识别'])]:
    ax.set_title(title,pad=18,fontweight='bold')
    for i,label in enumerate(labels):
        yy=.82-i*.28
        ax.text(.5,yy,label,ha='center',va='center',fontsize=13,bbox={'boxstyle':'round,pad=.8','facecolor':'#e9f3f5','edgecolor':'#7faebb'})
        if i<2:ax.annotate('',xy=(.5,yy-.17),xytext=(.5,yy-.08),arrowprops={'arrowstyle':'->','color':'#387c90','lw':2})
fig.subplots_adjust(left=.03,right=.97,bottom=.17,top=.84,wspace=.17)
fig.text(.5,.045,'两列是不同观测层级：膜位移不能直接替代毛束刺激、神经响应或主观感知。',ha='center',fontsize=12,color='#526370')
save(fig,'measurement-chain')
(out/'parameters.json').write_text(json.dumps({'nature':'educational, not experimental','sample_rate':fs,'Q':Q,'delay_ms':'0.3+6*x^2','place_examples':table,'figure2_default':'passive-1D-coupled','figure2_coupled_parameters':{'length_m':.035,'height_m':.001,'density_kg_m3':1000,'mass_kg_m2':.3,'damping_ratio':.05,'nodes':1201,'normalization':'per-frequency peak','boundaries':'p(0)=1 Pa, p(L)=0'}},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(table,ensure_ascii=False))
