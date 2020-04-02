## ICLR 2020 MARL

[link](https://zhuanlan.zhihu.com/p/90393651)
[link](https://chillee.github.io/OpenReviewExplorer/)
[blog](https://sites.google.com/view/learning-to-simulate/home)

<!-- ***************************************************** -->
Papers on Multi-agent Reinforcement Learning, covering topics on 
- emergent communication
- multi-agent cooperation 
- multi-agent exploration 
- game theoretic perspective to multi-agent learning
- transfer learning 

<!-- ***************************************************** -->
---
#### List of Works
- [XX](#1)
- [YY](#2)

<!-- ***************************************************** -->
---
#### Work Summaries

<a name="1"></a> 
:+1: SIMPLIFIED ACTION DECODER FOR DEEP MULTI-AGENT REINFORCEMENT LEARNING

[link](https://arxiv.org/pdf/1912.02288.pdf)

- allows other agents to not only observe the (exploratory) action chosen, but agents instead also observe the greedy action of their team mates.
-  commonly required to reason over the intents, points of views and beliefs of other agents from observing their actions.
- On the one hand, an RL agent needs to explore in order to discover good policies through trial and error. On the other hand, when carried out naively, this exploration will add noise to the policy of the agent during the training process, making their actions strictly less informative to their team mates.
- optionally train an auxiliary task that predicts key hidden game properties from the action-observation trajectories.


--- 
<a name="2"></a> 
IN:+1: FLUENCE-BASED MULTI-AGENT EXPLORATION

[link](https://arxiv.org/pdf/1910.05512.pdf)

- present two exploration methods: exploration via information-theoretic influence (EITI) and exploration via decision-theoretic influence (EDTI), by exploiting the role of interaction in co- ordinated behaviors of agents.
- EITI uses mutual information to capture influence transition dynamics.
- EDTI uses a novel intrinsic reward, called Value of Inter- action (VoI), to characterize and quantify the influence of one agent’s behavior on expected returns of other agents.
- draws a connection between coordinated exploration and intrinsic reward distribution.
- propose exploration strategies where agents start with decentralized exploration driven by their individual curiosity, and are also encouraged to visit interaction points to influence the ex- ploration processes of other agents and help them get more extrinsic and intrinsic rewards. 
- also imply that these influential states are implicitly discovered as subgoals in search space that guide and coordinate exploration.
- **need further read on details of the two exploration metrics**


--- 
<a name="3"></a> 
:+1: CM3: COOPERATIVE MULTI-GOAL MULTI-STAGE MULTI-AGENT REINFORCEMENT LEARNING

[link](https://arxiv.org/pdf/1809.05188.pdf)

- a novel two-stage curricu- lum, in which single-agent goal attainment is learned prior to learning multi-agent cooperation.
- derive a new multi-goal multi-agent policy gradient with a credit function for localized credit assignment.
- use a function augmentation scheme to bridge value and policy functions across the curriculum. 
- the multi-goal scenario can benefit from fine-grained credit assignment that leverages available structure in action-goal interactions.
- first training an actor-critic pair to achieve different goals in an induced single-agent setting (Stage 1), then using them to initialize all agents in the multi-agent environment (Stage 2). 
- reduce the number of trainable parameters of the actor-critic in Stage 1 by limiting their input space to the part that is sufficient for single-agent training, then augment the architecture in Stage 2 with additional inputs and trainable parameters for learning in the multi-agent environment.
- propose a credit function, which is an action-value function that specifically evaluates action- goal pairs, for localized credit assignment in multi-goal MARL. 


--- 
<a name="4"></a> 
:+1: LEARNING NEARLY DECOMPOSABLE VALUE FUNCTIONS VIA COMMUNICATION MINIMIZATION

[link](https://arxiv.org/pdf/1910.05366.pdf)

- agents act on their own most of the time but occasionally send messages to other agents in order for effective coordination.
- hybridizes value function factorization learning and communication learning by introducing two information-theoretic regularizers.
- regularizers are maximizing mu- tual information between decentralized Q functions and communication messages while minimizing the entropy of messages between agents.
- allows to cut off more than 80% communication without sacrificing the performance.
- adopt diagonal covariance for our message embedding, bits in a message are independent. thus make decision bit by bit and send messages with various length.
- test on *sensor*, *Hallway* tasks and StarCraft II micromanagemtn benchmark.


--- 
<a name="5"></a> 
GRAPH CONVOLUTIONAL REINFORCEMENT LEARNING

[link](https://arxiv.org/pdf/1810.09202.pdf)

- graph convolution adapts to the dynamics of the underlying graph of the multi-agent environment, and relation kernels cap- ture the interplay between agents by their relation representations.
- Temporal regularization, which minimizes the KL divergence of relation representations in succes- sive timesteps, boosts the cooperation, helping the agent to form a long-term and consistent policy in the highly dynamic environment with many moving agents.


--- 
<a name="6"></a> 
MULTI-AGENT INTERACTIONS MODELING WITH CORRELATED POLICIES

[link](https://arxiv.org/pdf/2001.03415.pdf)

- multi-agent imitation learning frame- work with explicit modeling of correlated policies by approximating opponents’ policies, which can recover agents’ policies that can regenerate similar interactions. 
- Prior studies for multi-agent imitation learning typically limit the complexity in demonstrated interactions by assuming isolated reward structures and independence in per-agent policies that overlook the high correlations among agents.
- prove that the proposed framework treats the demonstrator interactions as one of ε-Nash Equilibrium (ε-NE) solutions under the recovered reward.
- comparisons for both the reward gap between learned agents and demonstrators, along with the distribution divergence between demonstrations and regen- erated interacted trajectories from learned policies.


--- 
<a name="7"></a> 
JELLY BEAN WORLD: A TESTBED FOR NEVER-ENDING LEARNING

[link](https://arxiv.org/pdf/2002.06306.pdf)

- two-dimensional grid worlds which are filled with items and in which agents can navigate. 
- produce non-stationary environments and facilitating experimentation with multi-task, multi-agent, multi-modal, and curriculum learning settings.
- let $\pi_{\star}$ be the (computable) learning algorithm that maximizes expected reward in an environment $E$. Then we define the complexity of $E$ to be the length of the shortest program (Turing machine) that implements $\pi_{\star}$:
- The JBW also explicitly restricts learning to a single never-ending episode. 


--- 
<a name="8"></a> 
POSTERIOR SAMPLING FOR MULTI-AGENT REINFORCEMENT LEARNING: SOLVING EXTENSIVE GAMES WITH IMPERFECT INFORMATION

[link](https://openreview.net/pdf?id=Syg-ET4FPS)

- PSRL maintains a posterior distribution of the environment and then makes planning on an environment sampled from the posterior distribution.
- extend PSRL to two-player zero-sum extensive-games with imperfect information (TEGI).
- combine PSRL with counterfactual regret minimization (CFR), which is a leading algorithm for TEGI with a known environment.
- provably converges to the Nash Equilibrium at a rate of $O(\sqrt{log T / T})$


--- 
<a name="9"></a> 
LEARNING EXPENSIVE COORDINATION: AN EVENT-BASED DEEP RL APPROACH

[link](https://openreview.net/pdf?id=ryeG924twB)

- consider the single-leader multi-follower Stackelberg Markov Games (SMG).
- model the leader’s decision-making process as a semi-Markov Decision Process and propose a novel multi-agent event-based policy gradient to learn the leader’s long-term policy. 
- exploit the leader-follower consistency scheme to design a follower-aware module and a follower-specific attention module to predict the followers’ behaviors and make accurate response to their behaviors.
- propose an action abstraction-based policy gradient algorithm to reduce the followers’ decision space and thus accelerate the training process of followers. 


--- 
<a name="10"></a> 
:+1: Reinforcement Learning with Competitive Ensembles of Information-Constrained Primitives

[link](https://arxiv.org/pdf/1906.10667.pdf)

- train policy primitives, each primitive can decide for themselves whether they wish to act in the current state.
- each primitive chooses how much information it needs about the current state to make a decision and the primitive that requests the most information about the current state acts in the world.
- primitives are regularized to use as little information as possible.
- primitives focus on distinct regions of the state space.
- individual primitive mechanisms can be recombined in a “plug-and-play” fashion, and can be transferred seamlessly to new environments.
- each primitive is trained with a information bottleneck loss (use KL divergence and variation approx), a on-policy rewards (re-distributed according to level of participation) and a regularization loss.
$$
J_k(\theta) = E_{\pi_{\theta}}[r_k] - \beta_{inid}L_k - \beta_{reg}L_{reg}   
$$
$$
L_k = D_{KL}(p_{enc}(Z_k|S) || N(0,1))
$$
$$
\alpha_k = exp(L_k) / \sum_{j}exp(L_j)
$$
$$
L_{reg} = \sum_{k}\alpha_k L_k = -H(\alpha) + LSE(L_1,...,L_k)
$$
$$
\pi_{\theta}^k(A|S) = \int_{z}p_{enc}(z_k|S)p_{dec}(A|z_k)dz_k
$$


--- 
<a name="11"></a> 
:+1: INTRINSIC MOTIVATION FOR ENCOURAGING SYNERGISTIC BEHAVIOR

[link](https://arxiv.org/pdf/2002.05189.pdf)

- key idea is that a good guiding principle for intrinsic motivation in synergistic tasks is to take actions which affect the world in ways that would not be achieved if the agents were acting on their own.
- incentivize agents to take (joint) actions whose effects cannot be predicted via a composition of the pre- dicted effect for each individual agent.
- one based on the true states encountered, and another based on a dynamics model trained concurrently with the policy ( benefit of being analytically differentiable with respect to the action taken.).


--- 
<a name="12"></a> 
Learning Structured Communication for Multi-agent Reinforcement Learning

[link](https://arxiv.org/pdf/2002.04235.pdf)

- use a more flexible and efficient communication topology.
- adaptive agent grouping to form different hierarchical formations over episodes, which is generated by an auxiliary task combined with a hierarchical routing protocol.
- Given each formed topology, a hierarchical graph neural network is learned.
- identify several common communication topplogies: full-connected (DIAL, TARMAC, SchedNet), star (CommNet, IC3), tree (ATOC), neighboring (DGN), propose hierarchical (HAMA, this)
- common issue in GCN, shallow GCN without pooling layers can hardly explore rich global information as discussed in H-GCN.
- weight generator and the Cluster-Based Routing Protocol (CBRP), leading to a distributed election of high-level agents.


--- 
<a name="13"></a> 
MULTIPOLAR: MULTI-SOURCE POLICY AGGREGATION FOR TRANSFER REINFORCEMENT LEARNING BETWEEN DIVERSE ENVIRONMENTAL DYNAMICS

[link](https://arxiv.org/pdf/1909.13111.pdf)

- only a set of source policies collected under unknown diverse dynamics is available for learning a target task efficiently.
- learn to aggregate the actions provided by the source policies adaptively to maximize the target task performance. 
- learn an auxiliary network that predicts residuals around the aggregated actions, which ensures the target policy’s expres- siveness even when some of the source policies perform poorly.
- potential improvement on testing each source on the target task and taking them into account in the training phase only when they are found useful.
- assumes source and target environment instances to be different only in their state transition distribution. An interesting direction for future work is to involve other types of environmental differences, such as dissimilar rewards and state/action spaces.


<!-- ***************************************************** -->
---
#### References
