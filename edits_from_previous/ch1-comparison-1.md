# Comparison: 1.1 Variables, Data Types, Operators and File I/O

Old counterpart: **1.1 Variables, Control Flow, and File I/O** (tutorial, `W1_S1_Tutorial.html`) +
**1.2 (Exercises) Text and Tabular Files** (`W1_S1.html`). Old 1.1 bundled control flow together
with variables/file I/O; that portion is tracked in `ch1-comparison-2.md` instead, since it moved
to new 1.2. Rows below still list it, so this table stays a complete record of old 1.1's structure.

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.1 intro | Six scalar types (int, float, complex, bool, str, NoneType) and four data structures (list, set, tuple, dict) previewed up front | **Reframed.** New 1.1 introduces only the five scalar types it uses (no `complex`) one at a time, each tied to a real measurement from a running example station, rather than a type-system overview table. |
| 1.1.1 Basic Variables: Numbers and Strings | Naming, `type()`, multi-assignment, string concat/indexing, f-strings, dot-notation methods | **Kept**, reframed around the "a name is a contract" computational-thinking box — new. |
| 1.1.1.1 String | Concatenation, indexing incl. negative, slicing, f-strings, `.capitalize()` | **Kept**, mostly — slicing/f-strings carry over. `.capitalize()` specifically not confirmed in new 1.1, which uses `.strip()`/`.split()`/`.title()`/`.lower()` instead in its parsing example. |
| 1.1.1.2 Math Operators | `+ - * / ** %`, division returns float, `round()` | **Kept**, split out: `round()` gets its own dedicated new section (1.1.3) with a round-half-to-even note not confirmed in the old material. |
| 1.1.1.3 Relational Operators | `== != > <` | **Kept** as one of new 1.1's three named "operator families" (comparison/assignment/logical). |
| 1.1.1.4 Assignment Operators | `+= *=` | **Kept**, same as above. |
| 1.1.1.5 Logical Operators | `and or not`, identity `is`/`is not` | **Kept**, same as above; new 1.1 explicitly separates "logical" from "identity" as distinct named families, where old bundles both under one heading. |
| *(casting)* | Not confirmed as its own subsection — type coercion mentioned only in passing under Math Operators | **Expanded.** New 1.1 gives casting (`int()`/`float()`/`str()`) its own treatment, including an explicit "`int()` truncates, it does not round" pitfall callout not confirmed in the old material. |
| *(f-string formatting)* | Introduced inline in 1.1.1, no dedicated section | **Expanded** into its own "1.1.4 Formatting numbers with f-strings" section covering format specifiers. |
| 1.1.2 Control Flow | — | **Moved to new 1.2** — see `ch1-comparison-2.md`. |
| 1.1.2.1 Conditional Statements | `if`/`elif`/`else`, nesting, indentation | Moved to new 1.2. |
| 1.1.2.2 Loop Statements | `for` with `range()` (three call forms), `while` | Moved to new 1.2. |
| 1.1.2.2.1 Loop control statements | `break`, `continue`, `pass` | Moved to new 1.2. |
| 1.1.3.1 TXT files — Opening Files | Basic file handling (mechanism not confirmed — plain `open()` vs. `pathlib` unclear) | **Rewritten.** New 1.1's "1.1.7 Files and paths with pathlib" uses `pathlib.Path`/`.open()` as a context manager exclusively; the old tutorial never uses `Path` as far as could be confirmed. The overwrite-vs-append distinction ("what happens if we run the cells above again?") is new framing not found in the old material. |
| 1.1.3.2.1 Tabular files — Opening Files | Reading CSV with the `csv` package | **Dropped.** New 1.1 reads plain-text records by hand with `pathlib`; tabular/CSV handling is deferred entirely to pandas in 1.5. |
| 1.1.3.2.2 Extract data and write to new CSV file | Writing filtered/derived CSV output | Dropped along with the `csv`-package approach above. |
| 1.1.3.3 Serialization and Deserialization with Pickle | `pickle` for object persistence | **Dropped.** No equivalent found anywhere in the new book's Part I. |
| 1.1.4.1 Bonus: Structural Data with JSON | Reading/working with JSON | **Dropped** from 1.1. Not verified whether JSON reappears in a later new subchapter. |
| 1.1.4.2.1 Bonus: netCDF4 — creating and storing | Opening a dataset, creating dimensions, adding variable attributes, writing data, with the raw `netCDF4` package | **Replaced.** New 1.1 has no netCDF content; netCDF appears instead in new 1.4 via xarray's high-level `to_netcdf`/`open_dataset`, not the raw `netCDF4` package the old book used. |
| 1.1.4.2.2 Bonus: netCDF4 — reading stored files | Reading a netCDF4 file back | Same replacement as above — via xarray in 1.4, not here. |
| *(no old equivalent)* | — | **New:** "When generated code lies: a hidden type bug" AI-critique (string-vs-numeric comparison) closes the subchapter — this device doesn't exist anywhere in the old book. |
| Old 1.2, Warm-up 1–3 | While-loop playlist ratings, for-loop equivalent, `enumerate` over a list of colors | These are control-flow warm-ups; dropped as written. `enumerate` itself resurfaces in new 1.2, not 1.1. |
| Old 1.2, Exercise 1 (Text File) | Write a sentence, read it back, append three more, using the `math` module for π precision | **Reframed.** New 1.1's Exercises 6–7 ("Round-trip through a file[, with an append]") cover the same write/read/append arc with `pathlib`, dropping the `math.pi` framing device. |
| Old 1.2, Exercise 2 (Tabular File) | Uncertain — the old page truncated before this exercise's body; a `pandas`/`numpy` import was visible at the top of the notebook, which would be off-sequence for an old-1.1-equivalent lesson if actually used there | Not reproduced. New 1.1's Exercise 8 (a real multi-step station-data exercise, continued into 1.2) is a different, purpose-built real-dataset capstone, not a port of this specific exercise. |

## New in the new book, no old-book counterpart

- The "a name is a contract" and casting-pitfall computational-thinking framing.
- `pathlib.Path` as the sole file-I/O interface, with the overwrite-vs-append distinction taught explicitly.
- The "When generated code lies" AI-critique device — present in every new subchapter, absent everywhere in the old book.
- A single running dataset (the Jungfraujoch station) threading through the whole subchapter, vs. the old tutorial's scattered, self-contained mini-examples.
