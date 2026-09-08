# Comparison: 1.6 Geospatial Vector Data

Old counterpart: **1.11 Geospatial Data with Geopandas** (tutorial, `W3_S2_Tutorial.html`) +
**1.12 (Exercise) Hurricane Track Analysis** (`W3_S2.html`).

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.11.1 Installing GeoPandas | pyshp, shapely, descartes, rtree, data download | **Dropped** — new 1.6 assumes geopandas is already available, consistent with the rest of the new book not dedicating space to installation. |
| 1.11.2 Geopandas Data Structure | `GeoDataFrame` as a `pandas.DataFrame` subclass, `geometry` column, `GeoSeries` with a crs | **Kept** — new 1.6's "GeoDataFrame and shapely geometries" section covers this directly. |
| 1.11.3.1 Reading Files | `geopandas.read_file()`, automatic filetype detection | **Kept.** |
| 1.11.3.2 Vector Format Spatial Data | Point/Line/Polygon geometry types, interior/boundary/exterior | **Kept.** Point and Polygon confirmed in new 1.6; LineString is now also used directly (a `LineString` between two projected station points, with its `.length` computed in km), closing a gap flagged in an earlier review pass. |
| 1.11.3.3 Writing Files | `GeoDataFrame.to_file()`, defaults to Shapefile | **Kept, plus an explicit preference stated.** New 1.6 writes GeoJSON and GeoPackage as its main round-trip, and now also demonstrates a `.shp` write/read round-trip (with a note on the sidecar files a shapefile actually produces), alongside an explicit stated preference for GeoPackage over shapefile (multi-file, column-name/size limits) — no equivalent stated preference confirmed in old. |
| 1.11.4.1 Area and Distance | `.area`, `.distance()` | **Kept, and reframed as the AI-critique.** Verified via direct text search: old 1.11.4.3 ("Projection") only frames reprojection as *aligning data from different sources*, with no discussion of degrees-vs-metres or measuring area/distance correctly. New 1.6 makes exactly that mistake — computing `.area`/`.distance()` in a geographic crs — the spine of its AI-critique, computational-thinking box, and worked before/after cells. This framing is new, not carried over. |
| 1.11.4.2 Boundary and Centroid | `.boundary` (LineString), `.centroid` | **Restored.** New 1.6 uses `.boundary` once, to plot hazard-zone outlines, and now also uses `.centroid` in the buffer/dissolve/overlay section — a representative point computed from the dissolved hazard zone, folded into the section header ("buffer, dissolve, overlay, and centroid") and its own Learning-objectives/Takeaways bullets. |
| 1.11.4.3 Projection | `.crs` inspection, `.to_crs()` reprojection, framed around aligning data from different sources | **Kept**, reframed — see the Area/Distance row above. `to_crs` itself carries over directly (`to_crs(2056)` in new 1.6). |
| 1.11.4.4 Plot | `.plot()` for quick maps | **Kept** — new 1.6's "Plotting a map" section. |
| 1.11.5 Spatial Relationships and Operations | Predicates as direct boolean tests: `contains()`, `within()`, `intersects()`, `touches()`, `crosses()`, `disjoint()`; operations: `buffer()`, `unary_union`, `convex_hull`, `envelope` | **Reworked.** `within`/`intersects` carry over as predicate names. `buffer()` carries over. But the *mechanism* changes: old teaches predicates as direct boolean-returning method calls on a `GeoSeries`; new 1.6 wraps this into `gpd.sjoin(..., predicate="within")`, a dedicated spatial-join function — a direct text search of the old tutorial's retrievable content found no occurrence of `sjoin` anywhere. `convex_hull` and `envelope` are not confirmed as covered in new 1.6. |
| 1.11.6.1 Set-Operations with Overlay | `gpd.overlay(gdf1, gdf2, how='intersection')` | **Kept** — carries over almost verbatim into new 1.6's `gpd.overlay(..., how="intersection")`. |
| *(not confirmed anywhere in old outline)* | `dissolve()` | **New, or at least not confirmed old.** A direct text search of the old tutorial's retrievable content found no occurrence of "dissolve." New 1.6 teaches it as one of three named geometry-combination operations (`buffer`, `dissolve`, `overlay`). |
| Old 1.12, Q1–Q2 | Import geopandas/pandas; read a US-states shapefile with `read_file` | **Restored in Exercise 8** — new 1.6's hurricane capstone reads the same kind of US-states boundary file (a Census Bureau GeoJSON this time, not a shapefile). |
| Old 1.12, Q3 | Identify geometry types present in the data | **Restored** as Exercise 8's new Step 3 — print the distinct `.geom_type` values present in both the states and track layers, before any filtering or plotting, with subsequent steps renumbered (old Step 3–5 → 4–6). |
| Old 1.12, Q4 | Visualize US states, excluding Alaska and Hawaii | **Restored directly** — Exercise 8, Step 3 excludes the same two states by the same reasoning. |
| Old 1.12, Q5 | Convert the Florence track DataFrame into a GeoDataFrame | **Restored**, with an added real-data wrinkle new 1.6 calls out explicitly: the track's `Long` column is a positive "degrees west" magnitude, not a signed longitude, and needs negating — not confirmed as flagged in the old exercise. |
| Old 1.12, Q6 | Plot US states and the hurricane track together on one map | **Restored directly** — Exercise 8, Step 4. |
| Old 1.12, Q7 | Determine the CRS of the datasets | **Restored, and gone further** — old asks students to *inspect* a CRS as one step; Exercise 8's Step 5 requires an actual reprojection (to EPSG:5070) before measuring, not just inspection, matching the subchapter's central CRS lesson. |
| Old 1.12, Q8 | Identify which states were affected by the hurricane's path | **Restored, with a different mechanism.** Old's approach is described only as unspecified "spatial overlay/intersection analysis." New 1.6's Exercise 8, Step 5 buffers the reprojected track by 50 km and finds states intersecting that buffer — a concrete, reproducible version of the same idea. |

## New in the new book, no old-book counterpart

- The CRS/degrees-vs-metric AI-critique and its computational-thinking box — the dominant structural change in this subchapter, reframing content (`.area`/`.distance()`) that old already taught but never warned about.
- `gpd.sjoin()` as the mechanism for spatial joins, replacing old's direct-predicate-method approach.
- `dissolve()`.
- Going-deeper on raster data with rioxarray, zonal statistics, DEM slope/aspect, and interactive maps with folium — none of these appear anywhere in the old material.

Every short exercise (1–7) is blank with a matching worked solution in a separate
`1.6-geospatial-vector-data-solutions.ipynb`; Exercise 8, the real-dataset walkthrough, has no
solution provided.

**2026-09-08 fix pass:** a pre-launch professor review found the AI-critique cell's committed
output included a fabricated third line (a "geopandas warned about a geographic crs" claim the
cell's own code couldn't produce) and that `.isin()`/`.assign()` were used in the map-plotting
section with no introduction anywhere in 1.1–1.5. Fixed: the AI-critique cell now genuinely
captures and checks geopandas's real CRS warning via `warnings.catch_warnings()` (needs a re-run
to populate real output — nothing was fabricated); `.isin()` now gets a one-sentence gloss where
it's first used. The `.shp`/`LineString`/`.length` additions noted in the table above were added
in the same pass, closing the overclaim between the Learning-objectives/Takeaways boxes and what
the notebook actually demonstrated.
