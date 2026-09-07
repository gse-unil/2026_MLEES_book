# Chapter 8: Graph Neural Networks and Interconnected Systems

This chapter introduces graph neural networks (GNNs) — architectures built for data that lives
on irregular, connected structures rather than grids or sequences — and applies the core ideas
to a small, well-known benchmark graph.

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

::::

## Resources

### Textbooks and tutorials this chapter's exercises adapt

- Kipf, T. N., & Welling, M. "Semi-Supervised Classification with Graph Convolutional Networks." *International Conference on Learning Representations* (2017) — the source of the Graph Convolutional Network (GCN) architecture used in 8.2. (8.1, 8.2)
- [PyTorch Geometric's "Introduction: Hands-on Graph Neural Networks" tutorial](https://colab.research.google.com/drive/1h3-vJGRVloF5zStxL5I0rSy4ZUPNsjy8) by Matthias Fey — the direct source of 8.2's PyG data-handling and GCN sections. (8.2)
- [jdwittenauer's NetworkX tutorial](https://colab.research.google.com/github/jdwittenauer/ipython-notebooks/blob/master/notebooks/libraries/NetworkX.ipynb) — the source of 8.2's NetworkX basics section. (8.2)
- Stanford CS224W (Machine Learning with Graphs) — the source of 8.2's graph-statistics exercises (average degree, clustering coefficient, PageRank, closeness centrality) and node-embedding exercise. (8.2)

### PyTorch Geometric and NetworkX

- [PyTorch Geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/) — datasets, `GCNConv`, and other graph neural network layers. (8.2)
- [NetworkX documentation](https://networkx.org/documentation/stable/) — graph creation, manipulation, and analysis in Python. (8.2)

### Datasets

- [Zachary's karate club network](https://en.wikipedia.org/wiki/Zachary%27s_karate_club) — a 34-member social network with 4 known communities, the standard toy benchmark for GNNs. (8.2)
