"""Register actual source access scopes for the illusion entry."""
from pathlib import Path
import json,re,html,urllib.request,urllib.parse
ROOT=Path(__file__).resolve().parents[1];DOC=ROOT/'docs/research/auditory-illusion-2026-10-10'
rows=json.loads((DOC/'verified-metadata.json').read_text(encoding='utf-8'))
notes={
'ai-riecke':'原始摘要：人类fMRI与知觉连续性、相同刺激不同报告的响应联系；不是完整声学波形重建证明。',
'ai-petkov':'原始摘要：清醒猕猴A1单元、被噪声替换的纯音及外周模拟对照；物种与单元层次保留。',
'ai-warren':'原始摘要：删除语音片段由外来声音替代，与静音缺口对照；用于音素恢复的经典发现。',
'ai-leonard':'原始摘要及Nature/PMC相关原文：临床植入电极人类皮层记录、声学语音层恢复及额叶先行活动；不称为所有区域的统一机制。',
'ai-shepard':'Crossref原始摘要：计算机合成复合音、相对音高循环与接近原则；教学合成参数为本站设定。',
'ai-scale':'Crossref原始摘要：上行/下行C大调音阶交替换耳，按频率范围分组、多种知觉与利手关联；不写成所有人固定左右模式。',
'ai-octave':'Nature原始论文公开摘要：400/800Hz、250ms、等幅双耳相反交换；具体知觉与后续理论据其他来源。',
'ai-chambers':'PubMed原始摘要与Crossref书目：四项实验提出双耳融合与双听解释，反对简单抑制模型；保留争议。',
'ai-deutsch-reply':'原始摘要：批评前研究程序并报告新实验，支持八度差与两通路解释；不宣称争论已终结。',
'ai-tritone':'出版方及Crossref原始摘要：不同调与听者的方向差异；构造和示例另据作者官方页。',
'ai-song':'原始摘要：原样重复、移调与打乱对照；主观歌唱感与模仿音高分别测量。',
'ai-language':'原始摘要及PMC相关段：20名多语言年轻成人、母语类别与理解程度和效应关联；不把声调语言刺激本身与听者母语混同。',
'ai-mcgurk':'Nature公开原始摘要：听觉ba与视觉ga产生da报告、反向配对与单模态对照；不是普遍恒定融合公式。',
'ai-mcgurk-limit':'原始摘要：同听者McGurk与噪声句子视听收益未显示关联；任务不能直接替代。',
'ai-bistability':'原始摘要：不变输入下听觉声流组织交替、视觉比较与个体偏差；动态测量，不把一次报告当作固定分类。',
'ai-ci':'原始摘要：真实CI使用者与正常听力/8通道声码器比较，连续性与识别获益分测；特定条件可恢复，不等同正常听者。',
'ai-song-2025':'原始摘要：诱发与不诱发短语、首次/第八次歌唱感与模仿表现；印刷年2025、DOI含2024，不以重复次数当普遍阈值。',
'ai-bird-2025':'原始摘要及Nature相关检索可见原文：麻醉斑胸草雀同种歌声、上下文改变、单元群体恢复；没有清醒知觉自述。'}
bib={};abstracts=[]
for r in rows:
 c=r.get('crossref') or {};e=r.get('europe_pmc') or {}
 if not c.get('title'):
  try:
   with urllib.request.urlopen('https://api.crossref.org/works/'+urllib.parse.quote(r['doi'],safe=''),timeout=20) as response:c=json.load(response)['message']
   r['crossref']={k:c.get(k) for k in ['title','author','container-title','published','published-print','volume','issue','page','URL','type','abstract']};r['metadata_retry_succeeded']=True
  except Exception:pass
 title=(c.get('title') or [e.get('title')])[0];assert title,r['id']
 authors='; '.join(' '.join(filter(None,[a.get('given'),a.get('family')])) for a in c.get('author') or []) or e.get('authorString','')
 date=c.get('published-print') or c.get('published') or {};year=str(date.get('date-parts',[[int(e.get('pubYear','2000'))]])[0][0])
 if r['id']=='ai-song-2025':year='2025'
 if r['id']=='ai-ci':year='2014'
 if r['id']=='ai-mcgurk-limit':year='2017'
 pub=', '.join(str(v) for v in [(c.get('container-title') or [e.get('journalInfo',{}).get('journal',{}).get('title','')])[0],c.get('volume'),c.get('issue'),c.get('page')] if v)
 access='fulltext' if r['id']=='ai-language' else 'abstract'
 bib[r['id']]=dict(title=html.unescape(title),authors=html.unescape(authors),year=year,publication=html.unescape(pub),doi=r['doi'],url='https://doi.org/'+r['doi'],access=access,supports='2026-10-10：'+notes[r['id']])
 ab=e.get('abstractText') or c.get('abstract') or ''
 abstracts.append({'id':r['id'],'abstract':html.unescape(re.sub('<[^>]+>','',ab)),'scope':notes[r['id']]})
docs=[
('ai-overview','Auditory Illusions','Diana Deutsch','Encyclopedia of Perception, 2009, author manuscript','https://deutsch.ucsd.edu/pdf/Enc_Perception_Vol1_2009_160-164.pdf','作者百科原稿：错觉的输入—知觉区别与经典类型；用于导论，结果优先对应原始研究。'),
('ai-scale-doc','Scale Illusion','Diana Deutsch','UC San Diego author research and sound demonstrations','https://deutsch.ucsd.edu/psychology/pages.php?i=203','作者页与演示入口：交替换耳及多种组织；链接原演示，不转载其图或录音。'),
('ai-tritone-doc','Tritone Paradox','Diana Deutsch','UC San Diego author research and sound demonstrations','https://deutsch.ucsd.edu/psychology/pages.php?i=206','作者页：八度相关分量、三全音对、语言经验与方向差异，演示需要实听而非文本断言。'),
('ai-song-doc','Speech-to-Song Illusion','Diana Deutsch','UC San Diego author research and sound demonstrations','https://deutsch.ucsd.edu/psychology/pages.php?i=212','作者发现回顾、原样/移调对照与录音演示；原音频和图不下载转载。'),
('ai-octave-doc','Octave Illusion','Diana Deutsch','UC San Diego author research and sound demonstrations','https://deutsch.ucsd.edu/psychology/pages.php?i=202','作者页：多种知觉、耳机交换与提出的what/where解释；与反对观点并列，不把作者模型视为定论。')]
for key,title,authors,pub,url,note in docs:bib[key]=dict(title=title,authors=authors,year='2009' if key=='ai-overview' else '核对2026-10-10',publication=pub,url=url,access='documentation',supports='2026-10-10：'+note)
assert len(bib)==23
(ROOT/'src/data/auditory-illusion-references.ts').write_text("import type { Reference } from './references';\n\nexport const auditoryIllusionReferences: Record<string, Reference> = "+json.dumps(bib,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
(DOC/'abstracts-read.jsonl').write_text('\n'.join(json.dumps(a,ensure_ascii=False) for a in abstracts)+'\n',encoding='utf-8')
(DOC/'verified-metadata.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'references':len(bib),'original_doi_records':len(rows)}))
