### Data-Efficient Hierarchical Reinforcement Learning 
[link](https://arxiv.org/pdf/1805.08296.pdf)

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

#### Intro 

-



<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 






<!--- *********************************************************************************************************************************************** --->
--- 