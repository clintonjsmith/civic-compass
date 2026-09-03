# Civic Compass

**Build a personal values charter, then evaluate any ballot against it — with cited
reasoning you can audit.** An ideology-neutral Claude Code plugin for civic decision-support.

Civic Compass does not tell you what to value or who to vote for. It supplies a *method*:
a structured way to write down what you actually believe, ranked by priority, with a clear
decision rule and a set of hard lines you won't cross — and then a disciplined, fact-checked
way to apply that framework to a real ballot. A progressive, a libertarian, and a
conservative running it get the same rigor and the same neutrality.

---

## Why this exists

Most voters face a long ballot, little information, and a firehose of persuasion. Civic
Compass is built on a simple bet: **democracy is healthier when individual decisions are
deliberate, grounded in verified facts, and traceable back to the voter's own values.**

Its contribution to election integrity is structural, not partisan:

1. **Fact-grounded, with citations.** Every claim and recommendation carries a source link —
   the direct antidote to the disinformation that erodes trust in elections.
2. **Transparent, auditable reasoning.** You can see exactly *why* a recommendation follows
   from *your* stated values. No black box, no thumb on the scale.
3. **Ideology-neutral by construction.** The tool never supplies values — it elicits yours.
4. **It follows facts even against your own premise.** If your assumption about a candidate
   is wrong, it tells you (with sources) rather than flattering you. It sharpens judgment
   instead of confirming it.

It is **decision-support, not persuasion.** See [Ethics & guardrails](#ethics--guardrails).

---

## What you get

Three commands (and the equivalent skills, which Claude can also invoke conversationally) —
the workflow is **build → ground (optional) → analyze**:

| Command | What it does | Output |
|---|---|---|
| **`/build-charter`** | A Socratic interview: your identity, influences, values (ranked into tiers), your decision rule, your hard disqualifiers, your positions, and trusted/distrusted sources. | `CHARTER.md` |
| **`/ground-charter`** | *(optional)* Reconciles your charter against your own writing — an X/Reddit/Bluesky export, blog, or essays — to confirm, sharpen, add, and **surface contradictions**, with dated citations. Catches what the interview missed. | updated `CHARTER.md` |
| **`/analyze-ballot`** | Ingests your ballot (PDF, photo, sample-ballot URL, or pasted text), enumerates every contest and measure, deep-researches each with citations, applies your charter, and surfaces genuine judgment calls to you. | `VOTING-GUIDE.md` |

Both produce plain Markdown files you own and can edit. Nothing leaves your machine except
the web searches needed to research candidates.

---

## Install

Civic Compass is distributed as a Claude Code plugin. The repo doubles as its own marketplace.

```
# 1. Add this repo as a plugin marketplace
/plugin marketplace add clintonjsmith/civic-compass

# 2. Install the plugin
/plugin install civic-compass@civic-compass
```

Or open the interactive menu with `/plugin` and enable it there.

> **Note:** Claude Code's plugin manifest format has evolved across versions. If install
> fails, check the current schema with `/plugin` and the official Claude Code plugin docs,
> then adjust `.claude-plugin/marketplace.json` and `plugins/civic-compass/.claude-plugin/plugin.json`.

---

## Use it

```
/build-charter                       # ~15-30 min interview → CHARTER.md
/ground-charter ./my-x-archive       # optional: validate it against your own posts
/analyze-ballot ./my-ballot.pdf      # point it at your ballot → VOTING-GUIDE.md
```

Build the charter once; reuse it every election. Re-run `/build-charter` anytime to refine —
it keeps a change log. The charter is the source of truth; the guide always traces back to it.

**Grounding (optional, recommended).** If you have a data export of your own writing (e.g.,
*X → Settings → Your account → Download an archive of your data*), `/ground-charter` reconciles
your charter against what you've actually posted and liked — confirming, sharpening, and
flagging anything that contradicts your stated self-image. Your archive is sensitive personal
data: it stays **local**, only text is read, and neither the archive nor a personalized charter
should ever be committed to a public repo.

---

## Privacy — read before you run `/ground-charter`

Civic Compass generates and consumes genuinely sensitive material. Nothing leaves your
machine except the web searches used to research candidates, but what lands *on* your
machine deserves care.

**Your charter is sensitive-category data.** A written record of your political values,
under your name, is treated as a special category of personal data in many jurisdictions
(GDPR Art. 9 and equivalents). Publishing it is irreversible — forks, caches, and archive
scrapers mean you cannot take it back.

**A social export is far more than your posts.** If you feed `/ground-charter` a full X
archive, be aware that the download contains — well beyond the public timeline —

- **direct messages**, including the other person's words and account IDs (third-party
  data you cannot consent away on their behalf)
- your **phone number** and email-change history
- an **IP audit**: every login IP with timestamps, i.e. a geolocation history
- **private AI chat** transcripts
- **likes**, which are no longer publicly browsable and reveal positions you never posted
- **block and mute lists**, and ad-targeting inferences about you

`/ground-charter` reads text only and never transmits the archive. Even so, unpack it
outside any repo, and delete it when you're done.

**This repo ships a `.gitignore` that blocks all of it** — charters, voting guides, ballot
PDFs and photos, and social exports. Leave those rules in place. If you ever intend to
publish a charter, force-add that single file deliberately rather than loosening the list.

---

## How it works (the method)

The full method is in [`reference/METHODOLOGY.md`](plugins/civic-compass/reference/METHODOLOGY.md).
In brief, the charter captures:

- **Ranked value tiers** — *Tier-0 hard gates* (disqualifiers, absolute) → *Tier-1
  load-bearing* (your one or two non-negotiable priorities) → *Tier-2 core* → *Tier-3
  preferences*. Higher tiers dominate lower ones.
- **A decision rule** — *your* selection principle (e.g., "most aligned electable
  candidate," "best on climate," "most pro-liberty"), bounded by the hard gates.
- **A validation procedure** — gates first, then viability, then tier-scoring, then the rule;
  with an explicit *decline-to-vote vs. cross-camp* test for when your preferred side fails a gate.
- **A due-diligence & sourcing standard** — deep background (not headlines), cite everything,
  follow facts even against your premise.

See worked, fictional examples for two different worldviews:
[progressive](plugins/civic-compass/examples/example-progressive-charter.md) ·
[libertarian](plugins/civic-compass/examples/example-libertarian-charter.md).

---

## Ethics & guardrails

- **Decision-support, not persuasion.** Civic Compass helps you apply *your* values. It will
  not try to change them, and it will not nudge you toward a party or candidate.
- **Neutral by construction.** No built-in ideology. The examples deliberately span the spectrum.
- **Facts over agreement.** It is instructed to correct you when the evidence contradicts your
  assumption, and to cite sources so you can verify.
- **Your data is yours.** The charter and guide are local Markdown files that never leave
  your machine. See [Privacy](#privacy--read-before-you-run-ground-charter) before pointing
  the tool at a social export or committing anything.
- **Verify logistics with official sources.** For registration, deadlines, polling places, and
  official candidate lists, always rely on your election authority (e.g., your Secretary of
  State or county registrar) — not this tool.
- **It can be wrong.** Research is only as good as what's online and current; treat the guide
  as a well-reasoned draft to check, not gospel.

---

## Contributing

Improvements to the *method*, templates, and neutral examples are welcome. Please keep the
core ideology-neutral: contributions that bias the scaffolding toward any party or worldview
will be declined. Additional fictional example charters from underrepresented viewpoints are
especially welcome — they strengthen the neutrality guarantee.

## License

MIT — see [LICENSE](LICENSE).
