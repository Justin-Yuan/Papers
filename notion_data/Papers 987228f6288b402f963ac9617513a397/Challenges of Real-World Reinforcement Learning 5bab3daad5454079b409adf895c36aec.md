# Challenges of Real-World Reinforcement Learning

Created: Sep 10, 2020 7:29 AM
Institute: Deepmind, Google Brain
Tags: read, real-world rl

High-levels 

## Aim

- 9 challenges to productionize RL

![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled.png)

- learning needs data from real system, due to lack of available simulators
- robust evaluation is required, e.g. safety

## Conclusion

- presented 9 challenges, with their motivation, examples, formulation and references
- presented an example environment and evaluation criteria

## Background

- MDP, general RL formulation

---

Main body & details 

## Methods

- Batch off-line and off-policy training
    - need to ensure new policy improves upon previous policy → estimate policy's performance without running on the real system → **off-policy evaluation**
        - importance sampling, learn a transition model, doubly-robust estimators, etc
    - warm-start performance of a new learning algorithm given behavior policy's data is also important

![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%201.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%201.png)

- Learning on the real system from limited samples
    - exploration in real system is limited → sample efficiency
        - quick adaptation, e.g. MAML, Bootstrap DQN
        - use expert demonstrations, model-based methods
    - metric for data efficiency

        ![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%202.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%202.png)

- High-dimensional continuous state and action spaces
    - Action Elimination Deep Q Networks, Deep Reinforcement Relevance Network, etc
    - propose to evaluate policy performance according to number of actions and relation over the actions
- Satisfying safety constraints
    - safety is important during system operation and exploratory learning
    - formulated as constrained MDPs, constrained optimization problem

        ![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%203.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%203.png)

    - formulated as budgeted MDPs, allows trade-off between safety violation and reward gain

        ![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%204.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%204.png)

    - addition of safety layer to the network
    - use Lyapunov functions to learn safe policies and exploration
    - evaluate safety by counting safety violations for each individual constraints
- Partial observability and non-stationarity
    - partially observable MDPs
    - incorporate history into observation or use recurrent network to track hidden state
    - transfering learnt policies from simulation to real system, need to deal with noisy, non-stationary systems
        - robust MDP

        ![Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%205.png](Challenges%20of%20Real-World%20Reinforcement%20Learning%205bab3daad5454079b409adf895c36aec/Untitled%205.png)

        - domain randomization → policy robust against various perturbations during training
        - system identification → policy determine online the environment
    - evaluate policy with average test performance across K perturbed test environments
    - evaluate policy on a stream of constantly changing environment perturbations and its ability to adapt online
- Unspecified and multi-objective reward functions
    - policy should perform well for all task instances (full distribution of reward), not just in expectation
        - conditional value at risk (CVaR), looks at a given percentile of the reward distribution
        - distributional DQN
    - recover the underlying reward function from demonstrations, e.g. inverse RL
    - multi-objective reward functions
        - pareto-optimal reward function
        - need to track performance for each component
- Explainability
- Real-time inference
- System Delays

## Results

- DeepMind control suite, humanoid task
    - proposed a bunch of settings for each challenge above

---

Thoughts during readings, pros & cons, connection to your own research 

## Comments

- offline RL, sample efficiency and safety problem seem to be most urgent for RL production
- could pay extra attention in making simulation/experiment, so that the above challenges are in consideration and can be evaluated

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