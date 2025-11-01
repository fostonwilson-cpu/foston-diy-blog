# Foston DIY Blog

A refreshed static site for Foston's do-it-yourself home repair hub. The redesign introduces:

- A hero header with clear navigation, skip links, and dark-mode toggle persistence
- Rich featured project details, planning resources, kickoff essentials, and a newsletter call-to-action
- A fully styled tips archive with deep-linked categories, quick-share legends, and live filtering by tag or keyword
- A new about page highlighting Foston's story, favorite tools, and collaboration options
- Additional planner, resource shelf, events calendar, and community spotlight sections on the homepage
- Strict security headers, sanitized filtering logic, and guardrail tests that keep the static pages resilient

## Local preview

To preview locally, open `index.html` in your browser or run a lightweight server:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Public deployment

Pushes to the `main` branch automatically publish the static assets to GitHub Pages.
The workflow bundles the HTML, CSS, and JavaScript into an artifact before deploying,
so the public site only exposes the necessary files. You can also trigger the
deployment manually from the GitHub Actions tab via the **Deploy static site** workflow.

## Security hardening

- Every page sends a hardened Content Security Policy that blocks third-party scripts, confines images and
  media to first-party assets, prevents worker/frame injection, and upgrades any attempted insecure requests.
- Additional headers (Referrer-Policy, X-Content-Type-Options, Permissions-Policy, and cross-origin isolation
  directives) reduce passive metadata leaks, enforce MIME correctness, and isolate the browsing context.
- Automated tests enforce the headers, ensure no inline event handlers or risky DOM injection APIs creep in,
  and now fail the build if any external URLs sneak into the HTML or CSS or if spacing rules turn negative.
