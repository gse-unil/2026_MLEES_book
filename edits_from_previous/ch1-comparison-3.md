# Comparison: 1.3 Scientific Computing with Numpy

Old counterpart: **1.5 Scientific Computing with Numpy** (tutorial, `W2_S1_Tutorial.html`) +
**1.6 (Exercise) Ocean Floats Data Analysis** (`W2_S1.html`).

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.5.1 Importing and Examining a New Package | `import numpy as np`, exploring a library with `dir()` | **Dropped.** New 1.3 doesn't teach the `dir()`-exploration habit; it goes straight into arrays. |
| 1.5.2 NDArrays | The `ndarray` object, advantages over lists (dimensions, uniform dtype, speed), `dtype`/`shape` | **Kept and expanded** — new 1.3's opening comparison table (dimensions/contents/arithmetic/speed) covers the same ground, plus a going-deeper box on `dtype`/precision (`float32` vs. `float64`) not confirmed as covered in old. |
| 1.5.3 Array Creation | `zeros()`, `ones()`, `full()`, `arange()`, `linspace()`, `logspace()`, `meshgrid()` | **Mostly kept.** `zeros`/`ones`/`full`/`arange`/`linspace`/`meshgrid` all confirmed in new 1.3. `logspace()` not confirmed — possibly dropped or just unmentioned. |
| 1.5.4 Indexing | Element selection, row/column extraction, slicing, boolean indexing | **Kept**, expanded with a computational-thinking box ("think in arrays, not loops") and a going-deeper box on memory layout/views/strides — neither confirmed present in the old material. |
| 1.5.5 Visualizing Arrays with Matplotlib | 1D arrays with `plot()`, 2D arrays with `pcolormesh()`, used inline within the numpy lesson | **Moved to new 1.4.** New 1.3 has no plotting at all; numpy and its visualization were deliberately split into separate subchapters. |
| 1.5.6.1 Array Operations — Basic Math | Element-wise arithmetic, trigonometric functions | **Kept**, folded into "vectorised math" generally rather than kept as its own catalogued subsection; specific trig functions not individually itemized in new 1.3. |
| 1.5.6.2 Array Operations — Manipulating Dimensions | `transpose()`, `reshape()`, `tile()` | **Reduced.** `reshape` is confirmed core in new 1.3. `transpose()` and `tile()` are not confirmed — no equivalent seen. |
| 1.5.7 Broadcasting | Aligning shapes from the last axis backwards | **Kept and deepened** — new 1.3 adds explicit `[:, None]`/`np.newaxis` treatment and a dedicated going-deeper box on vectorisation vs. loops, neither confirmed in old. |
| 1.5.8 Reduction Operations | `sum()`, `mean()`, `std()`, axis-specific reductions | **Kept** — new 1.3 adds `argmin`/`argmax`/`cumsum`/`cumprod` to the reduction table and a method-vs-function equivalence box (`arr.mean()` vs `np.mean(arr)`), not confirmed as an explicit topic in old. |
| 1.5.9 Data Files | `np.save()`/`np.load()` for `.npy` | **Kept**, with an added note that `.npy` is for convenience, not archiving (self-describing formats like netCDF recommended instead) — framing not confirmed in old. |
| *(no old equivalent)* | — | **New:** boolean masking as its own named topic; `np.where`; NaN-aware reductions (`np.nanmean`) vs. ordinary ones; `np.interp` for 1D gap-filling; a going-deeper box on basic linear algebra (`np.linalg.solve`); a going-deeper box on dask for bigger-than-memory arrays. None of these are confirmed anywhere in the old material — old 1.5's outline shows no missing-data, interpolation, or linear-algebra content at all. |
| Old 1.6, learning objectives | `linspace`/`arange`, computing formulas with arrays, loading `.npy` files, reductions (mean/std), 1D line plots and scatterplots, annotating plots | **Reworked.** New 1.3's Exercise 9 (Argo ocean float profiles) covers array loading, axis rebuilding, reductions, masking, and NaN-aware statistics — but explicitly defers plotting to 1.4 ("you will return to this same data... to plot it"), unlike the old exercise which did its own plotting inline. |
| Old 1.6 exercise body | Real Argo data; reductions and plotting, no confirmed density computation | **Expanded.** New Exercise 9 goes further: it computes real seawater density from the data via the `gsw` (TEOS-10) library — no evidence of a density computation in the old exercise. |

## New in the new book, no old-book counterpart

- Boolean masking, `np.where`, NaN-aware reductions, and `np.interp` — a whole missing-data/interpolation thread absent from old 1.5.
- Going-deeper boxes on linear algebra and dask.
- The dtype-truncation AI-critique (`np.zeros_like` silently inheriting an integer dtype) — no AI-critique device exists anywhere in the old book.
- The `gsw`-based real seawater-density computation in Exercise 9.

Every short exercise (1–8) is blank with a matching worked solution in a separate
`1.3-numpy-solutions.ipynb`; Exercise 9, the real-dataset walkthrough, has no solution provided.
