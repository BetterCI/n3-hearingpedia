import type { Reference } from './references';

export const helmholtzReferences: Record<string, Reference> = {
  'helmholtz-gerlach-1969': {
    title: 'Helmholtz, Hermann Ludwig Ferdinand von', authors: 'Walther Gerlach', year: '1969', publication: 'Neue Deutsche Biographie, 8, 498–501',
    url: 'https://www.deutsche-biographie.de/gnd11854893X.html', access: 'fulltext',
    supports: '阅读1969年NDB传记的教育、任职、生卒与1883年封爵段落；与同页1906年ADB传记区分。'
  },
  'helmholtz-association-history': {
    title: 'Hermann von Helmholtz', authors: 'Helmholtz Association', year: '无日期（2026-10-09核验）', publication: '机构历史介绍',
    url: 'https://www.helmholtz.de/en/about-us/who-we-are/history/hermann-von-helmholtz/', access: 'documentation',
    supports: '核对医学与物理研究背景、眼科仪器、音的感觉著作及PTR首任院长身份；不以机构纪念材料证明全部学术优先权。'
  },
  'helmholtz-tone-1895': {
    title: 'On the Sensations of Tone as a Physiological Basis for the Theory of Music', authors: 'Hermann L. F. Helmholtz; Alexander J. Ellis（译注）', year: '1895（第二英语版重印；德文初版1863）', publication: 'Longmans, Green, and Co.',
    url: 'https://archive.org/stream/onsensationsofto00helmrich/onsensationsofto00helmrich_djvu.txt', access: 'fulltext',
    supports: '阅读题名页、版本前言，以及共振器、音叉合成、相位控制、耳蜗共振、拍与差音相关章节；另对照Saltire第3、6、8章原书转录。1895不是初版年份；现代网页交互插入内容不作为原书文字。'
  },
  'helmholtz-kursell-2018': {
    title: 'Alexander Ellis’s Translation of Helmholtz’s Sensations of Tone', authors: 'Julia Kursell', year: '2018', publication: 'Isis, 109(2)', doi: '10.1086/698239',
    url: 'https://www.journals.uchicago.edu/doi/full/10.1086/698239', access: 'fulltext',
    supports: '阅读英语翻译、Ellis的语音学背景及音叉装置相关历史论述；用于版本流传背景，不代替原著声学论断。'
  },
  'helmholtz-schmidgen-time': {
    title: 'Helmholtz’s “psychological” time experiments', authors: 'Henning Schmidgen', year: '无日期（以作者2002年研究为基础）', publication: 'Virtual Laboratory, Max Planck Institute for the History of Science',
    url: 'https://vlp.mpiwg-berlin.mpg.de/pdfgen/essays/art10.pdf', access: 'fulltext',
    supports: '阅读六页历史研究，核对1850年蛙神经与人类反应时研究的区别、差减逻辑及注意干扰；PDF末页说明以2002年Endeavour论文为基础，不将2002擅作网页发布日期。'
  },
  'helmholtz-unsw-resonance': {
    title: 'Helmholtz Resonance', authors: 'UNSW Music Acoustics', year: '无日期（2026-10-09核验）', publication: 'University of New South Wales',
    url: 'https://www.phys.unsw.edu.au/jw/Helmholtz.html', access: 'documentation',
    supports: '读取腔体空气弹性、颈部空气质量和端部修正说明；瓶状集总模型不直接作为原历史双开口、耳负载仪器的精确模型。'
  },
  'helmholtz-smithsonian-resonator': {
    title: 'Acoustic Resonator', authors: 'National Museum of American History, Smithsonian Institution', year: '无日期（2026-10-09核验）', publication: '馆藏编号 nmah_1814384',
    url: 'https://americanhistory.si.edu/collections/object/nmah_1814384', access: 'documentation',
    supports: '核对Rudolph Koenig制作的共振器装置馆藏说明，区分理论研究者与仪器制造者；馆藏照片标有使用限制，本文不采用其图片。'
  },
  'helmholtz-ptb-foundation': {
    title: 'Helmholtz and the Founding Years', authors: 'Helmut Rechenberg', year: '2012', publication: 'PTB-Mitteilungen, 122(2), English edition',
    url: 'https://www.ptb.de/cms/fileadmin/internet/publikationen/ptb_mitteilungen/mitt2012/Heft2/PTB-Mitteilungen_2012_Heft_2_en.pdf', access: 'fulltext',
    supports: '读取可检索原PDF相关历史段落：1887年机构创办，1888年Helmholtz任院长；直接PDF打开未成功，不声称整册阅读。'
  },
  'helmholtz-consonance-2010': {
    title: 'Individual differences reveal the basis of consonance', authors: 'Josh H. McDermott; Andriana J. Lehr; Andrew J. Oxenham', year: '2010', publication: 'Current Biology, 20(11), 1035–1041', doi: '10.1016/j.cub.2010.04.019',
    url: 'https://pubmed.ncbi.nlm.nih.gov/20493704/', access: 'abstract',
    supports: '阅读原研究摘要：对谐和性、无拍声音的偏好与和弦协和偏好的关系；不把摘要关联结果扩大成普遍机制或文化因果结论。'
  },
  'helmholtz-portrait-source': {
    title: 'File: Hermann von Helmholtz-2.jpg', authors: 'AIP Emilio Segrè Visual Archives, General Collection（署名）；Wikimedia Commons（授权记录）', year: '2022（上传日期，非摄影日期）', publication: 'Wikimedia Commons',
    url: 'https://commons.wikimedia.org/wiki/File:Hermann_von_Helmholtz-2.jpg', access: 'documentation',
    supports: '核对肖像来源、CC0 1.0及原图尺寸；AIP原记录未成功打开，因此不重述照片距最后疾病三天的细节，不将2022写成摄影年份。'
  },
  'helmholtz-resonator-photo': {
    title: 'File: Helmholtz resonator.jpg', authors: 'brian0918', year: '2006（摄影文件记录）', publication: 'Case Western Reserve University Physics Department; Wikimedia Commons',
    url: 'https://commons.wikimedia.org/wiki/File:Helmholtz_resonator.jpg', access: 'documentation',
    supports: '核对照片CC BY-SA 2.5、Max Kohl制造、约1890–1900年同类仪器及原尺寸；不称为Helmholtz亲手制作的原件。'
  }
};
