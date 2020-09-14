# RL: Exploration

---

## Lil'Log

[Exploration Strategies in Deep Reinforcement Learning](https://lilianweng.github.io/lil-log/2020/06/07/exploration-strategies-in-deep-reinforcement-learning.html)

### classical exploration strategies

- **Epsilon-greedy**: The agent does random exploration occasionally with probability $\epsilon$  and takes the optimal action most of the time with probability $1-\epsilon$.
- **Upper confidence bounds**: The agent selects the greediest action to maximize the upper confidence bound $\hat{Q}_t(a)+ \hat{U}_t(a)$, where $\hat{Q}_t(a)$ is the average rewards associated with action $a$ up to time  $t$ and $\hat{U}_t(a)$ is a function reversely proportional to how many times action $a$ has been taken. See [here](https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html#upper-confidence-bounds) for more details.
- **Boltzmann exploration**: The agent draws actions from a [boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution) (softmax) over the learned $Q$ values, regulated by a temperature parameter $\tau$.
- **Thompson sampling**: The agent keeps track of a belief over the probability of optimal actions and samples from this distribution. See [here](https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html#thompson-sampling) for more details.

### with neural networks for function approximation

- **Entropy loss term**: Add an entropy term $H(\pi(a|s))$ into the loss function, encouraging the policy to take diverse actions.
- **Noise-based Exploration**: Add noise into the observation, action or even parameter space

### key problems

- **hard-exploration problem**: refers to exploration in an environment with very sparse or even deceptive reward, e.g. Montezuma’s Revenge
- **Noisy-TV problem**:  Imagine that an RL agent is rewarded with seeking novel experience, a TV with uncontrollable & unpredictable random noise outputs would be able to attract the agent’s attention forever

### Intrinsic Rewards as Exploration Bonuses

- Discovery of novel states
- Improvement of the agent’s knowledge about the environment.
- **Count-based Exploration**
    - empirical count function $N_n(s)$
    - counting by density model (e.g. Context Tree Switching density model, PixelCNN, Gaussian Mixture Model)
    - counting after hashing
        - count high-dimensional states by mapping states into hash codes
        - hash function $\phi: S \rightarrow Z^k$
        - alternative hash functions: Locality-Sensitive Hashing (LSH), SimHash
- **Prediction-based Exploration**
    - agent’s familiarity with the environment dynamics can be estimated through a prediction model → to measure curiosity
    - Forward Dynamics
        - Learning a forward dynamics prediction model $f: (s_t, a_t) \rightarrow s_{t+1}$, or an emsemble of them
        - use prediction error or ensemble output variance as intrinsic reward
    - Random Networks
    - Physical properties prediction tasks
- problems with reward-based exploration
    - Function approximation is slow to catch up.
    - Exploration bonus is non-stationary.
    - Knowledge fading, meaning that states cease to be novel and cannot provide intrinsic reward signals in time.

### Memory-based Exploration

- Episodic Memory
    - Never Give Up (NGU)
        - combines an episodic novelty module that can rapidly adapt within one episode with RND as a lifelong novelty module.
        - *Rapidly discourages* revisiting the same state *within* the same episode;
        - *Slowly discourages* revisiting states that have been visited many times *across* episodes.
    - Agent57
        - A population of policies are trained, each equipped with a different exploration parameter pair $\{(\beta_j, \gamma_j)\}^N_{j=1}$ for exploration bonus weight $r_{j,t} = r_t^e + \beta_j r_t^i$ and reward discount factor
        - new parameterization of Q-value function that decomposes the contributions of the intrinsic and extrinsic rewards in a similar form as the bundled reward: $Q(s,a;\theta_j) = Q(s,a;\theta_j^e) + \beta_j Q(s,a;\theta_j^i)$
        - the two value function components are optimized separately with corresponding rewards
    - Episodic Curiosity (EC)
        - Instead of using the Euclidean distance to measure closeness of states in episodic memory, measure the number of steps needed to visit one state from other states in memory
        - novelty bonus depends on reachability between states.
- Direct Exploration
    - Go-Explore
    - policy-based Go-Explore
        - self-imitation learning (SIL) loss
    - Diverse Trajectory-conditioned Self-Imitation Learning (DTSIL)
        - maintains a memory of diverse demonstrations collected during training and uses them to train a trajectory-conditioned policy via SIL
        - prioritize trajectories that end with a rare state during sampling.

### Q-Value Exploration

- Bootstrapped DQN
    - inspired by Thompson sampling
    - Bootstrapping is to approximate a distribution by sampling with replacement from the same population multiple times and then aggregate the results.
- adding random prior into bootstrapped DQN for better exploration
    - use Bayesian linear regression
    - core idea of Bayesian regression is: We can “generate posterior samples by training on noisy versions of the data, together with some random regularization”.

### Variational Options

- Options are policies with termination conditions
- By explicitly including intrinsic options into modeling, the agent can obtain intrinsic rewards for exploration.
- Variational Intrinsic Control (VIC)
- Variational Auto-encoding Learning of Options by Reinforcement (VALOR)
    - relies on the whole trajectory to extract the option context
- Diversity is all you need (DIAYN)

---

## Papers

### Unifying Count-Based Exploration and Intrinsic Motivation

link: [http://arxiv.org/abs/1606.01868](http://arxiv.org/abs/1606.01868)  

---

### #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning

link: [http://arxiv.org/abs/1611.04717](http://arxiv.org/abs/1611.04717)  

---

### Never Give Up: Learning Directed Exploration Strategies

link: [http://arxiv.org/abs/2002.06038](http://arxiv.org/abs/2002.06038) 

---

### Episodic Curiosity through Reachability

link: [http://arxiv.org/abs/1810.02274](http://arxiv.org/abs/1810.02274) 

---

### Agent57: Outperforming the Atari Human Benchmark

link: [http://arxiv.org/abs/2003.13350](http://arxiv.org/abs/2003.13350) 

---

### Go-Explore: a New Approach for Hard-Exploration Problems

link: [http://arxiv.org/abs/1901.10995](http://arxiv.org/abs/1901.10995) 

---

### First return then explore

link: [http://arxiv.org/abs/2004.12919](http://arxiv.org/abs/2004.12919) 

---

### Self-Imitation Learning

link: [http://arxiv.org/abs/1806.05635](http://arxiv.org/abs/1806.05635)

---

### Self-Imitation Learning via Trajectory-Conditioned Policy for Hard-Exploration Tasks

link: [http://arxiv.org/abs/1907.10247](http://arxiv.org/abs/1907.10247) 

---

###