# Addressing Function Approximation Error in Actor-Critic Methods
[link](https://arxiv.org/pdf/1802.09477.pdf)

**TD3**

## Intro 

- value-based RL, function approximation errors lead to overestimated value estimates and suboptimal policies, such problem persists in actor-critic setting 
- use double Q-learning, take minimum value between a pair of critics to limit overestimation 
- delay policy updates to reduce per-update error 
- build on DDPG -> Twin Delayed DDPG (TD3) 
- result of estimation error: overestimation bias & high variance build-up 
 
## Modeling 

- slow-changing policy in AC, the current and target networks are too similar to make an independent estimatino -> pairs of actors and critics 
- upper-bound the less biased value estimate by the biased estimate -> taking minimum between the 2 estimates
- induce underestimation bias, more preferable since value of underestimated actions will not be explicitly propagated through policy update 
- by sufficiently delaying policy updates, limit the likehood of repeating updates with respect to an unchanged critic -> two-timescale algorithm 
- target policy smoothing -> approximate edpe3ctation over actions by adding random noise to target policy and average over mini-batches 