# Merging Shivanshi's LDM downscaling notebook into main

Working notes, not published content. Source: branch `ldm_notebook_branch`, file
`part-IV/10.4-ldm_downscaling_exercise.ipynb` (93 cells, 32 code, 1.7 MB), plus
`part-IV/data_and_helpers/data_LDM/{preprocessing.py,stats.json,requirements.txt}` and 11
`__MACOSX/` resource-fork stubs. The branch is well behind main (it still has `S1_3_ex_*.npy`
under their old names and predates the Advertising/argo data), so this wants a cherry-pick of the
part-IV files, not a branch merge.

## 1. The data URL — resolved

**Working link** (confirmed 2026-09-14):

```
https://unils-my.sharepoint.com/:u:/g/personal/tom_beucler_unil_ch/IQA4OoCmFuOJQJ0JT8OTIK83AYTSStTOTO0bWDlnIVoQakE?e=oo1bkB&download=1
```

Fetched with `requests` — the library pooch itself uses — from this machine with no Microsoft
session: `200`, `content-type: application/x-zip-compressed`,
`content-disposition: attachment; filename="data_LDM.zip"`, `content-length: 2 083 870 133`
(1.94 GiB), first bytes `PK\x03\x04`, and the first entries are `data_LDM/`,
`__MACOSX/._data_LDM`, `data_LDM/.DS_Store` — so the archive does hold a single top-level
`data_LDM/` folder, which is what the `data_dir` handling in §2 relies on.

**A quirk worth recording, because it will mislead whoever tests this next.** A bare
`curl -L "<link>&download=1"` returns `403 FORBIDDEN` on this same working link. The share link
sets a cookie partway through its redirect chain, and curl drops it unless given a cookie jar
(`-c`/`-b`); `requests` carries cookies across redirects inside a single call, so pooch is
unaffected. To test a SharePoint link the way pooch will see it, use requests, not curl:

```python
import requests
with requests.get(URL, stream=True, allow_redirects=True, timeout=120) as r:
    print(r.status_code, r.headers.get("content-type"), r.headers.get("content-length"))
    print(next(r.iter_content(8192))[:4])     # b"PK\x03\x04" for a zip
```

Two earlier links did **not** work, and the distinction matters when this link eventually expires:

| Link | Result |
|---|---|
| folder-view URL (`/shared?listurl=…&id=…data_LDM.zip`), with and without `&download=1`, and the `download.aspx?SourceUrl=…` form | `403` → `authenticate.aspx` |
| the link currently in the notebook (`shivanshi_asthana_unil_ch/IQBv7NF_roh…?e=uJ6Aha&download=1`) | `403` |
| first "anyone with the link" attempt (`…IQA4OoCmFuOJ…?e=IUS1mf`) | redirects through `Authenticate.aspx` → `_forms/default.aspx` → `login.microsoftonline.com`, returning 25 KB of Microsoft sign-in HTML |

The failing anonymous-looking link ended at the tenant login page; the working one resolves
straight to `…/Documents/ML_Env_Sci/data_LDM.zip`. So the sharing scope, not the URL shape, is
what decides it.

**Risks to plan for.** The `?e=` token can be rotated or revoked, and the link has no expiry
guarantee. When it dies, SharePoint answers with an HTML sign-in page rather than an error — and
the notebook's current downloader would save that HTML as `data_LDM.zip` and then, thanks to its
`if not os.path.exists(zip_path)` guard, treat it as valid on every later run. The pinned
`known_hash` in §2 is what turns that silent corruption into a loud failure. If the link proves
fragile in teaching, **Zenodo** is the durable alternative: free, 50 GB per record, DOI, direct
download, and it makes the data citable next to the Tomasi et al. paper the exercise is built on.

**Size.** 2 083 870 133 bytes (1.941 GiB), streamed end to end and hashed on 2026-09-14: `sha256:507046ce08b28ba3853d0b65a82edb50588a9060bd5eaa40fa330975f750b309`. The byte count matched the advertised `content-length` exactly, so the link serves the whole archive, not a truncated one. The data stays remote regardless — CLAUDE.md stops at 50 MB and the repo
has no git-lfs. Worth checking whether it needs to be that big: the notebook reports
`Using 24 of 48 files from 2020`, so if the bulk is a full year of frames, shipping only the
frames the exercise touches plus the three checkpoint sets could shrink it a great deal.

**The archive carries macOS junk** — `__MACOSX/` and `.DS_Store` entries are inside the zip, and
will be extracted onto every reader's disk. Harmless, but worth rebuilding the zip without them
if it is being re-uploaded anyway (`zip -rX data_LDM.zip data_LDM -x '*.DS_Store'`).

## 2. The pooch cell

Drop-in replacement for cells 2 to 13 of the notebook (eight cells become one). It keeps the
`data_dir` variable, with the same meaning, so every downstream cell — `sys.path.append(
f"{data_dir}/data_LDM")`, `get_file_list(...)`, the checkpoint paths in the YAML config — works
unchanged. The URL and hash below are the verified ones from section 1.

```python
# Pre-supplied: download and unpack the data and pretrained checkpoints (1.94 GiB).
# The download runs once; pooch reuses the cached copy on every later run.
import os
import sys
import pooch

DATA_URL = (
    "https://unils-my.sharepoint.com/:u:/g/personal/tom_beucler_unil_ch/"
    "IQA4OoCmFuOJQJ0JT8OTIK83AYTSStTOTO0bWDlnIVoQakE?e=oo1bkB&download=1"
)
DATA_HASH = "sha256:507046ce08b28ba3853d0b65a82edb50588a9060bd5eaa40fa330975f750b309"
EXTRACT_DIR = "data_LDM_unzipped"

files = pooch.retrieve(
    url=DATA_URL,
    known_hash=DATA_HASH,
    fname="data_LDM.zip",
    path=pooch.os_cache("mlees"),
    processor=pooch.Unzip(extract_dir=EXTRACT_DIR),
)

# The archive holds one top-level data_LDM/ folder, so data_dir is the directory that
# contains it -- the same meaning the variable had before, so later cells are unchanged.
data_dir = os.path.join(pooch.os_cache("mlees"), EXTRACT_DIR)
if not os.path.isdir(os.path.join(data_dir, "data_LDM")):
    raise FileNotFoundError(
        f"expected a data_LDM/ folder inside {data_dir}; the archive layout has changed"
    )

print("data ready at:", data_dir)
print(sorted(n for n in os.listdir(os.path.join(data_dir, "data_LDM"))
             if not n.startswith(".")))
```

What this fixes beyond the URL:

- **The notebook never unzips anything.** `extractall` appears nowhere in all 93 cells; cell 12
  is a bare `print(f"Data extracted to: {data_dir}")` and `zipfile` is imported but never used.
  The committed outputs hide this — they were produced on a machine where the folder was already
  unpacked by hand. `pooch.Unzip` does it and verifies it.
- **No integrity check.** The current hand-rolled `requests` loop writes whatever comes back,
  including an HTML error page, and the `if not os.path.exists(zip_path)` guard then treats that
  file as valid on every later run. This is exactly the existence-vs-integrity bug Bonus A is
  built around. `known_hash` catches it.
- **Data written into the repo tree.** `download_choice="permanent"` sets
  `data_dir = "data_and_helpers/"`, a relative path, so a 2 GB download lands inside `part-IV/`
  next to the notebook and is not gitignored. `pooch.os_cache("mlees")` puts it where every other
  dataset in the book goes.
- Drops `download_choice`, the progress-percentage loop, and the `! ls` shell escape (cell 13),
  which assumes a Unix shell.

## 3. The rest of the merge checklist

**Blockers — the notebook is wrong or will not run without these**

| # | Issue | Fix |
|---|---|---|
| B1 | Data URL 403s; no hash; 2 GB (§1) | Anonymous link or Zenodo deposit, then fill in §2 |
| B2 | Nothing ever unzips the archive | §2 |
| B3 | Cell 78 (the training run) carries a committed `KeyboardInterrupt` traceback | Re-run to completion, or clear outputs |
| B4 | Not wired into `myst.yml` | Add under chapter 10 with the other part-IV files |
| B5 | Dependencies — see §4. `requirements.txt` is both over- and under-specified | Install the six packages actually imported; drop the pins |
| B8 | **`preprocessing.py` hardcodes a Colab path**: `DATA_DIR = "/content/drive/MyDrive/data_LDM/"`, never overridden by the notebook. Outside Colab `get_file_list()` globs nothing and returns an empty list, printing `Using 0 of 0 files from 2020.` — it does not raise | Repoint the module after importing it (two lines, see §4), or better, give `get_file_list` a directory argument |
| B9 | `properscoring` is imported in cell 16 (`from properscoring import crps_ensemble`, used for the Q8 CRPS scoring) but is **not in `requirements.txt`** | Add it |
| B6 | 11 `__MACOSX/` resource-fork files committed under `part-IV/data_and_helpers/` | Delete |
| B7 | Two copies of `preprocessing.py`/`stats.json`: one committed at `part-IV/data_and_helpers/data_LDM/`, one inside the downloaded zip, and `sys.path` points at the downloaded one | Pick one. Committing them (they are 5.6 KB and 861 B) and importing from the repo is the more reproducible half |

**Conventions — needed to match the rest of the book**

| # | Issue | Fix |
|---|---|---|
| C1 | Filename `10.4-ldm_downscaling_exercise.ipynb` uses an underscore and a singular suffix | `10.4-ldm-downscaling-exercises.ipynb` |
| C2 | Three `# @title` Colab cell markers | Remove |
| C3 | Five base64-embedded images (4 png, 1 webp) inflate the file to 1.7 MB | Move to `part-IV/_static/`, reference with `{figure}` directives, with alt text and credits |
| C4 | **Image licensing unchecked.** One is figure 1 of Tomasi et al. 2025 (GMD, `gmd-18-2051-2025-f01`), one is a medium.com `.webp`, one a MIT vision-book screenshot, one an untitled `images.png`, one a personal screenshot | GMD is CC-BY so it is reusable with attribution; the medium.com and screenshot images need a source or a replacement. Same call made in 1.8 last week: two unlicensed images were dropped rather than reused |
| C5 | Question numbering runs Q1, Q2, Q3, Q4, **Q5**, Q5.1, **Q5**, Q6, Q7, Q7b, Q8 — two different sections are both "Q5", and there is a "Q7b" | Renumber Q1–Q10 |
| C6 | `###About the paper`, `###Q5.`, `###Q5.1.` — no space after the hashes, so MyST will not treat them as headings | Add the space |
| C7 | One emoji (`🇰`, in "you will learn 🇰 1.") — likely a mangled character; the book bans emoji | Remove |
| C8 | Learning objectives are a plain `### Learning objectives :` heading | Convert to the `tip` admonition the palette specifies |
| C9 | Colab-style fill-in-the-blank cells (`class VAE(__________)`, 18 of them) | **Decide.** Part I uses prompt → empty cell → solution; ported chapters keep their own shape. Given "keep it close to the original", leaving the blanks is defensible — but then there is no solutions notebook, and no other part-IV exercise works this way |
| C10 | Headings and prose use `Pytorch`, `Pytorch Lightning`, `Unet` | `pytorch`, `pytorch lightning`, `UNet` — scientific lowercasing, consistently |
| C11 | Committed outputs carry absolute Colab paths (`/usr/local/lib/python3.12/dist-packages/...`) | Clears itself when B3 is re-run in this environment |
| C12 | No `## Resources` section and no takeaways box | Add, matching the other part-IV chapters |

**Open questions for the author**

- The notebook needs a GPU ("Make sure to run this on a GPU!!!") and trains a hierarchy of three
  models. What is the intended runtime, and is the expectation that readers run the training at
  all or only the inference from the shipped checkpoints? That decides whether B3 is a re-run or
  a restructure.
- `download_choice` offered a 2 GB permanent copy next to the notebook. Is there a reason readers
  would want that rather than the shared cache?
- Is chapter 10 the right home, and does 10.4 follow 10.3 in the intended reading order?

## 4. Dependencies: what is actually needed

Asked directly — *can this run on the project's own torch and matplotlib?* Probably yes, and the
pins are not the real obstacle. What each requirement is actually worth, checked by grepping every
import in the notebook and in `preprocessing.py`:

**Resolved 2026-09-14: all six added to `pyproject.toml`** with `uv add lightning omegaconf
properscoring zstandard rioxarray rasterio`, resolving to lightning 2.6.6, omegaconf 2.3.1,
properscoring 0.1, zstandard 0.25.0, rioxarray 0.23.0, rasterio 1.5.1 — all unpinned, none of the
versions the old `requirements.txt` asked for. `PyYAML` needed nothing: 6.0.3 was already there
transitively. Verified on the project's own **torch 2.14.0** and **matplotlib 3.11.1**: the whole
stack imports, xarray registers the `rasterio` engine the helper depends on, and a Lightning
checkpoint round-trips through `load_from_checkpoint`. So the answer to "can it run on the torch
in the lock file" is yes — the `torch==2.8.0` and `matplotlib==3.9.1` pins were never needed.

**Pinned `lightning>=2.5.3,<2.6`, and the reason matters.** On lightning 2.6.6 the pretrained
`ldm-epoch=19.ckpt` fails to load with `UnpicklingError`; on 2.5.x, same torch, it loads fine.
Lightning 2.5 passed `weights_only=False` to `torch.load`; 2.6 passes `None` and lets torch's
own 2.6+ default (`True`) apply — and that checkpoint cannot be read under `weights_only=True`,
because `save_hyperparameters()` stored a **live `Conditioner` `nn.Module` instance** and two
`omegaconf.DictConfig` objects in its hyper-parameters rather than plain values. So the constraint
everyone assumed was on torch is really on Lightning.

Two consequences worth acting on:

- The ldm checkpoint can only be unpickled from a context where a class named `Conditioner` exists
  as `__main__.Conditioner`. The notebook satisfies this because cell 64 defines it before cells
  66 and 83 load the checkpoint — but it breaks if that class is renamed, if the cell is moved
  after the load, or if anyone loads the checkpoint from a module or script rather than the
  notebook. Verified both ways: without the class, `AttributeError: Can't get attribute
  'Conditioner'`; with any class of that name defined, it loads and yields 36 tensors.
- **The durable fix is the author's**: pass the conditioner's *config* to `save_hyperparameters()`
  instead of the built module, and plain dicts instead of `DictConfig`. Re-saved that way the
  checkpoints load under any recent Lightning with no pin and no name coupling. Until then the pin
  is what holds.

One wart: `properscoring` is unmaintained (0.1, released 2015) and emits three
`SyntaxWarning: invalid escape sequence` messages from its own docstrings on import. Harmless, but
it will show up in the notebook's output unless filtered.

**Imported, and therefore needed:**

| Package | Used for | Pin worth keeping? |
|---|---|---|
| `lightning` | `LightningModule`, `LightningDataModule`, `Trainer`, `ModelCheckpoint`, and `load_from_checkpoint` for all three pretrained models | unpinned; it is the one to watch against torch 2.14 |
| `omegaconf` | the YAML config object threaded through `train_hierarchy(cfg)` | unpinned |
| `properscoring` | `crps_ensemble`, the whole of Q8 | **missing from `requirements.txt`** |
| `zstandard` | `decompress_zst_pt` — the frames are `.pt.zst` | drop the `==0.23.0`; only `ZstdDecompressor().decompress()` is used |
| `rioxarray` + `rasterio` | registers the `engine="rasterio"` backend for the three static `.tif` files | drop the `==0.15.0`; only `xr.open_dataset(..., engine="rasterio")` is used |
| `PyYAML` | `import yaml` when the config is written out | unpinned |

**In `requirements.txt` but imported nowhere** — `torchvision`, `torchaudio`, `torchmetrics`,
`imageio`, `nest_asyncio`, `pybind11-global`, `hydra-core`, `lightning-utilities`,
`matplotlib-inline`, `typing-inspection`, `typing_extensions`. Dropping `torchvision` and
`torchaudio` matters most: they are the packages that genuinely constrain the torch version, and
removing them removes the only hard reason to stay on torch 2.8.

**On the two pins asked about:**

- `matplotlib==3.9.1` — the notebook only calls `plt.subplots`, `imshow`, `plot` and `colorbar`.
  Nothing there changed between 3.9 and 3.11. The pin looks like a `pip freeze` of whatever Colab
  had, not a requirement.
- `torch==2.8.0` against the project's 2.14 — the one place version drift can actually bite is
  reading the pretrained `.ckpt` files. Two things make that low-risk here: the checkpoints are
  loaded through Lightning's `load_from_checkpoint`, which handles the `weights_only` default that
  changed in torch 2.6, and the data files go through an explicit
  `torch.load(..., weights_only=False)` in `preprocessing.py`. So the honest answer is that it
  will probably work, and it is cheap to find out: install the six packages, run the download
  cell, and load one checkpoint. That test takes minutes and settles it better than any amount of
  reading.

If a checkpoint does refuse to load, the fallback is not to downgrade the whole project — it is to
re-save the checkpoints from the environment that produced them, as plain `state_dict` files,
which are far more portable across versions than full Lightning checkpoints.

**The two lines the pooch cell needs alongside it**, because of B8:

```python
import preprocessing
preprocessing.DATA_DIR = os.path.join(data_dir, "data_LDM") + os.sep
preprocessing.STATIC_DIR = os.path.join(preprocessing.DATA_DIR, "static_vars")
```

`get_file_list()` reads `DATA_DIR` at call time, so reassigning the module attribute is enough and
leaves `preprocessing.py` untouched. Cleaner still would be to give the function an argument, but
that edits the author's file.

Two smaller things in `preprocessing.py` worth a look while it is open: `YEARS = [str(y) for y in
range(2021)]` builds every year from `"0"` to `"2020"` and globs all 2021 of them (harmless, since
only `2020/` exists, but it is not what was meant), and `n_keep = int(0.5 * n_total)` sits under a
comment saying `# keep first 80%`.

## 5. End-to-end test, 2026-09-14

Ran on the project environment — torch 2.14.0, matplotlib 3.11.1, lightning 2.5.6 — against the
real archive. Every stage the notebook depends on:

| Stage | Result |
|---|---|
| the §2 pooch cell | downloaded 1.94 GiB, **hash verified against the pin**, unzipped to 315 files, `data_LDM/` present with `2020/`, `checkpoints/`, `static_vars/`, `preprocessing.py`, `stats.json` |
| **B8, the Colab path** | reproduced exactly: as shipped, `get_file_list()` prints `Using 0 of 0 files from 2020.` and returns an empty list, no error. After repointing `preprocessing.DATA_DIR`, 24 files. The two-line fix in §4 works |
| `zstandard` + `torch.load` on a real frame | 2020-02-12 decoded, 24 hourly records, 15 variables, `2mT` at (84, 72) |
| `rioxarray`/`rasterio` engine on the static tifs | all three load at (672, 576) |
| UNet and VAE checkpoints | read on torch 2.14, saved by lightning 2.5.3. Note `vae-epoch=19.ckpt` has **empty** `hyper_parameters`, so `load_from_checkpoint` must be given `vae=`/`unet_module=` explicitly — which the notebook does |
| LDM checkpoint | loads once `Conditioner` is defined and lightning is <2.6 — see §4 |

**Where the 1.94 GiB goes, and how much of it is dead weight:**

| | files | size | used? |
|---|---|---|---|
| `2020/*_high_UV.pt.zst` | 48 | **1349.4 MiB** | **never referenced by any code in the notebook or `preprocessing.py`** |
| `2020/*_high_2mT.pt.zst` | 48 | 558.5 MiB | yes — globbed by `get_file_list()` |
| `2020/*_low.pt.zst` | 48 | 70.3 MiB | yes — derived from the high filenames |
| `static_vars/` | 3 | 8.9 MiB | yes |
| `checkpoints/` | 3 | 8.5 MiB | yes |

`get_file_list()` globs only `*_high_2mT.pt.zst` and derives `_low.pt.zst` from it. The wind-component
files are **69% of the archive and are never opened**. Dropping them is behaviour-preserving and takes
the download from 1.94 GiB to about **637 MiB** — a 3× cut for free, worth doing before any decision
about where to host it. (Dropping the unused half of the *pairs* as well would halve it again, but
`get_file_list` computes its train/val/test split from the full list of 48, so that one does change
behaviour.)

## 6. Merged, 2026-09-15

Done and in the working tree as `part-IV/10.4-ldm-downscaling-exercises.ipynb` (85 cells, 977 KB),
cherry-picked from `origin/ldm_notebook_branch` rather than merged, since that branch is far behind
`main`. The branch head carried 102 cells, not the 93 recorded in §1 — three later "Corrected
notebook" commits — and in that version the `KeyboardInterrupt` traceback of **B3** is already gone,
so only the Colab-path stderr needed stripping.

**Decisions taken by you before the work started:** keep the fill-in-the-blank cells as they are
(so **C9** is closed as "no change, no solutions notebook" — 8.2 already works this way), and pin the
verified SharePoint URL with the §1 hash rather than waiting on a slimmed archive or a Zenodo
deposit.

| Item | Outcome |
|---|---|
| B1, B2 | §2's pooch cell, verbatim but with `sys` imported alongside `os`; eight cells become one |
| B3 | no traceback on the branch head; Colab-path stderr dropped from the two cells that had it (**C11**) |
| B4 | `myst.yml`, after 10.3; card and four Resources entries added to `ch-10-intro.md` |
| B5, B9 | nothing to do — all six packages were already in `pyproject.toml` from the §4 pass, `properscoring` included |
| B6 | the 11 `__MACOSX/` stubs were simply not copied across |
| B7 | `preprocessing.py` committed to `part-IV/ldm_helpers/`; `stats.json` and `requirements.txt` were not — the first is regenerated into `cfg.paths.output_dir` by `train_hierarchy`, the second is superseded by `pyproject.toml` |
| B8 | the import cell picks the repo copy when it exists and the archive's otherwise, then repoints `preprocessing.DATA_DIR`/`STATIC_DIR`. Note the **repo copy is already the corrected one**: `DATA_DIR = os.path.dirname(os.path.abspath(__file__))`, `YEARS = range(2020, 2021)`, no stale "keep first 80%" comment — the Colab-hardcoded version §4 describes is the copy inside the zip |
| C1 | `10.4-ldm-downscaling-exercises.ipynb` |
| C2, C7 | `# @title` ×3, the `! ls` shell escape, and the mangled `🇰` removed |
| C3, C4 | Tomasi figure 1 → `_static/10.4-tomasi-2025-domain.png`, in a `{figure}` directive crediting the article and CC BY 4.0 (licence and full citation checked against the article page: Tomasi, Franch & Cristoforetti, *GMD* 18, 2051–2078). The PyTorch-vs-Lightning screenshot was **rebuilt as a markdown table** rather than dropped — its content is text, so nothing is lost and it now renders in both themes and is searchable. The MIT vision-book figure, the medium.com diagram and the Hydra clip-art were dropped, and the three sentences that pointed at them rewritten |
| C5 | Q1–Q9; the second "Q5" (denoising UNet) became Q6 and everything after it shifted |
| C6 | `###About`/`###Data` given their space |
| C8 | learning objectives → `tip` admonition, moved from below the domain figure to directly under the H1 |
| C10 | `Pytorch`/`Pytorch Lightning`/`PytorchLightning`/`Unet` → `PyTorch`/`PyTorch Lightning`/`UNet`. **Note this goes against §4's suggestion of lowercase**: 10.2, 10.3 and every Part III page already write "PyTorch", so matching the siblings won over CLAUDE.md's library-lowercasing rule for this one word |
| C12 | Resources went on `ch-10-intro.md`, not in the notebook — 10.2 and 10.3 have no in-notebook Resources section either. No takeaways box: that is a Part I convention, and CLAUDE.md says not to retrofit those onto ported material |

**Also changed, beyond the checklist:** the H1 became
`10.4) (Exercise) Learning to Downscale Coarse Climate Fields Using Latent Diffusion`, matching the
chapter's numbering-in-the-title convention; the classroom references ("this TA hopes…", "after
class", "for this session") were rewritten, per CLAUDE.md; roughly a dozen typos fixed
(`auxilliary`, `chanels`, `tiemstep`, `heirarchy`, `runnign`, `goodle colab`, `conjuction`,
French-style spacing before `?` and `,`); and a Colab/Kaggle-guarded `pip install` cell was added,
since the original's requirements-file mechanism was dropped and none of these six packages ship
with Colab.

**Left for you.** The two open questions from §3 that only you can answer — the intended runtime and
whether readers are expected to train at all — are unresolved, and the notebook still says both
things (train it yourself, or use the shipped checkpoints). The archive is still the full 1.94 GiB
behind a revocable link; §5's finding that `*_high_UV.pt.zst` is 69% of it and never read makes a
~637 MiB rebuild the obvious next step, with Zenodo the durable home. And, as everywhere in this
repo, the notebook has not been run here: the committed outputs are the branch's own.
