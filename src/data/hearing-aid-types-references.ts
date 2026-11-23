import type { Reference } from './references';

export const hearingAidTypesReferences: Record<string, Reference> = {
  'types-nhs-hearing-aids': {
    title: 'Hearing aids and implants', authors: 'National Health Service',
    year: '在线资料（2026-11-24 核验）', publication: 'NHS health information',
    url: 'https://www.nhs.uk/tests-and-treatments/hearing-aids-and-implants/', access: 'documentation',
    supports: '核对外形定义、RITE连接、CIC/IIC和盒式的概述；不把英国获取渠道或通用功率描述当作各国规则或全型号规格。'
  },
  'types-aaa-pediatric-2013': {
    title: 'Clinical Practice Guidelines: Pediatric Amplification', authors: 'American Academy of Audiology',
    year: '2013', publication: 'Clinical Practice Guidelines, June 2013, section 4.2',
    url: 'https://www.audiology.org/wp-content/uploads/2021/05/PediatricAmplificationGuidelines.pdf', access: 'fulltext',
    supports: '阅读4.2外形选择及BTE/RIC术语相关段落：儿童耳部生长、可更换耳模、输出及操作安全；历史指南用于稳定结构原则，不标为现行最新产品规范。'
  },
  'types-aao-bone-conduction': {
    title: 'Position Statement: Bone Conduction Hearing Devices', authors: 'American Academy of Otolaryngology–Head and Neck Surgery',
    year: '2021（页面标注2025年7月复核）', publication: 'AAO-HNS Position Statements',
    url: 'https://www.entnet.org/resource/position-statement-bone-conduction-hearing-devices/', access: 'documentation',
    supports: '骨导用于传导性、混合性及部分单侧聋情形，区分非植入和植入形式；不提供通用手术年龄或输出上限。'
  },
  'types-implant-consensus-2022': {
    title: 'Consensus Statement on Bone Conduction Devices and Active Middle Ear Implants in Conductive and Mixed Hearing Loss',
    authors: '未列作者（PubMed 书目记录）', year: '2022', publication: 'Otology & Neurotology, 43(5), 513–529',
    doi: '10.1097/MAO.0000000000003491', url: 'https://pubmed.ncbi.nlm.nih.gov/35383700/', access: 'abstract',
    supports: '核对书目及摘要：常规康复不可行时的植入选择框架。未读取全文，不引用型号适应证、阈值或手术操作细节。'
  },
};
