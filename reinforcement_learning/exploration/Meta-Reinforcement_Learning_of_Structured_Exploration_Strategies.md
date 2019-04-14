# Meta-Reinforcement Learning of Structured Exploration Strategies
[link](https://arxiv.org/pdf/1802.07245.pdf)


## Intro 

- explore how prior tasks can in- form an agent about how to explore effectively in new situations

- prior experience is used both to initialize a policy and to acquire a latent exploration space that can inject structured stochasticity into a pol- icy,

- injects temporally correlated noise to randomize exploration strategies, but the way this noise is utilized and sampled is determined by a meta-learning process and informed by past experience

## Related work 

- intrinsic motivation
- Thompson sampling 
- information gain 
- parameter space exploration 


## Model 

- condition the policy on per-episode random variables drawn from a learned latent distribution



## Future work 

- combine with task-agnostic exploration strategies, e.g. intrinsic motivation 