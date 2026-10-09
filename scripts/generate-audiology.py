"""Original diagrams and hypothetical screening counts; no clinical observations.

Run from any directory with Python, numpy and matplotlib. SVG and PNG outputs
share a source. Assertions verify 2x2 totals and Bayes' formula independently.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/audiology';OUT.mkdir(parents=True,exist_ok=True)
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    font_manager.fontManager.addfont(str(font));family=font_manager.FontProperties(fname=str(font)).get_name()
else:family='Noto Sans CJK SC'
plt.rcParams.update({'font.family':family,'font.size':22,'svg.fonttype':'path','svg.hashsalt':'hearingpedia-audiology-20261009','axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
B,O,G='#1865a2','#b85a16','#526375';sizes={}

def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None,'Creator':'Hearingpedia original teaching figure'})
    p=OUT/(name+'.svg');p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
    fig.savefig(OUT/(name+'.png'),dpi=100)
    sizes[name]={'png_pixels':[round(v*100) for v in fig.get_size_inches()]}
    plt.close(fig)

def canvas(title,h=10):
    fig,ax=plt.subplots(figsize=(20,h));ax.set_axis_off();ax.set(xlim=(0,20),ylim=(0,h))
    fig.subplots_adjust(left=.02,right=.98,bottom=.025,top=.96)
    ax.text(10,h-.6,title,ha='center',fontsize=28,color=B)
    return fig,ax

def box(ax,x,y,w,h,title,detail,color=B):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12,rounding_size=.13',facecolor='#f4f7fa',edgecolor=color,lw=2))
    ax.text(x+w/2,y+h-.6,title,ha='center',va='center',fontsize=25,color=color)
    ax.text(x+w/2,y+h*.39,detail,ha='center',va='center',fontsize=21,linespacing=1.55)

def arrow(ax,a,b):
    ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':2.5,'color':G})

fig,ax=canvas('听力评估：连接不同层次，分别取得证据')
items=[('声学输入','输出、校准与传递\n声音是否符合条件？'),('听觉功能','检测与生理响应\n哪些功能得到评价？'),('任务表现','言语与感知任务\n在何种条件下完成？'),('日常参与','交流与活动目标\n实际困难是否改善？')]
for i,(t,d) in enumerate(items):
    x=.55+i*4.95;box(ax,x,4.2,4.1,3.7,t,d,B if i<2 else O)
    if i<3:arrow(ax,(x+4.3,6),(x+4.7,6))
ax.text(10,2.75,'贯穿各层次：检查条件 · 个人与家庭背景 · 语言 · 环境 · 目标',ha='center',fontsize=25)
ax.text(10,1.1,'箭头表示需要建立解释联系；各栏之间没有一对一的自动换算',ha='center',fontsize=21,color=G)
save(fig,'01-assessment-levels')

fig,ax=canvas('测量对象不同，解释范围也不同',h=12)
xs=[.3,4.2,11.4];widths=[3.7,6.9,8.3]
for x,w,t in zip(xs,widths,['方法','主要提供的信息','不能独立推导的结论']):
    ax.add_patch(FancyBboxPatch((x,9.8),w,1,boxstyle='square,pad=0',facecolor=B,edgecolor='white'))
    ax.text(x+w/2,10.3,t,ha='center',va='center',color='white',fontsize=24)
rows=[('纯音测听','规定条件下的检测敏感度','全部阈上能力与日常交流表现'),('言语测量','特定材料和背景中的任务表现','唯一病因或所有生活情境的成绩'),('声导抗／声反射','中耳传递与反射相关信息','仅凭一个曲线形状确定病因'),('耳声发射','耳蜗相关声学响应的记录','整条神经通路和言语功能正常'),('ABR／ASSR','刺激相关电活动与听阈估计','无需条件或校正的行为听力图')]
for i,row in enumerate(rows):
    y=8.25-i*1.55
    for x,w,t in zip(xs,widths,row):
        ax.add_patch(FancyBboxPatch((x,y),w,1.45,boxstyle='square,pad=0',facecolor='#eef4f8' if i%2==0 else '#f9fafb',edgecolor='white'))
        ax.text(x+w/2,y+.72,t,ha='center',va='center',fontsize=21,color=B if x==xs[0] else G)
ax.text(10,.6,'教学整理：不是疾病诊断表；用途随年龄、刺激与程序而改变',ha='center',fontsize=21,color=G)
save(fig,'02-test-questions')

N=10000;se=.9;sp=.95;records=[]
for p in [.01,.10]:
    positive=round(N*p);negative=N-positive
    tp=round(positive*se);fn=positive-tp;tn=round(negative*sp);fp=negative-tn
    ppv=tp/(tp+fp);npv=tn/(tn+fn)
    analytic=se*p/(se*p+(1-sp)*(1-p))
    assert tp+fn+fp+tn==N
    assert abs(tp/positive-se)<1e-12 and abs(tn/negative-sp)<1e-12
    assert abs(ppv-analytic)<1e-12
    records.append({'N':N,'prevalence':p,'sensitivity':se,'specificity':sp,'TP':tp,'FN':fn,'FP':fp,'TN':tn,'PPV':ppv,'NPV':npv,'analytic_error':abs(ppv-analytic)})
fig,axs=plt.subplots(1,2,figsize=(20,10));fig.subplots_adjust(left=.07,right=.96,top=.8,bottom=.22,wspace=.3)
x=np.arange(2);tp=[r['TP'] for r in records];fp=[r['FP'] for r in records]
axs[0].bar(x,tp,color=B,width=.55,label='真阳性 TP')
axs[0].bar(x,fp,bottom=tp,color='#f1d4bb',edgecolor=O,hatch='///',width=.55,label='假阳性 FP')
for i,r in enumerate(records):
    axs[0].text(i,r['TP']/2,str(r['TP']),ha='center',va='center',color='white',fontsize=22)
    axs[0].text(i,r['TP']+r['FP']/2,str(r['FP']),ha='center',va='center',fontsize=22)
    axs[0].text(i,r['TP']+r['FP']+40,f"总计 {r['TP']+r['FP']}",ha='center',fontsize=22)
axs[0].set(xticks=x,xticklabels=['目标状态 1%','目标状态 10%'],ylabel='筛查阳性人数 / 每 10000 人',ylim=(0,1650))
axs[0].legend(fontsize=19,loc='upper left');axs[0].set_title('（a）进入进一步评估的人数',fontsize=24,pad=20)
ppvs=[r['PPV']*100 for r in records]
axs[1].bar(x,ppvs,color=[B,O],width=.55)
for i,p in enumerate(ppvs):axs[1].text(i,p+3,f'{p:.2f}%',ha='center',fontsize=25)
axs[1].set(xticks=x,xticklabels=['目标状态 1%','目标状态 10%'],ylabel='阳性预测值 PPV / %',ylim=(0,100))
axs[1].set_title('（b）阳性者中目标状态的比例',fontsize=24,pad=20)
fig.text(.5,.93,'相同假设性能，不同人群构成，产生不同预测值',ha='center',fontsize=28)
fig.text(.5,.075,'教学设定：灵敏度 90%，特异度 95%；不是任何设备或项目的实测准确率',ha='center',fontsize=21,color=G)
save(fig,'03-screening-predictive-value')

fig,ax=canvas('助听服务：输出验证与功能评价共同支持调整',h=12)
box(ax,6.25,8.9,7.5,1.7,'个人及家庭的交流目标','',B)
box(ax,.9,4.9,8.2,2.8,'设备输出验证','真耳输出与适用处方目标\n设备在规定输入下怎样工作？',B)
box(ax,10.9,4.9,8.2,2.8,'实际功能评价','言语、自评、舒适度及使用情况\n目标活动中的困难是否改善？',O)
arrow(ax,(8,8.65),(5,8));arrow(ax,(12,8.65),(15,8))
box(ax,4.75,1.1,10.5,2.4,'共同解释并随访','调整设备、交流策略、环境与支持',G)
arrow(ax,(5,4.6),(7,3.8));arrow(ax,(15,4.6),(13,3.8))
ax.plot([15.5,19.65,19.65,15.5],[2.2,2.2,9.8,9.8],color=G,lw=2)
arrow(ax,(15.5,9.8),(14.05,9.8))
ax.text(19.5,10.55,'复查目标与条件',ha='right',fontsize=20,color=G)
save(fig,'04-verification-and-validation')

verification={'date':'2026-10-09','source':'scripts/generate-audiology.py','data_type':'Hypothetical counts and original conceptual diagrams; no participant or device measurements','figures':sizes,'screening_counts':records,'assertions':['2x2 counts sum to N','sensitivity and specificity match stipulated inputs','count PPV matches Bayes formula to 1e-12'],'font':family}
(OUT/'verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(verification,ensure_ascii=False))
