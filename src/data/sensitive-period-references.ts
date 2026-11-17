import type { Reference } from './references';

export const sensitivePeriodReferences: Record<string, Reference> = {
  'asp-barkat-2011': {
    title: 'A critical period for auditory thalamocortical connectivity', authors: 'Barkat TR, Polley DB, Hensch TK.', year: '2011',
    publication: 'Nature Neuroscience, 14(9), 1189–1194', doi: '10.1038/nn.2882', url: 'https://pubmed.ncbi.nlm.nih.gov/21804538/', access: 'fulltext',
    supports: '2026-11-17阅读作者实验室PDF第一页与结果、图1–2说明及摘要：小鼠纯音暴露、皮层与丘脑频率图谱差异、丘脑皮层连接与Icam5；不将小鼠出生后天数换算成人类干预年龄。PDF：https://www.brainsoundlab.com/wp-content/uploads/2015/12/NatNeurosci_2011.pdf'
  },
  'asp-kalish-2020': {
    title: 'Single-nucleus RNA sequencing of mouse auditory cortex reveals critical period triggers and brakes', authors: 'Kalish BT, Barkat TR, Diel EE, Zhang EJ, Greenberg ME, Hensch TK.', year: '2020',
    publication: 'PNAS, 117(21), 11744–11752', doi: '10.1073/pnas.1920433117', url: 'https://pubmed.ncbi.nlm.nih.gov/32404418/', access: 'abstract',
    supports: '2026-11-17核对PubMed书目及Europe PMC原始摘要：小鼠单核RNA测序、声音暴露、GABA回路功能与开启、Nogo受体信号与关闭的功能成像证据；没有把候选基因全部当成因果开关，不提供人体用药建议。'
  },
  'asp-chang-2003': {
    title: 'Environmental noise retards auditory cortical development', authors: 'Chang EF, Merzenich MM.', year: '2003',
    publication: 'Science, 300(5618), 498–502', doi: '10.1126/science.1082163', url: 'https://pubmed.ncbi.nlm.nih.gov/12702879/', access: 'abstract',
    supports: '2026-11-17阅读PubMed原始摘要：幼鼠持续中等噪声饲养、皮层组织与选择性成熟推迟及后续纯音重组；不推导儿童日常背景噪声的安全阈值或家庭方案。'
  },
  'asp-bilateral-2026': {
    title: 'Outcomes in Adolescents From Sequential vs Bilateral Cochlear Implantation in Young Children', authors: 'Asp F, Eklöf M, Moumèn-Denanto F, Kral A, Karltorp E.', year: '2026',
    publication: 'Pediatrics, 157(5), e2025074086', doi: '10.1542/peds.2025-074086', url: 'https://pubmed.ncbi.nlm.nih.gov/42002288/', access: 'abstract',
    supports: '2026-11-17阅读PubMed及Europe PMC原始摘要：37人（17同时、20序贯），12–21岁、至少一耳2.5岁前植入、间隔小于4年；同时组定位较好、言语识别相近。保留横断面、筛选和参加比例限制，不写成随机试验或统一手术建议。'
  }
};
