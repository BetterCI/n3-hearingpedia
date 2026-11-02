"""Cache and identify the exact material used in the psychology course audit."""
from pathlib import Path
from urllib.request import build_opener,ProxyHandler,Request
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io,json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'artifacts/psychology/sources';REC=ROOT/'docs/research/psychology-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
ROWS=[]
def add(id,title,authors,url,supports,year='在线版；2026-11-02核对',kind='Noba_author_textbook',publication='Noba，专家署名教材模块',doi=None):
    r=dict(id='psych-'+id,title=title,authors=authors,url=url,supports=supports,year=year,kind=kind,publication=publication,access='fulltext')
    if doi:r['doi']=doi
    ROWS.append(r)
def n(id,slug,title,authors,supports):add(id,title,authors,'https://nobaproject.com/modules/'+slug,supports)
add('scope','What Is Psychology?','Rose M. Spielman, William J. Jenkins, Marilyn D. Lovett','https://openstax.org/books/psychology-2e/pages/1-1-what-is-psychology','心理与行为的科学研究、间接观察与学科范围；只用于定义和定位，未复用教材文字或插图。','2020；在线版2026-11-02核对','OpenStax_author_textbook','Psychology 2e，§1.1')
n('science','thinking-like-a-psychological-scientist','Thinking like a Psychological Scientist','Erin I. Smith','可检验问题、证据评估与科学推断；不把单次观察当成一般机制证明。')
n('design','research-designs','Research Designs','Christie Napa Scollon','操纵、相关、随机分派和纵向设计；正文不采用原页“相关只能研究两个变量”的错误泛化，也不把随机分派当实际样本必然完全平衡。')
n('measurement','personality-assessment','Personality Assessment','David Watson','标准化评分、自陈与他评、信度和效度证据；正文区分相关、绝对一致与分数用途。')
n('perception','sensation-and-perception','Sensation and Perception','Adam John Privitera','感觉与知觉、多模态和阈值概念；本文另明确任务猜测下限、准则与操作性阈值，未把50%用于所有任务。')
add('sdt','Calculation of signal detection theory measures','Harold Stanislaw, Natasha Todorov','https://www.jessicagrahn.com/uploads/6/0/8/5/6085172/stanislawtodorovdprim1999.pdf','读取等方差高斯是/否任务的d prime、c及极端比例处理；图与数字为另行原创计算。','1999','research_paper','Behavior Research Methods, Instruments, & Computers 31:137–149','10.3758/BF03207704')
add('psychometric','The psychometric function: I. Fitting, sampling, and goodness of fit','Felix A. Wichmann, N. Jeremy Hill','https://courses.washington.edu/matlab1/pdf/Wichmann_Hill_2001a.pdf','心理测量函数、猜测和失误、拟合及采样；本文明确lambda为上渐近线与1的差，而非自动等于全部随机失误概率。','2001','research_paper','Perception & Psychophysics 63:1293–1313','10.3758/BF03194544')
n('attention','attention','Attention','Frances Friedrich','选择、分配和持续注意；正文避免单一资源池和完全不加工无关注信息的绝对化。')
n('memory','memory-encoding-storage-retrieval','Memory (Encoding, Storage, Retrieval)','Kathleen B. McDermott, Henry L. Roediger III','编码、保持、提取、工作记忆、情景与语义记忆；图为过程示意及指定衰减模型，不是原实验数据。')
add('retrieval','Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention','Henry L. Roediger III, Jeffrey D. Karpicke','https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf','读取2006年两项散文学习实验；只支持所研究材料与延迟下的提取练习结果，不推广为所有学生和所有测试必然获益。','2006','research_paper','Psychological Science 17:249–255','10.1111/j.1467-9280.2006.01693.x')
n('learning','conditioning-and-learning','Conditioning and Learning','Mark E. Bouton','经典/操作性条件作用、强化与惩罚、消退和观察学习；不把重复、消退或奖励主观好坏混同。')
add('rw','A Theory of Pavlovian Conditioning: Variations in the Effectiveness of Reinforcement and Nonreinforcement','Robert A. Rescorla, Allan R. Wagner','https://bpb-us-w2.wpmucdn.com/about.illinoisstate.edu/dist/6/45/files/2021/01/RescorlaWagner.1972.pdf','原始联结强度更新、复合线索总预测误差与阻塞；正文将alpha乘beta并为教学有效速率，保留模型失配和并非生理电压的限制。','1972','original_theory','Classical Conditioning II, pp.64–99；大学课程存档')
n('decision','judgment-and-decision-making','Judgment and Decision Making','Max H. Bazerman','启发式、判断和决策及其任务背景；本文Bayes数字完全自定，不冒充行为实验。')
add('ddm','The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks','Roger Ratcliff, Gail McKoon','https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/','双选择扩散模型的漂移、边界、起点与非决策时间；本文取无跨试次变异的对称简化模型，公式和数值另作边值方程核验。','2008','research_paper','Neural Computation 20:873–922','10.1162/neco.2008.12-06-420')
n('emotion','functions-of-emotions','Functions of Emotions','Hyisung Hwang, David Matsumoto','情绪的个体、人际和文化功能；不由表情或单一生理指标唯一识别内心状态。')
n('motivation','motives-and-goals','Motives and Goals','Ayelet Fishbach, Maferima Touré-Tillery','目标、动机、目标冲突与行为；不把未完成任务归因为一个不可测的“意志力值”。')
n('development','research-methods-in-developmental-psychology','Research Methods in Developmental Psychology','Angela Lukowski, Helen Milojevich','儿童能力适配、横断和纵向的区别、队列及流失；不从年龄组差直接推出个体衰退或固定阶段。')
n('aging','aging','Aging','Tara Queen, Jacqui Smith','毕生发展、多种变化轨迹与个体差异；原创队列示例不是年龄常模。')
n('traits','personality-traits','Personality Traits','Edward Diener, Richard E. Lucas','人格特质、五因素维度与跨情境倾向；不把维度当互斥类型、命运或全部人格结构。')
n('social','an-introduction-to-the-science-of-social-psychology','An Introduction to the Science of Social Psychology','Robert Biswas-Diener','他人在场、社会情境与行为及研究方法；不复述争议经典实验为无条件定律。')
n('culture','culture','Culture','Robert Biswas-Diener, Neil Thin','文化意义、规范与样本的局限；区分组均值、个体归类与跨群体测量可比性。')
add('reverse','Can cognitive processes be inferred from neuroimaging data?','Russell A. Poldrack','https://brainmapping.org/NITP/PNA/Readings/Poldrack2006.pdf','读取反向推断的Bayes分析：脑区激活的选择性及先验不可省；不声称反向推断永远无效。','2006','research_paper','Trends in Cognitive Sciences 10:59–63','10.1016/j.tics.2005.12.004')
add('asa','American Statistical Association Releases Statement on Statistical Significance and P-Values','American Statistical Association','https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf','官方2016年发布说明，完整列出六原则；用于p值不等于假设为真概率、不等于效应量及不能只按阈值判断。','2016','official_statement','American Statistical Association，2016-03-07')
add('replication','Estimating the reproducibility of psychological science','Open Science Collaboration','https://pure.coventry.ac.uk/ws/files/3948863/Psychological%20science.pdf','读取100项、三个期刊及2008年研究的复制项目；正文只报告该抽样范围的36%显著性指标，不把它当全心理学真伪率。','2015','research_paper','Science 349:aac4716；Coventry大学作者存档','10.1126/science.aac4716')
add('ethics','Ethical Principles of Psychologists and Code of Conduct','American Psychological Association','https://www.apa.org/ethics/code','核对研究知情同意、可理解语言、退出、保密、欺骗与事后说明；作为专业伦理来源，不声称其等同于各地区法律或替代当地审查。','2017修订生效版；2026-11-02核对','official_code','APA，§8研究与发表、§9评估')
def get(url):
    op=build_opener(ProxyHandler({'https':'http://127.0.0.1:7897'}))
    with op.open(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:return r.read()
def fetch(row):
    excerpt=OUT/(row['id']+'.verified-excerpt.txt')
    if excerpt.exists():
        data=excerpt.read_bytes();text=data.decode('utf-8')
        assert len(text)>1000 and ('Total lines:' in text)
        assert ('criterion' in text.lower()) if row['id']=='psych-sdt' else ('8.02' in text and '8.07' in text)
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8')
        return dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),hash_target='saved web-tool text extraction; not original HTTP/PDF bytes',text_characters=len(text),checked_at='2026-11-02',reading_method='targeted source passages via web reader; direct HTTP unavailable')
    suffix='.pdf' if row['url'].lower().split('?')[0].endswith('.pdf') else '.html';path=OUT/(row['id']+suffix)
    try:
        data=path.read_bytes() if path.exists() else get(row['url']);path.write_bytes(data)
        if suffix=='.pdf':
            reader=PdfReader(io.BytesIO(data));text='\n'.join(p.extract_text() or '' for p in reader.pages);pages=len(reader.pages)
        else:
            soup=BeautifulSoup(data,'html.parser');main=soup.select_one('main') or soup.select_one('article') or soup
            for x in main.select('script,style,nav,header,footer'):x.decompose()
            text=main.get_text(' ',strip=True);pages=None
        # RW is an author-uploaded scan. Extracted cover text is not full chapter text.
        if row['id']=='psych-rw':
            assert pages==38 and 'Wagner' in text
        else:assert len(text)>1000,(row['id'],len(text))
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8')
        return dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(text),pdf_pages=pages,checked_at='2026-11-02',reading_method='scanned PDF; targeted pages visually inspected' if row['id']=='psych-rw' else 'text extraction; targeted passages read')
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','doi','url','access','supports']
    refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/psychology-references.ts').write_text("import type { Reference } from './references';\nexport const psychologyReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
