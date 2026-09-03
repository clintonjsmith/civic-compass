# The Civic Compass Method

This is the ideology-neutral scaffolding behind both skills. It describes *how* to structure
and apply a set of values — never *which* values to hold. Any worldview plugs into the same frame.

---

## 1. Ranked value tiers

Values are useless for deciding until they're *ordered*. Civic Compass ranks them into tiers;
higher tiers dominate lower ones.

- **Tier 0 — Hard gates (disqualifiers).** Things that make a candidate or measure unacceptable
  *regardless of merit on everything else.* These are character/fitness lines, not policy
  preferences. They are **absolute** — never traded away. (Examples vary by user: one person's
  gate is anti-democratic conduct; another's is corruption; another's is a specific rights
  violation.)
- **Tier 1 — Load-bearing.** The one or two priorities that do the most work in close calls.
  Often a single value the user considers primary.
- **Tier 2 — Core.** Important, frequently decisive, but below the load-bearing value.
- **Tier 3 — Strong preferences.** Real tilts that break ties but yield to higher tiers.

**Absolute vs. tradeable.** Tier-0 gates are absolute. Lower-tier negatives — even severe ones
— are *heavy but tradeable*: a candidate can be wrong on a Tier-1 issue and still be the pick
if the alternative is worse or non-viable. Keeping this distinction explicit prevents two
errors: treating a policy disagreement as disqualifying, and treating a true disqualifier as
merely a heavy mark.

---

## 2. The decision rule (parameterized)

Every user needs an explicit **selection principle** — the rule for choosing among candidates.
It has two common components:

- **Direction:** what you're maximizing ("most aligned," "best on [issue]," "most [value]").
- **Viability (optional):** whether electability is part of the rule. Some users want the best
  *electable* option (don't waste the vote); others vote conscience regardless of odds.

The rule is **bounded by the Tier-0 gates** — the *responsibility filter*. A candidate the
rule would otherwise select is still disqualified if they trip a gate. "Rather decline than
endorse someone who fails a hard line" is the spirit.

> One well-known rule that fits this slot is the "Buckley Rule" (back the rightward-most
> viable candidate, bounded by a responsibility filter). A progressive, a libertarian, or a
> single-issue voter would each fill it differently. Yours can be anything — the structure
> is what generalizes, not the rule.

---

## 3. Validation procedure (how a pick is made)

For each candidate:

1. **Gates first.** Run the Tier-0 gates. Any hit → disqualified; stop. Don't let strength on a
   top issue buy back a gated candidate.
2. **Viability.** Who can realistically win/advance?
3. **Score survivors** on Tiers 1–3 (load-bearing dominates).
4. **Apply the decision rule** to the acceptable, viable set.
5. **Decline-vs-cross** (below) if the preferred camp has no acceptable viable candidate.

For measures: score against the tiers; note strategic structure (competing measures, thresholds).

---

## 4. The decline-vs-cross hinge

When the candidate your rule prefers fails a Tier-0 gate, the next step turns on **one test:**

> *Does any **other** viable candidate clear both the Tier-0 gates **and** your value floor?*

- **No** → **decline/undervote.** Nobody is acceptable; declining is a legitimate, principled
  output — especially when the gated candidate will win/advance anyway, so your vote changes nothing.
- **Yes** → **cross** to that candidate, even from another party/camp. A tolerable alternative
  who clears your lines beats legitimizing one who doesn't.

An undervote is for when *no one* is acceptable — not a reflex whenever your side's candidate fails.

---

## 5. Due-diligence & sourcing standard (non-negotiable)

The framework is only as good as the facts fed into it.

1. **Deep background, not headlines.** Vet beyond the obvious vote/issue: the record on your
   gate issues, scandals/corruption, competence and fit for the *specific* office. A single
   famous position is a starting point, not a dossier.
2. **Cite every stated position.** Each factual claim carries a source link, so it's auditable.
   Prefer primary sources; flag claims resting only on partisan sources and seek corroboration.
3. **Follow facts even against the premise — including the user's.** Report findings honestly
   when they contradict an assumption. No agreeable shortcuts; no propagating unverified claims.
4. **Verify recency.** Use web search for current races; rely on the ballot for the candidate list.
5. **Surface forks; don't silently decide.** Genuine judgment calls go back to the user with
   the trade-off laid out.

---

## 6. Why this is pro-integrity, not persuasion

- It supplies **method, not values** — so it can't push a partisan line.
- It is **fact-grounded and cited** — countering disinformation rather than amplifying it.
- Its reasoning is **transparent and auditable** — the opposite of a manipulation black box.
- It **corrects the user** when facts demand it — sharpening judgment, not flattering it.

A tool that helps citizens make deliberate, fact-checked decisions from their own sincerely-held
values strengthens democratic deliberation. The moment it starts supplying the values or nudging
the outcome, it becomes persuasion — which is why the neutrality and anti-sycophancy guardrails
*are the product*, not decoration.

---

## 7. Grounding the charter in the user's own record

An interview captures what someone *says* they believe. Their actual writing — years of posts,
and what they *amplify* (likes, retweets, shares) — both validates the charter and catches what
the interview missed (an entire vocation, a recurring value, a sharper position). This is an
optional but powerful third step, between **build** and **analyze**.

**Method:**
1. **Process programmatically** — never load thousands of posts into context. Parse, theme-scan,
   count, and sample with a script (see `scripts/x-archive-scan.py`); read only the samples.
2. **Originals AND endorsements** — what someone likes/retweets is often the clearest signal.
3. **Derive theme buckets from the charter** (its tiers, gates, issues), plus discovery buckets.
4. **Classify each charter claim** against the record: CONFIRMS / SHARPENS / ADDS NEW /
   CONTRADICTS / NO SIGNAL — with dated quotes as citations.
5. **Reconcile** — add an evidence section and targeted edits; **surface contradictions to the
   user** instead of silently overwriting a stated value.

**Why it matters for integrity:** this is where the anti-sycophancy rule (§5.3) applies to the
*user themselves*. A charter that only flatters someone's self-image is weaker than one tested
against what they actually wrote. Grounding makes the document evidenced, not just asserted.

**Privacy is paramount.** Personal archives are sensitive. Keep them local, extract only text,
never upload, and keep both the archive and any personalized charter out of public repos.

## 8. Output artifacts

- **CHARTER.md** — the canonical values document. Source of truth. Carries a change log.
- **VOTING-GUIDE.md** — per-ballot application. Every pick traces to a charter tier and carries
  citations. Always reconcilable back to the charter.

The full workflow: **build → ground (optional) → analyze.**
