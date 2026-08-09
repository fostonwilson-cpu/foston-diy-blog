---
name: check-voice
description: Audit existing tips.html content for drift from knowledge-base/Voice-and-Style.md and Headline-Swipe-File.md — bullet counts, marker density, banned phrases, headline patterns. Use when asked to review content consistency, voice, or tone across the knowledge base.
---

# Check Voice

`write-tip` and `new-category` write new content to spec, but nothing re-checks content already on the page — including entries added before those skills existed, or drifted over multiple edits. This skill audits what's already live.

## Steps

1. Read `knowledge-base/Voice-and-Style.md` and `knowledge-base/Headline-Swipe-File.md` in full.
2. For every `<article class="tips-card">` in `tips.html`, check:
   - Bullet count is 3-5 (per `Content-Architecture.md`'s established range).
   - Marker density: roughly two or three of the bullets carry a 🧩/🔐/⚙️ marker, not zero and not all of them.
   - The `<h2>` matches one of the two title patterns in `Headline-Swipe-File.md` (Domain & Function, or Domain "&" Domain) — not a question, gerund, or anything over three words.
   - The framing `<p>` is one sentence, verb-first, naming a payoff rather than describing the activity.
   - Bullets lead with a deliverable noun phrase (checklist, playbook, matrix, template, guide, kit), not a bare problem description.
   - No banned phrasing from the "Things we never say" list (absolute compliance claims, unsourced product endorsements, first-person urgency).
3. Note anything that's a judgment call rather than a clear violation — this skill should flag drift, not silently rewrite copy that's merely a different reasonable interpretation of the notes.

## Output

A per-card report: card id, any findings, and whether it's clean. If everything reads clean, say so. Do not edit `tips.html` as part of this skill — it's a checker; propose specific fixes in the report and let the user decide whether to apply them (or hand off to `write-tip`-style editing separately).
