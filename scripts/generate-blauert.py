"""Original functional diagrams and a two-point ITD calculation, not listener data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'public/figures/jens-blauert'
RESEARCH = ROOT/'docs/research/jens-blauert-2026-10-10'
OUT.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei', 'font.size':13, 'svg.fonttype':'path'})
BLUE, ORANGE, GREEN, GRAY = '#276582', '#ad683c', '#477e63', '#526472'

def save(fig, name):
    for ext in ['svg', 'png']:
        path = OUT/(name+'.'+ext)
        fig.savefig(path, dpi=100, facecolor='white')
        if ext == 'svg':
            path.write_text('\n'.join(line.rstrip() for line in path.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

def box(ax, x, y, w, h, title, detail='', color=BLUE, size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008,rounding_size=0.012',lw=1.5,edgecolor=color,facecolor='#f6f9fb'))
    ax.text(x+w/2,y+h*.69,title,ha='center',va='center',color=color,fontsize=size,fontweight='bold')
    ax.text(x+w/2,y+h*.3,detail,ha='center',va='center',fontsize=12,color=GRAY,linespacing=1.5)

def arrow(ax, a, b, color=GRAY, style='-'):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':color,'lw':1.7,'linestyle':style,'shrinkA':0,'shrinkB':0})

fig, ax = plt.subplots(figsize=(12.8,6.5))
fig.subplots_adjust(left=.035,right=.965,top=.81,bottom=.14)
fig.suptitle('把物理布置、两耳信号和感知报告分别验证',fontsize=21,fontweight='bold',y=.95)
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
xs=[.018,.27,.522,.774]
titles=['声源与房间','到达两耳的信号','听觉事件','行为报告']
details=['位置、方向、反射\n刺激与背景','时间、声级、频谱\n传递函数与校准','方向、范围、距离印象\n对象与场景','定位角度、事件宽度\n外化评分、质量判断']
checks=['核对几何与刺激条件','测量或计算耳边信号','用模型解释候选线索','用具体任务检验感知']
for i,(x,title,detail,check) in enumerate(zip(xs,titles,details,checks)):
    box(ax,x,.55,.207,.3,title,detail, [BLUE,BLUE,ORANGE,GREEN][i])
    if i<3: arrow(ax,(x+.217,.70),(xs[i+1]-.013,.70))
    ax.text(x+.1035,.38,check,ha='center',fontsize=13,color=GRAY)
    arrow(ax,(x+.1035,.51),(x+.1035,.425),style='--')
ax.text(.5,.16,'物理声源的位置 ≠ 听者报告的位置；同一刺激可产生不同任务结果',ha='center',fontsize=16,color=BLUE)
fig.text(.5,.055,'原创功能框图；没有神经解剖结构、听者数据或一对一映射假设',ha='center',fontsize=12,color=GRAY)
save(fig,'event-and-evidence')

d,c=.18,343.
theta=np.linspace(-180,180,1441)
tau=d*np.sin(np.deg2rad(theta))/c*1e6
pair=d*np.sin(np.deg2rad([30.,150.]))/c*1e6
assert np.allclose(pair,pair[0])
assert np.isclose(tau.max(),d/c*1e6)
assert np.allclose(tau,-tau[::-1])
assert np.allclose(d*np.sin(np.deg2rad([0,180]))/c,0)
fig, axs=plt.subplots(1,2,figsize=(12.8,6.5))
fig.subplots_adjust(left=.075,right=.965,top=.78,bottom=.22,wspace=.35)
fig.suptitle('相同的两耳到达时间差，可对应前后两个方向',fontsize=21,fontweight='bold',y=.95)
ax=axs[0]
ax.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),aspect='equal',title='（a）方向空间与两点接收模型')
ax.axis('off')
ax.plot([-1,1],[0,0],color='#d8e0e5',lw=1)
ax.plot([0,0],[-1,1],color='#d8e0e5',lw=1)
ax.text(0,1.02,'前方 0°',ha='center',fontsize=12)
ax.text(0,-1.1,'后方 180°',ha='center',fontsize=12)
ax.text(1.03,0,'右',ha='left',fontsize=12)
ax.text(-1.03,0,'左',ha='right',fontsize=12)
for angle,col,marker in [(30,BLUE,'o'),(150,ORANGE,'s')]:
    x,y=np.sin(np.deg2rad(angle)),np.cos(np.deg2rad(angle))
    ax.annotate('',xy=(x,y),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':col})
    ax.plot(x,y,marker,color=col,ms=7)
    ax.text(x+.06,y,f'{angle}°',color=col,va='center',fontsize=14)
# Receiver positions on a one-metre radial display: distance d remains geometrically correct.
ax.plot([-d/2,d/2],[0,0],'o',color=GREEN,ms=8)
ax.text(-.1,-.14,'L',ha='center',fontsize=12,color=GREEN)
ax.text(.1,-.14,'R',ha='center',fontsize=12,color=GREEN)
ax.text(-.75,-.72,'接收点间距 d = 0.18 m\n箭头指向声源方向\n平面远场；无头部遮挡',fontsize=11,color=GRAY,linespacing=1.5)
ax=axs[1]
ax.plot(theta,tau,color=BLUE,lw=2)
ax.axhline(0,color='#a5b4bd',lw=.8)
ax.axhline(pair[0],color=ORANGE,lw=1.4,ls='--')
ax.plot([30,150],pair,'o',color=ORANGE,ms=7)
ax.text(86,pair[0]+80,f'30° 与 150°：{pair[0]:.0f} μs',ha='center',color=ORANGE,fontsize=12)
ax.set(xlim=(-180,180),ylim=(-610,610),xticks=[-180,-90,0,90,180],xlabel='方位角 θ / °（0° 前，90° 右，180° 后）',ylabel='左耳到达减右耳到达 Δτ / μs',title='（b）Δτ = d sinθ / c')
ax.grid(alpha=.18);ax.set_axisbelow(True)
ax.spines[['top','right']].set_visible(False)
fig.text(.5,.065,'d = 0.18 m；c = 343 m/s；最大差约 525 μs\n原创几何计算，不是人体实测；未模拟耳廓、声级差、近场或头部运动',ha='center',fontsize=12,color=GRAY)
save(fig,'itd-ambiguity')

fig,ax=plt.subplots(figsize=(12.8,7.5))
fig.subplots_adjust(left=.035,right=.965,top=.84,bottom=.10)
fig.suptitle('双耳房间模拟：从场景条件到可检验的聆听结果',fontsize=21,fontweight='bold',y=.96)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
box(ax,.02,.71,.25,.22,'场景与听者条件','几何、材料、声源位置\n两耳位置与朝向')
box(ax,.34,.71,.29,.22,'声场与双耳传递','生成或读取 hL、hR\n保留传播与方向线索')
arrow(ax,(.28,.82),(.325,.82))
box(ax,.02,.38,.19,.20,'干声 x','未含目标房间的输入')
box(ax,.34,.30,.29,.32,'双通道卷积','yL = x * hL\nyR = x * hR',size=15)
arrow(ax,(.22,.49),(.325,.49))
arrow(ax,(.485,.695),(.485,.635))
box(ax,.74,.38,.23,.24,'校准重放与聆听','耳机及校准条件\n任务与行为测量',color=GREEN)
arrow(ax,(.64,.49),(.725,.49))
ax.text(.35,.15,'静态：固定位置与朝向\n动态：追踪姿态并更新传递；检验延迟与切换',ha='center',fontsize=12,color=GRAY,linespacing=1.5)
ax.text(.84,.17,'输出不是“保真”结论\n还需验证感知结果',ha='center',fontsize=12,color=GREEN,linespacing=1.5)
fig.text(.5,.04,'验证三层：声场和传播条件 → 耳边信号和重放 → 定位、外化、理解与质量\n原创功能示意；不是1992年软件实现复原；没有实测声场、听者数据或效果预测',ha='center',fontsize=12,color=GRAY)
save(fig,'binaural-simulation')

manifest=[
 {'name':'event-and-evidence','nature':'original functional diagram','source_ids':['blauert-median','blauert-introduction'],'limits':'No neural anatomy, fixed causality or measured perceptual outcome'},
 {'name':'itd-ambiguity','nature':'original far-field two-point geometric calculation','receiver_distance_m':d,'sound_speed_m_s':c,'angle_definition':'0 front; 90 right; 180 back','delay_definition':'left arrival minus right arrival','angles_deg':[30,150],'delays_us':pair.tolist(),'maximum_delay_us':d/c*1e6,'checks':['equal delays for front-back pair','maximum equals d/c','odd symmetry','zero at 0 and 180 degrees'],'source_ids':['middlebrooks-1991'],'limits':'No head diffraction, pinna, near field, level differences or movement'},
 {'name':'binaural-simulation','nature':'original functional diagram','source_ids':['blauert-room','blauert-sofa'],'limits':'Not a historic software reconstruction or measured behavioral prediction'}
]
(RESEARCH/'figure-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':3,'equal_delay_us':float(pair[0]),'checks':'passed','auditory_models_executed':False}))
