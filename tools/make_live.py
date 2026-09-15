#!/usr/bin/env python3
"""Generate notebook-friendly "live" copies of the book notebooks.

The notebooks under appendix/ and part-*/ are the single source of truth, and
they are written for the website: MyST admonition and figure directives, and
code grouped into cells that read well on a page. Those same files are what a
student opens from the Colab badge, and Colab renders none of that syntax --
`:::{admonition}` and `:class: tip` arrive as literal text, and `_static/`
image paths do not resolve outside a repo checkout.

This script writes a second copy of each notebook under live/, at the same
relative path, in which:

  * admonitions become plain markdown -- a bold, marked title line for the
    flat ones and a collapsed <details> block for the dropdowns, both of which
    render in Colab, JupyterLab and VS Code alike;
  * figure directives become an <img> pointing at this repo's raw GitHub URL,
    so the image appears in Colab, with the caption below it;
  * long code cells are split into smaller ones, so that a cell is one step in
    a live session rather than one paragraph on a page;
  * outputs are stripped -- the website carries them, and a split cell's
    outputs cannot be attributed to its pieces anyway;
  * a setup cell goes in at the top, installing the niche packages the notebook
    imports that a hosted runtime lacks (cartopy is the usual one) and creating
    the `_files/` directory it writes into.  Both are guarded, so the cell does
    nothing in an environment that is already complete.

live/ is generated. Editing it by hand loses the edit on the next run: change
the book notebook and regenerate. The files do have to be committed and
pushed, because Colab and Kaggle fetch them from GitHub -- colab-badge.mjs and
kaggle-badge.mjs prefix every badge URL with live/.

Usage:
    python tools/make_live.py                 # regenerate everything
    python tools/make_live.py part-I/1.3-numpy.ipynb [more.ipynb ...]
    python tools/make_live.py --check         # exit 1 if any copy is stale
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

# Must match REPO / BRANCH in colab-badge.mjs and kaggle-badge.mjs.
REPO = "gse-unil/2026_MLEES_book"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

ROOT = Path(__file__).resolve().parent.parent
LIVE_DIR = ROOT / "live"
SOURCE_DIRS = ["appendix", "part-I", "part-II", "part-III", "part-IV"]

# One marker per admonition class, mirroring the book's fixed-role palette.
# The class is the key exactly as it appears after `:class:`.
MARKERS = {
    "tip": "\N{DIRECT HIT}",                     # learning objectives
    "danger": "\N{PUSHPIN}",                     # takeaways
    "important": "\N{BRAIN}",                    # computational-thinking fundamental
    "warning": "\N{WARNING SIGN}\N{VARIATION SELECTOR-16}",   # pitfalls, AI-critique
    "note": "\N{INFORMATION SOURCE}\N{VARIATION SELECTOR-16}",  # asides, definitions
    "hint": "\N{INFORMATION SOURCE}\N{VARIATION SELECTOR-16}",
    "seealso dropdown": "\N{LEFT-POINTING MAGNIFYING GLASS}",   # going deeper
    "note dropdown": "\N{WHITE HEAVY CHECK MARK}",              # solutions
}
DEFAULT_MARKER = "\N{INFORMATION SOURCE}\N{VARIATION SELECTOR-16}"

# --- code-cell splitting -------------------------------------------------
# Split a cell only when it is long enough to be worth breaking up, and only
# at a top-level statement that already has a blank line above it, so the
# author's own paragraphing chooses the cuts.
SPLIT_MIN_LINES = 16

# Never split a cell that touches figure state. With the inline backend, each
# cell execution flushes the current figure, so `fig, ax = plt.subplots()` in
# one cell and `ax.plot(...)` in the next draws into a figure that has already
# been rendered, and the final `plt.show()` displays nothing.
FIGURE_STATE = re.compile(
    r"\bplt\.|\bsns\.|\bfig\b|\bfigure\b|\baxes?\b|\bax\d\b|\.plot\(|\.plot_|\bccrs\b"
)

# An explicit split marker in the source overrides the heuristic in both
# directions: it splits where the heuristic would not, and it is the only
# thing consulted in a cell that carries one.
SPLIT_MARKER = re.compile(r"^[ \t]*#[ \t]*%%[ \t]*$")

# Cell tags honoured on the source notebooks.
TAG_KEEP_WHOLE = "live-keep-whole"   # never split this cell
TAG_DROP = "teaching-drop"           # omit this cell from the live copy

DIRECTIVE_OPEN = re.compile(r"^(:{3,})\{([a-z-]+)\}[ \t]*(.*)$")
CLASS_OPTION = re.compile(r"^:class:[ \t]*(.+)$")
FIGURE_OPEN = re.compile(r"^```\{figure\}[ \t]*(\S+)[ \t]*$")
OPTION_LINE = re.compile(r"^([a-z-]+):[ \t]*(.*)$")
BACKTICK_SPAN = re.compile(r"`([^`]+)`")


# --- hosted-runtime setup ------------------------------------------------
# Colab and Kaggle start in an empty working directory and do not ship every
# package these notebooks import. The generated setup cell fixes both, guarded
# so that it is a no-op in an environment that is already complete.
#
# Only niche packages are listed. numpy, pandas, matplotlib, scipy, sklearn,
# seaborn, torch and torchvision are deliberately left out: they are present on
# every hosted runtime, and installing torch or torchvision from here could
# pull a build that does not match the runtime's CUDA.
COLAB_PIP = {
    "cartopy": "cartopy",
    "geopandas": "geopandas",
    "gsw": "gsw",
    "lightning": "lightning>=2.5.3,<2.6",
    "netCDF4": "netcdf4",
    "omegaconf": "omegaconf",
    "palmerpenguins": "palmerpenguins",
    "plotly": "plotly",
    "pooch": "pooch",
    "properscoring": "properscoring",
    "rasterio": "rasterio",
    "rioxarray": "rioxarray",
    "shap": "shap",
    "torch_geometric": "torch-geometric",
    "torchmetrics": "torchmetrics",
    "xarray": "xarray",
    "xgboost": "xgboost",
    "zarr": "zarr",
    "zstandard": "zstandard",
}

IMPORT_LINE = re.compile(r"^[ \t]*(?:import|from)[ \t]+([A-Za-z_]\w*)")
FILES_USE = re.compile(r"""["']\.{0,2}/?_files/""")


def code_sources(nb: dict) -> list[str]:
    return ["".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code"]


def uncommented(source: str) -> str:
    return "\n".join(re.sub(r"#.*$", "", line) for line in source.split("\n"))


def setup_source(nb: dict) -> str | None:
    """The generated setup cell for one notebook, or None if it needs nothing."""
    imported: set[str] = set()
    writes_files = False
    for source in code_sources(nb):
        for line in source.split("\n"):
            if line.lstrip().startswith(("!", "%")):
                continue
            m = IMPORT_LINE.match(line)
            if m:
                imported.add(m.group(1))
        if FILES_USE.search(uncommented(source)):
            writes_files = True

    needed = {mod: COLAB_PIP[mod] for mod in sorted(imported & COLAB_PIP.keys())}
    if not needed and not writes_files:
        return None

    lines = ["# --- environment setup (generated, not part of the lesson) ---"]
    if needed:
        lines.append("# Colab and Kaggle do not ship every package this notebook imports.")
    if writes_files:
        lines.append("# Colab and Kaggle start in an empty working directory.")
    lines.append("# This is a no-op in an environment that is already set up.")

    if needed:
        entries = ", ".join(f'"{mod}": "{pkg}"' for mod, pkg in needed.items())
        lines += [
            "import importlib.util",
            "import subprocess",
            "import sys",
            "",
            f"for module, package in {{{entries}}}.items():",
            "    if importlib.util.find_spec(module) is None:",
            '        subprocess.run([sys.executable, "-m", "pip", "install", "-q", package], check=True)',
        ]
    if writes_files:
        if needed:
            lines.append("")
        lines += [
            "from pathlib import Path",
            "",
            'Path("_files").mkdir(exist_ok=True)   # the folder this notebook writes into',
        ]
    return "\n".join(lines)


def strip_blank_edges(lines: list[str]) -> list[str]:
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def space_fences(lines: list[str]) -> list[str]:
    """Blank-line-separate fenced code from surrounding prose.

    MyST tolerated a fence flush against the paragraph above it; inside a
    <details> block a stricter renderer can swallow it, so put the blank line
    in rather than rely on that.
    """
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            if not in_fence and out and out[-1].strip():
                out.append("")
            out.append(line)
            in_fence = not in_fence
            continue
        if (
            not in_fence
            and line.strip()
            and out
            and out[-1].lstrip().startswith("```")
        ):
            out.append("")
        out.append(line)
    return out


def render_box(cls: str, title: str, body: list[str]) -> list[str]:
    """One admonition as markdown that renders anywhere."""
    marker = MARKERS.get(cls, DEFAULT_MARKER)
    title = title.strip().strip("*").strip() or cls.split()[0].capitalize()
    body = space_fences(strip_blank_edges(list(body)))

    if "dropdown" in cls.split():
        # Inside <summary> the backticks are HTML, not markdown, so spell the
        # code spans out. A blank line after <summary> is what lets the body
        # keep being parsed as markdown.
        summary = BACKTICK_SPAN.sub(r"<code>\1</code>", title)
        return [
            "<details>",
            f"<summary><b>{marker} {summary}</b></summary>",
            "",
            *body,
            "",
            "</details>",
            "",
        ]
    return [f"**{marker} {title}**", "", *body, ""]


def convert_admonitions(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = DIRECTIVE_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        fence, name, title = m.group(1), m.group(2), m.group(3)
        j = i + 1
        # `:::{admonition}` carries its role in a :class: option; `:::{hint}`
        # and friends carry it in the directive name itself.
        cls = name
        if j < len(lines):
            opt = CLASS_OPTION.match(lines[j])
            if opt:
                cls = opt.group(1).strip()
                j += 1

        body: list[str] = []
        while j < len(lines) and lines[j].rstrip() != fence:
            body.append(lines[j])
            j += 1
        if j >= len(lines):            # unterminated: leave the cell alone
            return text
        j += 1                          # step over the closing fence

        out.extend(render_box(cls, title, body))
        i = j
    return "\n".join(out)


def convert_figures(text: str, notebook_dir: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = FIGURE_OPEN.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue

        target = m.group(1)
        j = i + 1
        options: dict[str, str] = {}
        if j < len(lines) and lines[j].strip() == "---":
            j += 1
            while j < len(lines) and lines[j].strip() != "---":
                opt = OPTION_LINE.match(lines[j].strip())
                if opt:
                    options[opt.group(1)] = opt.group(2).strip()
                j += 1
            j += 1
        else:
            while j < len(lines) and lines[j].startswith(":"):
                opt = OPTION_LINE.match(lines[j].lstrip(":"))
                if opt:
                    options[opt.group(1)] = opt.group(2).strip()
                j += 1

        caption: list[str] = []
        while j < len(lines) and lines[j].rstrip() != "```":
            caption.append(lines[j])
            j += 1
        if j >= len(lines):            # unterminated: leave the cell alone
            return text
        j += 1

        # A relative target resolves against the notebook's own directory, so
        # the same `_static/x.jpg` works from part-I/ and from live/part-I/.
        if "://" in target:
            url = target
        else:
            url = f"{RAW_BASE}/{notebook_dir}/{target}".replace("/./", "/")

        width = options.get("width", "").strip()
        attrs = f'src="{url}"'
        if options.get("alt"):
            attrs += f' alt="{options["alt"]}"'
        if width:
            attrs += f' width="{width.removesuffix("px")}"'

        out.append(f"<img {attrs}>")
        caption = strip_blank_edges(caption)
        if caption:
            out.append("")
            out.append("<em>" + "\n".join(caption) + "</em>")
        out.append("")
        i = j
    return "\n".join(out)


def split_points(source: str) -> list[int]:
    """0-based line indices at which to start a new cell."""
    lines = source.split("\n")

    marked = [k for k, line in enumerate(lines) if SPLIT_MARKER.match(line)]
    if marked:
        return marked

    if len(strip_blank_edges(list(lines))) < SPLIT_MIN_LINES:
        return []
    if FIGURE_STATE.search(source):
        return []
    try:
        tree = ast.parse(source)
    except SyntaxError:      # magics, shell escapes
        return []

    cuts: list[int] = []
    for stmt in tree.body[1:]:
        start = min(
            [stmt.lineno] + [d.lineno for d in getattr(stmt, "decorator_list", [])]
        ) - 1
        # Carry any comment lines immediately above the statement with it.
        top = start
        while top > 0 and lines[top - 1].lstrip().startswith("#"):
            top -= 1
        if top > 0 and not lines[top - 1].strip():
            cuts.append(top)
    return cuts


def split_code_cell(cell: dict) -> list[str]:
    source = "".join(cell["source"]).rstrip("\n")
    if TAG_KEEP_WHOLE in cell.get("metadata", {}).get("tags", []):
        return [source]

    cuts = split_points(source)
    if not cuts:
        return [source]

    lines = source.split("\n")
    pieces: list[str] = []
    for start, end in zip([0] + cuts, cuts + [len(lines)]):
        chunk = [ln for ln in lines[start:end] if not SPLIT_MARKER.match(ln)]
        chunk = strip_blank_edges(chunk)
        if chunk:
            pieces.append("\n".join(chunk))
    return pieces or [source]


def as_source(text: str) -> list[str]:
    """Back to nbformat's line list, each line but the last newline-terminated."""
    return text.splitlines(keepends=True) if text else []


def convert(nb: dict, rel_path: Path) -> dict:
    notebook_dir = rel_path.parent.as_posix()
    cells: list[dict] = []

    header = (
        f"> Notebook-friendly copy of `{rel_path.as_posix()}`, generated by "
        f"`tools/make_live.py`. Edit the book notebook, not this file."
    )
    cells.append({"cell_type": "markdown", "metadata": {}, "source": as_source(header)})

    setup = setup_source(nb)
    if setup:
        cells.append(
            {
                "cell_type": "code",
                "metadata": {},
                "execution_count": None,
                "outputs": [],
                "source": as_source(setup),
            }
        )

    for cell in nb["cells"]:
        tags = cell.get("metadata", {}).get("tags", [])
        if TAG_DROP in tags:
            continue

        if cell["cell_type"] == "markdown":
            text = "".join(cell["source"])
            text = convert_admonitions(text)
            text = convert_figures(text, notebook_dir)
            text = text.strip("\n")
            if not text:
                continue
            cells.append(
                {"cell_type": "markdown", "metadata": {}, "source": as_source(text)}
            )
        elif cell["cell_type"] == "code":
            for piece in split_code_cell(cell):
                cells.append(
                    {
                        "cell_type": "code",
                        "metadata": {},
                        "execution_count": None,
                        "outputs": [],
                        "source": as_source(piece),
                    }
                )
        else:
            cells.append(cell)

    for n, cell in enumerate(cells):
        cell["id"] = f"live-{n:04d}"

    out = {k: v for k, v in nb.items() if k != "cells"}
    out["cells"] = cells
    return out


def render(path: Path) -> tuple[Path, str]:
    rel = path.relative_to(ROOT)
    nb = json.loads(path.read_text(encoding="utf-8"))
    live = convert(nb, rel)
    return LIVE_DIR / rel, json.dumps(live, indent=1, ensure_ascii=False) + "\n"


def sources(args: list[str]) -> list[Path]:
    if args:
        return [Path(a).resolve() for a in args]
    found: list[Path] = []
    for d in SOURCE_DIRS:
        found.extend(sorted((ROOT / d).glob("*.ipynb")))
    return found


def main(argv: list[str]) -> int:
    check = "--check" in argv
    paths = sources([a for a in argv if not a.startswith("--")])

    stale: list[Path] = []
    written = 0
    for path in paths:
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            return 2
        dest, text = render(path)
        if check:
            current = dest.read_text(encoding="utf-8") if dest.exists() else None
            if current != text:
                stale.append(dest.relative_to(ROOT))
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or dest.read_text(encoding="utf-8") != text:
            dest.write_text(text, encoding="utf-8")
            written += 1

    if check:
        if stale:
            print("live copies out of date (run tools/make_live.py):")
            for s in stale:
                print(f"  {s}")
            return 1
        print(f"{len(paths)} live copies up to date")
        return 0

    print(f"{len(paths)} notebooks processed, {written} live copies written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
