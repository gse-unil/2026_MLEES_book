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
| Old 1.8, Exercise 1, Part II | Scatter plot of real earthquake data, log-scaled depth colouring, magnitude-scaled markers | **Still dropped from this pairing** — not attempted this pass; real earthquake data is used elsewhere in the book (1.5, 1.9) but not for a scatter/colour-mapping exercise in 1.4. |
| Old 1.8, Exercise 2, Part I | Cartopy: Antarctic Sea Ice | **Restored** — new Exercise 10 uses two real NOAA/NSIDC Antarctic sea-ice concentration snapshots (August and December 2017, `data/part-I/seaice_conc_daily_sh_f17_*.nc`) on a south polar stereographic grid with 2D lat/lon coordinates, plotted with `ccrs.SouthPolarStereo()`. It is also new 1.4's first hints-as-comments, no-solution real-dataset capstone — a structural gap this subchapter had relative to its siblings, now closed. |
| Old 1.8, Exercise 2, Part II | Cartopy: mapping 2014 earthquakes | **Still no counterpart** — not attempted this pass. |

## New in the new book, no old-book counterpart

- Xarray promoted from a bonus appendix to co-equal core content — the dominant structural change in this subchapter.
- The flipped-map AI-critique's diagnosed "why this is wrong" narrative (the old tutorial shows the fix option but doesn't build a critique around it).
- Going-deeper boxes on lazy loading with dask and cloud-native zarr (ARCO-ERA5) — neither concept appears anywhere in the old material.
- The explicit vector-vs-raster figure-saving section.

Every exercise (1–9) is blank with a matching worked solution in a separate
`1.4-matplotlib-and-xarray-solutions.ipynb`. Exercises 1–8 use synthetic data; Exercise 9 (NASA
GISTEMP) and Exercise 10 (Antarctic sea ice) use real data — Exercise 10 has no solution
provided, matching the book's capstone-exercise convention.
