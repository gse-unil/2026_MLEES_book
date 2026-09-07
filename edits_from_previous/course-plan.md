# Course plan: fitting the new book to the 2026 syllabus (superseded — see note)

**Superseded.** This file describes a 10-subchapter book (1.1–1.10, `01-`/`02-`… filenames, two
separate held-back subchapters — reproducible-data-pipelines and defensive-programming-and-
packaging) that was later consolidated into today's structure: 8 numbered subchapters (1.1–1.8,
`1.N-slug.ipynb` filenames) plus one bonus subchapter, Bonus A. Defensive programming merged onto
1.7; packaging then moved from there into Bonus A. See CLAUDE.md's "Current state" section for
the authoritative current picture, and `ch1-comparison-7.md`/`ch1-comparison-bonus-a.md`/
`ch1-comparison-bonus-b.md` for where each piece of content described here actually lives now.
Kept below as a historical record of the session that restored cartopy and k-means/PCA — that
work is real and still reflected in today's 1.4 and 1.8 (since further expanded — see
`ch1-comparison-4.md` and `ch1-comparison-8.md`) — not because its session-numbering is current.

Syllabus: *Introduction to Scientific Programming with Python* (2 ECTS), 4 weeks × 2 sessions = 8
sessions, written against the *old* 16-subchapter book. The new book has 10 subchapters (1.1–1.10);
per your call, 06 (reproducible data pipelines) and 08 (defensive programming and packaging) are
the two held back as extra/self-study material, leaving exactly 8 notebooks for 8 sessions.

**Status: the content gaps below have been implemented.** This file originally flagged them as
open questions; it now records what was done and why, plus the one item deliberately left for a
follow-up.

## Recommended session-by-session mapping

| Week | Session | Notebook | Old syllabus said | What changes |
|---|---|---|---|---|
| 1 | 1 | **1.1** Variables, data types, operators, file I/O | File I/O, retrieving/storing data, if/for/while loops, git | Control flow (if/for/while) moves to session 2 — old 1.1 bundled it with file I/O, new 1.1 doesn't. Git/GitHub is covered separately — see below. |
| 1 | 2 | **1.2** Data structures and control flow | Functions, classes/objects, dictionaries | Control flow joins this session instead of session 1. Classes move out entirely (to week 4) — dictionaries and functions stay. |
| 2 | 1 | **1.3** Numpy | Numpy (creation, indexing, broadcasting) & interpolation | Clean match — `np.interp` is core content in 1.3. |
| 2 | 2 | **1.4** Matplotlib and xarray | Matplotlib (line/contour) and cartopy (maps, projections); bonus: xarray | Xarray is promoted from "bonus" to half the session's core content. Cartopy is now a live, taught section again — see below. |
| 3 | 1 | **1.5** Pandas | Analyzing tabular data with pandas | Clean match, and stronger than old 1.9 (adds `groupby`, missing-data handling, `.rolling`); now also has a real-dataset capstone exercise (USGS earthquakes) — see below. |
| 3 | 2 | **1.9** Geospatial vector data | Analyzing geospatial data with geopandas | Clean match. Needs 1.4 already taught (uses matplotlib for its map-plotting section) — satisfied by this ordering. |
| 4 | 1 | **1.7** OOP for natural systems | *(old: classes, in week 1)* | Deliberately moved late. Two reasons: (1) the book's own going-deeper box in 1.7 and the opening paragraph of 1.10 explicitly cross-reference each other — 1.10 says outright "the estimator-as-object pattern is the one introduced in the object-oriented subchapter" — so the book was written assuming OOP comes right before the ML content; (2) 1.7's own content doesn't need numpy/pandas first (it's self-contained plain Python + dataclasses), so nothing is lost by moving it, and the payoff of landing right before 1.10 is real. |
| 4 | 2 | **1.10** Statistical foundations and ML | Regression/classification/clustering (sklearn) + seaborn | Needs 1.5 (pandas) and 1.7 (OOP, for the estimator-as-object callback) already taught — satisfied. k-means and PCA are now live, core content with a real dataset — see below. |

Everything in 1.1–1.5/1.9/1.7/1.10 is self-contained relative to this ordering — each notebook's
imports and core content were checked for hard dependencies on another subchapter's material
before proposing the swaps (1.7↔1.9 relative to file order).

## The three gaps: what was actually done

**1. Cartopy — restored to the live session.** 1.4 now has a full "Maps with cartopy" section
(two live, executed cells: a `PlateCarree` map with coastlines, then the same field re-drawn in an
`Orthographic` projection to demonstrate "changing projection" as the syllabus text promises), plus
a matching Exercise 8 in both the exercises and solutions notebooks. Learning objectives and
Takeaways were updated to mention it. The old going-deeper box was replaced with a slimmer one
covering more advanced features (`set_extent`, `add_feature`, `gridlines`) so there's still a path
deeper without repeating the now-live content.

**2. k-means and PCA — added to 1.10 as core content, not going-deeper, using real data.** A new
"Unsupervised learning: clustering and dimensionality reduction" section sits between "Scaling and
pipelines" and the AI-critique. It uses the real Palmer Archipelago penguins dataset (Horst, Hill &
Gorman, 2020, doi:10.5281/zenodo.3960218) — 344 real measurements of three penguin species,
committed to `data/part-I/palmer_penguins.csv` and fetched via the same `pooch` pattern already
used elsewhere in the book. `KMeans` on two features shows a real, imperfect clustering (Gentoo
separates cleanly, Adelie/Chinstrap overlap) — a genuinely honest result, not a cherry-picked clean
one. `PCA` on all four scaled features then separates all three species much better, which is
itself the pedagogical point: PCA uses what clustering on two hand-picked features couldn't. A
matching Exercise 8 (2-cluster k-means + PCA on the same data) was added to the exercises notebook,
with its worked solution in the separate `10-statistical-foundations-and-ml-solutions.ipynb`.
Learning objectives, Takeaways, and Resources were all updated (this update was lost at one point
during the session and had to be reapplied — see `final-audit.md`).

**3. Git/GitHub — already covered; nothing needed adding.** This is a correction to my earlier
review, not new work: I only looked inside `part-I/` when I first assessed this gap and missed
`appendix/00-setup-version-control-ai-literacy.ipynb`, which is already in the book's table of
contents and already covers exactly this — `git init`/`add`/`commit`/`branch`/`push`/`pull`, SSH
authentication to GitHub, cloning, plus going-deeper boxes on SSH keys, `.gitignore`, and
Ruff/pre-commit. It's thorough and well-written; the only issue was a leftover `% #TODO` comment in
`appendix/appendix.md`, now removed. Point students at this appendix for week 1 session 1 instead
of writing new material — there was no gap to fill here, only a filing mistake on my part.

## Real datasets: reintroduced where it fit, flagged where it didn't

Per your instruction to reintroduce the old book's real datasets wherever possible:

- **Done — 1.10 (k-means/PCA):** real Palmer Penguins data, as above. This was also the old book's own dataset for its k-means content, so it's a direct restoration, not just "a" real dataset.
- **Done — 1.5 (pandas), new Exercise 8:** a real, fixed snapshot of the USGS earthquake catalog (629 events, magnitude ≥ 4.5, January 2023 — `data/part-I/usgs_earthquakes_2023_01.csv`, fetched the same pinned-hash way), echoing the old book's earthquake exercise. Structured as the "one long exercise on a real dataset, hints as comments, no solution" pattern already used by 1.1's and 1.3's capstone exercises — 1.5 didn't have one of these before, so this also fills a structural gap, not just a content one.
- **Done — 1.9 (geospatial), new Exercise 8:** the old book's Hurricane Florence track exercise, restored with real data you supplied — `data/part-I/florence.csv` (the NHC advisory track, 105 records) and `data/part-I/gz_2010_us_040_00_5m.json` (US Census Bureau state boundaries), fetched the same pinned-hash way. Ported the old exercise's shape (read both files, build a GeoDataFrame from the track, exclude Alaska/Hawaii, plot states with the track layered on top, identify affected states) but reworked the last step to use this subchapter's own tools: reproject to a metric crs, buffer the track by 50 km, and find states intersecting that buffer — a genuine extension of the old "spatial overlay/intersection" step rather than a copy. One real data quirk worth knowing: the track's `Long` column stores a positive "degrees west" magnitude, not a signed longitude, so it needs negating before it'll plot correctly — the exercise calls this out explicitly rather than silently fixing it.
- **Not attempted — 1.10's regression content (old book's advertising dataset) and the old book's marathon-data seaborn exercise:** both are reasonable candidates for the same kind of treatment, not done in this pass, flagging for the same reason as above.

## Exercises and solutions: now consistent across all 10 subchapters

Two follow-on passes, independent of the content work above, brought every subchapter to the same
standard:

- **Every subchapter now has a working, in-sync solutions notebook.** 03 and 04 were rebuilt at the
  very start of this whole effort; 05–10 had their inline dropdown solutions split out into
  separate `*-solutions.ipynb` files; 01 and 02 turned out to need the same treatment as 03 once
  audited — worse, in fact, since their *exercises* notebooks had leaked answer cells sitting in
  the open (three exercises in 01 had no blank attempt cell at all, just the answer). All of that
  is now fixed — see `final-audit.md` for the specifics. Every exercises notebook in the book is
  now blank-cells-only, with a separate, verified solutions notebook alongside it.
- **Exercise headings are now uniform book-wide**: `## Exercise N: Title`, colon style, everywhere
  (01–04 already used this; 05–10 used an em-dash for short exercises and reserved the colon for
  capstones — standardized to colon-everywhere on your call).

## A structural bug the content work surfaced

A later full-book audit (`final-audit.md`) found that 1.9 alone had three real content sections
(spatial joins, buffer/dissolve/overlay, plotting a map) sequenced *after* its own AI-critique,
unlike every other subchapter, which finishes its content, then critiques, then wraps up. Reordered
so 1.9 now matches the rest of the book. Also caught and fixed a real regression: 1.10's k-means/PCA
section had lost the Learning-Objectives/Takeaways/Resources/intro updates that were meant to
introduce it — the content was there, but nothing pointed to it. Both are fixed; full detail in
`final-audit.md`.

## Mechanical fixes — all applied

Everything catalogued in `quality-review.md` has been fixed:
- Every H1 title in 05–10 (lecture and exercises) now matches its actual file position; 1.6's lecture title no longer says "GeoPandas and Cartopy."
- 1.9's stray leftover code cell (`a = 1`) is deleted.
- 1.9's broken GeoDataFrame-construction output (kernel traceback + `ModuleNotFoundError`) is replaced with the real, verified output.
- 1.10's overfitting demo now uses degree 8 instead of degree 10 (train R² 0.971, test R² −7.1) — still a dramatic, unambiguous overfitting story, but far less numerically explosive across scikit-learn versions than degree 10 was.
- `myst.yml`'s table of contents now includes 08 and 09, which were previously commented out and unreachable from the published book at all, regardless of the live-teaching question.

## Is the new content better than the old book?

Yes, on balance, and not narrowly.

**What's clearly better:**
- The AI-critique device (a plausible, silently-wrong generated-code example, diagnosed and fixed) appears in every single subchapter and has no equivalent anywhere in the old book — including in the appendix's own AI-literacy example (an unstated-unit bug), which ties the same device back to prompting practice.
- Computational-thinking boxes (one per subchapter) give students a portable principle, not just a syntax tour.
- 1.10's train/test-split, RMSE/R², and overfitting content is a real, substantive addition the old sklearn tutorial didn't have.
- 1.9's whole subchapter is built around the CRS/degrees-vs-metres mistake, which the old geopandas tutorial doesn't appear to address at all.
- 1.6 and 1.8 (data pipelines, defensive programming/testing/packaging) are genuinely new, valuable material with no old-book equivalent — the right two to hold back as extras precisely because they're additions, not replacements.
- With cartopy and k-means/PCA now restored as live content, 1.4 and 1.10 no longer trade away syllabus-promised topics for the new material — they cover both.

**Remaining neutral trade-off, not a regression:** seaborn's chart-type breadth is still narrower in 1.10 than the old dedicated seaborn subchapter (a handful of plot types in service of the modelling narrative, vs. a full tour of chart types). This is a defensible framing choice, not something I'd change without you asking for it specifically.

## Where things stand now

The old-syllabus wording that named cartopy, k-means/PCA, and git as required topics can stay as
written — all three are genuinely taught. 1.9's real-dataset gap is closed (the Hurricane Florence
exercise, above). The only two items still open from the original real-datasets request are 1.10's
regression content (the old book's advertising dataset) and the old marathon-data seaborn exercise
— both noted above as not attempted, and both reasonable candidates for a follow-up pass whenever
you want them.
