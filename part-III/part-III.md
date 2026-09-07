# (Part III) Deep Learning for the Geosciences

## Introduction

Part III moves from the classical machine learning of Part II into deep learning: neural
networks with many layers, trained end to end, applied to the kinds of high-dimensional data
common in the geosciences — images, satellite imagery, and time series. It assumes Part II
throughout, and uses PyTorch as its only deep-learning library.

Chapter 6 covers convolutional neural networks (CNNs) — the architecture behind most modern
image analysis — applied to two remote-sensing problems: classifying flower photographs and
classifying Sentinel-2 satellite imagery into land-cover types, following the EuroSAT benchmark.
Chapter 7 covers recurrent neural networks (RNNs), applied to generating Bach-style chorales and
forecasting streamflow from a hydrological time series. Chapter 8 covers graph neural networks
(GNNs), applied to Zachary's karate club network — a small, well-known benchmark graph.

As in Part II, each chapter pairs one tutorial notebook with several standalone exercise
notebooks, rather than Part I's one-lecture-one-exercises structure. Exercises adapt notebooks
originally built around Keras and TensorFlow, ported here to PyTorch throughout — including
rewriting Keras's callback-based training (`.fit()`, `EarlyStopping`, `ModelCheckpoint`) as
explicit, manual training loops, which is how PyTorch expects training to be written.
