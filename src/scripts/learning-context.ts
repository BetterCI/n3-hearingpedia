export function initLearningContexts(document: Document, pathId: string | null) {
  for (const context of document.querySelectorAll<HTMLElement>('[data-learning-context]')) {
    const panels = [...context.querySelectorAll<HTMLElement>('[data-route-panel]')];
    const active = panels.find(panel => panel.dataset.routePanel === pathId);
    if (!active) continue;
    context.hidden = false;
    active.hidden = false;
    const options = context.querySelector<HTMLElement>('[data-learning-options]');
    if (options) options.hidden = true;
    if (context.dataset.routePosition === 'bottom') document.querySelector<HTMLElement>('[data-directory-navigation]')?.setAttribute('hidden', '');
  }
}
