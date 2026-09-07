# Chapter 6: Convolutional Neural Networks and Remote Sensing

This chapter introduces convolutional neural networks (CNNs) — the architecture behind most
modern image analysis — then applies them to two real remote-sensing problems: photographic
flower classification and satellite land-cover classification.

::::{grid} 1 1 2 2

:::{card} 6.1) Convolutional Neural Networks and Remote Sensing
:link: 6.1-cnn-remote-sensing.ipynb

Convolutional and pooling layers, well-known CNN architectures, and where CNNs show up in
vegetation and land-cover remote sensing.

:::

:::{card} 6.2) (Exercises) Deep Computer Vision
:link: 6.2-deep-computer-vision-exercises.ipynb

Training a CNN to classify flower photos, with and without data augmentation, tracking both
runs with early stopping, checkpointing, and TensorBoard.

:::

:::{card} 6.3) (Exercises) Land Cover Classification
:link: 6.3-land-cover-classification-exercises.ipynb

Classifying Sentinel-2 satellite imagery from the EuroSAT dataset into 10 land-cover classes,
then improving on a baseline CNN with more capacity, dropout, and transfer learning from a
pretrained VGG16.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Aurélien Géron; chapter 12 (deep computer vision using convolutional neural networks) is the source of this chapter's CNN material. (6.1, 6.2)
- Kattenborn, T., Leitloff, J., Schiefer, F., & Hinz, S. "Review on Convolutional Neural Networks (CNN) in Vegetation Remote Sensing." *ISPRS Journal of Photogrammetry and Remote Sensing* 173 (2021): 24-49 — the source of this chapter's CNN architecture and application figures. (6.1)
- Helber, P., Bischke, B., Dengel, A., & Borth, D. "EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification." *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing* 12.7 (2019): 2217-2226 — the source of the EuroSAT dataset and exercise. (6.3)

### PyTorch and TorchVision

- [`torch.nn.Conv2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) and [`torch.nn.MaxPool2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.MaxPool2d.html) — the core convolution and pooling layers. (6.1, 6.2, 6.3)
- [TorchVision datasets](https://docs.pytorch.org/vision/stable/datasets.html) and [transforms](https://docs.pytorch.org/vision/stable/transforms.html) — loading image datasets and building preprocessing/augmentation pipelines. (6.2)
- [TorchVision pretrained models](https://docs.pytorch.org/vision/stable/models.html) — VGG16 and transfer learning. (6.3)
- [`torch.utils.tensorboard`](https://docs.pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html) — logging training curves to TensorBoard. (6.2)

### Datasets

- [tf_flowers](https://www.tensorflow.org/datasets/catalog/tf_flowers) — 3,670 photos of five flower species. (6.2)
- [EuroSAT](https://github.com/phelber/EuroSAT) — Sentinel-2 satellite imagery across 10 land-use and land-cover classes. (6.3)
