import type { Reference } from './references';
export const nonlinearityReferences: Record<string, Reference> = {
  "ndist-mit": {
    "title": "Signals and Systems: Syllabus",
    "authors": "MIT OpenCourseWare / Dennis Freeman",
    "year": "2011",
    "publication": "6.003",
    "url": "https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/syllabus/",
    "access": "documentation",
    "supports": "课程范围与线性时不变系统、卷积及频率响应；正文恒等式为独立推导。"
  },
  "ndist-smith": {
    "title": "Physical Audio Signal Processing: Nonlinear Distortion",
    "authors": "Julius O. Smith III",
    "year": "2010",
    "publication": "Online book",
    "url": "https://www.dsprelated.com/freebooks/pasp/Nonlinear_Distortion.html",
    "access": "fulltext",
    "supports": "读取硬削顶、软削顶、奇次非线性与混叠相关说明；本文数值为独立教学计算。"
  },
  "ndist-ap": {
    "title": "More about THD+N and THD",
    "authors": "Audio Precision",
    "year": "2013",
    "publication": "Technical explanation",
    "url": "https://www.audioprecision.com/news/more-about-thdn-and-thd",
    "access": "fulltext",
    "supports": "读取THD、THD+N残余构成、FFT方法及APx不同分母定义。"
  },
  "ndist-ti": {
    "title": "Guidelines for Measuring Audio Power Amplifier Performance (Rev. A)",
    "authors": "Texas Instruments",
    "year": "2022",
    "publication": "SLOA068A",
    "url": "https://www.ti.com/lit/an/sloa068a/sloa068a.pdf",
    "access": "documentation",
    "supports": "检索可见第4节THD+N定义与基频归一化；不声称核读完整标准或运行仪器。"
  },
  "ndist-robles": {
    "title": "Mechanics of the mammalian cochlea",
    "authors": "Luis Robles; Mario A. Ruggero",
    "year": "2001",
    "publication": "Physiological Reviews 81(3):1305–1352",
    "doi": "10.1152/physrev.2001.81.3.1305",
    "url": "https://doi.org/10.1152/physrev.2001.81.3.1305",
    "access": "abstract",
    "supports": "核对PubMed书目及出版社可见段落：主动耳蜗力学、压缩和失真；未重读全文。"
  }
};
