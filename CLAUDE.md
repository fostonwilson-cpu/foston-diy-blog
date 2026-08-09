# Foston IT Help Desk — agent notes

This repo is a static site (`index.html`, `about.html`, `tips.html`) with a hardened CSP and a guardrail test suite in `tests/test_site_integrity.py`. Read that file before editing any HTML, JS, or CSS — its assertions are non-negotiable.

## Adding knowledge-base content

New content for `tips.html` is not freehand — it follows a fixed process backed by a small knowledge base of notes in `knowledge-base/`, modeled on an Obsidian-style vault: a master checklist note that points to supporting notes on voice, audience, architecture, and hard constraints.

- Start at `knowledge-base/Creating-a-New-Article.md` — it's the checklist, and it links to everything else you need in the order you need it.
- The `write-tip` skill (`.claude/skills/write-tip/SKILL.md`) operationalizes that checklist end to end: give it a topic and it reads the notes, drafts the entry, inserts it into `tips.html`, and runs the test suite before reporting done.

Use this process for any new tip/guide/runbook addition, even if not invoked via the skill explicitly — it's the standing process for this repo, not an optional shortcut.
