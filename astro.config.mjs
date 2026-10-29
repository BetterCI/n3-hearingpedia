import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { unified } from '@astrojs/markdown-remark';

const basePath = process.env.BASE_PATH || '/n3-hearingpedia';
const mergedFilterPath = `${basePath.replace(/\/$/, '')}/concepts/fir-and-iir-filters/`;

export default defineConfig({
  site: process.env.SITE_URL || 'https://betterci.github.io',
  base: basePath,
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/concepts/fir-filter/': mergedFilterPath,
    '/concepts/iir-filter/': mergedFilterPath,
  },
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [[rehypeKatex, { strict: 'warn', throwOnError: true }]],
    }),
  },
});
