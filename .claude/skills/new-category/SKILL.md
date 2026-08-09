---
name: new-category
description: Add a brand-new knowledge-base category card to tips.html, for a topic that doesn't fit any existing card. Use when the user explicitly wants a new category/section, not just a new bullet in an existing one.
---

# New Category

Adds a whole new `<article class="tips-card">` to `tips.html`, following the "Add a new card" path in `knowledge-base/Content-Architecture.md`. This is the exception path — `write-tip` should be preferred whenever a topic fits an existing card. Only use this skill when the topic genuinely doesn't belong under any current `<h2>`.

## Steps

1. Read `knowledge-base/Creating-a-New-Article.md`, `Voice-and-Style.md`, `Audience.md`, `Content-Architecture.md`, `Headline-Swipe-File.md`, and `Site-Guardrails.md`.
2. Confirm the new-card decision: list every existing `<h2>` in `tips.html` and explain why the topic fits none of them. If it's a closer fit for an existing card than it first appears, stop and recommend `write-tip` instead.
3. Pick a short kebab-case `id`, unique against every existing `id` in `tips.html`.
4. Write the `<h2>` and framing `<p>` using the patterns in `Headline-Swipe-File.md`.
5. Draft 3-5 bullets per `Voice-and-Style.md` and the bullet-phrasing patterns, with tags drawn from `quick`/`security`/`automation` per `Content-Architecture.md`.
6. Insert the new `<article>` at the end of `<section class="tips-grid">`, before the closing `</section>`.
7. Decide whether the new category is flagship enough for a homepage callout on `index.html` (a CTA button linking to `tips.html#<id>`, matching the existing callout pattern) — use judgment, this is optional.
8. Check against `Site-Guardrails.md`, then run `python3 -m unittest tests/test_site_integrity.py`. Do not report done until it passes.

## Output

- The new `<article>` card in `tips.html`, and the homepage CTA in `index.html` if added.
- Test suite run and passing.
- A summary: the new category's id/title, its tags, why it needed a new card rather than extending one, and whether a homepage CTA was added.
