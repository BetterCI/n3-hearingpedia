"""Original teaching figures: ideal sound paths and evidence relationships."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/figures/comparative-hearing'
RESEARCH = ROOT / 'docs/research/comparative-hearing-2026-10-10'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 13, 'svg.fonttype': 'path'})
BLUE, GREEN, ORANGE, GRAY = '#286582', '#367d66', '#aa6239', '#526472'
records = []

def save(fig, name, params, size):
    for ext in ['svg', 'png']:
        fig.savefig(OUT / (name + '.' + ext), dpi=100, facecolor='white')
    plt.close(fig)
    records.append({'name': name, 'width': size[0], 'height': size[1], 'parameters': params,
                    'nature': 'original conceptual diagram or analytic teaching calculation; not animal, human or device measurements'})

def canvas(title, subtitle, height=720):
    fig, ax = plt.subplots(figsize=(12.8, height / 100))
    ax.set(xlim=(0, 1280), ylim=(0, height))
    ax.axis('off')
    ax.text(640, height-48, title, ha='center', fontsize=23, weight='bold')
    ax.text(640, height-94, subtitle, ha='center', fontsize=14, color=GRAY)
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax

def box(ax, x, y, w, h, text, color=BLUE, fontsize=14):
    ax.add_patch(FancyBboxPatch((x,y), w,h, boxstyle='round,pad=0,rounding_size=10',
                              facecolor='#f3f7fa', edgecolor=color, lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fontsize,color=color,linespacing=1.55)

def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1), arrowprops={'arrowstyle':'->','color':GRAY,'lw':1.8})

fig, ax = canvas('从动物听觉到人类研究：三条证据路线', '先明确解决的问题，再决定需要怎样的跨物种验证')
for x,w,t in [(35,230,'动物与问题'),(305,340,'可检验的机制'),(685,550,'对人类的研究方向')]:
    ax.text(x+w/2,566,t,ha='center',fontsize=16,weight='bold',color=GRAY)
rows = [
    (435, '仓鸮\n两耳时间比较', '延迟与符合检测\n经验怎样校准空间表征', '机制解释\n用人体行为与生理资料检验模型', BLUE),
    (315, '蝙蝠\n回声属于哪次发声？', '发声与接收构成闭环\n频谱、时序和方向共同起作用', '机制与训练\n设计人类回声定位的独立测试', BLUE),
    (195, '寄生蝇 Ormia\n耳间距极小仍需定位', '鼓膜机械耦合\n增强接收结构的方向性', '仿生工程\n从传感器实验到设备与使用者评价', GREEN),
    (75, '鸡与鹌鹑\n受损后重新形成毛细胞', '支持细胞参与再生\n组织恢复与功能恢复分别测量', '听觉修复\n验证成熟哺乳动物中的可行性', ORANGE),
]
for y,t1,t2,t3,col in rows:
    box(ax,35,y,230,92,t1,col)
    box(ax,305,y,340,92,t2,col)
    box(ax,685,y,550,92,t3,col)
    arrow(ax,265,y+46,300,y+46); arrow(ax,645,y+46,680,y+46)
ax.text(640,25,'箭头表示研究思路；不表示机制相同、应用已成熟或临床疗效已经成立',ha='center',fontsize=12,color=GRAY)
save(fig,'evidence-routes',{'layout':'four representative cases, three translational routes'},(1280,720))

c=343.0
theta=np.linspace(-90,90,361)
small_d=.00052
large_d=.18
small=small_d*np.sin(np.deg2rad(theta))/c*1e6
large=large_d*np.sin(np.deg2rad(theta))/c*1e6
dist=np.linspace(0,3,301)
delay=2*dist/c*1e3
assert np.isclose(small[-1],1.5160349854227404)
assert np.isclose(delay[100],5.830903790087463)
fig, axs = plt.subplots(1,2,figsize=(12.8,6.8))
fig.subplots_adjust(left=.085,right=.94,bottom=.23,top=.74,wspace=.40)
fig.suptitle('两种时间线索：双耳路径差与回声往返',fontsize=23,weight='bold',y=.95)
fig.text(.5,.86,'理想传播算例：静止空气、c = 343 m/s；与神经和行为阈值分别解释',ha='center',color=GRAY,fontsize=14)
ax=axs[0]
positive=theta>=1
ax.plot(theta[positive],large[positive],color=BLUE,lw=2,label='教学间距 d = 18 cm')
ax.plot(theta[positive],small[positive],color=ORANGE,lw=2,ls='--',label='d = 0.52 mm')
ax.set_yscale('log')
ax.set(xlabel='声源角度 θ（°）',ylabel='时间差幅度 |Δt|（µs，对数轴）',title='（a）Δt = d sinθ / c',xlim=(0,90),ylim=(.01,1000),xticks=[0,30,60,90])
ax.legend(loc='upper left',fontsize=11)
ax.text(27,.12,'同一角度下\n幅度相差约346倍',fontsize=12,color=GRAY)
axs[1].plot(dist,delay,color=GREEN,lw=2)
axs[1].scatter([1],[2/c*1e3],color=GREEN,zorder=3)
axs[1].text(1.15,5.5,'1 m → 5.83 ms',fontsize=12,color=GREEN)
axs[1].set(xlabel='目标距离 r（m）',ylabel='往返时间 t（ms）',title='（b）t = 2r / c',xlim=(0,3),ylim=(0,19),xticks=[0,1,2,3])
for ax in axs:
    ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16)
fig.text(.5,.10,'0.52 mm对应文献所述寄生蝇耳间距；18 cm仅为教学设定，未建模头部绕射或鼓膜耦合',ha='center',fontsize=12,color=GRAY)
fig.text(.5,.055,'回声曲线忽略反射强弱、多径与处理延迟；两图都不能推出可辨方向或距离的阈值',ha='center',fontsize=12,color=GRAY)
save(fig,'time-cues',{'sound_speed_m_s':c,'ear_distances_m':[small_d,large_d],'angle_definition':'positive means right-path longer, broadside zero','plot_angle_degrees':[1,90],'time_difference_axis':'absolute value, logarithmic, microseconds','echo_distance_m':[0,3]},(1280,680))

fig, ax=canvas('怎样判断听觉修复是否成立？','分层测量并相互约束：后一个结论需要补充证据，而非由前一个自动推出',760)
stages=[
    (575,'1　细胞来源','谱系与增殖证据：新生细胞，还是原有细胞改变标志物？',BLUE),
    (455,'2　成熟与连接','细胞身份、毛束与突触：形成的细胞能否承担相应功能？',BLUE),
    (335,'3　外周与通路','感受与电生理响应：测量位置、刺激和残余功能是否明确？',GREEN),
    (215,'4　听觉行为','听阈、辨别与复杂声音任务：不同功能是否共同恢复？',GREEN),
    (95,'5　人体应用','持续收益与不良影响：需要人体研究及临床结局评价',ORANGE),
]
for y,lab,txt,col in stages:
    box(ax,80,y,270,80,lab,col,15)
    box(ax,395,y,800,80,txt,col,14)
    arrow(ax,350,y+40,389,y+40)
    if y>95: arrow(ax,215,y-2,215,y-36)
ax.text(640,32,'这是评价框架，不是某个物种或治疗已完成全部阶段的记录',ha='center',fontsize=12,color=GRAY)
save(fig,'repair-evidence',{'stages':['origin','maturity and connectivity','physiology','behavior','human outcomes'],'nature':'editorial evaluation framework'},(1280,760))
(RESEARCH/'figure-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Generated 3 SVG and PNG figures; analytic calculations verified.')
