"""Original pedagogical plots; no clinical data, norms or device recommendations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'docs/drafts/assets/acoustic-immittance-tympanometry'
RESEARCH=ROOT/'docs/research/immittance-2026-10-11'
ASSETS.mkdir(parents=True,exist_ok=True);RESEARCH.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name(),
 'svg.fonttype':'path','axes.unicode_minus':False,'font.size':11,'figure.facecolor':'white',
 'axes.spines.top':False,'axes.spines.right':False,'axes.titlepad':14})
P,T,G='#6952b4','#267f80','#667085'
def save(fig,name):
 fig.savefig(ASSETS/(name+'.svg'));fig.savefig(ASSETS/(name+'.png'),dpi=150);plt.close(fig)
def foot(fig,t):fig.text(.055,.035,t,fontsize=9,color=G)

# Single passive port with R=M*omega0=1/(C*omega0)=Z0.
rho,c,S=1.2,343.,.5e-4;Z0=rho*c/S;f0=1000.;R=Z0;M=Z0/(2*np.pi*f0);C=1/(Z0*2*np.pi*f0)
f=np.geomspace(125,8000,400);w=2*np.pi*f
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.07,right=.97,top=.83,bottom=.23,wspace=.3)
ax[0].semilogx(f,w*M/Z0,color=P,label='质量抗：ωM/Z0')
ax[0].semilogx(f,-1/(w*C*Z0),color=T,ls='--',label='顺性抗：−1/(ωCZ0)')
ax[0].semilogx(f,(w*M-1/(w*C))/Z0,color=G,ls=':',lw=2,label='总声抗 X/Z0')
ax[0].axhline(0,color=G,lw=.7);ax[0].set(xlabel='频率（Hz，对数轴）',ylabel='归一化声抗（无量纲）',ylim=(-6,6),title='声抗由质量与顺性共同决定');ax[0].legend(frameon=False,fontsize=10)
for ms,ks,label,color,ls in [(1,1,'基准参数',P,'-'),(1,2,'刚度 ×2',T,'--'),(2,1,'质量 ×2',G,':')]:
 z=R+1j*(w*M*ms-ks/(w*C));y=Z0/abs(z);ax[1].semilogx(f,y,label=label,color=color,ls=ls,lw=2)
 rf=f0*np.sqrt(ks/ms);ax[1].plot(rf,1,'o',color=color)
ax[1].set(xlabel='频率（Hz，对数轴）',ylabel='归一化导纳幅值 |Y|Z0（无量纲）',ylim=(0,1.16),title='同一单自由度模型：共振位置移动');ax[1].legend(frameon=False,fontsize=10)
for axis in ax:axis.set_xticks([125,250,500,1000,2000,4000,8000],labels=['125','250','500','1000','2000','4000','8000']);axis.tick_params(axis='x',labelsize=9)
foot(fig,'原创集中参数模型：Z = R + j(ωM − 1/ωC)，R = Z0，基准共振 1 kHz。采用 exp(jωt) 约定。\n曲线不是正常耳模板；真实耳存在多个模态、腔室、负载及测量位置效应。')
save(fig,'01-complex-immittance')

q=np.linspace(-400,200,601);sigma=70.;tw=2*np.sqrt(2*np.log(2))*sigma
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.075,right=.97,top=.83,bottom=.23,wspace=.32)
def gauss(amp,mean,s):return amp*np.exp(-.5*((q-mean)/s)**2)
for amp,mu,s,label,color,ls in [(1,0,70,'A：单峰',P,'-'),(.3,0,65,'As：峰较低',T,'--'),(2,0,65,'Ad：峰较高',G,':'),(1,-180,75,'C：峰偏负压','#ad6b32','-.')]:ax[0].plot(q,gauss(amp,mu,s),color=color,ls=ls,lw=2,label=label)
ax[0].plot(q,np.full_like(q,.07),color='#444',ls=(0,(5,3)),label='B：近似平坦');ax[0].set(xlabel='耳道静压 q（daPa，相对环境）',ylabel='补偿导纳幅值（声学 mmho）',ylim=(0,2.4),title='低频鼓室图的形态词汇');ax[0].legend(frameon=False,fontsize=9,ncol=2,loc='upper left')
tail=.7;total=tail+gauss(1,0,sigma)
ax[1].plot(q,total,color=P,lw=2,label='总导纳幅值（教学假设）');ax[1].axhline(tail,color=G,ls=':',label='假定耳道尾端分量 0.7')
ax[1].vlines(0,tail,1.7,color=T,lw=2);ax[1].text(70,1.55,'峰高 − 尾端\n= 1.0 mmho',fontsize=10,color=T)
half=tw/2;ax[1].hlines(1.2,-half,half,color=T,lw=2);ax[1].text(-260,1.27,f'半高宽 TW = {tw:.1f} daPa',fontsize=10,color=T)
ax[1].set(xlabel='耳道静压 q（daPa，相对环境）',ylabel='导纳幅值（声学 mmho）',ylim=(0,2.2),title='峰压、补偿峰高与半高宽');ax[1].legend(frameon=False,fontsize=9,loc='upper left')
foot(fig,'原创高斯教学曲线；曲线类型不是病因诊断。右图假设耳道与中耳导纳同相，可作幅值相减。\n峰压 0 daPa、峰高 1.7、尾端 0.7 mmho，σ = 70 daPa；不提供临床正常范围。')
save(fig,'02-tympanogram')

rmag=.6;angles=[0,np.pi/3];rr=rmag*np.exp(1j*np.array(angles));zz=(1+rr)/(1-rr);A=1-rmag*rmag
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.075,right=.97,top=.82,bottom=.23,wspace=.32)
ax[0].bar([0,1],[A,A],color=P,width=.5,label='吸收率 A = 0.64')
ax[0].bar([0,1],[.36,.36],bottom=[A,A],color='#d8d2e8',width=.5,label='功率反射率 = 0.36')
ax[0].set(xticks=[0,1],xticklabels=['反射系数相位 0°','反射系数相位 60°'],ylabel='相对入射功率（无量纲）',ylim=(0,1.18),title='相同 |r| = 0.6：吸收率完全相同');ax[0].legend(frameon=False,fontsize=10)
ax[1].axhline(0,lw=.7,color=G);ax[1].axvline(0,lw=.7,color=G)
for z,label,color in zip(zz,['0°：Z/Z0 = 4','60°：Z/Z0 ≈ 0.842 + j1.367'],[P,T]):
 ax[1].annotate('',xy=(z.real,z.imag),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':color});ax[1].text(z.real+.08,z.imag+.09,label,fontsize=10,color=color)
ax[1].set(xlabel='归一化声阻 Re(Z/Z0)',ylabel='归一化声抗 Im(Z/Z0)',xlim=(-.2,5.25),ylim=(-.3,2),title='相位不同：复数阻抗明显不同')
foot(fig,'原创解析例子：r = (Z − Z0)/(Z + Z0)，Z0 为实数特性阻抗；被动、单端口、无损管道近似。\nA = 1 − |r|² 表示未返回的功率比例，既不保留反射相位，也不指明到耳蜗的功率。')
save(fig,'03-reflectance-phase')

qme=-120.;qs=180.;press=np.linspace(-300,200,201);freq=np.geomspace(250,8000,220)
def absorb(ff,qq):
 ww=2*np.pi*ff;kfac=1+((qq-qme)/qs)**2;z=R+1j*(ww*M-kfac/(ww*C));r=(z-Z0)/(z+Z0);return 1-abs(r)**2
grid=absorb(freq[:,None],press[None,:]);assert grid.min()>=0 and grid.max()<=1+1e-12
fig,ax=plt.subplots(1,2,figsize=(12.8,5.5));fig.subplots_adjust(left=.075,right=.965,top=.83,bottom=.24,wspace=.38)
im=ax[0].pcolormesh(press,freq/1000,grid,shading='auto',cmap='viridis',vmin=0,vmax=1);ax[0].set_yscale('log');ax[0].set(xlabel='耳道静压 q（daPa）',ylabel='频率（kHz，对数轴）',title='压力—频率吸收率教学图')
ax[0].axvline(0,color='white',ls='--',lw=1.5);ax[0].axvline(qme,color='white',ls=':',lw=1.5)
fig.colorbar(im,ax=ax[0],label='吸收率 A（无量纲）',pad=.03)
for pp,label,color,ls in [(0,'环境压力：q = 0 daPa',P,'--'),(qme,'设定压差抵消点：q = −120 daPa',T,'-')]:ax[1].semilogx(freq,absorb(freq,pp),label=label,color=color,ls=ls,lw=2)
ax[1].set(xlabel='频率（Hz，对数轴）',ylabel='吸收率 A（无量纲）',ylim=(0,1.12),title='同一压力—频率面上的两个切片');ax[1].legend(frameon=False,fontsize=9,loc='upper right')
ax[0].set_yticks([.25,.5,1,2,4,8],labels=['0.25','0.5','1','2','4','8'])
ax[1].set_xticks([250,500,1000,2000,4000,8000],labels=['250','500','1000','2000','4000','8000']);ax[1].tick_params(axis='x',labelsize=9)
foot(fig,'原创单端口模型：设定中耳静压 −120 daPa，以 K(q)/K0 = 1 + [(q + 120)/180]² 表示附加刚度。\n该压力依赖为教学假设，无临床拟合；设定点不等于所有频率的实测峰压，改变耳道压力也不是治疗。')
save(fig,'04-wideband-pressure')

volume=1e-6;yc=2*np.pi*226*volume/(rho*c*c);complex_total=1+1j;tail_y=.7j
comp=abs(complex_total-tail_y);scalar=abs(complex_total)-abs(tail_y)
assert np.isclose(A,.64);assert np.isclose(zz[0],4)
assert np.isclose(comp,np.sqrt(1.09));assert scalar<comp
examples={'scope':'Original illustrative calculations, not empirical data, reference norms or recommendations',
 'time_convention':'exp(j omega t)','units':{'impedance':'Pa s / m^3','admittance':'m^3 / (Pa s)','acoustic_mmho_si':1e-8},
 'model':{'rho_kg_m3':rho,'c_m_s':c,'area_m2':S,'Z0':Z0,'R':R,'M_acoustic_kg_m4':M,'C_acoustic_m3_Pa':C,'f0_Hz':f0,'stiffness_x2_resonance_Hz':f0*np.sqrt(2),'mass_x2_resonance_Hz':f0/np.sqrt(2)},
 'equivalent_volume':{'volume_cm3':1,'frequency_Hz':226,'admittance_SI':yc,'admittance_acoustic_mmho':yc/1e-8,'assumptions':'rigid sealed small cavity, ideal uniform pressure, rho=1.2 and c=343'},
 'tympanogram':{'gaussian_sigma_daPa':sigma,'width_half_height_daPa':tw,'total_peak_acoustic_mmho':1.7,'tail_acoustic_mmho':.7,'compensated_peak_acoustic_mmho':1},
 'complex_compensation':{'total_G_B':[1,1],'tail_G_B':[0,.7],'complex_difference_magnitude':comp,'difference_of_magnitudes':scalar,'unit':'acoustic mmho'},
 'reflectance':{'magnitude':rmag,'angles_degrees':[0,60],'absorbance':A,'normalized_impedance':[{'real':float(z.real),'imag':float(z.imag)} for z in zz]},
 'pressure_model':{'middle_ear_pressure_daPa':qme,'stiffness_pressure_scale_daPa':qs,'ambient_resonance_Hz':f0*np.sqrt(1+(qme/qs)**2)},
 'checks':['passive model absorbance in [0,1]','equal reflection magnitudes imply equal absorbance','complex compensation differs from scalar subtraction','rigid 1 cm3 cavity near 1 acoustic mmho at 226 Hz']}
(RESEARCH/'calculations.json').write_text(json.dumps(examples,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('4 SVG/PNG pairs and calculations.json created')
