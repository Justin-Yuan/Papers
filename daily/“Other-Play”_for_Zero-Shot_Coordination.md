## “Other-Play” for Zero-Shot Coordination

[link](https://arxiv.org/pdf/2003.02979.pdf)
[code](https://colab.research.google.com/drive/19O0Uv6K2I3FZZqTL6tuNr2gpJbAMC854)

<!-- ***************************************************** -->
zero-shot coordination is about constructing agents that can coordinate with novel partners they have not seen before. 

assume Markov Game provided a set of symmetries (arbitrary relabelings of the state/action space that leave trajectories unchanged up to relabeling).

Other-Play's goal is to find a strategy that is maximally robust to partners breaking symmetries in different ways while still playing in the same class. 

Self-Play may reach inefficient equilibria since agents can arbitrary decide how to break symmetries together but might fail when faced with new agents.

connection with domain randomization: a policy should be invariant to how an agent's partner breaks symmetries in the underlying game. 

<!-- ***************************************************** -->
---
#### Key Points

- equivariance mapping $\phi \in \Phi, {\phi_{S}, \phi_{A}, \phi_{O}}$, now the OP objective is 
$$
\pi^{*} = argmax_{\pi}E_{\phi \sim \Phi} J(\pi^1, \phi(\pi^2))
$$

<!-- ***************************************************** -->
---
#### Results

- test on Lever Game and Hanabi 
- also tried multi-agent adaptations of **cognitive hierarchies**, **k-level reasoning** and population training, none has yield better results. 

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References



