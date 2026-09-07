# Comparison: Bonus B Defensive Programming and Packaging

No old counterpart, so there's no old-book spine to build a table from — testing, logging,
packaging, and the assert-vs-exception distinction are not topics in any old session. This
subchapter (`bonus-b-defensive-programming-and-packaging.ipynb`) is entirely new material.

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
validation), each blank with a matching worked solution in a separate
`bonus-b-defensive-programming-and-packaging-solutions.ipynb`.

## Why this subchapter exists

The old book never taught students to test their own code, distinguish `assert` from exception
handling, use `logging`, or package a notebook's worth of functions into an installable project.
Every one of those is standard practice for research code but absent from the old 16-subchapter
curriculum. The `assert`-under-`-O` AI-critique — a bug that is invisible until code runs in
optimised mode — is, like every AI-critique in this book, a new device with no old-book
equivalent.

This is one of the two subchapters held back from live teaching (per the course plan) — genuinely
new, valuable material, and the right kind of content to hold back precisely because it's an
addition, not a replacement for something the syllabus already promised. It also happens to be
where `raise`/`try`/`except` and type hints — used informally as core content earlier in the book
(1.6, 1.7) after only a going-deeper introduction in 1.2 — finally get a systematic, dedicated
treatment.
