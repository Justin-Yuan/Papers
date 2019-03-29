### GRAPH LEARNING NETWORK: A STRUCTURE LEARNING ALGORITHM
[link](https://openreview.net/pdf?id=HylRk2A5FQ)


<!--- *********************************************************************************************************************************************** --->
--- 

### Photographic Image Synthesis with Cascaded Refinement Networks
[link](https://arxiv.org/pdf/1707.09405.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks
[link](https://arxiv.org/pdf/1612.03242v2.pdf)





<!--- *********************************************************************************************************************************************** --->
--- 

### A Note on the Inceptin Score 
[link](https://arxiv.org/pdf/1801.01973.pdf)





<!--- *********************************************************************************************************************************************** --->
--- 

### Improved Techniques for Training GANs
[link](https://arxiv.org/pdf/1606.03498.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### SPICE: Semantic Propositional Image Caption Evaluation
[link](https://arxiv.org/pdf/1607.08822.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### Image Transformer
[link](https://arxiv.org/pdf/1802.05751.pdf)

#### Intro 

- self-attention for a sequence modeling formulation of image generation with a tractable likelihood 
- PixelRNN & PixelCNN ahve tractable likelihood 
- specific locally restricted form of multi-head self-attention -> interpreted as a sparsely parameterized form of gated convolution 

#### Future work 

- likelihood-based models of images in GANs 
- tasks combining modalities, e.g. language-driven editing of images 
- move beyond still images to video 


<!--- *********************************************************************************************************************************************** --->
--- 

### Self-Attention Generative Adversarial Networks
[link](https://arxiv.org/pdf/1805.08318.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Neural Relational Inference for Interacting Systems
[link](https://arxiv.org/pdf/1802.04687.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Non-local Neural Networks
[link](https://arxiv.org/pdf/1711.07971.pdf)

#### Intro 

- non-local operations as a generic family of building blocks for capturing long-range dependencies 
- non-local operation computes the response at a position as a weighted sum of the features at all positions (the set of positions can be in space, time or spacetime)

#### Modeling 

- choices for pairwise function 
    - Gaussian, raise e to the power of the dot product of the pair of features 
    - Embedded Gaussian, embed features -> self-attention 
    - Dot product 
    - Concatenation 
- with residual connection 
- using small mini-batches, freeze all BN layers 


<!--- *********************************************************************************************************************************************** --->
--- 

### GLoMo: Unsupervisedly Learned Relational Graphs as Transferable Representations
[link](https://arxiv.org/pdf/1806.05662.pdf)

**Very cool idea**

#### Intro 

- learning generic latent relational graphs, capture dependencies between pairs of data units from large-scale data
- transfer graphs to downstream tasks, graphs multiplied by task-specific features to produce structure-aware features 
- nodes of a latent graph are input units, task is to learn an affinity matrix where weights capture dependencies between pairs of input units 
- affinity matrix is asymmetric, representing a directed weighted graph 
- graph predictor network & feature predictor network 
- graph predictor network takes input, produce set of graphs 
- feature predictor network takes set of graphs and input, perform a predictive task 

#### Modeling 

- graph predictor = key CNN + query CNN 
- feature predictor = zero-th layer features are embeddings of x + affinity matrix is combined with current features to compute the next-layer features 
- RNN decoder maximizes conditional log proability of context prediction in an auto-regressive fashion 
- key points 
    - decoupling graphs and features 
    - sparisity using squared ReLU activation 
    - Hierarchical graph representations with multiple layers of graphs 
    - Unit-level objectives, impose context prediction objective on each unit 
    - Sequence prediction, predict the context of some length 


<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 