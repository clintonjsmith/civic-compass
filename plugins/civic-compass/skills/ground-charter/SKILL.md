---
name: ground-charter
description: >
  Ground/validate a CHARTER.md against the user's own writing record — a social-media export
  (X/Twitter, Reddit, Bluesky, Mastodon, Facebook), a blog/Substack, or a folder of essays.
  Parse the corpus programmatically, scan themes, pull dated representative quotes, then confirm
  / sharpen / correct the charter with citations — and surface contradictions honestly. Use when
  the user provides a data export or posting history, or asks to ground, validate, back, or
  fact-check their charter against their own words.
---

# Ground Charter

Turn a charter from *stated* values into *evidenced* values by reconciling it with the user's
actual public writing — and, crucially, **surfacing where the record contradicts what they
stated.** The anti-sycophancy rule applies to a person's self-image too: people are not always
who they say they are, and the record sometimes knows better.

Inputs: `CHARTER.md` + a corpus of the user's own writing — an X/Twitter archive `.zip`, a
Reddit / Bluesky / Mastodon / Facebook export, a blog/Substack, or a folder of essays.
Reusable starter script: `${CLAUDE_PLUGIN_ROOT}/scripts/x-archive-scan.py`.

## Prime directives

- **Process programmatically. Never dump the corpus into context.** Thousands of posts will
  blow the context window and bury the signal. Use a script to parse, theme-scan, count, and
  sample; read only the samples.
- **Read originals AND endorsements.** What someone *amplifies* (retweets, likes, shares) is
  signal, not noise — often the clearest signal. Analyze both.
- **Quote with dates.** Every charter claim you confirm/sharpen gets a dated quote as a citation.
- **Confirm, sharpen, AND correct.** Do not cherry-pick confirmations. Classify the evidence
  honestly, and report contradictions plainly.
- **Privacy first** (see Guardrails).

## Procedure

1. **Identify corpus + format.** For an X export `.zip`: extract only the **text** files (skip
   media) — `data/tweets.js` (posts, replies, retweets), `data/like.js` (likes),
   `data/account.js`. Other platforms have analogous JSON/CSV exports; a blog is just text files.
2. **Stats pass.** Total items, date range, and the split: originals vs. replies vs.
   retweets/shares vs. likes.
3. **Theme scan — derive buckets FROM THE CHARTER.** Build keyword buckets from the charter's
   own tiers, gates, and issue positions, plus a few open "discovery" buckets to catch themes the
   interview missed. Count each theme across originals / retweets / likes, then print dated samples.
   (`x-archive-scan.py` does this; edit its `THEMES` dict to match the charter.)
4. **Classify the evidence.** For each charter claim, label the record: **CONFIRMS / SHARPENS /
   ADDS NEW / CONTRADICTS / NO SIGNAL.** Note new themes the interview missed entirely (a whole
   vocation, an issue they care about, a recurring value).
5. **Reconcile the charter.** Add a "Grounded by the record" section with dated quotes; make
   targeted edits to sections the evidence sharpens; and for any **contradiction**, do NOT
   silently overwrite a stated value — present the conflict to the user and let them resolve it.
6. **Log it.** Add a change-log entry and summarize: confirmed / sharpened / new / contradicted.

## Output

Update `CHARTER.md` (evidence section + targeted edits + change log). Give the user a plain
summary of what their record confirmed, sharpened, added, and — if anything — contradicted.

## Guardrails (privacy is paramount)

- **The archive is sensitive personal data.** Keep it **local**. Extract only text; never upload
  it to any service, never commit it to a repo, and explicitly remind the user to keep both the
  archive and any personalized charter out of public repositories.
- **Distinguish voices.** A user's own posts ≠ content they quoted to *criticize*. Don't
  attribute a quote-tweeted opponent's view to the user.
- **Apply anti-sycophancy to the user.** If the record contradicts their stated self-image, say
  so, with evidence — gently, but say it.
