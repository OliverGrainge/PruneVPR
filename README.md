# Structured Pruning for Efficient Visual Place Recognition (VPR)

This repository will host the source code and models for the paper:

**[Structured Pruning for Efficient Visual Place Recognition](https://arxiv.org/abs/2409.07834)**

Authors: Oliver Grainge, Michael Milford, Indu Bodala, Sarvapali D. Ramchurn and Shoaib Ehsan

## Introduction

This repository implements a novel approach to optimize Visual Place Recognition (VPR) using structured pruning. VPR is crucial for global re-localization in robotics, enabling efficient recognition of previously visited locations based on visual inputs. Our method introduces a dual-pruning mechanism that reduces redundancies in both the feature extraction network and the embedding space, leading to substantial gains in memory efficiency and latency while maintaining high accuracy.

### Key Features
- **Structured Pruning**: Removes non-salient filters and neurons, resulting in a dense pruned network for faster inference.
- **Dual Optimization**: Optimizes both feature extraction and retrieval, reducing the embedding dimension without sacrificing recall@1 performance.
- **Resource Efficiency**: Achieves significant reductions in memory usage (21%) and latency (16%) with less than a 1% impact on recall@1 accuracy.
- **Compatibility**: Designed to work on embedded platforms like Nvidia Xavier NX for real-time applications.

## Paper

You can find the full paper on [arXiv](https://arxiv.org/abs/2409.07834). Please cite our work as follows:

```bibtex
@article{grainge2024structuredpruningefficientvisual,
  title = {Structured Pruning for Efficient Visual Place Recognition},
  author = {Oliver Grainge and Michael Milford and Indu Bodala and Sarvapali D. Ramchurn and Shoaib Ehsan},
  journal = {arXiv preprint arXiv:2409.07834},
  year = {2024},
  eprint = {2409.07834},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  url = {https://arxiv.org/abs/2409.07834}
}
