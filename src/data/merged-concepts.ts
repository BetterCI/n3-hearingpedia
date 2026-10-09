/**
 * Historical article routes for the Mandarin phonetics consolidation (2026-10-09).
 * Inputs: none. Output: old slugs, surviving articles and stable section anchors.
 * Side effects: none; the Astro article route renders redirects from these records.
 * Boundary: slugs must be retired and each target/anchor must exist; verify checks both.
 * Usage: expand getStaticPaths with mergedConceptRedirects and validate built redirects.
 * Copyright: Huali Zhou, zhouhuali224@gmail.com
 * School of Electronics and Information Engineering, Heyuan Polytechnic, Heyuan, Guangdong, China.
 */

/** A retired article slug maps to one surviving article and its section anchor. */
export interface MergedConceptRedirect {
  slug: string;
  target: string;
  anchor: string;
}

export const mergedConceptRedirects = [
  { slug: 'mandarin-initials', target: 'mandarin-consonants', anchor: 'initials' },
  { slug: 'mandarin-consonant-ipa', target: 'mandarin-consonants', anchor: 'ipa' },
  { slug: 'mandarin-alveolar-retroflex', target: 'consonant-place-of-articulation', anchor: 'alveolar-retroflex' },
  { slug: 'mandarin-alveolo-palatal', target: 'consonant-place-of-articulation', anchor: 'alveolo-palatal' },
  { slug: 'plosive', target: 'consonant-manner-of-articulation', anchor: 'plosive' },
  { slug: 'affricate', target: 'consonant-manner-of-articulation', anchor: 'affricate' },
  { slug: 'fricative', target: 'consonant-manner-of-articulation', anchor: 'fricative' },
  { slug: 'nasal-consonant', target: 'consonant-manner-of-articulation', anchor: 'nasal' },
  { slug: 'lateral-consonant', target: 'consonant-manner-of-articulation', anchor: 'lateral' },
] as const satisfies readonly MergedConceptRedirect[];
