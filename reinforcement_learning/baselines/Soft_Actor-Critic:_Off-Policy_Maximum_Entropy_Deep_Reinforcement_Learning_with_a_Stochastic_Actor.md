# Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor
[link](https://arxiv.org/pdf/1801.01290.pdf)

**SAC**

## Intro 

- major challenges: high sample complexity & brittle convergence properties 
- aim to maximize expected reward while also maximizing entropy 
- on-policy learing requires new samples t obe collecteed for each gradient step -> expensive, off-policy algorithms aim to reuse past experience 
- DDPG, a separate actor network is used to perform the maximization in Q-learning 
- combine off-policy training with a stochastic actor 

## Modeling 

- temperature parameter to control relative impotance of the entropy term against the reward -> control stochasticity of optimal policy  
- policy iteration: iterative policy evaluation (apply soft Bellman backup operator until convergence) + policy improvement 
- soft actor-critic: parameterized state value function + soft Q-function + tractable policy 
- soft value function trained to minimize the squared residual error 
- soft Q-function trained to minimize the soft Bellman residual (with targe value network) 
- policy learned by directly minimizing the expected KL-divergence for policy update/improvement 