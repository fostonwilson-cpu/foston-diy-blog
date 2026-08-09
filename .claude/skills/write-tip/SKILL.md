---
name: write-tip
description: Autonomously draft and add a new IT Help Desk knowledge-base entry to tips.html. Use when the user asks to add a tip, guide, runbook, or knowledge-base article to this site, or invokes /write-tip.
---

# Write Tip

Adds a new entry to the Foston IT Help Desk knowledge base (`tips.html`) by following the repo's knowledge base of process notes end to end, the same way every time.

## Steps

Follow `knowledge-base/Creating-a-New-Article.md` exactly, in order. That note is the source of truth for this process — read it first, then read every note it points to (`Voice-and-Style.md`, `Audience.md`, `Content-Architecture.md`, `Headline-Swipe-File.md`, `Site-Guardrails.md`) before drafting anything.

Do not shortcut by writing markup from memory of "what IT tip sites usually look like" — the voice, structure, and constraints are specific to this repo and are only correct if pulled from those notes.

## Input

The user will give a topic (e.g. "add a tip about rotating shared Wi-Fi passwords") and optionally a source of intel (a doc, a past incident writeup, specific tool names). If no scope/tool specifics are given and the topic needs them to be concrete, ask before drafting rather than inventing specifics.

## Output

- The new bullet(s) or `<article>` inserted into `tips.html`, following the architecture and guardrails notes exactly.
- `python3 -m unittest tests/test_site_integrity.py` run and passing before the task is reported done.
- A short summary of what was added (category, tags, new card vs. extension).
