### Data-Efficient Hierarchical Reinforcement Learning 
[link](https://arxiv.org/pdf/1805.08296.pdf)

**HIRO**

#### Intro 

- lower-level controllers are supervised with goals learned and proposed automatically by the higher-level contorllers 
- use off-policy experience for both higher- and lower-level training 
- high-level actions be goal states and reward the lower-level policy for performing actions which yield it an observation close to matching the desired goal 
- non-stationary problem for high-level policy -> re-label an experience in the past with a high-level action chosen to maximize the probability of the past lower-level actions 
- use states as goals directly 
- off-policy training with correction -> sample-efficient 

#### Modeling 

- temporal difference learning, from state-action-reward (next state) transition tuples 
- use TD3, variant of DDPG
- deterministic neural network policy + state-action Q-function; Q trained using average Bellman error over all sampled transitions; policy trained to yield actions which maximize Q-value at each state; its behavior policy is augmented with Gaussian noise 
- TD3 use an ensemble over Q-value models and add noise to policy when computing target value in average Bellman error 
- use parameterized reward functins to specify a potentially infinite set of lower-level policies, an intrinsic reward the higher-level policy gives to lower-level policy 
- correct goals from past experience to match what's likely to result in the same lower-level action under current policy 


<!--- *********************************************************************************************************************************************** --->
--- 

### Addressing Function Approximation Error in Actor-Critic Methods
[link](https://arxiv.org/pdf/1802.09477.pdf)

**TD3**

#### Intro 

- value-based RL, function approximation errors lead to overestimated value estimates and suboptimal policies, such problem persists in actor-critic setting 
- use double Q-learning, take minimum value between a pair of critics to limit overestimation 
- delay policy updates to reduce per-update error 
- build on DDPG -> Twin Delayed DDPG (TD3) 
- result of estimation error: overestimation bias & high variance build-up 
 
#### Modeling 

- slow-changing policy in AC, the current and target networks are too similar to make an independent estimatino -> pairs of actors and critics 
- upper-bound the less biased value estimate by the biased estimate -> taking minimum between the 2 estimates
- induce underestimation bias, more preferable since value of underestimated actions will not be explicitly propagated through policy update 
- by sufficiently delaying policy updates, limit the likehood of repeating updates with respect to an unchanged critic -> two-timescale algorithm 
- target policy smoothing -> approximate edpe3ctation over actions by adding random noise to target policy and average over mini-batches 


<!--- *********************************************************************************************************************************************** --->
--- 

### Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor
[link](https://arxiv.org/pdf/1801.01290.pdf)

**SAC**

#### Intro 

- major challenges: high sample complexity & brittle convergence properties 
- aim to maximize expected reward while also maximizing entropy 
- on-policy learing requires new samples t obe collecteed for each gradient step -> expensive, off-policy algorithms aim to reuse past experience 
- DDPG, a separate actor network is used to perform the maximization in Q-learning 
- combine off-policy training with a stochastic actor 

#### Modeling 

- temperature parameter to control relative impotance of the entropy term against the reward -> control stochasticity of optimal policy  
- policy iteration: iterative policy evaluation (apply soft Bellman backup operator until convergence) + policy improvement 
- soft actor-critic: parameterized state value function + soft Q-function + tractable policy 
- soft value function trained to minimize the squared residual error 
- soft Q-function trained to minimize the soft Bellman residual (with targe value network) 
- policy learned by directly minimizing the expected KL-divergence for policy update/improvement 


<!--- *********************************************************************************************************************************************** --->
--- 

### A Distributional Perspective on Reinforcement Learning
[link](https://arxiv.org/pdf/1707.06887.pdf)

**inpiring work**

#### Intro 



<!--- *********************************************************************************************************************************************** --->
--- 

### IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures
[link](https://arxiv.org/pdf/1802.01561.pdf)

#### Intro 

- solve a large collection of tasks with a single agent 
- stable learning & high throughput by combining decoupled acting and learning with off-policy correction method **V-trace**
- IMPALA actors communicate trajectoriesof excperience to a centralized learner 
- policy lag between actors and learners

#### Modeling 

- on-policy case, V-trace reduces to on-policy n-steps Bellman update 
- the truncated importance sampling weights, similar to "trace cutting" coefficients in **Retrace**, the product of them measures how much a temporal difference for V observed at time t impacts the update of the value function at a previous time s


<!--- *********************************************************************************************************************************************** --->
--- 

### Rainbow: Combining Improvements in Deep Reinforcement Learning
[link](https://arxiv.org/pdf/1710.02298.pdf)

#### Intro 

- examine combination DRL DQN extensions 
- **Double DQN**, addresses an overestimatino bias of Q-learning, decouple selection and evaluation of the bootstrap action 
- **Prioritized experience replay**, improves data efficiency, replay more often transitions
- **Dueling network**, generalize across actions by separately representing state values and action advantages 
- **Learning from multi-step bootstrap targets**
- **Distributional Q-learning**
- **Noisy DQN**, use stochastic network layers for exploration 


<!--- *********************************************************************************************************************************************** --->
--- 

### Visual Reinforcement Learning with Imagined Goals
[link](https://arxiv.org/pdf/1807.04742.pdf)

#### Intro 

- combine unsupervised representatino learning and reinforcement leraning of goal-conditioned policies 
- agent performs a self-supervised phase where it imagines goals and attempts to achieve them 
- learn a visual representation that 
	- sample goals for self-supervised practice 
	- provide structured transformation of raw sensory inputs 
	- compute a reward signal for goal reaching (provide meaningful distances than that in the original observation space)
- visual representation -> learned latent variable model, VAE 
- retroactive goal relabeling scheme 

#### Modeling 

- embed the state and goals into a latent space Z using an encoder, train a beta-VAE while executing a random policy and collecting state observations 
- use **TD3** as backbone 
- use the **negative Mahalanobis distance** in the latent space 
- could potentially convert a triplet (state, action, next state) transition into infinitely many valid training data by generating a new goal and new reward 
- similarity with **Hindsight experience replay (HER)**, but here half of the goals generated from the prior and half from goals seen along the trajectory 


<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 