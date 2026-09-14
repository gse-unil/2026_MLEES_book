#!/usr/bin/env python3
"""Execute every book notebook for CI.

Lecture and *-solutions.ipynb notebooks are expected to run clean: any error
there is a real bug and fails the build. *-exercises.ipynb notebooks contain
deliberate inline blanks (e.g. `_____`) for students to fill in, so they are
allowed to error; the resulting error outputs are stripped afterward so the
published page shows the incomplete code with no traceback, while any cells
that *did* run (e.g. setup/import cells before the first blank) keep their
real, fresh output.

Run from the repo root: uv run python .github/scripts/execute_notebooks.py
"""

import sys
import time
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

REPO_ROOT = Path(__file__).resolve().parents[2]
PARTS = ["part-I", "part-II", "part-III", "part-IV", "appendix"]
CELL_TIMEOUT = (
    600  # seconds per cell -- raise if a training cell legitimately needs longer
)
KERNEL_NAME = "python3"


def is_exercise_notebook(path: Path) -> bool:
    return path.stem.endswith("-exercises")


def strip_error_outputs(nb) -> bool:
    """Clear outputs on any cell that produced an error. Returns True if anything changed."""
    changed = False
    for cell in nb.cells:
        if cell.get("cell_type") != "code":
            continue
        outputs = cell.get("outputs", [])
        if any(o.get("output_type") == "error" for o in outputs):
            cell["outputs"] = []
            cell["execution_count"] = None
            changed = True
    return changed


def execute_notebook(path: Path) -> None:
    nb = nbformat.read(path, as_version=4)
    allow_errors = is_exercise_notebook(path)

    ep = ExecutePreprocessor(
        timeout=CELL_TIMEOUT,
        kernel_name=KERNEL_NAME,
        allow_errors=allow_errors,
    )

    start = time.time()
    try:
        ep.preprocess(nb, {"metadata": {"path": str(path.parent)}})
    except CellExecutionError as exc:
        # allow_errors=False and a cell failed: this is a real bug, not an
        # expected student blank. Let it propagate and fail the build.
        print(f"::error file={path}::Execution failed: {exc}", file=sys.stderr)
        raise
    elapsed = time.time() - start

    if allow_errors and strip_error_outputs(nb):
        print(f"[cleaned] {path} ({elapsed:.0f}s, stripped expected blank-fill errors)")
    else:
        print(f"[ok]      {path} ({elapsed:.0f}s)")

    nbformat.write(nb, path)


def main() -> None:
    notebooks = sorted(p for part in PARTS for p in (REPO_ROOT / part).rglob("*.ipynb"))
    if not notebooks:
        print("No notebooks found -- check PARTS / working directory.", file=sys.stderr)
        sys.exit(1)

    failures = []
    for path in notebooks:
        try:
            execute_notebook(path)
        except CellExecutionError:
            failures.append(path)

    if failures:
        print(
            f"\n{len(failures)} notebook(s) failed to execute cleanly (real bugs, not expected blanks):"
        )
        for f in failures:
            print(f"  - {f.relative_to(REPO_ROOT)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
