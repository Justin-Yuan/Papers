## PolyGen: An Autoregressive Generative Model of 3D Meshes

[link](https://arxiv.org/pdf/2002.10880.pdf)
[code]()

<!-- ***************************************************** -->
model meshes by predicting mesh vertices and faces sequentially using a Transformer-based architecture. can condition on different inputs, such as class, voxels and images. 

vertex model unconditioanlly models mesh vertices and face model models the mesh faces conditioned on input vertices. 
$$
p(M) = p(V,f) = p(F|V)p(V)
$$

vertex model uses a masked Transformer decoder, face model combines Transformer with pointer networks to express a distribution over variable length vertex sequences. 


<!-- ***************************************************** -->
---
#### Key Points

- represent meshes using n-gons rather than triangles
- vertex model, autoregressive model, generate vertices in order (z first, then y, finally x), with stopping token 
$$
p(V^{seq};\theta) = \prod_{n=1}^{N_V}p(v_n|v_{<n};\theta)
$$
- face model orders faces by their lowest vertex index, concatenate faces to form a flattened sequence with a final stopping token. 
$$
p(F^{seq}|V;\theta) = \prod_{n=1}^{N_F}p(f_n|f_{<n,V;\theta})
$$
- train to maximize log-likelihood 


<!-- ***************************************************** -->
---
#### Results

- test on ShapeNet Core V2 dataset
- compar with Occupancy Networks 

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References



