# Security Policy

## Reporting a vulnerability

**Please do not open a public issue for a security problem.**

Report it privately through GitHub: go to the repository's **Security** tab and click
**Report a vulnerability**, or use
[this link](https://github.com/clintonjsmith/civic-compass/security/advisories/new).
That opens a private advisory thread visible only to you and the maintainer — nothing is
disclosed publicly unless and until an advisory is published.

This project is maintained by one person in their spare time. Expect a first response
within about a week. There is no bug bounty.

**Supported version:** the latest commit on `main`. Older tags do not receive fixes.

---

## What this plugin is

Civic Compass is a Claude Code plugin: a set of Markdown skill and command definitions,
document templates, and one local Python script (`x-archive-scan.py`). There is no server,
no hosted service, no account, and no telemetry. Nothing is transmitted anywhere except the
web searches the agent performs while researching candidates.

It runs inside Claude Code, with your permissions, on your machine, against your files.

## Trust model

The plugin deliberately ingests content it cannot vouch for:

- **Ballots** — a PDF, photo, URL, or pasted text supplied to `/analyze-ballot`
- **Social/writing exports** — an archive supplied to `/ground-charter`
- **Search results** — pages fetched while researching candidates and measures

All three are attacker-influenceable text that flows into a language model which is, at that
moment, reading and writing files on your computer. Treat that as the primary risk surface.

A consequence worth stating plainly: **prompt injection is a real and unsolved risk class for
tools of this kind.** A crafted document could attempt to steer the agent's reasoning, and for
a tool that produces voting recommendations, a successful attempt is a meaningful harm. The
structural mitigations are that every recommendation must cite sources you can check, and that
the output is explicitly a draft to verify rather than an instruction to follow. Neither is a
guarantee. Verify the picks that matter to you.

## In scope

Reports along these lines are wanted:

- A crafted ballot document, archive, or web page that reliably alters recommendations,
  suppresses a disqualifying fact, or manipulates the reasoning in a way a reader would not
  detect from the cited sources
- Any path by which the plugin transmits your charter, ballot analysis, or archive off your
  machine
- `x-archive-scan.py` mishandling a malicious archive — path traversal, writes outside the
  target directory, or code execution
- Skill or command instructions that could cause the agent to read unrelated sensitive files,
  or to write outside the working directory
- Anything that would cause a user's charter, archive, or personal data to be committed or
  published against their intent

## Out of scope

- **Disagreeing with a recommendation.** That is not a vulnerability. Ideological neutrality
  *is* a design goal, though — if the scaffolding itself biases toward a party or worldview,
  please open a normal public issue. That belongs in the open.
- **The model being wrong or out of date.** Documented in the README; verify against your
  election authority.
- **Vulnerabilities in Claude Code, Anthropic's models, or your operating system.** Report
  those to the relevant vendor.
- Social engineering, physical access, or an already-compromised machine.

## The most likely harm is self-inflicted

Realistically, the greatest risk to a user of this tool is not an attacker — it is
accidentally publishing their own data. A charter is a written record of political values;
a social export contains direct messages, a phone number, IP and geolocation history, and
private chat transcripts.

This repository ships a `.gitignore` that blocks all of it by default. Leave those rules in
place, keep your archive outside any repository, and read the
[Privacy section](README.md#privacy--read-before-you-run-ground-charter) before running
`/ground-charter`.
