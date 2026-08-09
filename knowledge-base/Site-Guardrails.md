# Site Guardrails

Hard constraints enforced by `tests/test_site_integrity.py`. Every one of these fails CI if broken — check the draft against this list before finishing, every time.

- **No external URLs** in any `.html` or `style.css` file, except the two already allow-listed (LinkedIn, YouTube company links). Don't link out to sources, tools, or vendors by URL — describe them by name in text instead.
- **No inline event handlers** — `onclick=`, `onload=`, `onerror=`, `onfocus=`, `onblur=`, `onmouseover=`, `onmouseenter=`, `onmouseleave=`, `onsubmit=`, `onreset=`. All interactivity goes through the existing `theme-toggle.js` / `tips-filter.js`, not new inline JS.
- **No `innerHTML`, `outerHTML`, or `insertAdjacentHTML`** in any `.js` file.
- **Every HTML page keeps its full security meta-tag block** (CSP, Referrer-Policy, X-Content-Type-Options, Permissions-Policy, and the three cross-origin headers) verbatim. Never trim or "clean up" these tags.
- **No negative spacing values** in `style.css` (`margin: -`, `padding: -`, `top: -`, `bottom: -`, `left: -`, `right: -`).
- **Every HTML file starts with `<!DOCTYPE html>`** and contains a `<main>` landmark.
- **HTML must parse cleanly** — close every tag, quote every attribute.

After drafting, run the test suite to confirm before calling the work done:

```bash
python3 -m unittest tests/test_site_integrity.py
```
