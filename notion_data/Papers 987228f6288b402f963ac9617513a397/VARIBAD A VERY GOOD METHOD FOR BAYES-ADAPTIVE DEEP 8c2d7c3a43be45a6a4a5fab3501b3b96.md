# VARIBAD: A VERY GOOD METHOD FOR BAYES-ADAPTIVE DEEP RL VIA META-LEARNING

Created: Sep 11, 2020 4:07 AM
Tags: bayes-rl, meta-rl, read, rl exploration

High-levels 

## Aim

- learn approximate, tractable Bayes-optimal policy for a given distribution of tasks for better exploration exploitation trade-off
- use meta-learning, policy leverages task uncertainty by using an inferred task embedding

## Conclusion

- works in gridwork environment, learnt policy matches with Bayes-optimal policy
- scales to Mujoco tasks
- opens a path to tractable approximate Bayes-optimal exploration for RL

## Background

- multi-task meta-learning, distribution over MDPs
- Bayesian RL, Bayes-Adaptive MDP

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled.png)

- posterior sampling

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%201.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%201.png)

- Bayes-optimal policy

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%202.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%202.png)

---

Main body & details 

## Methods

- distribution of transition and reward functions → transition and reward function that condition on a task embedding 11
- learn a model of the environment (decoder) and the amortized inference network (encoder, for task embedding)

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%203.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%203.png)

- use variational lower bound (ELBO) to optimize the above objective

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%204.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%204.png)

- learn policy and VAE together, although samples can be separate

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%205.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%205.png)

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%206.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%206.png)

## Results

- grid world for navigating to a goal with periodic reset in an episode
    - agent learnt to update posterior over cells, learnt policy explores first and is optimal afterwards after locating the goal
    - task latent converges after goal is located

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%207.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%207.png)

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%208.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%208.png)

- Mujoco HalfCheetahDir (run forward or backward, 2 tasks), HalfCheetahVel (run at different velocities, infinite tasks)
    - variBAD adapts quickly (after a single rollout)

![VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%209.png](VARIBAD%20A%20VERY%20GOOD%20METHOD%20FOR%20BAYES-ADAPTIVE%20DEEP%208c2d7c3a43be45a6a4a5fab3501b3b96/Untitled%209.png)

---

Thoughts during readings, pros & cons, connection to your own research 

## Comments

- still unsure of the motivation for Bayes-optimal policy (fast adaptation, exploration?)
    - the Bayesian part is not obvious enough? use 1 sample for inferred transition and reward function seems inadequate, a non-Bayes version just to claim inferring a task embedding to condition policy on seems to make sense just fine
- the significance of decoding not only the past but also future states, given action up to time t is not experimentally justified
- mentioned extending variBAD to off-policy methods

---

Reasons why your read this ? why you take notes ? 

## Why

- [ ]  literature research
- [x]  experiment design
- [x]  writing guide

---

Links to relevant resources 

## References

-