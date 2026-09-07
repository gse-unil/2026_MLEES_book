# Comparison: Bonus A Reproducible Data Pipelines

No old counterpart, so there's no old-book spine to build a table from — none of the old book's 16
subchapters teach fetching, caching, or verifying a dataset before using it. This subchapter
(`bonus-a-reproducible-data-pipelines.ipynb`) is entirely new material.

## What's here (all new, no old-book mapping)

| Section | Contains |
|---|---|
| A tour of formats | CSV vs. parquet vs. netCDF vs. zarr vs. GeoTIFF, matched to data shape/scale; live comparison of CSV/parquet file size and dtype retention; netCDF file vs. zarr directory store |
| Fetching data over HTTP | `requests.get`, `raise_for_status`, writing bytes — shown, not run |
| pooch: download once, verify always | `pooch.retrieve(url, known_hash=..., path=...)` — shown, not run (book builds offline) |
| The idempotent fetch: cache, hash, skip | a real, executed cache→hash→skip function using `pooch.file_hash` on a local stand-in file; computational-thinking box: pin your inputs; quick exercise: one-line integrity check |
| When generated code lies: trusting a file that is merely present | an existence-only check silently returns a truncated, stale cached file |
| Going deeper | multi-file registries (`pooch.create`); DOI-versioned data (Zenodo/figshare); intake catalogs; provenance and FAIR |
| Takeaways / Resources | — |

Exercises: 6 short exercises (CSV vs. parquet, netCDF vs. zarr, hashing for integrity, an
idempotent fetch, fix the existence-only check, a real `pooch.retrieve` call), each blank with a
matching worked solution in a separate `bonus-a-reproducible-data-pipelines-solutions.ipynb`.

## Why this subchapter exists

The old book never taught students to fetch, cache, or verify a dataset before using it — students
always started from a file already sitting in the working directory. This fills that gap. The
"existence is not integrity" AI-critique (an existence-only file check silently returning
corrupted/stale data) is, like every AI-critique in this book, a device with no old-book
equivalent anywhere.

This is one of the two subchapters held back from live teaching (per the course plan) — genuinely
new, valuable material, and the right kind of content to hold back precisely because it's an
addition, not a replacement for something the syllabus already promised.
