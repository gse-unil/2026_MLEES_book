# Quality review: 1.5–1.10 (superseded — see note)

**Superseded.** Written against the same 10-subchapter, `05`–`10` numbered structure as
`course-plan.md` and `final-audit.md` (see those files' notes) — today's book has 8 numbered
subchapters + Bonus A; what this file calls "06 reproducible data pipelines" and "08 defensive
programming and packaging" are today's Bonus A and part of 1.7 respectively, and "09"/"10" are
today's 1.6/1.8. See CLAUDE.md's "Current state" for the authoritative picture. Kept as a
historical record of the bugs it found (the title-numbering mess, the stray `a = 1` cell, the
degree-10 overfitting instability, the missing k-means/PCA content) — those fixes are real and
still in effect. A separate, independent pre-launch review (see the `ch1-comparison-N.md` files
and `todo-list.md`) has since re-audited all of today's 1.1–1.8 plus Bonus A and found its own,
different set of issues — the two audits don't overlap in what they checked.

Full-depth review (structure, palette, sequencing, style, stale outputs, resources) of the six
lecture notebooks and their paired exercises not yet covered in earlier passes: pandas (05),
reproducible data pipelines (06), OOP for natural systems (07), defensive programming and
packaging (08), geospatial vector data (09), statistical foundations and ML (10).

**Status: all blockers and majors below are now fixed** (mechanical fixes applied, plus cartopy and
k-means/PCA added to close the two content-scope majors — see `course-plan.md` for the content
changes). This file is kept as the original findings record, with an outcome noted on each row. A
later full-book audit found one more structural issue in this 05–10 range (added below) plus
several issues in 01–04 that were out of this file's original scope — see `final-audit.md` for
those.

## Findings

| Severity | Location | Issue | Outcome |
|---|---|---|---|
| Blocker | Book-wide: title numbers | Every H1 title across 05–10 (lecture *and* exercises) carried a stale or outright wrong subchapter number, in at least three different numbering schemes bleeding into each other. See the table below for the full picture. | **Fixed.** Every lecture H1 now matches its file position (05→1.5 … 10→1.10); every exercises notebook now uses the bare "# Exercises" title, matching 01–04's convention. |
| Blocker | `06-reproducible-data-pipelines.ipynb`, cell 0 | The H1 read "# 1.6) GeoPandas and Cartopy" — wrong topic entirely — with an orphan paragraph "Reproducible data pipelines" sitting under it. | **Fixed.** H1 now reads "# 1.6) Reproducible Data Pipelines"; the orphan line is gone. |
| Blocker | `09-geospatial-vector-data.ipynb`, cell 1 | A stray leftover code cell, just `a  = 1`, sat between the H1/intro and the Learning objectives box. | **Fixed.** Cell deleted. |
| Blocker | `09-geospatial-vector-data.ipynb` (was cell 4, now cell 3 after the stray-cell deletion) | Committed output was broken: a raw Jupyter-kernel-internal traceback followed by `ModuleNotFoundError: No module named 'geopandas'`. | **Fixed.** Regenerated in a scratch geopandas install and re-verified against every downstream cell; real output now committed. |
| Blocker | `09-geospatial-vector-data.ipynb`, structure | Unlike every other subchapter in 05–10 (and the book generally), 1.9 had three real content sections — spatial predicates/joins, buffer/dissolve/overlay, plotting a map — sequenced *after* its own AI-critique instead of before it, with the critique stranded mid-notebook. Found in a later full-book audit, not the original pass through 05–10. | **Fixed.** Reordered so the critique now immediately precedes the going-deeper boxes and Takeaways, matching every sibling subchapter. Checked variable dependencies (`in_hazard`, `zones`, `stations_lv95`) before moving anything — see `final-audit.md`. |
| Major | `10-statistical-foundations-and-ml.ipynb` (the overfitting demo) | Degree-10 polynomial fit on ~12 points is numerically ill-conditioned; I got visibly different numbers on a fresh scikit-learn (train R² 0.97, test R² -54.1) than the committed (0.99, -1450.0). | **Fixed.** Lowered to degree 8 (train R² 0.971, test R² −7.1, re-verified) — still a dramatic, unambiguous overfitting story, far less numerically explosive across library versions. |
| Major | `10-statistical-foundations-and-ml.ipynb`, content scope | k-means clustering and PCA were absent — not even as going-deeper boxes — despite the syllabus naming both, and despite the old book's counterpart covering k-means as a primary topic. | **Fixed.** Added as core content (not going-deeper), using the real Palmer Penguins dataset — see `course-plan.md` for detail. |
| Minor | `10-statistical-foundations-and-ml.ipynb`, seaborn coverage | seaborn is used for exactly two plot types (`regplot`, `heatmap`) vs. the old book's dedicated seaborn subchapter. | **Left as-is** — a defensible framing choice (seaborn as an EDA tool feeding modelling, not a chart-type tour), not touched. |
| Minor | `05-pandas.ipynb`, Resources | The McKinney "Python for Data Analysis" link's exact page slug couldn't be independently verified (site blocks automated fetches with a 403); domain and book are confirmed real. | **Not re-checked** — low risk, left as originally written. |

### Everything else checked and clean

- **Structure/order** (content → AI-critique → takeaways → resources): correct in all six notebooks — none needed the kind of reordering 1.4 did.
- **Admonition palette**: every box in 05–10 uses its assigned class correctly; each notebook has at most one `important`-class computational-thinking box, as required.
- **Style**: no "ai assistants" lowercase slip anywhere in 05–10 (they consistently phrase it as "an assistant" / "asked to...", which sidesteps the issue that hit 1.3/1.4 entirely).
- **Sequencing**: no core-code use of an unintroduced construct. Two soft, book-order dependencies are worth naming for the course plan rather than flagging as bugs: 06's core code uses `raise ValueError(...)` and 07 uses type hints throughout every method signature — both were only formally introduced as *going-deeper*, optional material back in 1.2, and both get their first *core*, dedicated treatment in 1.8 (defensive programming) specifically. Since 1.8 is one of the two chapters being cut from live teaching, this is worth a one-line mention when teaching 06 and 07 live — see `course-plan.md`.
- **Outputs**: independently re-verified (via scratch installs, not the project's own environment) for 05 spot-checks, all of 06, all of 09 except cell 4, and all of 10 except the degree-10 cells noted above. Nothing else was stale.
- **Exercises structure** (as of the original pass): all six exercises notebooks (05–10) correctly used inline `note dropdown` solutions for every exercise, matching 07/08's pattern at the time. Superseded since: all ten subchapters' exercises notebooks were later split into blank-cells-only exercises plus a separate solutions notebook each, and all exercise headings standardized to colon style — see `final-audit.md` and `course-plan.md`.

## The title-numbering mess, as found (now fixed book-wide)

| File | Lecture H1 said | Exercises H1 said |
|---|---|---|
| 01–04 | correct (1.1–1.4) | *(no number, "# Exercises")* |
| 05 | correct (1.5) | **1.10** |
| 06 | number right, **topic text wrong** ("GeoPandas and Cartopy") | **1.12** |
| 07 | correct (1.7) | **1.14** |
| 08 | **1.15** | **1.16** |
| 09 | **1.17** | **1.18** |
| 10 | **1.8** | **1.20** |

Two different stale schemes were visible here: 08/09's lecture numbers and all of 05–10's exercise
numbers followed an old double-numbering convention (tutorial = 2×position−1, exercise =
2×position) left over from before subchapters were consolidated; 10's lecture number (1.8) instead
reflected an even earlier plan where this was going to be the book's 8th and final subchapter,
before geospatial (09) and defensive programming (08) were inserted ahead of it. All of 05–10's
lecture titles now read `1.N)` matching file position, and all exercises notebooks (01–10) now
uniformly use the bare "# Exercises" title, resolving the second, unrelated inconsistency too.
