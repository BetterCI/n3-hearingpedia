"""Original teaching diagrams and calculations, not clinical data or device settings."""
from pathlib import Path
import json,re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch,Circle
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/speech-audiometry';OUT.mkdir(parents=True,exist_ok=True)
RECORD=ROOT/'docs/research/speech-audiometry-2026-10-09';RECORD.mkdir(parents=True,exist_ok=True)
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':25,'axes.unicode_minus':False,'svg.fonttype':'path','svg.hashsalt':'speech-audiometry-2026-10-09','figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
BLUE='#24678d';GREEN='#39775a';ORANGE='#b3652d';INK='#263944';GRAY='#65747d';PALE='#eaf2f6'
manifest=[]
def canvas(h):
 fig=plt.figure(figsize=(1200/72,h/72));ax=fig.add_axes([.025,.025,.95,.95]);ax.set_xlim(0,12);ax.set_ylim(0,h/100);ax.axis('off');return fig,ax

def box(ax,x,y,text,w=4.5,h=1.05,color=BLUE,size=28):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=.05',lw=2,facecolor=PALE,edgecolor=color));ax.text(x,y,text,ha='center',va='center',fontsize=size,color=INK)

def arrow(ax,a,b,c=BLUE):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=25,lw=2.5,color=c))
def save(fig,name,desc,params):
 for ext in ('svg','png'):
  path=OUT/(name+'.'+ext);fig.savefig(path,dpi=90,metadata={'Date':None} if ext=='svg' else None)
  if ext=='svg':path.write_text('\n'.join(x.rstrip() for x in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
 svg=(OUT/(name+'.svg')).read_text(encoding='utf8');manifest.append({'name':name,'files':[name+'.svg',name+'.png'],'svg_viewbox':[float(x) for x in re.search(r'viewBox="([^"]+)"',svg).group(1).split()],'description':desc,'parameters':params,'empirical_data':False,'generator':'scripts/generate-speech-audiometry.py','attribution':'n³ Hearingpedia；AI 辅助编写与绘图','copyright':'原创教学图；未转载论文图片或受试者数据','usage':'本站展示与教学复现；对外开放许可证尚待维护者确定'});plt.close(fig)
fig,ax=canvas(850)
ax.text(.2,7.9,'言语测听：任务不同，数字含义不同',fontsize=34,weight='bold',color=INK)
rows=[('检测：有没有语音','检测阈 SDT / SAT\n声级（须注明参考）',BLUE),('安静识别：达到规定比例','接收阈 SRT\n声级（须注明参考）',GREEN),('固定条件：认对了多少','正确数 / 总数 → 百分比\n须注明声级与评分单位',BLUE),('噪声识别：在背景中表现如何','固定条件正确率 / 所需 SNR\nSNR loss 还需匹配参考',ORANGE)]
for y,(l,r,c) in zip([6.45,4.8,3.15,1.5],rows):
 box(ax,3,y,l,w=5.1,color=c);arrow(ax,(5.65,y),(6.3,y),c);ax.text(9.15,y,r,ha='center',va='center',fontsize=28,color=INK)
ax.text(6,.25,'材料、呈现链、反应方式与耳别，须和结果一起记录',ha='center',fontsize=25,color=GRAY)
save(fig,'01-tasks','四类任务的输出；非严重度分级。',{'four_tasks':['detection','quiet_threshold','fixed_level_recognition','speech_in_noise'],'data':None})

fig,ax=canvas(800)
ax.text(.2,7.45,'非测试耳掩蔽 ≠ 竞争背景声',fontsize=34,weight='bold',color=INK)
ax.text(.3,6.65,'（a）耳机：控制哪只耳参与',fontsize=30,color=INK)
box(ax,2.1,5.55,'目标语音',w=2.8,h=.8);box(ax,9.9,5.55,'掩蔽声',w=2.8,h=.8,color=ORANGE)
box(ax,4.7,4.5,'测试耳',w=2.4,h=.9);box(ax,7.3,4.5,'非测试耳',w=2.4,h=.9,color=ORANGE)
arrow(ax,(3.5,5.3),(4.5,5.0));arrow(ax,(8.5,5.3),(7.5,5.0),ORANGE)
ax.text(6,3.6,'目标：限制对侧听觉参与，取得可解释的耳别结果',ha='center',fontsize=26,color=GRAY)
ax.plot([.3,11.7],[3.2,3.2],lw=1,color='#c9d3d8')
ax.text(.3,2.75,'（b）声场：构造噪声中的识别任务',fontsize=30,color=INK)
box(ax,2,1.65,'目标语音源',w=3,h=.8);box(ax,10,1.65,'竞争声源',w=3,h=.8,color=ORANGE)
box(ax,6,1.2,'双耳开放\n或指定设备配置',w=3.2,h=1.05,size=26,color=GREEN)
arrow(ax,(3.55,1.65),(4.35,1.35));arrow(ax,(8.45,1.65),(7.65,1.35),ORANGE)
ax.text(6,.25,'图形位置不规定测试方位、距离或掩蔽声级',ha='center',fontsize=25,color=GRAY)
save(fig,'02-noise-roles','两种噪声功能；箭头只表示指定呈现路径，省略跨耳传递与声场传播。',{'geometry':'schematic, not to scale','masking_levels':None,'data':None})

x=np.linspace(-20,30,1001); b=.2; caps=[.98,.70];ms=[float(np.log(2*u-1)/b) for u in caps]
def logistic(x,u,b,m):return u/(1+np.exp(-b*(x-m)))
fig=plt.figure(figsize=(1200/72,950/72));fig.text(.065,.955,'同一阈值可以对应不同上限；不同横轴要分别解释',fontsize=30,weight='bold',color=INK)
ax=fig.add_axes([.13,.57,.80,.27]);ax.set_title('（a）安静任务：两条曲线的50%点相同',loc='left',fontsize=27,pad=16)
for u,m,c,ls in zip(caps,ms,[BLUE,ORANGE],['-','--']):
 assert np.isclose(logistic(0,u,b,m),.5);ax.plot(x,100*logistic(x,u,b,m),color=c,ls=ls,lw=3,label=f'模型上限 {u*100:.0f}%')
ax.axhline(50,c=GRAY,ls=':',lw=1.8);ax.axvline(0,c=GRAY,ls=':',lw=1.8);ax.scatter([0],[50],c=INK,s=70,zorder=5);ax.set_xlim(-20,30);ax.set_ylim(0,105);ax.set_ylabel('正确率（%）');ax.set_xlabel('相对参考的言语声级变化（dB）');ax.legend(loc='lower right',fontsize=24);ax.set_yticks([0,50,100]);ax.grid(alpha=.12)
ax=fig.add_axes([.13,.15,.80,.27]);ax.set_title('（b）噪声任务：50%点相差4 dB SNR',loc='left',fontsize=27,pad=16)
nx=np.linspace(-15,15,601)
for m,c,ls in [(-3,BLUE,'-'),(1,ORANGE,'--')]:
 ax.plot(nx,100*logistic(nx,1,.45,m),c=c,ls=ls,lw=3,label=f'教学阈值 {m:+d} dB SNR');ax.vlines(m,0,50,color=c,ls=':',lw=1.8);ax.scatter([m],[50],s=60,c=c,zorder=5)
ax.axhline(50,c=GRAY,ls=':',lw=1.8);ax.annotate('',xy=(1,64),xytext=(-3,64),arrowprops={'arrowstyle':'<->','color':INK,'lw':2});ax.text(-1,71,'4 dB',ha='center',fontsize=24);ax.set_xlim(-15,15);ax.set_ylim(0,105);ax.set_ylabel('正确率（%）');ax.set_xlabel('信噪比（dB SNR）');ax.legend(loc='lower right',fontsize=24);ax.set_yticks([0,50,100]);ax.grid(alpha=.12)
fig.text(.5,.03,'逻辑函数教学计算；非临床常模、疾病曲线或设备效果',ha='center',fontsize=25,color=GRAY)
save(fig,'03-functions','逻辑函数教学计算；无受试者数据。',{'formula':'p=u/(1+exp(-b*(x-m)))','quiet':{'caps':caps,'b_per_dB':b,'m_dB':ms,'threshold_at_50_percent_dB':0},'noise':{'cap':1,'b_per_dB':.45,'thresholds_dB_SNR':[-3,1],'difference_dB':4},'gamma':0})

z=1.96;intervals=[]
def wilson(k,n):
 p=k/n;den=1+z*z/n;center=(p+z*z/(2*n))/den;half=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;return float(center-half),float(center+half)
fig=plt.figure(figsize=(1200/72,780/72));fig.text(.07,.925,'同样80%正确率：分母影响估计精度',fontsize=33,weight='bold',color=INK)
ax=fig.add_axes([.18,.29,.75,.48])
for y,n,c in [(3,25,ORANGE),(2,50,BLUE),(1,100,GREEN)]:
 k=int(n*.8);lo,hi=wilson(k,n);assert lo<.8<hi
 ax.hlines(y,lo*100,hi*100,color=c,lw=4);ax.vlines([lo*100,hi*100],y-.11,y+.11,color=c,lw=2.5);ax.plot([80],[y],marker='o',ms=10,c=c)
 ax.text((lo+hi)*50,y+.27,f'{lo*100:.1f}% — {hi*100:.1f}%',ha='center',fontsize=25,color=INK)
 intervals.append({'correct':k,'N':n,'p':.8,'wilson_95_percent':[lo*100,hi*100]})
ax.set_yticks([3,2,1],['20 / 25','40 / 50','80 / 100']);ax.set_ylim(.55,3.6);ax.set_xlim(50,100);ax.set_xlabel('正确概率估计（%）',labelpad=15);ax.set_ylabel('正确数 / 总数');ax.set_xticks([50,60,70,80,90,100]);ax.grid(axis='x',alpha=.16)
fig.text(.5,.12,'横线：单个成绩的双侧95% Wilson区间',ha='center',fontsize=28,color=INK)
fig.text(.5,.055,'假设项目独立且同概率；非实测误差线，也非两次差异判据',ha='center',fontsize=25,color=GRAY)
save(fig,'04-uncertainty','二项模型下的Wilson95%区间；非患者数据、非差异检验。',{'z':z,'assumptions':['independent','common correct probability'],'intervals':intervals,'source':'https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm'})
(OUT/'parameters.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(RECORD/'figure-verification.json').write_text(json.dumps({'date':'2026-10-09','figures':manifest,'automated_checks':['SVG viewboxes match HTML dimensions','two quiet functions p(0)=0.5','noise threshold difference=4 dB','Wilson limits contain observed 80%'], 'visual_review':'pending','clinical_review':'pending'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Generated',len(manifest),'SVG + PNG figure pairs')
