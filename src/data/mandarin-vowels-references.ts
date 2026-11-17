import type { Reference } from './references';

export const mandarinVowelsReferences: Record<string, Reference> = {
  'mv-hsieh-apical-2026': {
    title: 'Spatiotemporal tongue kinematics from ultrasound imaging: Articulatory divergence in Mandarin apical vowels',
    authors: 'Hsieh F.-F.', year: '2026', publication: 'JASA Express Letters, 6(8), 085202',
    doi: '10.1121/10.0044524', url: 'https://pubmed.ncbi.nlm.nih.gov/42549994/', access: 'abstract',
    supports: '2026-11-17核对原始摘要搜索索引与书目信息；PubMed直接打开只返回页脚，未取得全文。仅引用超声时序分析显示两类舌尖音发音策略不同，不引入样本数或未读取的统计效应。'
  },
  'mv-yang-compound-2017': {
    title: 'Mandarin compound vowels produced by prelingually deafened children with cochlear implants',
    authors: 'Yang J, Xu L.', year: '2017',
    publication: 'International Journal of Pediatric Otorhinolaryngology, 97, 143–149', doi: '10.1016/j.ijporl.2017.04.012',
    url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5472838/', access: 'abstract',
    supports: '2026-11-17核对原始摘要及PMC与作者PDF的可检索方法段：选定普通话复元音、9个等距时间点的F1/F2、Bark坐标和动态指标。全文直接访问不稳定，未记为阅读全文；用途限于产出研究与动态测量示例，不作为听辨或植入疗效证据。'
  },
  'mv-yang-nlfc-2018': {
    title: 'Effects of nonlinear frequency compression on the acoustic properties and recognition of speech sounds in Mandarin Chinese',
    authors: 'Yang J, Qian J, Chen X, Kuehnel V, Rehmann J, von Buol A, Li Y, Ren C, Liu B, Xu L.', year: '2018',
    publication: 'The Journal of the Acoustical Society of America, 143(3), 1578–1590', doi: '10.1121/1.5027404',
    url: 'https://pubmed.ncbi.nlm.nih.gov/29604675/', access: 'abstract',
    supports: '2026-11-17核对原始摘要和书目信息：非线性频率压缩后普通话元音、擦音的声学变化及正常听力听者识别。作者PDF直接打开超时；不据该实验宣称助听器使用者的临床获益。'
  }
};
