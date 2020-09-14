# DL: Graph Neural Networks

---

## Expressiveness

### Weisfeiler-Lehman Test

[Expressive power of graph neural networks and the Weisfeiler-Lehman test](https://towardsdatascience.com/expressive-power-of-graph-neural-networks-and-the-weisefeiler-lehman-test-b883db3c7c49)

- whether graph neural networks can distinguish between different types of graph structures
- graph isomorphism problem, aiming to determine whether two graphs are topologically equivalent. Two isomorphic graphs have the same connectivity and differ only by a permutation of their nodes.
- Weisfeiler-Lehman (WL) test for graph isomorphism problem, works for almost all graphs, in the probabilistic sense

    ![DL%20Graph%20Neural%20Networks%205a3802651fe448a48ae88a3f3888f3b9/gnn2.png](DL%20Graph%20Neural%20Networks%205a3802651fe448a48ae88a3f3888f3b9/gnn2.png)

    - based on iterative graph recolouring
    - starting with all nodes of identical colour. At each step, the algorithm aggregates the colours of nodes and their neighbourhoods representing them as multisets, and hashes the aggregated colour multisets into unique new colours
    - algorithm stops upon reaching a stable colouring
    - If at that point the colourings of the two graphs differ, the graphs are deemed non-isomorphic. However, if the colourings are the same, the graphs are possibly (but not necessarily) isomorphic
    - necessary but insufficient condition for graph isomorphism, couter-example:

        ![DL%20Graph%20Neural%20Networks%205a3802651fe448a48ae88a3f3888f3b9/gnn1.png](DL%20Graph%20Neural%20Networks%205a3802651fe448a48ae88a3f3888f3b9/gnn1.png)

- resemblance to graph message passing neural networks and WL test
    - The choice of the aggregation and the update operations is crucial: only multiset injective functions make it equivalent to the WL algorithm.
    - e.g. Graph Isomorphism Networks (GIN)
- k-WL test is a higher-order extension of the Weisfeiler-Lehman algorithm that works on k-tuples instead of individual nodes, also referred to as Weisfeiler-Lehman hierarchy
    - e.g. k-GNN
    - this higher-order GNN is non-local, k-GNNs require 𝒪(nᵏ) memory
    - e.g. Invariant Graph Networks (IGN) based on k-order tensors
    - 3-WL-equivalent IGN has “only” quadratic complexity, which is probably the only practically useful graph neural network architecture strictly more powerful than message passing
    - connection with graph theory and distributed local algorithms
- but better expressivity does not necessarily offer better generalization, or it is possible that the graph isomorphism model might not capture correctly the actual notion of graph similarity in specific applications

---

### Substructures

[Beyond Weisfeiler-Lehman: using substructures for provably expressive graph neural networks](https://towardsdatascience.com/beyond-weisfeiler-lehman-using-substructures-for-provably-expressive-graph-neural-networks-d476ad665fa3)

- local and computationally efficient provably powerful graph neural networks
- Graph Substructure Networks (GSN)
    - conceptually similar to positional encoding or graphlet descriptors, make the message passing mechanism aware of the local graph structure, allowing for computing messages differently depending on the topological relationship between the endpoint nodes
    - done by passing to message passing functions additional structural descriptors associated with each node, constructed by subgraph isomorphism counting
    - The choice of the substructures to count is crucial both to the expressive power of GSNs and the computational complexity of the pre-computation step.
    - k-isoregular graphs, are instances on which the (k+1)-WL test fails, but can be distinguished by GSN with appropriate structures.
    - GSN with small substructures such as cycles, paths, and cliques work for strongly regular graphs, which are known to be a tough nut for the Weisfeiler-Lehman tests.
    - observed that different problems and datasets benefit from different substructures

---

### Approximate isomorphisms and metric embeddings

[Beyond Weisfeiler-Lehman: approximate isomorphisms and metric embeddings](https://towardsdatascience.com/beyond-weisfeiler-lehman-approximate-isomorphisms-and-metric-embeddings-f7b816b75751)

- Graph neural networks can be seen as attempting to find a graph embedding f(G), with the desired property f(G)=f(G′) iff G~G′
- two non-isomorphic graphs can result in equal embeddings.
- In practical applications, we rarely deal with exactly isomorphic graphs but rather graphs that are approximately isomorphic
- A proper way of quantifying the notion of “approximate isomorphism” is in the form of a metric d, d(G,G′)=0 iff G~G′
    - e.g. Graph edit distance or the Gromov-Hausdorff distance
- isometric embedding

    $$|f(G)−f(G′)|=d(G,G′)\ \  \forall G, G′$$

    - but Instead of requiring the equation to hold exactly, one can relax it by bounding the metric dilation (expressed as the bi-Lipschitz constant c of the embedding f) → approximate isometry

        $$c^{-1} d(G,G′) ≤ |f(G)−f(G′)| ≤ c d(G,G′)\ \  for\  c≥1$$

    - further relaxed allowing for additional metric distortion ε, which sets a tolerance on how far apart can isomorphic graphs be

        $$c^{-1} d(G,G′)−ε ≤ |f(G)−f(G′)| ≤ c d(G,G′)+ε \ \ for\  c≥1$$

- The approximate isomorphism problem can be rewritten as a probabilistic statement in the “probably approximately correct” (PAC) form

    $$𝖯\bigg( c^{-1} d(G,G′)−ε ≤ |f(G)−f(G′)| ≤ c d(G,G′) \bigg) > 1−δ$$

    - “approximately” is understood in the sense of the metric dilation c and “probably” is that the bound holds with high probability 1−δ for some distribution of graph
- conenction to metric geometry

---

## Papers

### How Powerful are Graph Neural Networks?

link: [http://arxiv.org/abs/1810.00826](http://arxiv.org/abs/1810.00826)

---

### Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks

link: [http://arxiv.org/abs/1810.02244](http://arxiv.org/abs/1810.02244)

---

### Provably Powerful Graph Networks

link: [http://arxiv.org/abs/1905.11136](http://arxiv.org/abs/1905.11136)

---

### Differentiable Graph Module (DGM) for Graph Convolutional Networks

link: [http://arxiv.org/abs/2002.04999](http://arxiv.org/abs/2002.04999)

---

### Improving Graph Neural Network Expressivity via Subgraph Isomorphism Counting

link: [http://arxiv.org/abs/2006.09252](http://arxiv.org/abs/2006.09252)

---