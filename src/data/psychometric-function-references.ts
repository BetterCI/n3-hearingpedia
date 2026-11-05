import type { Reference } from './references';

export const psychometricFunctionReferences: Record<string, Reference> = {
  'pf-prins-2012': {
    title: 'The psychometric function: The lapse rate revisited',
    authors: 'Nicolaas Prins', year: '2012', publication: 'Journal of Vision, 12(6), 25',
    doi: '10.1167/12.6.25', url: 'https://pubmed.ncbi.nlm.nih.gov/22715196/', access: 'abstract',
    supports: '2026-11-06：核对Crossref书目、原论文摘要及作者研究页。模拟复核指出放开失误参数仍可留下阈值与斜率偏差；不据摘要宣称通用最优先验或重建论文原始模拟。',
  },
  'pf-shen-richards-2012': {
    title: 'A maximum-likelihood procedure for estimating psychometric functions: Thresholds, slopes, and lapses of attention',
    authors: 'Yi Shen; Virginia M. Richards', year: '2012', publication: 'The Journal of the Acoustical Society of America, 132(2), 957–967',
    doi: '10.1121/1.4733540', url: 'https://faculty.washington.edu/shenyi/site/publications/ShenRichards2012b.pdf', access: 'fulltext',
    supports: '2026-11-06：核对作者PDF和PMC可读索引中的模型定义、参数约定及sweet-point推导与讨论相关段落。支持不同参数需要不同刺激信息，不引用其试次数为通用设计要求。',
  },
  'pf-shen-2013': {
    title: 'Comparing adaptive procedures for estimating the psychometric function for an auditory gap detection task',
    authors: 'Yi Shen', year: '2013', publication: 'Attention, Perception, & Psychophysics, 75(4), 771–780',
    doi: '10.3758/s13414-013-0438-9', url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3634902/', access: 'abstract',
    supports: '2026-11-06：Crossref书目及原始研究摘要/公开索引核对听觉间隙任务中三种程序的比较范围；不报告未经本轮全文核对的样本和效率数值，不当作所有听觉任务的算法排序。',
  },
  'pf-prins-kingdom-2018': {
    title: 'Applying the Model-Comparison Approach to Test Specific Research Hypotheses in Psychophysical Research Using the Palamedes Toolbox',
    authors: 'Nicolaas Prins; Frederick A. A. Kingdom', year: '2018', publication: 'Frontiers in Psychology, 9, 1250',
    doi: '10.3389/fpsyg.2018.01250', url: 'https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01250/full', access: 'fulltext',
    supports: '2026-11-06：读取原文模型比较、参数约束和假设检验相关章节；支持条件间共享/自由参数需对应科学问题。没有安装或运行Palamedes；官网页面本轮另遇403，未把官网访问写成成功。',
  },
  'pf-psignifit-docs': {
    title: 'psignifit documentation: Get thresholds and slopes; Change the threshold percentage correct',
    authors: 'Psignifit contributors', year: '2026-11-06访问', publication: '官方Python方法文档，latest快照',
    url: 'https://psignifit.readthedocs.io/en/latest/how_to/How-to-Get-Thresholds-and-Slopes.html', access: 'documentation',
    supports: '实际读取阈值、斜率、scaled/unscaled和thresh_PC页面及区间警告；归一化阈值参数与原始正确率须区分。未安装或运行psignifit，不把latest文档当作固定软件版本或执行验证。',
  },
  'pf-leek-2001': {
    title: 'Adaptive procedures in psychophysical research',
    authors: 'Marjorie R. Leek', year: '2001', publication: 'Perception & Psychophysics, 63(8), 1279–1292',
    doi: '10.3758/BF03194543', url: 'https://pubmed.ncbi.nlm.nih.gov/11800457/', access: 'abstract',
    supports: '2026-11-06：核对原始综述摘要与书目，自适应根据历史刺激和反应选择后续刺激；仅用于程序概念与范围，不由摘要添加具体实现规则。',
  },
  'pf-wallis-2013': {
    title: 'The slope of the psychometric function and non-stationarity of thresholds in spatiotemporal contrast vision',
    authors: 'Stuart A. Wallis; Daniel H. Baker; Tim S. Meese; Mark A. Georgeson', year: '2013（在线2012）', publication: 'Vision Research, 76, 1–10',
    doi: '10.1016/j.visres.2012.09.019', url: 'https://pubmed.ncbi.nlm.nih.gov/23041562/', access: 'abstract',
    supports: '2026-11-06：原始摘要核对视觉任务、跨时段汇总与非稳定性；研究所测非稳定性较小，实际两种估计差异可忽略。正文仅用来说明层级与平均的解释问题，不推断听觉效应量；配图为独立解析构造。',
  },
  'pf-quickpsy-2016': {
    title: 'quickpsy: An R Package to Fit Psychometric Functions for Multiple Groups',
    authors: 'Daniel Linares; Joan López-Moliner', year: '2016', publication: 'The R Journal, 8(1), 122–131',
    doi: '10.32614/RJ-2016-008', url: 'https://journal.r-project.org/articles/RJ-2016-008/', access: 'fulltext',
    supports: '2026-11-06：原刊网页Statistical model、Point estimation and confidence intervals、工具范围等章节；核对二项似然、分组拟合和失误偏差限制。页面标注的2015-11-08不作期刊出版年；期刊与DOI书目为2016。未运行R包。',
  },
};
