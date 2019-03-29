# Image Generation from Scene Graphs
[link](https://arxiv.org/pdf/1804.01622.pdf)

## Intro 

- challenges:
    - method to process graph-structured input 
    - ensure generated images respect the objects and relationships specified in graph 
    - ensure synthesized images are realistic
- use graph convolution to process input graphs
- compute a scene layout by predicting bounding boxes and segmentation masks for objects
- convert layout to image with cascaded refinement network 
- train adversarially against a pair of discriminator networks 
- evaluate with Amazon Mechanical Turk, compared to StackGAN 

## Modeling 

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