from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':14,'svg.fonttype':'none','axes.unicode_minus':False})
out=Path('public/figures/gene-therapy-for-hearing-loss');out.mkdir(parents=True,exist_ok=True)
blue='#245c88';green='#287566';gray='#445363'
def save(fig,name):
 fig.savefig(out/(name+'.svg'),bbox_inches='tight',facecolor='white');fig.savefig(out/(name+'.png'),dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
 svg=out/(name+'.svg');svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
def box(ax,x,y,w,h,text,color=blue):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.015,rounding_size=0.02',edgecolor=color,facecolor='#f4f8fb',linewidth=1.5));ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=gray,linespacing=1.6)
def arrow(ax,a,b):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=gray,lw=1.6))
f,ax=plt.subplots(figsize=(11,6));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off');ax.set_title('双载体 OTOF：共同递送只是第一步',loc='left',fontsize=20,pad=20)
box(ax,.03,.68,.25,.17,'载体 A\n一部分表达材料');box(ax,.03,.34,.25,.17,'载体 B\n另一部分表达材料');box(ax,.39,.48,.26,.22,'同一内毛细胞\n完整表达的重建');arrow(ax,(.29,.75),(.38,.63));arrow(ax,(.29,.42),(.38,.54));box(ax,.75,.48,.22,.22,'耳畸蛋白\n与突触传递',green);arrow(ax,(.66,.59),(.74,.59));ax.text(.5,.15,'仍需分别检验：表达与定位 → 神经响应 → 行为及言语功能',ha='center',fontsize=15,color=gray);ax.text(.5,.04,'概念示意；无剂量、比例和解剖尺度，不保证每一步成功。',ha='center',fontsize=11,color=gray);save(f,'delivery')
f,ax=plt.subplots(figsize=(9,8));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1));ax.set_title('恢复发生在哪一个层级？',loc='left',fontsize=20,pad=16)
items=[('分子与细胞','蛋白表达、定位、转导或胞吐'),('神经响应','ABR 阈值与波形'),('行为敏感性','频率特异阈值与纯音平均值'),('言语与双耳功能','识别、噪声聆听、声源定位'),('长期生活与发展','语言发展、参与及生活功能')]
for i,(a,b) in enumerate(items):
 y=.82-i*.18;box(ax,.08,y,.84,.13,a+'\n'+b,blue if i<3 else green)
 if i<4:arrow(ax,(.5,y-.005),(.5,y-.045))
ax.text(.5,.015,'各层需要自己的测量；连线不是疗效必然传递的承诺。',ha='center',fontsize=12,color=gray);save(f,'outcomes')
f,ax=plt.subplots(figsize=(9,5.6));freq=['0.5','1','2','4'];a=[100,100,95,95];b=[60,55,45,40];ax.plot(freq,a,'o--',label='教学基线：平均 97.5 dB HL',color=gray,markersize=8);ax.plot(freq,b,'s-',label='教学随访：平均 50 dB HL',color=green,markersize=8);ax.set_ylim(115,0);ax.set_xlabel('频率（kHz）');ax.set_ylabel('行为听阈（dB HL）');ax.grid(alpha=.2);ax.set_title('假设数据：平均阈值降低 47.5 dB',loc='left',fontsize=19,pad=15);ax.legend(loc='upper right',fontsize=12);f.text(.5,.005,'等权四频平均；无受试者数据；阈值变化不等于恢复百分比。',ha='center',fontsize=11,color=gray);f.tight_layout(rect=(0,.035,1,1));save(f,'threshold-example')
print('Generated 3 SVG + 3 PNG figures')
