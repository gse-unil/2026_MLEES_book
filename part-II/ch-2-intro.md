# Chapter 2: Linear Regression for Regression, Logistic Regression for Classification and Statistical Forecasting

This chapter covers linear regression for regression problems and logistic regression for
classification problems, closing with statistical forecasting applied to environmental time
series.

::::{grid} 1 1 2 2

:::{card} 2.1) Classification and Regression
:link: 2.1-classification-and-regression.ipynb

Classification vs. regression, cost functions, gradient descent, and the metrics used to
evaluate a classifier.

:::

:::{card} 2.2) (Exercises) Classification
:link: 2.2-classification-exercises.ipynb

Tuning a k-nearest-neighbours classifier on MNIST digits with grid search, then a random forest
and a support-vector classifier on the Titanic dataset.

:::

:::{card} 2.3) (Exercises) Training Models
:link: 2.3-training-models-exercises.ipynb

Implementing logistic regression from scratch — the logistic function, log loss, and gradient
descent — on Palmer penguin bill measurements.

:::

:::{card} 2.4) Statistical Forecasting in Environmental Sciences
:link: 2.4-statistical-forecasting-in-environmental-sciences.ipynb

Regression as a forecasting tool: feature selection, postprocessing, prediction intervals, and
model output statistics.

:::

:::{card} 2.5) (Exercises) Statistical Forecasting
:link: 2.5-statistical-forecasting-exercises.ipynb

Fitting a linear regression to real pressure and temperature readings, then a logistic
regression to classify El Niño years.

:::

::::

## Resources

### Textbooks this chapter's exercises adapt

- [Hands-On Machine Learning with Scikit-Learn](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) — Aurélien Géron; the source of the classification and training-models exercises. (2.2, 2.3)
- [Statistical Methods in the Atmospheric Sciences](https://www.elsevier.com/books/statistical-methods-in-the-atmospheric-sciences/wilks/978-0-12-815823-4) — Wilks; the source of the pressure/temperature data used in the statistical-forecasting exercise. (2.5)

### Scikit-learn

- [Getting started](https://scikit-learn.org/stable/getting_started.html) — the estimator interface, fit/predict, pipelines. (2.1–2.5)
- [Model selection: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) — hyperparameter search with cross-validation. (2.2)
- [Metrics and scoring](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) — accuracy, log loss, and the other classification metrics used throughout. (2.1, 2.2)

### Datasets

- [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) — Horst, Hill & Gorman (2020); the real dataset behind the from-scratch logistic regression. (2.3)
- [MNIST](https://en.wikipedia.org/wiki/MNIST_database) and [the Titanic dataset](https://www.kaggle.com/c/titanic) — the two real datasets behind the classification exercises. (2.2)
