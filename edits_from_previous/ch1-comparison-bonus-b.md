# Comparison: Bonus B Defensive Programming and Packaging (superseded — see note)

**This subchapter no longer exists as a standalone file.** Bonus B was merged rather than shipped
on its own: the defensive-programming half (assert/exceptions/logging/pytest, and the
`assert`-under-`-O` AI-critique below) moved onto the bottom of 1.7, which was retitled
"Object-Oriented and Defensive Programming" — see `ch1-comparison-7.md`'s scope note. The
packaging half (`uv`, the `src` layout, and the four going-deeper boxes on Ruff/typing/CI/semver)
moved on again into Bonus A, retitled "Reproducible Code and Data Pipelines" — see
`ch1-comparison-bonus-a.md`. This file is kept as a record of what the content *was* before that
split, not of where it lives now; the table below still accurately describes each piece of
content, just not its current location or file name.

No old counterpart, so there's no old-book spine to build a table from — testing, logging,
packaging, and the assert-vs-exception distinction are not topics in any old session. This
material (originally `bonus-b-defensive-programming-and-packaging.ipynb`) was entirely new.

## What's here (all new, no old-book mapping)

| Section | Contains |
|---|---|
| assert for invariants | `assert` for internal-logic checks; stripped under `python -O` |
| Exceptions: raise, custom types, and try/except/else/finally | a custom `PhysicalRangeError(ValueError)`; full `try/except/else/finally` |
| Validating physical preconditions | validating external input with exceptions, not asserts |
| Logging over print | `logging.basicConfig`, severity levels (`debug`/`info`/`warning`) |
| Testing with pytest | writing a module + test file to disk; plain tests, a fixture, `@pytest.mark.parametrize`; actually running the suite via `subprocess` |
| Packaging with uv: the src layout | `uv init --lib`, `src/` layout, `uv.lock` |
| When generated code lies: assert as input validation | `assert` silently compiled out under `python -O`, letting invalid data through |
| Going deeper | Ruff (lint/format); static type checking (mypy/ty); pre-commit and CI; semantic versioning and coverage |
| Takeaways / Resources | — |

Exercises: 7 exercises (an invariant with assert, a custom exception, try/except/else/finally,
validate preconditions, logging with levels, write and run a pytest suite, replace assert-based
validation) were appended onto 1.7's own exercises (renumbered as Exercises 8–14) rather than
kept in a separate solutions file — see `ch1-comparison-7.md`.

## Why this subchapter exists

The old book never taught students to test their own code, distinguish `assert` from exception
handling, use `logging`, or package a notebook's worth of functions into an installable project.
Every one of those is standard practice for research code but absent from the old 16-subchapter
curriculum. The `assert`-under-`-O` AI-critique — a bug that is invisible until code runs in
optimised mode — is, like every AI-critique in this book, a new device with no old-book
equivalent.

This was genuinely new, valuable material with no syllabus-promised equivalent to replace — the
reason it was structured as held-back extra material in the first place (see the scope note at
the top: it's now folded into 1.7 and Bonus A rather than standing alone). It's also where
`raise`/`try`/`except` and type hints — introduced only as going-deeper material back in 1.2 —
finally get a systematic, dedicated core treatment, in what is now 1.7's second half.
