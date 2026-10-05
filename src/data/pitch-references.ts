import type { Reference } from './references';

export const pitchReferences: Record<string, Reference> = {
  'shackleton-1994': { title: 'The role of resolved and unresolved harmonics in pitch perception and frequency modulation discrimination', authors: 'Shackleton, T. M. & Carlyon, R. P.', year: '1994', publication: 'Journal of the Acoustical Society of America, 95(6), 3529–3540', doi: '10.1121/1.409970', url: 'https://pubmed.ncbi.nlm.nih.gov/8046144/', access: 'abstract', supports: '已核对原始摘要：不同频谱范围、基频及分量相位条件下的音高匹配和调频辨别；用于说明可分辨性与任务、相位之间的关系，不规定通用谐波阶数分界。' },
  'shepard-1964': { title: 'Circularity in Judgments of Relative Pitch', authors: 'Shepard, R. N.', year: '1964', publication: 'Journal of the Acoustical Society of America, 36(12), 2346–2353', doi: '10.1121/1.1919362', url: 'https://doi.org/10.1121/1.1919362', access: 'fulltext', supports: '已核对原始论文摘要及相关引言：特殊复合音的循环相对音高判断，用于区分音高高低与音级；不认定全部音高关系都必为二维。' },
  'shepard-1982': { title: 'Geometrical approximations to the structure of musical pitch', authors: 'Shepard, R. N.', year: '1982', publication: 'Psychological Review, 89(4), 305–333', doi: '10.1037/0033-295X.89.4.305', url: 'https://doi.org/10.1037/0033-295X.89.4.305', access: 'fulltext', supports: '已核对 Crossref 书目及原始论文摘要、Simple Helical Representations 与音级圆环相关段落：每圈一个八度，同音级沿轴向对齐。网站音高螺旋独立绘制，几何距离不是主观距离或神经结构的测量值。' },
};
