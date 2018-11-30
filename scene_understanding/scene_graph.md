### Datasets 

#### Visual Genome 
[link](https://visualgenome.org/)

#### COCO-Stuff 
[link](https://github.com/nightrome/cocostuff)

#### Visual Relationship Detection
[link](https://cs.stanford.edu/people/ranjaykrishna/vrd/)


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


#### Modeling 




<!--- *********************************************************************************************************************************************** --->
--- 

### Scene Graph Generation from Objects, Phrases and Region Captions
[link](https://arxiv.org/pdf/1707.09700.pdf)



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

### Generating Semantically Precise Scene Graphs from Textual Descriptions for Improved Image Retrieval
[link](http://anthology.aclweb.org/W/W15/W15-2812.pdf)





<!--- *********************************************************************************************************************************************** --->
--- 

### Visual Relationship Detection with Language Priors
[link](https://cs.stanford.edu/people/ranjaykrishna/vrd/vrd.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 

### Deep Variation-structured Reinforcement Learning for Visual Relationship and Attribute Detection
[link](https://arxiv.org/pdf/1703.03054.pdf)





<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 