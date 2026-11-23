import type { Reference } from './references.ts';

export const artificialHearingReferences: Record<string, Reference> = {
  'ah-hearing-aids': {
    title: 'Hearing Aids', authors: 'National Institute on Deafness and Other Communication Disorders',
    year: '2022（页面更新；2026-11-24 核验）', publication: 'NIH/NIDCD 官方说明',
    url: 'https://www.nidcd.nih.gov/health/hearing-aids', access: 'documentation',
    supports: '读取 What is a hearing aid、How can hearing aids help 与 Are new types of aids available：声学放大、残余感觉转导、中耳机械驱动及骨导。只使用稳定机制，不采用历史使用率或费用信息。',
  },
  'ah-abi': {
    title: "Outcomes in nontumor adults fitted with the auditory brainstem implant: 10 years' experience.",
    authors: 'Colletti V, Shannon R, Carner M, Veronese S, Colletti L.', year: '2009', publication: 'Otology & Neurotology, 30(5), 614–618',
    doi: '10.1097/MAO.0b013e3181a864f2', url: 'https://pubmed.ncbi.nlm.nih.gov/19546832/', access: 'abstract',
    supports: '2026-11-24 经 Europe PMC 核对原始摘要与书目：部分非肿瘤成人出现开放式言语识别，病因与结果差异明显；特定中心观察结果，不作为所有 ABI 使用者的预期成绩。',
  },
  'ah-ami': {
    title: 'The auditory midbrain implant: a new auditory prosthesis for neural deafness-concept and device description.',
    authors: 'Lenarz T, Lim HH, Reuter G, Patrick JF, Lenarz M.', year: '2006', publication: 'Otology & Neurotology, 27(6), 838–843',
    doi: '10.1097/01.mao.0000232010.01116.e9', url: 'https://pubmed.ncbi.nlm.nih.gov/16936570/', access: 'abstract',
    supports: '2026-11-24 核对原始摘要与书目：以耳蜗核为 ABI 靶点、以下丘中央核为 AMI 原型靶点的设计动机。原型概念文，不能支持当代常规应用或疗效优于 CI。',
  },
  'ah-opto': {
    title: 'Near physiological spectral selectivity of cochlear optogenetics.',
    authors: 'Dieter A, Duque-Afonso CJ, Rankovic V, Jeschke M, Moser T.', year: '2019', publication: 'Nature Communications, 10, 1962',
    doi: '10.1038/s41467-019-09980-7', url: 'https://doi.org/10.1038/s41467-019-09980-7', access: 'abstract',
    supports: '2026-11-24 经 Europe PMC 核对摘要：沙鼠下丘多通道记录比较声、电、光遗传刺激的选择性，保留强度条件与动物神经终点；不表述为人类语言或音乐功能已恢复正常。',
  },
  'ah-audioset': {
    title: 'Audio Set: An ontology and human-labeled dataset for audio events',
    authors: 'Gemmeke JF, Ellis DPW, Freedman D, Jansen A, Lawrence W, Moore RC, Plakal M, Ritter M.',
    year: '2017', publication: 'IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)',
    url: 'https://research.google/pubs/audio-set-an-ontology-and-human-labeled-dataset-for-audio-events/', access: 'abstract',
    supports: '2026-11-24 读取作者机构发布的论文摘要与书目：声音事件类别体系、人类标注及分类任务。论文中的本体类别与发布子集类别数不同，正文不混用数量，也不据任务成绩判断主观体验。',
  },
};
