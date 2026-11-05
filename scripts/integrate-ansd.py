"""Register verified ANSD references and narrowly scoped navigation changes."""
from pathlib import Path
import json,re,html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/research/auditory-neuropathy-spectrum-disorder-2026-11-06'
records={r['doi'].lower():r for r in json.loads((OUT/'bibliographic-check.json').read_text(encoding='utf-8'))}
refs={}
def paper(key,doi,url,access,supports,year=None):
    r=records[doi.lower()];assert r['status']==200
    authors=[' '.join([a.get('given',''),a.get('family',a.get('name',''))]).strip() for a in r['author']]
    if len(authors)>8:authors=authors[:3]+['et al.']
    refs[key]={'title':r['title'][0],'authors':'; '.join(authors),'year':year or str(r['published']['date-parts'][0][0]),
      'publication':f"{html.unescape(r['container-title'][0])}, {r['volume']}"+(f"({r['issue']})" if r.get('issue') else '')+f", {r['page']}",
      'doi':doi,'url':url,'access':access,'supports':'2026-11-06：'+supports}
def doc(key,title,authors,url,supports,year='2019'):
    refs[key]={'title':title,'authors':authors,'year':year,'publication':'官方专业指南／监管文件','url':url,'access':'documentation','supports':'2026-11-06：'+supports}
paper('ansd-rance-1999','10.1097/00003446-199906000-00006','https://pubmed.ncbi.nlm.nih.gov/10386850/','abstract','原始摘要：20例临床资料，行为阈值从正常至极重度、言语辨别及放大获益个体差异；风险样本的患病比例不外推至总体。')
paper('ansd-desiati-2020','10.3390/jcm9041074','https://pmc.ncbi.nlm.nih.gov/articles/PMC7230308/','fulltext','PMC／Europe PMC开放全文综述及病例相关段落：ANSD异质性、受体与神经测量、突触病变概念及管理边界；用作术语和机制背景，不替代原始临床研究。')
paper('ansd-gcan-2026','10.1002/wjo2.70003','https://onlinelibrary.wiley.com/doi/10.1002/wjo2.70003','fulltext','出版方正文第2、4及管理章节：中文临床命名、病因及综合评估。在线发表2025-05-21，2026年卷期；不照搬固定胆红素阈值，不把约2岁植入表述泛化为所有儿童等待线。','2026（在线2025）')
paper('ansd-santarelli-2015','10.1093/brain/awu378','https://pmc.ncbi.nlm.nih.gov/articles/PMC4339771/','fulltext','PMC摘要、方法、结果及讨论：OPA1错义变异相关末端树突病变解释及植入后获益；不是所有突触后ANSD均无效，也不承诺全部OPA1病例获益。')
paper('ansd-buchman-2006','10.1097/01.aud.0000224100.30525.ab','https://pubmed.ncbi.nlm.nih.gov/16825889/','abstract','PubMed摘要：具有AN特征的儿童可伴耳蜗神经发育不足；支持影像评估，未沿用旧文对影像神经缺如的一刀切治疗结论。')
paper('ansd-zeng-2006','10.1044/1092-4388(2006/029)','https://pubmed.ncbi.nlm.nih.gov/16671850/','abstract','原始摘要：13名AN参与者、其中7名植入，清晰语音及安静／噪声实验；不把样本优势幅度当个人预后。')
paper('ansd-rance-barker-2009','10.1080/14992020802665959','https://pubmed.ncbi.nlm.nih.gov/19925339/','abstract','原始摘要：10名植入AN/AD儿童与其他植入儿童及长期助听器使用者比较；非随机分组，支持个体化选择。')
paper('ansd-birman-2016','10.1097/MAO.0000000000000997','https://pubmed.ncbi.nlm.nih.gov/27050647/','abstract','原始摘要：50名耳蜗神经缺如／发育不足植入者的回顾性研究；影像与发育因素影响沟通结局，耳数和人数不同。')
paper('ansd-jiang-2026','10.1038/s41586-026-10393-y','https://pubmed.ncbi.nlm.nih.gov/42020731/','abstract','PubMed原始摘要和出版方可检索图注：8中心42人，0.8–32.3岁，最长2.5年；不是所有人完成2.5年。AAV1-hOTOF单臂研究，不与DB-OTO混为同一产品。')
paper('ansd-dboto-2026','10.1056/NEJMoa2400521','https://pubmed.ncbi.nlm.nih.gov/41085057/','abstract','原始摘要：DB-OTO开放标签单组研究、24周行为听阈主要终点；与FDA标签数据截止和人数分别处理，不推导随机比较结论。')
paper('ansd-lv-2024','10.1016/S0140-6736(23)02874-X','https://pubmed.ncbi.nlm.nih.gov/38280389/','abstract','出版PDF首页摘要及方法入口：6名儿童单臂早期研究，5名听力恢复；不等同于永久治愈或所有ANSD适用。')
doc('ansd-bsa-2019','Assessment and Management of Auditory Neuropathy Spectrum Disorder (ANSD) in Young Infants','British Society of Audiology','https://www.thebsa.org.uk/wp-content/uploads/2023/10/OD104-85-Recommended-Procedure-Assessment-and-Management-of-ANSD-in-Young-Infants.pdf','已读取官方45页PDF的第7–14、19–22页相关段落：诊断组合、OAE变化、行为验配与随访／转诊。虽复审日期为2024，核查时仍列于官方Current Guidance。')
doc('ansd-bsa-cm-2019','Recommended Procedure: Cochlear Microphonic Testing','British Society of Audiology','https://www.thebsa.org.uk/wp-content/uploads/2023/10/OD104-87-Recommended-Procedure-for-Cochlear-Microphonic-Testing.pdf','官方测试规程：极性翻转、插入换能器与声管阻断伪迹控制；教学图参数自设，不是诊断刺激协议或临床CM数据。')
doc('ansd-fda-2026','OTARMENI: product information and approval documents','U.S. Food and Drug Administration','https://www.fda.gov/vaccines-blood-biologics/otarmeni','官方产品页及2026-04-23批准文件入口：OTOF双等位变异、外毛细胞功能、同耳无既往人工耳蜗等适应证条件；限美国监管状态。','2026')
doc('ansd-otarmeni-label-2026','OTARMENI (lunsotogene parvec-cwha): Prescribing Information','U.S. Food and Drug Administration; Regeneron Pharmaceuticals','https://www.fda.gov/media/192098/download','标签第1及14节：加速批准、24周PTA、20名疗效分析16名达标、双耳治疗按较好耳；区分≤70 dB HL与正常听力，长期临床获益待验证。','2026')
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8')
write('src/data/auditory-neuropathy-spectrum-disorder-references.ts',"import type { Reference } from './references';\n\nexport const auditoryNeuropathyReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n')
p='src/data/references.ts';s=read(p)
if 'import { auditoryNeuropathyReferences }' not in s:
    s="import { auditoryNeuropathyReferences } from './auditory-neuropathy-spectrum-disorder-references.ts';\n"+s
    s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...auditoryNeuropathyReferences,')
write(p,s)
backlinks={'hearing-loss':'受体活动与神经反应不匹配时的诊断、病因及干预边界，见[听觉神经病谱系障碍（ANSD）](../auditory-neuropathy-spectrum-disorder/)。',
'otoacoustic-emissions':'OAE保留或后续消失时如何结合CM、ABR和功能评价，详见[听觉神经病谱系障碍（ANSD）](../auditory-neuropathy-spectrum-disorder/)。',
'auditory-brainstem-response':'ABR缺失而受体活动保留的证据组合、伪迹控制及干预解释，详见[听觉神经病谱系障碍（ANSD）](../auditory-neuropathy-spectrum-disorder/)。'}
for slug,line in backlinks.items():
    p=f'src/content/concepts/{slug}.md';s=read(p)
    if line not in s:
        at=s.index('\n## ');s=s[:at]+'\n'+line+'\n'+s[at:]
        s=re.sub(r'last_updated:.*','last_updated: "2026-11-06"',s,count=1)
    write(p,s)
p='src/data/relations.ts';s=read(p)
relations=[('hearing-loss','生理表型不能由听力损失程度单独描述。'),('otoacoustic-emissions','保留的耳蜗声学活动不等于神经传递完整。'),('auditory-brainstem-response','ABR严重异常需结合CM或OAE及伪迹控制。'),('inner-hair-cell','OTOF等突触前病因连接受体活动与递质释放。'),('cochlear-synaptopathy','突触机制与ANSD临床表型不能直接等同。'),('speech-intelligibility','听阈、言语理解及语言发展需要分层评价。'),('hearing-aid','可听度改善和交流获益应分别验证。'),('cochlear-implant','病变部位及残存神经功能影响电刺激获益。')]
if "link('auditory-neuropathy-spectrum-disorder'" not in s:
    lines='\n'.join(f"  link('auditory-neuropathy-spectrum-disorder','{target}','related','{note}',3)," for target,note in relations)
    at=s.index('\n];\nexport function relationshipsFor');s=s[:at]+'\n'+lines+s[at:]
write(p,s)
p='src/data/paths.ts';s=read(p);line=next(l for l in s.splitlines() if "id:'measurement'" in l)
if "'auditory-neuropathy-spectrum-disorder'" not in line:s=s.replace(line,line.replace("'auditory-brainstem-response',","'auditory-brainstem-response','auditory-neuropathy-spectrum-disorder',"))
write(p,s)
print('Registered',len(refs),'sources; added three backlinks and eight relations.')
