---
name: analyze-ballot
description: >
  Evaluate a ballot against the user's CHARTER.md. Ingest a ballot (PDF, photo, sample-ballot
  URL, or pasted text), enumerate every contest and measure, deep-research each candidate with
  citations, apply the charter's ranked tiers and decision rule (including the decline-vs-cross
  logic), surface genuine judgment calls to the user, and write a sourced VOTING-GUIDE.md. Use
  when the user wants to analyze, rank, or get recommendations on a ballot, election, or
  specific races/measures.
---

# Analyze Ballot

Apply the user's charter to a real ballot and produce **VOTING-GUIDE.md** — a per-contest set
of recommendations, each traceable to the charter and backed by citations.

Method reference: `${CLAUDE_PLUGIN_ROOT}/reference/METHODOLOGY.md`
Guide template: `${CLAUDE_PLUGIN_ROOT}/templates/VOTING-GUIDE.template.md`

## Preconditions

1. **Load the charter.** Read `CHARTER.md`. If none exists, say so and offer to run
   `/build-charter` first — do not invent values to fill the gap.
2. **Ingest the ballot.** Accept a PDF, photo, sample-ballot URL, or pasted text. Read it
   fully and **enumerate every contest and measure** — don't skip down-ballot races.
3. **Identify the election system**, because it changes strategy:
   - *Top-two / jungle primary* — all parties on one ballot; top two advance regardless of party.
   - *Closed/partisan primary* — only your party's contest; registration matters.
   - *Ranked-choice* — rank rather than pick one.
   - *General* / *nonpartisan* / *ballot measures*.
   State the implication for the user's decision rule (e.g., viability and cross-camp logic
   work differently under each).

## Per-contest procedure

For each contest, follow the charter's validation procedure:

1. **Run the user's Tier-0 gates first.** Any hit → disqualified; stop scoring that candidate.
   Do not let strength on a top issue "buy back" a gated candidate.
2. **Establish viability** — who can realistically win/advance? Identify the live top contenders.
3. **Score the gate-survivors** on the user's value tiers (Tier-1 load-bearing dominates).
4. **Apply the decision rule** to pick among acceptable, viable candidates.
5. **If the preferred camp's candidates all fail**, apply the decline-vs-cross test from the
   charter: cross to an acceptable viable alternative if one exists; otherwise undervote.
6. For ballot measures: score against the value tiers; note strategic structure (e.g.,
   competing measures where the higher vote total wins).

## The standards (non-negotiable — from the charter)

- **Deep background, not headlines.** Vet each viable candidate *beyond* the obvious: their
  record on the user's gate issues, scandals/corruption, competence/fit for the specific
  office — not just one famous vote. Shallow vetting produces wrong answers.
- **Cite every position.** Every factual claim and recommendation gets a source link. Prefer
  primary sources and reputable outlets; flag when a strong claim rests only on a partisan
  source, and seek corroboration.
- **Follow facts even against the user's premise.** If the user (or you) assumed something
  about a candidate and the evidence contradicts it, say so plainly with sources. Never
  propagate an unverified claim to be agreeable.
- **Verify recency.** Elections are time-sensitive and may post-date your training. Use web
  search for current candidates, results, and developments; rely on the ballot document for the
  authoritative candidate list.
- **Surface forks; don't silently decide.** When a pick is a genuine judgment call (a close
  values trade-off, a borderline gate, a viability-vs-alignment tension), present the options
  and the trade-off and let the *user* choose — then record their decision.
- **Stay neutral.** Apply the user's framework, not your own. Don't editorialize for or against
  parties beyond what their charter implies.

## Output

Write **VOTING-GUIDE.md** from the template, with:
- A **ballot card** (quick reference: one line per contest with the pick + confidence/status).
- A **full write-up per contest**: recommendation, reasoning tied to specific charter tiers,
  the strongest case against, viability notes, and a **Sources** line of links.
- A **cross-check** section if the charter names trusted sources — note agreements and
  document any conscious departures with reasoning.
- An **open items** list (unresolved forks, picks needing deeper vetting, logistics to verify
  with official election sources).

Close by reminding the user to confirm logistics (deadlines, polling place, official candidate
list) with their election authority, and that the guide is a reasoned draft to verify, not gospel.
