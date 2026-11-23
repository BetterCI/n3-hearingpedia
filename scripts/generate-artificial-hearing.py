"""Original conceptual diagrams and an explicitly hypothetical psychometric example."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':15,'svg.fonttype':'none','axes.unicode_minus':False})
OUT=Path('public/figures/artificial-hearing'); OUT.mkdir(parents=True,exist_ok=True)
BLUE='#245c88'; GREEN='#287566'; ORANGE='#b56528'; INK='#334859'; GRAY='#627481'
def save(fig,name):
 fig.savefig(OUT/(name+'.svg'),facecolor='white',bbox_inches='tight')
 fig.savefig(OUT/(name+'.png'),facecolor='white',dpi=140,bbox_inches='tight')
 plt.close(fig)
 svg=OUT/(name+'.svg')
 svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def box(ax,x,y,w,h,label,color=BLUE,size=15):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.005,rounding_size=0.015',fc='#f5f8fa',ec=color,lw=1.6))
 ax.text(x+w/2,y+h/2,label,ha='center',va='center',color=INK,fontsize=size,linespacing=1.7)
def arrow(ax,a,b,color=GRAY):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':color,'lw':1.6})

f,ax=plt.subplots(figsize=(12,7.5));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.set_title('人工听觉：逐步扩展的讨论范围',loc='left',fontsize=22,pad=22)
for x,t in [(.15,'范围'),(.49,'人工介入'),(.82,'功能主体与结果')]:ax.text(x,.93,t,ha='center',color=GRAY,fontsize=15)
rows=[('（a）植入假体','机械或神经接口','人：由假体支持的听觉'),('（b）装置助听','加入体外信号处理与传递','人：利用残余生物听觉'),('（c）生物修复','加入分子与细胞干预','人：恢复后的生物听觉'),('（d）机器听觉','加入声音计算与任务模型','机器：指定声音任务')]
for i,(a,b,c) in enumerate(rows):
 y=.72-i*.20;col=GREEN if i==2 else ORANGE if i==3 else BLUE
 box(ax,.02,y,.25,.14,a,col);box(ax,.33,y,.32,.14,b,col,size=14);box(ax,.71,y,.28,.14,c,col,size=14)
 arrow(ax,(.28,y+.07),(.32,y+.07));arrow(ax,(.66,y+.07),(.70,y+.07))
ax.text(.5,.025,'本文编辑框架；行序表示范围扩大，不表示疗效、成熟度或时间顺序。',ha='center',fontsize=12,color=GRAY)
save(f,'scope')

f,ax=plt.subplots(figsize=(13,7.4));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.set_title('同一声音，可以从不同接口进入系统',loc='left',fontsize=22,pad=22)
labels=['声学与\n机械传导','耳蜗\n机械分析','毛细胞\n机械电转导','内毛细胞\n突触传递','听神经','耳蜗核\n与后续中枢']
xs=np.linspace(.005,.845,6)
for i,(x,label) in enumerate(zip(xs,labels)):
 box(ax,x,.72,.15,.18,label,size=15)
 if i<5:arrow(ax,(x+.154,.81),(xs[i+1]-.006,.81))
box(ax,.005,.43,.21,.15,'助听器／机械装置\n调整声或振动输入',BLUE,14);arrow(ax,(.08,.585),(.08,.71),BLUE)
box(ax,.365,.43,.24,.15,'OTOF 基因补充\n修复突触传递',GREEN,14);arrow(ax,(.57,.585),(.584,.71),GREEN)
box(ax,.64,.22,.16,.15,'人工耳蜗\n提供电输入',BLUE,14);arrow(ax,(.72,.375),(.752,.71),BLUE)
box(ax,.815,.43,.18,.15,'脑干植入\n耳蜗核接口',BLUE,14);arrow(ax,(.92,.585),(.92,.71),BLUE)
ax.plot([.02,.98],[.17,.17],color='#c5d0d7',linestyle='--',lw=1)
ax.text(.02,.10,'机器支路',fontsize=14,color=ORANGE,va='center')
box(ax,.18,.045,.19,.11,'麦克风',ORANGE,14);box(ax,.44,.045,.24,.11,'计算表征与模型',ORANGE,14);box(ax,.75,.045,.24,.11,'检测／识别／定位',ORANGE,14)
arrow(ax,(.38,.10),(.43,.10),ORANGE);arrow(ax,(.69,.10),(.74,.10),ORANGE)
f.text(.5,.005,'功能示意：省略反馈回路与机械耦合细节；OTOF 只代表一种生物修复靶点。',ha='center',fontsize=12,color=GRAY)
save(f,'interfaces')

x=np.linspace(-12,12,481);k=.5;theta_a=-2;theta_b=2
def p(x,t):return 100/(1+np.exp(-k*(x-t)))
f,ax=plt.subplots(figsize=(10,6.2))
ax.plot(x,p(x,theta_a),color=BLUE,lw=2.6,label='假想 A：SRT = −2 dB')
ax.plot(x,p(x,theta_b),color=ORANGE,lw=2.6,ls='--',label='假想 B：SRT = +2 dB')
ax.axhline(50,color=GRAY,ls=':',lw=1.2)
for t,c in [(theta_a,BLUE),(theta_b,ORANGE)]:ax.vlines(t,0,50,color=c,ls=':',lw=1.3)
ax.plot(0,p(0,theta_a),'o',color=BLUE,ms=9);ax.plot(0,p(0,theta_b),'s',color=ORANGE,ms=8)
ax.annotate('73.1%',(0,p(0,theta_a)),xytext=(-4.5,84),color=BLUE,arrowprops={'arrowstyle':'-','color':BLUE})
ax.annotate('26.9%',(0,p(0,theta_b)),xytext=(2.7,16),color=ORANGE,arrowprops={'arrowstyle':'-','color':ORANGE})
ax.set(xlim=(-12,12),ylim=(0,100),xlabel='信噪比（dB）',ylabel='预期关键词正确率（%）')
ax.set_title('教学计算：听阈之外，还要比较噪声中的识别',loc='left',fontsize=19,pad=18)
ax.grid(alpha=.16);ax.legend(loc='upper left',fontsize=13)
f.text(.5,.01,'假设参数 k = 0.5／dB；无临床数据；SRT 相差 4 dB 不能换算为康复百分比。',ha='center',fontsize=12,color=GRAY)
f.tight_layout(rect=(0,.05,1,1));save(f,'outcome-example')
assert abs(p(0,theta_a)-73.10585786)<1e-6
assert abs(p(0,theta_b)-26.89414214)<1e-6
(OUT/'parameters.json').write_text(json.dumps({'data_type':'hypothetical teaching model, no participant data','model':'100/(1+exp(-k*(snr-theta)))','k_per_dB':k,'theta_A_dB':theta_a,'theta_B_dB':theta_b,'P_A_at_0_percent':p(0,theta_a),'P_B_at_0_percent':p(0,theta_b),'SRT_difference_dB':theta_b-theta_a},indent=2)+'\n',encoding='utf8')
print('Generated 3 SVG + 3 PNG; teaching values verified.')
