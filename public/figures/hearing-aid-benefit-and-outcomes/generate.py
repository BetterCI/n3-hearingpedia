"""Original synthetic teaching figures; no patient or product data."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

OUT=Path(__file__).resolve().parent
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():
    from matplotlib import font_manager
    font_manager.fontManager.addfont(str(font))
    plt.rcParams['font.family']=FontProperties(fname=str(font)).get_name()
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','axes.unicode_minus':False})
blue='#287994'; orange='#b26938'
def save(fig,name):
    fig.tight_layout()
    fig.savefig(OUT/f'{name}.png',dpi=170,facecolor='white')
    p=OUT/f'{name}.svg'
    fig.savefig(p,facecolor='white')
    p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

u=np.array([80,40]); a=np.array([90,70]); b=a-u
fig,ax=plt.subplots(figsize=(7.5,5.8))
x=np.arange(2)
ax.bar(x-.18,u,.34,label='未助听',color=orange)
ax.bar(x+.18,a,.34,label='助听',color=blue)
for xx,v in zip(x,u): ax.text(xx-.18,v+1,str(v),ha='center')
for xx,v in zip(x,a): ax.text(xx+.18,v+1,str(v),ha='center')
ax.set(xticks=x,xticklabels=['甲：获益10个百分点','乙：获益30个百分点'],ylabel='正确率 / %',ylim=(0,110),title='最终表现与获益的排序可以不同')
ax.legend(loc='upper center',ncol=2)
save(fig,'baseline')

n=np.array([25,50,100]); se=100*np.sqrt(.8*.2/n); mdc=1.96*np.sqrt(2)*4
fig,axs=plt.subplots(2,1,figsize=(7.5,8.2))
axs[0].plot(n,se,'o-',color=blue)
for xx,v in zip(n,se): axs[0].annotate(f'{v:.2f}',(xx,v),xytext=(0,10),textcoords='offset points',ha='center')
axs[0].set(xticks=n,xlabel='独立项目数 n',ylabel='标准误 / 百分点',ylim=(0,10),title='（a）独立二项模型：p = 0.8')
axs[1].barh(['测量标准误 SEM','可检测差值 MDC95'],[4,mdc],color=[blue,orange])
for yy,v in enumerate([4,mdc]): axs[1].text(v+.15,yy,f'{v:.2f}',va='center')
axs[1].set(xlim=(0,14),xlabel='抽象量表分数 / 分',title='（b）两次误差独立、等方差的教学近似')
save(fig,'uncertainty')

fig,ax=plt.subplots(figsize=(7.5,5.8))
ax.plot([0,1],[40,65],'o-',color=blue,label='干预组：+25分')
ax.plot([0,1],[40,50],'s--',color=orange,label='对照组：+10分')
ax.annotate('变化差：15分',xy=(1,57.5),xytext=(.35,56),arrowprops={'arrowstyle':'->','color':'#555'})
ax.set(xticks=[0,1],xticklabels=['基线','随访'],ylabel='抽象结果分数 / 分',ylim=(30,75),xlim=(-.1,1.2),title='前后变化不等于组间变化差')
ax.legend(loc='upper left')
save(fig,'comparator')
assert b.tolist()==[10,30]
assert np.allclose(se,[8,5.656854249492381,4])
assert abs(mdc-11.087434329005065)<1e-10
assert (65-40)-(50-40)==15
(OUT/'validation.json').write_text(json.dumps({'data_type':'synthetic teaching examples, not clinical thresholds','percentage_point_benefit':b.tolist(),'binomial_se_percentage_points':se.tolist(),'assumed_SEM':4,'MDC95':mdc,'difference_in_changes':15,'SRT_benefit_dB':5-2,'assertions':'passed'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
