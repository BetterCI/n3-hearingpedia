export interface ShareCardData {
  title: string;
  english: string;
  summary: string;
  area: string;
  kind: string;
  depth: string;
  facts: { label: string; value: string }[];
  updated: string;
  status: string;
  reviewNote: string;
  references: number;
  articleUrl: string;
  qrDataUrl: string;
}

const fonts = '"PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", system-ui, sans-serif';
const width = 540;
const margin = 44;
const textWidth = width - margin * 2;

// Keep Latin words together; split only tokens that cannot fit on a line.
function wrapText(ctx: CanvasRenderingContext2D, text: string, maxWidth: number): string[] {
  const lines: string[] = [];
  for (const paragraph of text.split(/\r?\n/)) {
    let line = '';
    const tokens = paragraph.match(/[A-Za-z0-9]+(?:[’'._/-][A-Za-z0-9]+)*|./gu) || [];
    for (const token of tokens) {
      if (ctx.measureText(line + token).width <= maxWidth) { line += token; continue; }
      if (line.trim()) lines.push(line.trimEnd());
      line = token.trimStart();
      if (ctx.measureText(line).width > maxWidth) {
        const chars = [...line];
        line = '';
        for (const char of chars) {
          if (ctx.measureText(line + char).width > maxWidth && line) { lines.push(line); line = ''; }
          line += char;
        }
      }
    }
    if (line.trim()) lines.push(line.trimEnd());
  }
  return lines;
}

export async function createShareCard(data: ShareCardData): Promise<{ blob: Blob; src: string }> {
  await document.fonts.ready;
  const qr = new Image();
  qr.src = data.qrDataUrl;
  await qr.decode();
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  if (!ctx) throw new Error('Canvas unavailable');
  const font = (size: number, weight = 400) => { ctx.font = `${weight} ${size}px ${fonts}`; };
  font(38, 700);
  const title = wrapText(ctx, data.title, textWidth);
  font(16);
  const english = wrapText(ctx, data.english, textWidth);
  font(20);
  const summary = wrapText(ctx, data.summary, textWidth - 15);
  const facts = data.facts.map(fact => {
    font(13, 600);
    const label = wrapText(ctx, fact.label, textWidth - 36);
    font(17);
    const value = wrapText(ctx, fact.value, textWidth - 36);
    return { label, value, height: 24 + label.length * 20 + value.length * 27 };
  });
  font(13);
  const classification = wrapText(ctx, `${data.area} / ${data.kind}`, textWidth);
  font(12);
  const review = wrapText(ctx, data.reviewNote, textWidth);
  const titleY = 144;
  const englishY = titleY + title.length * 51 + 9;
  const classificationY = englishY + english.length * 24 + 23;
  const summaryY = classificationY + classification.length * 21 + 31;
  const factsY = summaryY + summary.length * 33 + 35;
  const factsBottom = factsY + 36 + facts.reduce((height, fact) => height + fact.height + 9, 0);
  const metaY = factsBottom + 11;
  const footerY = metaY + 30 + review.length * 20 + 30;
  const qrSide = qr.naturalWidth / 2;
  const footerWidth = textWidth - qrSide - 20;
  font(12);
  const host = wrapText(ctx, new URL(data.articleUrl).host, footerWidth);
  const height = Math.max(720, Math.ceil(footerY + Math.max(112 + host.length * 17, qrSide) + 43));
  canvas.width = width * 2;
  canvas.height = height * 2;
  ctx.scale(2, 2);
  ctx.textBaseline = 'top';

  const background = ctx.createLinearGradient(0, 0, width, height);
  background.addColorStop(0, '#f2eefb');
  background.addColorStop(.4, '#ffffff');
  background.addColorStop(1, '#f6f7fb');
  ctx.fillStyle = background;
  ctx.fillRect(0, 0, width, height);
  ctx.fillStyle = '#765aa5';
  ctx.fillRect(0, 0, width, 6);

  const text = (value: string, x: number, y: number, size: number, color = '#263047', weight = 400) => {
    font(size, weight); ctx.fillStyle = color; ctx.fillText(value, x, y);
  };
  const block = (lines: string[], x: number, y: number, size: number, lineHeight: number, color = '#263047', weight = 400) => {
    lines.forEach((line, index) => text(line, x, y + index * lineHeight, size, color, weight));
  };
  const rule = (y: number) => { ctx.fillStyle = '#dfd9ec'; ctx.fillRect(margin, y, textWidth, 1); };

  text('n³', margin, 35, 36, '#6e5199', 700);
  text('Hearingpedia', margin + 59, 45, 20, '#4b3a68', 600);
  text('听觉科学 · 概念、机制与方法', margin, 87, 12, '#79738c');
  // A small waveform echoes the site's hearing-science identity.
  ctx.strokeStyle = '#b8a6d3'; ctx.lineWidth = 2;
  for (let i = 0; i < 15; i++) {
    const amplitude = 3 + Math.pow(Math.sin(i * .6), 2) * 20;
    const x = 386 + i * 7;
    ctx.beginPath(); ctx.moveTo(x, 61 - amplitude); ctx.lineTo(x, 61 + amplitude); ctx.stroke();
  }
  block(title, margin, titleY, 38, 51, '#28243c', 700);
  block(english, margin, englishY, 16, 24, '#80728e');
  block(classification, margin, classificationY, 13, 21, '#6e5199');
  ctx.fillStyle = '#765aa5'; ctx.fillRect(margin, summaryY, 3, summary.length * 33 - 7);
  block(summary, margin + 15, summaryY - 2, 20, 33);

  text('核心信息', margin, factsY, 14, '#6e5199', 600);
  let y = factsY + 36;
  for (const fact of facts) {
    ctx.fillStyle = '#f2f3f8';
    ctx.beginPath(); ctx.roundRect(margin, y, textWidth, fact.height, 9); ctx.fill();
    block(fact.label, margin + 18, y + 12, 13, 20, '#81788f', 600);
    block(fact.value, margin + 18, y + 12 + fact.label.length * 20, 17, 27);
    y += fact.height + 9;
  }
  text(`${data.depth} · ${data.status}`, margin, metaY, 12, '#756b84');
  const updated = `更新 ${data.updated.replaceAll('-', '.')}`;
  font(12);
  text(updated, width - margin - ctx.measureText(updated).width, metaY, 12, '#756b84');
  block(review, margin, metaY + 28, 12, 20, '#8d8497');
  rule(footerY - 16);

  // QR pixels map 1:1 to the exported PNG, without resampling.
  ctx.imageSmoothingEnabled = false;
  ctx.drawImage(qr, width - margin - qrSide, footerY, qrSide, qrSide);
  font(21, 600);
  block(wrapText(ctx, '扫码，继续探索', footerWidth), margin, footerY + 16, 21, 29, '#4b3a68', 600);
  text('完整词条与参考文献', margin, footerY + 56, 14, '#81788f');
  text(`${data.references} 项参考来源`, margin, footerY + 80, 12, '#81788f');
  block(host, margin, footerY + 112, 12, 17, '#81788f');

  const blob = await new Promise<Blob>((resolve, reject) => {
    canvas.toBlob(value => value ? resolve(value) : reject(new Error('PNG export failed')), 'image/png');
  });
  return { blob, src: canvas.toDataURL('image/png') };
}
