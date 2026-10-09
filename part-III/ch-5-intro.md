# Chapter 5: Artificial Neural Networks and Surrogate Modeling

This chapter is the entry point to deep learning: what an artificial neural network is made of,
how it is trained, and how to build and train one in pytorch — first on a small synthetic
regression problem, then on a real image-classification benchmark with the full training
machinery (learning-rate selection, early stopping, checkpointing, and logging) — and finally as
a surrogate for the small-scale physics of a climate model, where physical knowledge decides
whether the network still works in a warmer climate.

::::{grid} 1 1 2 2

:::{card} 5.1) Introduction to Artificial Neural Networks
:link: 5.1-introduction-to-artificial-neural-networks.ipynb

Neurons, layers, and activation functions; the perceptron and the multilayer perceptron; then
the seven steps of building a network in pytorch — from data preparation through loss and
optimizer, an explicit training loop, evaluation, and the hyperparameters that set both the
architecture and the training.

:::

:::{card} 5.2) (Exercise) Artificial Neural Networks with PyTorch
:link: 5.2-artificial-neural-networks-with-pytorch-exercises.ipynb

Classifying handwritten MNIST digits end to end: loading and splitting the data, normalizing it,
finding a learning rate with an exponential range test, writing the training loop by hand, then
training for 100 epochs with early stopping, checkpointing, and TensorBoard logging before
evaluating on the test set.

:::

:::{card} 5.3) (Exercise) Physically-Informed Climate Modeling
:link: 5.3-physically-informed-climate-modeling-exercises.ipynb

Training a neural network to emulate the effect of storms, clouds, and turbulence on
atmospheric heating, on a cold climate simulation, and testing it on a warmer one: where it fails
to extrapolate, how rescaling the inputs with physical formulas (relative humidity, plume
buoyancy, a moisture-disequilibrium flux) removes the failure, and a custom data generator that
applies the rescalings batch by batch.

:::

::::

## Resources

### Textbooks this chapter adapts

- *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Aurélien Géron; chapter 9 (introduction to artificial neural networks) and chapter 10 (building neural networks with PyTorch) are the source of this chapter's material. (5.1, 5.2)

### Papers and code this chapter adapts

- Beucler, T., Pritchard, M., Yuval, J., Gupta, A., Peng, L., Rasp, S., Ahmed, F., et al., ["Climate-invariant machine learning"](https://arxiv.org/abs/2112.08440) (arXiv preprint) — the study behind 5.3: the cold and warm climate simulations, the physical rescalings, and the comparison of brute-force and climate-invariant networks. (5.3)
- [CBRAIN-CAM](https://github.com/raspstephan/CBRAIN-CAM) — the code base whose `data_generator.py` is the starting point of 5.3's data generator. (5.3)

### PyTorch

- [`torch.nn`](https://docs.pytorch.org/docs/stable/nn.html) — layers, containers such as `Sequential`, and loss functions. (5.1, 5.2)
- [`torch.optim`](https://docs.pytorch.org/docs/stable/optim.html) — optimizers and learning-rate schedulers, including the `ExponentialLR` used for the learning-rate range test. (5.1, 5.2)
- [`torch.utils.data`](https://docs.pytorch.org/docs/stable/data.html) — `Dataset` and `DataLoader`, which handle batching and shuffling. (5.2)
- [`torch.utils.tensorboard`](https://docs.pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html) — logging losses and metrics to TensorBoard. (5.2)
- [TorchVision datasets](https://docs.pytorch.org/vision/stable/datasets.html) — loading MNIST. (5.2)
- [TorchMetrics](https://lightning.ai/docs/torchmetrics/stable/) — the streaming accuracy metric tracked during training. (5.2)
- [`torch.utils.data.DataLoader`](https://docs.pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) with `batch_size=None` — how 5.3's data generator, which already returns whole batches, is fed to the training loop. (5.3)
- [`netCDF4`](https://unidata.github.io/netcdf4-python/) and [xarray](https://docs.xarray.dev/en/stable/) — reading the two simulations. (5.3)

### Datasets

- [MNIST](https://yann.lecun.com/exdb/mnist/) — 70,000 labelled 28×28 images of handwritten digits. (5.2)
- The cold and warm climate simulations of 5.3 — two reduced climate-simulation outputs of about 2.4 million samples each, hosted on a university SharePoint link and downloaded with a pinned checksum; see 5.3 for the details. (5.3)
