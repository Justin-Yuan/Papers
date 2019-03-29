# Scene Graph Generation by Iterative Message Passing
[link](http://vision.stanford.edu/pdf/xu2017cvpr.pdf)

## Intro 

- pass messages containing contextual information between a pair of bipartite sub-graphs of the scene graph, iteratively refine the predictions using RNN 
- can be considered as a more general framework for graph generation problem 

## Modeling 

- all nodes share the same GRU weights, all edges share the other set of GRU weights 
- a message pooling function to dynamically aggregate hidden GRU states into messages 
- disjoint sub-graphs: primal graph defines channels for passing message from edge GRUs to node GRUs, dual graph does the other way round 
- use mean field to perform approximate inference 
- randomly select 128 boxes from NMS as object proposals

## Evaluation 

- metrics
    - R@k, measures the fraction of ground-truth relationship triplets (subjectpredicate-object) that appear among the top k most confident triplet predictions in an image.
    - predicate classification (**PREDCLS**), predict the predicates of all pairwise relationships of a set of localized objects 
    - scene graph classification (**SGCLS**), predict the prediate as well as the object categories of the subject and the object in every pairwise relationship given a set of localized objects 
    - scene graph generation (**SGGEN**), detect a set of objects and predict the predicate between each pair of the detected objects. 
- performance of final model peaks at training with 2 iterations and degrades afterwards 