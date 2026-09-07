# Chapter 10: Generative Modeling and Uncertainty Quantification

Chapter 10 covers two closely related themes: quantifying how confident a model's predictions
are, and generating new data samples rather than just predicting labels. It moves from
distributional regression and CRPS-based uncertainty quantification to autoencoders, GANs, and
diffusion models.

::::{grid} 1 1 2 2

:::{card} 10.1) Generative Modeling: From Uncertainty Quantification to Stochastic Downscaling
:link: 10.1-generative-modeling-and-uncertainty-quantification.ipynb

Generative modeling, ways of adding uncertainty to machine learning models, how to evaluate
uncertainty estimates, and an overview of autoencoders, GANs, VAEs, and probabilistic graphical
models.

:::

:::{card} 10.2) (Exercise) Introduction to Uncertainty Quantification and Generative Modeling
:link: 10.2-uncertainty-quantification-exercises.ipynb

Aleatoric vs. epistemic uncertainty, distributional regression with the continuous ranked
probability score (CRPS), and evaluating a trained model with spread-skill plots and a PIT
histogram.

:::

:::{card} 10.3) (Exercise) Autoencoders, Generative Adversarial Networks, and Diffusion Models
:link: 10.3-autoencoders-gans-diffusion-exercises.ipynb

Stacked, denoising, and variational autoencoders; GANs and deep convolutional GANs; and a
UNet-based diffusion model, all trained on CIFAR-10.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Aurélien Géron; the source this chapter's autoencoder/GAN/diffusion exercise (10.3) is adapted from, converted here to PyTorch throughout. (10.3)
- Haynes, K., Lagerquist, R., McGraw, M., Musgrave, K., & Ebert-Uphoff, I. "Creating and Evaluating Uncertainty Estimates with Neural Networks for Environmental-Science Applications." *Artificial Intelligence for the Earth Systems* 2.2 (2023) — the source of the uncertainty-quantification framing and figures used throughout 10.1 and 10.2. (10.1, 10.2)
- Ho, J., Jain, A., & Abbeel, P. "Denoising Diffusion Probabilistic Models." *NeurIPS* (2020), and Nichol, A., & Dhariwal, P. "Improved Denoising Diffusion Probabilistic Models." *ICML* (2021) — the diffusion process and cosine variance schedule used in 10.3. (10.3)

### PyTorch

- [`torch.nn`](https://docs.pytorch.org/docs/stable/nn.html) — the layers (`Linear`, `LazyLinear`, `Conv2d`, `ConvTranspose2d`, `BatchNorm2d`) used to build every architecture in this chapter. (10.2, 10.3)
- [`torchvision.datasets.CIFAR10`](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html) — the image dataset used throughout 10.3. (10.3)
- [`sklearn.manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) — visualizing the autoencoder's compressed representations. (10.3)

### Datasets

- A synthetic x/y dataset built for this chapter's uncertainty-quantification exercise (10.2), heteroscedastic and non-Gaussian by design.
- [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) — 60,000 32×32 color images across 10 classes. (10.3)
