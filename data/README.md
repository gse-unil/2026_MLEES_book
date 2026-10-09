# Datasets

Where the files committed under `data/` come from: one section per file, with what was checked
and when, and what would break if the file were replaced.

## `part-I/station_iib_daily_max_temp_2022.csv`

Daily maximum air temperature for 2022 at station IIB, Independence Municipal Airport, Iowa,
US. Used in 1.1 (Exercise 9) and 1.2 (Exercise 16), exercises and solutions.

| Field | Value |
|---|---|
| Station | IIB (ICAO KIIB), Independence Municipal Airport, Buchanan County, Iowa, US |
| Station type | automated weather observing system (AWOS), listed in the Iowa Environmental Mesonet's Iowa ASOS network, `IA_ASOS` |
| Location | 42.4544° N, 91.9504° W, elevation 294 m (IEM station metadata) |
| Variable | daily maximum air temperature, in degrees Fahrenheit |
| Period | 2022-01-01 to 2022-12-31, one row per day, 365 rows |
| Missing values | 16 empty temperature fields, 25 October to 9 November 2022 |
| Format | CSV with CRLF line endings; header `station,day,max_temp_f`; day as `dd.mm.yy` |
| Size | 6797 bytes |
| sha256 | `034755fb289b4e157e5d029995481786a359eb25a80df62c09ee83d063013144` |
| Licence | IEM products are public domain; IEM asks for attribution to the Iowa Environmental Mesonet of Iowa State University |

### Origin

The file comes from the 2025 edition of the course. There, the lab at
<https://freddy0218.github.io/2025_MLEES_book_online/notebook/W1_S1.html> fetched its station
data as a zip from a University of Lausanne SharePoint link, which returned HTTP 403 on
2026-09-23. That page and its tutorial page do not name the station or say where the data came
from. The file was committed here on 2026-08-20 as `data/part-I/Ch1-Lab01-Ex8.csv` and renamed
on 2026-09-15; its bytes are unchanged (same sha256).

### Upstream source

The values match the Iowa Environmental Mesonet (IEM) "Computed Daily Summary of Observations"
for station IIB, variable `max_temp_f`. Compared on 2026-09-23 against a fresh download:

<https://mesonet.agron.iastate.edu/cgi-bin/request/daily.py?network=IA_ASOS&stations=IIB&year1=2022&month1=1&day1=1&year2=2022&month2=12&day2=31&var=max_temp_f&format=csv&na=blank>

- The header, `station,day,max_temp_f`, is identical. IEM writes the day as `yyyy-mm-dd`; this
  file uses `dd.mm.yy`.
- The 16 empty days are the same 16 days in both.
- Of the 349 days with a value, 188 are identical and 229 agree to within 0.1 °F.
- 118 days are 0.2 to 1.3 °F higher in this file than in the current IEM record, and two differ
  by far more: 31 January 2022 (55.0 °F here, 46.6 °F at IEM) and 31 March 2022 (65.1 °F here,
  51.8 °F at IEM).

IEM computes these summaries from the observations it has collected, so the most likely
explanation is that this file was downloaded before IEM recomputed the 2022 values. That is an
inference: when and how the 2025 file was produced is not recorded anywhere found. The station
identity does not rest on that inference: the same 16-day gap and 188 identical values are not
something an unrelated station would reproduce.

### Before replacing it

A fresh IEM download is not this file: the values differ as above, and the day format and line
endings differ too. Replacing it changes the sha256, so the `known_hash` in all four 1.1 and 1.2
notebooks (exercises and solutions) must be updated, and every value quoted in their solution
comments rechecked: the 1.1 solutions quote the first two records, 14.7 °F and 8.6 °F.

Station metadata: <https://mesonet.agron.iastate.edu/sites/site.php?station=IIB&network=IA_ASOS>.
IEM terms of use: <https://mesonet.agron.iastate.edu/disclaimer.php>.

## `part-I/uscrn_daily_2017_ny_millbrook_3w.txt`

One year of daily observations from the U.S. Climate Reference Network (USCRN), station
Millbrook 3 W, New York. Used in 1.5's lecture, section "Reading Data Files: Weather Station Data"
and everything after it.

| Field | Value |
|---|---|
| Station | WBANNO 64756, Millbrook 3 W, New York, US |
| Location | 41.79° N, 73.74° W |
| Period | 2017-01-01 to 2017-12-31, one row per day, 365 rows plus one header line |
| Variables | 28 columns, as listed in NOAA's `HEADERS.txt`: daily air temperature, precipitation, solar radiation, surface temperature, relative humidity, and soil moisture and soil temperature at 5, 10, 20, 50 and 100 cm |
| Missing values | −9999.0 (−99.000 in the three-decimal soil-moisture columns). No data at all on 2017-10-04; soil moisture at 5 cm is missing on 48 days, 43 of them in January and February |
| Format | whitespace-separated text, variable-width columns; dates as `YYYYMMDD` |
| Size | 79650 bytes |
| md5 | `5129dcfd19300eb8d4d8d1673fcfbcb4` (the hash the 2025 edition pinned) |
| sha256 | `f97637cf9909548a10843e9af352470b8aa1f9df5d971aa74e7478d63c7eca07` |
| Licence | the Zenodo mirror is CC-BY-4.0; the underlying NOAA data are a US government product |

### Origin

The 2025 edition's pandas tutorial
(<https://freddy0218.github.io/2025_MLEES_book_online/notebook/W3_S1_Tutorial.html>) fetched
`data.txt` with pooch from the Zenodo record "Mirror of data from NOAA U.S. Climate Reference
Network for Research Computing in Earth Science" (R. Abernathey,
<https://doi.org/10.5281/zenodo.5564850>), pinned by md5. Downloaded from that record on
2026-10-05; the md5 matched. The file was committed here under a descriptive name, bytes unchanged.

### Upstream source

`data.txt` is the mirror's `CRND0103-2017-NY_Millbrook_3_W.txt` with one header line of column
names prepended; below the header the two are byte-identical (checked 2026-10-05). Compared the
same day against NOAA's current file,
<https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/2017/CRND0103-2017-NY_Millbrook_3_W.txt>:
16 of 365 rows differ, all between 2017-10-06 and 2017-12-30, all in the soil-moisture columns,
and never by more than 0.001 m³ m⁻³. NOAA reprocessed those values after the mirror was made.
Column definitions and the missing-value codes are in
<https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/README.txt>.

### Before replacing it

A fresh NOAA download has no header line and slightly different soil-moisture values, so
`read_csv` would need `names=` and the hash in 1.5's fetch cell would change. Values quoted in 1.5's
prose — 364 temperature values, 48 soil-moisture gaps, the `fillna(0)` bias — would need
rechecking.

## `part-III/climate_invariant_*` (5.3)

Normalization constants and the vertical grid for the climate-invariant parameterization exercise
in 5.3. Five small files, all of them read by 5.3's data cells with `pooch` from this repo.

| File | Size | sha256 |
|---|---|---|
| `climate_invariant_norm_raw.nc` | 23,634 B | `ee3c669928031af1a03ec3bc61373107575173decf66ede9b0c3b8568214ca0f` |
| `climate_invariant_norm_RH.nc` | 23,634 B | `4d5275746eb1aad4a2279e16784befaa4beeab5a2aa6545e0e85437c8d73476f` |
| `climate_invariant_norm_BMSE.nc` | 22,914 B | `396df61a24f6111acc1b908cdda3d10e0649d3eb551de860b3ebeb4419adc514` |
| `climate_invariant_norm_LHF_nsDELQ.nc` | 23,634 B | `514413a6ab0f33039df5f815a925cf8916454d288f384615050131f1bdc8b06f` |
| `climate_invariant_hyam_hybm.npz` | 982 B | `760ea10734da9382d0c367407ef0469ba651dd96f3d4b6290a8736b093038fca` |

The four `.nc` files hold the mean, standard deviation, minimum and maximum of each input and output
variable, once for the raw inputs and once for each rescaled input (relative humidity `RH`, plume
buoyancy `BMSE`, latent heat flux over moisture disequilibrium `LHF_nsDELQ`), computed over the cold
climate. They are byte-identical copies of the files the 2025 edition's notebook fetched from
SharePoint; each sha256 above equals the `known_hash` that notebook pinned, checked on 2026-10-09.
The `.npz` file holds the 30 hybrid-coordinate coefficients `hyam` and `hybm` of the climate model's
vertical grid. The 2025 edition fetched them as a pickle (676 bytes, sha256
`343339f9b0fd4d92a8a31aabf774c0a17b6ac904feb6a2cd03e19ae4ff2bd329`); the arrays were re-saved with
`numpy.savez` so that the notebook does not unpickle a file, and compared equal element by element.

### Not committed: the two climate simulations

`EfHoI_pZ…` (cold, file name `2023_15_02_RG_TEST_M4K_reduced.nc`) and `Eeq_n6Qv…` (warm,
`2023_15_02_RG_TEST_P4K_reduced.nc`) are fetched by 5.3 from a personal SharePoint share (`tom_beucler_unil_ch`),
the same pattern as 10.4. Streamed and hashed on 2026-10-09; both resolve to a
NetCDF (HDF5) file of 1,822,652,866 bytes (1.70 GiB) with 2,398,208 samples and 184 stacked
variables.

| Climate | sha256 |
|---|---|
| cold | `7b793afdd866a2e9b0db8fdb5029a88d557bf98525601275f5a335e95b26ac1a` |
| warm | `211db8ae89904f1fa3e2f17dc623bc6f5c6156cf24f4e3a42d92660ab1790fd4` |

Both equal the hashes the 2025 notebook pinned. The links carry no `?e=` token, so they do not expire
by themselves, but the owner can still revoke them; the pinned hash makes a revoked link fail with a
checksum error instead of saving a sign-in page. The files are far over the 50 MB ceiling and no
git-lfs is configured, so they stay remote. A Zenodo deposit would make them durable and citable.

### Dropped from the 2025 notebook

The 2025 notebook also fetched three 22 to 26 MB files (`RH_train_open`, `BMSE_train_open`,
`LHFnsDELQ_train_open`, 15,400 samples each) only to build "normalization generators", of which it
used the `sub` and `div` attributes. Those two arrays depend on the normalization files above, not on
the samples, so 5.3 computes them from the `.nc` files directly and does not download the three
files. Checked on 2026-10-09: the arrays are equal to the ones the 2025 code produces.
