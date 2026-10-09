import type { CollectionEntry } from 'astro:content';
import QRCode from 'qrcode';
import { knowledgeAreaById, kindLabels } from '../data/knowledge';
import type { ShareCardData } from './share-card';

export async function buildShareCardData(data: CollectionEntry<'concepts'>['data'], articleUrl: string): Promise<ShareCardData> {
  const modules = QRCode.create(articleUrl, { errorCorrectionLevel: 'M' }).modules.size;
  const qrScale = Math.max(1, Math.floor(288 / (modules + 8)));
  const qrDataUrl = await QRCode.toDataURL(articleUrl, {
    errorCorrectionLevel: 'M', margin: 4, scale: qrScale,
    color: { dark: '#20283b', light: '#ffffff' },
  });
  const statusLabels = { draft: '待审阅', reviewed: '已审阅', stable: '稳定版本', 'needs-update': '待更新' };
  return {
    title: data.title, english: data.english, summary: data.summary,
    area: knowledgeAreaById[data.knowledge_area].title,
    kind: kindLabels[data.kind], depth: data.depth === 'standard' ? '基础词条' : '深度词条',
    facts: data.key_facts.slice(0, 4),
    updated: data.last_updated, status: statusLabels[data.status],
    reviewNote: data.status === 'draft' ? 'AI 辅助编写 · 尚未完成专业审阅'
      : data.status === 'needs-update' ? '内容待更新 · 请阅读原词条了解详情'
      : `专业审阅：${data.reviewer} · ${data.reviewed_at}`,
    references: data.references.length, articleUrl, qrDataUrl,
  };
}
