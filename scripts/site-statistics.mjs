import { readdir, readFile, writeFile } from 'node:fs/promises';
import { parseFrontmatter } from '@astrojs/markdown-remark';
import { summarizeSite, formatReadmeStatistics } from '../src/lib/site-statistics.ts';

const mode = process.argv[2];
if (!['--check', '--write'].includes(mode)) throw new Error('Usage: node scripts/site-statistics.mjs --check | --write');
const files = (await readdir('src/content/concepts')).filter(file => file.endsWith('.md'));
const entries = await Promise.all(files.map(async file => ({
  data: parseFrontmatter(await readFile(`src/content/concepts/${file}`, 'utf8')).frontmatter,
})));
const statistics = summarizeSite(entries);
const expected = formatReadmeStatistics(statistics);
const readme = (await readFile('README.md', 'utf8')).replaceAll('\r\n', '\n');
const block = /<!-- site-statistics:start -->[\s\S]*?<!-- site-statistics:end -->/;
if (!block.test(readme)) throw new Error('README statistics markers are missing');
if (mode === '--write') {
  await writeFile('README.md', readme.replace(block, expected));
  console.log('Updated README statistics from current source data.');
} else if (readme.match(block)[0] !== expected) {
  throw new Error('README statistics are out of date. Run pnpm stats:update and commit README.md.');
} else {
  console.log('README statistics match current source data.');
}
console.log(JSON.stringify(statistics, null, 2));
