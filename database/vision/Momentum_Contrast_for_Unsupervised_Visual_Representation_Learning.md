## Momentum Contrast for Unsupervised Visual Representation Learning

[link](https://arxiv.org/pdf/1911.05722.pdf)
[code](https://github.com/facebookresearch/moco) (multi-gpu only)
[code](https://github.com/HobbitLong/CMC)

<!-- ***************************************************** -->
contrastive learning [27] as dictionary look-up for unsupervised learning. key is building dynamic dictionaries. 

build dictionaries that are: (i) large and (ii) consistent as they evolve during training. Intuitively, a larger dictio- nary may better sample the underlying continuous, high- dimensional visual space, while the keys in the dictionary should be represented by the same or similar encoder so that their comparisons to the query are consistent. 

maintain the dictionary as a queue of data samples: the encoded repre- sentations of the current mini-batch are enqueued, and the oldest are dequeued.

<!-- ***************************************************** -->
---
#### Key Points

- Contrastive losses measure the similarities of sam- ple pairs in a representation space.
- Adversarial losses measure the difference between probability distributions.
- Pretext tasks. Examples include recovering the input under some corruption.
- uses **InfoNCE**. The contrastive loss serves as an unsupervised objective function for training the encoder networks that represent the queries and keys. The input $x_q$ and $x_k$ can be images, patches, or context consisting a set of patches.
$$
L_q = -log \frac{exp(q \cdot k_{+} / \tau)}{\sum_{i=0}^K exp(q \cdot k_i / \tau)}
$$
- The dictionary is dynamic in the sense that the keys are randomly sampled, and that the key encoder evolves during training.
- use momentum update to keep encoded samples in dictionary/queue consistent. Only the parameters θq are updated by back-propagation. The momentum update makes $\theta_k$ evolve more smoothly than $\theta_q$.
$$
\theta_k \leftarrow m \theta_k + (1-m)\theta_q
$$
- use simple inistance discrimination task for pretext task. consider a query and a key as a pos- itive pair if they originate from the same image, and otherwise as a negative sample pair (from the dictionary/queue). 
- use $Shuffling BN$ to prevent information leak inside a batch 

<!-- ***************************************************** -->
---
#### Results

- MoCo largely closes the gap between un- supervised and supervised representation learning in many computer vision tasks, and can serve as an alternative to ImageNet supervised pre-training in several applications.

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References

[1] Noise-contrastive estimation: A new estimation principle for unnormalized statistical models [link](http://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf)

[2] Unsupervised Feature Learning via Non-Parametric Instance Discrimination [link](https://arxiv.org/pdf/1805.01978v1.pdf)
