# Scene Graph Generation by Belief RNNs
[link](http://www.cs.tau.ac.il/~joberant/teaching/advanced_nlp_spring_2018/past_projects/scene_graph.pdf)

**model not powerful enough**

## Intro 

- model infers directly on the beliefs (not taking into account the visual features), which is more generic
- feature extraction module + belief RNNs module 

## Modeling 

- 2 ResNet50 to predict objects and predicates separately, unary and pairwise beliefts taken from the last layer before softmax 
- a sequence of RNNs, inputs predicates and object beliefs, output a new improved predicates and objects beliefs 