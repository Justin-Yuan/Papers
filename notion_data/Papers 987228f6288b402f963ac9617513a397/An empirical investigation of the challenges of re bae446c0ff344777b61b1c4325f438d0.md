# An empirical investigation of the challenges of real-world reinforcement learning

Created: Sep 10, 2020 7:26 AM
Institute: Deepmind
Tags: read, real-world rl

High-levels 

## Aim

- identify challenges for real-world RL deployment, analyze effects and state-of-the-art algorithms, purposed environment **realworldrl-suite**

![An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled.png](An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled.png)

- learning algorithms use DMPO and D4PG
- realworldrl-suite includes 7 DeepMind Control Suite tasks
    - cartpole:swingup & balance,
    - walker:walk & run
    - quadruped:walk & run
    - humanoid:walk & stand

## Conclusion

- offline learning and safety constraints are particularly important
- proposed metrics for efficiency (performance regret and stability) show interesting findings
- observation and action delays quickly degrade algorithm performance, but reward delays have less impact globally

## Background

- related work: bsuite, Safety Gym

---

Main body & details 

## Methods

- Learning on the real system from limited samples
    - evaluation metric: normalized regret w.r.t to the performance of final policy
        - interpreted as amount of actual return lost, prior to convergence

        ![An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled%201.png](An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled%201.png)

    - evaluation metric once converged: instability regret
        - quantify how much policy performance drops below the lower confidence interval after convergence

        ![An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled%202.png](An%20empirical%20investigation%20of%20the%20challenges%20of%20re%20bae446c0ff344777b61b1c4325f438d0/Untitled%202.png)

- System delays
    - implements delays in observation, action and reward with an n-step buffer between the environment and the agent.
    - An action delay is defined here as delaying the agent’s action execution for n timesteps, whereas an observation/reward delay is defined as withholding an agent’s observation/reward for n timesteps.
- High-dimensional continuous state and action spaces
    - add dummy state variables sampled from a standard Gaussian
    - the additional dummy dimensions slightly affect convergence speed indicating that the learning algorithm learns to deal with noise efficiently, but it does slow down learning progress
- Satisfying environmental constraints
    - 
- 

## Results

- 

---

Thoughts during readings, pros & cons, connection to your own research 

## Comments

- 

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