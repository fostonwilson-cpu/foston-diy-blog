---
status: active
project: foston-diy-blog
type: process
---

# Creating a New Article

When adding new content to the IT Help Desk knowledge base, always follow each of these steps, no matter what.

1. Read [[Voice-and-Style]], [[Audience]], and [[Content-Architecture]]. Do not skim. Do not skip. These notes give you the architecture and the voice you need to understand before writing anything.

2. Read [[Site-Guardrails]]. This, combined with the architecture note, is the fuel you need to write markup that survives CI. You will learn about the hard constraints, about the test suite, and how it checks your work.

3. Check the existing categories in `tips.html`. Decide: does this topic extend an existing `<article class="tips-card">`, or does it need a new one? [[Content-Architecture]] explains how to make that call — extending is the default; a new card is the exception.

4. Gather the required intel for the topic. This can happen in several different ways. If the user gives a source (a doc, a past incident, a specific tool), read it before drafting — do not invent specifics that weren't supplied. If the user only gives a topic name, ask what tool/OS/scope it should cover before writing steps that need to be concrete.

5. Ask what tag(s) apply — `quick`, `security`, `automation`, or some combination — using the taxonomy in [[Content-Architecture]]. These tags drive the on-page filter; getting them wrong makes the entry unfindable.

6. Write the `<h2>` title and framing `<p>` using the patterns in [[Headline-Swipe-File]]. This is the part that decides whether a scanning reader keeps reading — match a pattern exactly, don't freelance a new voice.

7. Draft the bullets: 3-5 per card, action-first, one idea each, per [[Voice-and-Style]]. Mark only the one or two bullets that most clearly earn a 🧩/🔐/⚙️ marker.

8. Insert the markup into `tips.html` in the right place (append to an existing `<ul data-tags="...">`, or add a new `<article>` before the closing `</section>` of `.tips-grid`). If it's a new card and it's flagship enough to deserve a homepage callout, add a matching CTA link on `index.html` pointing at `tips.html#<id>` — optional, use judgment.

9. Check the draft against every item in [[Site-Guardrails]], then run:

   ```bash
   python3 -m unittest tests/test_site_integrity.py
   ```

   Do not report the work done until this passes.

10. Summarize what was added — the category, the tags, and whether it was a new card or an extension — so it's easy to review the diff.
