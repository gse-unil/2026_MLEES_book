% TODO: check for errors in the text

# Contributing to the MLEES book

Thanks for helping build *Machine Learning for Earth and Environmental Sciences*. This guide covers everything you need to edit the book: how to set up your environment, how the publishing pipeline works, and the conventions we follow so the book stays consistent and reproducible.

The book is a [Jupyter Book 2](https://jupyterbook.org) project (built on the MyST document engine) hosted at <https://gse-unil.github.io/2026_MLEES_book/>. Source lives in [`gse-unil/2026_MLEES_book`](https://github.com/gse-unil/2026_MLEES_book); the live site is built automatically from `main` by GitHub Actions.

You do not need to be a software engineer to contribute. If you can edit a notebook and use git, you can help.

---

## 1. One-time setup

You need [git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/) (a fast Python environment manager).

**macOS / Linux:**

```bash
# install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# clone the book and enter it
git clone git@github.com:gse-unil/2026_MLEES_book.git
cd 2026_MLEES_book

# create the pinned environment (reads pyproject.toml + uv.lock)
uv sync
```

**Windows (PowerShell):**

```powershell
# install uv if you don't have it
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# clone the book and enter it
git clone git@github.com:gse-unil/2026_MLEES_book.git
cd 2026_MLEES_book

# create the pinned environment (reads pyproject.toml + uv.lock)
uv sync
```

If `git clone` over SSH fails because you haven't set up an SSH key yet, either follow GitHub's
[SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) or clone
over HTTPS instead: `git clone https://github.com/gse-unil/2026_MLEES_book.git`.

`uv sync` installs the exact, version-locked toolchain — everyone works in the same environment, which is what keeps builds reproducible, on every OS. Do not install the book's tools globally with `pip`.

Node.js is **not** required for authoring. The MyST engine underneath is Node-based, so the first time you preview locally it will offer to install Node for you. If you prefer to have it system-wide: `brew install node` on macOS, or download the installer from [nodejs.org](https://nodejs.org) on Windows.

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
- **CI executes every notebook before publishing.** The deploy workflow installs the project's Python environment and runs each notebook, then builds the site from those fresh outputs — not from whatever you last saved locally. Lecture notebooks must run clean: any error there fails the *entire* deploy, not just that page. `*-exercises.ipynb` notebooks are the deliberate exception — their fill-in-the-blank cells (`_____`) are expected to raise, so CI lets those errors happen and strips only the failed cells' output afterward, leaving the blank code visible with no traceback. See §5 for what this means day to day.
- **`main` is the published branch.** Any merge to `main` redeploys the site within a few minutes. Do not push directly to `main`; use a branch and a pull request (§4).

---

## 4. Editing workflow (git)

**New changes shouldn't be pushed straight to `main` — every change, from a typo fix to a new subchapter, should go through a branch and a pull request.** This lets others review and lets CI check the build before anything goes live.

```bash
git checkout main
git pull                                   # start from the latest
git checkout -b part1/add-xarray-section   # descriptive branch name

# ...make your edits, preview locally...

git add -A
git commit -m "Add xarray section to Part I data-loading chapter"
git push -u origin part1/add-xarray-section
```

Then open the pull request itself, either from the command line with the [GitHub CLI](https://cli.github.com/):

```bash
gh pr create --title "Add xarray section to Part I data-loading chapter" --body "What changed and why."
```

or from the browser — GitHub shows a "Compare & pull request" button on the repository page right after you push a new branch; click it, fill in the same title/description, and open the PR against `main`.

Describe what you changed and why. A reviewer will look it over; once approved and merged, the site rebuilds automatically.

Branch-name and commit conventions: prefix branches with the area you're touching (`part1/`, `ml/`, `infra/`, `fix/`); write commit messages in the imperative ("Fix broken link", not "Fixed" or "Fixes").

---

## 5. Working with notebooks

Notebooks are the heart of the book. CI now executes them for you (§3), so committing correct baked-in outputs is no longer what makes the *site* correct. Running a notebook locally before committing is still strongly recommended, though, for three things a green CI run can't cover:

- **A broken lecture notebook fails the whole deploy**, not just its own page. Catching that locally, before you push, is far faster than finding out from a failed GitHub Action.
- **CI only catches crashes, not silently wrong output.** A cell that runs without error but produces a flipped plot or a nonsense number sails straight through. Only looking at it yourself catches that.
- **`*-exercises.ipynb` notebooks are allowed to error on their fill-in-the-blank cells** — CI strips those specific outputs so the page shows clean, unsolved code. It won't tell you whether the *surrounding* code (setup cells, hints, anything before the first blank) still works; that's still on you to check.

In Jupyter: *Kernel → Restart Kernel and Run All Cells*. Confirm every cell runs without error — outside of a fill-in-the-blank exercise cell, where that's expected — and the figures look right, then save.

To sanity-check that a notebook runs cleanly without opening Jupyter — or to scope the check to just what you've changed instead of the whole book — pass it directly to a scoped, executed build:

```bash
uv run myst build --execute part-I/1.5-pandas.ipynb

# or scoped to whatever notebooks you've actually edited:
uv run myst build --execute $(git diff --name-only -- '*.ipynb')
```

This catches execution errors fast, but it renders into `_build/`, not into the notebook itself — it does not replace *Restart Kernel and Run All Cells* for saving fresh outputs into the file you commit. Note it uses plain MyST semantics, not CI's: it has no notion of `*-exercises.ipynb` being allowed to fail, so running it against an exercise notebook will halt (and report failure) at the first blank, same as any other error. That's expected, not a sign something's wrong — the failure just isn't meaningful signal there. To check an exercise notebook exactly the way CI will, run the CI script itself: `uv run python .github/scripts/execute_notebooks.py`.

Practical consequences:

- A lecture notebook that fails halfway now breaks the *entire* deploy — the whole site fails to publish until it's fixed, not just that page. An `*-exercises.ipynb` notebook failing on its intentional blanks is fine and expected; CI strips just that cell's error output.
- Keep cell outputs clean. Clear stray debugging prints and long warning spew before saving. Noisy `stderr` can be suppressed project-wide in `myst.yml` settings, but tidy notebooks are better.
- Set a fixed random seed wherever results would otherwise change run to run, so figures are stable across rebuilds.
- Keep runtimes short. Heavy training does not belong in a notebook that contributors must run; precompute, cache, or load a small representative result instead.

### Adding a Python package

If a notebook you're writing needs a package that isn't already in the environment, add it with
`uv` rather than `pip install`ing it — this keeps `pyproject.toml` and `uv.lock` (and therefore
every other contributor's environment) in sync:

```bash
uv add <package-name>
```

This updates `pyproject.toml`'s dependency list and `uv.lock`'s pinned resolution, and installs
the package into your local environment in one step. Commit both changed files alongside your
notebook changes — a package your notebook imports but that isn't in `pyproject.toml` will work
locally for you and then fail for the next contributor (or in CI) with an unhelpful `ImportError`.

Do not edit `pyproject.toml`'s dependency list by hand and then run `uv sync` — always go through
`uv add` so the lockfile stays consistent with what's declared.

### The `live/` copies: generated, never edited

`live/` holds a copy of every notebook in the book, at the same relative path
(`live/part-I/1.3-numpy.ipynb` for `part-I/1.3-numpy.ipynb`). The Colab and Kaggle badges open
these copies, not the book source. Colab renders neither MyST directives nor `_static/` image
paths, so `tools/make_live.py` converts admonitions to plain markdown, rewrites figures to raw
GitHub URLs, strips outputs, and adds a setup cell that installs what a hosted runtime lacks.

Every file in `live/` is overwritten the next time the script runs. An edit made there directly
is erased without warning, and until then students opening the badge see a notebook that no
longer matches the book. So:

- **Edit the source notebook in `part-*/` or `appendix/`, then regenerate:**

  ```bash
  python3 tools/make_live.py part-I/1.3-numpy.ipynb   # or no argument to regenerate all
  ```

  Commit the regenerated `live/` file together with the source change. Colab and Kaggle fetch
  `live/` from GitHub, so a copy that was not pushed shows the old version, or a 404 for a new
  notebook.
- **Do not save back to GitHub from Colab.** When you open a badge, Colab's *File → Save a copy
  in GitHub* commits straight into `live/`. Even with no content change, Colab reorders the
  notebook's JSON and adds its own metadata, so `python3 tools/make_live.py --check` then reports
  the copy as stale. Use *File → Save a copy in Drive* for your own experiments. If you fixed
  something while working in Colab, make the same change in the source notebook and regenerate.
- **If a `live/` file was edited by mistake,** check whether the edit contains a real change
  (compare cell sources, not the raw JSON diff, which Colab's reformatting inflates). Move
  anything worth keeping into the source notebook, then regenerate to restore the copy.

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

### Sharing a draft before it's ready

Want feedback on a notebook before it's polished enough to register as a real page above? Put it
in `drafts/` at the repository root instead. `myst.yml` excludes `drafts/**` from the build
entirely, so a draft notebook doesn't need a `toc` entry, doesn't need to run clean, and can't
break the published site no matter what state it's in.

```bash
git checkout -b part1/draft-new-topic
mkdir -p drafts
cp your-notebook.ipynb drafts/
git add drafts/your-notebook.ipynb
git commit -m "Add draft: new topic for review"
git push -u origin part1/draft-new-topic
```

Open a pull request the same way as any other change (§4), and say in the description that it's a
draft, not a finished page — that tells reviewers to comment on direction and content rather than
check it against the pre-PR checklist in §9. Once it's ready to actually publish, move it out of
`drafts/` into the right `part-*/` directory, register it in `myst.yml`'s `toc` as above, and make
sure it runs clean before committing (§5) — from there it's a normal page going through normal
review.

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
- [ ] `live/` was regenerated with `tools/make_live.py`, not hand-edited, and `python3 tools/make_live.py --check` passes (§5).
- [ ] Any dataset you added is a verified, hash-pinned snapshot in `data/<part>/`, fetched via `pooch` (§7) — not a bare third-party URL, and not committed unprompted if over 50 MB.
- [ ] No `_build/`, no stray checkpoints, no notebook-generated output (`_files/`) are staged (`git status` is clean of these).
- [ ] New pages are added to the `toc` in `myst.yml`.
- [ ] New citations are in `references.bib` with a DOI/URL.
- [ ] Links and badges resolve (CI runs a link check; you can run `uv run jupyter book build --check-links --strict` locally).

---

## 10. Getting help

Open an issue on the repository for anything unclear, broken, or worth discussing before you start a larger change. For substantial restructuring, open an issue first so we can agree on the approach before you invest the effort.

Welcome aboard, and thank you for contributing.