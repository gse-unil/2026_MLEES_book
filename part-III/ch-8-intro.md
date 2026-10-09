# Chapter 8: Graph Neural Networks and Interconnected Systems

This chapter introduces graph neural networks (GNNs) — architectures built for data that lives
on irregular, connected structures rather than grids or sequences — and applies the core ideas
to a small, well-known benchmark graph, then to the graph formulation of weather forecasting.

::::{grid} 1 1 2 2

:::{card} 8.1) What are Graph Neural Networks (GNNs)?
:link: 8.1-what-are-graph-neural-networks.ipynb

Nodes, edges, and graph types; the GNN design pipeline; GCN, GAT, and GraphSAGE
architectures; and where GNNs show up across the sciences.

:::

:::{card} 8.2) (Exercises) Graph Neural Networks with PyTorch
:link: 8.2-graph-neural-networks-with-pytorch-exercises.ipynb

NetworkX fundamentals and graph statistics (degree, clustering, PageRank, closeness
centrality) on Zachary's karate club network, then representing that graph in PyTorch
Geometric, training a node-embedding model from scratch, and building a 3-layer GCN to
classify its communities.

:::

:::{card} 8.3) (Exercises) Neural Weather Prediction
:link: 8.3-neural-weather-prediction-exercises.ipynb

The graph formulation of limited-area weather forecasting, at toy scale: building a multiscale
and a hierarchical mesh over a grid and measuring how far information has to travel, writing a
message-passing layer, assembling the encode-process-decode forecast step of neural-lam, and
rolling the trained model forward to read the forecast error against lead time.

:::

::::

## Resources

### Textbooks and tutorials this chapter's exercises adapt

- Kipf, T. N., & Welling, M. "Semi-Supervised Classification with Graph Convolutional Networks." *International Conference on Learning Representations* (2017) — the source of the Graph Convolutional Network (GCN) architecture used in 8.2. (8.1, 8.2)
- [PyTorch Geometric's "Introduction: Hands-on Graph Neural Networks" tutorial](https://colab.research.google.com/drive/1h3-vJGRVloF5zStxL5I0rSy4ZUPNsjy8) by Matthias Fey — the direct source of 8.2's PyG data-handling and GCN sections. (8.2)
- [jdwittenauer's NetworkX tutorial](https://colab.research.google.com/github/jdwittenauer/ipython-notebooks/blob/master/notebooks/libraries/NetworkX.ipynb) — the source of 8.2's NetworkX basics section. (8.2)
- Stanford CS224W (Machine Learning with Graphs) — the source of 8.2's graph-statistics exercises (average degree, clustering coefficient, PageRank, closeness centrality) and node-embedding exercise. (8.2)
- [neural-lam](https://github.com/mllam/neural-lam) — Joel Oskarsson and Tomas Landelius's code base for graph-based neural weather prediction on limited areas, whose encode-process-decode step 8.3 rebuilds at toy scale; see 8.3 for the papers behind it. (8.3)

### PyTorch Geometric and NetworkX

- [PyTorch Geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/) — datasets, `GCNConv`, and other graph neural network layers. (8.2)
- [NetworkX documentation](https://networkx.org/documentation/stable/) — graph creation, manipulation, and analysis in Python. (8.2)
- [`Tensor.index_add_`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.index_add_.html) — the summation of messages at each receiving node in 8.3's message-passing layer. (8.3)
- [`scipy.sparse.csgraph.shortest_path`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.shortest_path.html) — the path lengths behind 8.3's mesh diameters. (8.3)

### Datasets

- [Zachary's karate club network](https://en.wikipedia.org/wiki/Zachary%27s_karate_club) — a 34-member social network with 4 known communities, the standard toy benchmark for GNNs. (8.2)
