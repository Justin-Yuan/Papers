# IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures
[link](https://arxiv.org/pdf/1802.01561.pdf)

## Intro 

- solve a large collection of tasks with a single agent 
- stable learning & high throughput by combining decoupled acting and learning with off-policy correction method **V-trace**
- IMPALA actors communicate trajectoriesof excperience to a centralized learner 
- policy lag between actors and learners

## Modeling 

- on-policy case, V-trace reduces to on-policy n-steps Bellman update 
- the truncated importance sampling weights, similar to "trace cutting" coefficients in **Retrace**, the product of them measures how much a temporal difference for V observed at time t impacts the update of the value function at a previous time s