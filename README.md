# Foston DIY Blog

A refreshed static site for Foston's do-it-yourself home repair hub. The redesign introduces:

- A hero header with clear navigation, skip links, and dark-mode toggle persistence
- Rich featured project details, planning resources, kickoff essentials, and a newsletter call-to-action
- A fully styled tips archive with deep-linked categories, quick-share legends, and live filtering by tag or keyword
- A new about page highlighting Foston's story, favorite tools, and collaboration options
- Additional planner, resource shelf, events calendar, and community spotlight sections on the homepage

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
