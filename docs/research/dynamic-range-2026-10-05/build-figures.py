"""Original qualitative illustrations for the local dynamic-range review."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent
font_path = 'C:/Windows/Fonts/msyh.ttc'
font_manager.fontManager.addfont(font_path)
plt.rcParams.update({
    'font.family': [font_manager.FontProperties(fname=font_path).get_name(), 'DejaVu Sans'],
    'font.size': 12, 'axes.titlesize': 13, 'axes.labelsize': 12,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.unicode_minus': False, 'svg.fonttype': 'none',
    'figure.facecolor': 'white', 'savefig.facecolor': 'white',
})
BLUE, ORANGE, GREEN, GREY = '#0072b2', '#d55e00', '#00846b', '#666666'

def save(fig, name, description):
    fig.savefig(OUT/(name+'.svg'), metadata={'Date': None, 'Description': description})
    fig.savefig(OUT/(name+'.png'), dpi=180)
    plt.close(fig)

# Acoustic conditions share a qualitative acoustic axis. Electrical stimulation
# uses its own axis; neither positions nor lengths are normative measurements.
fig, axes = plt.subplots(1, 2, figsize=(12, 5.0), layout='constrained', gridspec_kw={'width_ratios': [1.65, 1]})
ax = axes[0]
ax.set_title('(a) 声学听觉：可能的端点关系', loc='left', pad=18)
rows = [(2.6, .08, .94, '正常听力示例', BLUE),
        (1.6, .46, .94, '耳蜗性听损示例', ORANGE),
        (.6, .08, .66, '上端耐受下降示例', GREEN)]
for y, lower, upper, label, color in rows:
    ax.plot([lower, upper], [y, y], lw=8, solid_capstyle='butt', color=color)
    ax.plot([lower, lower], [y-.10, y+.10], lw=1.5, color=color)
    ax.plot([upper, upper], [y-.10, y+.10], lw=1.5, color=color)
    ax.text(lower, y+.18, '听阈' if y!=1.6 else '听阈升高', fontsize=10.5, ha='left')
    ax.text(upper, y-.20, '不舒适水平' if y!=.6 else '上端下降', fontsize=10.5, ha='right', va='top')
ax.set(xlim=(-.02, 1.02), ylim=(-.12, 3.15), yticks=[r[0] for r in rows], yticklabels=[r[3] for r in rows], xticks=[.08,.94], xticklabels=['较低','较高'], xlabel='声级（概念坐标，无数值刻度）')
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0, pad=12)
ax.tick_params(axis='x', length=0)
ax = axes[1]
ax.set_title('(b) 人工耳蜗：电刺激范围', loc='left', pad=18)
ax.plot([.20,.80], [1.55,1.55], color=BLUE, lw=8, solid_capstyle='butt')
ax.plot([.20,.20],[1.43,1.67],color=BLUE,lw=1.5)
ax.plot([.80,.80],[1.43,1.67],color=BLUE,lw=1.5)
ax.text(.20,1.86,'T：行为阈值',fontsize=11,ha='left')
ax.text(.80,1.20,'C／M：上端舒适水平',fontsize=11,ha='right')
ax.text(.50,.50,'依赖电极与脉冲参数\n条带长度不能与左图比较',fontsize=10.5,ha='center',color=GREY,linespacing=1.8)
ax.set(xlim=(0,1),ylim=(-.12,3.15),yticks=[],xticks=[.15,.85],xticklabels=['较低','较高'],xlabel='电刺激水平（独立概念坐标）')
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x',length=0)
save(fig,'01-listening-states','Separate qualitative acoustic and electrical axes; widths are not comparable. No clinical data, population norms, or diagnostic boundaries.')

fig, axes = plt.subplots(1, 3, figsize=(14, 5.0), layout='constrained')
input_level = np.linspace(30, 100, 501)
output = np.where(input_level <= 50, input_level+30, 80+(input_level-50)/2)
output = np.minimum(output,100)
ax = axes[0]
ax.set_title('(a) 助听器：声学压缩',loc='left',pad=16)
ax.plot(input_level,output,color=BLUE,lw=2.1)
ax.axhline(100,color=GREY,lw=1,linestyle='--')
ax.axvline(50,color=GREY,lw=1,linestyle=':')
ax.plot([50],[80],'o',color=BLUE,ms=5)
ax.text(33,80,'固定增益段',fontsize=11)
ax.text(64,83,'压缩段：2∶1',fontsize=11)
ax.text(60,101.5,'示意输出上限',fontsize=10.5,color=GREY)
ax.set(xlim=(30,100),ylim=(50,110),xlabel='输入声压级（dB SPL）',ylabel='输出声压级（dB SPL）')
ax.grid(alpha=.16)
level = np.linspace(35,85,1001)
amplitude_ratio = 10 ** ((level-85)/20)
minimum_ratio = 10 ** (-50/20)
log_mapping = np.log(amplitude_ratio/minimum_ratio)/np.log(1/minimum_ratio)
linear_in_db = (level-35)/50
matched_levels = np.array([35.,60.,85.])
matched_amplitudes = 10 ** ((matched_levels-85)/20)
matched_currents = np.array([0.,.5,1.])
ax = axes[1]
ax.set_title('(b) 人工耳蜗：线性幅度坐标',loc='left',pad=16,fontsize=12)
ax.plot(amplitude_ratio,log_mapping,color=ORANGE,lw=2.1,label='对数幅度压缩')
ax.plot(matched_amplitudes,matched_currents,'o',color=BLUE,ms=5)
ax.axhline(.5,color=GREY,lw=.8,linestyle=':',alpha=.55)
ax.annotate('60 dB SPL',xy=(matched_amplitudes[1],.5),xytext=(.25,.43),fontsize=10,color=BLUE,arrowprops={'arrowstyle':'-','color':BLUE,'lw':.8})
ax.text(.025,.045,'阈值端',fontsize=10,color=BLUE)
ax.text(.97,.91,'上端',fontsize=10,color=BLUE,ha='right')
ax.set(xlim=(0,1.02),ylim=(-.04,1.05),xlabel=r'相对声学包络幅度 $A/A_{\max}$',ylabel='归一化电流位置',yticks=[0,.25,.5,.75,1])
ax.legend(frameon=False,loc='lower right',fontsize=10.5)
ax.grid(alpha=.16)
ax = axes[2]
ax.set_title('(c) 同一映射：分贝坐标',loc='left',pad=16,fontsize=12)
ax.plot(level,log_mapping,color=ORANGE,lw=2.1,label='同一对数压缩函数')
ax.plot(matched_levels,matched_currents,'o',color=BLUE,ms=5)
ax.axhline(.5,color=GREY,lw=.8,linestyle=':',alpha=.55)
ax.text(62,.46,'60 dB SPL',fontsize=10,color=BLUE)
ax.text(37,.02,'阈值端',fontsize=10,color=BLUE)
ax.text(83,.85,'上端',fontsize=10,color=BLUE,ha='right')
ax.set(xlim=(34,86),ylim=(-.04,1.05),xlabel='输入声压级（dB SPL）',ylabel='归一化电流位置',yticks=[0,.25,.5,.75,1],xticks=[35,45,60,75,85])
ax.legend(frameon=False,loc='upper left',fontsize=10.5)
ax.grid(alpha=.16)
for ax in axes:
    ax.xaxis.label.set_fontsize(11)
    ax.yaxis.label.set_fontsize(11)
    ax.tick_params(labelsize=10)
save(fig,'02-device-mapping','Hypothetical hearing-aid compression. Panels b and c show the SAME logarithmic acoustic-amplitude-to-linear-current mapping, first on a linear envelope-amplitude axis and then on a dB SPL axis. Teaching input window 35–85 dB SPL. Based on Zeng 2004 section 5.2, not a complete manufacturer implementation or measured loudness function.')
assert np.all(np.diff(output)>=0) and output.max()==100
assert abs(log_mapping[0])<1e-12 and abs(log_mapping[-1]-1)<1e-12
assert np.max(np.abs(log_mapping-linear_in_db))<1e-12
assert np.all(np.diff(log_mapping)>0)
checks={'empiricalData':False,'crossSystemWidthsComparable':False,'figures':2,'deviceMappingPanels':3,'compressionRatio':2,'inputKneepointDbSpl':50,'gainAtKneepointDb':30,'outputLimitDbSpl':100,'ciTeachingInputWindowDbSpl':[35,85],'ciMapping':'logarithmic acoustic amplitude to linear current','minimumRelativeAcousticAmplitude':float(minimum_ratio),'matchedLevelsDbSpl':matched_levels.tolist(),'matchedRelativeAmplitudes':matched_amplitudes.tolist(),'matchedNormalizedCurrents':matched_currents.tolist(),'coordinateEquivalenceMaxError':float(np.max(np.abs(log_mapping-linear_in_db))),'source':'Zeng 2004 section 5.2, equations 5.2.1–5.2.3'}
(OUT/'figure-verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(checks))
