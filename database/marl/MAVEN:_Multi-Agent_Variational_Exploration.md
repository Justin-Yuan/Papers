## MAVEN: Multi-Agent Variational Exploration

[link](https://arxiv.org/pdf/1910.07483.pdf)
[code](https://github.com/AnujMahajanOxf/MAVEN)

<!-- ***************************************************** -->
Operate in partial observability, QMIX cannot handle nonmonotonic Q functions. For a fixed time budget T, increasing QMIX’s exploration rate lowers its probability of learning the optimal action due to its representational limitations.

Extending from QMIX, the coupling of $\epsilon$-greedy exploration and representational limitations of monotonic mixing function leads to poor exploration. 

propose to condition agent value function on a sampled latent (inputs are episode initial state and a random discrete/continuous variable) to produce distinctive greedy behaviors (also to simulate committed exploration). 

train the latent as a hierarchical policy with policy gradient (fixing other parameters) and with mutual information maximization between the sampled latent and the encoded episode. 

use variational distribution to approximate entropy of latent conditioned on encoded episode to bypass intractability. 



<!-- ***************************************************** -->
---
#### Key Points

- 

<!-- ***************************************************** -->
---
#### Results

- test ton a simple m-step matrix game 
- test on SMAC benchmark suite, with additional environments to assess multi-agent exploration techniques (2-corridors) and to test state exploration (zealot_cave)
- plot t-SNE of initial states colored by sampled latent across time steps. show latentss partition the state-action space with distinct joint behaviors.

<!-- ***************************************************** -->
---
#### Notes/Questions

- future work includes theoretical analysis, evaluation on continuous latent and condition the latent per time step (perhaps shared across agents :point_right: low communication cost, centralized execution).

<!-- ***************************************************** -->
---
#### References

[1] QTRAN: Learning to Factorize with Transformation for
Cooperative Multi-Agent Reinforcement learning [link](https://arxiv.org/pdf/1905.05408.pdf)

