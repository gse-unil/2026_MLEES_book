# TODO list

Working list of open items — Part III porting gaps from the current session, plus every
pre-existing `%TODO`-style marker found by scanning the rest of the book. Not published content.

## Part I — open from the pre-launch review

- ~~`data/part-I/S1_3_ex_lat.npy`, `S1_3_ex_lon.npy`, `S1_3_ex_temp.npy`~~ — **resolved.** These
  turned out to already be gone from the live `data/part-I/` tree (only stale worktree copies
  remained). `data/part-I/float_data/` itself — the directory this note said the files were
  superseded by — turned out to be orphaned too (confirmed unreferenced by any notebook; the
  exercises notebook uses `argo_float_data.zip` instead). Moved, not deleted, to
  `data/part-I/_orphaned/float_data/` on 2026-09-08.
- **The repeated "the distributed hand-out omits the solutions" phrasing** in every subchapter's
  exercises intro box (1.3–1.8, and now also 1.1/1.2 after retrofitting the missing box) sits
  close to CLAUDE.md's "never mention lectures/universities" spirit — "hand-out" evokes a
  classroom setting the book's own framing (an open, online textbook) doesn't otherwise use.
  Flagged during the 1.3 review; not changed since it's a deliberate, consistent choice repeated
  6+ times, not a one-off slip — needs an explicit decision, not a silent rewrite.
- **[Bonus A](../part-I/bonus-a-reproducible-data-pipelines-exercises.ipynb) exercises have no
  packaging/uv coverage.** All 6 exercises are from the data-pipelines half of the lecture only;
  none touch the `src/` layout, `uv init --lib`, or `uv.lock` content in the packaging half. Left
  as-is at your call — packaging is awkward to exercise "from scratch in an empty code cell"
  since it's CLI/project-scaffolding work, not notebook-native, which may be why it was never
  added rather than an oversight. Revisit if a CLI-description-style exercise format is wanted.
  Re-confirmed during the 2026-09-08 fix pass, still deliberate, still not touched.
- ~~[Bonus A](../part-I/bonus-a-reproducible-data-pipelines.ipynb) cell `ff96d4b8` (CSV vs.
  parquet size comparison) — committed `ImportError` traceback for a missing pyarrow
  dependency~~ — **resolved 2026-09-08, confirmed by the user.** `pyarrow` (and `zarr`, needed by
  the same notebook's format-tour section) added as proper `uv`-managed dependencies; the
  transient `ArrowKeyError: A type extension with name pandas.period already defined` seen on one
  run was environment/kernel noise, not a real problem — a clean re-run succeeded.
- ~~[1.8](../part-I/1.8-statistical-foundations-and-ml-solutions.ipynb) Exercise 7's overfitting
  demo~~ — **resolved 2026-09-08, verified by execution.** Needed three iterations beyond the
  initial km-rescaling: rescaling alone gave train R²=0.962/test R²=0.94 (not overfitting — the
  real cause was training-set size relative to the 9 parameters, not conditioning); shrinking the
  training set to 9-12 points (matching the lecture's near-saturated ratio) only closed the gap to
  ~0.19-0.26, since the elevations are randomly scattered rather than evenly spaced, so a sparse
  interpolation gap doesn't reliably force wild swings the way it does in the lecture's demo. The
  fix that actually worked was a different mechanism: train only on the lowest 30% of the
  elevation range and evaluate on the full test set, forcing extrapolation — degree-8 polynomial
  extrapolation error grows explosively outside the fitted range, regardless of point count or
  noise. Confirmed result: train R²=0.895, test R²≈−1.16×10¹². Both the exercise prompt and
  solution updated to match.
- **New, found during the 2026-09-08 fix pass:** [1.5](../part-I/1.5-pandas.ipynb) — a discrepancy
  surfaced between two review passes: cells `8a6e288b`, `3eabc0f4`, `30861396` were originally
  reported as having zero committed output, but on a later pass all three already had output in
  the file. Not re-investigated further; worth a quick glance to confirm the current output is
  genuinely current and not stale.

### 2026-09-15 exercise/image audit — resolved the same day

Everything raised by [`ch1-exercises-and-images-audit.md`](ch1-exercises-and-images-audit.md) was
actioned in the same session; see that file's §6 for the full record. Closed:

- ~~1.1 solutions cells 14–19 shifted and duplicated~~ — **resolved.** Each answer now sits under
  its own heading; the duplicate π solution and the stale "Exercise 7" heading are gone.
- ~~1.4's "The last two have no worked solution"~~ — **resolved.** The sentence was false and has
  been deleted from both notebooks; Exercises 20 and 21 keep their solutions.
- ~~1.3 promising the Argo plots in 1.4~~ — **resolved.** The three old plotting questions are back
  in 1.3 Exercise 9 as Steps 9–11, where the 2025 book had them, with its own target figures and a
  "Beyond this subchapter" box for `matplotlib`. Both forward references rewritten.
- ~~`data/part-I/USGS_Earthquakes.zip` orphaned~~ — **resolved.** Removed.
- ~~Exercise coverage gaps in 1.8~~ — **resolved** except `enumerate` (see below). The old penguin
  clustering exercise is back as 1.8 Exercise 11 (elbow, `silhouette_score`, both k=3 and k=2
  scatters) and the old marathon exercise as 1.8 Exercise 12 (`jointplot`, `PairGrid`, `kdeplot`,
  `violinplot`), each with its original target figures.
- ~~Missing figures~~ — **resolved.** The Argo dive-cycle diagram is in 1.3 Exercise 9, the
  expectation-maximization figure in 1.8's k-means section, the NASA montage in 1.2 Exercise 16.

Correction to the audit: 1.8 Exercises 5, 9 and 10 *did* have solutions — hidden below the
`pooch.retrieve` call inside cells labelled "Pre-supplied: download the data file". Those three
cells have been split so the label tells the truth. No other Part I notebook has that pattern.

## Cross-part — TOC titles, 2026-09-15

Chapter-page card titles were checked against every linked page's own H1, on the rule that the page
title is the real title. Seventeen cards were stale and have been rewritten to match:
ch-1 (six: 1.1, 1.3, 1.4, 1.5, 1.6, 1.7), ch-3 (four), ch-4 (three), ch-6 (two), ch-7 (two).
All 42 chapter-page cards now match their page exactly.

The cards were only half of it. `myst.yml`'s sidebar carried its own `title:` overrides holding the
same stale short titles, so fixing the cards alone would have left the sidebar and the chapter page
disagreeing. Eleven subchapter overrides (Parts II and III) were deleted so the sidebar inherits the
page H1 — which is what Part I already does, and why Part I's sidebar was correct while its chapter
page was not. Deleting the override rather than correcting it is what stops this drifting again.

**Then, at your instruction, the exercise page titles were put back to the 2025 book's own
`(Exercises)/(Exercise) Topic` format** — fixing it at the source rather than in the TOC, so the
cards and the sidebar both inherit it. The 2025 book's sidebar was re-fetched to get the wording
verbatim rather than reconstructed; it uses plural in chapters 2, 3 and 8 and singular in 4 to 7
and 9 to 11, and that split is now reproduced exactly. Ten notebook H1s changed:

| Page | Was | Now |
|---|---|---|
| 3.2 | Exercise 1: Comparing Different Types of Support Vector Machines for Classification | (Exercises) Support Vector Machines |
| 3.3 | Exercise 2: Training and Fine-Tuning a Decision Tree for the Moons Dataset | (Exercises) Decision Trees and Random Forest |
| 3.4 | Exercise 3: Comparing (Ensemble of) Classifiers on MNIST Data | (Exercises) Ensemble Modeling and Stacking |
| 3.5 | Exercise 4: Mapping Wildfire Susceptibility in the Liguria Region with Simple Machine Learning Classifiers | (Exercises) Wildfire Susceptibility Mapping |
| 4.2 | Dimensionality Reduction | (Exercise) Dimensionality Reduction |
| 4.3 | Clustering | (Exercise) Clustering |
| 4.4 | Ocean Regimes Identification | (Exercise) Ocean Regimes Identification |
| 6.3 | (Exercise) Land Cover Classification using Convolutional Neural Networks (CNNs) | (Exercise) Land Cover Classification |
| 7.3 | Exercise 1: Comparing Different Types of Recurrent and Convolutional Neural Networks to Compose Bach Chorales | (Exercise) Composing Music |
| 7.4 | Exercise 2 – Recurrent Neural Networks for Hydrological Modeling | (Exercise) Hydrological Modeling |

2.2, 2.3, 2.5, 5.2, 6.2, 8.2, 9.2, 10.2, 10.3 and 11.2 already carried the format and were left
alone. Nothing in the book's prose cross-referenced any of the removed long titles.

After the retitle, all 39 chapter-page cards match their page, `myst.yml` has no subchapter title
override left to drift, and the only sidebar/page differences remaining are the deliberate
`N)` vs `Chapter N:` numbering on the ten chapter landing pages.

Still open, and needing your call:

- **`index.md` was not touched** — its cards point at part-level pages, not chapters, and its titles
  are deliberately short ("Part I — Scientific Python" for a page titled "(Part I) Basics of
  Scientific Programming for Applied Machine Learning"). Note that its Part IV card reads
  "Towards **Thustworthy** AI" — a typo, in four separate copies of the card block.
- **There is no `part-III/ch-5-intro.md`.** Chapters 6, 7 and 8 have landing pages; chapter 5 does
  not, and its `myst.yml` entry is commented out. Consistent with 5.3 being unstarted, but it means
  5.1 and 5.2 currently hang off the part page with no chapter card.
- ~~Pre-existing notebook hygiene: missing and duplicate cell ids~~ — **resolved 2026-09-15.**
  All 62 notebooks declared `"nbformat_minor": 5`, which requires a per-cell `id`, but 1385 of 2888
  cells had none: 26 legacy notebooks ported from the 2025 book had none at all, and 15 Part I
  notebooks were a mix from tooling that did not add the field. 1385 ids added and the two duplicates
  in `part-I/1.4-matplotlib-and-xarray.ipynb` renamed. `nbformat.validate` is now clean across all
  62 with warnings promoted to errors.

  Worth knowing how it was done, in case the pass is ever repeated: writing notebooks back through
  `nbformat` or a default `json.dumps` reformats the whole file — it unescapes `\uXXXX` sequences and
  collapses `"source"` from nbformat's list-of-lines into a single string — which buries a one-line
  change in a whole-file diff. Instead each notebook was re-serialised with the exact `json.dumps`
  parameters that reproduce its own current bytes (three variants are in use across this repo:
  `indent=1` with and without a trailing newline, and `indent=1, ensure_ascii=True` for the three
  notebooks holding emoji and accented characters). The resulting diff contains only the added `id`
  lines. Verified semantically as well: 52 of 62 notebooks are cell-for-cell identical to HEAD, and
  the other 10 differ only in the H1 line that the retitle above changed.

## Part I — still open after 2026-09-15

- ~~CLAUDE.md's exercises convention no longer matches Part I~~ — **resolved 2026-09-15 at your
  instruction.** The "one long exercise on a real dataset ... **no solution**" rule is gone.
  CLAUDE.md's "Structure of a subchapter" now states that every exercise has a worked solution in a
  separate solutions notebook, that the two notebooks carry identical exercise headings in
  identical order, and that no solution may hide inside a cell labelled as pre-supplied setup.
  `/check-coverage` step 8 updated to match, and a new step 9 checks the solutions notebook.
- **`enumerate` is taught in 1.2 and exercised nowhere.** The old warm-up that covered it looped
  over a list of colour names; there was nothing there worth restoring, so the gap is still open
  and wants a purpose-built short exercise rather than a port.
- **`PairGrid` and `violinplot` are exercised in 1.8 Exercise 12 but taught nowhere.** Handled for
  now with a "Beyond this subchapter" box, the same device 1.5 and 1.6 use. If 1.8's lecture is
  ever extended, these two are the obvious additions.
- **The Argo dive-cycle figure is credited "© Thomas Haessig"** on Euro-Argo's own outreach page —
  an all-rights-reserved credit, not an open licence. Added at your explicit instruction with full
  attribution and a link. Permission has not been sought. Worth settling before the book is
  published, or worth redrawing locally the way `_static/make_numpy_diagrams.py` does for 1.3.
- **`data/part-I/marathon-data.csv` is not pushed yet**, so 1.8 Exercise 12's `pooch` URL 404s
  until it is — the usual first-addition state for a dataset here. The solution was verified
  against the local copy.

## Part III — open from this session

- **5.3 (Physically-Informed Climate Modeling) — not started.** Blocked on a sizing decision for
  two climate-simulation files (`P4K`/`M4K` reduced NetCDFs, 1.82 GB each, ~3.64 GB total) —
  deferred at your request ("I'll come back to it"). Options on the table were: subset to ~2% or
  ~10% of samples, or split and commit the full files as-is (~92 chunk files). Nothing in `data/`
  or `part-III/` yet for this subchapter.
- **8.3 (Neural Weather Prediction / neural-lam) — not started.** Deferred at your request
  ("skip it for now"). Wraps an external repo ([`mllam/neural-lam`](https://github.com/mllam/neural-lam)),
  needs Google Drive + pinned old torch/CUDA versions, and a dead SharePoint dataset link. Needs a
  decision on approach (conceptual walkthrough vs. full port vs. permanent skip) before starting.
- **[7.4](../part-III/7.4-hydrological-modeling-exercises.ipynb), cell 24** — still missing the
  "get it?" scales-pun image (a StandardScaler joke from the original course material). This is
  now the only missing image anywhere in the completed 5.x/6.x/7.x/8.x subchapters.

## Part IV — open from this session

- **Chapter 10, latent-diffusion downscaling notebook — skipped, not ported.** The live reference
  site lists a third chapter-10 notebook ("Learning to downscale coarse climate fields using
  Latent Diffusion," `ldm_env_notebook_empty.ipynb`) that isn't in the reference repo's own
  `_toc.yml` on `main`. Its first cells mount the original instructor's personal Google Drive and
  read a `requirements.txt` from their own local VSCode setup — not reproducible outside that one
  person's environment, likely why it was dropped from the TOC. Skipped at your request. 10.1's
  own title ("...Stochastic Downscaling") still references this material even though no notebook
  covers it. If this is ever revisited, it would need a rework replacing the personal Drive/VSCode
  dependency with this book's usual pooch-based data fetch.
- **[11.2](../part-IV/11.2-hybrid-glacier-modeling-exercises.ipynb), CNN training-data cell** —
  raises `NotImplementedError` by design. Its source dataset (`ex.nc`, ~1.16 GB, glacier
  simulation states) is far over this book's 50 MB auto-commit ceiling; deferred at your request.
  Needs a sizing decision (subset to the 6 variables the exercise actually uses + fewer timesteps,
  full commit with explicit go-ahead, or git-lfs) before it can be wired up the way
  [`bedrock.nc`](../data/part-IV/bedrock.nc) already is a few cells earlier in the same notebook.
- **[10.3](../part-IV/10.3-autoencoders-gans-diffusion-exercises.ipynb) — gaps found cross-checking against the new Géron PyTorch edition's chapter 18** (*Autoencoders, GANs, and Diffusion
  Models*, book pp. 695–740). None of these are bugs — the core math (VAE reparameterization, the
  `/784` latent-loss scaling, the diffusion forward/reverse formulas, the Huber loss choice) matches
  the new edition exactly everywhere it overlaps. These are possible content additions:
  - **Multi-head attention in the diffusion U-Net** (pp. 735) — the new edition's DDPM uses
    attention at several resolution levels; this notebook's `DiffusionModel` has none, since the
    old TF/Keras reference it was ported from explicitly dropped attention as "overkill for
    Fashion MNIST." The most significant of the four gaps.
  - **Sparse autoencoders** (pp. 711–714) — a KL-divergence sparsity-constrained variant, not
    covered at all currently.
  - **Discrete VAEs / VQ-VAE** (pp. 720–724) — Gumbel-softmax categorical latents, the mechanism
    behind models like DALL·E's first stage.
  - **Fast DDIM sampling** (pp. 735–737) — reuses the already-trained `DiffusionModel` unchanged,
    generates in ~50 steps instead of ~4000; purely an inference-time addition, no retraining.

## Pre-existing `%TODO` markers found across the rest of the book

- `README.md:72` — confirm authors, year, and add a DOI (e.g. via Zenodo) for citing the book.
- `README.md:89` — confirm and adjust to the license the project actually wants.
- `README.md:96` — list maintainers and contributors by name.
- `index.md:15` — add a link to previous versions of the book.
- `index.md:56` — check for GitHub restrictions around the contributor workflow.
- `CONTRIBUTING.md:1` — check for errors in the text.
- `CONTRIBUTING.md:2` — add instructions for platforms other than macOS.
- `CONTRIBUTING.md:3` — add a policy for drafts in `drafts/`.
- `part-I/1.2-data-structures-and-control-flow.ipynb` (cell 2, lists section) — "add the rest of
  the methods in the exercises."
- `part-I/1.2-data-structures-and-control-flow.ipynb` (cell 51, AI-critique section) — "improve
  this" on the mutable-default-argument diagnosis.
- ~~`part-I/1.1-environment-and-data-types-exercises.ipynb` (Exercise 8) — `% TODO: link for
  data.` marker~~ — **resolved 2026-09-08.** The marker was stale — the fetch cell right below it
  already had a working `pooch.retrieve` URL and hash — and has been deleted.

## Not included

Fill-in-blank `# TODO: implement this` markers inside exercise code cells (e.g. throughout
[8.2](../part-III/8.2-graph-neural-networks-with-pytorch-exercises.ipynb)) are the exercises
themselves, not authoring gaps — excluded from this list.
