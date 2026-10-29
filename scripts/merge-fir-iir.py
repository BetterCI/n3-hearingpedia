"""One-time editorial merge; retains the two original drafts as research snapshots."""
from pathlib import Path
import re,json

ROOT=Path(__file__).resolve().parents[1]
REC=ROOT/'docs/research/fir-iir-2026-10-29'
ARCHIVE=REC/'before-merge'
ARCHIVE.mkdir(exist_ok=True)
def read(slug):
    p=ROOT/f'src/content/concepts/{slug}.md'
    if p.exists():
        s=p.read_text(encoding='utf-8')
        (ARCHIVE/f'{slug}.md').write_text(s,encoding='utf-8')
    else:s=(ARCHIVE/f'{slug}.md').read_text(encoding='utf-8')
    return s
f=read('fir-filter');i=read('iir-filter')
def sections(s):
    return {title:body.strip() for title,body in re.findall(r'^## (.+)\n([\s\S]*?)(?=^## |\Z)',s,re.M)}
F,I=sections(f),sections(i)
intro='''**FIR 滤波器**（finite impulse response filter，有限脉冲响应滤波器）和 **IIR 滤波器**（infinite impulse response filter，无限脉冲响应滤波器）是按零状态单位脉冲响应是否有限区分的两类线性时不变滤波器。FIR 的响应只在有限个样本处非零，常用有限卷积实现；IIR 的理论响应延伸至无限多个样本，常用反馈递推，以少量状态产生长时间的动态过程。[1](#ref-fi-smith-window)[1](#ref-fi-smith-recursive)

两类系统都能改变声音的频率成分，也会改变时间结构。在听觉研究中，滤波用于刺激构造、频带分解、均衡、采样率转换和神经记录预处理；选择方案时需要同时检验幅度、相位、稳定性、延迟、计算成本及实际输出。FIR 不自动保证线性相位，IIR 不必然不稳定；“有限或无限响应”“线性或最小相位”“因果或非因果”“实时或离线”是不同的分类维度。

本文以固定实系数、离散时间、因果有理系统为主要对象，先建立统一数学框架，再分别说明设计和实现，用共同指标比较两类方案。真实耳蜗、动态压缩和自适应系统可能超出固定线性模型；所有数值图均为原创教学计算，不能直接作为设备处方或听觉获益证据。'''

parts=[]
def add(title,body):parts.append(f'## {title}\n\n{body.strip()}')
add('定义、卷积与反馈递推',F['有限记忆怎样形成频率选择']+'\n\n'+I['反馈怎样产生无限响应'].replace('### 差分方程与符号约定','### IIR：差分方程与符号约定').replace('### 一阶平滑器的解析例子','### IIR 一阶平滑器的解析例子'))
stable=F['验证、报告与常见误读'].split('### 稳定性与有限精度\n\n')[1].split('\n\n延迟补偿')[0]
add('稳定性、零极点与共振','### FIR 的有限响应与稳定性\n\n'+stable+'\n\n### IIR 的极点判据与动态过程\n\n'+I['零极点、稳定性与共振'])
add('从任务写出可检验的规格',F['从任务写出可检验的滤波规格'])
add('FIR 设计：窗函数、等波纹与拟合',F['三类常用设计方法'])
add('IIR 设计：经典原型与双线性变换','### 经典原型的不同目标\n\n'+I['经典原型的不同目标']+'\n\n### 双线性变换与频率预畸变\n\n'+I['双线性变换与频率预畸变'])
phase=F['线性相位、最小相位与时间扩散'].replace('转换接口与默认参数见来源 6，原理见来源 7。','转换接口与最小相位原理见相应正文引文。')
add('相位、群延迟与时间扩散',phase+'\n\n### IIR 群延迟与离线前后向处理\n\n'+I['相位、群延迟和前后向滤波'])
add('计算实现、有限精度与状态管理','### FIR：直接卷积、FFT 与多相\n\n'+F['实现：直接卷积、FFT 与多相']+'\n\n### IIR：级联二阶节\n\n'+I['为什么通常采用级联二阶节']+'\n\n### IIR：初始状态、分块与记录端点\n\n'+I['初始状态、分块与记录端点'])
icomp=I['同一任务下与 FIR 的比较']
table=icomp[icomp.index('| 比较项目'):icomp.index('\n\n读图时')]
numerics=icomp[icomp.index('本地计算中，IIR 最大极点半径'):]
add('共同指标下的完整比较算例',F['与 IIR 共用指标的数值算例']+'\n\n'+table+'\n\n'+numerics)
apps=F['听觉研究与设备中的使用']
extra=I['听觉应用及其解释边界']
model=extra[extra.index('共振型 IIR 可以'):extra.index('### 电生理与行为实验')].strip()
apps+='\n\n### 共振模型与通道合成\n\n'+model
apps+='\n\n对[听觉脑干反应](../auditory-brainstem-response/)等短潜伏期记录，原型、截止、方向和边界同样会影响峰形与潜伏期。应保留原始数据，使用已知起点的响应检查整条处理链；神经响应的时序不能仅凭滤波后的一个峰判断。[1](#ref-fi-mne-filtering)[1](#ref-widmann-2015)'
add('听觉实验、设备与模型中的应用',apps)
verify=F['验证、报告与常见误读'].split('### 稳定性与有限精度')[0].strip()
iv=I['验证、沿革与继续研究']
longtail=iv.split('### 怎样报告长尾与可忽略误差\n\n')[1].split('\n\n递归结构')[0]
implementation=iv.split('### 从设计模型到可用实现\n\n')[1].split('\n\n### 怎样报告长尾')[0]
add('验证、报告与结果解释',verify+'\n\n### 实现与分块一致性检查\n\n'+implementation+'\n\n### IIR 长尾与可忽略误差\n\n'+longtail+'\n\n### 最小报告信息\n\n一份可复现报告应保存采样率与输入单位、全部频带边界、容差及 dB 定义、最终阶数、全部系数或 SOS、增益、设计方法与软件版本，明确单向或前后向、相位类型、初始化、端点与分块状态。数字阶段报告实际频响、群延迟和脉冲响应；实时部署另报位宽、内部数值范围、缓冲及端到端延迟，多通道另报同步和重建误差。专业听觉评价还需报告人群、材料、声级、任务和设备耦合条件。')
add('方法沿革与继续研究',F['方法沿革与继续研究']+'\n\n'+iv.split('\n\n递归结构')[1].split('\n\n一份可复现报告')[0].join(['递归结构',''])+'\n\n对于动态更新参数的系统，还需检验系数切换和状态迁移；每组固定系数的稳定性不能代替时变系统的整体分析。工程指标改善是否转化为可懂度、音质或实际使用收益，需要对应研究任务的数据。')
add('参见与图源说明','可结合[相位延迟与群延迟](../phase-and-group-delay/)、[频谱与功率谱密度](../spectrum-and-power-spectral-density/)、[最小相位系统](../minimum-phase-system/)、[倒谱](../cepstrum/)、[听觉滤波器](../auditory-filter/)、[时域包络](../temporal-envelope/)和[通道相互作用](../channel-interaction/)阅读。\n\n五张图均为本站原创教学计算，未转载第三方图像。脚本为 `scripts/generate-fir-iir.py`；实际软件版本、系数和数值检查保存于 `docs/research/fir-iir-2026-10-29/figure-verification.json`。来源覆盖基础理论和公开方法文档，本次合并未开展新的文献检索，不是完整最新研究综述。词条保留 Draft 待专业审阅。')
body=intro+'\n\n'+'\n\n'.join(parts)+'\n'
# A newly written cross-link is optional if another concurrent draft does not exist.
if not (ROOT/'src/content/concepts/minimum-phase-system.md').exists():
    body=body.replace('[最小相位系统](../minimum-phase-system/)、','')
ids=[]
def cite(m):
    rid=m[1]
    if rid not in ids:ids.append(rid)
    return f'[{ids.index(rid)+1}](#ref-{rid})'
body=re.sub(r'\[\d+\]\(#ref-([^\s)]+)\)',cite,body)
number=0
def figure(m):
    global number
    number+=1
    return f'<figcaption><strong>图 {number}　'
body=re.sub(r'<figcaption><strong>图 \d+　',figure,body)
assert number==5
assert len(re.findall('01-common-specification.svg',body))==2 # one anchor, one img
front=f'''---
title: "FIR 与 IIR 滤波器"
english: "FIR and IIR Filters"
slug: "fir-and-iir-filters"
summary: "在统一框架下比较 FIR 与 IIR 滤波器，连接卷积、反馈、零极点、稳定性和相位，展开两类设计与实现方法，并用共同指标算例说明听觉实验、设备和神经记录中的选择与验证。"
categories: ["signal-processing", "acoustics", "research-methods"]
tags: ["FIR", "IIR", "数字滤波器", "卷积", "反馈", "线性相位", "最小相位", "二阶节", "稳定性"]
aliases: ["FIR 滤波器", "IIR 滤波器", "有限脉冲响应滤波器", "无限脉冲响应滤波器", "有限冲激响应滤波器", "无限冲激响应滤波器", "FIR filter", "IIR filter", "finite impulse response", "infinite impulse response"]
level: ["undergraduate", "graduate"]
status: draft
depth: in-depth
last_updated: "2026-10-29"
literature_checked_at: "2026-10-29"
authors: ["AI 辅助编写"]
reviewer: null
reviewed_at: null
knowledge_area: "methods"
kind: "analysis"
key_facts:
  - {{label: "分类依据", value: "零状态单位脉冲响应是否只在有限个样本处非零"}}
  - {{label: "FIR", value: "常用有限卷积实现；有限系数保证理想系统 BIBO 稳定"}}
  - {{label: "IIR", value: "常用反馈递推；因果最简有理系统稳定需全部极点严格在单位圆内"}}
  - {{label: "相位", value: "FIR 可设计为线性或最小相位；常见 IIR 群延迟随频率变化"}}
  - {{label: "选择目标", value: "共同权衡幅度、时间扩散、延迟、计算成本与有限精度"}}
references: {json.dumps(ids,ensure_ascii=False)}
order: 6.4
---

'''
(ROOT/'src/content/concepts/fir-and-iir-filters.md').write_text(front+body,encoding='utf-8')
for slug in ['fir-filter','iir-filter']:
    p=ROOT/f'src/content/concepts/{slug}.md'
    if p.exists():p.unlink()
print(json.dumps({'references':len(ids),'figures':number,'chinese_characters':len(re.findall(r'[\u3400-\u9fff]',body))},ensure_ascii=False))
