"""Original, non-proportional teaching diagrams. Run with Python + Matplotlib.

No patient data or manufacturer images. SVG text stays editable; PNGs use
the same figure, with Chinese fonts selected from installed system fonts.
"""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle, Ellipse
from matplotlib.path import Path as MPath
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
names = {f.name for f in font_manager.fontManager.ttflist}
font = next((f for f in ['Microsoft YaHei', 'Noto Sans CJK SC', 'SimHei'] if f in names), None)
if not font:
    raise RuntimeError('Install Microsoft YaHei, Noto Sans CJK SC or SimHei.')
plt.rcParams.update({'font.family': font, 'font.size': 13, 'svg.fonttype': 'none', 'axes.unicode_minus': False})
BLUE, ORANGE, GREEN, INK, GRAY = '#286a9d', '#c56c22', '#297963', '#263744', '#9aa8ad'

def base(w, h):
    fig = plt.figure(figsize=(w/100, h/100), dpi=100, facecolor='white')
    ax = fig.add_axes([0,0,1,1]); ax.set(xlim=(0,w), ylim=(h,0)); ax.axis('off')
    return fig, ax

def text(ax, x, y, s, size=16, color=INK, ha='left', weight='normal'):
    return ax.text(x,y,s,fontsize=size,color=color,ha=ha,va='center',fontweight=weight)

def box(ax,x,y,w,h,label='',fc='#edf4f9',ec=BLUE,size=15):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=12',facecolor=fc,edgecolor=ec,lw=1.7))
    if label: text(ax,x+w/2,y+h/2,label,size,ha='center')

def arrow(ax,x1,y1,x2,y2,color=BLUE,style='-',lw=2.5):
    ax.annotate('',(x2,y2),(x1,y1),arrowprops=dict(arrowstyle='-|>',color=color,lw=lw,linestyle=style,shrinkA=2,shrinkB=2))

def save(fig, name):
    fig.savefig(OUT/(name+'.svg'),dpi=100)
    fig.savefig(OUT/(name+'.png'),dpi=100)
    plt.close(fig)

def ear(ax,x,y):
    # Simplified lateral cutaway: pinna on left, canal directed right.
    verts=[(x+165,y+240),(x+110,y+290),(x+85,y+218),(x+100,y+165),(x+43,y+95),(x+85,y+10),(x+156,y+15),(x+231,y+15),(x+243,y+111),(x+204,y+158)]
    codes=[MPath.MOVETO]+[MPath.CURVE3]*8+[MPath.LINETO]
    ax.add_patch(PathPatch(MPath(verts,codes),fc='none',ec=GRAY,lw=4))
    ax.plot([x+204,x+345],[y+158,y+158],color=GRAY,lw=3)
    ax.plot([x+184,x+345],[y+213,y+213],color=GRAY,lw=3)
    ax.plot([x+345,x+351],[y+158,y+213],color=GRAY,lw=3)
    ax.add_patch(Ellipse((x+182,y+178),57,86,fc='#f5f7f8',ec=GRAY,lw=1.5))
    text(ax,x+342,y+238,'鼓膜',12,GRAY,ha='center')

# Figure 1: six styles in a shared coordinate system.
fig,ax=base(1440,960)
text(ax,42,39,'部件放在哪里？',24,weight='bold')
text(ax,42,77,'同一耳部参照的简化剖示 · 位置示意，不按实际比例',15)
styles=[('（a）BTE 耳背式','声管连接耳模'),('（b）RIC／RITE','导线连接耳道内受话器'),('（c）ITE 耳内式','外壳占据耳甲腔'),('（d）ITC 耳道式','外壳靠近耳道入口'),('（e）CIC 完全耳道式','主要位于耳道内'),('（f）IIC 深耳道式','更深放置，需符合耳形')]
for i,(title,caption) in enumerate(styles):
    x=30+(i%3)*475; y=116+(i//3)*405
    text(ax,x+12,y+10,title,18,weight='bold'); ear(ax,x+26,y+42)
    if i<2:
        box(ax,x+65,y+86,35,107,fc='#dcebf6')
        if i==0:
            ax.add_patch(Rectangle((x+73,y+107),18,30,fc=ORANGE))
            ax.plot([x+82,x+90,x+154,x+201,x+239],[y+103,y+66,y+62,y+150,y+228],color=ORANGE,lw=3,ls='--')
            box(ax,x+203,y+205,47,49,fc='#d9e2e6',ec=GRAY)
        else:
            ax.plot([x+82,x+90,x+154,x+201,x+283],[y+103,y+66,y+62,y+150,y+228],color=BLUE,lw=2.5)
            ax.add_patch(Ellipse((x+287,y+228),28,48,fc='#e7ecee',ec=GRAY))
            ax.add_patch(Rectangle((x+267,y+216),27,23,fc=ORANGE))
    else:
        specs={2:(173,153,66,109),3:(211,200,58,56),4:(254,207,48,45),5:(296,207,40,45)}
        dx,dy,w,h=specs[i];box(ax,x+dx,y+dy,w,h,fc='#dcebf6')
        ax.add_patch(Rectangle((x+dx+w-24,y+dy+h/2-9),18,18,fc=ORANGE))
    text(ax,x+237,y+362,caption,15,ha='center')
text(ax,45,936,'蓝色区域：机壳／定制外壳     橙色块：受话器     灰色：耳部结构／耦合件',15)
save(fig,'01-styles')

# Figure 2: functional interfaces, not anatomical distances.
fig,ax=base(1440,720)
text(ax,42,40,'BTE 与 RIC：电声转换发生在哪里？',24,weight='bold')
for i,title in enumerate(['（a）BTE：受话器在耳后','（b）RIC：受话器在耳道']):
    y=120+i*280;text(ax,45,y,title,19,weight='bold')
    box(ax,45,y+38,550,170,fc='#f5f8fa',ec=GRAY);text(ax,65,y+65,'耳后机壳',14)
    box(ax,825,y+38,555,170,fc='#f5f8fa',ec=GRAY);text(ax,845,y+65,'耳道',14)
    box(ax,75,y+100,175,65,'麦克风 → 处理器',size=14)
    if i==0:
        box(ax,365,y+100,160,65,'受话器',fc='#fbebde',ec=ORANGE)
        arrow(ax,250,y+132,365,y+132)
        arrow(ax,525,y+132,900,y+132,ORANGE,'--')
        text(ax,706,y+108,'声管：声波',16,ORANGE,ha='center')
        box(ax,900,y+100,180,65,'耳模／耳塞',fc='white',ec=GRAY)
        arrow(ax,1080,y+132,1220,y+132,ORANGE,'--')
    else:
        arrow(ax,250,y+132,900,y+132,BLUE)
        text(ax,706,y+108,'导线：电信号',16,BLUE,ha='center')
        box(ax,900,y+100,180,65,'受话器',fc='#fbebde',ec=ORANGE)
        arrow(ax,1080,y+132,1220,y+132,ORANGE,'--')
    text(ax,1280,y+132,'耳内声场',16,ha='center')
text(ax,45,686,'实线：电信号     虚线：声学路径     受话器 = 微型扬声器',16)
save(fig,'02-bte-ric')

# Figure 3: straightened ear canal; consistent RIC receiver in all panels.
fig,ax=base(1440,840)
text(ax,42,40,'同一种 RIC，可以采用不同耳道耦合',24,weight='bold')
for i,(title,note) in enumerate([('（a）开放耳塞','保留较大的直达声通路'),('（b）通气耳模','通过设计的通气孔连通'),('（c）较封闭耳模','减少泄漏，需评估自身声音')]):
    x=40+i*475;text(ax,x,108,title,19,weight='bold')
    text(ax,x+180,167,'外界 → 耳道 → 鼓膜',15,ha='center')
    ax.plot([x+20,x+370],[280,280],color=GRAY,lw=5)
    ax.plot([x+20,x+370],[510,510],color=GRAY,lw=5)
    ax.plot([x+370,x+382],[280,510],color=GRAY,lw=4)
    if i==0:
        ax.add_patch(Ellipse((x+185,405),58,120,fc='#dcebf6',ec=BLUE,lw=2))
        arrow(ax,x+25,320,x+337,320,GREEN,'--');text(ax,x+150,249,'直达声',14,GREEN,ha='center')
    else:
        box(ax,x+125,282,107,226,fc='#dcebf6',ec=BLUE)
        if i==1:
            ax.add_patch(Rectangle((x+124,311),109,27,fc='white',ec='none'))
            ax.plot([x+125,x+232],[311,311],color=BLUE,lw=1)
            ax.plot([x+125,x+232],[338,338],color=BLUE,lw=1)
            arrow(ax,x+25,325,x+337,325,GREEN,'--')
            text(ax,x+178,249,'通气孔',14,GREEN,ha='center')
        else:
            text(ax,x+180,249,'实际密封需验证',14,ha='center')
    ax.plot([x+20,x+160],[420,420],color=BLUE,lw=3)
    box(ax,x+160,383,58,45,fc='#fbebde',ec=ORANGE)
    arrow(ax,x+220,405,x+340,405,ORANGE)
    text(ax,x+190,560,'受话器仍在耳道内',15,ha='center')
    text(ax,x+190,630,note,15,ha='center')
text(ax,42,730,'蓝色：耳部接口与导线     橙色：受话器及输出     绿色虚线：直达声通路',16)
text(ax,42,780,'耳道直管化示意；图中箭头不表示声级，通路也允许声音向外泄漏。',15)
save(fig,'03-coupling')

# Figure 4: signal routing, explicitly distinct ear inputs.
fig,ax=base(1440,960)
text(ax,42,40,'两侧都有设备，声音是否分别进入两只耳？',24,weight='bold')
for i,title in enumerate(['（a）常规双耳助听：两耳均可助听','（b）CROS：较好耳正常或接近正常','（c）BiCROS：较好耳也需要放大']):
    y=110+i*275;text(ax,45,y,title,19,weight='bold')
    if i==0:
        for x,side in [(90,'左'),(910,'右')]:
            box(ax,x,y+50,380,65,side+'侧采集 → 处理')
            arrow(ax,x+190,y+115,x+190,y+153,ORANGE)
            box(ax,x,y+153,380,60,side+'耳获得声学输入',fc='#fbebde',ec=ORANGE)
    else:
        box(ax,90,y+50,380,65,'较差侧：传声端')
        box(ax,910,y+50,380,65,'接收端' if i==1 else '接收端 + 本地采集与放大')
        arrow(ax,470,y+82,905,y+82,BLUE);text(ax,685,y+57,'跨耳传输',15,BLUE,ha='center')
        box(ax,90,y+153,380,60,'此耳不获得助听声输出',fc='#f5f7f8',ec=GRAY,size=15)
        arrow(ax,1100,y+115,1100,y+153,ORANGE)
        box(ax,910,y+153,380,60,'较好耳获得声学输入',fc='#fbebde',ec=ORANGE,size=15)
        if i==1:
            arrow(ax,710,y+183,905,y+183,GREEN,'--')
            text(ax,695,y+154,'自然声',14,GREEN)
text(ax,45,936,'橙色：耳内声学输出     蓝色：电子信号路由     绿色：自然声输入（示例配置）',15)
save(fig,'04-routing')

manifest={'font':font,'figures':4,'data':'original conceptual diagrams; no patient data; not to scale','dimensions':{'01-styles':[1440,960],'02-bte-ric':[1440,720],'03-coupling':[1440,840],'04-routing':[1440,960]},'invariants':['BTE receiver behind ear; RIC receiver in canal','all coupling panels use an in-canal receiver','CROS/BiCROS output only to better ear in these examples','arrows do not encode benefit or sound level']}
(OUT/'validation.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False))
