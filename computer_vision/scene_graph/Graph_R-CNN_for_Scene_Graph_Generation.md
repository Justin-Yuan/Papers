# Graph R-CNN for Scene Graph Generation
[link](https://arxiv.org/pdf/1808.00191.pdf)

## Intro 

- scene graph form an interpretable structured representation of the image that supports higher-level visual intelligence tasks 
- leverage object-relationship regularities 

## Modeling 

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

## Evaluation 

- recall of <subject, predicate, object> triplets (**SGGen**) 
- recall of objects and predicates given groud truth object localizations (**PredCls**, **PhrCls**)
- novel, more holistic metric (**SGGen+**), computes total recall for singleton entities (objects & predicates), pair entities <object, attribute>, triplet entities <subject, predicate, object>
- SGGen is overly sensitive to label errors on objects with relationships 