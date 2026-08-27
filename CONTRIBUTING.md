% TODO: check for errors in the text
% TODO: add different platforms not only MacOS
% TODO: add policy for drafts in drafts/

# Contributing to the MLEES book

Thanks for helping build *Machine Learning for Earth and Environmental Sciences*. This guide covers everything you need to edit the book: how to set up your environment, how the publishing pipeline works, and the conventions we follow so the book stays consistent and reproducible.

The book is a [Jupyter Book 2](https://jupyterbook.org) project (built on the MyST document engine) hosted at <https://gse-unil.github.io/2026_MLEES_book/>. Source lives in [`gse-unil/2026_MLEES_book`](https://github.com/gse-unil/2026_MLEES_book); the live site is built automatically from `main` by GitHub Actions.

You do not need to be a software engineer to contribute. If you can edit a notebook and use git, you can help.

---

## 1. One-time setup

You need [git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/) (a fast Python environment manager). On macOS:

```bash
# install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# clone the book and enter it
git clone git@github.com:gse-unil/2026_MLEES_book.git
cd 2026_MLEES_book

# create the pinned environment (reads pyproject.toml + uv.lock)
uv sync
```

`uv sync` installs the exact, version-locked toolchain — everyone works in the same environment, which is what keeps builds reproducible. Do not install the book's tools globally with `pip`.

Node.js is **not** required for authoring. The MyST engine underneath is Node-based, so the first time you preview locally it will offer to install Node for you. If you prefer to have it system-wide, `brew install node` once.

---

## 2. Preview the book locally

While editing, run a live local server rather than waiting on CI:

```bash
uv run jupyter book start
```

This serves the book at a local URL and reloads as you save. Use it constantly — it is far faster than pushing and watching the GitHub Action.

To reproduce exactly what CI does (a static HTML build):

```bash
uv run jupyter book build --html
```

---

## 3. How the pipeline works (read this once)

Understanding the build model prevents the most common mistakes.

- **Source in, site out.** The repository contains only source: notebooks, markdown, `myst.yml`, and `references.bib`. The built website is generated fresh by CI on every push to `main`. **Never commit the `_build/` directory** — it is git-ignored for a reason.
- **CI does not run your notebooks.** The deploy workflow installs only Node and the MyST engine. It renders the outputs **already saved inside your `.ipynb` files** and does not execute them. This is deliberate: a notebook that errors cannot publish a traceback to the live site. The corollary is critical — *the quality of the published outputs is entirely your responsibility, set when you run the notebook locally before committing* (see §5).
- **`main` is the published branch.** Any merge to `main` redeploys the site within a few minutes. Do not push directly to `main`; use a branch and a pull request (§4).

---

## 4. Editing workflow (git)

Always work on a branch and open a pull request. This lets others review and lets CI check the build before anything goes live.

```bash
git checkout main
git pull                                   # start from the latest
git checkout -b part1/add-xarray-section   # descriptive branch name

# ...make your edits, preview locally...

git add -A
git commit -m "Add xarray section to Part I data-loading chapter"
git push -u origin part1/add-xarray-section
```

Then open a pull request against `main` on GitHub. Describe what you changed and why. A reviewer will look it over; once approved and merged, the site rebuilds automatically.

Branch-name and commit conventions: prefix branches with the area you're touching (`part1/`, `ml/`, `infra/`, `fix/`); write commit messages in the imperative ("Fix broken link", not "Fixed" or "Fixes").

---

## 5. Working with notebooks

Notebooks are the heart of the book, and they have one golden rule that follows directly from §3:

**Before committing a notebook, restart and run it top to bottom, then commit it *with* its outputs.**

In Jupyter: *Kernel → Restart Kernel and Run All Cells*. Confirm every cell runs without error and the figures look right. Save. The outputs you see locally are exactly what readers will see, because CI does not re-run anything.

Practical consequences:

- A notebook that fails halfway will not break the build — it will silently publish broken or missing outputs. Catching that is on you, locally.
- Keep cell outputs clean. Clear stray debugging prints and long warning spew before saving. Noisy `stderr` can be suppressed project-wide in `myst.yml` settings, but tidy notebooks are better.
- Set a fixed random seed wherever results would otherwise change run to run, so figures are stable across rebuilds.
- Keep runtimes short. Heavy training does not belong in a notebook that contributors must run; precompute, cache, or load a small representative result instead.

---

## 6. Adding or moving a page

The book's structure lives in the `toc` block of `myst.yml`, not in the folder layout. To add a page, create the file, then register it:

```yaml
project:
  toc:
    - file: index.md
    - file: part-I/part-I.md
      children:
        - file: part-I/ch-1-intro.md
          children:
            - file: part-I/1.1-environment-and-data-types.ipynb
            - file: part-I/1.2-data-structures-and-control-flow.ipynb
            - file: part-I/1.3-numpy.ipynb   # <- your new page
```

Filenames follow a `{chapter}.{subchapter}-slug.ipynb` prefix (`1.1-`, `2.3-`, ...), matching the
subchapter's own number, with `-exercises`/`-solutions` suffixes for the paired notebooks.
**Do not hand-write Colab badges or internal links against raw file paths** — they break when
files move or are renamed. Construct links from the page slug, or use the project-level badge
mechanism so a rename can't orphan them. (Hand-written badges pointing at the wrong path were a
recurring failure in the previous edition; we are avoiding that by construction.)

---

## 7. Data handling

**Datasets are committed to the repository, then fetched through `pooch`.** This is the opposite
of "keep data out of git": every real dataset a notebook depends on — a CSV, a pickle, a small
netCDF, a zipped bundle of `.npy` arrays — gets a verified snapshot committed to `data/<part>/`
(one subfolder per part, e.g. `data/part-I/`, `data/part-II/`), then the notebook fetches *that*
copy at runtime with [`pooch`](https://www.fatiando.org/pooch/):

```python
import pooch

path = pooch.retrieve(
    url="https://raw.githubusercontent.com/gse-unil/2026_MLEES_book/main/data/part-II/your_file.csv",
    known_hash="sha256:...",
    fname="your_file.csv",
    path=pooch.os_cache("mlees"),
)
```

This holds regardless of file size, down to a 15 KB CSV — "small enough to just leave inline" is
never the right call. The point is a snapshot under this repo's own control, not a bare
third-party URL: those move, expire, or (a recurring trap) turn out to sit behind a login —
a SharePoint/OneDrive personal-share link can return HTTP 200 with an HTML sign-in page as the
body, so verify a fetched file by its actual content (row counts, a shape or value the notebook
itself asserts), not by status code alone. Never invent a hash or leave a placeholder — if a
source is inaccessible, say so and ask for the file rather than guessing a replacement.

**Exception: datasets larger than 50 MB.** Stop before committing and flag it instead — the file,
its size, and how you'd like to proceed (a smaller/subsetted cut, git-lfs, cloud-native reads
against an existing public zarr/COG store for reanalysis-scale gridded fields, or an explicit
go-ahead to commit it as-is). The repository has no git-lfs configured today; treat committing
anything near or above that threshold as a judgment call, not a default.

- Avoid `files.upload()` and Google Drive mounts in notebooks; they are not reproducible for a
  reader who isn't you.

---

## 8. Writing and code conventions

These keep the book coherent across many authors.

**Audience.** Part I (scientific Python) must remain accessible to readers with no programming background, while offering optional depth for stronger students. Keep the core path simple and linear; put advanced material in clearly marked, collapsible asides rather than inflating the main thread.

**Prose style.** Write clear, plain explanations. Apply scientific lowercasing: do not capitalize technical terms, methods, or fields unless they begin a sentence or are proper nouns or eponyms — so "machine learning", "convolutional neural network", "backpropagation", "convection", but "Python", "Gaussian", "Navier–Stokes". Avoid emphasis capitalization.

**Units and notation.** Use SI units. Keep mathematical notation consistent with the field and preserve case-specific meaning of symbols. Label equations, figures, and tables so they can be cross-referenced with MyST's `[](#label)` syntax.

**Code.** Python is the language of the book; deep-learning content uses **PyTorch** (the book is migrating off Keras/TensorFlow — new contributions should be PyTorch). Write minimal, readable code with concise comments. Follow standard style (PEP 8); a formatter such as `ruff` is recommended.

**Static assets vs. generated output.** Each part keeps two separate local folders, both named consistently across `part-I/`, `part-II/`, etc.: images and other assets you author or source yourself (figures, diagrams, downloaded reference images) go in that part's `_static/`, referenced with a relative path or a `{figure}` directive; anything a notebook writes when it runs (saved plots, cached intermediate files) goes in that part's `_files/`, which is git-ignored — never commit generated output.

**Citations.** Only cite work that genuinely exists, and verify the title, authors, year, and DOI before adding it. Put references in `references.bib` and cite inline with `[@key]`; MyST builds the bibliography automatically. Every reference should carry a DOI or a stable URL. When unsure a citation is correct, leave it out and flag the gap rather than guessing.

---

## 9. Before you open a pull request

A short checklist:

- [ ] The book builds locally: `uv run jupyter book build --html` succeeds.
- [ ] Any notebook you touched runs clean from a restarted kernel, and is committed with its outputs.
- [ ] Any dataset you added is a verified, hash-pinned snapshot in `data/<part>/`, fetched via `pooch` (§7) — not a bare third-party URL, and not committed unprompted if over 50 MB.
- [ ] No `_build/`, no stray checkpoints, no notebook-generated output (`_files/`) are staged (`git status` is clean of these).
- [ ] New pages are added to the `toc` in `myst.yml`.
- [ ] New citations are in `references.bib` with a DOI/URL.
- [ ] Links and badges resolve (CI runs a link check; you can run `uv run jupyter book build --check-links --strict` locally).

---

## 10. Getting help

Open an issue on the repository for anything unclear, broken, or worth discussing before you start a larger change. For substantial restructuring, open an issue first so we can agree on the approach before you invest the effort.

Welcome aboard, and thank you for contributing.