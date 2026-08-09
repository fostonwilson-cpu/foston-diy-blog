---
name: check-deploy-bundle
description: Verify the GitHub Pages deploy workflow bundles every file the site actually needs, and nothing it doesn't. Use when asked to check the deploy workflow, verify the site bundle, or after adding/removing a script or stylesheet reference in the HTML.
---

# Check Deploy Bundle

`.github/workflows/deploy.yml`'s "Prepare site bundle" step hand-copies a fixed file list into `dist/`. That list has drifted from the actual HTML before — `tips-filter.js` was referenced by `tips.html` but missing from the bundle, so the deployed knowledge-base filter silently 404'd (fixed, but nothing stops it from happening again on the next new script or stylesheet).

## Steps

1. Read `.github/workflows/deploy.yml` and extract the exact file list from the "Prepare site bundle" `cp` command.
2. Extract every local (non-external) `<script src="...">` and `<link rel="stylesheet" href="...">` reference across `index.html`, `about.html`, and `tips.html`, plus the three HTML files themselves.
3. Diff the two sets:
   - Anything referenced by the HTML but missing from the bundle list is a real bug — the deployed site will 404 on it.
   - Anything in the bundle list but not referenced by any HTML file is dead weight — not breaking, but worth flagging.
4. Simulate the bundle step locally (`mkdir -p /tmp/dist-check && cp <the same file list> /tmp/dist-check/`) and confirm it succeeds with no missing-file errors.
5. Run `python3 -m unittest tests/test_site_integrity.py` as a baseline sanity check (it won't catch bundle drift directly, but should still pass).

## Output

A pass/fail report: whether the bundle list and the HTML's actual asset references match exactly, with specifics on any mismatch (file, which side it's missing from). If a real gap is found, propose the exact `cp` line fix rather than applying it unprompted — this is a checker, and workflow-file edits should be confirmed given they affect the live deploy pipeline.
