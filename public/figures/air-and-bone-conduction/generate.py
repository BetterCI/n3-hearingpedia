"""Original conceptual figures; all audiometric numbers are synthetic, not norms."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

OUT=Path(__file__).resolve().parent
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists(): font_manager.fontManager.addfont(str(font))
plt.rcParams.update({'font.family':'Microsoft YaHei' if font.exists() else 'sans-serif',
                     'font.size':13,'svg.fonttype':'path','axes.unicode_minus':False,
                     'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white'})
BLUE='#176b9b'; ORANGE='#b7572a'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'))
    fig.savefig(OUT/(name+'.png'),dpi=150)
    plt.close(fig)

fig,ax=plt.subplots(figsize=(9,8),layout='constrained')
ax.set(xlim=(0,10),ylim=(0,9));ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.12',
                              fc='white',ec=color,lw=1.8))
    ax.text(x,y,text,ha='center',va='center',color=color,linespacing=1.6)
def arrow(a,b):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#687782'})
ax.text(5,8.7,'不同机械输入，共同作用于耳蜗',ha='center',fontsize=18,weight='bold')
box(2.3,7.5,3.3,.9,'气导：外部空气声压',BLUE)
box(7.5,7.5,3.3,.9,'骨导：头部机械刺激',ORANGE)
box(2.3,4.8,3.3,2,'耳道声压\n鼓膜与听骨链运动\n内耳液体耦合',BLUE)
box(7.5,4.8,3.9,3.1,'并行机械贡献\n耳道壁辐射声压\n听骨链相对运动\n内耳液体惯性\n骨性边界形变\n颅内压力传递',ORANGE)
arrow((2.3,6.9),(2.3,6));arrow((7.5,6.9),(7.5,6.5))
box(5,2,5.4,.9,'耳蜗内的压差与相对运动',BLUE)
arrow((2.3,3.65),(3.3,2.6));arrow((7.5,3.1),(6.7,2.6))
box(5,.55,5.4,.8,'感觉换能 → 听神经与中枢处理',BLUE)
arrow((5,1.4),(5,1.08))
save(fig,'routes')

freq=np.array([500,1000,2000,4000])
examples=[('传导性模式：骨导相对保留',[35,40,35,40],[5,10,5,10]),
          ('感音神经性模式：两条曲线共同升高',[35,40,45,50],[35,40,45,50]),
          ('混合性模式：骨导升高，同时仍有差值',[60,65,70,75],[30,35,40,45])]
fig,axes=plt.subplots(3,1,figsize=(9,10),layout='constrained')
gaps={}
for ax,(title,ac,bc) in zip(axes,examples):
    ax.plot(freq,ac,'o-',color=BLUE,ms=9,label='气导：自定义圆点')
    ax.plot(freq,bc,'s--',color=ORANGE,ms=6,mfc='white',label='骨导：自定义方点')
    ax.set_xscale('log',base=2);ax.set_xticks(freq,[str(f) for f in freq])
    ax.set(title=title,xlabel='频率 / Hz',ylabel='听阈 / dB HL',ylim=(90,-10))
    ax.set_yticks(np.arange(-10,91,20));ax.grid(alpha=.22);ax.legend(loc='lower left',fontsize=11)
    gaps[title]=(np.array(ac)-np.array(bc)).tolist()
assert gaps[examples[0][0]]==[30]*4
assert gaps[examples[1][0]]==[0]*4
assert gaps[examples[2][0]]==[30]*4
save(fig,'audiograms')

at,bt,bn,ia,ib=70,40,10,40,0
au=min(at,bn+ia);bu=min(bt,bn+ib)
assert (au,bu,au-bu,at-bt)==(50,10,40,30)
fig,ax=plt.subplots(figsize=(9,5.6),layout='constrained')
pos=np.arange(3);w=.32
bars1=ax.bar(pos-w/2,[at,au,at],w,label='气导',color=BLUE)
bars2=ax.bar(pos+w/2,[bt,bu,bt],w,label='骨导',color=ORANGE)
ax.bar_label(bars1,padding=3);ax.bar_label(bars2,padding=3)
ax.set_xticks(pos,['模型真实阈值','未掩蔽的可能读数','充分且不过量掩蔽'])
ax.set(ylim=(0,90),ylabel='阈值 / dB HL',title='跨耳检出可制造较好的表面听阈')
ax.grid(axis='y',alpha=.18);ax.legend(loc='upper left')
save(fig,'cross-hearing')

m=np.arange(0,71,10)
threshold=np.minimum(m+10,40)+np.maximum(m-50,0)
assert threshold.tolist()==[10,20,30,40,40,40,50,60]
fig,ax=plt.subplots(figsize=(9,5.6),layout='constrained')
ax.axvspan(0,30,color='#f2e1d8',alpha=.7)
ax.axvspan(30,50,color='#e0efe8',alpha=.8)
ax.axvspan(50,70,color='#f2e1d8',alpha=.7)
ax.plot(m,threshold,'o-',color=BLUE,lw=2)
for x,text in [(15,'不足掩蔽区'),(40,'平台区'),(60,'过掩蔽区')]:
    ax.text(x,68,text,ha='center',fontsize=12)
ax.set(xlim=(0,70),ylim=(0,75),xlabel='相对任意起点的掩蔽增量 / dB',
       ylabel='测试音阈值 / dB HL',title='理想平台示意：区段边界不代表临床操作值')
ax.grid(alpha=.18)
save(fig,'plateau')

# Phasor subtraction and scale examples are algebraic checks, not physiological fits.
same=abs(1+0j-(1+0j));opposite=abs(1+0j-(-1+0j))
assert same==0 and opposite==2
result={'data_type':'synthetic educational examples; no patient data',
        'audiogram_frequencies_Hz':freq.tolist(),'air_bone_gaps_dB':gaps,
        'cross_hearing':{'test_AC_dBHL':at,'test_BC_dBHL':bt,'other_BC_dBHL':bn,
        'assumed_AC_IA_dB':ia,'assumed_BC_IA_dB':ib,'unmasked_AC_dBHL':au,
        'unmasked_BC_dBHL':bu,'apparent_gap_dB':au-bu,'true_gap_dB':at-bt},
        'plateau':{'relative_masker_increment_dB':m.tolist(),'tone_threshold_dBHL':threshold.tolist(),
        'clinical_setting_values':False},'unit_pressure_phasor_difference':{'same_phase':same,'opposite_phase':opposite},
        'assertions':'passed','numpy':np.__version__,'matplotlib':matplotlib.__version__}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Four figures generated; numeric assertions passed.')
