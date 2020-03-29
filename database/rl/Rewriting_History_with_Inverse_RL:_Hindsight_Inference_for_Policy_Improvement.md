## Rewriting History with Inverse RL: Hindsight Inference for Policy Improvement

[link](https://arxiv.org/pdf/2002.11089.pdf)
[code]()

<!-- ***************************************************** -->
hindsight relabeling is inverse RL. key idea is to use inverse RL to infer task label for experiences and use them to train policy in multi-task setting.

maximum entropy (MaxEnt) RL and MaxEnt inverse RL optimize the same multi-task objective, one with respect to trajectories and one with respect to tasks.

MaxEnt inverse RL can be viewed as an inference problem, to calculte either the posterior distribution over reward functions or the maximum a-posteriori (MAP) estimate. MaxEnt RL can be viewed as minimizing an KL divergence.  

<!-- ***************************************************** -->
---
#### Key Points

- Given a prior over tasks $p(\phi)$, MaxEnt RL and MaxEnt inverse RL are maximizing the joint distribution over tasks and trajectories (from different factorizations) 
$$
p(\tau, \phi) = p(\phi)\frac{1}{Z(\phi)}p_1(s_1)\prod_t p(s_{t+1}|s_t,a_t)e^{r_{\phi}(s_t,a_t)}
$$
- partition function in inverse RL is important for hindsight relabeling since it will normalize the rewards from tasks with varying difficulty and reward scale.
- can use relabelled data for off-policy RL and behavior cloning

<!-- ***************************************************** -->
---
#### Results

- test on several mujoco tasks (goal reaching)

<!-- ***************************************************** -->
---
#### Notes/Questions

- mention task inference is ever-present in meta-learning, combining inserse RL into meta RL can be interestings

<!-- ***************************************************** -->
---
#### References

[1] Inverse Reward Design [link](https://arxiv.org/pdf/1711.02827.pdf)

[2] On Stochastic Optimal Control and Reinforcement
Learning by Approximate Inference [link](https://ipvs.informatik.uni-stuttgart.de/mlr/papers/12-rawlik-RSS.pdf)

