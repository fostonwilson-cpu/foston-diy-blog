# Content Architecture

How the site is structured. Read this before touching any HTML.

## Pages

- `index.html` — landing page. Hero, a featured guide, and CTA links that deep-link into `tips.html#<id>` anchors for the flagship categories.
- `about.html` — company/stack page. Not a target for new knowledge-base content.
- `tips.html` — the knowledge base itself. This is where new content goes.

## Anatomy of a knowledge-base category

Each category on `tips.html` is one `<article class="tips-card">` block:

```html
<article id="category-slug" class="tips-card">
  <h2>Category Title</h2>
  <p>One-sentence framing of what this category covers.</p>
  <ul data-tags="quick security automation">
    <li>Bullet one 🧩</li>
    <li>Bullet two</li>
    <li>Bullet three 🔐</li>
    <li>Bullet four</li>
  </ul>
</article>
```

- `id` is a short kebab-case slug, unique across the page — it's the anchor other pages link to.
- `data-tags` on the `<ul>` is a space-separated list drawn only from `quick`, `security`, `automation` (see `tips-filter.js`). It applies to the whole card, not per-bullet — pick every tag that meaningfully applies.
- 3–5 `<li>` bullets per card is the established range. Going shorter reads thin; going longer breaks the scan-in-10-seconds goal from [[Audience]].
- Emoji markers on bullets are cosmetic (they don't drive filtering — the `data-tags` attribute does) but they must still follow [[Voice-and-Style]] usage rules.

## Two ways to add content

1. **Extend an existing card** — add 1-2 bullets to a category that already covers the topic. Preferred when the topic is a natural fit for an existing category; keeps the page from sprawling.
2. **Add a new card** — only when the topic doesn't fit any existing category `<h2>`. New cards go at the end of the `<section class="tips-grid">`, before the closing `</section>`.

## Hard constraints (non-negotiable, enforced by tests)

See [[Site-Guardrails]] before writing or editing any markup — these are checked by `tests/test_site_integrity.py` and a change that violates them will fail CI.
