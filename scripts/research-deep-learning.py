"""Cache scoped author textbook chapters, original papers and versioned official docs."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from pypdf import PdfReader
import subprocess,json,hashlib,io
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'artifacts/deep-learning/sources';REC=ROOT/'docs/research/deep-learning-2026-11-02'
for p in [OUT,REC]:p.mkdir(parents=True,exist_ok=True)
ROWS=[]
def add(id,title,authors,url,supports,year,publication,kind='original_paper',doi=None):
    row=dict(id='dl-'+id,title=title,authors=authors,url=url,supports=supports,year=year,publication=publication,kind=kind,access='fulltext')
    if doi:row['doi']=doi
    ROWS.append(row)
def book(id,title,path,supports):add(id,title,'Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola','https://d2l.ai/'+path+'.html',supports,'2023；在线1.0.3，2026-11-02核对','Dive into Deep Learning，作者官方在线教材','author_textbook')
book('mlp','Multilayer Perceptrons','chapter_multilayer-perceptrons/mlp','多层仿射变换、激活和表示；XOR小网络与参数计数另行构造，不将其视为深层必胜的证据。')
book('backprop','Forward Propagation, Backward Propagation, and Computational Graphs','chapter_multilayer-perceptrons/backprop','计算图、链式法则和反向传播；本文采用批次为行的矩阵约定，平均损失梯度另作有限差分核对。')
book('init','Numerical Stability and Initialization','chapter_multilayer-perceptrons/numerical-stability-and-init','梯度消失/爆炸、对称性及Xavier缩放；He-ReLU二阶矩的简化推导另明确独立、对称与零偏置假设。')
book('sgd','Minibatch Stochastic Gradient Descent','chapter_optimization/minibatch-sgd','批次、更新与学习率；正文区分epoch和step、均匀抽样的梯度估计与不保证全局最优。')
book('adam','Adam','chapter_optimization/adam','一阶矩、二阶原始矩及偏差校正；不称二阶矩为Hessian或普遍全局收敛保证。')
book('dropout','Dropout','chapter_multilayer-perceptrons/dropout','训练时随机失活与倒置缩放；均值保持不等于非线性全网络输出或集成预测精确相同。')
book('batchnorm','Batch Normalization','chapter_convolutional-modern/batch-norm','按特征跨批次统计与训练/推理区别；未把所有归一化都称为仅因解决内部协变量偏移而有效。')
book('conv','Convolutions for Images','chapter_convolutional-neural-networks/conv-layer','局部共享权重、互相关与数学卷积；本文一维步长、膨胀、因果左填充及感受野另作索引推导和计算。')
book('rnn','Recurrent Neural Networks','chapter_recurrent-neural-networks/rnn','共享状态递推、参数与序列长度、循环模型的结构；状态不直接等于全部历史或生物记忆。')
book('lstm','Long Short-Term Memory (LSTM)','chapter_recurrent-modern/lstm','门控、细胞状态和长依赖；不把门值当已观察的生理机制或声称完全消除梯度问题。')
book('attention','Attention Scoring Functions','chapter_attention-mechanisms-and-transformers/attention-scoring-functions','查询键值、缩放点积及掩码归一化；正文另检查每行有效键、全部屏蔽与因果前端。')
book('transformer','The Transformer Architecture','chapter_attention-mechanisms-and-transformers/transformer','多头、位置、前馈、残差和归一化；区分编码器、因果解码器及cross attention，不把单一注意力矩阵叫作完整Transformer。')
book('generalization','Generalization in Deep Learning','chapter_multilayer-perceptrons/generalization-deep','深网络容量、训练与泛化边界；原创tanh回归例仅展示一批指定数据与优化轨迹，不宣称所有误差均为U形。')
add('resnet','Deep Residual Learning for Image Recognition','Kaiming He; Xiangyu Zhang; Shaoqing Ren; Jian Sun','https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf','原始残差学习和恒等/投影捷径；正文的I加Jacobian与标量梯度比较为另行指定计算。','2016','CVPR 2016, pp.770–778',doi='10.1109/CVPR.2016.90')
add('he-init','Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification','Kaiming He; Xiangyu Zhang; Shaoqing Ren; Jian Sun','https://openaccess.thecvf.com/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf','读取ReLU/PReLU与前向/反向初始化尺度；正文He缩放仅在给定独立、对称和零偏置分析下保持二阶矩，不转述历史图像性能为当前结论。','2015','ICCV 2015, pp.1026–1034',doi='10.1109/ICCV.2015.123')
add('transformer-paper','Attention Is All You Need','Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez; Łukasz Kaiser; Illia Polosukhin','https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf','读取原始Transformer、缩放点积与解码掩码；不引用其机器翻译实验作为当前语音性能排名。','2017','Advances in Neural Information Processing Systems 30')
add('adamw','Decoupled Weight Decay Regularization','Ilya Loshchilov; Frank Hutter','https://arxiv.org/pdf/1711.05101','权重衰减与L2在自适应优化器中不同；本文指定对角预条件一步反例说明代数差异，未当Adam完整轨迹。','2019','ICLR 2019；作者开放稿')
add('wav2vec','wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations','Alexei Baevski; Henry Zhou; Abdelrahman Mohamed; Michael Auli','https://papers.nips.cc/paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf','读取潜在表示遮挡、量化对比目标与微调；区分原始模型的无转写预训练、带转写微调和其他变体。','2020','Advances in Neural Information Processing Systems 33')
add('hubert','HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units','Wei-Ning Hsu; Benjamin Bolte; Yao-Hung Hubert Tsai; Kushal Lakhotia; Ruslan Salakhutdinov; Abdelrahman Mohamed','https://arxiv.org/pdf/2106.07447','读取聚类伪标签、遮挡预测与迭代目标；不把聚类标签直接当真实音素，不声称所有自监督方法都不使用任何标签。','2021','IEEE/ACM TASLP 29:3451–3460；作者开放稿',doi='10.1109/TASLP.2021.3122291')
add('vae','Auto-Encoding Variational Bayes','Diederik P. Kingma; Max Welling','https://arxiv.org/pdf/1312.6114','读取潜变量、变分下界与重参数化；正文只作生成学习定位，不把重建损失低等同语义正确或隐私保证。','2014','ICLR 2014；作者开放稿')
add('gan','Generative Adversarial Nets','Ian J. Goodfellow; Jean Pouget-Abadie; Mehdi Mirza; Bing Xu; David Warde-Farley; Sherjil Ozair; Aaron Courville; Yoshua Bengio','https://proceedings.nips.cc/paper_files/paper/2014/file/f033ed80deb0234979a61f95710dbe25-Paper.pdf','读取生成器和判别器的对抗训练；不把感知逼真等同输入事实保真。','2014','Advances in Neural Information Processing Systems 27')
add('diffusion','Denoising Diffusion Probabilistic Models','Jonathan Ho; Ajay Jain; Pieter Abbeel','https://arxiv.org/pdf/2006.11239','读取前向高斯链、alpha乘积边缘分布及反向学习；本篇只模拟前向加噪，不展示已训练去噪结果或声称加噪可唯一反演。','2020','Advances in Neural Information Processing Systems 33；作者开放稿')
add('ctc','Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks','Alex Graves; Santiago Fernández; Faustino Gomez; Jürgen Schmidhuber','https://www.cs.toronto.edu/~graves/icml_2006.pdf','读取空白、重复折叠、对齐路径求和与条件独立；本文三帧双符号例用穷举和动态规划另行核对。','2006','ICML 2006, pp.369–376',doi='10.1145/1143844.1143891')
add('calibration','On Calibration of Modern Neural Networks','Chuan Guo; Geoff Pleiss; Yu Sun; Kilian Q. Weinberger','https://proceedings.mlr.press/v70/guo17a/guo17a.pdf','读取置信度校准、温度缩放和独立验证集拟合；本文Bernoulli0.6算例是已知总体的精确风险，不冒充额外测试数据。','2017','ICML 2017, PMLR70:1321–1330')
for id,name,support in [
('ce-api','CrossEntropyLoss','核对类索引目标、未归一化logits、ignore_index和reduction语义；本文仅在未加权硬标签且忽略项不计分母的特例推导均值。'),
('ln-api','LayerNorm','核对指定末维的归一化轴、epsilon及训练/推理均使用输入统计；不把所有网络的“层”任意作为统计轴。'),
('grad-api','no_grad','核对关闭梯度记录不同于切换模块训练/推理状态；不宣称no_grad自动关闭Dropout或更新BatchNorm统计。')]:
    add(id,name,'PyTorch developers','https://docs.pytorch.org/docs/2.15/generated/torch.'+('nn.' if id!='grad-api' else '')+name+'.html',support,'2.15文档；2026-11-02核对','PyTorch官方版本文档','official_documentation')
    ROWS[-1]['access']='documentation'
def fetch(row):
    # The CTC, arXiv and OpenReview URLs return PDF despite not ending in .pdf.
    pdf=row['kind']=='original_paper';suffix='.pdf' if pdf else '.html';path=OUT/(row['id']+suffix)
    try:
        if path.exists():data=path.read_bytes()
        else:
            result=subprocess.run(['curl.exe','-fLsS','--connect-timeout','12','--max-time','30','--proxy','http://127.0.0.1:7897',row['url']],capture_output=True,timeout=35)
            assert result.returncode==0,result.stderr.decode(errors='replace');data=result.stdout
            assert data[:4]==b'%PDF' if pdf else len(data)>1000
            path.write_bytes(data)
        if pdf:
            reader=PdfReader(io.BytesIO(data));pages=len(reader.pages)
            try:text='\n'.join(p.extract_text() or '' for p in reader.pages);method='pypdf text extraction'
            except Exception:
                target=OUT/(row['id']+'.txt')
                result=subprocess.run(['pdftotext','-layout',str(path),str(target)],capture_output=True,timeout=35)
                assert result.returncode==0,result.stderr.decode(errors='replace')
                text=target.read_text(encoding='utf-8');method='Poppler pdftotext; pypdf font decoding failed'
        else:
            soup=BeautifulSoup(data,'html.parser');main=soup.select_one('[role="main"]') or soup.select_one('article') or soup.select_one('main') or soup
            for el in main.select('script,style,nav'):el.decompose()
            text=main.get_text(' ',strip=True);pages=None;method='HTML main article text'
        assert len(text)>1500,(row['id'],len(text))
        (OUT/(row['id']+'.txt')).write_text(text,encoding='utf-8')
        return dict(**row,status='fetched',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(text),pdf_pages=pages,checked_at='2026-11-02',extraction_method=method)
    except Exception as e:return dict(**row,status='failed',error=str(e))
if __name__=='__main__':
    with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,ROWS))
    (REC/'source-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    keys=['title','authors','year','publication','doi','url','access','supports'];refs={r['id']:{k:r[k] for k in keys if k in r} for r in rows}
    (ROOT/'src/data/deep-learning-references.ts').write_text("import type { Reference } from './references';\nexport const deepLearningReferences: Record<string, Reference> = "+json.dumps(refs,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    print(json.dumps(dict(total=len(rows),fetched=sum(r['status']=='fetched' for r in rows),failures=[dict(id=r['id'],error=r['error']) for r in rows if r['status']!='fetched'])))
