# Chapter 9: Explainable Artificial Intelligence and Understanding Predictions

Chapter 9 opens Part IV with explainable AI (XAI): the tools that make a trained model's
predictions interpretable, from partial dependence plots and permutation feature importance on
tabular models to SHAP-based explanations for tree ensembles and neural networks.

::::{grid} 1 1 2 2

:::{card} 9.1) Why do we need machine learning model interpretability?
:link: 9.1-why-model-interpretability.ipynb

Local vs. global and model-agnostic vs. model-specific explanation methods, partial dependence
plots, permutation feature importance, and explanation methods for neural networks.

:::

:::{card} 9.2) (Exercise) XAI on Simple Datasets
:link: 9.2-xai-on-simple-datasets-exercises.ipynb

Partial dependence plots and permutation importance on a Titanic survival classifier, SHAP
values on a wine-quality XGBoost classifier, and SHAP's DeepExplainer on a CNN trained on MNIST.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- Molnar, C. *Interpretable Machine Learning* — the source of the black-box/white-box framing, the partial dependence plot definition, and the SHAP bicycle-rental example. (9.1, 9.2)
- Du, M., Liu, N., & Hu, X. "Techniques for interpretable machine learning." *Communications of the ACM* 63.1 (2019): 68-77 — source of the interpretability-progress figure. (9.1)
- Wang, T., & Lin, Q. "Hybrid predictive models: When an interpretable model collaborates with a black-box model." *The Journal of Machine Learning Research* 22.1 (2021): 6085-6122 — source of the interpretability/accuracy trade-off figure. (9.1)
- Obringer, R., & Nateghi, R. "Predicting urban reservoir levels using statistical learning techniques." *Scientific Reports* 8.1 (2018): 5164 — source of the streamflow partial dependence plot example. (9.1)
- Nirmalraj, S., et al. "Permutation feature importance-based fusion techniques for diabetes prediction." *Soft Computing* (2023): 1-12 — source of the permutation-importance-for-feature-filtering example. (9.1)
- Molina, M. J., Gagne, D. J., & Prein, A. F. "A benchmark to test generalization capabilities of deep learning methods to classify severe convective storms in a changing climate." *Earth and Space Science* 8.9 (2021): e2020EA001490 — source of the saliency-map example. (9.1)
- The Titanic survival exercise adapts a [Kaggle competition notebook](https://www.kaggle.com/code/dansbecker/partial-dependence-plots) on partial dependence plots. (9.2)

### SHAP and scikit-learn

- [SHAP documentation](https://shap.readthedocs.io/) — partial dependence plots, waterfall/bar/beeswarm/force plots, `TreeExplainer`, and `DeepExplainer`. (9.2)
- [`sklearn.inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html) and [`sklearn.inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html). (9.1, 9.2)
- [XGBoost Python API](https://xgboost.readthedocs.io/en/stable/python/python_api.html) — the tree-based classifier explained with SHAP's `TreeExplainer`. (9.2)

### Datasets

- [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic) — passenger records used to train a survival classifier. (9.2)
- [UCI Wine Quality (red)](https://archive.ics.uci.edu/dataset/186/wine+quality) — chemical properties and quality scores for Portuguese "Vinho Verde" red wine. (9.2)
- [MNIST](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html) — handwritten digits, used to train the CNN explained with SHAP's `DeepExplainer`. (9.2)
