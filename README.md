# Foston IT Help Desk

A refreshed static site for Foston's IT support hub. The redesign introduces:

- A hero header with clear navigation, skip links, and dark-mode toggle persistence
- A featured secure-remote-work rollout guide, incident planning framework, and resource library downloads
- A knowledge base with deep-linked categories covering support, security, automation, and compliance
- An updated about page highlighting Foston's preferred tech stack and collaboration options
- Training events, community success stories, and a status brief subscription to keep stakeholders informed
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

## Content agent workflow

New knowledge-base entries follow a repeatable process instead of being drafted freehand:

- `knowledge-base/` holds a small set of process notes (voice, audience, site architecture, headline patterns, and
  hard guardrails) plus a master checklist, `Creating-a-New-Article.md`, that ties them together.
- The `write-tip` Claude Code skill (`.claude/skills/write-tip/`) runs that checklist end to end — read the notes,
  draft the entry, insert it into `tips.html`, and verify it against the test suite — from a single topic prompt.
- `CLAUDE.md` documents this as the standing process for any future contribution to the knowledge base.

## Security hardening

- Every page sends a hardened Content Security Policy that blocks third-party scripts, confines images and
  media to first-party assets, prevents worker/frame injection, and upgrades any attempted insecure requests.
- Additional headers (Referrer-Policy, X-Content-Type-Options, Permissions-Policy, and cross-origin isolation
  directives) reduce passive metadata leaks, enforce MIME correctness, and isolate the browsing context.
- Automated tests enforce the headers, ensure no inline event handlers or risky DOM injection APIs creep in,
  and now fail the build if any external URLs sneak into the HTML or CSS or if spacing rules turn negative.
