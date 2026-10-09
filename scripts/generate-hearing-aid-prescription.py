"""Original scientific teaching figures, fixed inputs and numerical verification.
No NAL-NL2, NAL-NL3 or DSL target generation; no participant data.
"""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.ticker import NullFormatter

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/figures/hearing-aid-prescription'
RECORD=ROOT/'docs/research/hearing-aid-prescription-2026-10-09'
OUT.mkdir(parents=True,exist_ok=True); RECORD.mkdir(parents=True,exist_ok=True)
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'font.size':25,'axes.unicode_minus':False,
 'svg.fonttype':'path','svg.hashsalt':'hearing-aid-prescription-2026-10-09',
 'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
BLUE='#24678d'; ORANGE='#b3652d'; GREEN='#39775a'; GRAY='#65747d'; INK='#263944'; PALE='#eaf2f6'
manifest=[]
def save(fig,name,description,parameters):
 for ext in ('svg','png'):
  path=OUT/(name+'.'+ext)
  fig.savefig(path,dpi=90,metadata={'Date':None} if ext=='svg' else None)
  if ext=='svg': path.write_text('\n'.join(x.rstrip() for x in path.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8')
 svg=(OUT/(name+'.svg')).read_text(encoding='utf8')
 manifest.append({'name':name,'files':[name+'.svg',name+'.png'],
  'svg_viewbox':[float(x) for x in re.search(r'viewBox="([^"]+)"',svg).group(1).split()],
  'description':description,'parameters':parameters,'empirical_data':False,
  'generator':'scripts/generate-hearing-aid-prescription.py','copyright':'原创教学图，未转载文献图片',
  'attribution':'n³ Hearingpedia；AI 辅助编写与绘图',
  'usage':'用于本站词条展示和教学计算复现；对外开放许可证依项目约定，尚待维护者确定'})
 plt.close(fig)
def canvas(height=840):
 fig=plt.figure(figsize=(1200/72,height/72)); ax=fig.add_axes([.02,.025,.96,.95])
 ax.set_xlim(0,12); ax.set_ylim(0,height/100); ax.axis('off'); return fig,ax
def box(ax,x,y,text,w=3.35,h=1.1,color=BLUE,fill='white',size=25):
 ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.06',lw=2,facecolor=fill,edgecolor=color))
 ax.text(x,y,text,ha='center',va='center',fontsize=size,color=INK)
def arrow(ax,a,b,color=BLUE,dashed=False):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=24,linewidth=2.4,
  linestyle='--' if dashed else '-',color=color))

fig,ax=canvas()
ax.text(.2,7.8,'处方目标、声学验证与功能评价',fontsize=31,weight='bold',color=INK)
box(ax,2,6.4,'输入资料\n听阈、个体、声学条件',h=1.3,fill=PALE)
box(ax,6,6.4,'处方算法\n具体版本与选项',h=1.3,fill=PALE)
box(ax,10,6.4,'多维目标\n频率 × 输入声级',h=1.3,fill=PALE)
arrow(ax,(3.75,6.4),(4.25,6.4)); arrow(ax,(7.75,6.4),(8.25,6.4))
box(ax,10,3.8,'编程与声学耦合\n装置、耳塞、耳道',h=1.3)
box(ax,6,3.8,'输出验证\n耳内实测／相容转换',h=1.3)
box(ax,2,3.8,'功能评价\n言语、舒适度、使用',h=1.3,color=GREEN)
arrow(ax,(10,5.65),(10,4.55)); arrow(ax,(8.25,3.8),(7.75,3.8)); arrow(ax,(4.25,3.8),(3.75,3.8),color=GREEN)
arrow(ax,(6,3.05),(6,1.65),dashed=True)
ax.text(6,1.15,'检查测量、输入资料及设置，记录调整前后曲线',ha='center',fontsize=27,color=INK)
ax.text(6,.35,'接近目标 ≠ 自动得到相同的使用获益',ha='center',fontsize=26,color=GRAY)
save(fig,'01-targets-and-verification','目标生成、实际输出与功能结局分层；框图不编码疗效。',{'quantitative_data':None})

freq=np.array([250,500,1000,2000,4000,6000]); hl=np.array([25,30,40,50,60,60.])
bias=np.array([-17,-8,1,-1,-2,-2]); critical=float(sum(hl[1:4])); x=.05*critical
raw=x+.31*hl+bias; gain=np.maximum(raw,0); half=hl/2
assert critical==120 and x==6
assert np.allclose(raw,[-3.25,7.3,19.4,20.5,22.6,22.6])
fig=plt.figure(figsize=(1200/72,840/72)); ax=fig.add_axes([.13,.19,.82,.65])
ax.semilogx(freq,gain,'o-',color=BLUE,lw=3.5,ms=11,label='NALR 实现：控制点计算')
ax.semilogx(freq,half,'s--',color=ORANGE,lw=3,ms=10,label='逐点半增益：对照')
ax.set_xticks(freq,[str(f) for f in freq]); ax.set_xlim(220,6900); ax.set_ylim(-5,40)
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlabel('频率（Hz）',labelpad=14); ax.set_ylabel('增益（dB）',labelpad=14)
ax.grid(alpha=.2); ax.legend(frameon=False,loc='upper left',fontsize=24)
for f,g in zip(freq,gain): ax.annotate(f'{g:.1f}',(f,g),xytext=(0,-29),textcoords='offset points',ha='center',fontsize=23,color=BLUE)
fig.text(.13,.92,'线性处方示例：频率修正与跨频率整体项',fontsize=30,weight='bold',color=INK)
fig.text(.13,.055,'教学听阈；连线仅辅助阅读，未计算实际滤波器响应',fontsize=24,color=GRAY)
save(fig,'02-linear-nalr-example','所核对Clarity NALR代码在总听阈≤180分支的六控制点计算，不是非线性NAL目标。',
 {'frequencies_hz':freq.tolist(),'thresholds_db_hl':hl.tolist(),'bias_db':bias.tolist(),'critical_sum':critical,
  'x_db':x,'raw_gain_db':raw.tolist(),'gain_db':gain.tolist(),'half_gain_db':half.tolist(),
  'implementation_commit':'dcceaabab7786a94ba5ba8bef4177040f4521ccc','fir_simulated':False})

def output(i):
 i=np.asarray(i); return np.select([i<35,i<50,i<90],[50+1.5*(i-35),i+15,65+.5*(i-50)],default=85.)
inputs=np.linspace(20,100,401); outputs=output(inputs)
assert np.allclose(output([35,50,90]),[50,65,85])
assert np.all(np.diff(outputs)>=0)
fig=plt.figure(figsize=(1200/72,1000/72)); a=fig.add_axes([.13,.55,.82,.32]); b=fig.add_axes([.13,.13,.82,.27])
a.plot(inputs,outputs,lw=3.7,color=BLUE); a.plot(inputs,inputs,'--',lw=2,color=GRAY,label='零增益参考')
regions=[(20,35,'扩展',ORANGE),(35,50,'线性',GREEN),(50,90,'压缩',BLUE),(90,100,'限制',GRAY)]
for lo,hi,label,color in regions:
 a.axvspan(lo,hi,color=color,alpha=.08); a.text((lo+hi)/2,99,label,ha='center',fontsize=23,color=color)
for boundary in [35,50,90]:
 a.axvline(boundary,color=GRAY,ls=':',lw=1.5); b.axvline(boundary,color=GRAY,ls=':',lw=1.5)
a.set(xlim=(20,100),ylim=(20,107),ylabel='输出（dB SPL）'); a.legend(loc='lower right',frameon=False,fontsize=22)
a.set_title('（a）稳态输入输出：分段连续',loc='left',fontsize=27,pad=17)
b.plot(inputs,outputs-inputs,lw=3.7,color=GREEN); b.axhline(0,color=GRAY,ls='--',lw=1.5)
b.set(xlim=(20,100),ylim=(-20,25),xlabel='输入（dB SPL）',ylabel='增益（dB）')
b.set_title('（b）增益 = 输出 − 输入',loc='left',fontsize=27,pad=15)
for axis in [a,b]: axis.grid(alpha=.16)
fig.text(.13,.94,'多阶段函数的教学关系',fontsize=30,weight='bold',color=INK)
fig.text(.13,.035,'固定输入／输出坐标；未调用 DSL 算法，未模拟瞬态',fontsize=24,color=GRAY)
save(fig,'03-multistage-input-output','四阶段斜率与增益的独立教学模型，连续边界通过核验。',
 {'breakpoints_input_db_spl':[35,50,90],'breakpoints_output_db_spl':[50,65,85],
 'slopes':[1.5,1,.5,0],'timing_simulated':False,'dsl_computed':False})

fig,ax=canvas()
ax.text(.2,7.8,'RECD：同一声源的耦合腔与真耳转换',fontsize=30,weight='bold',color=INK)
box(ax,6,6.2,'耦合腔：80 dB SPL\n固定 1 kHz 声源',w=5,h=1.3,fill=PALE)
arrow(ax,(4.8,5.48),(3,4.6)); arrow(ax,(7.2,5.48),(9,4.6),color=ORANGE)
ax.text(2.2,5.15,'RECD = +5 dB',ha='center',fontsize=27,color=BLUE)
ax.text(9.8,5.15,'RECD = +12 dB',ha='center',fontsize=27,color=ORANGE)
box(ax,3,3.5,'假设耳道 A\n耳内：85 dB SPL',w=4.4,h=1.55)
box(ax,9,3.5,'假设耳道 B\n耳内：92 dB SPL',w=4.4,h=1.55,color=ORANGE)
ax.text(6,1.8,'同一频率、同一声源、相容耦合条件',ha='center',fontsize=27,color=INK)
ax.text(6,.7,'教学数值；耳道 A、B 不代表成人／儿童常模',ha='center',fontsize=25,color=GRAY)
assert 80+5==85 and 80+12==92
save(fig,'04-recd-coordinate-example','匹配声源与耦合条件下的单频声压转换。',{'frequency_hz':1000,'coupler_db_spl':80,'recd_db':[5,12],'ear_db_spl':[85,92],'normative_data':False})

f=np.array([500,1000,2000,4000]); levels=[50,65,80]
targets=np.array([[65,70,75,70],[75,80,85,80],[83,88,93,88.]])
first=np.array([[65,69,72,63],[75,79,81,72],[83,87,89,80.]])
second=targets+np.array([0,0,-1,-1])
errors=first-targets; errors2=second-targets
rms=np.sqrt(np.mean(errors**2,axis=1)); rms2=np.sqrt(np.mean(errors2**2,axis=1))
assert np.isclose(rms[1],4.5) and np.allclose(rms2,np.sqrt(.5))
fig=plt.figure(figsize=(1200/72,1000/72)); a=fig.add_axes([.13,.56,.82,.31]); b=fig.add_axes([.13,.15,.82,.25])
a.semilogx(f,targets[1],'s--',color=GRAY,lw=3,ms=10,label='目标')
a.semilogx(f,first[1],'o-',color=ORANGE,lw=3,ms=10,label='第一次构造输出')
a.semilogx(f,second[1],'^-',color=BLUE,lw=3,ms=10,label='第二次构造输出')
a.set_xticks(f,['500','1000','2000','4000']); a.set_ylim(68,93); a.set_ylabel('耳内输出（dB SPL）')
a.set_title('（a）65 dB SPL 输入：目标与两次输出',loc='left',fontsize=27,pad=18)
a.legend(frameon=False,fontsize=21,loc='upper left',ncol=2); a.grid(alpha=.2)
for i,(level,color,marker,style,size) in enumerate(zip(levels,[BLUE,ORANGE,GREEN],['o','s','^'],['-','--',':'],[9,14,8])):
 b.semilogx(f,errors[i],marker+style,color=color,lw=2.8,ms=size,
  markerfacecolor='white' if i==1 else color,label=f'{level} dB SPL 输入')
b.axhline(0,color=GRAY,lw=1.5); b.set_xticks(f,['500','1000','2000','4000'])
b.set(xlabel='频率（Hz）',ylabel='目标偏差（dB）',ylim=(-10,3)); b.grid(alpha=.2)
b.set_title('（b）第一次输出：负值表示低于目标',loc='left',fontsize=27,pad=15)
b.legend(frameon=False,fontsize=21,loc='lower left',ncol=3)
for axis in [a,b]: axis.xaxis.set_minor_formatter(NullFormatter())
fig.text(.13,.94,'目标误差：保留声级和频率结构',fontsize=30,weight='bold',color=INK)
fig.text(.13,.045,'目标与输出均为教学设定；RMS 改善不直接代表言语获益',fontsize=24,color=GRAY)
save(fig,'05-target-error-example','三声级输出误差，正文65dB例子和图使用相同数值。',
 {'frequencies_hz':f.tolist(),'overall_input_levels_db_spl':levels,'targets_db_spl':targets.tolist(),
 'first_outputs_db_spl':first.tolist(),'second_outputs_db_spl':second.tolist(),'first_errors_db':errors.tolist(),
 'first_rms_db':rms.tolist(),'second_rms_db':rms2.tolist(),'apparent_1khz_ratios':[15/10,15/8,30/18],
 'identical_base_spectrum':True,'normative_or_participant_data':False})
record={'date':'2026-10-09','figures':manifest,'checks':{'nalr_control_points':True,'piecewise_continuity':True,
 'piecewise_monotonicity':True,'recd_addition':True,'rms_and_apparent_ratios':True}}
(RECORD/'figure-verification.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figures':len(manifest),'nalr_gain_db':gain.tolist(),'rms_db':rms.tolist(),'after_rms_db':rms2.tolist()},ensure_ascii=False))
