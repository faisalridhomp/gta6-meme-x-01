// gta6-meme-x-01 entry (Node 22, standard library only): the entry is the X
// post itself — this program hands the grader what it needs from the repo:
// POST.json (the post's address, filled in after the post goes live) and
// meme.png (the finished meme, made in this session: AI Vice City background
// + the real make.fun ghost mark + the "WASTED -> PAID" joke, see gen_meme.py).
// Deterministic: the same bytes out on every run. No network, no wall clock,
// no files outside the repository.
//
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
for (const file of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, file), join(OUTPUT_DIR, file));
  } catch (err) {
    console.error(`${file} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}
