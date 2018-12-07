### Datasets 

#### Visual Genome 
[link](https://visualgenome.org/)

#### COCO-Stuff 
[link](https://github.com/nightrome/cocostuff)

#### Visual Relationship Detection
[link](https://cs.stanford.edu/people/ranjaykrishna/vrd/)

#### NYU Depth v2 dataset
[link](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html)


<!--- *********************************************************************************************************************************************** --->
--- 

### Image Retrieval using Scene Graphs
[link](https://hci.stanford.edu/publications/2015/scenegraphs/JohnsonCVPR2015.pdf)

#### Intro 

- conditional random field (CRF), likelihoods of groundings used as ranking scores for retrieval
- detailed semantics: objects, attributes, relationships 
-  Replacing textual queries with scene graphs allows queries to describe the semantics of the desired image in precise detail without relying on unstructured text
- scene graph and scene graph grounding 
- need to measure the agreement between a query scene graph and an unannotated test image 


<!--- *********************************************************************************************************************************************** --->
--- 

### Visual Genome 
[link](https://visualgenome.org/static/paper/Visual_Genome.pdf)

#### Intro 

- 3 key elements 
    - a grounding of visual concepts to language 
    - more complete set of descriptions and QAs for each image based on multiple image regions 
    - a formalized representation of the components of an image 
- knowledge base representation in NLP to represent object relations -> scene graph 
- all objects, attributes and relationships are canonicalized to its corresponding WordNet ID (synset ID)

#### Modeling 

- main components: region descriptions, objects, attributes, relationships, region graphs, scene graphs, question answer pairs
- free-form QA (based on the entire image) & region-based QA, 6 types of question per image: what, where, how, when, who, why 


<!--- *********************************************************************************************************************************************** --->
--- 

### Graph R-CNN for Scene Graph Generation
[link](https://arxiv.org/pdf/1808.00191.pdf)

#### Intro 

- scene graph form an interpretable structured representation of the image that supports higher-level visual intelligence tasks 
- leverage object-relationship regularities 

#### Modeling 

- model 
    - object node extraction -> object region proposal 
    - relationship edge pruning -> relationship proposal 
    - graph context integration -> graph labeling 
- relation proposal network (RePN), efficiently compute relatedness scores between object pairs, to prune unlikely scene graph connections
- exploit estimated class distributions to infer relatedness, learning soft class-relationships priors, kernel trick 
- non-maximal suppression to filter out object pairs with significant overlap 
- attentional graph convolution network (aGCN), to propogate higher-order context, place attention on reliable edges and dampen influence of unlikely ones 
- add skip-connect edges directly between all object nodes 
- run both a visual and semantic aGCN, one with visual features and the other with pre-softmax outputs, set attention in semantic aGCN to be that fo the visual aGCN to modulate flow of semantic information based on visual cues 
- loss
    - same loss used in RPN: binary cross entropy on proposals and regression loss for anchors  
    - binary cross entropy on relation proposals 
    - 2 multi-class cross entropy losses for object classification and predicate classification 

#### Evaluation 

- recall of <subject, predicate, object> triplets (**SGGen**) 
- recall of objects and predicates given groud truth object localizations (**PredCls**, **PhrCls**)
- novel, more holistic metric (**SGGen+**), computes total recall for singleton entities (objects & predicates), pair entities <object, attribute>, triplet entities <subject, predicate, object>
- SGGen is overly sensitive to label errors on objects with relationships 


<!--- *********************************************************************************************************************************************** --->
--- 

### Scene Graph Generation by Iterative Message Passing
[link](http://vision.stanford.edu/pdf/xu2017cvpr.pdf)

#### Intro 

- pass messages containing contextual informatino between a pair of bipartite sub-graphs of the scene graph, iteratively refine the predictions using RNN 
- can be considered as a more general framework for graph generation problem 

#### Modeling 

- all nodes share the same GRU weights, all edges share the other set of GRU weights 
- a message pooling function to dynamically aggregate hidden GRU states into messages 
- disjoint sub-graphs: primal graph defines channels for passing message from edge GRUs to node GRUs, dual graph does the other way round 
- use mean field to perform approximate inference 
- randomly select 128 boxes from NMS as object proposals

#### Evaluation 

- metrics
    - R@k, measures the fraction of ground-truth relationship triplets (subjectpredicate-object) that appear among the top k most confident triplet predictions in an image.
    - predicate classification (**PREDCLS**), predict the predicates of all pairwise relationships of a set of localized objects 
    - scene graph classification (**SGCLS**), predict the prediate as well as the object categories of the subject and the object in every pairwise relationship given a set of localized objects 
    - scene graph generation (**SGGEN**), detect a set of objects and predict the predicate between each pair of the detected objects. 
- performance of final model peaks at training with 2 iterations and degrades afterwards 


<!--- *********************************************************************************************************************************************** --->
--- 

### Scene Graph Generation from Objects, Phrases and Region Captions
[link](https://arxiv.org/pdf/1707.09700.pdf)

#### Intro 

- 3 levels of scene understanding: object detection, scene graph generation, region captioning 
- Multi-level Scene Description Network (MSDN), solve the 3 tasks jointly
- leverage the spatial and semantic correlations of the visual features

#### Modeling 

- 3 parallel branch for 3 vision tasks, based on conv layers of VGG-16
- Faster-RCNN for object detection 
- entire process 
    - region proposal -> 3 sets of proposals
        - object region proposals
        - phrase region proposals -> group N object proposals to N(N-1) object pairs 
        - caption region proposals
    - feature specialization -> 3 sets of FCs 
    - dynamic graph construction -> connect 3 sets of regions (**subject-predicate-object** triplet)
    - feature refinement -> 3 parallel steps for message passing 
        - object refining 
        - phrase refining 
        - caption refining 
    - final prediction (classify objects, predicates, generate captions)

#### Evaluation 

- Top-K recall, not using mAP since annotations of the relationships are incomplete, mAP will falsely penalize the positive but unlabeled predictions


<!--- *********************************************************************************************************************************************** --->
--- 

### Scene Graph Generation by Belief RNNs
[link](http://www.cs.tau.ac.il/~joberant/teaching/advanced_nlp_spring_2018/past_projects/scene_graph.pdf)

**model not powerful enough**

#### Intro 

- model infers directly on the beliefs (not taking into account the visual features), which is more generic
- feature extraction module + belief RNNs module 

#### Modeling 

- 2 ResNet50 to predict objects and predicates separately, unary and pairwise beliefts taken from the last layer before softmax 
- a sequence of RNNs, inputs predicates and object beliefs, output a new improved predicates and objects beliefs 


<!--- *********************************************************************************************************************************************** --->
--- 

### Image Generation from Scene Graphs
[link](https://arxiv.org/pdf/1804.01622.pdf)

#### Intro 

- challenges:
    - method to process graph-structured input 
    - ensure generated images respect the objects and relationships specified in graph 
    - ensure synthesized images are realistic
- use graph convolution to process input graphs
- compute a scene layout by predicting bounding boxes and segmentation masks for objects
- convert layout to image with cascaded refinement network 
- train adversarially against a pair of discriminator networks 
- evaluate with Amazon Mechanical Turk, compared to StackGAN 

#### Modeling 

- embedding layer to convert scene graph nodes from categorical vector to dense vector 
- graph convolution network to process embedding scene graph 
- image discriminator ensures overall appearance of generated image is realistic 
- object discriminator ensures each object in the image appears realistic, recognizable 
- training 
    - box loss -> L1 difference of ground-truth and predicted boxes 
    - mask loss -> pixelwise cross-entropy on masks
    - pixel loss -> L1 difference of ground-truth and generated images 
    - image adversarial loss and 
    - auxiliaryly classifier loss from 
- augment scene graphs with **image** object, add **in image** relationships to connect each true object with the **image** object -> all scene graphs are connected 


<!--- *********************************************************************************************************************************************** --->
--- 

### Generating Semantically Precise Scene Graphs from Textual Descriptions for Improved Image Retrieval
[link](http://anthology.aclweb.org/W/W15/W15-2812.pdf)

#### Intro 

- parse scene description to scene graph
- Including relations and attributes in the query graph outperforms a model that only considers objects 
- parsing to scene graphs can be used to generate 3D scenes 
- parse image description to dependency trees to produce semantic graph 


<!--- *********************************************************************************************************************************************** --->
--- 

### Visual Relationship Detection with Language Priors
[link](https://cs.stanford.edu/people/ranjaykrishna/vrd/vrd.pdf)

#### Intro 

- visual appearance module, learns appearance of objects and predicates and fuses them together to jointly predict relationships 
- propose a language module, use pre-trained word vectors to cast relationships into vector, similar relationships are optimized to be close to each other


<!--- *********************************************************************************************************************************************** --->
--- 

### Deep Variation-structured Reinforcement Learning for Visual Relationship and Attribute Detection
[link](https://arxiv.org/pdf/1703.03054.pdf)

**Need to look into more carefully**

#### Intro 

- sequentially detect relationship and attribute instances by exploiting global context cues 
- ambiguity-aware object mining scheme to assign each object with the most appropriate category given the global scene context 
- VRL can be generalized into an unsupervised learning framework to learn from unlabeled images -> interesting 


<!--- *********************************************************************************************************************************************** --->
--- 

### Neural scene representation and rendering
[link](https://deepmind.com/blog/neural-scene-representation-and-rendering/)

#### Intro 

-



<!--- *********************************************************************************************************************************************** --->
--- 

### Neural Scene De-rendering
[link](http://nsd.csail.mit.edu/papers/nsd_cvpr.pdf)

#### Intro 

-


<!--- *********************************************************************************************************************************************** --->
--- 

### Picture: A Probabilistic Programming Language for Scene Perception
[link](https://mrkulk.github.io/www_cvpr15/1999.pdf)

#### Intro 

-



<!--- *********************************************************************************************************************************************** --->
--- 

### Configurable 3D Scene Synthesis and 2D Image Rendering with Per-Pixel Ground Truth using Stochastic Grammars
[link](https://arxiv.org/pdf/1704.00112.pdf)

#### Intro 

-


<!--- *********************************************************************************************************************************************** --->
--- 

### Visual Translation Embedding Network for Visual Relation Detection
[link](https://arxiv.org/pdf/1702.08319.pdf)

#### Intro 

- relation modeled as a vector translation, subject + predict ~ object 
- feature extraction layer for class probabilities, locations(bbox coordinates and scales), RoI visual features 

#### Modeling 

- projection matrices from feature space to relation space 
- use large-margn metriclearning loss function 


<!--- *********************************************************************************************************************************************** --->
--- 

### Neural Motifs: Scene Graph Parsing with Global Context
[link](https://arxiv.org/pdf/1711.06640.pdf)

**useful analysis to Visual Genome statistics**

#### Intro 

- motifs: regulary appearing substructures in scene graphs 
- key is to encode global context that can directly inform the local predictors 
- Visual Genome, predominant relations are geometric and possessive 
- use bidirectional LSTM to produce global contexts 


<!--- *********************************************************************************************************************************************** --->
--- 

### Tensorize, Factorize and Regularize: Robust Visual Relationship Learning
[link](http://pages.cs.wisc.edu/~hwkim/papers/cvpr2018_hwang.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### Scenic: Language-Based Scene Generation
[link](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2018/EECS-2018-8.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### Shuffle-Then-Assemble: Learning Object-Agnostic Visual Relationship Features
[link](http://openaccess.thecvf.com/content_ECCV_2018/papers/XU_YANG_Shuffle-Then-Assemble_Learning_Object-Agnostic_ECCV_2018_paper.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### PPR-FCN: Weakly Supervised Visual Relation Detection via Parallel Pairwise R-FCN
[link](https://arxiv.org/pdf/1708.01956.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Weakly-supervised learning of visual relations
[link](https://arxiv.org/pdf/1707.09472.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### MAttNet: Modular Attention Network for Referring Expression Comprehension
[link](https://arxiv.org/pdf/1801.08186.pdf)

#### Intro 

- decompose phrase into: subject appearance, location, relationship to other objects 
- 2 types of attention: language-based attention to learn module weights & word/phrase attention + visual attention 
- 


<!--- *********************************************************************************************************************************************** --->
--- 

### Context-Aware Visual Policy Network for Sequence-Level Image Captioning
[link](https://arxiv.org/pdf/1808.05864.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Learning to Compose Task-Specific Tree Structures
[link](https://arxiv.org/pdf/1707.02786.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### COCO-Stuff: Thing and Stuff Classes in Context
[link](https://arxiv.org/pdf/1612.03716.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### From Recognition to Cognition: Visual Commonsense Reasoning
[link](https://arxiv.org/pdf/1811.10830.pdf)



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

### 3D-Aware Scene Manipulation via Inverse Graphics
[link](http://papers.nips.cc/paper/7459-3d-aware-scene-manipulation-via-inverse-graphics.pdf)

**very similar idea**

#### Intro 

- interpreable expressive, disentangled (semantics, geometry, appearance) scene representation, contaisn comprehensive structural and textural information for each object
-  scene encoder for inverse graphics, decoder = differentiable shape renderer + neural texture generator
- 3D scene de-rendering networks (3D-SDN)

#### Modeling 

- semantic branch -> Dilated Residual Networks (DRN) for semantic segmentation 
- geometric branch -> Mask-RCNN for object proposal generation, 8 object meshes as car CAD models from ShapeNet 
- textural branch 
- VGG network as feature extractor 

#### Evaluation 

- evaluated on Virtual KITTI and Cityscapes 
- built **Virtual KITTI Image Editing Benchmark**
- learned representations can be useful for image reasoning, captining, analogy-making 

#### Future Work 

- handle uncommon object appearance and pose 
- deal with deformable shapes, e.g. human bodies 


<!--- *********************************************************************************************************************************************** --->
--- 

### Learning Hierarchical Semantic Image Manipulation through Structured Representations
[link](http://papers.nips.cc/paper/7536-learning-hierarchical-semantic-image-manipulation-through-structured-representations.pdf)

**very similar idea**


<!--- *********************************************************************************************************************************************** --->
--- 

### Probabilistic Neural Programmed Networks for Scene Generation
[link](https://papers.nips.cc/paper/7658-probabilistic-neural-programmed-networks-for-scene-generation.pdf)

#### Intro 

- dynamically programmable networks 


<!--- *********************************************************************************************************************************************** --->
--- 

### Learning to Compose Dynamic Tree Structures for Visual Contexts
[link](https://arxiv.org/pdf/1812.01880.pdf)

#### Intro 

- dynamically construct visual context tree 
- use bi-TreeLSTM for efficient context encoding 
- transform multi-branch tree to the equivalent left-child right-sibling binary tree
- scene graph detection is a high-level task and not yet reliable 
- visual contexts are inherently content-/task-driven, object layout should vary from content to content, question to question. 
- maintain a trainable task-specific score matrix of the objects, where each entry indicates the contextual validity of the pairwise objects
- trim a maximum spanning tree from the score matrix 
- the above VCTREE construct is discrete and non-differentiable -> REINFORCE for tree structure exploration & supervised learning for context encodding 

#### Future work 

- explore dynamic forest as the underlying context structure 


<!--- *********************************************************************************************************************************************** --->
--- 

### Scene Dynamics: Counterfactual Critic Multi-Agent Training for Scene Graph Generation
[link](https://arxiv.org/pdf/1812.02347.pdf)

**mind-blowing formulatoin**

#### Intro 

- existing methods exploit visual context by modeling message passing among objecats; scene dynamic is not properly learned by using the prevailing corss-entropy based supervised learning paradigm, which is not sensitive to graph inconsistency
- 2 inherent mismatches
    - coherent objective v.s. independent reward
    - local action v.s. global pooling reward 
- propose a communicative multi-agent model, objects are viewed as cooperative agents that maximize graph-level metrics such as Recall@K or SPICE
- after several rounds of communication, use a visual relationship detection model for scene graph generation that triggers graph-level reward by comparing generated scene graph with ground-truth 
- to disentangle reward of individual agent action, subtract a counterfactual baseline from the reward by varying the target agent while fixing others before feeding into the reward function 
- discardf the widely-used relatioship nodes, reduce message passing complexity 


<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 