# Compositional Imitation Learning: Explaining and executing one task at a time 
[link](https://arxiv.org/pdf/1812.01483.pdf)

## Intro 

jointly learning to segment, explain, and imitate agent behavior (from demonstrations) via an unsupervised auto-encoding objective

The encoder learns to jointly infer event boundaries and high-level abstractions (latent encodings) of activity within each event segment, while the task of the decoder is to reconstruct or imitate the original behavior by executing the inferred sequence of latent codes

address segmentation problem by predicting soft segment masks 

## Related work 

option discovery 
