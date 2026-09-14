# Comparison: 1.5 Pandas

Old counterpart: **1.9 Tabular Data with Pandas** (tutorial, `W3_S1_Tutorial.html`) +
**1.10 (Exercise) Earthquake Data Analysis** (`W3_S1.html`).

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.9.1 Introduction | Pandas as a data-analysis library overview | **Kept** in spirit as new 1.5's opening framing. |
| 1.9.2 Pandas Data Structures: Series | Creation, labelled 1D array | **Kept** — new 1.5's "Series and DataFrame" section. |
| 1.9.2.1 Indexing | Accessing Series elements by index | **Kept**, folded into the broader "Selecting: .loc, .iloc, and boolean masks" section rather than a Series-only topic. |
| 1.9.3 Pandas Data Structures: DataFrame | Two-dimensional tabular structure | **Kept.** |
| 1.9.4 Merging Data | Combining multiple datasets | **Kept** — new 1.5's "Combining tables: merge and concat" pairs `merge` with `concat`; `concat` specifically not confirmed as covered in old. |
| 1.9.5 Modifying Values | Updating/transforming data elements | **Restored** — new 1.5 has a dedicated "Updating and transforming values" section (column assignment for a derived column, and a masked `.loc` update for matching rows only), right after the selecting section. |
| 1.9.6 Plotting | Pandas' built-in `.plot()` convenience methods | **Restored** — new 1.5 has a "Quick plots with .plot()" section (a line plot and a `kind="bar"` groupby summary via the pandas convenience wrapper). matplotlib/xarray (1.4, taught first) and seaborn (1.10) still own the fuller plotting content; this section stays deliberately thin. |
| 1.9.7 Time Indexes | Datetime-based indices | **Kept and expanded** — new 1.5's "A datetime index: resample and rolling windows" adds `.rolling()`, not confirmed as covered in old. |
| 1.9.8 Reading Data Files: Weather Station Data | Loading external data | **Kept**, made more deliberate — new 1.5 explicitly pins `dtype`/`parse_dates` on `read_csv` as a robustness habit, framing not confirmed as emphasized in old. |
| 1.9.9 Quick statistics | Summary statistics | **Kept** — folded into new 1.5's missing-data and groupby sections rather than a standalone "quick stats" topic. |
| 1.9.10 Plotting Values | More `.plot()` usage | **Restored**, same section as 1.9.6 above. |
| 1.9.11 Resampling | Changing time-series frequency/aggregation | **Kept** — part of the same section as 1.9.7 above. |
| *(not confirmed anywhere in old outline)* | `groupby`, `isna`/`fillna`/`dropna` | **New, or at least not confirmed old.** A direct text search of the old tutorial's retrievable content found none of these terms present. New 1.5 makes missing-data handling and `groupby` two of its central topics — see below. `.loc`/`.iloc` are not new: `W3_S1_Tutorial.ipynb` uses `.loc[` 10 times and `.iloc[` 8 times in a dedicated "Modifying Values" section, so new 1.5's "Selecting: .loc, .iloc, and Boolean Masks" section continues existing old-book material rather than introducing it. |
| Old 1.10, learning objectives | Log-scale axis exercise, filtered-vs-unfiltered histogram comparison | **Restored.** New Exercise 8 (a log-scale axis, `logy=True` on a right-skewed synthetic discharge series) and Exercise 9 (filtered vs. unfiltered histogram, a synthetic stuck-sensor scenario) cover both directly. The earthquake capstone (now Exercise 10) also gained a sixth step doing the same log-scale-histogram task on real event depths, tying the synthetic practice to the real dataset. |
| Old 1.10 dataset | Real earthquake catalog | **Different dataset, same idea restored.** New 1.5's Exercise 10 (renumbered from 8 after Exercises 8–9 were inserted ahead of it) uses a real, pinned USGS earthquake catalog snapshot (629 events, magnitude ≥ 4.5, January 2023) — a genuine real-dataset capstone, built around parsing/resampling/grouping/missing-data auditing, now also including the old exercise's log-scale-histogram task (step 6) on event depth. |

## New in the new book, no old-book counterpart

- The "missing is not zero" computational-thinking box and the `fillna(0)` AI-critique — no dedicated missing-data section confirmed anywhere in old 1.9.
- `groupby` as a named, dedicated section with multiple named aggregations (`.agg(mean_temp=..., max_discharge=..., n_obs=...)`).
- `.rolling()` windows.
- Going-deeper on time zones, multi-index, `apply`, and polars as a fast alternative — none confirmed in the old material.
- Exercise 10's real USGS earthquake capstone, structured as the "long exercise, hints as comments, no solution" pattern already used in 1.1 and 1.3 — 1.5 didn't have one of these before this pass.

Every short exercise (1–9) is blank with a matching worked solution in a separate
`1.5-pandas-solutions.ipynb`; Exercise 10, the real-dataset walkthrough, has no solution provided.

**2026-09-14 — the old book's USGS earthquake photo restored to Exercise 10.** The old pandas
exercises notebook (`W3_S1.ipynb`) opened with a USGS photograph of surface rupture from the 2014
South Napa earthquake, embedded as base64 with a short caption; the new 1.5 exercises had no
image. Re-added to Exercise 10, the USGS-catalog capstone, between the description of the data
and the "everything you need is from this subchapter" line.

Sourced from the USGS page the user supplied
(<https://www.usgs.gov/media/images/2014-south-napa-ca-m6-earthquake-august-24-6>), which was
fetched and confirmed to resolve: title "2014 South Napa CA M6 Earthquake - August 24", explicitly
**public domain**, and its own description matches the old book's caption word for word, so the
old caption was a verbatim quote of the USGS one. The full-size original (2592 × 1936, 4.1 MB)
was downscaled to 1600 px wide / 598 KB and committed as
`part-I/_static/usgs-2014-south-napa-earthquake.jpg` — the old book's embedded copy was only
1180 × 881, so this is a better version of the same photograph, not a re-encode of theirs.

The caption keeps the USGS wording on the "mole track" and the east–west compression, keeps the
old book's link to the USGS fault-types explainer, adds the magnitude and full date, and credits
the image page and its public-domain status. One added clause ties it to the exercise — the photo
is what one row of the catalog being loaded actually looks like on the ground. Figure styling
follows the convention the other part-I photographs use (`width: 800px`, credit as an HTML anchor
in the caption), not the 100%-width used for the replication targets in 1.4.

**2026-09-14 — pandas logo added as the subchapter cover.** 1.5 was the only part-I subchapter
with a library of its own but no logo: 1.3 opens with the numpy logo and 1.4 with matplotlib's,
cartopy's and xarray's. Added in its own markdown cell between the H1/intro cell and the
learning-objectives box, the same position and figure styling those use (`width: 500px`, credit
as an HTML anchor in the caption).

Fetched from the Wikimedia Commons page the user supplied, which was checked before use: the file
is the project's own logo, designed by Marc Garcia (22 October 2019), taken from the pandas
repository's `web/pandas/static/img/pandas.svg`, and carries the BSD-3-Clause licence with the
"Copyright © 2008 AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team"
notice. Downloaded from `upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg` and
committed as `part-I/_static/pandas_logo.svg` (2.6 KB vector, so it stays sharp at any width —
same choice as 1.4's `xarray_logo.svg`). The caption names the designer, links the Commons page,
and states the licence.

**2026-09-14 — Exercise 10 restored to the original book's eleven questions.** The old pandas
exercises notebook (`W3_S1.ipynb`, "(Exercise) Earthquake Data Analysis") was a single
eleven-question walkthrough of one real USGS catalog; the new 1.5's Exercise 10 had compressed it
to six steps on a different, smaller snapshot. Rewritten to the original's content, question count
and links.

*Dataset switched back.* The original's `known_hash` (`84d455fb…`) is the hash of
`data/part-I/usgs_earthquakes_2014.csv` — the 2014 worldwide catalog, 120 108 rows — not the
January 2023 snapshot the rewrite had used. Exercise 10 now fetches the 2014 file from the repo's
own raw URL, and the variable is called `datafile`, as the original's prose names it.
`usgs_earthquakes_2023_01.csv` stays referenced by 1.7's exercises, so nothing is orphaned.

*The eleven questions, as in the original:* Q1 imports and display options · Q2 `read_csv` then
`.head()`/`.info()`, ending on the observation that the date columns were not parsed · Q3 re-read
with both date columns parsed and the earthquake ID as the index · Q4 `describe` · Q5 `nlargest`
for the top 20 by magnitude · Q6 extract the state or country out of `place` with `.str.split` into
a new `country` column · Q7 `unique` on it · Q8 filter to magnitude above 4 · Q9 count the filtered
events [Num 1], count per country with `value_counts` [Num 2], and bar-chart the top 5 · Q10
histogram of magnitude, then the same with a logarithmic count axis, then filtered against
unfiltered side by side · Q11 scatter of longitude against latitude coloured by magnitude,
filtered against unfiltered. Closes on the original's own question: "Do you notice a difference
between the filtered and unfiltered datasets?"

*Links.* Every documentation link from the original is carried over and **each was fetched and
checked**. One was dead: the `DataFrame.hist` link pinned to pandas 0.23
(`pandas-docs/version/0.23/generated/pandas.DataFrame.hist.html`) 404s, replaced with the current
canonical `pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html`. A `value_counts` link
was added where the original only named the function. The USGS fault-types link in the photo
caption returns 403 to a plain `curl` but 200 to a browser user agent — bot filtering, not a dead
page.

*What was not carried over.* The original's Colab "fill in the blank version. Double click to
reveal" cells, which do not work outside Colab and conflict with the book's prompt → empty cell
convention; the "assignment" framing and the emoji; and the dead SharePoint data URL. The
original's five plot screenshots were re-rendered from the real 2014 data at proper resolution
instead of being extracted as low-res JPEGs — `1.5-target-top5-bar.png`,
`1.5-target-magnitude-hist.png`, `1.5-target-magnitude-hist-log.png`,
`1.5-target-hist-filtered-unfiltered.png`, `1.5-target-quake-scatter.png`, each matching the
original's design (the top-5 counts come out at 1907/1290/1114/990/729, matching the original
screenshot's bars). The original's five *table* screenshots were not reproduced: they are
screenshots of dataframe output in someone's Colab, and the expected result is stated in prose
instead.

**Sequencing gap, flagged not silently fixed.** Restoring the original's questions brings in six
things 1.5's lecture never demonstrates: `describe`, `nlargest`, string methods including
`.str.split`, `value_counts`, `.count()`, and scatter plots. The lecture does cover `read_csv`,
`.head()`, `.info()`, `.unique`, `kind="bar"`, `kind="hist"` and `logy`, so Q1–Q3, Q7, Q9's chart
and Q10's histograms sit on taught ground. The original handled the rest by giving a documentation
link per function, which is why every question carries one, and those links are preserved — but by
the book's own sequencing rule this is a gap in 1.5's lecture, not a licence in the exercise.

Verified: all eleven questions walked through end to end against the real file — the pooch fetch,
both reads, `describe`, `nlargest`, the split, `unique` (201 distinct values, coming out with the
leading space a plain split leaves, as Q7 now says), the filter (16 371 events), the counts, all
three histograms and both scatter panels. Markdown and empty cells only, so no notebook execution
is needed.
