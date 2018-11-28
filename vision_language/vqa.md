### Datasets 

#### FigureQA
[link](https://datasets.maluuba.com/FigureQA)

#### NLVR
[link](http://lic.nlp.cornell.edu/nlvr/)

#### VQA 
[link](http://www.visualqa.org/)

#### CLEVR
[link](https://cs.stanford.edu/people/jcjohns/clevr/)


<!--- *********************************************************************************************************************************************** --->
--- 

### VQA: Visual Question Answering
[link](https://arxiv.org/pdf/1505.00468.pdf)

#### Intro 

- free-form, open-ended, amenable to automatic evaluation, answers provided in a multiple-choice format 
- motivation: iamge captioning is not "AI-complete", a coarse scene-level understanding of an image paired with word n-gram statistics suffices to generate reasonable image captions
- real images from COCO, abstract scenes, answers: open-answer or multiple-choice 


<!--- *********************************************************************************************************************************************** --->
--- 

### CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning
[link](https://arxiv.org/pdf/1612.06890.pdf)

#### Intro 

- existing VQA tasks and models fail to identity failure modes, propose this diagnostic dataset 
- contain simple 3D shapes, simply recognition and focus on reasoning skills 
- control question-conditional bias via rejection sampling within families of related questions 
- represent questions as **functional programs**, can be executed on an image's scene graph, yielding answers 
- CLEVR should be used in conjunction with other VQA datasets to study the reasoning abilities of models 
- contain two types of relationships: spatial and same-attribute 
- contain two question topoligies: chain-structured and tree-structured 

#### Evaluation 

- current systems fail in **short-term memory**
- current systems fail in **long reasoning chains**
- current systems fail in **spatial relationships**
- current systems fail in **disentangled representations** 


<!--- *********************************************************************************************************************************************** --->
--- 

### FiLM: Visual Reasoning with a General Conditioning Layer
[link](https://arxiv.org/pdf/1709.07871.pdf)

#### Intro 

- feature-wise affine transformation based on conditioning information 
- enable a RNN over an input question to influence CNN computation over an image 
- can be viewed as generalization of **Conditional Normalization methods**

#### Evaluation 

- appropriate feture modulation indirectly results in spatial modulation ~ spatial attention 
- 


<!--- *********************************************************************************************************************************************** --->
--- 