# Chapter 11: Hybrid Modeling and Knowledge-Guided Learning

Chapter 11 closes Part IV with hybrid modeling: combining physics-based models with machine
learning rather than treating ML as a standalone black box. The running example is glacier
flow, replacing the most computationally expensive part of a numerical ice-flow model with a
trained CNN emulator.

::::{grid} 1 1 2 2

:::{card} 11.1) Introduction to Hybrid Modeling
:link: 11.1-introduction-to-hybrid-modeling.ipynb

What knowledge-guided machine learning (KGML) is, why data-only and knowledge-only models each
fall short on their own, and where hybrid models are applied across climate science,
engineering, and medicine.

:::

:::{card} 11.2) (Exercise) Introduction to Hybrid Models: Combining Physics-Based and Machine Learning Models
:link: 11.2-hybrid-glacier-modeling-exercises.ipynb

Simulating glacier flow with the shallow ice approximation, training a CNN to emulate the ice
velocity field, then plugging that emulator into the numerical mass-conservation solver in
place of the expensive physics-based calculation.

:::

::::

## Resources

### Textbooks and papers this chapter's exercise adapts

- The *Instructed Glacier Model* ([IGM](https://github.com/jouvetg/igm)) — the CNN-emulator approach this exercise's hybrid model is based on. (11.2)
- The shallow ice approximation (SIA) used for the numerical ice-flow solver is standard in large-scale ice-sheet modeling; see e.g. Hutter, K. *Theoretical Glaciology* (1983) for its derivation. (11.2)

### PyTorch

- [`torch.nn.Conv2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) — the fully-convolutional CNN architecture used to emulate ice-flow velocity from ice thickness and surface slope. (11.2)
- [`torch.nn.functional.pad`](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.pad.html) and [`torch.where`](https://docs.pytorch.org/docs/stable/generated/torch.where.html) — the staggered-grid finite-difference operations behind the numerical ice-flow solver. (11.2)

### Datasets

- A bedrock topography grid for the exercise's synthetic glacier domain (`bedrock.nc`, committed to `data/part-IV/`). (11.2)
- The CNN's training dataset (simulated glacier states from a high-order ice-flow model) is not yet committed to the repository — flagged as a pending follow-up; see the chapter's port notes. (11.2)
