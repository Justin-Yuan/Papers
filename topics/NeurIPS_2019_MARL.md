## NeurIPS 2019 MARL

[link](https://nips.cc/Conferences/2019/Schedule?showParentSession=15613)

<!-- ***************************************************** -->
Papers on Multi-agent Reinforcement Learning, covering topics on 
- emergent communication
- multi-agent cooperation
- game theory to multi-agent learning
- multi-agent dynamics
- multi-agent exploration

<!-- ***************************************************** -->
---
#### List of Works
- [Biases for Emergent Communication in Multi-agent Reinforcement Learning](#1)
- [Ease-of-Teaching and Language Structure from Emergent Communication](#2)
- [Finding Friend and Foe in Multi-Agent Games](#3)
- [Learning Fairness in Multi-Agent Systems](#4)
- [Multi-Agent Common Knowledge Reinforcement Learning](#5)
- [Multi-Agent Common Knowledge Reinforcement Learning](#6)
- [MAVEN: Multi-Agent Variational Exploration](#7)


<!-- ***************************************************** -->
---
#### Work Summaries

<a name="1"></a> 
Biases for Emergent Communication in Multi-agent Reinforcement Learning

[link](https://arxiv.org/pdf/1912.05676.pdf)

- MARL with emergent communication is hard due in part to a difficult joint exploration problem, this work introduces inductive bias for positive signalling and positive listening (as auxiliary shaped loss) to address it. 
- test on task speaker-listener task on summing MNIST digits and a grid world environment based on search of a treasure (1 agent cannot reach goal but can observe goal, 1 agent smaller view but can reach goals). 
- assum agents learn independently, making communication channel non-differentiable.
- bias for positive signalling, maxmimze mutual information between speaker message and speaker trajectory, using estimates ffrom a batch of rollouts and a target entropy 
- bias for positive listening, maximize causal influence of communication (CIC), extended for multiple time steps. fit another listener's policy unconditioned on the messages received.


--- 
<a name="2"></a> 
Ease-of-Teaching and Language Structure from Emergent Communication

[link](https://arxiv.org/pdf/1906.02403.pdf)

- propose ease-of-teaching as pressure, introduce new agents periodicaally to replace old ones
- show that compositional language is easier to teach than a less structured one. 
- speaker is periodically forced to interact with new listeners during training. 
- more abrupt sequentiaal changes appear to be key in increasing the entropy of the speaker's policy, which seems to be leading to increasingly structured, easier-to-teach languages. 
- use LSTM to sequential output token until a fixed message length is reached.
- ues topographic similarity to quantify message structure. 


--- 
<a name="3"></a> 
Finding Friend and Foe in Multi-Agent Games

[link](https://arxiv.org/pdf/1906.02330.pdf)

- tackle the problem of "who to cooperate with".
- test on *The Resistance: Avalon*, the most popular hidden role game.
- integrates deductive reasoning into vector-form CFR to reason about joint beliefs and deduce partially observable actions.
- augment deep value networks with constraints that yield interpretable representations of win probabilities.
- extend from **DeepStack**, which uses heuristic search techniques that combine efficient depth-limited lookahead planning with a value function learned through self-play.


--- 
<a name="4"></a> 
Learning Fairness in Multi-Agent Systems

[link](https://arxiv.org/pdf/1910.14472.pdf)

-  learning efficiency and fairness simultaneously is a complex, multi-objective, joint-policy optimization.
- propose FEN, a novel hierarchical reinforcement learning model.
- decompose fairness for each agent and proporse fair-efficient reward. 
- design a hierarchy consisting of a controller and several sub-policies, where the controller maximizes the fair-efficient reward by switching among the sub-policies that provides diverse behaviors to interact with the environment.
- One of the sub-policies is designated to maximize the environmental reward, and other sub-policies are guided by information-theoretic reward to explore diverse possible behaviors for fairness. 
- prove that agents achieve Pareto efficiency and fairness is guaranteed in infinite-horizon sequential decision-making.  
- test in 3 scenarios: job scheduling, the Mathew effect, and manufacturing plant. 


--- 
<a name="5"></a> 
Modelling the Dynamics of Multiagent Q-Learning in Repeated Symmetric Games: a Mean Field Theoretic Approach

[link](http://papers.nips.cc/paper/9380-modelling-the-dynamics-of-multiagent-q-learning-in-repeated-symmetric-games-a-mean-field-theoretic-approach.pdf)

- most current multi-agent learning dynamics research uses evolutionary game theoretic approaches.
- study an n-agent setting with n tends to infinity, such that agents learn their policies concurrently over re peated symmetric bimatrix games with some other agents.
- Using the mean field theory, we approximate the effects of other agents on a single agent by an averaged effect. 
- A Fokker-Planck equation that describes the evolution of the probability distribution of Q-values in the agent population is derived. 
- major difficulty is to cope with non-stationarity.
- assume agents use Q-learning with Boltzmann exploration.
- under the n-agent setting considered, the Q-learning agents are usually myopic.
- **interesting idea, need further detailed read**


--- 
<a name="6"></a> 
Multi-Agent Common Knowledge Reinforcement Learning

[link](https://arxiv.org/pdf/1810.11702.pdf)

- show that common knowledge between agents allows for complex decentralised coordination. 
- propose a stochastic actor-critic algorithm that learns a hierarchical policy tree.
- test on a stochastic matrix game and StarCraft II unit micromanagement.
- policy involves stage to dynamically select the right level of coordination. 


--- 
<a name="7"></a> 
MAVEN: Multi-Agent Variational Exploration

[link](https://arxiv.org/pdf/1910.07483.pdf)

- show that the representational constraints on the joint action-values introduced by QMIX and similar methods lead to provably poor exploration and suboptimality.
-  hybridises value and policy-based methods by introducing a latent space for hierarchical control.
- achieve committed, temporally extended exploration.
- fixing the latent variable, each joint action-value function can be thought of as a mode of joint exploratory behaviour that persists over an entire episode.
- uses mutual information maximisation between the trajectories and latent variables to learn a diverse set of such behaviours. 
- consider nonmonotonic Q value functions that QMIX cannot handle.
- For a fixed time budget T, increasing QMIX’s exploration rate lowers its probability of learning the optimal action due to its representational limitations.
- test on m-step matrix game and StarCraft II environment.


<!-- ***************************************************** -->
---
#### References
