import type { Reference } from './references';

export const cochleaReferences: Record<string, Reference> = {
  "nidcd-hearing-2022": {
    "title": "How Do We Hear?",
    "authors": "National Institute on Deafness and Other Communication Disorders",
    "year": "2022",
    "publication": "NIDCD 官方科普资料",
    "url": "https://www.nidcd.nih.gov/health/how-do-we-hear",
    "access": "documentation",
    "supports": "核对NIDCD官方听觉过程资料，用于声输入到耳蜗和神经输出的基础描述。"
  },
  "wangemann-homeostasis-2006": {
    "title": "Supporting sensory transduction: cochlear fluid homeostasis and the endocochlear potential",
    "authors": "Wangemann, Philine",
    "year": "2006",
    "publication": "The Journal of Physiology, 576, (1), 11-21",
    "doi": "10.1113/jphysiol.2006.112888",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1995626/",
    "access": "fulltext",
    "supports": "核对公开原文的液体空间、血管纹与耳蜗内电位相关段落；完整钾循环路径不能按无分支闭环描述。"
  },
  "fettiplace-hair-cell-2017": {
    "title": "Hair Cell Transduction, Tuning, and Synaptic Transmission in the Mammalian Cochlea",
    "authors": "Fettiplace, Robert",
    "year": "2017",
    "publication": "Comprehensive Physiology, 7(4), 1197–1227",
    "doi": "10.1002/cphy.c160049",
    "url": "https://pubmed.ncbi.nlm.nih.gov/28915323/",
    "access": "abstract",
    "supports": "核对原论文摘要和公开片段，用于细胞机制框架；不声称本轮重新全文通读。"
  },
  "openstax-cochlea-2016": {
    "title": "Cross Section of the Cochlea",
    "authors": "OpenStax",
    "year": "2016",
    "publication": "Anatomy and Physiology；第二版第14.1节图14.7亦收录该图",
    "url": "https://openstax.org/books/anatomy-and-physiology-2e/pages/14-1-sensory-perception",
    "access": "documentation",
    "supports": "核对OpenStax教材图、官方图像资源及Wikimedia Commons许可记录；CC BY 4.0，保留原标注。"
  },
  "ren-cochlear-vibration-2016": {
    "title": "Reticular lamina and basilar membrane vibrations in living mouse cochleae",
    "authors": "Ren, Tianying; He, Wenxuan; Kemp, David",
    "year": "2016",
    "publication": "Proceedings of the National Academy of Sciences, 113, (35), 9910-9915",
    "doi": "10.1073/pnas.1607428113",
    "url": "https://pubmed.ncbi.nlm.nih.gov/27516544/",
    "access": "abstract",
    "supports": "核对活体小鼠原论文摘要与图注；网状板、基底膜的幅度和相位不同，不推断所有人耳的固定参数。"
  },
  "pan-tmc1-2018": {
    "title": "TMC1 Forms the Pore of Mechanosensory Transduction Channels in Vertebrate Inner Ear Hair Cells",
    "authors": "Pan, Bifeng; Akyuz, Nurunisa; Liu, Xiao-Ping; Asai, Yukako; Nist-Lund, Carl; Kurima, Kiyoto; Derfler, Bruce H.; György, Bence; Limapichat, Walrati; Walujkar, Sanket; Wimalasena, Lahiru N.; Sotomayor, Marcos; Corey, David P.; Holt, Jeffrey R.",
    "year": "2018",
    "publication": "Neuron, 99, (4), 736-753.e6",
    "doi": "10.1016/j.neuron.2018.07.033",
    "url": "https://pubmed.ncbi.nlm.nih.gov/30138589/",
    "access": "abstract",
    "supports": "核对原论文摘要和公开图注；TMC1为孔道重要组分，不将其表述为整个转导装置唯一蛋白。"
  },
  "brandt-cav13-2003": {
    "title": "CaV1.3 Channels Are Essential for Development and Presynaptic Activity of Cochlear Inner Hair Cells",
    "authors": "Brandt, Andreas; Striessnig, Joerg; Moser, Tobias",
    "year": "2003",
    "publication": "The Journal of Neuroscience, 23, (34), 10832-10840",
    "doi": "10.1523/JNEUROSCI.23-34-10832.2003",
    "url": "https://pubmed.ncbi.nlm.nih.gov/14645476/",
    "access": "abstract",
    "supports": "核对原论文摘要；CaV1.3与小鼠内毛细胞发育和突触传递，区分发育影响和成熟工作机制。"
  },
  "ruggero-furosemide-1991": {
    "title": "Furosemide alters organ of corti mechanics: evidence for feedback of outer hair cells upon the basilar membrane",
    "authors": "Ruggero, MA; Rich, NC",
    "year": "1991",
    "publication": "The Journal of Neuroscience, 11, (4), 1057-1067",
    "doi": "10.1523/JNEUROSCI.11-04-01057.1991",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3580957/",
    "access": "abstract",
    "supports": "核对原论文摘要；呋塞米改变生理状态与龙猫耳蜗机械响应的实验，不将药物操作当作外毛细胞单一特异性干预。"
  },
  "kazmierczak-tip-link-2007": {
    "title": "Cadherin 23 and protocadherin 15 interact to form tip-link filaments in sensory hair cells",
    "authors": "Kazmierczak, Piotr; Sakaguchi, Hirofumi; Tokita, Joshua; Wilson-Kubalek, Elizabeth M.; Milligan, Ronald A.; Müller, Ulrich; Kachar, Bechara",
    "year": "2007",
    "publication": "Nature, 449, (7158), 87-91",
    "doi": "10.1038/nature06091",
    "url": "https://www.nature.com/articles/nature06091",
    "access": "abstract",
    "supports": "核对出版方原论文摘要；CDH23和PCDH15构成顶端连接，不把连接本身当作离子通道。"
  },
  "roux-otoferlin-2006": {
    "title": "Otoferlin, Defective in a Human Deafness Form, Is Essential for Exocytosis at the Auditory Ribbon Synapse",
    "authors": "Roux, Isabelle; Safieddine, Saaid; Nouvian, Régis; Grati, M'hamed; Simmler, Marie-Christine; Bahloul, Amel; Perfettini, Isabelle; Le Gall, Morgane; Rostaing, Philippe; Hamard, Ghislaine; Triller, Antoine; Avan, Paul; Moser, Tobias; Petit, Christine",
    "year": "2006",
    "publication": "Cell, 127, (2), 277-289",
    "doi": "10.1016/j.cell.2006.08.040",
    "url": "https://pubmed.ncbi.nlm.nih.gov/17055430/",
    "access": "abstract",
    "supports": "核对原论文摘要；Otof缺失小鼠的突触胞吐障碍，不把结构尚存当作传递功能正常。"
  },
  "effertz-nanophysiology-2020": {
    "title": "Recent advances in cochlear hair cell nanophysiology: subcellular compartmentalization of electrical signaling in compact sensory cells",
    "authors": "Effertz, Thomas; Moser, Tobias; Oliver, Dominik",
    "year": "2020",
    "publication": "Faculty Reviews, 9, 24",
    "doi": "10.12703/r/9-24",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7886071/",
    "access": "fulltext",
    "supports": "取得公开全文XML，核对原文图1、完整图注及CC BY 4.0许可；用于图3，不把图示的2020年分子机制概括当作完整装置。"
  },
  "verschooten-human-cochlea-2018": {
    "title": "High-resolution frequency tuning but not temporal coding in the human cochlea",
    "authors": "Verschooten, Eric; Desloovere, Christian; Joris, Philip X.",
    "year": "2018",
    "publication": "PLOS Biology, 16, (10), e2005164",
    "doi": "10.1371/journal.pbio.2005164",
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6201958/",
    "access": "fulltext",
    "supports": "读取公开全文XML及重点段落；人类复合电位推断调谐与同步，不当作单根纤维直接记录。"
  },
  "lopez-olivocochlear-2018": {
    "title": "Olivocochlear Efferents in Animals and Humans: From Anatomy to Clinical Relevance",
    "authors": "Lopez-Poveda, Enrique A.",
    "year": "2018",
    "publication": "Frontiers in Neurology, 9, 197",
    "doi": "10.3389/fneur.2018.00197",
    "url": "https://pubmed.ncbi.nlm.nih.gov/29632514/",
    "access": "fulltext",
    "supports": "核对公开原文相关段落；区分内／外侧橄榄耳蜗通路，以及动物与人类的证据强度。"
  },
  "kemp-oae-1978": {
    "title": "Stimulated acoustic emissions from within the human auditory system",
    "authors": "Kemp, D. T.",
    "year": "1978",
    "publication": "The Journal of the Acoustical Society of America, 64, (5), 1386-1391",
    "doi": "10.1121/1.382104",
    "url": "https://pubmed.ncbi.nlm.nih.gov/744838/",
    "access": "abstract",
    "supports": "核对原论文摘要；人耳刺激后声学输出的重要历史证据。"
  },
  "wu-presbycusis-2020": {
    "title": "Age-Related Hearing Loss Is Dominated by Damage to Inner Ear Sensory Cells, Not the Cellular Battery That Powers Them",
    "authors": "Wu, Pei-zhe; O'Malley, Jennifer T.; de Gruttola, Victor; Liberman, M. Charles",
    "year": "2020",
    "publication": "The Journal of Neuroscience, 40, (33), 6357-6366",
    "doi": "10.1523/JNEUROSCI.0937-20.2020",
    "url": "https://pubmed.ncbi.nlm.nih.gov/32690619/",
    "access": "abstract",
    "supports": "核对原论文摘要与图注；人尸检组织与听力图关联，限定所研究样本和统计模型。"
  },
  "wang-otof-gene-2024": {
    "title": "Bilateral gene therapy in children with autosomal recessive deafness 9: single-arm trial results",
    "authors": "Wang, Hui; Chen, Yuxin; Lv, Jun; Cheng, Xiaoting; Cao, Qi; Wang, Daqi; Zhang, Longlong; Zhu, Biyun; Shen, Min; Xu, Chunxin; Xun, Mengzhao; Wang, Zijing; Tang, Honghai; Hu, Shaowei; Cui, Chong; Jiang, Luoying; Yin, Yanbo; Guo, Luo; Zhou, Yi; Han, Lei; Gao, Ziwen; Zhang, Jiajia; Yu, Sha; Gao, Kaiyu; Wang, Jinghan; Chen, Bing; Wang, Wuqing; Chen, Zheng-Yi; Li, Huawei; Shu, Yilai",
    "year": "2024",
    "publication": "Nature Medicine, 30, (7), 1898-1904",
    "doi": "10.1038/s41591-024-03023-5",
    "url": "https://www.nature.com/articles/s41591-024-03023-5",
    "access": "abstract",
    "supports": "参照原文公开记录；查阅层次与范围见本词条研究记录。"
  },
  "fda-otarmeni-2026": {
    "title": "FDA Approves First-Ever Gene Therapy for Treatment of Genetic Hearing Loss Under National Priority Voucher Program",
    "authors": "U.S. Food and Drug Administration",
    "year": "2026",
    "publication": "FDA 公告，2026-04-23",
    "url": "https://www.fda.gov/news-events/press-announcements/fda-approves-first-ever-gene-therapy-treatment-genetic-hearing-loss-under-national-priority-voucher",
    "access": "documentation",
    "supports": "核对FDA 2026-04-23公告：美国加速批准、双等位基因OTOF病因、保留外毛细胞功能及同耳未植入人工耳蜗条件，持续批准涉及进一步验证。"
  }
};
