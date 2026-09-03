---
description: Ground/validate your CHARTER.md against your own writing record (social export, blog, essays).
argument-hint: "[path to your data export .zip / folder, e.g. your X archive]"
---

Run the **ground-charter** skill for the user. Read and follow
`${CLAUDE_PLUGIN_ROOT}/skills/ground-charter/SKILL.md` exactly.

Load `CHARTER.md`, then reconcile it against the user's own writing corpus at the path they
provide. Process the corpus **programmatically** — never load thousands of posts into context;
use `${CLAUDE_PLUGIN_ROOT}/scripts/x-archive-scan.py` (edit its `THEMES` to match the charter)
for X archives, or adapt the parse step for other exports. Read originals AND likes/retweets.
Classify the evidence as confirms / sharpens / adds-new / contradicts, then update the charter
with dated citations — and surface any contradiction to the user rather than overwriting a
stated value. Treat the archive as sensitive local data: text only, never upload, never commit.

Corpus path / context: $ARGUMENTS
