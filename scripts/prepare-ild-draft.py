"""Reproduce original teaching figures and checked calculations; no empirical data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT/'docs/drafts/assets/interaural-level-difference'
RESEARCH = ROOT/'docs/research/ild-2026-10-11'
ASSETS.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)
font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc').get_name()
plt.rcParams.update({'font.family':font,'svg.fonttype':'path','axes.unicode_minus':False,
                     'font.size':11,'axes.spines.top':False,'axes.spines.right':False,
                     'axes.titlepad':14,'figure.facecolor':'white','axes.facecolor':'white'})
PURPLE, TEAL, GRAY = '#6952b4', '#267f80', '#667085'
def save(fig, name):
    fig.savefig(ASSETS/f'{name}.svg', bbox_inches=None)
    fig.savefig(ASSETS/f'{name}.png', dpi=150)
    plt.close(fig)
def foot(fig, text):
    fig.text(.055,.035,text,fontsize=9,color=GRAY)

left=np.array([1.,4.]);right=np.array([4.,1.]);band_ild=10*np.log10(left/right)
assert np.allclose(band_ild,[-6.020599913,6.020599913])
assert np.isclose(10*np.log10(left.sum()/right.sum()),0)
fig,axs=plt.subplots(1,2,figsize=(12.8,5.4))
fig.subplots_adjust(left=.08,right=.97,top=.83,bottom=.22,wspace=.35)
x=np.arange(2);axs[0].bar(x-.17,left,.32,label='左耳',color=PURPLE);axs[0].bar(x+.17,right,.32,label='右耳',color=TEAL)
axs[0].set(xticks=x,xticklabels=['频带 A','频带 B'],ylabel='均方声压（统一的相对单位）',ylim=(0,5.1),title='两耳宽带能量相等，频谱却不同');axs[0].legend(frameon=False)
axs[1].bar([0,1,2],[*band_ild,0],color=[TEAL,PURPLE,GRAY],width=.55)
axs[1].axhline(0,color=GRAY,lw=.8);axs[1].set(xticks=[0,1,2],xticklabels=['频带 A','频带 B','宽带合计'],ylabel='ILD = 左耳声级 − 右耳声级（dB）',ylim=(-8,8),title='频带内相反的 ILD 在宽带统计中抵消')
for i,v in enumerate([*band_ild,0]):axs[1].text(i,v+(.45 if v>=0 else -.45),f'{v:+.2f} dB',ha='center',va='bottom' if v>=0 else 'top',fontsize=11)
foot(fig,'原创教学数据：两频带互不重叠；先合计均方声压再取对数。此图不代表某一频率的实测 HRTF。')
save(fig,'01-ild-frequency')

a=.09
def geo(r,theta):
    rad=np.deg2rad(theta)
    dl=np.sqrt(r*r+a*a-2*r*a*np.sin(rad)); dr=np.sqrt(r*r+a*a+2*r*a*np.sin(rad))
    return 20*np.log10(dr/dl)
angles=np.linspace(0,90,181);dist=np.geomspace(.15,5,300)
fig,axs=plt.subplots(1,2,figsize=(12.8,5.4));fig.subplots_adjust(left=.075,right=.965,top=.82,bottom=.24,wspace=.32)
for r,c,ls in [(.2,PURPLE,'-'),(.5,TEAL,'--'),(2,GRAY,':')]:axs[0].plot(angles,geo(r,angles),color=c,ls=ls,lw=2,label=f'r = {r:g} m')
axs[0].set(xlabel='朝左的方位角 θ（度）',ylabel='仅由距离差产生的 ILD（dB）',title='距离更近时，两耳传播距离差更显著',xlim=(0,90));axs[0].legend(frameon=False)
axs[1].semilogx(dist,geo(dist,90),color=PURPLE,lw=2)
for r in [.3,3]:
 v=float(geo(r,90));axs[1].plot(r,v,'o',color=TEAL);axs[1].annotate(f'{r:g} m：{v:.2f} dB',(r,v),xytext=(7,8),textcoords='offset points',fontsize=10)
axs[1].set(xlabel='声源到两耳中点的距离 r（m，对数轴）',ylabel='仅由距离差产生的 ILD（dB）',title='正左侧声源（θ = 90°）',ylim=(0,14));axs[1].grid(alpha=.17)
foot(fig,'原创解析模型：耳间距 2a = 0.18 m，点声源声压 ∝ 1/d；未计头部散射、耳廓、频率响应或反射。\n两耳只是采样点；该模型不能替代真实头部或近场 HRTF。')
save(fig,'02-near-field-geometry')

fig,axs=plt.subplots(1,2,figsize=(12.8,5.6));fig.subplots_adjust(left=.03,right=.96,top=.85,bottom=.24,wspace=.18)
ax=axs[0];ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off');ax.set_title('以左侧 LSO 为例的主要输入关系')
def box(x,y,w,h,label,c):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor='white',edgecolor=c,lw=1.6));ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10,color=c)
box(.3,6.7,2.7,1.5,'左耳 → 左侧\n耳蜗核',PURPLE);box(.3,2.2,2.7,1.5,'右耳 → 右侧\n耳蜗核',TEAL);box(4,2.2,2.2,1.5,'左侧 MNTB',TEAL);box(7,5,2.2,1.8,'左侧 LSO',PURPLE)
ax.annotate('',xy=(7,6.15),xytext=(3,7.35),arrowprops={'arrowstyle':'->','color':PURPLE,'lw':2});ax.text(4.5,7.2,'兴奋',color=PURPLE)
ax.annotate('',xy=(4,2.95),xytext=(3,2.95),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2});ax.text(3.5,4,'兴奋',ha='center',color=TEAL,fontsize=10)
ax.annotate('',xy=(7,5.25),xytext=(6.2,3.1),arrowprops={'arrowstyle':'-[','color':TEAL,'lw':2});ax.text(7.3,3.7,'抑制',color=TEAL)
ax.text(5,.45,'MNTB：内侧斜方体核\nLSO：外侧上橄榄',ha='center',fontsize=9,color=GRAY)
d=np.linspace(-20,20,250)
for b,c,ls in [(-3,TEAL,'--'),(0,PURPLE,'-'),(3,GRAY,':')]:axs[1].plot(d,1/(1+np.exp(-.35*(d-b))),color=c,ls=ls,lw=2,label=f'假设拐点 b = {b:+g} dB')
axs[1].set(xlabel='ILD（左 − 右，dB）',ylabel='归一化反应（无量纲）',ylim=(0,1.05),title='假设的率—ILD曲线：说明拐点变化');axs[1].legend(frameon=False,fontsize=9,loc='upper left')
foot(fig,'左：经典兴奋／抑制路径的功能示意，省略其他连接；左右对称路径未画出。\n右：原创 sigmoid 教学曲线，斜率参数 0.35/dB，非神经记录；不同曲线不对应实测声级或特定细胞。')
save(fig,'03-lso-circuit')

knee=50.;outknee=60.;cr=3.
def transfer(l):return np.where(l<=knee,l+(outknee-knee),outknee+(l-knee)/cr)
inp=np.array([66.,54.]);ind=transfer(inp);gain=float(transfer(inp.max())-inp.max());linked=inp+gain
assert np.isclose(ind[0]-ind[1],4);assert np.isclose(linked[0]-linked[1],12)
fig,axs=plt.subplots(1,2,figsize=(12.8,5.4));fig.subplots_adjust(left=.075,right=.96,top=.83,bottom=.25,wspace=.33)
li=np.linspace(30,80,200);axs[0].plot(li,transfer(li),color=PURPLE,lw=2);axs[0].axvline(knee,ls=':',color=GRAY)
axs[0].set(xlabel='单耳输入声级（dB，统一参考）',ylabel='单耳输出声级（dB，统一参考）',title='教学压缩曲线：拐点以上压缩比 3:1')
for i,c in enumerate([PURPLE,TEAL]):axs[0].scatter(inp[i],ind[i],color=c,s=40);axs[0].annotate(f'{inp[i]:g} → {ind[i]:.2f}',(inp[i],ind[i]),xytext=(4,7),textcoords='offset points',fontsize=9)
x=np.arange(3);axs[1].bar(x-.17,[inp[0],ind[0],linked[0]],.32,color=PURPLE,label='左耳');axs[1].bar(x+.17,[inp[1],ind[1],linked[1]],.32,color=TEAL,label='右耳')
axs[1].set(xticks=x,xticklabels=['输入','两耳独立压缩','共同增益'],ylim=(0,90),ylabel='声级（dB，统一参考）',title='同一输入，增益控制方式改变输出 ILD');axs[1].legend(frameon=False,loc='upper right')
for i,v in enumerate([12,4,12]):axs[1].text(i,70,f'ILD = {v} dB',ha='center',fontsize=10)
foot(fig,'原创静态示例：输入 66/54 dB，拐点 50 dB、拐点输出 60 dB。共同增益取较强耳决定的同一增益。\n未计攻击／释放时间、限幅、频率通道、底噪或实际设备；保持 ILD 不等于保证远耳可听性或定位效果。')
save(fig,'04-compression')

calc={'kind':'Original teaching calculations; not empirical data or clinical norms',
 'convention':'ILD = L_left - L_right',
 'band_example':{'left_mean_square':[1,4],'right_mean_square':[4,1],'band_ild_db':band_ild.tolist(),'broadband_ild_db':0},
 'wavelength_m':{'250_Hz':343/250,'4000_Hz':343/4000},
 'six_db':{'pressure_ratio':10**(6/20),'progressive_wave_intensity_ratio':10**(6/10),'sum_energy_change_db_at_fixed_mean_db':10*np.log10((10**.3+10**-.3)/2)},
 'geometry':{'half_ear_spacing_m':a,'left_source_90_deg_ild_db':{'0.3_m':float(geo(.3,90)),'3_m':float(geo(3.,90))},'assumptions':'point source, inverse distance pressure, sample points only, no scattering'},
 'sigmoid':{'slope_per_db':.35,'inflections_db':[-3,0,3],'units':'normalized dimensionless response'},
 'compression':{'input_db':inp.tolist(),'knee_input_db':knee,'knee_output_db':outknee,'ratio':cr,'independent_output_db':ind.tolist(),'common_gain_db':gain,'linked_output_db':linked.tolist()},
 'checks':['band ILDs ±6.0206 dB and broadband 0','independent compression ILD 4 dB','common-gain ILD 12 dB']}
(RESEARCH/'calculations.json').write_text(json.dumps(calc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('4 SVG/PNG figure pairs and calculations.json created')
