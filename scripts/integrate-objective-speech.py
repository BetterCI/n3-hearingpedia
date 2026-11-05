"""Register reviewed source descriptions and narrow, intentional cross-links."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8')
refs={}
def ref(key,title,authors,year,publication,url,access,supports,doi=None):
    refs[key]=dict(title=title,authors=authors,year=year,publication=publication,url=url,access=access,supports='2026-11-06：'+supports)
    if doi:refs[key]['doi']=doi
ref('ose-p800','Methods for subjective determination of transmission quality','ITU-T','1996','Recommendation ITU-T P.800','https://www.itu.int/rec/T-REC-P.800/en','documentation','官方目录确认现行条目；MOS定义与主观评分说明亦结合NISQA原文引言。未声称执行完整标准实验。')
ref('ose-p835','Subjective test methodology for evaluating speech communication systems and terminals providing noise suppression functionality','ITU-T','2026','Recommendation ITU-T P.835 (07/2026)','https://www.itu.int/rec/T-REC-P.835-202607-I/en','documentation','官方目录与公开Summary：2026-07-29批准，SIG/BAK/OVRL三维评价及适用配置；未访问受限标准正文。2022年DNSMOS使用当时框架，不冒称采用2026修订。')
ref('ose-vankuyk-2018','An Evaluation of Intrusive Instrumental Intelligibility Metrics','Steven Van Kuyk; W. Bastiaan Kleijn; Richard C. Hendriks','2018','IEEE/ACM Transactions on Audio, Speech, and Language Processing, 26(11), 2153–2166','https://pure.tudelft.nl/ws/portalfiles/portal/50160817/An_Evaluation_of_Intrusive_Instrumental_Intelligibility_Metrics.pdf','fulltext','作者机构接收稿Abstract与Introduction、正式书目；支持12种指标、跨失真泛化与开发数据接触的限制。不将旧版本排名推广到当前所有模型。','10.1109/TASLP.2018.2856374')
ref('ose-hasqi-2014','The Hearing-Aid Speech Quality Index (HASQI) Version 2','James M. Kates; Kathryn H. Arehart','2014','Journal of the Audio Engineering Society, 62(3), 99–117','https://aes.org/publications/elibrary/elibrary-page/?id=17126','abstract','出版方摘要与Crossref：外周听损模型、包络／精细结构及长期谱成分，线性与非线性项相乘。未复现模型。','10.17743/jaes.2014.0006')
ref('ose-kates-overview','An overview of the HASPI and HASQI metrics for predicting speech intelligibility and speech quality for normal hearing, hearing loss, and hearing aids','James M. Kates; Kathryn H. Arehart','2022','Hearing Research, 426, 108608','https://pmc.ncbi.nlm.nih.gov/articles/PMC10833438/','fulltext','作者方法综述；通过出版社及PMC可检索正文读取Introduction、3.1、3.2、5.7、5.8与Conclusions段落，支持不同参考模型、声级／听力及个体推广边界。PMC直接页遇验证页，全文XML请求失败；未取得完整本地全文。','10.1016/j.heares.2022.108608')
ref('ose-p862','Perceptual evaluation of speech quality (PESQ): An objective method for end-to-end speech quality assessment of narrow-band telephone networks and speech codecs','ITU-T','2001（2024撤销）','Recommendation ITU-T P.862','https://www.itu.int/rec/T-REC-P.862/en','documentation','官方条目明确P.862/1/2/3在2024-01-05撤销；支持历史标准身份及版本区分，不宣称本次执行标准参考实现。')
ref('ose-p863','Perceptual objective listening quality prediction','ITU-T','2018（含2020修订条目）','Recommendation ITU-T P.863','https://www.itu.int/rec/T-REC-P.863/en','documentation','官方现行目录与2018版Summary：预测ACR听音质量、窄带与全带模式、20 kHz全带上限及一致性检查；未读取全部算法附件。')
ref('ose-dnsmos-2022','DNSMOS P.835: A Non-Intrusive Perceptual Objective Speech Quality Metric to Evaluate Noise Suppressors','Chandan K. A. Reddy; Vishak Gopal; Ross Cutler','2022','ICASSP 2022, 886–890','https://arxiv.org/abs/2110.01763','fulltext','作者论文PDF摘要、引言及相关方法；模型学习P.835的SIG/BAK/OVRL人类评分。Crossref核对正式会议版本；官方GitHub补充实现入口，不作为行为获益证明。','10.1109/ICASSP43922.2022.9746108')
ref('ose-nisqa-2021','NISQA: A Deep CNN-Self-Attention Model for Multidimensional Speech Quality Prediction with Crowdsourced Datasets','Gabriel Mittag; Babak Naderi; Assmaa Chehadi; Sebastian Möller','2021','Interspeech 2021, 2127–2131','https://www.isca-archive.org/interspeech_2021/mittag21_interspeech.html','fulltext','ISCA论文PDF摘要与引言／模型说明：通信领域、总体质量与四个维度；不把特定数据集验证推广为普适。','10.21437/Interspeech.2021-299')
ref('ose-sisdr-2019','SDR – Half-Baked or Well Done?','Jonathan Le Roux; Scott Wisdom; Hakan Erdogan; John R. Hershey','2019','ICASSP 2019, 626–630','https://www.merl.com/publications/TR2019-013','fulltext','作者机构论文第2节特别是2.3及式4–5；投影定义与尺度边界。本文用独立正交正弦信号教学计算，不冒称感知实验。','10.1109/ICASSP.2019.8683855')
ref('ose-p808','Subjective evaluation of speech quality with a crowdsourcing approach','ITU-T','2021','Recommendation ITU-T P.808 (06/2021)','https://www.itu.int/rec/T-REC-P.808/en','documentation','官方现行目录和公开方法范围；支持众包语音评分方法身份，不宣称本次执行了标准或阅读全部规范。')
ref('ose-voicemos-2024','The VoiceMOS Challenge 2024: Beyond Speech Quality Prediction','Wen-Chin Huang; Szu-Wei Fu; Erica Cooper; Ryandhimas E. Zezario; Tomoki Toda; Hsin-Min Wang; Junichi Yamagishi; Yu Tsao','2024','IEEE Spoken Language Technology Workshop (SLT), 803–810','https://arxiv.org/abs/2409.07001','fulltext','作者机构PDF摘要、引言与赛道说明；高质量合成、歌声与少标签增强语音是不同域。按正式会议年记2024，未把所有系统称为通用MOS模型。','10.1109/SLT61566.2024.10832295')
ref('ose-fuse-2025','FUSE: Universal Speech Enhancement using Multi-Stage Fusion of Sparse Compression and Token Generation Models for the URGENT 2025 Challenge','Nabarun Goswami; Tatsuya Harada','2025','Interspeech 2025, 883–887','https://www.isca-archive.org/interspeech_2025/goswami25_interspeech.html','fulltext','ISCA官方摘要及论文Table 1/2和结论段；生成阶段感知指标与SDR的权衡是特定系统结果，不概括为波形下降总是无害。','10.21437/Interspeech.2025-251')
write('src/data/objective-speech-evaluation-references.ts',"import type { Reference } from './references';\n\nexport const objectiveSpeechEvaluationReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n')
p='src/data/references.ts';s=read(p)
if 'import { objectiveSpeechEvaluationReferences }' not in s:
    s="import { objectiveSpeechEvaluationReferences } from './objective-speech-evaluation-references.ts';\n"+s
    s=s.replace('export const references: Record<string, Reference> = {','export const references: Record<string, Reference> = {\n  ...objectiveSpeechEvaluationReferences,')
write(p,s)
# Upgrade only the source actually read in greater depth this turn.
p='src/data/speech-intelligibility-references.ts';s=read(p)
a=s.index('  "taal-2011":');b=s.index('  "jensen-2016":',a)
part=s[a:b].replace('"access": "abstract"','"access": "fulltext"').replace('"url": "https://doi.org/10.1109/TASL.2011.2114881"','"url": "https://ceestaal.nl/Taal%282011%29.pdf"')
part=re.sub(r'"supports": "[^"]*"','"supports": "2026-11-06：作者网站论文PDF第II节及式1–6，核对分帧、三分之一倍频程、静音剔除、能量归一化、截断及相关；STOI为指数，不是未经标定的正确率。"',part)
s=s[:a]+part+s[b:];write(p,s)
backlinks={'speech-intelligibility':'关于预测分数、参考条件、音质模型与跨材料验证，见[客观语音可懂度与音质评价](../objective-speech-evaluation/)。',
'wide-dynamic-range-compression':'压缩处理的算法评价还需区分识别预测、音质与波形误差，详见[客观语音可懂度与音质评价](../objective-speech-evaluation/)。',
'auditory-computational-models':'用于预测识别与听感的模型及其验证边界，见[客观语音可懂度与音质评价](../objective-speech-evaluation/)。'}
for slug,line in backlinks.items():
    p=f'src/content/concepts/{slug}.md';s=read(p)
    if line not in s:
        at=s.index('\n## ');s=s[:at]+'\n'+line+'\n'+s[at:]
        s=re.sub(r'last_updated:.*', 'last_updated: "2026-11-06"',s,count=1)
    write(p,s)
p='src/data/relations.ts';s=read(p)
relations=[('speech-intelligibility','related','客观预测必须对应明确的行为评分目标。'),('temporal-envelope','related','STOI与听觉模型以短时包络或调制特征描述语音。'),('auditory-computational-models','related','听觉前端与经验映射共同限定预测范围。'),('wide-dynamic-range-compression','related','压缩需要分别评价可听度、识别与音质。'),('audiometric-calibration','related','听损模型必须明确数字幅度、声级与听力阈值。'),('psychometric-function','related','指数到正确率的映射应独立标定与验证。'),('listening-effort','related','可懂度及音质预测不自动代表努力变化。'),('speech-reception-threshold','related','客观指数不能未经标定转换为行为阈值。')]
if "link('objective-speech-evaluation'" not in s:
    lines='\n'.join(f"  link('objective-speech-evaluation','{target}','{typ}','{note}',3)," for target,typ,note in relations)
    at=s.index('\n];\nexport function relationshipsFor');s=s[:at]+'\n'+lines+s[at:]
write(p,s)
p='src/data/paths.ts';s=read(p)
line=next(l for l in s.splitlines() if "id:'technology'" in l)
if "'objective-speech-evaluation'" not in line:s=s.replace(line,line.replace("'real-ear-measurement',","'real-ear-measurement','objective-speech-evaluation',"))
write(p,s)
print('Registered',len(refs),'new references; updated STOI access; added three backlinks and eight relations.')
