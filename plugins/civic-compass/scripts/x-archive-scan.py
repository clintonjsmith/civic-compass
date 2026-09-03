#!/usr/bin/env python3
"""
x-archive-scan.py — thematic scanner for an X/Twitter data archive (Civic Compass).

Parses an unzipped X export and prints, per theme: counts across your original posts,
retweets, and likes, plus dated sample quotes. Used by the `ground-charter` skill to
reconcile a CHARTER.md against the user's own posting record WITHOUT loading thousands of
posts into the model's context.

Privacy: runs entirely locally, reads only local text files, sends nothing anywhere.

USAGE
    # 1. Unzip your X archive (Settings > Your account > Download an archive of your data),
    #    extracting at least the text data files (media is not needed):
    unzip -o your-twitter-archive.zip 'data/tweets.js' 'data/like.js' 'data/account.js' -d x-archive

    # 2. Edit the THEMES dict below to match the CHARTER's tiers/gates/issues, then run:
    python3 x-archive-scan.py ./x-archive

    # Optional: --samples N (default 10), --theme NAME to focus one bucket.

Adapt the loaders for other platforms (Reddit/Bluesky/Mastodon/Facebook exports, or a blog)
— the theme-scan logic is platform-agnostic; only the parse step changes.
"""

import argparse, json, os, re, sys
from datetime import datetime

# ---------------------------------------------------------------------------
# EDIT THESE to match the charter you're grounding. Keys are theme labels;
# values are case-insensitive regex patterns. Include "discovery" buckets
# (e.g., a vocation, a hobby, a cause) to catch themes the interview missed.
# ---------------------------------------------------------------------------
THEMES = {
    "economy/markets":   r"(\bmarket|capitalis|deregulat|subsid|\btax|deficit|fiscal|inflation|price)",
    "democracy/rule-of-law": r"(democracy|authoritarian|insurrection|election integrity|stolen elect|voter fraud|constitution|rule of law)",
    "civil-liberties":   r"(free speech|first amendment|privacy|surveillance|due process|censor)",
    "immigration":       r"(immigrat|\bvisa|green card|\bborder\b|migrant)",
    "health/science":    r"(vaccin|\bvax|\bfda\b|\bscience|climate|measles)",
    "foreign/defense":   r"(ukrain|russia|\bchina\b|tariff|\bnato\b|israel|\biran\b|defense|war)",
    "social-issues":     r"(abortion|pro-life|second amendment|\b2a\b|\bguns?\b|religio)",
    "labor/unions":      r"(\bunion|right to work|\blabor\b|strike)",
    "energy/tech":       r"(\bai\b|automat|robot|manufactur|nuclear|\benergy|abundance)",
    "local/governance":  r"(housing|zoning|crime|homeless|school|\bdei\b|budget|pension)",
}


def load_js_array(path, prefix_re):
    """Load one of X's `window.YTD.<x>.part0 = [ ... ]` JS files as JSON."""
    if not os.path.exists(path):
        return []
    raw = open(path, encoding="utf-8").read()
    raw = re.sub(prefix_re, "", raw, count=1)
    return json.loads(raw)


def parse_archive(root):
    """Return (originals, retweets, likes) as lists of dicts: {text, date}."""
    def tdate(s):
        try:
            return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
        except Exception:
            return None

    tweets = load_js_array(os.path.join(root, "data", "tweets.js"),
                           r"^window\.YTD\.tweets\.part0 = ")
    posts = [{"text": t["tweet"]["full_text"], "date": tdate(t["tweet"]["created_at"])}
             for t in tweets]
    originals = [p for p in posts if not p["text"].startswith("RT @")]
    retweets  = [p for p in posts if p["text"].startswith("RT @")]

    likes_raw = load_js_array(os.path.join(root, "data", "like.js"),
                              r"^window\.YTD\.like\.part0 = ")
    likes = [{"text": l["like"].get("fullText", ""), "date": None} for l in likes_raw]
    return originals, retweets, likes


def scan(items, pattern):
    c = re.compile(pattern, re.I)
    return [x for x in items if c.search(x["text"])]


def fmt(x):
    d = x["date"].date() if x["date"] else "????-??-??"
    return f"[{d}] {' '.join(x['text'].split())[:240]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", help="path to the unzipped X archive dir (contains data/)")
    ap.add_argument("--samples", type=int, default=10)
    ap.add_argument("--theme", help="only scan this theme key")
    args = ap.parse_args()

    originals, retweets, likes = parse_archive(args.archive)
    dated = [p for p in originals if p["date"]]
    rng = (f"{min(p['date'] for p in dated).date()} -> {max(p['date'] for p in dated).date()}"
           if dated else "n/a")
    print(f"Corpus: {len(originals)} originals | {len(retweets)} retweets | {len(likes)} likes")
    print(f"Date range (originals): {rng}\n")

    themes = {args.theme: THEMES[args.theme]} if args.theme else THEMES
    for name, pat in themes.items():
        mo, mr, ml = scan(originals, pat), scan(retweets, pat), scan(likes, pat)
        print(f"===== {name}  (orig {len(mo)} | RT {len(mr)} | likes {len(ml)}) =====")
        sample = sorted([p for p in mo if p["date"]], key=lambda p: p["date"])
        step = max(1, len(sample) // args.samples) if sample else 1
        for p in sample[::step][:args.samples]:
            print("  " + fmt(p))
        print()


if __name__ == "__main__":
    main()
