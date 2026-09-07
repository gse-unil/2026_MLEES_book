# Comparison: 1.2 Data Structures and Control Flow

Old counterpart: the control-flow portion of **1.1 Variables, Control Flow, and File I/O**
(`W1_S1_Tutorial.html`, tracked fully in `ch1-comparison-1.md`) + the data-structures/functions
portion of **1.3 Data Structure, Functions, and Classes** (`W1_S2_Tutorial.html`) +
**1.4 (Exercises) Simple Data Structures** (`W1_S2.html`), minus classes/OOP (moved to new 1.7,
tracked in `ch1-comparison-7.md`). Two old lectures feed this one new subchapter.

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.1.2.1 Conditional Statements *(from old 1.1)* | `if`/`elif`/`else`, nesting, indentation-based scoping | **Kept.** New 1.2's "Control Flow" section covers this, though not given its own separately-headed subsection the way old 1.1.2.1 was. |
| 1.1.2.2 Loop Statements *(from old 1.1)* | `for` with `range(N)`, `range(A,B)`, `range(A,B,step)`; `while` | **Kept**, plus new: an explicit "`range()` method" admonition box and an "enumerate gives index + value" callout not confirmed as emphasized in old. |
| 1.1.2.2.1 Loop control statements *(from old 1.1)* | `break`, `continue`, `pass` | **Kept** as "Break and continue"; `continue` reframed around skipping `None`/missing values specifically — new framing, foreshadowing NaN-handling in 1.5. `pass` not confirmed as covered in new 1.2. |
| 1.3.1 Lists | `.append()`, `.extend()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, slicing, iteration, list comprehensions | **Reduced.** New 1.2 covers list creation/indexing/slicing/`len()`, and confirms `.append()`-level mutation; the fuller method list (`.extend`/`.insert`/`.remove`/`.pop`/`.sort`) isn't individually confirmed to all reappear. List comprehensions are demoted from core (old introduces them directly) to a going-deeper box, per deliberate project decision. |
| 1.3.1.1 Updating List | Modifying elements, removing ranges, add/delete via methods | Folded into the reduced list coverage above. |
| 1.3.1.2 Use Lists in Loops | Index-based `range()` loops vs. `enumerate()` | **Kept** — `enumerate` is core in new 1.2 (Exercise 6: "Pair two stations with zip" extends the same idea to `zip`, which isn't confirmed in the old material). |
| 1.3.2 Tuples | Creation, indexing, unpacking, `.index()`, immutability vs. lists | **Kept.** New 1.2's tuple exercise (unpacking + catching the `TypeError` from a mutation attempt) matches this closely; `.index()` not individually confirmed. |
| 1.3.3 Dictionaries | Creation, key access, `update()`, `.get()`, `.items()`/`.keys()`/`.values()` | **Kept and expanded** — new 1.2 gives `.get()` with a default value and safe lookup its own dedicated going-deeper box, more explicit than the old tutorial's brief treatment. |
| 1.3.4 Functions and Classes (DRY intro) | Code-organization framing, DRY philosophy | **Kept** in spirit; classes portion split out to new 1.7. |
| 1.3.4.1 Functions | `def`, optional/default arguments, `*args`, lambda, `map()`/`filter()` | **Reduced, then partially restored.** `def`, default arguments, and multi-return (tuple unpacking) are core in new 1.2. `*args` was initially dropped with no equivalent — **now restored as core**, right after default arguments, with its own worked example (`mean_of(*values)`) and a dedicated Exercise 10 ("A variable number of arguments") plus solution. `map()`/`filter()` are still dropped from core; new 1.2's Exercise 13 (renumbered from 12) reaches a filter-like result via a list comprehension instead of the `filter()` builtin. Lambda is demoted to a going-deeper box ("lambda and scope (LEGB)"). |
| 1.3.4.1.1 Pure vs Impure Functions | Functions that mutate arguments vs. those that don't | **Kept**, but demoted from core to a going-deeper box; gets a dedicated new exercise (Exercise 13: spot the impure function) not present in the old material. |
| 1.3.4.1.2 Namespace | Variable scope, shadowing, mutable-object gotchas | **Folded into the going-deeper lambda/LEGB box** rather than kept as its own standalone topic. |
| 1.3.4.2 / 1.3.4.2.1 / 1.3.4.2.2 Classes | `Hurricane` class, `__init__`, `__repr__`, input validation via `raise` | **Moved to new 1.7** — see `ch1-comparison-7.md`. |
| Old 1.1's data-structures overview | Sets *defined* alongside list/tuple/dict in the intro table | **Dropped**, by deliberate project decision. Old 1.3 itself never actually *uses* sets in a working example either, so little practical content is lost. |
| Old 1.4, Warm-up | Convert a list comprehension to an explicit loop; generate the first 20 cubes | Not reproduced as such; comprehensions are now going-deeper material with their own optional exercise set (12–14) instead of a core warm-up. |
| Old 1.4, Main Exercise Part I: Lists and Loops | Create/manipulate lists, iterate, index | **Kept** — new Exercises 1, 6, 7 cover this territory. |
| Old 1.4, Main Exercise Part II: Dictionary | Dictionary construction and lookup | **Kept** — new Exercise 3. |
| Old 1.4, Main Exercise Part III: Functions | Functions with optional keyword arguments | **Kept** — new Exercises 4, 5, 9. |
| Old 1.4, Main Exercise Part IV: Classes | Define classes, add custom methods | **Moved to new 1.7's exercises.** |
| *(no old equivalent)* | — | **New:** the mutable-default-argument AI-critique (`out=[]`) — old's Namespace section discusses scope but never demonstrates this specific bug. **New:** "match the structure to the access pattern" computational-thinking box. **New:** Exercise 10 ("fix the shared-default bug") and Exercise 14 (`raise` for invalid input) have no old counterpart. |

## New in the new book, no old-book counterpart

- The mutable-default-argument AI-critique, and Exercise 11 built around fixing it.
- The "match the structure to the access pattern" computational-thinking box.
- `.get()`-with-default and safe dictionary lookup as an explicit going-deeper topic.
- `*args` restored as core content (see the row above), with its own worked example and
  Exercise 10.
- Exercise 14 (spot the impure function) and Exercise 15 (reject impossible temperatures via
  `raise`).

Every short exercise here is blank with a matching worked solution in a separate
`1.2-data-structures-and-control-flow-solutions.ipynb`; Exercise 12, the real-dataset walkthrough
continued from 1.1, has no solution provided, matching the book's capstone-exercise convention.
