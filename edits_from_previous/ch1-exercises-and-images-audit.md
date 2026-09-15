# Part I audit, 2026-09-15: exercises and images against the 2025 book

A second granular pass over chapter 1, narrower than `ch1-comparison-1.md` … `-8.md` and
orthogonal to them: this one walks the **eight old exercise pages** question by question and maps
each to where it landed, then audits **every image** in both books. The per-subchapter comparison
files stay the record of the lectures; this file is the record of the exercises and the figures.

Not published content.

## Method

The old book was fetched page by page from
`https://freddy0218.github.io/2025_MLEES_book_online/notebook/<page>.html` and parsed to text, so
the mapping below is read off the deployed old pages rather than from memory. Old chapter 1 had 16
subchapters alternating tutorial / exercises; the eight exercise pages are `W1_S1`, `W1_S2`,
`W2_S1`, `W2_S2`, `W3_S1`, `W3_S2`, `W4_S1`, `W4_S2` (old 1.2, 1.4, 1.6, 1.8, 1.10, 1.12, 1.14,
1.16).

Every image in those pages was extracted from its base64 payload and inspected, which is how the
"could be ported" list below distinguishes real source figures from matplotlib output.

---

## 1. Old exercise pages, question by question

### Old 1.2 — (Exercises) Text and Tabular Files → new 1.1

| Old item | What it asked | Where it is now |
|---|---|---|
| Warm-up 1 | `while` loop over `PlayListRatings`, break below 6 | **Moved to 1.2**, rewritten as Exercise 6 (`while`, `break`, `continue`) on station data. The playlist framing is gone. |
| Warm-up 2 | Same, as a `for` loop | Absorbed into the same 1.2 Exercise 6. |
| Warm-up 3 | `enumerate` over a list of colours | **Dropped.** `enumerate` is taught in 1.2's lecture (cell 25) but is now exercised nowhere — see §3. |
| Exercise 1 (Text File) | Write a sentence, read back, append three lines, `math.pi` to four decimals via an f-string | **Restored 2026-09-14 as 1.1 Exercise 6**, close to the old prompt. |
| Exercise 2 (Tabular File) | Read a weather CSV with the `csv` module, split Jan/Feb/Mar into `jan.csv`/`feb.csv`/`mar.csv` | **Dropped.** The `csv` package is not taught anywhere in the new book; tabular I/O is deferred to pandas in 1.5. The *idea* — read a record file, filter by month, write a derived file — survives as 1.2 Exercise 15, done with `pathlib` and `dict` instead. |

New in 1.1 with no old counterpart: Exercises 1–5 (naming, unit conversion, operator families,
record parsing, slicing), Exercise 7 (seven-value round trip, no append), Exercise 9 (the real
station-data capstone).

### Old 1.4 — (Exercises) Simple Data Structures → new 1.2 and 1.7

The whole page is one running **solar-system** exercise across four parts. It is the largest
single thing dropped from the new chapter 1's exercises.

| Old item | What it asked | Where it is now |
|---|---|---|
| Warm-up 1 | Rewrite a list comprehension as a loop | **Reduced.** 1.2 Exercise 12 goes the other way (write the comprehension), and comprehensions are going-deeper rather than core. |
| Warm-up 2 | First twenty cubes | **Dropped.** |
| Part I, Q1–Q4 | Build the planet list, `len`, slice the rocky planets, print planets ending in "s" | **Dropped as written.** The mechanics (build, index, slice, loop with a condition) are 1.2 Exercises 1 and 6, on station data. |
| Part II, Q5–Q8 | Planet→mass dict, look up Earth, filter by mass, add Pluto | **Dropped as written**; mechanics are 1.2 Exercise 2. |
| Part III, Q9–Q11 | Mass-conversion function; keyword argument selecting the reference planet; one returning two values | **Dropped as written**; mechanics are 1.2 Exercises 3, 4, 7 (default argument + two return values). |
| Part IV, Q12–Q13 | `class planet` with `name`/`mass`; add an `is_light` method | **Moved to 1.7** as Exercises 1 and 4, on a `Glacier`/`Series`. 1.7's solution to Exercise 2 keeps a `Planet` class with a shared `g_earth` attribute — the only trace of the solar system left in the book. |

The dataset behind it (the NASA planetary fact sheet) is gone, and so is the single narrative
thread — the new 1.2 exercises are fifteen independent short items plus one capstone. Whether the
loss of a continuous, memorable, non-Earth-science storyline matters is a call for you, not a
defect: the replacement is on-theme for the book in a way planets are not.

### Old 1.6 — (Exercise) Ocean Floats Data Analysis → new 1.3 (partly), 1.4 (promised, absent)

| Old item | What it asked | Where it is now |
|---|---|---|
| Q1 | Load seven `.npy` files into named arrays | **Kept**, 1.3 Exercise 9 Step 1. |
| Q2 | Rebuild `level` with `arange` and `linspace`, check with `np.testing.assert_equal` | **Kept**, Step 3 — but checked with `np.allclose`, not `np.testing.assert_equal`, which the new book never introduces. |
| Q3 | Compare shapes, infer the shared dimensions | **Kept**, Step 2. |
| Q4 (density) | `CT_from_t` from `gsw`, then the Roquet et al. (2015) equation of state | **Kept verbatim**, Step 4, with the citation intact. |
| Q4 (plots) | One line plot per column of T, S, P, density against `level` | **Dropped.** |
| Q5 | Per-depth mean and standard deviation | **Kept**, Step 5. |
| Q6 | Same as mean profiles, with `plt.errorbar` error bars | **Dropped.** |
| Q7 | Recompute with `np.nanmean` / `np.nanstd` | **Kept and extended**, Step 6, which also asks for the missing-value count as a percentage. |
| Q8 | `plt.scatter` of float longitude against latitude | **Dropped.** |
| *(new)* | — | Steps 7 and 8 (`np.where` warm/cold labelling, `np.vstack` summary + save/reload round trip) have no old counterpart. |

**The three dropped questions are all the plotting ones, and 1.3 twice tells the reader it will
get them back in 1.4** — the exercise intro ("You will return to this same data in the next
subchapter to plot it") and the closing box ("In the next subchapter you will plot these
profiles"). 1.4's exercises never mention Argo. See §3.

### Old 1.8 — (Exercises) Replicating plots → new 1.4

Cleanest port in the chapter. All four targets kept, all four target figures regenerated locally
rather than copied.

| Old item | Data | Where it is now |
|---|---|---|
| Ex 1 Part I | NCEP/NCAR reanalysis: `contourf` + white −10 °C contour, zonal mean beside it | 1.4 Exercise 18, `_static/1.4-target-global-temperature.png` |
| Ex 1 Part II | NOAA significant earthquakes: scatter coloured by `log10(depth)`, sized by magnitude | 1.4 Exercise 19, `_static/1.4-target-earthquakes-scatter.png` |
| Ex 2 Part I | NOAA/NSIDC Antarctic sea ice, two dates, south polar stereographic | 1.4 Exercise 20, `_static/1.4-target-seaice.png` |
| Ex 2 Part II | USGS 2014 catalog over North America, Robinson, cartopy features | 1.4 Exercise 21, `_static/1.4-target-earthquakes-map.png` |

The old versions were fill-in-the-blank skeletons with the answer structure visible; the new ones
give an empty cell plus hint comments. The old `matplotlib.ticker.FuncFormatter` scientific-
notation helper for the colorbar was dropped.

### Old 1.10 — (Exercise) Earthquake Data Analysis → new 1.5

Ported near-verbatim as 1.5 Exercise 10, Q1–Q11, on the same USGS 2014 catalog and the same
hash. Improvements over the old page: a "Beyond this subchapter" box naming the six tools the
lecture did not demonstrate, a warning that a plain `str.split` leaves the leading space on the
country names, and the fill-in-the-blank skeletons removed.

Five of the old page's eleven screenshots were regenerated as targets
(`1.5-target-top5-bar`, `-magnitude-hist`, `-magnitude-hist-log`, `-hist-filtered-unfiltered`,
`-quake-scatter`). The six that were `DataFrame` screenshots (`aaaaa.jpg`, `aaaaa3`–`aaaaa6`)
were not, which is right — they showed table output the reader now produces and reads directly.

### Old 1.12 — (Exercise) Hurricane Track Analysis → new 1.6

Ported near-verbatim as 1.6 Exercise 8, Q1–Q8, same two files. The old page's pip-install
preamble, its `__MACOSX` junk entries, and its `warnings.filterwarnings('ignore')` cell are gone.
The `Long = 0 - Long` sign fix is now pre-supplied with a comment explaining the NHC convention
instead of appearing unexplained. Five of the six reference links kept; the DataCamp one dropped.

### Old 1.14 — (Exercises) Multivariate linear regression and clustering → new 1.8

| Old item | What it asked | Where it is now |
|---|---|---|
| Ex 1 Q1–Q3 | Advertising dataset: fit `LinearRegression` on TV/Radio/Newspaper, print coefficients and intercept | **Kept and strengthened** as 1.8 Exercise 5 — same file, same hash, plus a train/test split, test RMSE and R², and the "before concluding, what would you check about the three columns' scales?" question the old page did not ask. |
| Ex 2 Q1–Q2 | Penguins: `dropna`, build `X` from culmen length + flipper length | **Kept**, 1.8 Exercise 9 part 1 — but on bill length + **bill depth**, not flipper length. |
| Ex 2 Q3 | Elbow method (inertia against k) **and** silhouette analysis, each with its own target figure | **Dropped from the exercises.** The elbow method is taught in 1.8's lecture (§"Choosing k"), silhouette is mentioned there too — neither is exercised anywhere. |
| Ex 2 Q4 | k-means with k=3, compare against true species, recreate a scatter | **Reduced** to a `crosstab` of species against cluster, no figure. |
| Ex 2 Q5 | k-means with k=2, recreate a second scatter | **Reduced** into the same Exercise 9, k=2 only. |
| *(new)* | — | Exercise 9 part 2 (scale four measurements, `PCA` to two components, explained variance ratio) has no old counterpart. |

### Old 1.16 — (Exercise) Marathon Data Analysis → **dropped entirely**

The seaborn exercise page is the second large drop. Nothing from it survives; 1.8 Exercise 10 is
a different dataset (Montesinho forest fires) exercising different functions.

| Old item | What it asked | Status |
|---|---|---|
| Q1 | Convert `split`/`final` timedeltas to seconds, add two columns | Dropped |
| Q2 | `sns.jointplot(..., kind="hex")` with a steady-pace reference line | Dropped. `jointplot` **is** taught in 1.8's lecture and exercised nowhere. |
| Q3 | Add `split_frac = 1 - 2 * split_sec / final_sec` | Dropped |
| Q4 | Count negative splits (251 of ~40 000) | Dropped |
| Q5 | `sns.PairGrid` over age / split_sec / final_sec / split_frac, `hue="gender"` | Dropped. `PairGrid`/`pairplot` appears **nowhere** in the new Part I. |
| Q6 | `sns.kdeplot` of split fraction by gender | Dropped. `kdeplot` is taught in 1.8 and exercised nowhere. |
| Q7 (bonus) | `age_decade = 10 * (age // 10)`, `sns.violinplot` by decade and gender | Dropped. `violinplot` appears **nowhere** in the new Part I. |

New 1.8 Exercise 10 asks instead for `sns.boxplot` of temperature by month, `sns.barplot` of mean
wind by month, and a histogram of burned area before and after masking the zero-area records.
That is a defensible swap on subject matter — a marathon is not earth science — but it is a
narrower slice of seaborn than the old page covered.

---

## 2. Defects found in the current exercise set

| Severity | Where | Issue | Fix |
|---|---|---|---|
| **blocker** | `1.1-…-solutions.ipynb` cells 14–19 | The 2026-09-14 renumbering that inserted Exercise 6 left the tail of the notebook shifted and duplicated. Cell 15, under the heading "Exercise 7: Round-trip through a file", is a **second copy of Exercise 6's π solution** (it writes `_files/pi_exercise.txt`). Cell 17, under "Exercise 8: … with an append", writes all seven values at once with no append — that is **Exercise 7's** answer. Cell 19, under a stale "**Exercise 7**: … with an append" heading, does write-then-append — that is **Exercise 8's** answer. | Put cell 17's code under the Exercise 7 heading, cell 19's code under Exercise 8, and delete the duplicate π solution and the stale-numbered heading pair (cells 18–19 after the move). Net: the notebook loses two cells and the headings run 1…9 with no repeats. |
| **blocker** | `1.4-…-exercises.ipynb` cell 39 and `1.4-…-solutions.ipynb` cell 38 | Both say "The last two have no worked solution." The solutions notebook contains **full worked solutions for Exercise 20** (cell 46) and **Exercise 21** (cell 49). The statement is false, and it is false in the file that contradicts it. | Either delete the two solutions or delete the sentence. 1.1, 1.2, 1.3, 1.5 and 1.6 all now ship a solution for their real-dataset capstone, so keeping the solutions and dropping the sentence is the consistent choice — but that leaves CLAUDE.md's "one long exercise on a real dataset … **no solution**" rule describing only 1.7, 1.8 and Bonus A. Worth settling once for the whole chapter. |
| minor | `1.3-…-exercises.ipynb` cells 18 and 37, and the same two in `-solutions` | Both promise the Argo data comes back in 1.4 ("you will return to this same data in the next subchapter to plot it" / "In the next subchapter you will plot these profiles"). It does not: `argo` appears in no 1.4 cell. | Either add the three dropped Argo plotting questions to 1.4's exercises (see §3) or cut both forward references. |
| minor | `data/part-I/USGS_Earthquakes.zip` (221 KB) | Referenced by no notebook, no markdown page and not by `myst.yml`. Probably superseded by `usgs_earthquakes_2014.csv`. | Same treatment as `float_data/` got on 2026-09-08 — move to `data/part-I/_orphaned/`, don't delete. Confirm first. |

Checked and clean: exercise/solution heading parity in 1.2–1.8 and Bonus A (positional match, no
gaps); every `{figure}` path in Part I resolves to a file that exists; `part-I/_static` holds no
orphaned image (`make_numpy_diagrams.py` is the generator script, correctly unreferenced); every
exercises notebook opens with its intro note box.

---

## 3. Coverage gaps — taught in a lecture, exercised nowhere

Found by matching function names across each lecture and its paired exercises. These are not
regressions against the old book in every case, but they are places where the exercises are
thinner than the lecture they answer to.

| Subchapter | Taught but never exercised | Old book exercised it? |
|---|---|---|
| 1.2 | `enumerate` | Yes — old 1.2 warm-up 3 |
| 1.3 → 1.4 | Plotting the Argo profiles (line plots by depth, `errorbar` mean profiles, lon/lat scatter) | Yes — old 1.6 Q4, Q6, Q8 |
| 1.8 | elbow method / `inertia_` | Yes — old 1.14 Ex 2 Q3, with a target figure |
| 1.8 | `silhouette_score` | Yes — old 1.14 Ex 2 Q3, with a target figure |
| 1.8 | `sns.jointplot` | Yes — old 1.16 Q2, with a target figure |
| 1.8 | `sns.kdeplot`, `sns.displot` | Yes — old 1.16 Q6 (`kdeplot`) |
| 1.8 | `sns.heatmap` (correlation matrix) | No |

The 1.8 row is the substantial one: the lecture teaches eight seaborn functions and five
scikit-learn workflows, and the exercises reach `boxplot` and `barplot`. Both dropped old
exercise pages (1.14's clustering half, 1.16 entirely) fed exactly this subchapter, and nothing
replaced their volume.

Cheapest repairs, in order of value per edit:

1. **Add an elbow + silhouette step to 1.8 Exercise 9.** The data is already loaded there, the
   lecture already covers both, and it restores the old Q3 without a new dataset.
2. **Add the three Argo plotting questions to 1.4's exercises**, after Exercise 16 and before the
   NASA one. The `pooch` cell already exists in 1.3 and can be copied verbatim; it also makes
   1.3's two forward references true.
3. **Add a `jointplot` or `kdeplot` step to 1.8 Exercise 10.** The forest-fires table has
   `temp`, `wind`, `RH` and `area` — enough for a two-variable joint distribution.

---

## 4. Image audit

### 4.1 Ported from the old book

| Old file | New file | Used in |
|---|---|---|
| `snake-7386684_640.jpg` | `haim_charbit-snake-7386684.jpg` | 1.1 lecture |
| `heaven-3176544_640.jpg` | `dertobisturmjagd-heaven-3176544.jpg` | 1.1 exercises |
| `South_Napa_Earthquake.jfif` | `usgs-2014-south-napa-earthquake.jpg` | 1.5 exercises |
| `376px-Florence_2018-09-11_1750Z.jpg` | `nasa-hurricane-florence-2018-09-11.jpg` | 1.6 exercises |
| `lter_penguins.png` | `palmerpenguins-species.jpg` | 1.8 lecture |
| `culmen_depth.png` | `palmerpenguins-bill-dimensions.jpg` | 1.8 lecture |
| library logos (numpy, pandas, geopandas, scikit-learn, matplotlib, cartopy) | same, renamed | 1.3–1.8 lectures |
| — | `seaborn_logo.svg`, `xarray_logo.svg` | 1.8, 1.4 — new, the old book had no logo for either |
| old target screenshots `Unknown.png`, `Unknown-2`, `cartopy_pic1`, `cartopy_pic2` | regenerated as `1.4-target-*.png` (4) | 1.4 exercises |
| old target screenshots `aaaaa7`–`aaaaa11` | regenerated as `1.5-target-*.png` (5) | 1.5 exercises |

Note that the four 1.4 and five 1.5 targets were **regenerated**, not copied — they are the new
book's own renderings of the same data, which is why they are clean PNGs rather than the old
screenshots.

### 4.2 Old-book images not ported, and why

| Old image | Page | Assessment |
|---|---|---|
| `threefundamental.png` (numpy ndarray / ufunc / broadcasting diagram, hot-linked from `docs.scipy.org`) | old 1.5 tutorial | **Correctly dropped.** 1.3 has eleven purpose-drawn diagrams generated by `_static/make_numpy_diagrams.py` — strictly better, and not hot-linked. |
| `apple-pie-5479993_640.jpg` (Pixabay) | old 1.2 Ex 1 | The π/pie pun next to the π exercise. **Candidate** — see §4.3. |
| `weather-station-2373839_640.jpg` (Pixabay) | old 1.2 Ex 2 | Belongs to the dropped `csv`-module exercise. Nothing to attach it to. |
| `NASA_planets_edu.jpg` | old 1.4 exercises | Public-domain NASA composite of the eight planets. Belongs to the dropped solar-system exercise. Only worth porting if that exercise comes back. |
| `float_cycle_1.png` | old 1.6 exercises | Argo float dive cycle, seven labelled stages plus an example T/S profile. The best figure in the old chapter 1. **Candidate, with a licensing caveat** — see §4.3. |
| `Salinity_example.png`, `Salinity_mean.png` | old 1.6 exercises | Targets for the dropped Argo plotting questions. Would need regenerating if those come back (§3 item 2). |
| `plot1.png`–`plot4.png` | old 1.14 exercises | Targets for the elbow curve, silhouette curve, and two k-means scatters. Would need regenerating if §3 item 1 is done. |
| `Unknown-3.png`–`Unknown-6.png` | old 1.16 exercises | Targets for jointplot / PairGrid / kdeplot / violinplot. Dropped with the marathon exercise. |
| `flat_medium.jpg` | old 1.7 tutorial | A photo of a book held up against a monitor, illustrating "our media are flat" before the projections section. Low value; 1.4's projections tour makes the point with actual projections. Skip. |
| `05.11-expectation-maximization.png` (hot-linked from jakevdp's PythonDataScienceHandbook GitHub) | old 1.13 tutorial | A four-panel k-means/EM iteration figure. 1.8 teaches k-means with **no** picture of the algorithm. **Candidate** — see §4.3. |
| `1*UgYbimgPXf6XXxMy2yqRLw.png` | old 1.13 tutorial | Clip-art "Logistic Regression Model" diagram with happy/sad penguins, watermarked `@dataaspirant.com`. Skip — third-party branding, and it teaches nothing 1.8's own decision-boundary plot does not. |
| `1520-0469-JAS-D-20-0055_1__page_1___14_.png` | old 1.13 tutorial | A journal-page screenshot used as a decision-boundary illustration. Provenance unclear from the filename alone; skip rather than guess at attribution. |
| `related_tags_over_time-1-2000x2000.png` (Stack Overflow tag growth) | old 1.9 tutorial | Motivational chart for "why pandas". The data is now ~a decade old. Skip unless you want to redraw it from current data. |

### 4.3 Images worth adding

Three gaps where a figure would do real work, ranked:

1. **An Argo float cycle diagram in 1.3 Exercise 9.** The exercise opens with three sentences
   describing dive, drift, ascent and transmission and shows nothing. The old book's
   `float_cycle_1.png` is exactly this figure — but it carries a visible `© Thomas Haessig`
   credit in the lower right, so the old book's use of it was very likely not licensed for
   reuse and I would not copy it into this repo. I have not been able to confirm a
   freely-licensed equivalent, so I am not naming a source URL here. If you want the figure, the
   Argo programme's own outreach material is the place to look, and the licence needs checking
   before the file lands in `_static`.
2. **A k-means iteration figure in 1.8's "k-means clustering" section.** The lecture explains
   assign-then-update in prose only. The old book hot-linked jakevdp's figure from GitHub;
   hot-linking is not this repo's practice and that book's licence needs checking for reuse.
   Drawing one locally with the same generator pattern as `make_numpy_diagrams.py` avoids the
   question entirely, and matches how 1.3 solved the same problem.
3. **A figure for 1.7.** It is the only lecture in Part I with no image at all — 1.1 through 1.6
   and 1.8 each open with at least a logo or a photo, and 1.3 carries eleven diagrams. A single
   diagram of composition versus inheritance (the `WeatherStation` / `RiverGauge` pair the
   lecture already builds) would fit the existing style. No old-book counterpart exists; this is
   a new-book observation, not a port.

Lower priority: **Bonus A has no images** either, and its idempotent-fetch section (cache hit /
hash mismatch / re-download) is a natural three-state flowchart.

---

## 5. Cross-file updates made alongside this audit

- `ch1-comparison-1.md`, `-3.md`, `-4.md`, `-8.md` — dated pointer added to this file where the
  exercise mapping here goes finer than theirs.
- `todo-list.md` — the four §2 defects and the three §3 repairs added as open items.


---

## 6. 2026-09-15, same day: everything above actioned

The audit was written as a diagnosis; the same session then applied it. What follows is what
changed, and the two places where the audit itself was wrong.

### Corrections to this audit

- **§2 claimed 1.8 Exercises 5, 9 and 10 had no solution. They did.** The solution code was inside
  the cells headed `# Pre-supplied: download the data file and cache it locally.`, below the
  `pooch.retrieve` call — so a heuristic that looked for a code cell *after* the pre-supplied one
  found nothing. The real defect was the mislabel: three cells claimed to be downloads and carried
  the answers. Each has been split into a genuine fetch cell and a separate solution cell. Every
  other `# Pre-supplied` cell in Part I was checked for the same pattern; nothing else has it.
- §4.3 said the Argo dive-cycle figure's licence could not be confirmed. It can:
  [Euro-Argo ERIC's own outreach page](https://www.euro-argo.eu/Outreach/Educational-material/Discover-Argo-floats-for-kids/How-do-the-Argo-floats-fulfill-their-mission-in-the-Ocean)
  publishes it and credits it "© Thomas Haessig". That is an all-rights-reserved credit, not an open
  licence. It has been added at the user's explicit instruction, with the credit and a link to the
  Euro-Argo page in the caption — **flagged here because permission has not been sought.**

### Restored: the old book's long exercises, alongside the new short ones

| New location | Restored from | Contents |
|---|---|---|
| **1.2 Exercise 16** — The solar system | old 1.4 Parts I–III | Q1–Q11: list, `len`, slice, conditional loop; dict, lookup, filter, extend; three functions — fixed, defaulted, two-valued. Plus the bonus round trip, which deliberately fails and says why. |
| **1.7 Exercise 16** — The solar system, continued | old 1.4 Part IV | Q12–Q13 as written (`Planet`, `is_light`), then two questions the old version had no vocabulary for: Q14 rewrites `is_light` — which prints instead of returning and changes return type between branches — and Q15 validates in `__init__` with a `__repr__`. |
| **1.3 Exercise 9, Steps 9–11** | old 1.6 Q4, Q6, Q8 | Profiles by depth, mean profiles with `plt.errorbar`, lon/lat scatter — with the old book's own target figures. A "Beyond this subchapter" box names the four `matplotlib` functions used, the same device 1.5 and 1.6 already use. |
| **1.8 Exercise 11** — Clustering the penguin data, at length | old 1.14 Exercise 2 | Q1–Q5: `dropna`, `X` from bill length and flipper length, the elbow method, `silhouette_score`, then k=3 and k=2 scatters with marker shape carrying species and colour carrying cluster. All four original target figures restored. |
| **1.8 Exercise 12** — Marathon data analysis | old 1.16, whole | Q1–Q7: seconds columns, `jointplot(kind="hex")` with the even-pace line, `split_frac`, the 251 negative splits, `PairGrid` by gender, `kdeplot`, and `violinplot` by age decade. All four original target figures restored. |

The split of the solar-system exercise across 1.2 and 1.7 was the user's call, taken because
classes are not available until 1.7 and the sequencing rule is absolute. It uses the "continued"
pattern the book already runs from 1.1 Exercise 9 into 1.2 Exercise 15.

Placing the Argo plots back in 1.3 rather than in 1.4 was also the user's call — that is where the
old book had them. 1.3's two forward references ("you will plot these in the next subchapter") were
rewritten accordingly; they were describing something that never arrived.

### Exercise coverage after the restorations

Every gap in §3 is closed except one. `enumerate` is still taught in 1.2 and exercised nowhere —
the old warm-up that covered it was a list of colours, with nothing to restore that would not be
filler. The 1.8 gaps are all closed: the elbow method and `silhouette_score` by Exercise 11;
`jointplot`, `kdeplot`, `PairGrid` and `violinplot` by Exercise 12.

`PairGrid` and `violinplot` are exercised but not taught, which the "Beyond this subchapter" box in
Exercise 12 states plainly and links. That is a deliberate use of the existing device, not an
oversight — but if 1.8's lecture is ever extended, those two are the obvious additions.

### Solutions

Every exercise in Part I now has a worked solution, and the exercise and solution notebooks carry
identical exercise headings in identical order — checked programmatically across all nine pairs.
Specifically:

- 1.1's shifted and duplicated solution cells (§2, first blocker) repaired: Exercise 7's answer now
  sits under Exercise 7, Exercise 8's under Exercise 8, and the duplicate π solution and the
  stale-numbered heading are gone.
- 1.4's "The last two have no worked solution" sentence deleted from both notebooks. It was false —
  Exercises 20 and 21 are worked in full — and keeping the solutions is what matches 1.1, 1.2, 1.3,
  1.5 and 1.6. **CLAUDE.md's "one long exercise on a real dataset ... no solution" rule no longer
  describes Part I anywhere and should be updated or dropped.**
- Bonus A Exercise 6 pointed at `https://example.org/data/temperature.csv` with an all-zero hash, so
  its solution had to be commented out to avoid failing. It now fetches this repo's own
  `forest_fires.csv` with its real hash, runs, and demonstrates the cache-hit-on-second-run
  behaviour the subchapter is about.

### Data and images

- `data/part-I/USGS_Earthquakes.zip` removed (orphaned, 221 KB).
- `data/part-I/marathon-data.csv` added — 857 KB, sha256
  `0fff8a2bdf0cfb8887080c8132fed59399531fb836815c1935cc70823b940a85`, from
  [jakevdp/marathon-data](https://github.com/jakevdp/marathon-data). Its `pooch` URL 404s until the
  file is pushed, as every new dataset here does on first addition; the solution was verified
  against the local copy.
- Thirteen images added to `part-I/_static/`: `argo-float-cycle.png` (Euro-Argo/Haessig — see the
  licence flag above), `nasa-solar-system-montage.jpg` (NASA/JPL PIA03153, public domain),
  `kmeans-expectation-maximization.png` (VanderPlas, *Python Data Science Handbook*, code
  MIT-licensed), two `1.3-target-argo-*` and eight `1.8-target-*` figures taken from the old book's
  own rendered output.
- The 1.8 lecture's k-means section gained the expectation-maximization figure, and lost a
  duplicated opening sentence that had been sitting in two consecutive markdown cells.

### Verification

Nothing was executed as a notebook. Every solution block was extracted to a script and run against
the project environment: the full 1.3 Argo chain including the three new plotting steps; the full
1.8 solutions notebook; the new 1.2 and 1.7 solar-system blocks; the marathon block against the
local CSV. Every number quoted in a solution comment is a number that run produced — 251 negative
splits, 317.92294807370183 Earth masses, inertia `[77591, 21352, 14083, ...]`, explained variance
`[0.688 0.193]`, 247 of 517 zero-area fire records.

Two things worth knowing that the runs turned up:

- **The old marathon exercise's own conversion is now broken.** It used
  `data["split"].astype(int) / 1e9`, which assumed pandas stored timedeltas in nanoseconds. Current
  pandas uses microseconds, so that expression returns a value a thousand times too small, with no
  error. `split_frac` is a ratio and survives it, which is exactly how it would go unnoticed. The
  restored exercise uses `.dt.total_seconds()` and carries a `warning` box explaining the trap.
- The old exercise's `sns.kdeplot(..., shade=True)` and positional `sns.violinplot("x", "y")` are
  both removed in seaborn 0.13. The restored version uses `fill=True` and keyword axes; all four
  marathon figures were re-rendered and match the originals.

All 48 `{figure}` paths in Part I resolve, and `_static` has no unreferenced image.
