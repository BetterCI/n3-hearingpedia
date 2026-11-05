"""Register verified sources and narrowly scoped navigation changes."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/speech-enhancement-and-noise-reduction-2026-11-06'
records={r['doi'].lower():r for r in json.loads((OUT/'bibliographic-check.json').read_text(encoding='utf-8'))}
refs={}
def paper(key,doi,url,access,supports):
    r=records[doi.lower()];assert r['status']==200
    publication=html.unescape(r['container-title'][0])
    if r.get('volume'):publication+=', '+r['volume']+(f"({r['issue']})" if r.get('issue') else '')
    if r.get('page'):publication+=', '+r['page']
    refs[key]={'title':html.unescape(r['title'][0]),'authors':'; '.join(' '.join([a.get('given',''),a.get('family',a.get('name',''))]).strip() for a in r['author']),'year':str(r['published']['date-parts'][0][0]),'publication':publication,'doi':doi,'url':url,'access':access,'supports':'2026-11-06：'+supports}
paper('se-wang-chen-2018','10.1109/TASLP.2018.2842159','https://jitongchen.com/papers/overview_taslp2018.pdf','fulltext','作者公开全文：任务范围、掩蔽目标与泛化背景；综述用作导航，临床和具体系统结论另引原始研究。')
paper('se-boll-1979','10.1109/TASSP.1979.1163209','https://course.ece.cmu.edu/~ece491/homework/Boll79.pdf','fulltext','已读取CMU公开论文PDF的算法及残余噪声段落。原文主要为幅度谱减；词条另列功率谱减教学变体，不声称是原文逐式复现。')
paper('se-ephraim-1984','10.1109/TASSP.1984.1164453','https://malah.net.technion.ac.il/files/2017/08/Ephraim_Speech_Enhancement_ASSP84.pdf','fulltext','作者PDF摘要、检索可读的决策导向段落及出版元数据：短时谱幅度MMSE与先验SNR；不声称核对全文每个公式。维纳图为本站独立代数推导。')
paper('se-martin-2001','10.1109/89.928915','https://www.csd.uoc.gr/~hy578/2005/projects/ieee_sp_tsap_2001009_05jul_0504mart.pdf','fulltext','公开原论文PDF摘要及方法导言：最小统计量、无需硬VAD及最小值偏差补偿；未照抄具体参数。')
paper('se-paliwal-2011','10.1016/j.specom.2010.12.003','https://www.sciencedirect.com/science/article/abs/pii/S0167639310002086','abstract','出版方摘要和引言：32 ms窗条件下理想与非理想相位实验，不能把oracle结果当部署性能。')
paper('se-complex-2016','10.1109/TASLP.2015.2512042','https://pmc.ncbi.nlm.nih.gov/articles/PMC4826046/','abstract','Europe PMC原始摘要：同时估计复数掩蔽实虚部；文中两个相量案例为本站独立代数演示，不是论文实验数据。')
paper('se-souden-2010','10.1109/TASL.2009.2025790','https://www.wirelesslab.ca/File/pdf_files/journals/J042.pdf','fulltext','作者机构公开17页PDF：多通道维纳／MVDR约束与噪声失真折中。本站采用已知传递向量的标准形式和自设阵列，不冒充原文仿真复现。')
refs['se-deepfilter-2023']={'title':'DeepFilterNet: Perceptually Motivated Real-Time Speech Enhancement','authors':'Hendrik Schröter; Alberto N. Escalante-B.; Tobias Rosenkranz; Andreas Maier','year':'2023','publication':'Interspeech 2023, Show & Tell, 2008–2009','url':'https://www.isca-archive.org/interspeech_2023/schroter23b_interspeech.html','access':'fulltext','supports':'2026-11-06：ISCA会议PDF第2–4节；48 kHz、20 ms窗、10 ms步长、两帧前视与40 ms延迟；RTF 0.19限定原文CPU和实现。作者顺序按会议PDF，未沿用不同顺序的arXiv元数据。'}
paper('se-close-2024','10.23919/EUSIPCO63174.2024.10714927','https://www.eurasip.org/Proceedings/Eusipco/Eusipco2024/pdfs/0000021.pdf','fulltext','EUSIPCO原论文全文：预测器作为训练目标可能引入伪迹，主观评价验证其可察觉性；不泛化为所有生成式网络的行为。')
paper('se-pase-2026','10.1609/aaai.v40i39.40562','https://arxiv.org/html/2511.13300v1','fulltext','AAAI出版记录与Crossref核对2026卷期；出版全文受访问限制，实际读取作者arXiv:2511.13300v1全文的方法及评价段落。仅概述表征去噪、双流重建和保真目标，不引用最终版数值或宣称普遍领先。')
paper('se-hu-2007','10.1121/1.2766778','https://pubmed.ncbi.nlm.nih.gov/17927437/','abstract','Europe PMC原始摘要：8算法、4噪声、0与5 dB、正常听者；一个噪声条件例外，未得显著改善不解释为所有条件严格零效应。')
paper('se-healy-2013','10.1121/1.4820893','https://pmc.ncbi.nlm.nih.gov/articles/PMC3799726/','abstract','Europe PMC原始摘要：学习掩蔽、训练测试句子不同、所测噪声下正常和听损听者获益；不推出所有陌生噪声或日常设备均有相同改善。')
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8')
write('src/data/speech-enhancement-references.ts',"import type { Reference } from './references';\n\nexport const speechEnhancementReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n')
p='src/data/references.ts';s=read(p)
if 'import { speechEnhancementReferences }' not in s:
    s="import { speechEnhancementReferences } from './speech-enhancement-references.ts';\n"+s
    s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...speechEnhancementReferences,')
write(p,s)
backlinks={'objective-speech-evaluation':'降噪算法怎样在残余噪声、语音失真与实时约束之间取舍，见[语音增强与降噪](../speech-enhancement-and-noise-reduction/)。','hearing-aid':'数字降噪的估计原理、深度学习方法与实际聆听获益边界，详见[语音增强与降噪](../speech-enhancement-and-noise-reduction/)。','speech-intelligibility':'处理后的声音更安静为何未必更易懂，以及如何验证增强收益，见[语音增强与降噪](../speech-enhancement-and-noise-reduction/)。'}
for slug,line in backlinks.items():
    p=f'src/content/concepts/{slug}.md';s=read(p)
    if line not in s:
        at=s.index('\n## ');s=s[:at]+'\n'+line+'\n'+s[at:];s=re.sub(r'last_updated:.*','last_updated: "2026-11-06"',s,count=1)
    write(p,s)
p='src/data/relations.ts';s=read(p)
relations=[('spectrogram','时频表示连接噪声估计、掩蔽与分析合成。'),('phase-and-group-delay','复数相位决定频谱相加与波形重建。'),('microphone','阵列几何与传感器特性决定可利用的空间信息。'),('deep-learning','训练目标、数据与损失影响增强输出。'),('objective-speech-evaluation','音质与可懂度指标不能混为同一终点。'),('speech-intelligibility','算法获益需要独立行为验证。'),('hearing-aid','完整处理链、延迟与听者共同影响实际收益。'),('wide-dynamic-range-compression','压缩与降噪相互作用，应在完整处理链验证。')]
if "link('speech-enhancement-and-noise-reduction'" not in s:
    lines='\n'.join(f"  link('speech-enhancement-and-noise-reduction','{target}','related','{note}',3)," for target,note in relations)
    at=s.index('\n];\nexport function relationshipsFor');s=s[:at]+'\n'+lines+s[at:]
write(p,s)
p='src/data/paths.ts';s=read(p);line=next(l for l in s.splitlines() if "id:'technology'" in l)
if "'speech-enhancement-and-noise-reduction'" not in line:s=s.replace(line,line.replace("'objective-speech-evaluation',","'speech-enhancement-and-noise-reduction','objective-speech-evaluation',"))
write(p,s)
print('Registered',len(refs),'sources; three backlinks and eight relations.')
