# Chapter 3: Decision Trees, Random Forests, Support Vector Machines and Environmental Risk Analysis

This chapter introduces three classical classifiers — support vector machines, decision trees,
and random forests/ensembles — then applies them to a real environmental risk-mapping problem:
wildfire susceptibility in the Liguria region of Italy.

::::{grid} 1 1 2 2

:::{card} 3.1) Basic Machine Learning Algorithms for Classification Tasks
:link: 3.1-simple-machine-learning-algorithms.ipynb

Support vector machines, decision trees, and random forests/ensemble modeling: how each works,
their regularization hyperparameters, and where they show up in environmental science.

:::

:::{card} 3.2) (Exercises) Support Vector Machines
:link: 3.2-svm-exercises.ipynb

Comparing `LinearSVC`, `SVC`, and `SGDClassifier` on the iris dataset, then training an SVM
regressor on California housing prices.

:::

:::{card} 3.3) (Exercises) Decision Trees and Random Forest
:link: 3.3-decision-trees-and-random-forest-exercises.ipynb

Training and fine-tuning a decision tree on the moons dataset with grid search, then building a
random forest from scratch by growing and combining many trees.

:::

:::{card} 3.4) (Exercises) Ensemble Modeling and Stacking
:link: 3.4-ensemble-modeling-and-stacking-exercises.ipynb

Comparing individual classifiers against voting and stacking ensembles on MNIST digits.

:::

:::{card} 3.5) (Exercises) Wildfire Susceptibility Mapping
:link: 3.5-wildfire-susceptibility-mapping-exercises.ipynb

Training classifiers on real topography, land-cover, and climate data to map wildfire
susceptibility in the Liguria region of Italy.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- [Hands-On Machine Learning with Scikit-Learn](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) — Aurélien Géron; chapters [5](https://github.com/ageron/handson-ml2/blob/master/05_support_vector_machines.ipynb) (SVMs), [6](https://github.com/ageron/handson-ml2/blob/master/06_decision_trees.ipynb) (decision trees), and [7](https://github.com/ageron/handson-ml2/blob/master/07_ensemble_learning_and_random_forests.ipynb) (ensembles/random forests) are the source of the classifier exercises. (3.2, 3.3, 3.4). The current edition, *Hands-On Machine Learning with Scikit-Learn and PyTorch*, covers decision trees and random forests as chapters 5 and 6 but no longer has a standalone SVM chapter.
- [Tonini, M., et al. "A Machine Learning-Based Approach for Wildfire Susceptibility Mapping. The Case Study of the Liguria Region in Italy."](https://www.mdpi.com/2076-3263/10/3/105) *Geosciences* 10.3 (2020): 105 — the source of the wildfire-mapping exercise and its Liguria dataset. (3.5)
- [Trucchia, A., et al. "Defining Wildfire Susceptibility Maps in Italy for Understanding Seasonal Wildfire Regimes at the National Level."](https://www.mdpi.com/2571-6255/5/1/30) *Fire* 5.1 (2022): 30 — generalizes the Liguria case study to all of Italy. (3.5)

### Scikit-learn

- [Support vector machines](https://scikit-learn.org/stable/modules/svm.html) — `LinearSVC`, `SVC`, kernels, and regularization. (3.1, 3.2)
- [Decision trees](https://scikit-learn.org/stable/modules/tree.html) — the CART algorithm and its regularization hyperparameters. (3.1, 3.3)
- [Ensemble methods](https://scikit-learn.org/stable/modules/ensemble.html) — voting, bagging, random forests, and stacking. (3.1, 3.3, 3.4)
- [Model selection: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) — hyperparameter search with cross-validation. (3.3)

### Datasets

- [The iris dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset) and the [California housing dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) — bundled with scikit-learn. (3.2)
- [MNIST](https://en.wikipedia.org/wiki/MNIST_database) — handwritten digits, used for comparing individual and ensemble classifiers. (3.4)
- Liguria wildfire susceptibility data (topography, land cover, climate, and historical wildfire occurrence) — Trucchia, Meschi, and Tonini. (3.5)
