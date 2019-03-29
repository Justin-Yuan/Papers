# Scene Graph Generation from Objects, Phrases and Region Captions
[link](https://arxiv.org/pdf/1707.09700.pdf)

## Intro 

- 3 levels of scene understanding: object detection, scene graph generation, region captioning 
- Multi-level Scene Description Network (MSDN), solve the 3 tasks jointly
- leverage the spatial and semantic correlations of the visual features

## Modeling 

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

## Evaluation 

- Top-K recall, not using mAP since annotations of the relationships are incomplete, mAP will falsely penalize the positive but unlabeled predictions