import type { Reference } from './references';
export const deepLearningReferences: Record<string, Reference> = {
  "dl-mlp": {
    "title": "Multilayer Perceptrons",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_multilayer-perceptrons/mlp.html",
    "access": "fulltext",
    "supports": "多层仿射变换、激活和表示；XOR小网络与参数计数另行构造，不将其视为深层必胜的证据。"
  },
  "dl-backprop": {
    "title": "Forward Propagation, Backward Propagation, and Computational Graphs",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_multilayer-perceptrons/backprop.html",
    "access": "fulltext",
    "supports": "计算图、链式法则和反向传播；本文采用批次为行的矩阵约定，平均损失梯度另作有限差分核对。"
  },
  "dl-init": {
    "title": "Numerical Stability and Initialization",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html",
    "access": "fulltext",
    "supports": "梯度消失/爆炸、对称性及Xavier缩放；He-ReLU二阶矩的简化推导另明确独立、对称与零偏置假设。"
  },
  "dl-sgd": {
    "title": "Minibatch Stochastic Gradient Descent",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_optimization/minibatch-sgd.html",
    "access": "fulltext",
    "supports": "批次、更新与学习率；正文区分epoch和step、均匀抽样的梯度估计与不保证全局最优。"
  },
  "dl-adam": {
    "title": "Adam",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_optimization/adam.html",
    "access": "fulltext",
    "supports": "一阶矩、二阶原始矩及偏差校正；不称二阶矩为Hessian或普遍全局收敛保证。"
  },
  "dl-dropout": {
    "title": "Dropout",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_multilayer-perceptrons/dropout.html",
    "access": "fulltext",
    "supports": "训练时随机失活与倒置缩放；均值保持不等于非线性全网络输出或集成预测精确相同。"
  },
  "dl-batchnorm": {
    "title": "Batch Normalization",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_convolutional-modern/batch-norm.html",
    "access": "fulltext",
    "supports": "按特征跨批次统计与训练/推理区别；未把所有归一化都称为仅因解决内部协变量偏移而有效。"
  },
  "dl-conv": {
    "title": "Convolutions for Images",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html",
    "access": "fulltext",
    "supports": "局部共享权重、互相关与数学卷积；本文一维步长、膨胀、因果左填充及感受野另作索引推导和计算。"
  },
  "dl-rnn": {
    "title": "Recurrent Neural Networks",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_recurrent-neural-networks/rnn.html",
    "access": "fulltext",
    "supports": "共享状态递推、参数与序列长度、循环模型的结构；状态不直接等于全部历史或生物记忆。"
  },
  "dl-lstm": {
    "title": "Long Short-Term Memory (LSTM)",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_recurrent-modern/lstm.html",
    "access": "fulltext",
    "supports": "门控、细胞状态和长依赖；不把门值当已观察的生理机制或声称完全消除梯度问题。"
  },
  "dl-attention": {
    "title": "Attention Scoring Functions",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html",
    "access": "fulltext",
    "supports": "查询键值、缩放点积及掩码归一化；正文另检查每行有效键、全部屏蔽与因果前端。"
  },
  "dl-transformer": {
    "title": "The Transformer Architecture",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html",
    "access": "fulltext",
    "supports": "多头、位置、前馈、残差和归一化；区分编码器、因果解码器及cross attention，不把单一注意力矩阵叫作完整Transformer。"
  },
  "dl-generalization": {
    "title": "Generalization in Deep Learning",
    "authors": "Aston Zhang; Zachary C. Lipton; Mu Li; Alexander J. Smola",
    "year": "2023；在线1.0.3，2026-11-02核对",
    "publication": "Dive into Deep Learning，作者官方在线教材",
    "url": "https://d2l.ai/chapter_multilayer-perceptrons/generalization-deep.html",
    "access": "fulltext",
    "supports": "深网络容量、训练与泛化边界；原创tanh回归例仅展示一批指定数据与优化轨迹，不宣称所有误差均为U形。"
  },
  "dl-resnet": {
    "title": "Deep Residual Learning for Image Recognition",
    "authors": "Kaiming He; Xiangyu Zhang; Shaoqing Ren; Jian Sun",
    "year": "2016",
    "publication": "CVPR 2016, pp.770–778",
    "doi": "10.1109/CVPR.2016.90",
    "url": "https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf",
    "access": "fulltext",
    "supports": "原始残差学习和恒等/投影捷径；正文的I加Jacobian与标量梯度比较为另行指定计算。"
  },
  "dl-he-init": {
    "title": "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification",
    "authors": "Kaiming He; Xiangyu Zhang; Shaoqing Ren; Jian Sun",
    "year": "2015",
    "publication": "ICCV 2015, pp.1026–1034",
    "doi": "10.1109/ICCV.2015.123",
    "url": "https://openaccess.thecvf.com/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf",
    "access": "fulltext",
    "supports": "读取ReLU/PReLU与前向/反向初始化尺度；正文He缩放仅在给定独立、对称和零偏置分析下保持二阶矩，不转述历史图像性能为当前结论。"
  },
  "dl-transformer-paper": {
    "title": "Attention Is All You Need",
    "authors": "Ashish Vaswani; Noam Shazeer; Niki Parmar; Jakob Uszkoreit; Llion Jones; Aidan N. Gomez; Łukasz Kaiser; Illia Polosukhin",
    "year": "2017",
    "publication": "Advances in Neural Information Processing Systems 30",
    "url": "https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf",
    "access": "fulltext",
    "supports": "读取原始Transformer、缩放点积与解码掩码；不引用其机器翻译实验作为当前语音性能排名。"
  },
  "dl-adamw": {
    "title": "Decoupled Weight Decay Regularization",
    "authors": "Ilya Loshchilov; Frank Hutter",
    "year": "2019",
    "publication": "ICLR 2019；作者开放稿",
    "url": "https://arxiv.org/pdf/1711.05101",
    "access": "fulltext",
    "supports": "权重衰减与L2在自适应优化器中不同；本文指定对角预条件一步反例说明代数差异，未当Adam完整轨迹。"
  },
  "dl-wav2vec": {
    "title": "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations",
    "authors": "Alexei Baevski; Henry Zhou; Abdelrahman Mohamed; Michael Auli",
    "year": "2020",
    "publication": "Advances in Neural Information Processing Systems 33",
    "url": "https://papers.nips.cc/paper/2020/file/92d1e1eb1cd6f9fba3227870bb6d7f07-Paper.pdf",
    "access": "fulltext",
    "supports": "读取潜在表示遮挡、量化对比目标与微调；区分原始模型的无转写预训练、带转写微调和其他变体。"
  },
  "dl-hubert": {
    "title": "HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units",
    "authors": "Wei-Ning Hsu; Benjamin Bolte; Yao-Hung Hubert Tsai; Kushal Lakhotia; Ruslan Salakhutdinov; Abdelrahman Mohamed",
    "year": "2021",
    "publication": "IEEE/ACM TASLP 29:3451–3460；作者开放稿",
    "doi": "10.1109/TASLP.2021.3122291",
    "url": "https://arxiv.org/pdf/2106.07447",
    "access": "fulltext",
    "supports": "读取聚类伪标签、遮挡预测与迭代目标；不把聚类标签直接当真实音素，不声称所有自监督方法都不使用任何标签。"
  },
  "dl-vae": {
    "title": "Auto-Encoding Variational Bayes",
    "authors": "Diederik P. Kingma; Max Welling",
    "year": "2014",
    "publication": "ICLR 2014；作者开放稿",
    "url": "https://arxiv.org/pdf/1312.6114",
    "access": "fulltext",
    "supports": "读取潜变量、变分下界与重参数化；正文只作生成学习定位，不把重建损失低等同语义正确或隐私保证。"
  },
  "dl-gan": {
    "title": "Generative Adversarial Nets",
    "authors": "Ian J. Goodfellow; Jean Pouget-Abadie; Mehdi Mirza; Bing Xu; David Warde-Farley; Sherjil Ozair; Aaron Courville; Yoshua Bengio",
    "year": "2014",
    "publication": "Advances in Neural Information Processing Systems 27",
    "url": "https://proceedings.nips.cc/paper_files/paper/2014/file/f033ed80deb0234979a61f95710dbe25-Paper.pdf",
    "access": "fulltext",
    "supports": "读取生成器和判别器的对抗训练；不把感知逼真等同输入事实保真。"
  },
  "dl-diffusion": {
    "title": "Denoising Diffusion Probabilistic Models",
    "authors": "Jonathan Ho; Ajay Jain; Pieter Abbeel",
    "year": "2020",
    "publication": "Advances in Neural Information Processing Systems 33；作者开放稿",
    "url": "https://arxiv.org/pdf/2006.11239",
    "access": "fulltext",
    "supports": "读取前向高斯链、alpha乘积边缘分布及反向学习；本篇只模拟前向加噪，不展示已训练去噪结果或声称加噪可唯一反演。"
  },
  "dl-ctc": {
    "title": "Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks",
    "authors": "Alex Graves; Santiago Fernández; Faustino Gomez; Jürgen Schmidhuber",
    "year": "2006",
    "publication": "ICML 2006, pp.369–376",
    "doi": "10.1145/1143844.1143891",
    "url": "https://www.cs.toronto.edu/~graves/icml_2006.pdf",
    "access": "fulltext",
    "supports": "读取空白、重复折叠、对齐路径求和与条件独立；本文三帧双符号例用穷举和动态规划另行核对。"
  },
  "dl-calibration": {
    "title": "On Calibration of Modern Neural Networks",
    "authors": "Chuan Guo; Geoff Pleiss; Yu Sun; Kilian Q. Weinberger",
    "year": "2017",
    "publication": "ICML 2017, PMLR70:1321–1330",
    "url": "https://proceedings.mlr.press/v70/guo17a/guo17a.pdf",
    "access": "fulltext",
    "supports": "读取置信度校准、温度缩放和独立验证集拟合；本文Bernoulli0.6算例是已知总体的精确风险，不冒充额外测试数据。"
  },
  "dl-ce-api": {
    "title": "CrossEntropyLoss",
    "authors": "PyTorch developers",
    "year": "2.15文档；2026-11-02核对",
    "publication": "PyTorch官方版本文档",
    "url": "https://docs.pytorch.org/docs/2.15/generated/torch.nn.CrossEntropyLoss.html",
    "access": "documentation",
    "supports": "核对类索引目标、未归一化logits、ignore_index和reduction语义；本文仅在未加权硬标签且忽略项不计分母的特例推导均值。"
  },
  "dl-ln-api": {
    "title": "LayerNorm",
    "authors": "PyTorch developers",
    "year": "2.15文档；2026-11-02核对",
    "publication": "PyTorch官方版本文档",
    "url": "https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html",
    "access": "documentation",
    "supports": "核对指定末维的归一化轴、epsilon及训练/推理均使用输入统计；不把所有网络的“层”任意作为统计轴。"
  },
  "dl-grad-api": {
    "title": "no_grad",
    "authors": "PyTorch developers",
    "year": "2.15文档；2026-11-02核对",
    "publication": "PyTorch官方版本文档",
    "url": "https://docs.pytorch.org/docs/2.15/generated/torch.no_grad.html",
    "access": "documentation",
    "supports": "核对关闭梯度记录不同于切换模块训练/推理状态；不宣称no_grad自动关闭Dropout或更新BatchNorm统计。"
  }
};
