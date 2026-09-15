# Comparison: 1.4 Matplotlib and Xarray

Old counterpart: **1.7 Visualization with Matplotlib and Cartopy** (tutorial, `W2_S2_Tutorial.html`)
+ **1.8 (Exercises) Replicating plots** (`W2_S2.html`). Xarray was only a "bonus" appendix in the
old subchapter (1.7.13); it is co-equal, core content in the new one.

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.7.1 Matplotlib (intro) | Static/animated/interactive plots overview | **Kept** in spirit as new 1.4's opening framing, no dedicated intro subsection. |
| 1.7.2 Figure and Axes | Explicit figure creation, `add_axes()` manual positioning | **Reduced.** The figure/axes model itself is core and central to new 1.4 ("create `fig, ax`, call methods on `ax`, label everything"). `add_axes()` for manual axes positioning is not confirmed — only `plt.subplots()` is used. |
| 1.7.3 Subplots | `fig.subplots()` vs. the `plt.subplots()` shorthand | **Kept** — `plt.subplots(nrows, ncols)` is core in new 1.4. |
| 1.7.4 Drawing into Axes | Object-oriented `ax.plot()` | **Kept.** |
| 1.7.5 Labeling Plots | `set_xlabel`/`set_ylabel`/`set_title`, `tight_layout()` | **Kept**, with an explicit "always label axes with their physical quantity and SI unit" rule new 1.4 states as a governing principle. |
| 1.7.6.1 Line Styles | Dashed, dotted, dashdot | **Restored, core.** New 1.4 has a dedicated "Line styles, colors, and markers" subsection right after the first line plot, with a worked reference plot showing all four (`-`, `--`, `:`, `-.`). |
| 1.7.6.2 Colors | Named colors, grayscale, RGB tuples, hex, default color cycles | **Restored, core** — named colors and matplotlib's `tab:` cycle are used in the same new subsection; grayscale, raw RGB tuples, and hex codes are mentioned in prose but not individually demonstrated in a code cell. |
| 1.7.6.3 Markers | Size, edge properties | **Restored, core** — `marker=` (and `linestyle="none"` to show markers alone) is demonstrated; size/edge-property customization (`markersize`, `markeredgecolor`, etc.) is not individually demonstrated. |
| 1.7.6.4 Label, Ticks, and Gridlines | Tick positioning/labels, grid display | **Mostly dropped** — one exception: cartopy's `.gridlines(draw_labels=True)` is now core, live content in new 1.4 ("Useful GeoAxes Methods" and "Regional Maps"), but that's map-specific; ordinary matplotlib tick/gridline control still isn't covered. |
| 1.7.6.5 Axis Limits | Custom axis ranges | **Dropped.** |
| 1.7.6.6 Text Annotations | Text and annotated arrows | **Dropped.** |
| 1.7.6.7 Scatter Plots | Color mapping, size variation | **Kept**, simplified — new 1.4's scatter example uses a single fixed color/size, not the color/size-mapping depth of old. |
| 1.7.6.8 Bar Plots | Vertical/horizontal bar charts | **Dropped.** |
| 1.7.7.1 2D Plotting — imshow | Raster display, origin handling | **Kept and repurposed** — new 1.4 builds its entire AI-critique around `imshow`'s `origin='upper'` default flipping an ascending-latitude field. The old tutorial shows the same `origin='lower'` option side by side with the default, but with minimal explanation and no diagnosed "why this is wrong" narrative. |
| 1.7.7.2 2D Plotting — pcolormesh | Pseudocolor mesh with coordinate arrays | **Kept**, core to new 1.4's "Two-dimensional fields" section. |
| 1.7.7.3 2D Plotting — contour/contourf | Contour lines and filled contours | **Kept** (`contourf` confirmed; plain `contour` not individually confirmed). |
| 1.7.7.4 2D Plotting — quiver | Vector field arrows | **Dropped.** |
| 1.7.7.5 2D Plotting — streamplot | Streamline visualization | **Dropped.** |
| 1.7.8 Cartopy (intro) | Geographic visualization library overview | **Kept** — see rows below; no longer "much reduced" as of the cartopy expansion (below). |
| 1.7.9 Background: Projections | Foundational projection concepts | **Reduced** to the one-line framing "a projection turns a round Earth into a flat axes" in new 1.4's live cartopy section. |
| 1.7.10.1 Cartopy Projections and Reference Systems | Specifying a projection | **Kept** — new 1.4's live section uses `ccrs.PlateCarree()` and `ccrs.Orthographic()`, with `transform=` explained. |
| 1.7.10.2 Drawing a Map | Basic map creation | **Kept.** |
| 1.7.10.3 Useful Methods of GeoAxes | `set_global`, `set_extent`, `gridlines`, `coastlines`, `stock_img`, `imshow`, `add_geometries` | **Restored, core.** New 1.4 now has a dedicated "Useful GeoAxes Methods" section (live `set_global()` + `stock_img()` + `gridlines(draw_labels=True)`, on top of the `.coastlines()` already live elsewhere) — promoted out of the going-deeper box it sat in before. `add_geometries`/raw `imshow` on a GeoAxes remain unconfirmed. |
| 1.7.10.4 Global Projections | Multiple global projection examples (`PlateCarree`, `Robinson`, `Mercator`, `Orthographic`, `InterruptedGoodeHomolosine`) | **Restored, core.** New 1.4 has "A Tour of Global Projections": the same real `t2m` field plotted into `PlateCarree`, `Robinson`, `Mercator`, and `Orthographic` in one 2×2 figure. `InterruptedGoodeHomolosine` not reproduced. |
| 1.7.10.5 Regional Maps | Localized geographic views via `set_extent` | **Restored, core.** New 1.4 has a dedicated "Regional Maps" section: the real field zoomed to the Swiss domain (`set_extent([5.5, 10.5, 45.5, 48.0], crs=ccrs.PlateCarree())`) with gridlines and 50m coastlines — no longer just a going-deeper mention. |
| 1.7.11 Adding Features to the Map | Coastlines, borders | **Kept**, `.coastlines()` live, `add_feature(BORDERS)` in going-deeper. |
| 1.7.12.1 Plotting 2D (Raster) Data on a Map | Gridded data over a map | **Kept** — this is exactly new 1.4's live cartopy demo (`ds["t2m"].mean("time").plot(ax=ax, transform=...)`). |
| 1.7.12.2 Showing Images on a Map | Imagery display | **Dropped, deliberately.** The old tutorial's own satellite image is fetched from a dead SharePoint link — same dead-link pattern hit repeatedly elsewhere in this book's data. Not restored without a real image to point at. |
| 1.7.13 Bonus: Xarray Integration | Brief xarray + cartopy mention, appendix-level | **Promoted to core**, and much expanded — see xarray rows below. Old 1.7.13 was a short bonus; new 1.4 gives xarray roughly half the subchapter. |
| 1.7.14 Doing More | Additional resources | **Kept** in spirit as new 1.4's Resources section. |
| *(no confirmed old equivalent)* | Saving figures | **Expanded.** New 1.4 gives vector-vs-raster saving (`.svg`/`.pdf` vs. `.png`) its own explicit section with a `pathlib.Path.glob` confirmation step — the old tutorial doesn't call this out as a distinct topic. |
| *(no old equivalent — xarray)* | — | **New, core:** `DataArray` vs. `Dataset`, `dims`/`coords`/`attrs`; `.isel`/`.sel` (incl. `method="nearest"`); label-aware reductions and arithmetic (`mean(dim="time")`); `.resample`/`.groupby`; `.plot()` auto-labelling; `to_netcdf`/`open_dataset` round-trip; the "refer to data by label, not by position" computational-thinking box. None of this is core in the old book — only a brief bonus mention. |
| Old 1.8, Exercise 1, Part I | Line/contour plots on real global temperature data | **Restored** — new Exercise 9 uses the real NASA GISTEMP global-temperature-anomaly record (`data/part-I/nasa_gistemp_global_temp_anomaly.csv`, monthly since 1880): a line plot of the annual mean, then the full `(year, month)` field built as an xarray `DataArray` and drawn with `.plot()` as a labelled heatmap — covering both the "line" and "contour/gridded" halves of the old exercise with one real dataset. |
| Old 1.8, Exercise 1, Part II | Scatter plot of real earthquake data, log-scaled depth colouring, magnitude-scaled markers | **Restored** as new Exercise 11, using the already-committed real USGS 2014 earthquake catalog (`data/part-I/usgs_earthquakes_2014.csv`, 120k events; a different, more recent catalog than 1.5/1.7's 2023 snapshot). Filtered to `mag >= 4`, `depth_km > 0` (17,533 events); colour by `np.log10(depth_km)`, size by `mag ** 2`, matching the old exercise's log-depth/magnitude-size scheme. Has a full worked solution, unlike Exercise 10. |
| Old 1.8, Exercise 2, Part I | Cartopy: Antarctic Sea Ice | **Restored** — new Exercise 10 uses two real NOAA/NSIDC Antarctic sea-ice concentration snapshots (August and December 2017, `data/part-I/seaice_conc_daily_sh_f17_*.nc`) on a south polar stereographic grid with 2D lat/lon coordinates, plotted with `ccrs.SouthPolarStereo()`. It is also new 1.4's first hints-as-comments, no-solution real-dataset capstone — a structural gap this subchapter had relative to its siblings, now closed. |
| Old 1.8, Exercise 2, Part II | Cartopy: mapping 2014 earthquakes | **Restored** as new Exercise 12, reusing Exercise 11's same 2014 catalog and `mag >= 4` filter, plotted on a `ccrs.PlateCarree()` map with coastlines. Hints as comments, no solution provided — matching the book's capstone-exercise convention (like Exercise 10). |

## New in the new book, no old-book counterpart

- Xarray promoted from a bonus appendix to co-equal core content — the dominant structural change in this subchapter.
- The flipped-map AI-critique's diagnosed "why this is wrong" narrative (the old tutorial shows the fix option but doesn't build a critique around it).
- Going-deeper boxes on lazy loading with dask and cloud-native zarr (ARCO-ERA5) — neither concept appears anywhere in the old material.
- The explicit vector-vs-raster figure-saving section.

Every exercise (1–12) is blank with a matching worked solution in
`1.4-matplotlib-and-xarray-solutions.ipynb`, except the two real-dataset capstones. Exercises 1–8
use synthetic data; Exercises 9 (NASA GISTEMP) and 11 (2014 earthquakes, scatter) use real data
with worked solutions; Exercises 10 (Antarctic sea ice) and 12 (2014 earthquakes, cartopy) have
no solution provided, matching the book's capstone-exercise convention.

**2026-09-14 fix pass:** restored the two earthquake exercises (old Exercise 1 Part II and
Exercise 2 Part II) flagged above as dropped, closing this subchapter's last known real-data gap.
Used the real USGS 2014 catalog already sitting committed but unreferenced at
`data/part-I/usgs_earthquakes_2014.csv` (hash-verified against the live file) rather than the old
book's dead-SharePoint source. The old exercise's own framing ("earthquakes in the US") doesn't
match this dataset, which is global — kept as a worldwide `mag >= 4` catalog rather than force a
US-only filter that would misrepresent the data.

Title renamed to "1.4) Visualization with matplotlib, cartopy, and xarray" (library names kept
lowercase per the book's scientific-lowercasing convention). Cover image added: the matplotlib
logo, credited to the project's own logo gallery.

**Content review, same pass:** the lecture used three unrelated synthetic datasets end to end —
a 1D time series for the line-plot section, a static 2D `field_celsius` for pcolormesh/contourf,
and an independently-drawn 3D `t2m`/`ds` for everything xarray and cartopy — with the AI-critique
at the end reverting to the orphaned 2D array instead of the xarray `ds` the second half of the
lecture was built around. Fixed by making `field_celsius` the actual spatial pattern inside
`t2m`: the xarray-construction cell now reuses it directly (`field_celsius[None, :, :] +
seasonal_celsius[:, None, None] + fresh day-to-day noise`) instead of redrawing an independent
field from scratch, and the AI-critique now bugs on `ds["t2m"].mean(dim="time").values` — pulling
a bare array back out of the xarray Dataset — rather than the disconnected `field_celsius`. The
lesson sharpens accordingly: the critique is no longer just "imshow flips latitude," it's "the
moment you drop out of xarray back to `.values`, you lose the coordinate safety net `.plot()` was
giving you for free," which directly motivates the preceding 20-odd cells of xarray content
instead of sitting apart from them. A one-line callback also ties the domain-mean line plot
(`ds["t2m"].mean(dim=("lat","lon")).plot()`) back to the very first plot in the notebook. Verified
end to end with a standalone script mirroring cell execution order (shapes, the flip itself, and
the north-colder-than-south gradient all check out) — needs the usual `Restart & Run All` for
committed output, since roughly half the notebook's cells now produce different numbers than
before (same look and shape, different literal values).

**2026-09-14, second fix pass — full restructure into three parts.** Reordered into matplotlib →
cartopy → xarray (previously matplotlib → xarray → cartopy-inside-xarray), each part now opening
with that project's own logo (matplotlib's already existed as the subchapter cover; cartopy's and
xarray's are new — `_static/cartopy_logo.png`, `_static/xarray_logo.svg`). Title changed to
"Visualization with matplotlib, cartopy, and xarray" to name all three.

*Matplotlib part, restored to old-book breadth (old 1.7.1–1.7.7, previously reduced — see
"New in the new book" above for what had been dropped: axis limits, text annotations, bar plots,
quiver, streamplot).* Reordered to old fidelity: figure/axes (`add_axes` shown explicitly, then
`plt.subplots()` as the shorthand used from there on) → subplots as its own structural section,
moved earlier → line styles/colors/markers → **new:** ticks and gridlines → **new:** axis limits
→ **new:** text annotations (`ax.text`/`ax.annotate`) → scatter (now with colour *and* size
mapping, closing the old "simplified" gap) and histograms → **new:** bar/barh → 2D fields, now
covering `imshow` neutrally (with `origin="lower"` shown correctly) alongside `pcolormesh`/
`contourf`, not just as the AI-critique's villain → **new:** quiver/streamplot on a synthetic
rotating wind field. Closes with a **new** "good plot vs bad plot" comparison (same mountain-
station data, one version with a cropped y-axis that turns 1°C of noise into a false crisis) —
deliberately not a second AI-critique device (the book allows one per subchapter; the flipped-map
one still closes the whole notebook, after xarray, unchanged).

*Cartopy part, entirely rebuilt.* Old content plotted the synthetic temperature field via
`pcolormesh`-on-`ds`; per instruction this was replaced with real coloured geography
(`cfeature.LAND`/`OCEAN`/`COASTLINE`) instead of a data gradient, and consequently no longer
depends on `ds` at all — it now sits *before* xarray in the notebook rather than after. Drops the
old Switzerland regional-zoom demo (`set_extent` survives only as part of the new polar-view
cell, zoomed to a hemisphere, not a country). New: a 2×2 tour of `PlateCarree`/`Robinson`/
`Mercator`/`Orthographic` that visibly shows Mercator's area inflation (Greenland vs. Africa, a
~14x true-area ratio, verified); `EqualEarth` with the 4 September 2026 UN "Correct the Map"
resolution (164–6–1, verified via news/Nature coverage, not asserted from memory); `Spilhaus`
(confirmed available in the project's installed cartopy 0.25.0 — `ccrs.Spilhaus`, added
relatively recently upstream) for the requested Antarctica-centred, ocean-connected view; a
zoomed `SouthPolarStereo` view. Closes with an explicit per-field paragraph the user asked for
verbatim: atmospheric science → PlateCarree (native NWP/reanalysis grid) / polar stereographic
(polar vortex, sea ice); oceanography → Spilhaus (connected circulation) / Mercator (its original
navigation use); geography/general reference → EqualEarth. All new visuals rendered and
eyeballed before being committed to the notebook, not just syntax-checked.

*Xarray part: content unchanged*, per instruction — same DataArray/Dataset build (still reusing
`field_celsius` from the matplotlib part), `.isel`/`.sel`, reductions, `.resample`/`.groupby`,
quick exercise, `.plot()`. Only the cartopy-dependent subsections that used to sit inside it
("Maps with cartopy", "Useful GeoAxes Methods", "A Tour of Global Projections", "Regional Maps",
and the cartopy-features going-deeper box) are gone, superseded by the new Part 2; the netCDF
round-trip cell, which is xarray-native and unrelated to cartopy, was preserved and moved to sit
with `.resample`/`.groupby` instead, right before the dask/zarr going-deeper boxes (also
xarray-native, also untouched).

Verified end to end: every code cell in the rewritten notebook extracted and run in sequence
against the project's actual installed packages (cartopy 0.25.0) — zero errors, all projections
including `Spilhaus` and `EqualEarth` render correctly. Takeaways and Resources rewritten to
match; two new Resources entries added (cartopy's own projection list, the Nature piece on the UN
resolution), both URLs verified to resolve before being added. Needs `Restart & Run All` — this
pass touched nearly every cell in the notebook.

**2026-09-14, third fix pass — matplotlib part re-ported for fidelity to old 1.7.1–1.7.7.**
Decided with the user: the *matplotlib* half of new 1.4 should follow the old tutorial's own
content and order closely; the cartopy part (rebuilt with `cfeature`, `EqualEarth`, `Spilhaus`,
`SouthPolarStereo`) and the xarray part stay exactly as the second fix pass left them. The
sections restored or added, in the old book's own order: figure/axes (`plt.figure`, `figsize`,
three `add_axes` cells including the two-axes case) → subplots (`fig.subplots(nrows, ncols)` and
its axes array, then the `plt.subplots()` shorthand, then `subplot_kw`) → **drawing into axes**
(`ax.plot` vs. `plt.plot`, and why the explicit form matters once there are two axes — old 1.7.4,
previously absent) → labeling → **customizing line plots** (several x/y pairs in one `plot` call,
swapped axes as a vertical profile, and a parametric plot — old 1.7.6, previously absent) →
line styles → colors (the single-letter codes, grayscale/RGB-tuple/hex, `plt.rcParams`'
`axes.prop_cycle` and an eleven-line figure that visibly exhausts the ten-color cycle — all
previously prose-only) → markers (now with `markersize`/`markerfacecolor`/`markeredgecolor`) →
ticks and gridlines → axis limits → text annotations → scatter (now two measured quantities
against each other, colored by time and sized by deviation, as in the old book) and histogram →
bar/barh → two-dimensional fields, now with `imshow`'s default shown *beside* `origin="lower"`,
`pcolormesh` with 1D and 2D coordinates, **cell centres vs. cell corners** (`shading="auto"` vs.
`shading="flat"` — the modern form of the old book's "last row and column ignored" demo, which no
longer applies: matplotlib 3.11 raises a `TypeError` instead of silently dropping them), and a
**curvilinear grid** → `contour` (1D and 2D coordinates, `clabel`, level counts) and `contourf`
(explicit levels, two colormaps, `extend="both"`) → quiver and streamplot.

Data: the running synthetic record now carries three stations (valley, ridge at ~1000 m, mountain
at ~2800 m) plus a lagged relative-humidity series, which is what makes the parametric plot a
real hysteresis loop rather than a line. `field_celsius` (the 4×6 temperature grid) is unchanged
and still feeds the xarray part. The contour/quiver/streamplot sections use a new finer field
over the same Swiss domain — a synthetic mean sea-level pressure low with an idealised flow along
its isobars, which replaces the old abstract rotation field and makes the quiver-over-contour
overlay a recognisable weather chart. The old book's `np.exp` was avoided (not introduced in 1.3)
in favour of an inverse-square radial profile.

**The good/bad plot was redone as the user asked**, as a single figure that breaks the practices
introduced immediately after it: no axis labels or units, the array index on the x-axis instead
of day of year, red against green with no legend, a vertical range auto-fitted to one summer
month, and default text in a 3.5-inch panel. The diagnosis is prose, then the same data replotted
with each fault fixed. **New closing section, "Best Practices for Figures in a Talk"** — a `note`
admonition (the palette has no dedicated role for a checklist; `note` is its "general aside"
slot) covering axis and colorbar labelling, plotting the coordinate rather than the index,
checking the vertical range, font size for projection, legends plus linestyle redundancy,
sequential vs. diverging colormaps and why not `jet`, what/where/when in the title, one message
per figure, and vector output. This is deliberately *not* a second AI-critique: the flipped-map
critique still closes the notebook after xarray, unchanged, per the one-per-subchapter rule.

Resources gained the user-supplied [Spilhaus story
map](https://storymaps.arcgis.com/stories/756bcae18d304a1eac140f19f4d5cb3d) (URL fetched and
confirmed to resolve, titled "The Spilhaus World Ocean Map in a Square"), placed with the cartopy
entries. Learning objectives and takeaways rewritten for the restored content.

Verified by extracting all 56 code cells of the finished notebook and running them in order
against the project's installed environment (matplotlib 3.11.1, cartopy 0.25.0): no errors. Every
new figure was rendered and eyeballed, not just syntax-checked. The matplotlib part's 42 code
cells carry no outputs — **needs `Restart & Run All`**.

**2026-09-14, fourth pass — exercises rebuilt for the new lecture, and the old book's
"replicate the figure" exercises brought back.** The set went from 12 exercises to 20, in three
blocks.

*Exercises 1–11, synthetic, matplotlib.* New coverage for everything the third pass restored to
the lecture: placing axes with `add_axes` (1), a 2×2 `plt.subplots` grid (2), telling three
series apart in greyscale with linestyles and markers (3), ticks/tick labels/major-and-minor
gridlines/axis limits (4), `ax.text` and `ax.annotate` (5), a parametric monthly
temperature–humidity loop (6), scatter with colour *and* size mapping plus a histogram (7),
`bar`/`barh` (8), one field drawn three ways — `imshow(origin="lower")`, `pcolormesh`, `contourf`
— and saved as svg (9), `quiver` over speed contours and `streamplot` (10), and **"fix the
figure"** (11): a pre-supplied cell that breaks most of the new best-practices checklist, to be
diagnosed in comments and redrawn. All eleven share one pre-supplied setup cell (three station
records plus a lagged humidity series, `default_rng(1)` — a different seed from the lecture's, so
lecture cells cannot simply be copied).

*Exercises 12–16, xarray and cartopy.* The previous set's exercises 4–8 kept verbatim, renumbered.

*Exercises 17–20, "Replicating plots".* This restores the old book's own exercise notebook
(`W2_S2.html`, "Replicating plots"), whose philosophy was: here is a figure, rebuild it. Each of
the four shows a target figure and asks for a reconstruction, with the data arriving through a
pre-supplied `pooch` cell — the same four subjects as the old notebook's Exercise 1 Parts I–II and
Exercise 2 Parts I–II:
- **17, global temperature record** — restores the old Exercise 1 Part I's *figure architecture*
  (a filled contour field beside a marginal mean line, `gridspec_kw={"width_ratios": [5, 1.5]}`)
  on data the book already has: GISTEMP anomaly as `contourf(month, year)` with the 0 °C contour
  in white, beside `.mean(dim="month")` plotted against year. The old book's own NCEP/NCAR
  reanalysis field came from a dead SharePoint link and no gridded global field is committed to
  `data/part-I/`, so the design was ported rather than the dataset. Worked solution provided.
  This replaces the previous exercise 9, which used the same file for a plainer line + `.plot()`
  heatmap pair.
- **18, historic significant earthquakes** — restores old Exercise 1 Part II exactly, including
  its dataset: `data/part-I/signif.txt.tsv` (NOAA significant-earthquake catalog, committed since
  "review of part-I" but never referenced until now; columns 8/9/20/21 are focal depth, magnitude,
  latitude, longitude, matching the old notebook's own indices). Scatter coloured by
  `log10(focal depth)` and sized by magnitude²; 2920 of 5958 rows survive the validity mask.
  Worked solution provided. This replaces the previous exercise 11, which did the same scatter on
  the 2014 catalog; that catalog is still used by exercise 20, so both committed files stay
  referenced.
- **19, Antarctic sea ice** — the previous exercise 10, kept as prose with hints and no solution.
  **No target figure: see the blocker below.**
- **20, 2014 earthquakes over North America** — restores old Exercise 2 Part II's actual design,
  which the previous exercise 12 had flattened to a global `PlateCarree` scatter: `ccrs.Robinson()`
  cropped with `set_extent([-140, -60, 12, 70])` over `LAND`/`OCEAN`/`LAKES`/`RIVERS`/`STATES`.
  The prompt is explicit that the map extent, not a filter, does the selecting, so the global
  catalog is not misrepresented as a US one. Hints, no solution.

Target figures rendered and committed as `part-I/_static/1.4-target-gistemp.png`,
`1.4-target-earthquakes-scatter.png`, `1.4-target-earthquakes-map.png`.

The old notebook's fill-in-the-blanks skeletons (`___,___ = _____._________(_, _, ...)`) were
*not* reproduced: the book's exercise convention is prompt → empty cell → solution, and the
blanks would conflict with it. The reconstruct-the-figure framing, the hint-at-a-time advice, and
the four subjects are what carried over. The old book's `matplotlib.ticker.FuncFormatter`
helper for powers-of-ten colorbar ticks was also dropped in favour of a plainly labelled
colorbar, per the new checklist.

Sequencing: `gridspec_kw`, `np.log10`, `&` and `~` on boolean masks, and cartopy's
`LAKES`/`RIVERS`/`STATES` are all named explicitly in the prompt or hints that need them, since
none is demonstrated in 1.1–1.4. **`&` and `~` for combining and negating boolean masks are not
taught anywhere in 1.3** — 1.3 covers single masks, `.sum()` on them, and `np.isnan`, but never
combines two. The previous exercise set already depended on this silently; it is now stated at
point of use, but 1.3 is the right place to fix it.

Verified: both notebooks extracted and run top to bottom against the project environment — all 18
solutions and all 8 pre-supplied cells execute without error, and the two new `pooch` URLs
(GISTEMP, `signif.txt.tsv`) were fetched live from the repo's raw GitHub URL with their hashes
checked. Both notebooks carry no committed outputs.

**Blocker, pre-existing and not introduced by this pass: exercise 19 cannot run in the project
environment.** `pyproject.toml` has neither `netcdf4` nor `h5netcdf`, and the two NSIDC sea-ice
files are HDF5-backed netCDF4 (magic bytes `\x89HDF`), so `xr.open_dataset` raises `ValueError:
found the following matches with the input file in xarray's IO backends: ['netcdf4',
'h5netcdf']. But their dependencies may not be installed`. The lecture's own netCDF round-trip
works only because `to_netcdf` falls back to scipy's netCDF3 writer. This also blocked rendering
a target figure for exercise 19, which is why it is the one replication exercise without one.
`pyproject.toml` is outside the writable paths, so the fix was left to the user: add `netcdf4`
(or `h5netcdf`) to the dependencies, after which the exercise 19 target figure can be rendered
and added like the other three.

**2026-09-14, fifth pass — the real NCEP/NCAR field found, and the replication set completed.**
The user identified the old Exercise 1 Part I dataset by its original name, `S1_3_ex_temp`, and it
turned out to be sitting in three stale worktree copies under
`.claude/worktrees/*/data/part-I/` — the same files the pre-launch review had flagged as orphaned
and believed gone. Their sha256 hashes match the dead SharePoint links' own `known_hash` values
exactly (`eaf54b88…` lon, `af1f4380…` lat, `e040ca25…` temp), so these are the genuine arrays the
old exercise handed out, not a reconstruction. Restored to `data/part-I/` and renamed to the
book's own convention, since `S1_3_ex_*` is the old book's session numbering and the review had
separately complained about the names: `ncep_global_temp_lon.npy` (192 longitudes),
`ncep_global_temp_lat.npy` (94 latitudes, north to south), `ncep_global_temp_kelvin.npy`
(94 × 192, kelvin — the name now states the unit the exercise has to convert). 73 KB in total.

*Orientation checked, not assumed.* `lat` runs north to south while the field's zonal mean is
−38.9 °C in row 0 and −18.2 °C in the last row, which looks backwards for an annual mean — so
both pairings were rendered and compared against the figure the user supplied. The arrays pair
correctly **as distributed** (no flip): the field is a *boreal-winter snapshot*, not an annual
mean, which is why the Arctic is colder than Antarctica and why the warmest zonal mean sits just
south of the equator. The flipped version puts the Tibetan cold anomaly at 35 °S and is visibly
wrong. The exercise's last step now asks the reader to work out which hemisphere's winter it is
from the zonal mean, which turns that trap into the point.

*Exercise set restructured to 21.* The GISTEMP exercise reverted to its pre-replication form —
real data, `DataArray`, annual-mean line plus `.plot()` heatmap — and moved to **17**, just before
the replication section, since the replication slot it had been standing in for now has its real
occupant. The section is then the old book's own four, each with a target figure:
**18** global surface air temperature and its zonal mean (NCEP, worked solution),
**19** historic significant earthquakes (worked solution), **20** Antarctic sea ice (no solution),
**21** the 2014 earthquakes over North America (no solution). Every committed part-I dataset stays
referenced.

Exercise 18 reproduces the old skeleton's recipe exactly — `gridspec_kw={"width_ratios": [5, 1.5]}`,
`cmap="magma"`, `levels=np.linspace(-30, 40, 15)`, `extend="both"`, a white `contour` at
`levels=[-10]` (matplotlib dashes a negative-level contour on its own, which is where the dashed
white line comes from), and `np.nanmean(temp_celsius, axis=1)` against `lat` — with the old
figure's labels (`Longitude`, `Latitude`, `$^o$C`, "Current Global Temperature") restated in the
book's own style: lowercase, units in parentheses, and "global surface air temperature" rather
than "current", which a fixed snapshot is not.

**The netCDF blocker recorded at the end of the previous pass is resolved:** `netcdf4>=1.7.4` is
now a project dependency, so exercise 20 runs, and its target figure
(`part-I/_static/1.4-target-seaice.png` — two `SouthPolarStereo` panels, winter against summer,
land in grey beneath the ice, one shared colorbar) was rendered and wired in. All four replication
exercises now show their target.

Target figures: `1.4-target-global-temperature.png`, `1.4-target-earthquakes-scatter.png`,
`1.4-target-seaice.png`, `1.4-target-earthquakes-map.png`. The previous pass's
`1.4-target-gistemp.png` was deleted: exercise 17 no longer replicates a figure, so nothing
referenced it.

Verified: both notebooks re-extracted and run top to bottom, 19 solutions and 9 pre-supplied cells,
no errors. The three `.npy` pooch URLs 404 until the files are committed and pushed (expected, same
as every dataset here on first addition); the exercise and solution code was verified against the
local copies in the meantime.

**2026-09-15 exercise/image audit:** 1.4's replicating-plots port is the cleanest in the chapter —
all four old targets kept and regenerated locally. One contradiction found: cell 39 of the
exercises (and cell 38 of the solutions) says "The last two have no worked solution", but the
solutions notebook works Exercises 20 and 21 in full. Recorded as a blocker in
[`ch1-exercises-and-images-audit.md`](ch1-exercises-and-images-audit.md) §2, together with the
proposal to add the dropped Argo plotting questions here.
