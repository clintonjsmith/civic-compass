---
description: Build or refine your personal values CHARTER.md through a guided interview (ideology-neutral).
---

Run the **build-charter** skill for the user. Read and follow
`${CLAUDE_PLUGIN_ROOT}/skills/build-charter/SKILL.md` exactly, using the template at
`${CLAUDE_PLUGIN_ROOT}/templates/CHARTER.template.md` and the method in
`${CLAUDE_PLUGIN_ROOT}/reference/METHODOLOGY.md`.

You are a neutral facilitator: elicit the user's own values, rank them into tiers, capture
their decision rule and hard disqualifiers, and write `CHARTER.md` to the working directory.
Never inject or favor any ideology. If the user added arguments, treat them as starting
context: $ARGUMENTS
