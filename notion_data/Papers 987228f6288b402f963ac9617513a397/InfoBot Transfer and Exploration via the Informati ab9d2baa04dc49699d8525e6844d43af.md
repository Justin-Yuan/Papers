# InfoBot: Transfer and Exploration via the Information Bottl\eneck

Created: Sep 10, 2020 8:19 AM
Tags: read, rl exploration

High-levels 

## Aim

- effecitve exploration shoud seek out **decision states** in the absense of useful reward signals
- decision states are those in the state space from where the agent can transition to new, potentially unexplored regions.
- train a goal-conditioned policy with information bottleneck to find these decision states
    - to not overfit to any individual goal, minimize policy dependence on individual goal, quantified by conditional mutual information $I(A;G|S)$
    - argue with **default policy**, $\pi_0(A|S) = \Sigma_gp(g)\pi_{\theta}(A|S,g)$, agents follows default policy until encountering decision states, where goal information is needed
    - train a policy with information bottleneck → then use it to provide exploration bonus to train a new policy

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled.png)

- claim that in new environment, agent can identify novel sobgoals

## Conclusion

- better direct policy transfer across tasks
- claim better than count-based bonus, VIME and curiosity

## Background

- subgoals in options framework, the connection between action-goal information and the structure of decision-making
- bottleneck state in hierarchical RL
- different RL exploration strategies

---

Main body & details 

## Methods

- objective

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%201.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%201.png)

- policy is a encoder + ecoder, integration uses a single sample

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%202.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%202.png)

- data processing inequality

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%203.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%203.png)

- maximize objective lower bound

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%204.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%204.png)

- use variational approximation for the marginalization $p(Z|S)$ , use unit Gaussian in practice

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%205.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%205.png)

- on-policy learning, update step is

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%206.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%206.png)

- use trained encoder and variational approximation to provide exploration bonus

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%207.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%207.png)

- algorithm

![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%208.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%208.png)

## Results

- MiniGrid environments, MultiRoomNXSY and FindObjSY tasks
    - direct policy transfer, train policy, evaluate on larger versions of tasks
        - beats goal-conditioned A2C
    - transferable exploration, train policy, use it to guide exploration for new policy
        - beats goal-conditioned A2C, TRPO+VIME, count based and curiosity based exploration on larger task, on par on small task
- partially observedgoal based MiniPacMan, navigate to reach goal
    - overall the best, notably beats curiosity, Feudal RL (hierarchical)
    - also demonstrate potential to help combine model-based and model-free RL

    ![InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%209.png](InfoBot%20Transfer%20and%20Exploration%20via%20the%20Informati%20ab9d2baa04dc49699d8525e6844d43af/Untitled%209.png)

---

Thoughts during readings, pros & cons, connection to your own research 

## Comments

- interesting, guided principle on RL exploration, optimization seems a bit loose (could use tighter bounds?)
- results mostly with goal navigation based tasks, could extend to other multi-task settings?
- might be useful to apply information guided principle on decentralized decision making problems
- also think about how multi-agent exploration can be improved ?
- and also the role of exploration in a transfer setting, where fast adaptation is needed with only limited online interactions ?

---

Reasons why your read this ? why you take notes ? 

## Why

- [ ]  literature research
- [ ]  experiment design
- [ ]  writing guide

---

Links to relevant resources 

## References

-