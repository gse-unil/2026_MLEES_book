# (Part IV) Towards Trustworthy AI

## Introduction

Part IV moves from building models that predict well to building models that can be trusted:
understanding why a model makes the predictions it does, quantifying how confident those
predictions are, and blending machine learning with physical knowledge rather than treating it
as a black box.

Chapter 9 covers explainable AI (XAI) — partial dependence plots, permutation feature
importance, and SHAP-based explanations, applied first to tabular classifiers (Titanic survival,
wine quality) and then to a convolutional neural network trained on MNIST.

Chapter 10 covers generative modeling and uncertainty quantification — distributional
regression with the continuous ranked probability score, then autoencoders, GANs, and a
diffusion model, all trained on CIFAR-10.

Chapter 11 covers hybrid modeling — combining a physics-based numerical model with a trained
CNN emulator, applied to glacier ice-flow simulation.

As in Parts II and III, each chapter pairs one tutorial notebook with separate exercise
notebooks, rather than Part I's one-lecture-one-exercises structure.
