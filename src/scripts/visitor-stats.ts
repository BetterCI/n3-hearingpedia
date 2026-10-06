type VisitorStats = {
  start: string; end: string; updatedAt: string; visits: number;
  countries: { name: string; visits: number }[];
};

export function initVisitorStats() {
  const section = document.querySelector<HTMLElement>('.visitor-stats');
  if (!section) return;
  const site = section.dataset.counterSite!;
  // Count only the published site; previews and local development remain excluded.
  if (location.hostname === 'betterci.github.io' && location.pathname.startsWith('/n3-hearingpedia/')) {
    const script = document.createElement('script');
    script.async = true;
    script.dataset.goatcounter = `${site}/count`;
    script.src = 'https://gc.zgo.at/count.js';
    document.head.append(script);
  }

  if (!section.dataset.statsUrl) return;
  void fetch(section.dataset.statsUrl, { signal: AbortSignal.timeout(8000) })
    .then(async response => {
      if (!response.ok) throw new Error('Statistics unavailable');
      return response.json() as Promise<VisitorStats>;
    }).then(data => {
      const dateValid = (value: string) => typeof value === 'string' && Number.isFinite(Date.parse(value));
      if (!dateValid(data.start) || !dateValid(data.end) || !dateValid(data.updatedAt)
          || !Number.isSafeInteger(data.visits) || data.visits < 0 || !Array.isArray(data.countries)
          || data.countries.some(item => typeof item.name !== 'string' || !Number.isSafeInteger(item.visits) || item.visits < 0)) return;
      const format = new Intl.NumberFormat('zh-CN');
      const date = new Intl.DateTimeFormat('zh-CN', { timeZone: 'Asia/Shanghai', month: 'numeric', day: 'numeric' });
      const set = (selector: string, value: string) => { section.querySelector<HTMLElement>(selector)!.textContent = value; };
      set('[data-stats-period]', `近 30 天 · ${date.format(new Date(data.start))}—${date.format(new Date(data.end))}`);
      set('[data-stats-visits]', format.format(data.visits));
      set('[data-stats-countries]', format.format(data.countries.length));
      const list = section.querySelector<HTMLUListElement>('ul')!;
      data.countries.slice(0, 5).forEach(country => {
        const item = document.createElement('li');
        item.textContent = `${country.name} ${format.format(country.visits)}`;
        list.append(item);
      });
      set('[data-stats-updated]', ` 更新于 ${date.format(new Date(data.updatedAt))}。`);
      section.hidden = false;
    }).catch(() => { /* Keep the footer compact until a real snapshot is available. */ });
}
