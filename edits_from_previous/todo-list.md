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
- **New, found during the 2026-09-08 fix pass:** [Bonus A](../part-I/bonus-a-reproducible-data-pipelines.ipynb)
  cell `ff96d4b8` (CSV vs. parquet size comparison) has a committed `ImportError` traceback for a
  missing pyarrow dependency — a genuinely broken output that slipped past the earlier pre-launch
  review. `pyarrow` has since been added as a proper `uv`-managed dependency
  (`pyarrow>=25.0.1` in `pyproject.toml`), but running the cell now raises a separate
  `ArrowKeyError: A type extension with name pandas.period already defined` — this looks like an
  environment/kernel issue (a `pandas`/`pyarrow` double-registration problem), not a bug in the
  cell's own code, which is ordinary `df.to_parquet(...)` usage. Needs a clean-kernel re-run to
  confirm; if it persists on a genuinely fresh kernel, may need a different `pyarrow` version
  pinned against `pandas 3.0.5`.
- **New, found during the 2026-09-08 fix pass:** [1.8](../part-I/1.8-statistical-foundations-and-ml-solutions.ipynb)
  Exercise 7's overfitting demo needed a *second* fix beyond the km-rescaling already applied —
  rescaling alone produced train R²=0.962/test R²=0.94 (confirmed by running it), not overfitting,
  because the real cause was training-set size (42 points) relative to the polynomial's 9
  parameters, not numerical conditioning. Refit on only the first 12 rows of the training set
  instead, matching the lecture's own near-saturated ratio — reasoned by analogy to the lecture's
  working demo, not yet verified by execution. Needs a re-run to confirm the gap is actually large
  this time.
- **New, found during the 2026-09-08 fix pass:** [1.5](../part-I/1.5-pandas.ipynb) — a discrepancy
  surfaced between two review passes: cells `8a6e288b`, `3eabc0f4`, `30861396` were originally
  reported as having zero committed output, but on a later pass all three already had output in
  the file. Not re-investigated further; worth a quick glance to confirm the current output is
  genuinely current and not stale.

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
