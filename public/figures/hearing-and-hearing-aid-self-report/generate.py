"""Original teaching figures; synthetic values, no clinical observations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

OUT = Path(__file__).resolve().parent
font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': font.get_name(), 'font.size': 15,
                     'axes.unicode_minus': False, 'svg.fonttype': 'path'})
BLUE, ORANGE = '#286896', '#c56929'

def start(title):
    fig, axes = plt.subplots(2, 1, figsize=(10.5, 9), dpi=96)
    fig.suptitle(title, fontsize=21, y=.975)
    fig.subplots_adjust(left=.16, right=.95, bottom=.09, top=.90, hspace=.50)
    for ax in axes:
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(axis='y', alpha=.18)
        ax.set_axisbelow(True)
    return fig, axes

def save(fig, name):
    fig.savefig(OUT / (name+'.svg'))
    fig.savefig(OUT / (name+'.png'), dpi=96)
    p=OUT/(name+'.svg')
    p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

fig, axes = start('评分方向不同，改善的正负号也不同')
for ax, values, limit, label, title, note in zip(axes, [[60,35],[4,7]], [100,10],
    ['困难评分（0—100）','能力评分（0—10）'],
    ['（a）越低越好','（b）越高越好'], ['改善：60 − 35 = 25 个评分点','改善：7 − 4 = 3 分']):
    ax.bar([0,1], values, width=.45, color=[BLUE,ORANGE])
    ax.set(xlim=(-.65,2.3), ylim=(0,limit), ylabel=label)
    ax.set_xticks([0,1], ['前','后'])
    ax.set_title(title, loc='left')
    ax.text(1.45,limit*.65,note.replace('：','：\n'),fontsize=14)
    for x,y in enumerate(values): ax.text(x,y+limit*.03,str(y),ha='center')
save(fig,'01-score-direction')

x=np.array([10,20,30,40,50]); y=x+10
fig, (a,b)=start('相关为 1，不代表两次评分一致')
a.plot([0,65],[0,65],'--',color='#777777',label='两次相等')
a.scatter(x,y,s=75,color=BLUE,label='模拟评分')
a.set(xlim=(0,65),ylim=(0,65),xlabel='第一次评分',ylabel='第二次评分')
a.set_title('（a）所有对象均增加 10 分',loc='left'); a.legend(loc='upper left',fontsize=12)
b.scatter((x+y)/2,y-x,s=75,color=ORANGE)
b.axhline(0,color='#777777',linestyle='--');b.axhline(10,color=ORANGE,linewidth=1)
b.set(xlim=(0,65),ylim=(-5,20),xlabel='两次评分的均值',ylabel='第二次 − 第一次')
b.set_title('（b）差值图显示固定偏移',loc='left')
save(fig,'02-correlation-agreement')

scores=np.array([2.,6.]); weights=np.array([[.8,.2],[.2,.8]])
means=weights@scores
fig,(a,b)=start('场景内评分不变，总体平均仍可改变')
pos=np.arange(2)
a.bar(pos-.17,scores,.34,color=BLUE,label='阶段一')
a.bar(pos+.17,scores,.34,color=ORANGE,hatch='//',label='阶段二')
a.set_xticks(pos,['安静场景','嘈杂场景']);a.set(ylim=(0,8),ylabel='困难评分（0—10）')
a.set_title('（a）两阶段的场景内评分相同',loc='left');a.legend(fontsize=12)
b.bar(pos-.17,[means[0],4],.34,color=BLUE,label='阶段一')
b.bar(pos+.17,[means[1],4],.34,color=ORANGE,hatch='//',label='阶段二')
b.set_xticks(pos,['实际场景构成\n80/20 → 20/80','统一场景构成\n各占 50%'])
b.set(ylim=(0,8),ylabel='加权平均困难评分')
b.set_title('（b）平均值取决于场景权重',loc='left')
for xx,yy in [(-.17,2.8),(.17,5.2),(.83,4),(1.17,4)]: b.text(xx,yy+.15,f'{yy:g}',ha='center')
save(fig,'03-context-mixture')

assert 60-35==25 and 7-4==3
assert np.isclose(np.corrcoef(x,y)[0,1],1)
assert np.all(y-x==10) and np.allclose(means,[2.8,5.2])
assert np.isclose(np.array([.5,.5])@scores,4)
result={'data_type':'synthetic teaching examples, not clinical data',
        'score_changes':[25,3], 'correlation':float(np.corrcoef(x,y)[0,1]),
        'fixed_difference':10,'context_means':means.tolist(),
        'standardized_mean':4,'illustrative_mdc_sem3':float(1.96*np.sqrt(2)*3),
        'figure_pixels':[1008,864], 'assertions':'passed'}
(OUT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
