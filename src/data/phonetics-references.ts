import type { Reference } from './references';

export const phoneticsReferences: Record<string, Reference> = {
  'phonetics-articulatory-tools': {
    title: 'Articulatory instrumentation and modelling; Electromagnetic Articulography',
    authors: 'Edinburgh Speech Science and Technology / Centre for Speech Technology Research; NeuroSpeech, University of Cologne',
    year: '未标年（2026-10-09核验）', publication: '研究机构方法说明',
    url: 'https://www.cstr.inf.ed.ac.uk/edsst/research.html', access: 'documentation',
    supports: '已阅读EdSST发音记录方法说明及科隆大学https://neurospeech.uni-koeln.de/methods/ema：EMA传感器位置轨迹、EPG舌腭接触、超声舌运动和同步录音。只引用测量对象，不据机构介绍声称临床疗效或本轮设备可用性。'
  },
  'phonetics-wayland-2018': {
    title: 'Phonetics: A Practical Introduction', authors: 'Wayland R.', year: '2018',
    publication: 'Cambridge University Press', doi: '10.1017/9781108289849',
    url: 'https://www.cambridge.org/highereducation/books/phonetics/CA1E1B9EEF87F3C8061DA8A4DAB3FA23', access: 'metadata',
    supports: '2026-10-09核对出版社书目与内容简介：发音、声学及听觉／感知三个研究领域。未阅读全文；只用于学科范围与延伸阅读，不支撑具体实验结果。'
  },
  'phonetics-modality': {
    title: '3.1 Modality', authors: 'Anderson C, Bjorkman B, Denis D, Doner J, Grant M, Sanders N, Taniguchi A.', year: '2022',
    publication: 'Essentials of Linguistics, 2nd edition; eCampusOntario',
    url: 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-1-modality/', access: 'fulltext',
    supports: '2026-10-09阅读官方章节与机构存档教材PDF：语言的实现模态、口语的发音—声学—听觉关系，以及手语也属于现代语音学研究范围。图1为本站原创简化框图。'
  },
  'phonetics-phonemes': {
    title: '4.1 Phonemes and allophones', authors: 'Anderson C, Bjorkman B, Denis D, Doner J, Grant M, Sanders N, Taniguchi A.', year: '2022',
    publication: 'Essentials of Linguistics, 2nd edition; eCampusOntario',
    url: 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/4-1-phonemes-and-allophones/', access: 'fulltext',
    supports: '2026-10-09经eCampusOntario机构存档原始教材PDF阅读4.1：具体实现、音位和变体的区别，方括号和斜线的记音层级。章节网页本轮403，未将网页访问失败记为成功。'
  },
  'phonetics-articulators': {
    title: '3.2 Speech articulators', authors: 'Anderson C, Bjorkman B, Denis D, Doner J, Grant M, Sanders N, Taniguchi A.', year: '2022',
    publication: 'Essentials of Linguistics, 2nd edition; eCampusOntario',
    url: 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-2-speech-articulators/', access: 'fulltext',
    supports: '2026-10-09经机构存档原始教材PDF阅读3.2：口腔、咽腔、鼻腔与发音器官；不把简化框图当成按比例解剖图。章节网页本轮403。'
  },
  'phonetics-vowels': {
    title: '3.5 Describing vowels', authors: 'Anderson C, Bjorkman B, Denis D, Doner J, Grant M, Sanders N, Taniguchi A.', year: '2022',
    publication: 'Essentials of Linguistics, 2nd edition; eCampusOntario',
    url: 'https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/chapter/3-5-describing-vowels/', access: 'fulltext',
    supports: '2026-10-09经机构存档原始教材PDF阅读3.5：舌位高低、前后、圆唇及连续元音空间。章节网页本轮403。'
  },
  'phonetics-praat-spectrogram': {
    title: 'Sound: To Spectrogram...', authors: 'Boersma P, Weenink D.', year: '2021（页面标注；2026-10-09核验）',
    publication: 'Praat official manual', url: 'https://praat.org/manual/Sound__To_Spectrogram___.html', access: 'documentation',
    supports: '已核对分析帧、窗长、窗形、帧移与频率步长说明：窗长影响分析带宽，不同窗形数值不同。本文5/40 ms周期Hann窗、4096点FFT及等效噪声带宽由原创脚本计算，不套用Praat Gaussian默认带宽公式。'
  },
  'phonetics-praat-pitch': {
    title: 'How to choose a pitch analysis method; Pitch analysis by filtered autocorrelation', authors: 'Boersma P, Weenink D.', year: '2023–2024（页面标注；2026-10-09核验）',
    publication: 'Praat official manual', url: 'https://praat.org/manual/how_to_choose_a_pitch_analysis_method.html', access: 'documentation',
    supports: '已阅读方法选择与filtered autocorrelation设置页：语调／声带振动频率分析和原始周期性分析的目标不同，搜索范围、清浊判定与倍频／半频错误需核查；不把算法输出等同主观音高。'
  },
  'phonetics-vot-review-2017': {
    title: 'Voice Onset Time (VOT) at 50: Theoretical and practical issues in measuring voicing distinctions',
    authors: 'Abramson AS, Whalen DH.', year: '2017', publication: 'Journal of Phonetics, 63, 75–86', doi: '10.1016/j.wocn.2017.05.002',
    url: 'https://pubmed.ncbi.nlm.nih.gov/29104329/', access: 'abstract',
    supports: '2026-10-09核对原始摘要及PubMed公开图注：经典定义、问题案例与标注一致性；负／正VOT及送气与周期振动重叠。PMC全文遇验证，Europe PMC XML失败；不声称阅读全文。图4为独立教学时间条。'
  },
  'phonetics-coarticulation-2013': {
    title: 'The time course of perception of coarticulation', authors: 'Beddor PS, McGowan KB, Boland JE, Coetzee AW, Brasher A.', year: '2013',
    publication: 'Journal of the Acoustical Society of America, 133(4), 2350–2366', doi: '10.1121/1.4794366',
    url: 'https://pubmed.ncbi.nlm.nih.gov/23556601/', access: 'abstract',
    supports: '2026-10-09核对原始摘要：美国英语词中提前／较晚的元音鼻化与图片眼动，听者可提前利用协同发音，权重随语境和个体变化。作者PDF未成功下载；不把摘要扩展到所有语言。'
  },
  'phonetics-mfa-2017': {
    title: 'Montreal Forced Aligner: Trainable Text-Speech Alignment Using Kaldi', authors: 'McAuliffe M, Socolof M, Mihuc S, Wagner M, Sonderegger M.', year: '2017',
    publication: 'Interspeech 2017, 498–502', doi: '10.21437/Interspeech.2017-1386',
    url: 'https://www.isca-archive.org/interspeech_2017/mcauliffe17_interspeech.html', access: 'fulltext',
    supports: '2026-10-09阅读ISCA原始PDF摘要、引言与方法：已有文字、词典和声学模型下的词／音段对齐，在英语实验室与会话语音中比较人工边界；自动时间戳不是直接观察到的发音器官事件。'
  },
  'phonetics-alignment-2024': {
    title: 'Tradition or Innovation: A Comparison of Modern ASR Methods for Forced Alignment', authors: 'Rousso R, Cohen E, Keshet J, Chodroff E.', year: '2024',
    publication: 'Interspeech 2024, 1525–1529', doi: '10.21437/Interspeech.2024-429',
    url: 'https://www.isca-archive.org/interspeech_2024/rousso24_interspeech.html', access: 'fulltext',
    supports: '2026-10-09阅读ISCA原始PDF摘要、引言、方法及相关结果：TIMIT/Buckeye英语语料，比较WhisperX/MMS正确识别词的词级对齐，MFA在这些条件下较好；不推广成所有语言、版本和音段边界的总排名。'
  },
  'phonetics-mri-2025': {
    title: '75-Speaker Annot-16: A benchmark dataset for speech articulatory rt-MRI annotation with articulator contours and phonetic alignment',
    authors: 'Shi X, Zhang Y, Lu Y, Ma M, Feng T, Toutios A, Hsu H, Goldstein L, Narayanan S.', year: '2025',
    publication: 'Interspeech 2025, 2175–2179', doi: '10.21437/Interspeech.2025-2394',
    url: 'https://www.isca-archive.org/interspeech_2025/shi25g_interspeech.html', access: 'fulltext',
    supports: '2026-10-09阅读ISCA原始PDF摘要、2.1–2.3及数据说明：从75人声道MRI数据库选16人详细标注，自动处理结合专家校验，包含正中矢状面轮廓与语音对齐；不声称75人均获同样精标，也不当作完整三维气流。'
  },
};
