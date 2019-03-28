# Rainbow: Combining Improvements in Deep Reinforcement Learning
[link](https://arxiv.org/pdf/1710.02298.pdf)

## Intro 

- examine combination DRL DQN extensions 
- **Double DQN**, addresses an overestimatino bias of Q-learning, decouple selection and evaluation of the bootstrap action 
- **Prioritized experience replay**, improves data efficiency, replay more often transitions
- **Dueling network**, generalize across actions by separately representing state values and action advantages 
- **Learning from multi-step bootstrap targets**
- **Distributional Q-learning**
- **Noisy DQN**, use stochastic network layers for exploration 