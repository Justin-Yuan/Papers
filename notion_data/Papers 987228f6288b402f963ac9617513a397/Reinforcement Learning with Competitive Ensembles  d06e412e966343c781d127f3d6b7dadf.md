# Reinforcement Learning with Competitive Ensembles of Information-Constrained Primitives

Created: Sep 10, 2020 8:20 AM
Tags: read, rl skills

High-levels 

## Aim

- action primitives decide for themselves whether to act in the current state
- use information-theoretic mechanism to enable decentralized decision making

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled.png)

- key motivation

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%201.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%201.png)

- constraining amount of accessible information for primitives, based on variational information bottleneck
- act as meaningful factorization of policy and effective decision mechanism

## Conclusion

- better transfer than flat policies and hierarchical RL baselines
- useful for continual learning settings, e.g. add more primitives policies over time

## Background

- hierarchical RL, Options framework
- information bottleneck

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%202.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%202.png)

---

Main body & details 

## Methods

- 3 components

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%203.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%203.png)

- 1st component, each primitive has an information bottleneck with respect to the input state
    - use 1 sample for the integration

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%204.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%204.png)

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%205.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%205.png)

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%206.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%206.png)

- 2nd component, use $L_k$ to construct weights so primitives can compete
    - environment reward is distributed according to their participation in the global decision
    - force different primitives to encode and focus on different parts of the state space

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%207.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%207.png)

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%208.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%208.png)

- 3rd component, introduce regularization term to encourage diverse primitives and to prevent primitives collapse

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%209.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%209.png)

- primitives can be reused and recombined

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%2010.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%2010.png)

![Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%2011.png](Reinforcement%20Learning%20with%20Competitive%20Ensembles%20%20d06e412e966343c781d127f3d6b7dadf/Untitled%2011.png)

## Results

- Minigrid for multi-task learning(Pickup, Unlock, UnlockPickup)
- Mujoco ant maze
- motion imitation tasks with a 2D biped character and motion capture clips from human actors

---

Thoughts during readings, pros & cons, connection to your own research 

## Comments

- interesting idea for decentralized control, information guided formulation seems well justified
- but performance doesn't seem impressive, and quantitative results seem insufficient and qualitative results are hard to interpret
- consider other RL skill learning baselines to compare with? (especially information guided ones)

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