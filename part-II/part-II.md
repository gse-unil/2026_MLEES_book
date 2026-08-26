# (Part II) Basics of Machine Learning for Earth and Environmental Science

## Introduction

Part II moves from the general-purpose Python and scientific-computing tools built in Part I to
machine learning itself: fitting models, evaluating them honestly, and applying them to real
environmental problems. It assumes Part I throughout — numpy, pandas, and the scikit-learn
estimator interface introduced there are used without re-explanation.

Three chapters carry the through-line. Chapter 2 covers linear regression for regression tasks
and logistic regression for classification, closing with statistical forecasting applied to
environmental time series. Chapter 3 turns to decision trees, random forests, and support vector
machines, applied to an environmental risk-mapping problem. Chapter 4 covers unsupervised
learning — dimensionality reduction and clustering — applied to identifying regimes in oceanic
data.

Each chapter pairs one tutorial notebook with several standalone exercise notebooks, rather than
Part I's one-lecture-one-exercises structure — a shape carried over from the material this part
is built on. Exercises adapt notebooks from Géron's *Hands-On Machine Learning with Scikit-Learn*
and, for the statistical-forecasting material, Wilks' *Statistical Methods in the Atmospheric
Sciences*, applied throughout to real environmental datasets: handwritten digits, Titanic
passenger records, Palmer Archipelago penguins, Ecuadorian pressure and temperature readings, and
El Niño years.