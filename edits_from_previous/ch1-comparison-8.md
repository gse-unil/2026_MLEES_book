# Comparison: 1.8 Statistical Foundations and the Machine-Learning Stepping-Stone

Old counterpart: **1.13 Regression, Classification, and Clustering with Scikit-learn** (tutorial,
`W4_S1_Tutorial.html`) + **1.14 (Exercises) Multivariate linear regression and clustering**
(`W4_S1.html`), plus **1.15 Statistical Graphics with Seaborn** (tutorial, `W4_S2_Tutorial.html`)
+ **1.16 (Exercise) Marathon Data Analysis** (`W4_S2.html`). The new book folds two old
subchapters (sklearn and seaborn) into one.

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.13.1 Linear Regression | `LinearRegression`, fit/predict on synthetic `y = 2x - 5 + noise`, least-squares framing | **Kept**, reframed around a real physical quantity (elevation → temperature lapse rate) instead of an abstract `y = 2x - 5` example. |
| 1.13.2.1 K-means Clustering | Algorithm explanation, 300 synthetic points in 4 clusters, `sklearn.cluster.KMeans` fit/predict | **Kept, real data restored.** New 1.8 clusters the real Palmer Penguins dataset (not synthetic points) on two features, as core content. |
| 1.13.2.2 Palmer Penguin Dataset | Real Palmer Penguins data (344 observations, 3 species), `body_mass_g`/`flipper_length_mm`, `n_clusters=3` vs. `n_clusters=2` compared | **Kept and extended.** New 1.8 uses the same real dataset and the same two features (`flipper_length_mm`/`body_mass_g`) for `k=3`; the `k=2` comparison specifically moved to Exercise 9 (renumbered from 8 after Exercise 5 was inserted ahead of it) rather than the lecture. A crosstab against true species (not confirmed as used in old) makes the imperfect 2-feature clustering explicit. |
| 1.13.2.3 Find the Right Cluster Number (elbow method) | Choosing *k* via inertia/elbow curve | **Restored, core.** New 1.8 now has a "Choosing k: the elbow method" subsection right after the fixed-`k=3` clustering demo — it refits `KMeans` across `k=1..6`, plots inertia, and diagnoses the bend, explicitly framed as "in general the right number of clusters is not known in advance." `sklearn.metrics.silhouette_score` is named as a complementary diagnostic in a one-line comment, not worked in full — the elbow curve carries the core content. |
| 1.13.3 Linear Classification | Heading confirmed present in the old table of contents; body content could not be retrieved despite repeated attempts — the source page truncates before this section in every fetch tried. Not verified whether it covers logistic regression, decision boundaries, or something else. | **Restored to core.** New 1.8 now has a dedicated "Linear classification" section between "Scaling and pipelines" and "Unsupervised learning": `LogisticRegression` fit on a frost/no-frost target derived from the same lapse-rate data (`temp_celsius < 0`), with a real train/test accuracy reported. The old going-deeper snippet is retargeted, not removed — it now covers classifiers *beyond* a linear boundary (k-NN, decision tree), since logistic regression itself is no longer going-deeper material. |
| *(not confirmed anywhere in retrievable old outline)* | Train/test split, RMSE, R², overfitting | **New, or at least not confirmed old.** Nothing in old 1.13's retrievable content (linear regression, clustering) mentions a train/test split or an evaluation metric; the syllabus's own topic list for this session ("Linear/logistic regression, k-means, PCA") doesn't mention evaluation methodology either. This is new 1.8's central, and strongest, addition. |
| *(not confirmed)* | PCA / dimensionality reduction | **Added.** No PCA content confirmed anywhere in old 1.13's retrievable material (nor named in the syllabus for this session) — new 1.8 covers it as core content on the real Palmer Penguins data. |
| 1.15.1 Seaborn Versus Matplotlib | High-level vs. low-level interface comparison | **Restored**, as a framing paragraph rather than a dedicated section — appended to the opening "Exploratory data analysis with seaborn" intro: seaborn is "a layer on top of" matplotlib, `ax=` still composes with it, and matplotlib remains the tool of choice whenever a plot needs more control than seaborn's defaults give. |
| 1.15.2.1 / 1.15.2.2 Histograms, KDE, and Densities | Distribution plots with KDE overlays | **Restored, core.** New 1.8 has a dedicated "Histograms, KDE, and Density Plots" section on the real Palmer Penguins data: `sns.histplot(..., hue="species", kde=True)` and `sns.jointplot(..., kind="kde")`, modernised from the old tutorial's deprecated `sns.distplot`/`shade=` calls into current, non-deprecated seaborn API (`histplot`+`kde=True`, `fill=`). |
| 1.15.3 Faceted Histograms | Multi-panel histogram displays, style customization | **Restored, as going-deeper** (not core, per your instruction) — `sns.displot(data=penguins, x="body_mass_g", col="species", ...)` on the real Palmer Penguins data already loaded earlier in the lecture. |
| 1.15.4.1 Boxplots | Distribution summaries by category | **Restored, as going-deeper** — `sns.boxplot` of `body_mass_g` by `species`, same real dataset. |
| 1.15.4.2 Bar Plots | Aggregated categorical comparisons | **Restored, as going-deeper** — `sns.barplot` of mean `flipper_length_mm` by `species`, with an error bar, same real dataset. |
| 1.15.5 Heat Maps | Correlation matrices via colour intensity | **Kept** — new 1.8's `sns.heatmap(df.corr()...)` covers this directly. |
| Old 1.14, Exercise 1 | Real advertising dataset (Sales ~ TV + Radio + Newspaper), multivariate `LinearRegression`, extract coefficients | **Restored** as new Exercise 5 ("Multivariate regression on real advertising data"), inserted right after Exercise 4 (Honest evaluation), renumbering everything from the old Exercise 5 onward by one. Builds `X` from `TV`/`Radio`/`Newspaper`, fits and evaluates with a train/test split, prints the three coefficients, and asks which channel's coefficient is largest — then, before letting that stand as an answer, what to check about the three columns' scales (a deliberate callback to the pipeline/scaling exercise that now follows it). **Resolved:** `data/part-I/Advertising.csv` has since been supplied and committed (200 rows, columns `TV`/`Radio`/`Newspaper`/`Sales` confirmed matching), and both the exercise and its solution now fetch it via `pooch.retrieve` rather than a bare path — this was also a fix for a real Colab-breaking bug (bare relative paths don't resolve in a fresh Colab session), not just a data-sourcing gap. |
| Old 1.14, Exercise 2 | Real Palmer Penguins clustering: drop missing values, elbow test, silhouette analysis, `k=3` then `k=2` | **Fully restored.** Missing-value handling (`.dropna()`) and the `k=3`/`k=2` comparison carry over into new 1.8's lecture and Exercise 9 (renumbered from 8) respectively; the elbow method is now core lecture content (see 1.13.2.3 above), closing the gap this row used to flag. |
| Old 1.16 (Marathon Data Analysis) | Real race-results dataset, presumably exercising seaborn's statistical-graphics toolkit | **Restored, with a different (and more relevant) dataset, per your instruction.** New Exercise 10 uses the real UCI Forest Fires dataset (Cortez & Morais, 2007 — 517 real fires, Montesinho natural park, Portugal; `data/part-I/forest_fires.csv`, downloaded and verified, hash pinned), exercising the newly-restored seaborn categorical toolkit (`boxplot` of temperature by month, `barplot` of wind by month) plus a filtered-vs-unfiltered histogram on the heavily right-skewed `area` (hectares burned) column — an environmental-science-appropriate swap for the old marathon-results exercise. |

## New in the new book, no old-book counterpart

- The entire train/test-split, RMSE/R², and overfitting narrative, and its AI-critique (a degree-8 polynomial scoring ~0.97 on training data, collapsing to roughly −7 on held-out data).
- `Pipeline` + `StandardScaler`, framed specifically around preventing test-set leakage.
- PCA as core content.
- The explicit callback to the OOP subchapter's "estimator-as-object" going-deeper box, tying `fit`/`predict` back to the class pattern taught in 1.7 — a cross-subchapter link the old book, with classes taught in a different week entirely, couldn't make.
- Going-deeper on statsmodels for inferential regression and bootstrap confidence intervals.

## Where this leaves the trade-off

**Status: every gap flagged below in the original pass has since been closed**, per your
follow-up instructions (elbow method, linear classification, seaborn-vs-matplotlib, the three
seaborn chart-type going-deeper boxes, the advertising exercise, and a forest-fires exercise in
place of the marathon one). New 1.8 now has real evaluation rigor (train/test, RMSE/R²,
overfitting, leakage) that old 1.13 didn't have, restores k-means clustering and elbow-method
k-selection plus adds PCA using the real Palmer Penguins data old 1.14 used, restores linear
classification to core, and covers multivariate real-data regression (advertising) and a
categorical-seaborn real-data exercise (forest fires) that old 1.14/1.16 had and new 1.8
initially didn't, and now also restores histograms/KDE/density plots (old 1.15.2), the one
seaborn item still marked dropped as of the previous pass. The advertising CSV gap (see the
Exercise 1 / old 1.14 row above) is resolved too — no open items remain from this file's original
audit.

Every exercise (1–10) is blank with a matching worked solution in a separate
`1.8-statistical-foundations-and-ml-solutions.ipynb`. Exercises 5 (advertising), 9 (Palmer
Penguins), and 10 (forest fires) use real data; the rest remain synthetic. Unlike most other
subchapters, 1.8 gives every exercise — including its real-data ones — a full worked solution
rather than reserving a no-solution capstone slot.

**2026-09-14 — old 1.13 re-read from the local notebook, and the gaps it exposed closed.** The
table above records old 1.13.3 "Linear Classification" as *"body content could not be retrieved
despite repeated attempts"*. That is now superseded: the old notebook exists locally at
`2025_MLEES_book_online/notebook/W4_S1_Tutorial.ipynb` (83 cells) and was read in full. The
section turned out to be a worked penguin example, not a stub, and several other pieces of old
1.13 were missing from new 1.8 as well. All of the following are now in the lecture.

*Logos and dataset artwork.* A seaborn logo opens the seaborn half and a scikit-learn logo opens
the machine-learning half, matching the pattern 1.3–1.6 use (own markdown cell, credit as an HTML
anchor). The scikit-learn logo comes from the Commons file the user supplied, which states
BSD-3-Clause and names the scikit-learn developers as author; the seaborn logo from the project's
own documentation. Old 1.13 also carried two Allison Horst illustrations that new 1.8 had dropped,
both restored: the three-species artwork in a **new "The Palmer Penguins Dataset" section** (the
dataset was previously loaded with no introduction at all), and the bill-dimensions diagram where
`bill_length_mm`/`bill_depth_mm` are first used — that diagram also explains the *culmen* naming,
which is what the old book's column names used and this book's do not. Attribution follows the
package's own requirement ("Artwork by @allison_horst"), with the data credited to K. Gorman and
the Palmer Station Antarctica LTER under CC-0.

*Content restored from old 1.13:*
- **The three-pillars framing** (regression, classification, clustering) opening the scikit-learn
  section, and the **least-squares cost function** $J(w,b)=\sum (y_i-\hat{y}_i)^2$ written out —
  old 1.13.1 stated both; new 1.8 had neither.
- **More data, better parameters** (old cells 18–19): the lapse-rate fit repeated at 80, 800 and
  8000 stations, recovering −6.35, −6.54 and −6.51 °C km⁻¹ against the −6.5 built into the data.
- **k-means on `make_blobs` before the real data** (old cells 23–26), with the fitted centroids
  drawn as white squares. New 1.8 went straight to the messy penguin case; the clean case is what
  makes the algorithm legible.
- **The feature-plane comparison** (old cells 52–55): body mass against flipper length beside bill
  length against flipper length, showing that the species Adelie/Chinstrap overlap in the first
  plane and separate in the second. New 1.8 asserted this in prose without showing it.
- **Silhouette analysis** as a worked subsection (old 1.13's "Silhouette Analysis", cells 49–51),
  with the score defined and computed across k=2..6. It was previously a one-line comment naming
  `silhouette_score`. The mean score peaks at k=2 (0.630 against 0.580 for k=3), reproducing the
  old book's own finding — and the prose now says what that means: both diagnostics answer how
  separable *these two features* are, not how many species exist.
- **The penguin classification example** (old 1.13.3, cells 57–81), added as
  "Separating two species by bill shape" after the existing frost example: Adelie against
  Chinstrap on the two bill measurements, per-species histograms showing bill length separates and
  bill depth barely does, `train_test_split` with `stratify`, `StandardScaler` inside a pipeline
  (motivated by the ~3× scale difference between the two features, as the old tutorial motivated
  it), 0.97 test accuracy, and the fitted weights read back and drawn as a horizontal bar chart —
  3.79 for bill length against −1.19 for bill depth, the same dominance and signs the old
  tutorial reported. The old book's manual standardisation cells were not reproduced: the
  `StandardScaler` pipeline is already core content earlier in new 1.8.

*Deliberately not restored:* two images in the old notebook whose provenance is a medium.com
upload and a journal page (`1*UgYbimgPXf6XXxMy2yqRLw.png`, `1520-0469-JAS-D-20-0055...png`) —
neither carries a usable licence statement, so neither was reused.

Learning objectives and takeaways rewritten for the new material. Verified: all 24 code cells
extracted and run in order against the project environment, no errors; every printed number in the
new prose was checked against the actual output, and the quoted bill-measurement ranges
(32–58 mm, 15–21 mm) and record count (344 records, 342 after dropping the two with no body
measurements) against the committed dataset. The notebook needs `Restart & Run All`.

**2026-09-15 exercise/image audit:** 1.8 absorbed *two* old exercise pages — 1.14 (multivariate
regression + penguin clustering) and 1.16 (marathon/seaborn) — and is the thinnest-covered
subchapter in the chapter as a result. The advertising regression survives and is stronger than
the old version; the elbow method and silhouette analysis were dropped from the exercises despite
staying in the lecture, and 1.16 was dropped whole, taking `jointplot`, `PairGrid`, `kdeplot` and
`violinplot` with it. `PairGrid`/`pairplot` and `violinplot` now appear nowhere in Part I. Full
question-by-question mapping, plus the cheapest repairs, in
[`ch1-exercises-and-images-audit.md`](ch1-exercises-and-images-audit.md) §1 and §3.
