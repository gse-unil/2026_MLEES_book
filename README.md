# Machine Learning for Earth and Environmental Sciences

[![Deploy](https://github.com/gse-unil/2026_MLEES_book/actions/workflows/deploy.yml/badge.svg)](https://github.com/gse-unil/2026_MLEES_book/actions/workflows/deploy.yml)
[![Book](https://img.shields.io/badge/read-the%20book-blue)](https://gse-unil.github.io/2026_MLEES_book/)
[![License: CC BY 4.0](https://img.shields.io/badge/content-CC--BY--4.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

An open, interactive textbook on scientific Python and machine learning for the Earth and environmental sciences. Every concept is taught against real geoscientific data — reanalysis fields, satellite imagery, hydrological records, earthquake catalogues — so that methods are learned in the context where they are actually used.

The book is course material for the *Machine Learning for Earth and Environmental Sciences* (MLEES) course at the University of Lausanne, and is freely available to anyone.

📖 **Read it here: <https://gse-unil.github.io/2026_MLEES_book/>**

---

## About

The book is designed for a wide range of backgrounds. Part I assumes no prior programming experience and builds scientific Python from the ground up, while offering optional depth for readers who want more. Later parts move from classical machine learning to deep learning and on to topics in trustworthy and physics-aware modelling, always anchored in environmental applications.

Broadly, it covers:

- **Part I — Scientific Python.** Programming foundations, the numerical and data stack (`numpy`, `pandas`, `xarray`, `matplotlib`), and reproducible, cloud-native data workflows for gridded geoscientific data.
- **Part II — Machine learning.** Regression and classification, model evaluation, unsupervised methods, and the bridge from classical estimators to neural networks.
- **Part III — Deep learning and applications.** Neural networks in PyTorch, architectures for spatial and sequential geoscientific data, and applications such as remote sensing, downscaling, and emulation, alongside explainability and uncertainty quantification.

The exact chapter list is defined in [`myst.yml`](myst.yml) and reflected in the site navigation.

---

## Reading and running the material

The simplest way to use the book is to read it online at the link above — all code and figures are rendered in place.

To run a notebook yourself, either open it in the cloud (look for the launch badge on each page) or work locally by cloning this repository and following the setup below. The notebooks are designed to run on modest hardware; large datasets are streamed from cloud storage rather than downloaded.

---

## Local development

You need [git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/). To get a live local preview:

```bash
git clone git@github.com:gse-unil/2026_MLEES_book.git
cd 2026_MLEES_book
uv sync                          # create the pinned environment
uv run jupyter book start        # live preview, reloads as you edit
```

To reproduce the static build that CI publishes:

```bash
uv run jupyter book build --html
```

Node.js is not required for authoring; the MyST engine installs it on first build if needed. Full details — the git workflow, notebook rules, data handling, and writing conventions — are in [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## How it is built

The book is a [Jupyter Book 2](https://jupyterbook.org) project built on the [MyST](https://mystmd.org) document engine. The repository contains only source — notebooks, markdown, configuration, and references. On every push to `main`, a [GitHub Actions workflow](.github/workflows/deploy.yml) builds the site and deploys it to GitHub Pages. Built output is never committed.

---

## Contributing

Contributions are welcome, from fixing a typo to authoring a new chapter. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request — it explains the environment, the branch-and-PR workflow, the all-important rule for committing notebook outputs, and the book's editorial conventions. For larger changes, open an issue first so we can agree on the approach.

---

## How to cite

If you use this book in teaching or research, please cite it. <!-- TODO: confirm authors, year, and add a DOI (e.g. via Zenodo) -->

```bibtex
@book{mlees,
  title     = {Machine Learning for Earth and Environmental Sciences},
  author    = {Beucler, Tom and others},
  year      = {2026},
  publisher = {University of Lausanne},
  url       = {https://gse-unil.github.io/2026_MLEES_book/},
  note      = {Open educational resource}
}
```

---

## License

<!-- TODO: confirm and adjust to the license we actually want. -->
Unless stated otherwise, prose and figures are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and code under the [MIT License](LICENSE). Add the corresponding `LICENSE` file(s) to the repository root.

---

## Authors and acknowledgements

Developed by Tom Beucler and the MLEES course team at the University of Lausanne, with contributions from the wider community. <!-- TODO: list maintainers and contributors -->