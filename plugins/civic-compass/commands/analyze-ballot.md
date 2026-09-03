---
description: Evaluate a ballot against your CHARTER.md and produce a sourced VOTING-GUIDE.md.
argument-hint: "[path or URL to your ballot, or paste contests]"
---

Run the **analyze-ballot** skill for the user. Read and follow
`${CLAUDE_PLUGIN_ROOT}/skills/analyze-ballot/SKILL.md` exactly, using the method in
`${CLAUDE_PLUGIN_ROOT}/reference/METHODOLOGY.md` and the template at
`${CLAUDE_PLUGIN_ROOT}/templates/VOTING-GUIDE.template.md`.

First load `CHARTER.md` (if absent, offer `/build-charter` first — do not invent values).
Then ingest the ballot, enumerate every contest, deep-research each candidate with citations,
apply the charter's tiers and decision rule (including the decline-vs-cross logic), surface
genuine judgment calls to the user, and write `VOTING-GUIDE.md`. Follow facts even when they
contradict an assumption. Ballot input / context: $ARGUMENTS
