# Louvain Algorithm for Community Detection

The **Louvain Algorithm** is an efficient method for detecting communities in large networks by maximizing modularity — a measure that quantifies the quality of community partitions.  
This repository contains an implementation of the Louvain algorithm with visualization and analysis tools.

---

## 📘 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Algorithm Steps](#algorithm-steps)
- [Performance](#performance)
- [References](#references)
- [License](#license)
- [Contributors](#contributors)

---

## 🧩 Overview

The **Louvain method** (Blondel et al., 2008) is a hierarchical clustering algorithm for detecting communities in networks.  
It works by repeatedly optimizing **modularity** locally and then aggregating nodes belonging to the same community, forming a smaller graph.  
This process is repeated until modularity improvement becomes insignificant.

The algorithm is:
- **Fast**
- **Scalable**
- **Widely used** in network science and social network analysis

---

## ✨ Features

- Detects **hierarchical community structures**
- Works with **weighted** and **unweighted** graphs
- Scales to **large networks**
- Includes visualization of communities
- Outputs community membership and modularity score

---

## ⚙️ Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/debopamghosh12/Louvian-algorithm.git
cd louvain-algorithm
```

### Dependencies
- Python ≥ 3.8  
- `networkx`  
- `numpy`  
- `matplotlib` *(optional for visualization)*

You can install them manually as:
```bash
pip install networkx numpy matplotlib
```

---

## 🚀 Usage

### Command Line Interface

```bash
python main.py --input data/graph.edgelist --output results/communities.txt
```

### As a Python Module

```python
from louvain import Louvain
import networkx as nx

# Load or create a graph
G = nx.karate_club_graph()

# Initialize and run Louvain algorithm
louvain = Louvain(G)
communities = louvain.run()

print("Detected communities:", communities)
print("Modularity:", louvain.modularity())
```

---

## 📊 Example

Example on **Zachary’s Karate Club** network:

```python
import networkx as nx
from louvain import Louvain
import matplotlib.pyplot as plt

# Create test graph
G = nx.karate_club_graph()

# Run Louvain algorithm
louvain = Louvain(G)
communities = louvain.run()

# Visualize results
louvain.draw_communities(G, communities)
```

Output:
- A community-colored network plot
- Printed modularity score and community list

---

## 🔍 Algorithm Steps

1. **Initialization** – Each node is placed in its own community.  
2. **Local Optimization** – For each node, move it to the neighboring community that yields the largest modularity gain.  
3. **Aggregation** – Nodes in the same community are merged to form a new graph.  
4. **Iteration** – Repeat the two phases until modularity improvement becomes negligible.

### Modularity Definition

\[
Q = \frac{1}{2m} \sum_{ij} [A_{ij} - \frac{k_i k_j}{2m}] \delta(c_i, c_j)
\]

Where:
- \(A_{ij}\): adjacency matrix  
- \(k_i\): degree of node *i*  
- \(m\): total number of edges  
- \(\delta(c_i, c_j)\): 1 if *i* and *j* are in the same community, 0 otherwise

---

## ⚡ Performance

| Property | Value |
|-----------|--------|
| **Time Complexity** | ~O(n log n) (approximate) |
| **Scalability** | Handles millions of nodes |
| **Graph Type** | Weighted / Unweighted |
| **Result Quality** | High modularity partitions |

---

## 📚 References

- Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008).  
  *Fast unfolding of communities in large networks.*  
  Journal of Statistical Mechanics: Theory and Experiment, 2008(10), P10008.


---
