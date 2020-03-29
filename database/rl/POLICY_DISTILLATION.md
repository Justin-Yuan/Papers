## POLICY DISTILLATION

[link](https://arxiv.org/pdf/1511.06295.pdf)
[code]()

<!-- ***************************************************** -->
extract the policy of a reinforcement learning agent and train a new network that performs at the expert level while being dramati- cally smaller and more efficient.

consolidate multiple task-specific policies into a single policy. or applied as a real-time, online learning process by continually distilling the best policy to a target network.

show results on (a) single game distillation, (b) single game distillation with highly compressed models, (c) multi-game distillation, and (d) online distillation.

<!-- ***************************************************** -->
---
#### Key Points

- 3 ways to impose a loss functions over source logits and distilled output logits: NLL loss, MSE loss over vector of Q values and KL-divergence over softened logits (by using softmax with lower temperature :point_right: since Q values are similar, hope to make them sharper for different observation inputs)
- for multi-task distillation, the distillation agent then learns from the n data stores sequentially, switching to a different one every episode. Since different tasks often have different action sets, a separate output layer (called the controller layer) is trained for each task and the id of the task is used to switch to the correct output during both training and evaluation.

<!-- ***************************************************** -->
---
#### Results

- tested on several Atari games

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References



