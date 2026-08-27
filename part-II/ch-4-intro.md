# Chapter 4: Unsupervised Learning (Clustering, Dimensionality Reduction) and Environmental Complexity

This chapter turns to unsupervised learning — dimensionality reduction with PCA and clustering
with K-means, GMMs, and DBSCAN — closing with a real application to identifying dynamical
regimes in ocean circulation data.

::::{grid} 1 1 2 2

:::{card} 4.1) Unsupervised Learning for Clustering and Dimensionality Reduction
:link: 4.1-unsupervised-learning-for-clustering-and-dimensionality-reduction.ipynb

Supervised vs. unsupervised vs. semi-supervised learning, PCA and other dimensionality-reduction
methods, and clustering with K-means, Gaussian mixture models, and DBSCAN.

:::

:::{card} 4.2) (Exercises) Dimensionality Reduction
:link: 4.2-dimensionality-reduction-exercises.ipynb

Does PCA always speed up training and improve performance? Comparing a random forest and a
logistic regression classifier on MNIST, with and without PCA.

:::

:::{card} 4.3) (Exercises) Clustering
:link: 4.3-clustering-exercises.ipynb

Choosing the number of clusters for K-means on a subsample of MNIST digits, using the silhouette
score and inertia, with and without PCA to speed up training.

:::

:::{card} 4.4) (Exercises) Ocean Regimes Identification
:link: 4.4-ocean-regimes-identification-exercises.ipynb

Clustering reduced-dimensionality ECCO ocean-model fields with xarray and K-means to identify
dynamical regimes in the North Atlantic, following Sonnewald et al.'s THOR method.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- [Hands-On Machine Learning with Scikit-Learn](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) — Aurélien Géron; chapters [8](https://github.com/ageron/handson-ml2/blob/master/08_dimensionality_reduction.ipynb) (dimensionality reduction) and [9](https://github.com/ageron/handson-ml2/blob/master/09_unsupervised_learning.ipynb) (unsupervised learning) are the source of the classifier exercises. (4.2, 4.3). The current edition, *Hands-On Machine Learning with Scikit-Learn and PyTorch*, covers the same material as chapters 7 and 8.
- Sonnewald, M., Wunsch, C., & Heimbach, P. (2019). [Unsupervised learning reveals geography of global ocean dynamical regions.](https://doi.org/10.1029/2018EA000519) *Earth and Space Science* — the THOR method and the source of the ocean-regimes exercise. (4.4)
- Sonnewald, M., & Lguensat, R. (2021). [Revealing the Impact of Global Heating on North Atlantic Circulation Using Transparent Machine Learning.](https://doi.org/10.1029/2021MS002496) *Journal of Advances in Modeling Earth Systems* — a follow-up applying THOR to circulation change under global heating. (4.4)
- Python scripts adapted from [Maike Sonnewald](https://github.com/maikejulie)'s own research code. (4.4)

### Scikit-learn

- [Decomposition: PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca) — principal component analysis and its variants. (4.1, 4.2)
- [Clustering](https://scikit-learn.org/stable/modules/clustering.html) — K-means, Gaussian mixture models, and DBSCAN. (4.1, 4.3, 4.4)
- [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation) — the silhouette score and inertia used to choose the number of clusters. (4.3)

### Xarray

- [Data structures](https://docs.xarray.dev/en/stable/user-guide/data-structures.html) — `Dataset`, `DataArray`, and the coordinate/dimension model used to reformat the ocean-model data. (4.4)
- [Reshaping and reorganizing data](https://docs.xarray.dev/en/stable/user-guide/reshaping.html) — `stack`/`unstack`, used to flatten the gridded fields for clustering and rebuild them for plotting. (4.4)

### Datasets

- [MNIST](https://en.wikipedia.org/wiki/MNIST_database) — handwritten digits, used throughout the dimensionality-reduction and clustering exercises. (4.2, 4.3)
- [ECCO (Estimating the Circulation and Climate of the Ocean)](https://www.ecco-group.org/products-ECCO-V4r4.htm) — the realistic ocean-model output behind the ocean-regimes dataset. (4.4)
