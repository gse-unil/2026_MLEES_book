# Comparison: Bonus A Reproducible Code and Data Pipelines

**Scope note (post-dates the rest of this file):** this subchapter later absorbed a second,
earlier half. The packaging/uv content below (`uv init --lib`, the `src` layout, `uv.lock`, and
the four going-deeper boxes on Ruff/static typing/pre-commit-CI/semver) moved in from the former
"Bonus B" subchapter when packaging was split out of what's now 1.7 — see
`ch1-comparison-bonus-b.md`. Bonus A was retitled "Reproducible Code and Data Pipelines"
accordingly, and is now the *only* held-back bonus subchapter — the "two subchapters held back"
framing below is stale; there is just this one. The data-pipelines content (formats through
Resources) is unchanged from what this file originally described.

No old counterpart, so there's no old-book spine to build a table from — none of the old book's 16
subchapters teach fetching, caching, or verifying a dataset before using it, or packaging a
notebook's worth of code into an installable project. This subchapter
(`bonus-a-reproducible-data-pipelines.ipynb`) is entirely new material.

## What's here (all new, no old-book mapping)

| Section | Contains |
|---|---|
| Packaging with uv: The src Layout | `uv init --lib`, the `src/` layout, `pyproject.toml`, `uv.lock`; going deeper: Ruff (lint/format), static type checking (mypy/ty), pre-commit and CI, semantic versioning and coverage |
| From reproducible code to reproducible data | transition paragraph between the two halves |
| A tour of formats | CSV vs. parquet vs. netCDF vs. zarr vs. GeoTIFF, matched to data shape/scale; live comparison of CSV/parquet file size and dtype retention; netCDF file vs. zarr directory store |
| Fetching data over HTTP | `requests.get`, `raise_for_status`, writing bytes — shown, not run |
| pooch: download once, verify always | `pooch.retrieve(url, known_hash=..., path=...)` — shown, not run (book builds offline) |
| The idempotent fetch: cache, hash, skip | a real, executed cache→hash→skip function using `pooch.file_hash` on a local stand-in file; computational-thinking box: pin your inputs; quick exercise: one-line integrity check |
| When generated code lies: trusting a file that is merely present | an existence-only check silently returns a truncated, stale cached file |
| Going deeper | multi-file registries (`pooch.create`); DOI-versioned data (Zenodo/figshare); intake catalogs; provenance and FAIR |
| Takeaways / Resources | — |

Exercises: 6 short exercises (CSV vs. parquet, netCDF vs. zarr, hashing for integrity, an
idempotent fetch, fix the existence-only check, a real `pooch.retrieve` call), each blank with a
matching worked solution in a separate `bonus-a-reproducible-data-pipelines-solutions.ipynb`. All
six are from the data-pipelines half — none exercise the packaging/uv half that later moved in
(flagged in `todo-list.md`; left as-is since packaging is CLI/project-scaffolding work, awkward to
exercise "from scratch in an empty code cell").

## Why this subchapter exists

The old book never taught students to fetch, cache, or verify a dataset before using it — students
always started from a file already sitting in the working directory. This fills that gap. The
"existence is not integrity" AI-critique (an existence-only file check silently returning
corrupted/stale data) is, like every AI-critique in this book, a device with no old-book
equivalent anywhere.

This is the one subchapter held back from live teaching as optional self-study material (see the
scope note at the top — it absorbed a second held-back subchapter's packaging content rather than
the two staying separate) — genuinely new, valuable material, and the right kind of content to
hold back precisely because it's an addition, not a replacement for something the syllabus
already promised.
