import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const concepts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/concepts' }),
  schema: z.object({
    title: z.string(),
    english: z.string(),
    slug: z.string(),
    summary: z.string(),
    categories: z.array(z.string()).min(1),
    tags: z.array(z.string()),
    aliases: z.array(z.string()).default([]),
    level: z.array(z.string()).default(['graduate']),
    status: z.enum(['draft', 'reviewed', 'stable', 'needs-update']),
    last_updated: z.string(),
    authors: z.array(z.string()).default([]),
    reviewer: z.string().nullable().default(null),
    reviewed_at: z.string().nullable().default(null),
    literature_checked_at: z.string().nullable().default(null),
    related: z.array(z.object({ slug: z.string(), relation: z.enum(['prerequisite', 'mechanism', 'application', 'method', 'related']) })),
    references: z.array(z.string()).min(1),
    batch: z.number().int().positive().default(1),
    order: z.number(),
  }),
});

export const collections = { concepts };
