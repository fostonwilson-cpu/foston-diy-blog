---
name: audit-guardrails
description: Read-only compliance sweep of the site against knowledge-base/Site-Guardrails.md and the guardrail test suite. Use when asked to audit, check, or verify the site is still compliant with its security/CSP constraints, or before a release.
---

# Audit Guardrails

Checks the live markup, styles, and scripts against every rule in `knowledge-base/Site-Guardrails.md`, independent of the test suite (which only catches what it's coded to catch — this skill reads the actual notes and looks with fresh eyes).

## Steps

1. Read `knowledge-base/Site-Guardrails.md` in full.
2. For each rule, grep the relevant files (`index.html`, `about.html`, `tips.html`, `style.css`, `theme-toggle.js`, `tips-filter.js`) and confirm compliance directly — don't just trust the test suite ran clean, since the guardrails note is the source of truth and the tests are one specific encoding of it.
3. Run `python3 -m unittest tests/test_site_integrity.py` and record the result.
4. Check for drift the automated tests don't cover: e.g. a security meta tag present but reordered/reworded in a way that still "looks right" but wouldn't match the test's exact-string check; a guardrail note updated but the test suite not updated to match, or vice versa.

## Output

A short pass/fail report, one line per guardrail rule, plus the test suite result. If something fails, describe exactly what and where (file + line) — do not silently fix it; report first, since a guardrail violation found outside the test suite might mean the test suite itself needs updating rather than the markup.
