export const phaseLockingReferences = {
  "phase-peterson2020": {
    "title": "Phase Locking of Auditory Nerve Fibers: The Role of Lowpass Filtering by Hair Cells.",
    "authors": "Peterson AJ; Heil P",
    "year": "2020",
    "publication": "The Journal of neuroscience : the official journal of the Society for Neuroscience, 40(24), 4700-4714",
    "doi": "10.1523/JNEUROSCI.2269-19.2020",
    "url": "https://pubmed.ncbi.nlm.nih.gov/32376778/",
    "access": "abstract",
    "supports": "原始摘要核验猫听神经数据、静态非线性/低通模型和纤维类型差异；不复述未核验全文的具体拟合参数。"
  },
  "six-goldberg1969": {
    "title": "Response of binaural neurons of dog superior olivary complex to dichotic tonal stimuli: some physiological mechanisms of sound localization.",
    "authors": "Goldberg JM; Brown PB",
    "year": "1969",
    "publication": "Journal of neurophysiology, 32(4), 613-636",
    "doi": "10.1152/jn.1969.32.4.613",
    "url": "https://pubmed.ncbi.nlm.nih.gov/5810617/",
    "access": "metadata",
    "supports": "仅原始正式书目与历史定位；向量强度公式另外按圆周平均定义推导，不依据书目推断实验结果。"
  },
  "phase-vinck2010": {
    "title": "The pairwise phase consistency: a bias-free measure of rhythmic neuronal synchronization.",
    "authors": "Vinck M; van Wingerden M; Womelsdorf T; Fries P; Pennartz CM",
    "year": "2010",
    "publication": "NeuroImage, 51(1), 112-122",
    "doi": "10.1016/j.neuroimage.2010.01.073",
    "url": "https://pubmed.ncbi.nlm.nih.gov/20114076/",
    "access": "abstract",
    "supports": "原始摘要：有限样本偏差、PPC总体对应平方PLV、跨条件试次/事件数问题。本文PPC与R代数关系为从事件对余弦平均展开的教学推导。"
  },
  "phase-heeringa2025": {
    "title": "Notched noise reveals differential improvement in the neural representation of the sound envelope.",
    "authors": "Heeringa AN; Klug J; Köppl C; Dietz M",
    "year": "2025",
    "publication": "Communications biology, 8(1), 1171",
    "doi": "10.1038/s42003-025-08536-4",
    "url": "https://pubmed.ncbi.nlm.nih.gov/40770410/",
    "access": "fulltext",
    "supports": "全文选读引言、结果、神经记录和人类心理物理方法：沙鼠单纤维、凹口噪声对同频包络锁定与跨耳通道匹配的条件性证据；不推广为加噪声的临床建议。"
  },
  "phase-mne-tfr": {
    "title": "mne.time_frequency.tfr_array_morlet",
    "authors": "MNE contributors",
    "year": "2026-10-10核验",
    "publication": "MNE 1.13.2 official documentation",
    "url": "https://mne.tools/stable/generated/mne.time_frequency.tfr_array_morlet.html",
    "access": "documentation",
    "supports": "MNE 1.13.2官方tfr_array_morlet文档：数组形状、连续数据、输出与ITC；未运行MNE分析。"
  },
  "phase-saddler2024": {
    "title": "Models optimized for real-world tasks reveal the task-dependent necessity of precise temporal coding in hearing.",
    "authors": "Saddler MR; McDermott JH",
    "year": "2024",
    "publication": "Nature communications, 15(1), 10590",
    "doi": "10.1038/s41467-024-54700-5",
    "url": "https://pubmed.ncbi.nlm.nih.gov/39632854/",
    "access": "fulltext",
    "supports": "正式期刊全文选读引言、图1方法、自然声音任务与讨论：模拟听神经时间精度操纵、任务依赖和人类对应边界。排除同研究2024预印本重复证据。"
  },
  "phase-rose1967": {
    "title": "Phase-locked response to low-frequency tones in single auditory nerve fibers of the squirrel monkey.",
    "authors": "Rose JE; Brugge JF; Anderson DJ; Hind JE",
    "year": "1967",
    "publication": "Journal of neurophysiology, 30(4), 769-793",
    "doi": "10.1152/jn.1967.30.4.769",
    "url": "https://pubmed.ncbi.nlm.nih.gov/4962851/",
    "access": "metadata",
    "supports": "仅正式书目：1967、松鼠猴单听神经纤维、经典研究定位；无原始摘要与全文，未据题名复述数值和结果。"
  },
  "phase-ashida2026": {
    "title": "Benefits of Enhanced Phase-Locking for Binaural Coding of Amplitude-Modulated Sounds.",
    "authors": "Ashida G",
    "year": "2026",
    "publication": "Trends in hearing, 30, 23312165261421708",
    "doi": "10.1177/23312165261421708",
    "url": "https://pubmed.ncbi.nlm.nih.gov/41671095/",
    "access": "fulltext",
    "supports": "2026-02-11正式期刊全文；选读Methods的AN/BC/LSO阶段、Results与Discussion，比较保留/绕过BC、ILD控制和包络ITD调谐。仅作计算证据，不作人类结果。"
  },
  "six-scipy-circle": {
    "title": "scipy.stats.circmean",
    "authors": "SciPy contributors",
    "year": "2026-10-10核验",
    "publication": "SciPy 1.18.0 official documentation",
    "url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.circmean.html",
    "access": "documentation",
    "supports": "SciPy 1.18.0官方circmean文档：角度平均、范围和不稳定方向；本页向量强度另外计算。"
  }
} as const;
