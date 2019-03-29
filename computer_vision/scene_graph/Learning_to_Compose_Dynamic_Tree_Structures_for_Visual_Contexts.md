# Learning to Compose Dynamic Tree Structures for Visual Contexts
[link](https://arxiv.org/pdf/1812.01880.pdf)

## Intro 

- dynamically construct visual context tree 
- use bi-TreeLSTM for efficient context encoding 
- transform multi-branch tree to the equivalent left-child right-sibling binary tree
- scene graph detection is a high-level task and not yet reliable 
- visual contexts are inherently content-/task-driven, object layout should vary from content to content, question to question. 
- maintain a trainable task-specific score matrix of the objects, where each entry indicates the contextual validity of the pairwise objects
- trim a maximum spanning tree from the score matrix 
- the above VCTREE construct is discrete and non-differentiable -> REINFORCE for tree structure exploration & supervised learning for context encodding 

## Future work 

- explore dynamic forest as the underlying context structure 