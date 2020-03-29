## Continuous Deep Q-Learning with Model-based Acceleration

[link](https://arxiv.org/pdf/1603.00748v1.pdf)
[code](https://github.com/ikostrikov/pytorch-ddpg-naf)

<!-- ***************************************************** -->
use Q-learning on continuous action task (normalized advantage functions, NAF), represents action value function in way for easier argmax operation.

use learned models to generate imaginary rollouts for better sample efficiency. help fix Q function better by exposing it to both good and bad tranasitions.

<!-- ***************************************************** -->
---
#### Key Points

- the imaginaary rollouts approach is similar to *Dyna-Q*
- normal Q-learning requires maximizing a complex, non-linear function at each Bellman update; NAF parameters $Q(s,a) = V(s) + A(s,a)$ where $A(s,a) = -(a - \mu(s))P(s)(a - \mu(s))^T$, P is a positive-definite matrix parameteried by a lower triangluar matrix output by neural net.
- most of benefit of model-based learning is at early stage of the learning process.
- iteratively refit time-varying linear models (for learning the dynamic model).

<!-- ***************************************************** -->
---
#### Results

- test on severala mujoco tasks, DDPG causes the tip to fluctuate continuously around the tar- get, and does not reach it precisely while NAF is smoother. 

<!-- ***************************************************** -->
---
#### Notes/Questions

- sample efficiency is higher, but is performance worse than policy gradient or actor-critic?

<!-- ***************************************************** -->
---
#### References



