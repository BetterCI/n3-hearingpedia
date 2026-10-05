from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle, Arc, PathPatch
from matplotlib.path import Path as MPath
from matplotlib.font_manager import FontProperties
folder=Path('docs/drafts/assets/cochlea')
font=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'svg.fonttype':'none','axes.unicode_minus':False,'font.size':12,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
ink='#25313b'; blue='#2675a1'; ochre='#b78333'; red='#ad5050'; green='#427969'
def txt(ax,x,y,s,**kwargs): return ax.text(x,y,s,color=ink,ha='center',va='center',**kwargs)
def arrow(ax,a,b,color=ink,**kwargs): ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.3,'color':color,**kwargs})
def leader(ax,a,b,s,ha='left',color=ink):
    ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=.9)
    ax.text(b[0]+(.08 if ha=='left' else -.08),b[1],s,ha=ha,va='center',color=color,fontsize=11)
def save(fig,name):
    fig.savefig(folder/(name+'.svg'),bbox_inches='tight',pad_inches=.18)
    fig.savefig(folder/(name+'.png'),dpi=190,bbox_inches='tight',pad_inches=.18)
    p=folder/(name+'.svg');p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    plt.close(fig)
# Cross-section: simplified outer envelope split into perilymph and triangular scala media.
fig,ax=plt.subplots(figsize=(11,7.4));ax.set_xlim(-1.2,11);ax.set_ylim(-.2,8.8);ax.axis('off')
outer=Ellipse((4.6,4.4),7.3,6.7,facecolor='#eef6fa',edgecolor=ink,lw=1.8);ax.add_patch(outer)
media=Polygon([[2.45,3.55],[2.45,4.9],[7.65,6.35],[7.65,3.55]],facecolor='#fff3d4',edgecolor='none');ax.add_patch(media)
ax.plot([2.45,7.65],[4.9,6.35],color=ochre,lw=1.8)
ax.plot([2.45,2.45],[3.55,4.9],color='#777',lw=2)
ax.plot([1.04,2.45],[3.55,3.55],color='#777',lw=5,solid_capstyle='butt')
ax.plot([2.45,7.65],[3.55,3.55],color=green,lw=2.5)
ax.add_patch(Rectangle((7.55,3.65),.19,2.4,color='#d09c56',alpha=.85))
# Supporting epithelial microstructure, with a pillar tunnel and one inner / three outer cells.
ax.add_patch(Polygon([[3.05,3.58],[3.95,4.25],[4.5,3.58]],facecolor='#eef0ef',edgecolor='#999',lw=1))
ax.plot([3.7,3.95,4.25],[3.6,4.25,3.6],color='#888',lw=2.2)
for x,y,w,h,c in [(3.25,3.98,.42,.8,blue),(4.8,4.02,.28,.9,red),(5.35,4.04,.28,.9,red),(5.9,4.06,.28,.9,red)]:
    ax.add_patch(Ellipse((x,y),w,h,facecolor=c,alpha=.75,edgecolor=ink,lw=.6))
    for k in range(3):ax.plot([x-.07+k*.07,x-.07+k*.07],[y+h/2,y+h/2+.12+k*.025],color=ink,lw=.8)
ax.plot([3.0,3.6,4.0,4.8,5.35,5.9,6.45],[4.33,4.38,4.31,4.43,4.45,4.47,4.15],color='#656565',lw=1.1)
ax.add_patch(Polygon([[2.85,4.45],[3.2,4.72],[5.9,4.72],[6.6,4.55],[6.3,4.47]],facecolor='#d9dfda',edgecolor=green,lw=1))
ax.add_patch(Ellipse((.65,3.1),.95,1.5,facecolor='#f2e5da',edgecolor=ink,lw=1))
for dx,dy in [(-.1,-.25),(.1,.2),(-.1,.35),(.15,-.35)]:ax.add_patch(Ellipse((.65+dx,3.1+dy),.18,.18,facecolor=ochre,edgecolor='none'))
ax.plot([3.25,2.95,1.8,1.0],[3.65,3.25,3.25,3.1],color=ochre,lw=1.3)
ax.text(3.8,6.55,'前庭阶\n外淋巴',ha='center',va='center',fontsize=15,color=blue,linespacing=1.8)
ax.text(6.35,5.35,'蜗管（中阶）\n内淋巴',ha='center',va='center',fontsize=13,color=ochre,linespacing=1.8)
ax.text(4.4,2.3,'鼓阶\n外淋巴',ha='center',va='center',fontsize=15,color=blue,linespacing=1.8)
leader(ax,(4.8,4.89),(8.7,7.45),'前庭膜') # target must sit on sloped line; corrected below
# Replace the just-added leader's target to the Reissner slope at x5.5.
ax.lines[-1].set_data([5.5,8.7],[4.9+(5.5-2.45)*1.45/5.2,7.45])
leader(ax,(7.65,5.0),(8.7,6.35),'血管纹')
leader(ax,(6.0,4.62),(8.7,5.35),'盖膜')
leader(ax,(5.35,4.04),(8.7,4.25),'柯蒂器：毛细胞与支持细胞')
leader(ax,(6.8,3.55),(8.7,3.15),'基底膜')
leader(ax,(3.7,4.34),(2.65,7.95),'网状板',ha='right')
leader(ax,(.65,3.1),(-.1,1.3),'螺旋神经节',ha='left')
ax.text(-.9,6.8,'蜗轴侧',fontsize=12,color=ink)
ax.text(8.7,1.6,'外侧壁',fontsize=12,color=ink)
ax.text(4.65,.2,'局部横断面示意 · 非按比例绘制 · 蜗孔位于蜗顶，未在此图表示',ha='center',fontsize=11,color='#666')
save(fig,'01-cross-section')
# Place map and illustrative spatial response envelopes.
d=np.linspace(0,1,700); freq=165.4*(10**(2.1*(1-d))-.88)
fig,(a,b)=plt.subplots(1,2,figsize=(11.7,5.9),gridspec_kw={'width_ratios':[1,1.15]})
fig.subplots_adjust(wspace=.33,bottom=.24,top=.87,left=.09,right=.97)
a.plot(d,freq/1000,color=blue,lw=2)
a.set_yscale('log');a.set_xlim(0,1);a.set_ylim(.02,25)
a.set_yticks([.02,.1,.5,1,4,8,20],['0.02','0.1','0.5','1','4','8','20'])
a.set_xlabel('从蜗底起算的归一化距离 d');a.set_ylabel('经验对应频率（千赫）');a.grid(axis='y',which='major',alpha=.18)
a.set_title('A  经验频位映射关系',loc='left',fontsize=14,pad=18)
b.set_title('B  定性行波包络',loc='left',fontsize=14,pad=18)
colors=[red,ochre,blue];positions={}
for j,(f,c) in enumerate(zip([8000,4000,1000],colors)):
    p=1-np.log10(f/165.4+.88)/2.1;positions[str(f)]=float(p)
    a.plot(p,f/1000,'o',ms=5,color=c)
    a.annotate(f'{f/1000:g}千赫',(p,f/1000),xytext=(9,-10),textcoords='offset points',fontsize=10,color=c)
    width=np.where(d<p,.17,.042)
    env=np.exp(-.5*((d-p)/width)**2);env=env/env.max()
    off=2-j;b.plot(d,.77*env+off,color=c,lw=1.9);b.fill_between(d,off,.77*env+off,color=c,alpha=.07)
    b.plot([0,1],[off,off],color='#ddd',lw=.8)
    b.plot([p,p],[off,off+.77],color=c,lw=.8,ls='--')
    b.text(.03,off+.45,f'{f/1000:g}千赫',color=c,fontsize=11)
b.set_xlim(0,1);b.set_ylim(-.25,3.25);b.set_yticks([.385,1.385,2.385],['1千赫','4千赫','8千赫']);b.tick_params(axis='y',length=0)
b.set_ylabel('各包络峰值分别归一化为1（纵向错开）',labelpad=15,fontsize=11)
b.set_xlabel('从蜗底起算的归一化距离 d')
arrow(b,(.1,2.99),(.7,2.99),color=ink);b.text(.4,3.13,'经典行波发展方向',ha='center',fontsize=10)
for q in [a,b]:q.set_xticks([0,.25,.5,.75,1],['0\n蜗底','0.25','0.50','0.75','1\n蜗顶'])
fig.text(.5,.035,'左图：格林伍德人耳经验函数，x = 1 − d。右图：教学包络，非实测或力学模型解。',ha='center',fontsize=11,color='#666')
save(fig,'02-place-and-wave')
# IHC synaptic versus OHC mechanical output, not actual adjacency/scale.
fig,ax=plt.subplots(figsize=(11.7,7.3));ax.set_xlim(0,12);ax.set_ylim(.2,10.2);ax.axis('off')
ax.add_patch(Rectangle((.15,7.6),11.7,2.1,facecolor='#fff5de',edgecolor='none'))
ax.plot([.15,11.85],[7.6,7.6],color='#9d9d9d',lw=1.5)
ax.text(6,9.28,'内淋巴：高钾环境',ha='center',fontsize=14,color=ochre)
ax.text(6,6.4,'基底外侧\n细胞外环境',ha='center',va='center',color='#666',fontsize=11,linespacing=1.8)
# flask-like IHC ending exactly at apical interface
verts=[(2.35,7.6),(2.2,6.95),(1.55,6.55),(1.65,5.2),(1.65,3.1),(3.85,3.1),(3.85,5.2),(3.95,6.55),(3.3,6.95),(3.15,7.6),(2.35,7.6)]
path=MPath(verts,[MPath.MOVETO]+[MPath.CURVE3]*8+[MPath.LINETO,MPath.CLOSEPOLY])
ax.add_patch(PathPatch(path,facecolor='#e7f2f8',edgecolor=blue,lw=1.8))
ax.add_patch(Ellipse((8.8,5.49),1.05,4.22,facecolor='#faeeee',edgecolor=red,lw=1.8))
# flatten top OHC border to apical interface with short cap
ax.plot([8.55,9.05],[7.6,7.6],color=red,lw=2)
for cx in [2.75,8.8]:
    for k in range(4):
        x=cx-.18+k*.12; top=8.05+k*.16
        ax.plot([x,x+.03],[7.6,top],color=ink,lw=2)
        if k<3:ax.plot([x+.03,x+.14],[top,top+.03],color=ink,lw=.8)
    arrow(ax,(cx-.36,8.75),(cx+.33,8.75),color=ink)
    ax.text(cx,8.49,'毛束偏转',ha='center',fontsize=10,color=ink)
    arrow(ax,(cx+.65,8.14),(cx+.10,8.23),color=ochre)
    ax.text(cx+.62,7.86,r'$K^+$',fontsize=12,color=ochre)
ax.text(2.7,6.1,'受体电位变化',ha='center',fontsize=11,color=blue)
ax.text(2.7,5.57,'内毛细胞',ha='center',fontsize=14,color=blue)
ax.text(8.8,5.8,'受体\n电位变化',ha='center',fontsize=10,color=red,linespacing=1.8)
# Ribbon & vesicles inside IHC, Ca entry across basolateral membrane
ax.add_patch(Polygon([[2.35,3.65],[2.55,4.24],[2.76,3.65]],closed=True,color=blue,alpha=.75))
for x,y in [(2.26,3.7),(2.8,3.7),(2.3,4.05),(2.75,4.07)]:ax.add_patch(Ellipse((x,y),.1,.1,facecolor=ochre,edgecolor='none'))
arrow(ax,(4.15,3.93),(3.35,3.93),color=green);ax.text(4.26,4.37,r'$Ca^{2+}$进入'+'\nCaV1.3通道',ha='center',fontsize=10,color=green,linespacing=1.7)
leader(ax,(2.55,3.86),(.35,4.45),'带状突触',ha='left')
# Synaptic cleft & nerve terminal BELOW IHC
ax.add_patch(Ellipse((2.55,2.82),1.56,.43,facecolor='#f4e8d6',edgecolor=ochre,lw=1.1))
for xx in [2.26,2.5,2.75]:
    ax.add_patch(Ellipse((xx,3.18),.065,.065,color=ochre));arrow(ax,(xx,3.14),(xx,2.97),color=ochre,lw=.8)
ax.text(4.27,2.88,'谷氨酸释放',ha='center',fontsize=11,color=ochre)
ax.plot([2.55,2.55,1.85],[2.62,1.84,1.5],color=ochre,lw=4)
arrow(ax,(2.94,2.28),(2.25,1.47),color=ochre)
ax.text(3.48,1.68,'听神经：动作电位',ha='left',fontsize=11,color=ochre)
# OHC side-wall prestin symbols and movement
for yy in np.linspace(4.3,6.6,8):
    for xx in [8.3,9.3]:ax.plot([xx-.04,xx+.04],[yy-.035,yy+.035],color=red,lw=2)
leader(ax,(9.3,5.0),(10.1,5.0),'侧壁普雷斯汀',ha='left',color=red)
ax.annotate('',xy=(9.7,7.35),xytext=(9.7,3.65),arrowprops={'arrowstyle':'<->','color':red,'lw':1.4})
ax.text(10.18,6.6,'长度变化',ha='left',fontsize=11,color=red)
ax.text(8.8,2.98,'外毛细胞',ha='center',fontsize=14,color=red)
arrow(ax,(8.8,2.55),(8.8,1.8),color=red)
ax.text(8.8,1.42,'参与耳蜗机械反馈',ha='center',fontsize=12,color=red)
ax.text(6,.5,'功能示意 · 非按比例绘制 · 支持细胞、传出末梢及外毛细胞Ⅱ型传入联系未显示',ha='center',fontsize=10,color='#666')
save(fig,'03-hair-cell-functions')
(folder/'figure-verification.json').write_text(json.dumps({'greenwoodHzAtApex':float(freq[-1]),'greenwoodHzAtBase':float(freq[0]),'peakDistanceFromBase':positions,'monotonicDecreasing':bool(np.all(np.diff(freq)<0)),'coordinateEquivalenceMaxError':float(np.max(np.abs(freq-165.4*(10**(2.1*(1-d))-.88)))),'illustrativeEnvelope':'Independent peak normalization; envelopes are not data or model solutions.'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated three SVG/PNG scientific figures.')
