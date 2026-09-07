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
| *(not confirmed anywhere in old outline)* | `groupby`, `isna`/`fillna`/`dropna`, `.loc`/`.iloc` by name | **New, or at least not confirmed old.** A direct text search of the old tutorial's retrievable content found none of these terms present. New 1.5 makes missing-data handling and `groupby` two of its central topics — see below. |
| Old 1.10, learning objectives | Log-scale axis exercise, filtered-vs-unfiltered histogram comparison | **Restored.** New Exercise 8 (a log-scale axis, `logy=True` on a right-skewed synthetic discharge series) and Exercise 9 (filtered vs. unfiltered histogram, a synthetic stuck-sensor scenario) cover both directly. The earthquake capstone (now Exercise 10) also gained a sixth step doing the same log-scale-histogram task on real event depths, tying the synthetic practice to the real dataset. |
| Old 1.10 dataset | Real earthquake catalog | **Different dataset, same idea restored.** New 1.5's Exercise 10 (renumbered from 8 after Exercises 8–9 were inserted ahead of it) uses a real, pinned USGS earthquake catalog snapshot (629 events, magnitude ≥ 4.5, January 2023) — a genuine real-dataset capstone, built around parsing/resampling/grouping/missing-data auditing, now also including the old exercise's log-scale-histogram task (step 6) on event depth. |

## New in the new book, no old-book counterpart

- The "missing is not zero" computational-thinking box and the `fillna(0)` AI-critique — no dedicated missing-data section confirmed anywhere in old 1.9.
- `groupby` as a named, dedicated section with multiple named aggregations (`.agg(mean_temp=..., max_discharge=..., n_obs=...)`).
- `.rolling()` windows.
- Going-deeper on time zones, multi-index, `apply`, and polars as a fast alternative — none confirmed in the old material.
- Exercise 10's real USGS earthquake capstone, structured as the "long exercise, hints as comments, no solution" pattern already used in 1.1 and 1.3 — 1.5 didn't have one of these before this pass.

Every short exercise (1–9) is blank with a matching worked solution in a separate
`05-pandas-solutions.ipynb`; Exercise 10, the real-dataset walkthrough, has no solution provided.
