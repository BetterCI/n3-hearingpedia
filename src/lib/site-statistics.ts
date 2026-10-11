import { knowledgeAreas, kindLabels } from '../data/knowledge.ts';
import { knowledgeRelations } from '../data/relations.ts';
import { learningPaths } from '../data/paths.ts';
import { domains } from '../data/domains.ts';
import { references } from '../data/references.ts';

interface Entry {
  data: { kind: string; depth?: string; status: string };
}

export function summarizeSite(entries: Entry[]) {
  return {
    entries: entries.length,
    conceptEntries: entries.filter(entry => entry.data.kind !== 'person').length,
    people: entries.filter(entry => entry.data.kind === 'person').length,
    inDepthConcepts: entries.filter(entry => entry.data.kind !== 'person' && entry.data.depth === 'in-depth').length,
    knowledgeAreas: knowledgeAreas.length,
    conceptKinds: Object.keys(kindLabels).length,
    registeredReferences: Object.keys(references).length,
    relationships: knowledgeRelations.length,
    learningPaths: learningPaths.length,
    domains: domains.length,
    draft: entries.filter(entry => entry.data.status === 'draft').length,
    reviewed: entries.filter(entry => entry.data.status === 'reviewed').length,
    stable: entries.filter(entry => entry.data.status === 'stable').length,
    needsUpdate: entries.filter(entry => entry.data.status === 'needs-update').length,
  };
}

export function formatReadmeStatistics(stats: ReturnType<typeof summarizeSite>) {
  return [
    '<!-- site-statistics:start -->',
    `- ${stats.entries} 个百科词条：${stats.conceptEntries} 个概念与领域词条、${stats.people} 个人物词条；概念与领域词条中有 ${stats.inDepthConcepts} 篇深度词条。`,
    `- ${stats.knowledgeAreas} 个知识层面、${stats.conceptKinds} 种词条类型、${stats.relationships} 条带说明的知识关系。`,
    `- ${stats.registeredReferences} 项登记参考来源、${stats.domains} 个学科索引、${stats.learningPaths} 条学习路径。登记来源数量不代表已完成科学审阅。`,
    `- 审阅状态：${stats.draft} 篇待审阅、${stats.reviewed} 篇已审阅、${stats.stable} 篇稳定、${stats.needsUpdate} 篇待更新。`,
    '<!-- site-statistics:end -->',
  ].join('\n');
}
