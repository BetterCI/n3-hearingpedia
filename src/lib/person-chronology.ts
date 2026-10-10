interface PersonEntry {
  data: { slug: string; core_work?: { year: number } };
}

// Use the selected original work, including original book editions, rather than
// article updates or later collections. Unverified years remain at the end.
export function comparePersonCoreWork(a: PersonEntry, b: PersonEntry): number {
  return (a.data.core_work?.year ?? Number.MAX_SAFE_INTEGER)
    - (b.data.core_work?.year ?? Number.MAX_SAFE_INTEGER)
    || a.data.slug.localeCompare(b.data.slug, 'en');
}
