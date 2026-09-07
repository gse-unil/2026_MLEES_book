# Final audit (superseded — see note)

**Superseded.** This audit was written against the same 10-subchapter, `01-`/`02-`… numbered
structure as `course-plan.md` (see that file's note) — file names like
`01-environment-and-data-types-exercises.ipynb` and subchapter numbers like "1.10" for what is
today's 1.8 predate the later consolidation to 8 subchapters + Bonus A. See CLAUDE.md's "Current
state" for the authoritative picture. Kept as a historical record of the specific bugs it found
and fixed (the k-means/PCA regression, 1.9→1.6's content-after-critique reorder, leaked answer
cells in 01/02, exercise-heading standardization) — those fixes are real and still in effect,
just described under since-renamed files and numbers. A separate, independent pre-launch review
(see the `ch1-comparison-N.md` files and `todo-list.md`) has since re-audited all of 1.1–1.8 plus
Bonus A against today's actual structure and found its own, different set of issues.

A full pass over all 10 subchapters (lectures, exercises, solutions), the appendix, and myst.yml,
checking for content correctness, cross-file consistency, structural flow, and mistakes. Fixed
what was clear-cut and low-risk along the way; flagged the rest below for a decision.

## Bugs found and fixed in this pass

1. **1.10 lost its own k-means/PCA framing.** The k-means/PCA section itself was present in the
   body, but the Learning Objectives, Takeaways, Resources, and intro-paragraph updates that were
   supposed to accompany it were missing from the file — the section existed without being
   introduced or summarized anywhere. Re-applied all four. Also found the crosstab explanatory
   comment in the k-means cell had gone missing the same way; re-added it. I don't have a clean
   explanation for how these were lost after apparently being written earlier in this session —
   flagging the uncertainty rather than guessing at a cause.
2. **1.9 had core content sequenced after its own AI-critique.** Every other subchapter in the
   book ends its content sections, *then* runs the AI-critique, *then* going-deeper boxes, *then*
   Takeaways. 1.9 alone had three real content sections — spatial predicates/joins,
   buffer/dissolve/overlay, plotting a map — sitting *after* the "measuring in degrees" critique,
   with the critique stranded in the middle of the notebook. Reordered so the critique now
   immediately precedes the going-deeper boxes and Takeaways, matching every sibling subchapter.
   Checked variable dependencies before moving anything (`in_hazard`, `zones`, `stations_lv95`) —
   all still resolve in the new order.
3. **1.1, Exercises 6 and 7 shared the identical title** ("Round-trip through a file") despite
   testing different things — Exercise 6 is a plain write, Exercise 7 adds an append-mode step.
   Retitled Exercise 7 to "Round-trip through a file, with an append."
4. **1.4's new cartopy going-deeper box used an import hidden inside a comment** (`import
   cartopy.feature as cfeature` was parenthetical, not a real line) — every other going-deeper
   snippet in the book is copy-paste runnable. Promoted it to a real import line.
5. **1.4's intro paragraph had an awkward dangling clause** from the cartopy addition ("xarray,
   which wraps ... then puts a field on a real map with cartopy" — grammatically attributing the
   cartopy step to xarray itself). Split into its own sentence.

## Everything else checked and clean

- All 30 `part-I/*.ipynb` files plus the appendix notebook parse as valid JSON.
- No `ERROR`/`ModuleNotFoundError` outputs anywhere in the book (re-swept after all this
  session's fixes, not just the ones known about going in).
- No leftover dropdown "Solution" cells in any of the six exercises notebooks split this session.
- Every lecture has exactly one `important`-class computational-thinking box (checked all 10,
  including the two touched this session — the cartopy and k-means/PCA additions didn't
  accidentally add a second one).
- Structural order (content → AI-critique → takeaways → resources) is now correct in all 10
  lectures, including 1.9 after the fix above.
- "AI assistants" capitalization is correct everywhere it appears (re-checked 1.2 specifically,
  which I hadn't explicitly re-verified before).
- `myst.yml`'s table of contents is complete and consistent with the files on disk — all 10
  subchapters and their exercises are listed; all 10 solutions notebooks are present as
  commented-out entries (reference material, not published), matching the 1.1–1.4 convention.
- Every `git status`-modified file this session is accounted for by a specific, known change.

## Follow-up: both open items resolved

**1. `01` and `02`'s solutions notebooks rebuilt.** Both had the same defect class `03` had at the
start of this session — worse, in fact: it turned out `01` and `02`'s *exercises* notebooks
themselves still had leaked full-answer cells sitting right next to (or, for three exercises in
`01`, entirely *instead of*) the blank attempt cell — a bug this audit hadn't caught yet, since I'd
only compared exercises against their separate solutions files, not scanned exercises notebooks
for embedded answers. Fixed both problems together:
- `01-environment-and-data-types-exercises.ipynb`: Exercises 3, 5, and 7 had no blank cell at
  all — the code cell directly under each was the full worked answer. Replaced each with a blank
  `# Your solution here` cell.
- `02-data-structures-and-control-flow-exercises.ipynb`: 11 of 14 exercises had a blank cell
  *followed by* a leaked answer cell. Removed the 11 leaked cells (verified each pairing before
  removing).
- Rebuilt both solutions notebooks from scratch: extracted and verified the leaked code where it
  existed (most exercises), and freshly wrote and tested the four that had never had a solution
  anywhere (01 Exercises 1, 2, 4, 6; 02 Exercises 4, 5). Both real-dataset capstones (01 Exercise 8,
  02 Exercise 11) correctly get no solution, matching the rest of the book.

All 10 subchapters now have an exercises notebook with nothing but blank attempt cells, and a
separate, verified, in-sync solutions notebook.

**2. Exercise headings standardized to `Exercise N: Title` everywhere.** Converted all 84 em-dash
headers across 05–10 (exercises and solutions) to the colon style already used in 01–04. Also
caught and fixed two side effects of the mechanical conversion: capitalized the word right after
the colon to match 01–04's convention (`Exercise 1: build a GeoDataFrame` → `Exercise 1: Build a
GeoDataFrame`, 82 headers), and reverted one case where that capitalization rule collided with a
scientific-lowercasing term — `netCDF versus zarr` had briefly become `NetCDF versus zarr`, fixed
back to the book's established lowercase-`n` spelling.
