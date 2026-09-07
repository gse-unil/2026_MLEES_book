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
