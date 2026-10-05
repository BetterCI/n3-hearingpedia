from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.font_manager import FontProperties

folder = Path('docs/drafts/assets/auditory-filter')
font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': font.get_name(), 'font.size': 10,
    'svg.fonttype': 'none', 'axes.unicode_minus': False, 'figure.facecolor': 'white',
    'savefig.facecolor': 'white', 'axes.spines.top': False, 'axes.spines.right': False})
blue, orange, green, ink = '#286f9b', '#b37528', '#45785a', '#26323c'

def erb(fc): return 24.7*(4.37*fc/1000+1)
def roex(f, fc, p):
    g=np.abs(f-fc)/fc
    return (1+p*g)*np.exp(-p*g)
def save(fig, name):
    fig.savefig(folder/(name+'.svg'),bbox_inches='tight')
    fig.savefig(folder/(name+'.png'),dpi=180,bbox_inches='tight')
    plt.close(fig)

# The weighting curves are illustrative, not measured human filters.
f=np.linspace(350,2050,7001)
tones=np.array([750.,1000.,1500.]); power=np.array([1.,.7,.8])
fc=np.linspace(400,2000,1000)
excitation=np.array([np.sum(power*roex(tones,c,4*c/erb(c))) for c in fc])
fig, axes=plt.subplots(1,3,figsize=(11.5,3.65),layout='constrained')
ax=axes[0]
marker,stems,base=ax.stem(tones,power,basefmt=' ')
plt.setp(marker,color=ink,markersize=4);plt.setp(stems,color=ink,linewidth=1.4)
ax.set(xlim=(350,2050),ylim=(0,1.12),xlabel='输入频率（赫兹）',ylabel='谱线相对功率',title='A  输入的三个频率成分')
ax=axes[1]
for c in [500,650,800,1000,1250,1600,2000]:
    ax.plot(f,roex(f,c,4*c/erb(c)),lw=1.2,color=blue,alpha=.9 if c==1000 else .35)
ax.set(xlim=(350,2050),ylim=(0,1.12),xlabel='输入频率（赫兹）',ylabel='归一化功率权重',title='B  中心频率不同的重叠滤波器')
ax=axes[2]
ax.plot(fc,excitation,color=green,lw=1.8)
ax.set(xlim=(350,2050),ylim=(0,1.2),xlabel='滤波器中心频率（赫兹）',ylabel='输出相对功率',title='C  同一输入的激励模式')
for ax in axes: ax.set_xticks([500,1000,1500,2000]);ax.grid(alpha=.12)
save(fig,'01-filterbank-excitation')

# Equal area and peak, different shape. Analytic Gaussian area used.
sigma=60.; gaussian_erb=np.sqrt(2*np.pi)*sigma
halfpower=2*np.sqrt(2*np.log(2))*sigma
gaussian_f=np.linspace(650,1350,5001); w=np.exp(-.5*((gaussian_f-1000)/sigma)**2)
fig,axes=plt.subplots(1,2,figsize=(10.3,3.8),layout='constrained')
ax=axes[0]
ax.fill_between(gaussian_f,w,color=blue,alpha=.12)
ax.plot(gaussian_f,w,color=blue,lw=1.8,label='高斯功率权重（教学函数）')
ax.add_patch(Rectangle((1000-gaussian_erb/2,0),gaussian_erb,1,fill=False,ec=orange,lw=1.6,ls='--'))
ax.plot([],[],color=orange,ls='--',label='同峰值、同面积的矩形')
ax.hlines(.5,1000-halfpower/2,1000+halfpower/2,color=ink,lw=1.4)
ax.text(1160,.50,'半功率带宽',fontsize=9,va='center')
ax.set(xlim=(650,1350),ylim=(0,1.20),xlabel='频率（赫兹）',ylabel='归一化功率权重',title='A  等效矩形带宽的面积定义')
ax.legend(frameon=False,fontsize=8,loc='upper right');ax.grid(alpha=.12)
ax=axes[1]
ff=np.geomspace(100,8000,500)
ax.plot(ff,erb(ff),color=blue,lw=1.8)
for c in [500,1000,2000,4000]: ax.scatter(c,erb(c),s=18,color=blue)
ax.annotate('1000赫兹：约133赫兹',xy=(1000,erb(1000)),xytext=(1200,300),fontsize=9,arrowprops={'arrowstyle':'-','color':ink})
ax.set(xscale='log',xlim=(100,8000),ylim=(0,930),xlabel='中心频率（赫兹，对数轴）',ylabel='等效矩形带宽（赫兹）',title='B  经典正常听力经验式')
ax.set_xticks([100,500,1000,2000,4000,8000],labels=['100','500','1000','2000','4000','8000'])
ax.grid(alpha=.12)
save(fig,'02-erb-definition')

# Fixed finite outer noise edges and fixed PSD, varying notch half-width.
f=np.linspace(500,1500,20001); weight=roex(f,1000,30)
fig,axes=plt.subplots(1,3,figsize=(11.5,3.8),layout='constrained')
integrals=[]
for ax,d,title in zip(axes[:2],[20,120],['A  较窄凹口','B  较宽凹口']):
    noise=(np.abs(f-1000)>=d).astype(float)
    passed=weight*noise
    integrals.append(float(np.trapz(passed,f)))
    ax.fill_between(f,passed,color=green,alpha=.23,label='噪声通过滤波器后的权重')
    ax.plot(f,weight,color=blue,lw=1.6,label='滤波器功率权重')
    ax.plot(f,noise,color=ink,lw=1.1,label='噪声谱密度／固定谱密度')
    ax.set(xlim=(500,1500),ylim=(0,1.13),xlabel='频率（赫兹）',ylabel='归一化权重／谱密度',title=title)
    ax.set_xticks([500,1000,1500]);ax.grid(alpha=.12)
handles,labels=axes[0].get_legend_handles_labels()
fig.legend(handles,labels,frameon=False,fontsize=8,loc='lower center',bbox_to_anchor=(.5,-.12),ncol=3)
ds=np.linspace(0,250,126)
passed=np.array([np.trapz(weight*(np.abs(f-1000)>=d),f) for d in ds])
floor=.01*passed[0]
classic=10*np.log10(passed/passed[0]); extended=10*np.log10((passed+floor)/(passed[0]+floor))
ax=axes[2]
ax.plot(ds,classic,color=blue,lw=1.6,label='仅考虑外部噪声')
ax.plot(ds,extended,color=orange,lw=1.6,label='另加固定内部噪声底')
ax.axhline(10*np.log10(floor/(passed[0]+floor)),color=orange,ls=':',lw=1)
ax.set(xlim=(0,250),ylim=(-28,1),xlabel='凹口半宽（赫兹）',ylabel='相对零凹口条件的阈值变化（分贝）',title='C  检测阈与凹口半宽的关系')
ax.grid(alpha=.12);ax.legend(frameon=False,fontsize=8,loc='lower left')
save(fig,'03-notched-noise')

checks={
 'erb_N_Hz':{str(c):float(erb(c)) for c in [500,1000,2000,4000]},
 'erb_number_1000':float(21.4*np.log10(1+.00437*1000)),
 'gaussian_sigma_Hz':sigma, 'gaussian_ERB_Hz':float(gaussian_erb),
 'gaussian_half_power_bandwidth_Hz':float(halfpower),
 'gaussian_area_numerical_Hz':float(np.trapz(w,gaussian_f)),
 'notch_halfwidths_Hz':[20,120], 'passed_noise_integrals_Hz':integrals,
 'wide_notch_passes_less_noise':bool(integrals[1]<integrals[0]),
 'threshold_nonincreasing':bool(np.all(np.diff(extended)<=1e-8)),
 'roex_p':30, 'roex_whole_line_ERB_Hz':4*1000/30,
 'internal_floor_fraction_of_zero_notch_noise':.01,
 'frequency_grid_step_Hz':float(f[1]-f[0]),
 'source':'Original teaching figures; no measured data copied.'
}
assert checks['wide_notch_passes_less_noise'] and checks['threshold_nonincreasing']
assert abs(checks['gaussian_area_numerical_Hz']-gaussian_erb)<1e-3
(folder/'figure-verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False))
