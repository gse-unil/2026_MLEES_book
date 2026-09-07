# Comparison: 1.7 Object-Oriented Programming for Natural Systems

Old counterpart: the classes/OOP portion of **1.3 Data Structure, Functions, and Classes**
(tutorial, `W1_S2_Tutorial.html`) + the "Part IV: Classes" portion of **1.4 (Exercises) Simple
Data Structures** (`W1_S2.html`). In the old book this material sat inside week 1, alongside
lists/dicts/functions (tracked in `ch1-comparison-2.md`); the new book gives it a full, standalone
subchapter placed much later (1.7), after numpy, matplotlib/xarray, and pandas are already known.

## Old book coverage, mapped to the new book

| # | Old section (old book order) | New book coverage |
|---|---|---|
| 1.3.4.2 Classes (intro) | Introducing OOP by creating custom classes with attributes and methods | **Kept**, reframed around a computational-thinking box ("reach for a class only when there is state to bundle") and its own "When not to use a class" section — neither confirmed in the old material, which goes straight from functions into classes with no discussion of when *not* to use OOP. |
| 1.3.4.2.1 A Class to Represent a Hurricane | Constructor with init params, input validation, custom methods (e.g. `is_dangerous()`), attribute access | **Kept in spirit, different example.** New 1.7 builds a `WeatherStation` class instead of `Hurricane`, with instance attributes, a custom method (`add_reading`), and a class attribute for a shared constant. Input validation inside `__init__` (the old class rejects an invalid longitude via `raise ValueError`) is **not** reproduced in new 1.7's own lecture class — that systematic treatment now lives in the Bonus B (defensive programming) subchapter instead, though new 1.7's Exercise 4 does add validation. |
| 1.3.4.2.2 Magic/Dunder Methods | `__init__`, `__repr__` | **Kept** — `__repr__` is still taught; `__eq__` (not confirmed in old) now appears via `@dataclass` auto-generation rather than being hand-written. Not kept as its own named subsection — folded into the main "Classes and instances" section. |
| *(not confirmed in old outline)* | Instance vs. class attributes as an explicit, dedicated comparison | **New**, or at least not confirmed as a dedicated topic in old — old focuses on building one example class rather than contrasting attribute kinds. |
| *(no old equivalent)* | `@dataclass` | **New** — no equivalent found in the old tutorial's outline at all. |
| *(no old equivalent)* | Composition (`StationNetwork` holding and delegating to `WeatherStation` objects) | **New** — not confirmed in the old material. |
| Old 1.4, Main Exercise Part IV: Classes | Define classes, add custom methods | **Kept in spirit** — new 1.7's exercises (a class with state+behaviour, instance vs. class attributes, a dataclass record, composition, inheritance) cover this territory with different, more varied tasks than the old exercise's single class-definition prompt. |

## New in the new book, no old-book counterpart

- `@dataclass` for lightweight records.
- Composition as a named, worked pattern.
- The class-vs-function decision framing and "When not to use a class" section.
- The shared-class-level-list AI-critique, explicitly framed as "the object-oriented twin of the shared-default-list trap" from 1.2 — a deliberate cross-reference the old book, which taught classes and default-argument mutability in entirely different contexts, couldn't make.
- Going-deeper on abstract base classes and the scikit-learn estimator-as-object pattern — the latter a deliberate forward link to the new statistics/ml subchapter (1.8, immediately following), itself new framing.
- Type hints used throughout every method signature as a matter of course — the old `Hurricane` class isn't confirmed to use type hints.

## What moved out, relative to the old class content

- **Placement**: moved from week 1 (old) to subchapter 1.7 (new) — deliberately late, after numpy/pandas are known, so a class can model something more substantial than toy state. A structural choice, not a drop; see `course-plan.md` for the pedagogical trade-off this creates against the old syllabus's week-1 placement.
- **Systematic input validation**: the old `Hurricane` class validates its own constructor input directly; new 1.7 doesn't do this in its own lecture class, deferring the systematic treatment to the Bonus B (defensive programming) subchapter.

Every exercise (1–7) is blank with a matching worked solution in a separate
`07-oop-for-natural-systems-solutions.ipynb`.
