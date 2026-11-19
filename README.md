# gta6-meme-x-01 — "WASTED → PAID"

Entry for make.fun's "Post a GTA 6 meme on X" ($500, top 50 paid).
Deadline 2026-11-23T14:00:00Z. No submission yet — the post goes out from
@0xfrrr first, then POST.json is filled with its real URL and this is submitted.

## The meme

`meme.png` (1024×1024, also legible shrunk to 480×480, which is how the
judge sees it): a neon Vice City street at sunset with a white sports car,
the real make.fun ghost mark front and centre, and the joke in GTA's own
language — **WASTED** struck through in red, replaced by big green **PAID.**

- Top: "WAITED 13 YEARS FOR GTA 6"
- Bottom: "MY AGENT MADE THIS MEME. make.fun PAID FOR IT."

Made by `gen_meme.py` (Pillow): AI-generated Vice City background
(`assets/media-generation-gta6-meme-bg-0-*.png`) + the real press-kit ghost
mark (`assets/mark-1024.png`, https://make.fun/press/) + text. Re-run it to
regenerate the meme byte-for-byte.

## The post (exact text for Faisal to post from @0xfrrr)

Attach `meme.png` as the first (only) picture, then post this text:

> 13 years waiting for GTA 6. my agent made this meme in seconds — @makefunai paid real money for it. agents earn on make.fun. play code: makefun-mackerel-echo-camp https://make.fun/bounty/gta6-meme-x-01

Why this text: it carries make.fun as a link AND the @makefunai tag, the
play code `makefun-mackerel-echo-camp`, and the pitch (people + their AI
agents earn real money on make.fun) in the meme's own voice.

## After the post is live

1. Copy the post URL (`https://x.com/0xfrrr/status/<id>`) into `POST.json`.
2. `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
3. From the kit dir:
   `node cli/makefun.mjs check --kit . --repo <this repo> --transcripts transcripts.tar.gz`
4. Submit:
   `node cli/makefun.mjs submit --competition gta6-meme-x-01 --repo-url https://github.com/faisalridhomp/<repo> --commit <sha> --title "WASTED -> PAID" --bundle transcripts.tar.gz --keypair ~/workspace/makefun/makefun-keypair.json`

## Notes

- `makefun record` does NOT apply to this competition (HTTP 400: "does not
  take recorded transcripts") — transcripts are uploaded as a bundle with
  the submission instead. No recording slot was consumed.
- Play code verified via the API (`X-API-Key` header): code 0 is
  `makefun-mackerel-echo-camp`.
- Kit: fresh download `~/workspace/makefun/gta6-meme-x-01-kit-v2/`
  (bundle 06b9828f…, harness@8430b248…).
- Repo anchor: `makefun anchor d5542f38a7f9538eb93d98f8de923dc2804ed7c5`,
  drand round 34102855, LICENSE MIT.
