---
name: check-links
description: Scan the site's HTML for broken internal references — anchor links pointing at ids that don't exist, and script/stylesheet references pointing at files that aren't in the repo. Use when asked to check for broken links, dead anchors, or 404s on the site.
---

# Check Links

The site has no external link checker (external URLs are disallowed entirely, per `knowledge-base/Site-Guardrails.md`), but internal references can still rot: an anchor CTA on `index.html` pointing at a `tips.html#id` that got renamed or removed, or an `<article>` `id` that nothing links to anymore.

## Steps

1. Read `knowledge-base/Content-Architecture.md` to understand the linking model (homepage CTAs → `tips.html#<id>` anchors).
2. Extract every `id="..."` attribute from `index.html`, `about.html`, and `tips.html`.
3. Extract every internal `href="...#..."` and `href="tips.html#..."` / `href="#..."` reference across all three HTML files, and every local `href`/`src` pointing at a same-repo file (`style.css`, `theme-toggle.js`, `tips-filter.js`, `index.html`, `about.html`, `tips.html`).
4. Cross-check: every anchor reference must resolve to an `id` that exists in the target file; every local file reference must resolve to a file that exists in the repo root.
5. Separately, flag any `id` in `tips.html` that nothing on `index.html` links to — not broken, but worth surfacing since it may be a missed homepage callout opportunity per `Content-Architecture.md`.
6. Do not touch `mailto:` links or the two allow-listed external URLs (LinkedIn, YouTube) — those are out of scope.

## Output

A report: broken references found (file, line, what it points at, why it's broken), and orphaned `id`s with no inbound link. If nothing is broken, say so plainly rather than manufacturing findings. Fix obviously-broken references only with explicit confirmation — this skill is a checker first, not an auto-fixer.
