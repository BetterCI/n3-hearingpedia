import test from 'node:test';
import assert from 'node:assert/strict';
import { initLearningContexts } from '../src/scripts/learning-context.ts';

function article() {
  const createContext = position => ({
    hidden: position === 'bottom', dataset: { routePosition: position },
    options: { hidden: false },
    panels: ['intro-sound-hearing', 'mechanisms'].map(id => ({ hidden: true, dataset: { routePanel: id } })),
    querySelectorAll() { return this.panels; },
    querySelector() { return position === 'top' ? this.options : null; },
  });
  const contexts = [createContext('top'), createContext('bottom')];
  const directory = { hidden: false, setAttribute(name) { if (name === 'hidden') this.hidden = true; } };
  return { contexts, directory, document: { querySelectorAll: () => contexts, querySelector: () => directory } };
}

test('an incoming route replaces directory navigation and selects matching panels at both ends', () => {
  const page = article();
  initLearningContexts(page.document, 'intro-sound-hearing');
  for (const context of page.contexts) {
    assert.equal(context.hidden, false);
    assert.equal(context.panels[0].hidden, false);
    assert.equal(context.panels[1].hidden, true);
  }
  assert.equal(page.contexts[0].options.hidden, true);
  assert.equal(page.directory.hidden, true);
});

test('a complete route can be selected independently of introductory routes', () => {
  const page = article();
  initLearningContexts(page.document, 'mechanisms');
  assert(page.contexts.every(context => context.panels[0].hidden && !context.panels[1].hidden));
});

test('independent reading, unknown routes and routes absent from this article retain the fallback', () => {
  for (const id of [null, '', 'unknown', 'intro-hearing-assessment', '<script>']) {
    const page = article();
    initLearningContexts(page.document, id);
    assert.equal(page.contexts[0].options.hidden, false);
    assert.equal(page.contexts[1].hidden, true);
    assert(page.contexts.every(context => context.panels.every(panel => panel.hidden)));
    assert.equal(page.directory.hidden, false);
  }
});
