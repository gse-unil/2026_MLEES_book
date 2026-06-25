# Machine Learning for Earth and Environmental Sciences

Welcome. This is a hands-on, open textbook about using scientific Python and
machine learning to study the Earth and its environment. It is built for a wide
range of readers — from someone opening a code editor for the very first time to
a researcher who wants to bring modern methods into their work — and every idea
is taught against real geoscientific data rather than toy examples, so that you
learn each tool in the setting where it is actually used.

:::{admonition} This book is under active development
:class: note
This is the fall 2026 edition of this book. Chapters are being written and refreshed. Expect content to grow and change.
If you spot an error or have a suggestion, see [how to contribute](CONTRIBUTING.md). Previous versions of this book are available at (#TODO: add link to previous versions.)
:::

## Who this book is for

No prior programming experience is assumed. Part I builds Python from the ground
up, carefully and from zero. At the same time, the book is meant to stay
interesting for readers who already know how to code: the harder material is
always within reach, just one step off the main path.

If you have a background in the environmental sciences and want to add
computation and machine learning to your toolkit, or a background in computing
and want to apply it to the Earth sciences, you are in the right place.

## How to use this book

**Two speeds, one page.** The main flow is the *core path*: read it straight
through and you will not miss anything essential. Alongside it you will find
collapsible **"Going deeper"** boxes holding optional material — the *why* behind
the *how*. Open them when you are curious; skip them with no loss of continuity.
This lets the same chapter serve a complete beginner and a motivated reader at
once.

**Everything runs.** Most pages are live notebooks. You can read them here as
rendered text and figures, or run them yourself — launch a page in google Colab using the badge icon at the top, or clone the
[repository](https://github.com/gse-unil/2026_MLEES_book) and run it locally. The
best way to learn is to change a value, re-run, and see what happens.

**Learn against real data.** Rather than a new toy dataset per topic, the book
keeps returning to real environmental data — near-surface temperature, satellite
imagery, hydrological and seismic records — so that methods accumulate into
something you could actually use in research.

## What's inside

::::{grid} 1 1 2 2
:gutter: 3

:::{card} Part I — Scientific Python
:link: part-I/part-I
Programming foundations from zero, the numerical and data stack
(`numpy`, `pandas`, `xarray`, `matplotlib`), plotting and maps, and reproducible,
cloud-native workflows for gridded geoscientific data.
:::

:::{card} Part II — Basics of Machine Learning for Earth and Environmental Sciences
:link: part-II/part-II
Regression and classification, honest model evaluation, unsupervised methods,
and the bridge from classical estimators to neural networks — each grounded in an
environmental problem.
:::

:::{card} Part III — Deep Learning for the Geosciences
:link: part-III/part-III
Neural networks in PyTorch, architectures for spatial and sequential data, and
applications such as remote sensing, downscaling, and emulation, alongside
explainability and uncertainty quantification.
:::

:::{card} Part IV — Towards Thustworthy AI
:link: part-IV/part-IV
Neural networks in PyTorch, architectures for spatial and sequential data, and
applications such as remote sensing, downscaling, and emulation, alongside
explainability and uncertainty quantification.
:::

:::{card} How to contribute
:link: CONTRIBUTING.md
The book is open. Fixing a typo or authoring a chapter — the contributor guide
explains the workflow and conventions. (# TODO: Check for GitHub restrictions)
:::

::::

## Before you start

For Part I you need nothing but a web browser; the Google Colab option to run the notebooks requires
only a free google account. To run the book on your own machine, you need
[git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/) — the
[setup instructions](CONTRIBUTING.md) walk you through it. A little familiarity
with the command line helps but is not required.

---

*This book is course material for the* Machine Learning for Earth and
Environmental Sciences *course at the University of Lausanne, and is released as
an open educational resource. See the
[repository](https://github.com/gse-unil/2026_MLEES_book) for license, citation,
and acknowledgements.*
