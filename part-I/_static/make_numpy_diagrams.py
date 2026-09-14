"""
Generates the 11 static diagrams embedded in part-I/1.3-numpy.ipynb via {figure} blocks.
Original artwork built from the lecture's own temp_celsius (4, 6) example -- not copied
from numpy's docs (those illustrations are third-party, CC BY-NC-SA) or any other source.

Run: uv run python edits_from_previous/make_numpy_diagrams.py
Writes PNGs directly into part-I/_static/.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUT = str(Path(__file__).resolve().parent.parent / "part-I" / "_static")

EDGE = "#333333"
BASE = "#f0f0f0"

temp_celsius = np.array([
    [ 5.2,  4.8,  6.1,  3.9,  2.7,  4.4],
    [ 1.3,  0.5, -0.8, -1.2,  0.9,  2.1],
    [-2.6, -3.1, -1.9,  0.2, -0.5,  1.1],
    [ 6.4,  7.0,  5.5,  8.1,  4.2,  5.8],
])


def draw_grid(ax, data, highlight=None, color="tab:blue", fontsize=9):
    """Draw a 1D or 2D array as a grid of labelled cells; `highlight` (same shape) marks cells to colour."""
    data = np.atleast_2d(data)
    hi = np.atleast_2d(highlight) if highlight is not None else None
    nrows, ncols = data.shape
    for r in range(nrows):
        for c in range(ncols):
            selected = hi is not None and hi[r, c]
            face = color if selected else BASE
            ax.add_patch(mpatches.Rectangle((c, nrows - 1 - r), 1, 1, facecolor=face, edgecolor=EDGE))
            try:
                label = f"{float(data[r, c]):.1f}"
            except (TypeError, ValueError):
                label = str(data[r, c])
            ax.text(c + 0.5, nrows - 1 - r + 0.5, label,
                    ha="center", va="center", fontsize=fontsize,
                    color="white" if selected else "black")
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_aspect("equal")
    ax.axis("off")


def arrow_between(fig, ax_left, ax_right, label, fontsize=9, y_off=0.03):
    fig.canvas.draw()
    bbox_l = ax_left.get_position(); bbox_r = ax_right.get_position()
    x = (bbox_l.x1 + bbox_r.x0) / 2
    y = (bbox_l.y0 + bbox_l.y1) / 2
    ax_left.annotate(
        "", xy=(bbox_r.x0, y), xytext=(bbox_l.x1, y),
        xycoords="figure fraction", textcoords="figure fraction",
        arrowprops=dict(arrowstyle="->", color="#444444", linewidth=1.4),
    )
    fig.text(x, y + y_off, label, fontsize=fontsize, family="monospace", ha="center", va="bottom")


def symbol_between(fig, ax_left, ax_right, symbol, fontsize=20):
    fig.canvas.draw()
    bbox_l = ax_left.get_position(); bbox_r = ax_right.get_position()
    x = (bbox_l.x1 + bbox_r.x0) / 2
    y = (bbox_l.y0 + bbox_l.y1) / 2
    fig.text(x, y, symbol, fontsize=fontsize, ha="center", va="center")


def vertical_arrow_between(fig, ax_top, ax_bottom, label, fontsize=10):
    fig.canvas.draw()
    bbox_t = ax_top.get_position(); bbox_b = ax_bottom.get_position()
    x = (bbox_t.x0 + bbox_t.x1) / 2
    ax_top.annotate(
        "", xy=(x, bbox_b.y1), xytext=(x, bbox_t.y0),
        xycoords="figure fraction", textcoords="figure fraction",
        arrowprops=dict(arrowstyle="->", color="#444444", linewidth=1.4),
    )
    y = (bbox_t.y0 + bbox_b.y1) / 2
    fig.text(x + 0.12, y, label, fontsize=fontsize, family="monospace", ha="left", va="center")


def add_axis_labels(ax, nrows, ncols, show_axis0=True, show_axis1=True, pad=0.5):
    """Draw axis=0 (down, through rows) and/or axis=1 (right, through columns) arrows
    directly on a grid already drawn by draw_grid, tying the axis number to its physical
    direction on the array."""
    if show_axis1:
        ax.annotate("", xy=(ncols, nrows + pad), xytext=(0, nrows + pad),
                    arrowprops=dict(arrowstyle="->", color="#444444", linewidth=1.2))
        ax.text(ncols / 2, nrows + pad + 0.15, "axis=1", ha="center", va="bottom",
                fontsize=9, family="monospace")
    if show_axis0:
        ax.annotate("", xy=(-pad, 0), xytext=(-pad, nrows),
                    arrowprops=dict(arrowstyle="->", color="#444444", linewidth=1.2))
        ax.text(-pad - 0.15, nrows / 2, "axis=0", ha="right", va="center",
                fontsize=9, family="monospace", rotation=90)
    ax.set_xlim(-pad - 0.9 if show_axis0 else -0.2, ncols + 0.3)
    ax.set_ylim(-0.3, nrows + (pad + 0.5 if show_axis1 else 0.2))


# ---------------------------------------------------------------------------
# 1. Array creation: temp_celsius with shape and ndim
# ---------------------------------------------------------------------------
def make_array_creation():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    draw_grid(ax, temp_celsius, fontsize=10)
    add_axis_labels(ax, 4, 6)
    ax.set_title("temp_celsius", fontsize=12, family="monospace", pad=28)
    fig.text(0.5, 0.04, f"shape: {temp_celsius.shape}    |    ndim: {temp_celsius.ndim}",
              fontsize=11, family="monospace", ha="center")
    fig.subplots_adjust(bottom=0.2, top=0.82)
    fig.savefig(f"{OUT}/numpy_array_creation.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 2. Indexing: 4-panel, 2x2
# ---------------------------------------------------------------------------
def make_indexing_4panel():
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.5))

    hi = np.zeros_like(temp_celsius, dtype=bool); hi[0, 0] = True
    draw_grid(axes[0, 0], temp_celsius, hi)
    axes[0, 0].set_title("temp_celsius[0, 0]", fontsize=11, family="monospace", pad=8)

    hi = np.zeros_like(temp_celsius, dtype=bool); hi[0, :] = True
    draw_grid(axes[0, 1], temp_celsius, hi)
    axes[0, 1].set_title("temp_celsius[0, :]", fontsize=11, family="monospace", pad=8)

    hi = np.zeros_like(temp_celsius, dtype=bool); hi[:, -1] = True
    draw_grid(axes[1, 0], temp_celsius, hi)
    axes[1, 0].set_title("temp_celsius[:, -1]", fontsize=11, family="monospace", pad=8)

    hi = np.zeros_like(temp_celsius, dtype=bool); hi[1:3, 2:4] = True
    draw_grid(axes[1, 1], temp_celsius, hi)
    axes[1, 1].set_title("temp_celsius[1:3, 2:4]", fontsize=11, family="monospace", pad=8)

    fig.tight_layout()
    fig.savefig(f"{OUT}/numpy_indexing_4panel.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Boolean mask: mask / selected-in-place / 1D result
# ---------------------------------------------------------------------------
def make_boolean_mask():
    freezing = temp_celsius < 0.0
    result_1d = temp_celsius[freezing]   # (6,)

    fig = plt.figure(figsize=(13, 3.6))
    fig.subplots_adjust(top=0.72, bottom=0.18)
    axes = fig.subplots(1, 3, gridspec_kw={"width_ratios": [6, 6, 6]})

    mask_labels = np.where(freezing, "True", "False")
    draw_grid(axes[0], mask_labels, freezing, fontsize=8)
    axes[0].set_title("freezing = temp_celsius < 0.0", fontsize=10, family="monospace", pad=8)

    draw_grid(axes[1], temp_celsius, freezing)
    axes[1].set_title("temp_celsius[freezing]\nselects these cells", fontsize=10, family="monospace", pad=8)

    draw_grid(axes[2], result_1d[None, :], np.ones((1, result_1d.size), dtype=bool))
    axes[2].set_title("temp_celsius[freezing]\n-> 1D array, shape (6,)", fontsize=10, family="monospace", pad=8)

    for a, b, sym in [(axes[0], axes[1], "->"), (axes[1], axes[2], "->")]:
        symbol_between(fig, a, b, sym, fontsize=16)

    fig.text(0.5, 0.05, f"n freezing cells: {int(freezing.sum())}",
              fontsize=11, family="monospace", ha="center")
    fig.savefig(f"{OUT}/numpy_boolean_mask.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Vectorized addition: array + scalar -> array, "no for loop needed"
# ---------------------------------------------------------------------------
def make_vectorized_add():
    temp_kelvin = temp_celsius + 273.15

    fig = plt.figure(figsize=(11, 4.8))
    fig.subplots_adjust(top=0.62, bottom=0.14)
    axes = fig.subplots(1, 3, gridspec_kw={"width_ratios": [6, 1.6, 6]})

    hi = np.zeros_like(temp_celsius, dtype=bool)
    hi[0, 0] = True
    draw_grid(axes[0], temp_celsius, hi, color="tab:red")
    axes[0].set_title("temp_celsius", fontsize=11, family="monospace", pad=8)

    axes[1].axis("off")
    axes[1].text(0.5, 0.5, "+ 273.15\n=", fontsize=13, family="monospace",
                 ha="center", va="center", transform=axes[1].transAxes)

    draw_grid(axes[2], temp_kelvin, hi, color="tab:red")
    axes[2].set_title("temp_kelvin", fontsize=11, family="monospace", pad=8)

    # a worked example: the same top-left cell in both grids, connected by a curved
    # arrow arcing above -- makes concrete what "every cell updates" means for one cell
    con = mpatches.ConnectionPatch(
        xyA=(0.5, 3.92), coordsA=axes[0].transData,
        xyB=(0.5, 3.92), coordsB=axes[2].transData,
        connectionstyle="arc3,rad=-0.4", arrowstyle="->",
        color="tab:red", linewidth=1.3, mutation_scale=15,
    )
    fig.add_artist(con)
    fig.text(0.5, 0.85, "5.2 + 273.15 = 278.35", fontsize=10, family="monospace",
              color="tab:red", ha="center")

    fig.text(0.5, 0.04, "no for loop needed -- every cell updates at once",
              fontsize=11, ha="center", style="italic")
    fig.savefig(f"{OUT}/numpy_vectorized_add.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 5. Impossible broadcasting: (4, 6) vs (4,)
# ---------------------------------------------------------------------------
def make_broadcast_impossible():
    lat_gradient_celsius = np.array([0.0, -1.5, -3.0, -4.5])

    fig = plt.figure(figsize=(9, 3.6))
    fig.subplots_adjust(top=0.72, bottom=0.2)
    axes = fig.subplots(1, 2, gridspec_kw={"width_ratios": [6, 4]})

    draw_grid(axes[0], temp_celsius)
    axes[0].set_title("temp_celsius  (4, 6)", fontsize=11, family="monospace", pad=8)

    draw_grid(axes[1], lat_gradient_celsius, color="tab:red")
    axes[1].set_title("lat_gradient_celsius  (4,)", fontsize=11, family="monospace", pad=8)

    fig.canvas.draw()
    bbox_l = axes[0].get_position(); bbox_r = axes[1].get_position()
    x = (bbox_l.x1 + bbox_r.x0) / 2
    y = (bbox_l.y0 + bbox_l.y1) / 2
    fig.text(x, y, "✗", fontsize=26, color="tab:red", ha="center", va="center")

    fig.text(0.5, 0.06, "last axis: 6 != 4 -- ValueError, shapes cannot broadcast",
              fontsize=10.5, family="monospace", ha="center", color="tab:red")
    fig.savefig(f"{OUT}/numpy_broadcast_impossible.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 6. Broadcasting result: (4, 6) + (4, 1) -> (4, 6)
# ---------------------------------------------------------------------------
def make_broadcast_result():
    lat_gradient_celsius = np.array([0.0, -1.5, -3.0, -4.5])
    lat_col = lat_gradient_celsius[:, None]
    adjusted = temp_celsius + lat_col

    fig = plt.figure(figsize=(11, 5.6))
    fig.subplots_adjust(top=0.52, bottom=0.05)
    axes = fig.subplots(1, 3, gridspec_kw={"width_ratios": [6, 1, 6]})

    # highlight the first column in both temp_celsius and adjusted, to trace one
    # concrete column through the broadcast
    col0 = np.zeros_like(temp_celsius, dtype=bool)
    col0[:, 0] = True

    draw_grid(axes[0], temp_celsius, col0, color="tab:red")
    axes[0].set_title("temp_celsius  (4, 6)", fontsize=10, family="monospace")

    draw_grid(axes[1], lat_col, highlight=np.ones_like(lat_col, dtype=bool), color="tab:orange")
    axes[1].set_title("lat_gradient_celsius\n[:, None]  (4, 1)", fontsize=8.5, family="monospace")

    draw_grid(axes[2], adjusted, col0, color="tab:red")
    axes[2].set_title("adjusted  (4, 6)", fontsize=10, family="monospace")

    symbol_between(fig, axes[0], axes[1], "+")
    symbol_between(fig, axes[1], axes[2], "=")

    # one column traced through: same first column, connected by a curved arrow
    # arcing above the whole figure
    con = mpatches.ConnectionPatch(
        xyA=(0.5, 3.95), coordsA=axes[0].transData,
        xyB=(0.5, 3.95), coordsB=axes[2].transData,
        connectionstyle="arc3,rad=-0.55", arrowstyle="->",
        color="tab:red", linewidth=1.3, mutation_scale=15,
    )
    fig.add_artist(con)
    fig.text(0.5, 0.86, "temp_celsius[:, 0] + lat_gradient_celsius[:, None] = adjusted[:, 0]",
              fontsize=9.5, family="monospace", color="tab:red", ha="center")

    fig.suptitle("A (4, 1) column stretches across the 6 longitudes", fontsize=11, y=0.98)
    fig.savefig(f"{OUT}/numpy_broadcast_result.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 7. mean() and sum(): array -> scalar
# ---------------------------------------------------------------------------
def make_mean_sum():
    fig = plt.figure(figsize=(10, 3.4))
    fig.subplots_adjust(top=0.72, bottom=0.08)
    axes = fig.subplots(1, 4, gridspec_kw={"width_ratios": [6, 1.2, 6, 1.2]})

    draw_grid(axes[0], temp_celsius)
    axes[0].set_title("temp_celsius", fontsize=10, family="monospace")
    val = np.array([[temp_celsius.mean()]])
    draw_grid(axes[1], val, np.ones((1, 1), dtype=bool), color="tab:green")
    axes[1].set_title(".mean()", fontsize=9, family="monospace")
    arrow_between(fig, axes[0], axes[1], "")

    draw_grid(axes[2], temp_celsius)
    axes[2].set_title("temp_celsius", fontsize=10, family="monospace")
    val = np.array([[temp_celsius.sum()]])
    draw_grid(axes[3], val, np.ones((1, 1), dtype=bool), color="tab:green")
    axes[3].set_title(".sum()", fontsize=9, family="monospace")
    arrow_between(fig, axes[2], axes[3], "")

    fig.savefig(f"{OUT}/numpy_mean_sum.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 8. Reductions by axis: col_means (row) and row_means (row)
# ---------------------------------------------------------------------------
def make_reductions_axis():
    col_means = temp_celsius.mean(axis=0)
    row_means = temp_celsius.mean(axis=1)

    fig = plt.figure(figsize=(11, 6))
    outer = fig.add_gridspec(2, 2, width_ratios=[6, 6], height_ratios=[1, 1], hspace=1.1, wspace=0.4)

    ax_main1 = fig.add_subplot(outer[0, 0])
    draw_grid(ax_main1, temp_celsius)
    add_axis_labels(ax_main1, 4, 6, show_axis0=True, show_axis1=False)
    ax_main1.set_title("temp_celsius  (4, 6)", fontsize=10, family="monospace", pad=10)
    ax_res1 = fig.add_subplot(outer[0, 1])
    draw_grid(ax_res1, col_means[None, :])
    ax_res1.set_title("col_means  (6,)", fontsize=10, family="monospace")
    arrow_between(fig, ax_main1, ax_res1, "mean(axis=0)")

    ax_main2 = fig.add_subplot(outer[1, 0])
    draw_grid(ax_main2, temp_celsius)
    add_axis_labels(ax_main2, 4, 6, show_axis0=False, show_axis1=True)
    ax_main2.set_title("temp_celsius  (4, 6)", fontsize=10, family="monospace", pad=28)
    ax_res2 = fig.add_subplot(outer[1, 1])
    draw_grid(ax_res2, row_means[None, :])
    ax_res2.set_title("row_means  (4,), shown as a row", fontsize=10, family="monospace")
    arrow_between(fig, ax_main2, ax_res2, "mean(axis=1)")

    fig.suptitle("temp_celsius.mean(axis=0) and temp_celsius.mean(axis=1)", fontsize=12, y=0.98)
    fig.savefig(f"{OUT}/numpy_reductions_axis.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 9. reshape(-1)
# ---------------------------------------------------------------------------
def make_reshape():
    flat = temp_celsius.reshape(-1)

    fig = plt.figure(figsize=(9, 5.2))
    outer = fig.add_gridspec(2, 1, height_ratios=[1.6, 1], hspace=0.7, top=0.93, bottom=0.12)
    ax_main = fig.add_subplot(outer[0])
    draw_grid(ax_main, temp_celsius)
    ax_main.set_title("temp_celsius  (4, 6)", fontsize=11, family="monospace")

    ax_res = fig.add_subplot(outer[1])
    draw_grid(ax_res, flat[None, :], fontsize=7)

    fig.canvas.draw()
    bbox_t = ax_main.get_position(); bbox_b = ax_res.get_position()
    x = (bbox_t.x0 + bbox_t.x1) / 2
    ax_main.annotate(
        "", xy=(x, bbox_b.y1 + 0.03), xytext=(x, bbox_t.y0 - 0.02),
        xycoords="figure fraction", textcoords="figure fraction",
        arrowprops=dict(arrowstyle="->", color="#444444", linewidth=1.4),
    )
    y_mid = (bbox_t.y0 + bbox_b.y1) / 2
    fig.text(x + 0.03, y_mid, "reshape(-1)", fontsize=10, family="monospace", ha="left", va="center")
    fig.text((bbox_b.x0 + bbox_b.x1) / 2, bbox_b.y0 - 0.06, "flat  (24,)",
              fontsize=10, family="monospace", ha="center", va="top")

    fig.savefig(f"{OUT}/numpy_reshape.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 10. vstack
# ---------------------------------------------------------------------------
def make_vstack():
    col_means = temp_celsius.mean(axis=0)
    index_row = np.arange(6, dtype=float)
    stacked = np.vstack([index_row, col_means])

    fig = plt.figure(figsize=(10, 4))
    outer = fig.add_gridspec(1, 3, width_ratios=[6, 1.4, 6], top=0.8, bottom=0.1)

    left_gs = outer[0].subgridspec(2, 1, hspace=0.7)
    ax_a = fig.add_subplot(left_gs[0])
    draw_grid(ax_a, index_row[None, :])
    ax_a.set_title("index_row  (6,)", fontsize=9, family="monospace")
    ax_b = fig.add_subplot(left_gs[1])
    draw_grid(ax_b, col_means[None, :])
    ax_b.set_title("col_means  (6,)", fontsize=9, family="monospace")

    ax_mid = fig.add_subplot(outer[1])
    ax_mid.axis("off")
    ax_mid.text(0.5, 0.5, "vstack\n->", fontsize=13, family="monospace", ha="center", va="center",
                transform=ax_mid.transAxes)

    ax_res = fig.add_subplot(outer[2])
    draw_grid(ax_res, stacked)
    ax_res.set_title("stacked  (2, 6)", fontsize=10, family="monospace")

    fig.suptitle("np.vstack([index_row, col_means])", fontsize=11, y=0.95)
    fig.savefig(f"{OUT}/numpy_vstack.png", dpi=200, transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 11. np.where and NaN
# ---------------------------------------------------------------------------
def make_where_nan():
    category = np.where(temp_celsius < 0.0, "freezing", "above")
    temp_with_gaps = temp_celsius.copy()
    temp_with_gaps[0, 0] = np.nan

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.4))
    draw_grid(axes[0], category, category == "freezing", fontsize=7)
    axes[0].set_title('np.where(temp_celsius < 0,\n"freezing", "above")', fontsize=9, family="monospace")

    draw_grid(axes[1], temp_with_gaps, np.isnan(temp_with_gaps), color="tab:red")
    axes[1].set_title("temp_with_gaps\n(NaN at [0, 0])", fontsize=9, family="monospace")

    fig.tight_layout()
    fig.savefig(f"{OUT}/numpy_where_nan.png", dpi=200, transparent=True)
    plt.close(fig)


if __name__ == "__main__":
    make_array_creation()
    make_indexing_4panel()
    make_boolean_mask()
    make_vectorized_add()
    make_broadcast_impossible()
    make_broadcast_result()
    make_mean_sum()
    make_reductions_axis()
    make_reshape()
    make_vstack()
    make_where_nan()
    print("done")
