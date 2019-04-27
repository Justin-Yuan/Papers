# TACO: Learning Task Decomposition via Temporal Alignment for Control
[link](http://proceedings.mlr.press/v80/shiarlis18a/shiarlis18a.pdf)


- extend CTC by combining sequence alignment an behavioral cloning 

- problem for behavioral cloning: covariate shift --> when small errors during testing cause the agent to drift away from states it encountered during training, yielding poor performance

- using disturbances for augmenting robot trajectories (DART)

- task sketch, each element comes from a dictionary of sub-tasks, the sketch indicates which sub-tasks are active in a trajectory

- simultaneously optimize the alignment between trajectory ρ and task sequence τ and learns theunderlying policies
