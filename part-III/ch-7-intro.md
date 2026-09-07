# Chapter 7: Recurrent Neural Networks and Hydrological Modeling

This chapter introduces recurrent neural networks (RNNs) — the architecture behind most
sequence and time-series modeling — then applies them to two problems: generating Bach-style
chorales and forecasting streamflow from a hydrological time series.

::::{grid} 1 1 2 2

:::{card} 7.1) Introduction to Recurrent Neural Networks (RNN)
:link: 7.1-introduction-to-recurrent-neural-networks.ipynb

Sequential data, recurrent neurons, vanishing/exploding gradients, and where RNNs and NLP show
up in environmental science.

:::

:::{card} 7.2) Neural Networks for Time Series Predictions
:link: 7.2-neural-networks-for-time-series-predictions.ipynb

Memory cells, LSTM and GRU gating, training RNNs through time, and the attention mechanism and
transformer architecture.

:::

:::{card} 7.3) (Exercises) Composing Music
:link: 7.3-composing-music-exercises.ipynb

Training a WaveNet-style dilated convolutional model, and recurrent architectures, to generate
new Bach chorales one note at a time.

:::

:::{card} 7.4) (Exercises) Hydrological Modeling
:link: 7.4-hydrological-modeling-exercises.ipynb

Forecasting streamflow from temperature and precipitation records with an LSTM, evaluated using
the Nash-Sutcliffe efficiency coefficient.

:::

::::

## Resources

### Textbooks and papers this chapter's exercises adapt

- *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Aurélien Géron; [chapter 13](https://github.com/ageron/handson-mlp/blob/main/13_processing_sequences_using_rnns_and_cnns.ipynb) (processing sequences using RNNs and CNNs) is the direct source of the Bach chorale/WaveNet exercise. (7.2, 7.3)
- Mishra, S., Bordin, C., Taharaguchi, K., & Palu, I. "Comparison of deep learning models for multivariate prediction of time series wind power generation and temperature." *Energy Reports* 6 (2020): 273-286 — the source of the RNN/LSTM schematic figure. (7.2)
- Rassem, A., El-Beltagy, M., & Saleh, M. "Cross-country skiing gears classification using deep learning." *arXiv preprint arXiv:1706.08924* (2017). (7.2)
- Yang, Y., et al. "A study on water quality prediction by a hybrid CNN-LSTM model with attention mechanism." *Environmental Science and Pollution Research* 28.39 (2021): 55129-55139. (7.2)
- Alerskans, E., et al. "A transformer neural network for predicting near-surface temperature." *Meteorological Applications* 29.5 (2022): e2098. (7.2)

### PyTorch

- [`torch.nn.LSTM`](https://docs.pytorch.org/docs/stable/generated/torch.nn.LSTM.html) and [`torch.nn.GRU`](https://docs.pytorch.org/docs/stable/generated/torch.nn.GRU.html) — recurrent layers. (7.4)
- [`torch.nn.Conv1d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv1d.html) and [`torch.nn.Embedding`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html) — the building blocks of the WaveNet architecture. (7.3)
- [`torch.utils.data.Dataset`](https://docs.pytorch.org/docs/stable/data.html) — building a custom windowed dataset. (7.3)

### Datasets

- [JSB Chorales](https://github.com/ageron/data) — 382 Bach chorales, from Géron's own public dataset repository. (7.3)
- Streamflow, temperature, and precipitation records for a gauged catchment. (7.4)
