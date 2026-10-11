"""Reproduce the unpublished article's teaching figures and source register.

All plotted numbers are explicitly hypothetical. No paper figures or data are copied.
Run from the repository root: python scripts/prepare-outer-middle-ear-draft.py
"""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

SLUG = 'outer-middle-ear-transmission'
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/drafts/assets' / SLUG
RESEARCH = ROOT / 'docs/research/outer-middle-ear-2026-10-11'
OUT.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)
font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': font.get_name(), 'svg.fonttype': 'path',
                     'axes.unicode_minus': False, 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False})
PURPLE, BLUE, ORANGE = '#6952b4', '#28769c', '#c28035'

def save(fig, name):
    fig.savefig(OUT / (name+'.svg'), bbox_inches='tight', facecolor='white')
    fig.savefig(OUT / (name+'.png'), dpi=160, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def box(ax, x, y, text, color=PURPLE, width=0.16):
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x-width/2,y-0.105), width, .21,
        boxstyle='round,pad=0.015', linewidth=1, edgecolor=color, facecolor='#f8f9fc'))
    ax.text(x,y,text,ha='center',va='center',fontsize=11)

def arrow(ax, a, b, label=''):
    ax.annotate('', xy=b, xytext=a, arrowprops={'arrowstyle':'->', 'color':'#66677a','lw':1.5})
    if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.05,label,ha='center',fontsize=9)

fig, ax = plt.subplots(figsize=(11,4.7))
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
for x,t,c in [(0.10,'外部声场\n参考声压 P_ref',BLUE),(.30,'耳廓与耳道\n耳道声压 P_EC',BLUE),
              (.50,'鼓膜两侧\n压差 ΔP_TM',PURPLE),(.70,'听骨链与镫骨\n速度 V_s',PURPLE),
              (.90,'耳蜗基底入口\n压差 P_SV − P_ST',ORANGE)]: box(ax,x,.62,t,c)
for x in [.20,.40,.60,.80]: arrow(ax,(x-.012,.62),(x+.012,.62))
ax.text(.1,.85,'空气声学',color=BLUE,ha='center')
ax.text(.6,.85,'结构力学',color=PURPLE,ha='center')
ax.text(.9,.85,'液体声学',color=ORANGE,ha='center')
box(ax,.50,.24,'中耳腔声压 P_ME\n咽鼓管参与静压调节',width=.27)
arrow(ax,(.50,.36),(.50,.50))
box(ax,.88,.24,'圆窗及耳蜗负载\n参与压力与流量边界',ORANGE,width=.20)
arrow(ax,(.88,.36),(.90,.50))
ax.text(.02,.02,'功能与测量量示意；不按解剖比例绘制。圆窗与咽鼓管并非图中主路径上的串联声源。',fontsize=10,color='#66677a')
save(fig,'01-transmission-path')

c, rho = 343., .8
freq = np.linspace(500,10000,1901)
fig, axes = plt.subplots(1,2,figsize=(11,4.5))
for L,col in [(.015,PURPLE),(.020,BLUE),(.025,ORANGE)]:
    H=1+rho*np.exp(-2j*2*np.pi*freq/c*L)
    axes[0].plot(freq/1000,20*np.log10(abs(H)),label=f'L = {L*1000:.0f} mm',color=col)
axes[0].axhline(0,color='#aaa',lw=.8,ls='--')
axes[0].set(xlabel='频率 / kHz',ylabel='总声压相对前向声压 / dB',ylim=(-16,7))
axes[0].legend(fontsize=9); axes[0].grid(alpha=.15)
x=np.linspace(0,.03,401); f=4000.
axes[1].plot(x*1000,20*np.log10(abs(1+rho*np.exp(-2j*2*np.pi*f/c*x))),color=PURPLE)
axes[1].axvline(c/(4*f)*1000,color=ORANGE,ls='--',label='首个压力极小值')
axes[1].set(xlabel='距鼓膜距离 / mm',ylabel='总声压相对前向声压 / dB',ylim=(-16,7))
axes[1].legend(fontsize=9); axes[1].grid(alpha=.15)
fig.suptitle('均匀无损耳道模型：同一前向声波，不同位置的总声压不同',fontsize=13)
fig.text(.5,-.025,'教学参数：c = 343 m/s；鼓膜处压力反射系数 ρ = 0.8（实数）；右图 f = 4 kHz。非实测。',ha='center',fontsize=10)
fig.tight_layout()
save(fig,'02-ear-canal-standing-waves')

G=1.3*55/3.2
fig,ax=plt.subplots(figsize=(10,4.3));ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
box(ax,.17,.62,'输入端\n鼓膜压差与体积速度',BLUE,width=.26)
box(ax,.50,.62,'理想无损变压器\nG = r A_T / A_s',PURPLE,width=.25)
box(ax,.84,.62,'输出端\n镫骨面声压与体积速度',ORANGE,width=.27)
arrow(ax,(.31,.62),(.36,.62));arrow(ax,(.64,.62),(.69,.62))
ax.text(.17,.29,'输入归一化\n声压幅度 1\n体积速度幅度 1\n平均功率 1',ha='center',va='center',linespacing=1.65)
ax.text(.50,.26,'教学假定\nA_T = 55 mm²\nA_s = 3.2 mm²；r = 1.3',ha='center',va='center',linespacing=1.7)
ax.text(.84,.29,f'输出归一化\n声压幅度 {G:.2f}\n体积速度幅度 {1/G:.4f}\n平均功率 1',ha='center',va='center',linespacing=1.65)
ax.text(.5,.94,'声压增大伴随体积速度减小；理想模型不创造能量',ha='center',fontsize=14)
ax.text(.5,.02,'只对同相、阻性负载的归一化例子直接显示功率；实际耳需保留复数相位和频率依赖。',ha='center',fontsize=10,color='#66677a')
save(fig,'03-transformer-power')

phi=np.linspace(0,np.pi,361)
diff=np.abs(1-.8*np.exp(1j*phi))
fig,axes=plt.subplots(1,2,figsize=(10.7,4.5))
axes[0].plot(phi*180/np.pi,diff,color=PURPLE,lw=2)
axes[0].scatter([0,180],[.2,1.8],color=ORANGE,zorder=3)
axes[0].set(xlabel='P_ST 相对 P_SV 的相位 / °',ylabel='基底入口压差幅度 / Pa',xlim=(0,180),ylim=(0,2))
axes[0].grid(alpha=.15)
axes[1].bar(['两压力同相','两压力反相'],[.2,1.8],color=[BLUE,PURPLE],width=.55)
axes[1].set(ylabel='|P_SV − P_ST| / Pa',ylim=(0,2))
for i,val in enumerate([.2,1.8]): axes[1].text(i,val+.06,f'{val:.1f} Pa',ha='center')
fig.suptitle('耳蜗输入压差取决于幅度和相位',fontsize=14)
fig.text(.5,-.025,'教学假定：|P_SV| = 1 Pa，|P_ST| = 0.8 Pa；同一频率、共同相位参考。非实测。',ha='center',fontsize=10)
fig.tight_layout();save(fig,'04-cochlear-pressure-phase')

calcs={'teaching_only': True, 'c_m_per_s': c,'reflection_coefficient':rho,
 'area_T_mm2':55,'area_s_mm2':3.2,'lever_ratio':1.3,
 'pressure_gain':G,'pressure_gain_db':20*math.log10(G),'volume_velocity_ratio':1/G,
 'quarter_wave_null_hz':{str(L):c/(4*L/1000) for L in [15,20,25]},
 'null_total_to_forward_db':20*math.log10(.2),
 'TM_to_null_pressure_db':20*math.log10(1.8/.2),
 'differential_pressure_same_phase_Pa':.2,'differential_pressure_opposite_phase_Pa':1.8}
assert abs(G*(1/G)-1)<1e-12
assert abs(calcs['pressure_gain_db']-26.983)<.01
assert abs(calcs['quarter_wave_null_hz']['20']-4287.5)<1e-9
(RESEARCH/'teaching-calculations.json').write_text(json.dumps(calcs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Bibliography is created once from the verified metadata cache, then becomes a
# self-contained tracked input. Later runs do not need to download papers again.
ref_path=RESEARCH/'references.json'
if not ref_path.exists():
    records=json.loads((ROOT/'artifacts/outer-middle-ear-research/source-metadata.json').read_text(encoding='utf-8'))
    by_pmc={r.get('pmcid'):r for r in records if r.get('pmcid')}
    by_doi={r['doi'].lower():r for r in records}
    refs=[]
    def manual(id,title,authors,year,publication,url,access,supports,doi=None):
        r=dict(id=id,title=title,authors=authors,year=year,publication=publication,url=url,access=access,supports=supports)
        if doi:r['doi']=doi
        refs.append(r)
    def paper(id,key,access,supports,grade='Core'):
        r=by_pmc[key] if key.startswith('PMC') else by_doi[key.lower()]
        ji=r.get('journalInfo',{});j=ji.get('journal',{}).get('medlineAbbreviation') or ji.get('journal',{}).get('title','')
        vol=ji.get('volume','');issue=ji.get('issue')
        pub=j+(' '+vol if vol else '')+(f'({issue})' if issue else '')
        manual(id,r['title'],r['authorString'],r['pubYear'],pub,
               'https://pmc.ncbi.nlm.nih.gov/articles/'+key+'/' if key.startswith('PMC') else 'https://pubmed.ncbi.nlm.nih.gov/'+r['id']+'/',access,supports,r['doi'])
        refs[-1].update(relevance=grade,verification_date='2026-10-11')
    manual('nidcd-hearing','How Do We Hear?','National Institute on Deafness and Other Communication Disorders','n.d.','NIDCD health information','https://www.nidcd.nih.gov/health/how-do-we-hear','documentation','传声结构概览；官方科普资料。')
    manual('mit-middle-ear-2004','Lecture 12: Middle Ear Structure–Function & Pathology','MIT 6.551J / HST.714J','2004','Acoustics of Speech and Hearing, course lecture notes','https://ocw.mit.edu/courses/6-551j-acoustics-of-speech-and-hearing-fall-2004/5cfca1eb3a60e20104b71642a519a8e7_lec_12_2004.pdf','documentation','阅读讲义中结构、二端口、负载和功率匹配内容；图示与计算另行原创。')
    paper('rosowski-transmission-2025','PMC12411397','fulltext','阅读检索服务可访问的综述原文中简化模型、颞骨制备及传声路径段落；未取得可下载全文。','Important')
    paper('voss-geometry-2025','PMC12198549','fulltext','取得全文 XML，阅读摘要、几何方法及年龄与个体差异结果；CT几何研究不是声学传递函数测量。')
    paper('charaziak-calibration-2017','PMC5848844','fulltext','阅读可访问原文的校准理论、方法及探头位置结果；前向声压与发射声压校正作用不同。')
    paper('keefe-infants-1993','10.1121/1.407347','abstract','核对摘要中的年龄组、耳道阻抗和反射系数发育结论；未阅读全文。')
    paper('cheng-tm-2019','PMC6338545','abstract','核对摘要：人尸颞骨全场全息测量，正反向刺激的鼓膜运动不同；未阅读全文。')
    paper('voss-responses-2000','10.1016/s0378-5955(00)00177-5','abstract','核对摘要列出的镫骨速度、腔声压、鼓膜输入阻抗及腔阻抗测量量；未阅读全文。')
    paper('nakajima-pressure-2009','PMC2644388','fulltext','阅读检索服务可访问的原文结果、结论及传感器方法段落；基底两阶复数压差与听骨链中断结果；未下载通读全文。')
    paper('rosowski-reflectance-2012','PMC3223546','abstract','核对摘要的58耳样本、声反射、脐部速度、鼓室图及频率依赖关联；未阅读全文。')
    manual('asha-adult-assessment','Hearing Loss in Adults','American Speech-Language-Hearing Association','n.d.','ASHA Practice Portal','https://www.asha.org/practice-portal/clinical-topics/hearing-loss/','documentation','阅读评估部分关于声导抗、鼓室图、声反射和听力检查的作用。')
    manual('mukerji-reflex-2010','Auditory Brainstem Circuits that Mediate the Middle Ear Muscle Reflex','Mukerji S; Windsor AM; Lee DJ','2010','Trends in Amplification 14(3):170–191','https://pmc.ncbi.nlm.nih.gov/articles/PMC3624626/','abstract','核对摘要及综述说明中的镫骨肌反射环路与物种差异；未通读全文。','10.1177/1084713810381771')
    paper('trevino-reflex-2023','PMC9867568','fulltext','阅读检索服务可访问的原文反射测量、临床应用及结论段落；人类与动物突触损伤证据边界；未下载通读全文。','Important')
    paper('voss-perforation-2001','10.1080/000164801300043343','abstract','核对摘要：穿孔大小、频率、腔容积及位置效应；未阅读全文。')
    paper('mehta-perforation-2006','PMC2918411','fulltext','阅读检索服务可访问的原文引言与结论，并核对摘要；临床穿孔位置影响有限的条件性结果；未下载通读全文。')
    paper('bevis-perforation-2022','PMC9130167','fulltext','取得全文 XML，阅读六个人颞骨的穿孔、激光测振及有限元分析方法和结果；保留与既往位置效应结论的分歧。')
    paper('stieger-bone-2018','PMC6226413','abstract','核对摘要中的骨导两阶声压与运动读数、骨振动伪迹及方法边界；未阅读全文。','Important')
    paper('fallon-discontinuity-2026','PMC12581600','abstract','核对摘要：六个颞骨与两例临床相关观察；期刊年2026、在线发表2025，未阅读全文。')
    manual('baselt-fresh-frozen-2025','Middle-ear sound transmission in human cadaveric temporal bones: fresh vs. fresh-frozen','Baselt B; Schär M; Huber A; Sim JH','2025','Hearing Research 467:109433','https://doi.org/10.1016/j.heares.2025.109433','abstract','核对出版者可检索摘要：101个颞骨、57新鲜与44冻存的组间比较；出版者正文未能访问，不能解释为同一标本的冻结因果试验。','10.1016/j.heares.2025.109433')
    paper('jiang-pediatric-wai-2024','PMC11352035','fulltext','取得全文 XML，阅读摘要与小儿宽带声导抗综述相关段落；综述提供方法概览，不能代替设备和年龄特定诊断验证。','Important')
    paper('chang-oct-2013','PMC3769454','abstract','核对摘要：龙猫耳 OCT 测振，同时观测鼓膜与听骨；属于动物技术演示，未阅读全文。','Important')
    paper('rosowski-blast-2019','PMC6881194','abstract','核对摘要及可检索原文引言中的强瞬态传声模型限制；未通读全文。','Important')
    ref_path.write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(calcs,ensure_ascii=False,indent=2))
