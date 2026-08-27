# Chapter 1: Introduction to Python for Earth and Environmental Sciences

This is the first chapter of the book; it covers the following subchapters. One further subchapter, held back as optional self-study material, lives in the [Bonus material](bonus.md) section after this chapter.

::::{grid} 1 1 2 2

:::{card} 1.1) Variables, Data Types, Operators, and File I/O
:link: 1.1-environment-and-data-types.ipynb

Variables, scalar types, casting, string formatting, and reading and writing text files.

:::

:::{card} 1.2) Data Structures and Control Flow
:link: 1.2-data-structures-and-control-flow.ipynb

Lists, tuples, and dicts, plus the control flow and functions that tie them together.

:::

:::{card} 1.3) Scientific Computing with Numpy
:link: 1.3-numpy.ipynb

The numpy array: creation, indexing, vectorised math, broadcasting, and reductions.

:::

:::{card} 1.4) Matplotlib and Xarray
:link: 1.4-matplotlib-and-xarray.ipynb

Building figures with matplotlib, and labelled, multi-dimensional arrays with xarray.

:::

:::{card} 1.5) Pandas
:link: 1.5-pandas.ipynb

Series and DataFrames: selecting, resampling, grouping, and handling missing data.

:::

:::{card} 1.6) Geospatial Vector Data with GeoPandas
:link: 1.6-geospatial-vector-data.ipynb

Points, lines, and polygons with geopandas: projections, joins, and measuring correctly.

:::

:::{card} 1.7) Object-oriented and defensive programming for environmental systems
:link: 1.7-oop-for-environmental-systems.ipynb

Bundling state and behaviour into classes, then reading and trusting code you didn't write — assertions, exceptions, logging, and tests.

:::

:::{card} 1.8) Statistical Foundations and the Machine-Learning Stepping-Stone
:link: 1.8-statistical-foundations-and-ml.ipynb

From descriptive statistics to a first, honestly evaluated regression, classification, and clustering model.

:::

::::

## Resources

Every subchapter above ends with its own short reading list, pointing at the specific tool or dataset just used. This section collects all of them in one place, and adds the resources worth knowing about for learning Python itself — at whatever level you are starting from.

### Learning Python: books and courses

**Getting started, no prior programming assumed**

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — Al Sweigart; free online. Practical, task-driven, and the resource already pointed to from subchapter 1.2.
- [Think Python](https://allendowney.github.io/ThinkPython/) — Allen Downey; free (the current edition is a set of runnable Jupyter notebooks). A slower, more conceptual first course than *Automate the Boring Stuff*, closer to how a first computer-science class is taught.
- [Python Crash Course](https://nostarch.com/python-crash-course-3rd-edition) — Eric Matthes (No Starch Press). The most widely used printed introduction; fast-paced and project-based, ending in small data-analysis, web, and game projects.
- [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official documentation's own introduction. Terser than a book, but authoritative and always current; already this book's own reference in subchapter 1.1.
- [Software Carpentry — Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) — a research-oriented introduction built around lists, loops, conditionals, and functions; already used throughout Part I.

**Comfortable with the basics, building fluency**

- [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/) — Jake VanderPlas; free. A fast second pass through the language for someone who already codes in something else, written explicitly as the on-ramp to the Data Science Handbook below.
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — Jake VanderPlas; free online. Covers numpy, pandas, matplotlib, and scikit-learn in real depth — arguably the single closest match to this part's own scope, and already this book's numpy resource in subchapter 1.3.
- [Effective Python](https://effectivepython.com/) — Brett Slatkin. Specific, well-explained practices for writing idiomatic Python once the basics are solid; the 3rd edition covers 125 of them.

**Going deeper**

- [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — Luciano Ramalho (O'Reilly). How Python's data model actually works underneath the syntax — for once the language feels comfortable and the question becomes *why*, not just *how*.

### The scientific Python stack

- [Python Data Science Handbook — Introduction to NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html) — arrays, broadcasting, masking, and ufuncs. (1.3)
- [Scientific Python Lectures — NumPy](https://lectures.scientific-python.org/intro/numpy/index.html) — a concise, research-oriented tour of the same material. (1.3)
- [Pythia Foundations — Matplotlib Basics](https://foundations.projectpythia.org/core/matplotlib/matplotlib-basics/) — the figure/axes model and the core plot types. (1.4)
- [Pythia Foundations — Introduction to Xarray](https://foundations.projectpythia.org/core/xarray/xarray-intro/) — DataArray/Dataset, label-based selection, built-in plotting. (1.4)
- [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/) — Abernathey and Key; numpy, matplotlib, and xarray on real geoscience data. (1.4)
- [Python for Data Analysis, 3rd ed. — Getting Started with pandas](https://wesmckinney.com/book/pandas-basics) — McKinney; Series/DataFrame mechanics and data cleaning. (1.5)
- [pandas — Getting started](https://pandas.pydata.org/docs/getting_started/index.html) — the official task-oriented tutorials. (1.5)

### Geospatial data

- [GeoPandas — Managing projections](https://geopandas.org/en/stable/docs/user_guide/projections.html) — setting and transforming coordinate reference systems. (1.6)
- [GeoPandas basics: maps, projections, and spatial joins](https://realpython.com/geopandas/) — a worked introduction to GeoDataFrames and spatial joins. (1.6)

### Object-oriented and defensive programming

- [Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/) — classes, instances, attributes, methods, inheritance. (1.7)
- [Python Classes: The Power of Object-Oriented Programming](https://realpython.com/python-classes/) — instance vs. class attributes, dataclasses, and when *not* to use a class. (1.7)
- [pytest documentation](https://docs.pytest.org/en/stable/) — writing tests, fixtures, parametrisation. (1.7)

### Machine learning and statistical graphics

- [scikit-learn — Getting started](https://scikit-learn.org/stable/getting_started.html) — the estimator interface, train/test evaluation, pipelines. (1.8)
- [seaborn](https://seaborn.pydata.org/) — statistical visualisation on dataframes. (1.8)
- [scikit-learn — Clustering](https://scikit-learn.org/stable/modules/clustering.html) and [Decomposing signals (PCA)](https://scikit-learn.org/stable/modules/decomposition.html#pca) — k-means and PCA reference documentation. (1.8)
- [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) — Horst, Hill & Gorman (2020); the real dataset behind 1.8's clustering and PCA content. (1.8)

### Reproducibility and tooling

- [Project Pythia Foundations](https://foundations.projectpythia.org/) — geoscience-flavoured tutorials across the whole scientific-python stack; a natural next step after this part. (1.1)
- [uv documentation](https://docs.astral.sh/uv/) — project creation, the src layout, dependency management. (Bonus A)
- [Ruff documentation](https://docs.astral.sh/ruff/) — the linter and formatter used in Bonus A's going-deeper boxes. (Bonus A)
- [pooch documentation](https://www.fatiando.org/pooch/latest/) — retrieving single files, registries, hashing, DOI downloads. (Bonus A)
- [Earth and Environmental Data Science — All About Data](https://earth-env-data-science.github.io/lectures/data.html) — Abernathey and Key on fetching remote data, Zenodo DOIs, FAIR practice. (Bonus A)
