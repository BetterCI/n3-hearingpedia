import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { crc32, deflateRawSync } from 'node:zlib';

const names = [
  'README.md',
  'basic-entry-template.md',
  'in-depth-entry-template.md',
  'ai-writing-prompts.md',
  'submission-template.md',
  'technical-integration.md',
];
const destination = resolve('public/downloads/contributor-kit');
await mkdir(destination, { recursive: true });
const entries = await Promise.all(names.map(async name => ({
  name,
  content: await readFile(resolve('docs/contributor-kit', name)),
})));

// Package the same source bytes as the individual downloads. A fixed ZIP date
// keeps the archive reproducible without a new package or a Python build step.
const localParts = [], centralParts = [];
let offset = 0;
for (const entry of entries) {
  await writeFile(join(destination, entry.name), entry.content);
  const name = Buffer.from(entry.name, 'utf8');
  const compressed = deflateRawSync(entry.content);
  const checksum = crc32(entry.content);
  const local = Buffer.alloc(30);
  local.writeUInt32LE(0x04034b50, 0);
  local.writeUInt16LE(20, 4);
  local.writeUInt16LE(0x0800, 6);
  local.writeUInt16LE(8, 8);
  local.writeUInt16LE(0x0021, 12); // 1980-01-01
  local.writeUInt32LE(checksum, 14);
  local.writeUInt32LE(compressed.length, 18);
  local.writeUInt32LE(entry.content.length, 22);
  local.writeUInt16LE(name.length, 26);
  localParts.push(local, name, compressed);

  const central = Buffer.alloc(46);
  central.writeUInt32LE(0x02014b50, 0);
  central.writeUInt16LE(20, 4);
  central.writeUInt16LE(20, 6);
  central.writeUInt16LE(0x0800, 8);
  central.writeUInt16LE(8, 10);
  central.writeUInt16LE(0x0021, 14);
  central.writeUInt32LE(checksum, 16);
  central.writeUInt32LE(compressed.length, 20);
  central.writeUInt32LE(entry.content.length, 24);
  central.writeUInt16LE(name.length, 28);
  central.writeUInt32LE(offset, 42);
  centralParts.push(central, name);
  offset += local.length + name.length + compressed.length;
}

const directory = Buffer.concat(centralParts);
const end = Buffer.alloc(22);
end.writeUInt32LE(0x06054b50, 0);
end.writeUInt16LE(entries.length, 8);
end.writeUInt16LE(entries.length, 10);
end.writeUInt32LE(directory.length, 12);
end.writeUInt32LE(offset, 16);
const archive = Buffer.concat([...localParts, directory, end]);
await writeFile(join(destination, 'hearingpedia-contributor-kit-v0.1.zip'), archive);
console.log(`Prepared ${entries.length} contributor documents and their ZIP archive.`);
