# Chapter 5: Artificial Neural Networks

This chapter is the entry point to deep learning: what an artificial neural network is made of,
how it is trained, and how to build and train one in pytorch — first on a small synthetic
regression problem, then on a real image-classification benchmark with the full training
machinery (learning-rate selection, early stopping, checkpointing, and logging).

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

::::

## Resources

### Textbooks this chapter adapts

- *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Aurélien Géron; chapter 9 (introduction to artificial neural networks) and chapter 10 (building neural networks with PyTorch) are the source of this chapter's material. (5.1, 5.2)

### PyTorch

- [`torch.nn`](https://docs.pytorch.org/docs/stable/nn.html) — layers, containers such as `Sequential`, and loss functions. (5.1, 5.2)
- [`torch.optim`](https://docs.pytorch.org/docs/stable/optim.html) — optimizers and learning-rate schedulers, including the `ExponentialLR` used for the learning-rate range test. (5.1, 5.2)
- [`torch.utils.data`](https://docs.pytorch.org/docs/stable/data.html) — `Dataset` and `DataLoader`, which handle batching and shuffling. (5.2)
- [`torch.utils.tensorboard`](https://docs.pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html) — logging losses and metrics to TensorBoard. (5.2)
- [TorchVision datasets](https://docs.pytorch.org/vision/stable/datasets.html) — loading MNIST. (5.2)
- [TorchMetrics](https://lightning.ai/docs/torchmetrics/stable/) — the streaming accuracy metric tracked during training. (5.2)

### Datasets

- [MNIST](https://yann.lecun.com/exdb/mnist/) — 70,000 labelled 28×28 images of handwritten digits. (5.2)
