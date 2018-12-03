### Visual Semantic Navigation Using Scene Priors 
[link](https://arxiv.org/pdf/1810.06543.pdf)

#### Intro 

- simulated agent navigation in household environment, using visual input, semantic target, GNN as scene prior/knowledge graph and RL framework
- AI2-THOR framework, phototrealistic & actionable 

#### Modeling 

- Visual Input: ImageNet pretrained ResNet-50 -> 512d feature 
- Semantic Target: FastText -> 512d embedding  
- Knowledge graph: GCN, predefined with **Visual Genome Dataset**
    - initial nodes as concat of visual feature and semantic embedding
    - 3 layes of propagation 
- Action space: with/without **Stop** action 

#### Evaluation 

- baselines: Random, A3C 
- proposed: A3C + Scene Priors with GCN 
- metric: Success Rate, Success weighted byPath LEngth (SPL)
- test on: Seen/Unseen scenes, Known/Novel objects 

#### Future Work 

- incorporate long-term memory 
- incorporate higher-order relationships between objects & sceens 


<!--- *********************************************************************************************************************************************** --->
--- 

###  Building Generalizable Agents With A Realistic And Rich 3D Environment 
[link](https://arxiv.org/pdf/1801.02209.pdf)

#### Intro

- sourced from **SUNCG Dataset** 
- Facebook House3D Environment, targeted navigation 
- include a table to compare different simulation environments 
- high throughput rendering 
- concept-driven navigation 
- multi-target learning problem 

#### Modeling 

- visual input: raw pixels, semantic segmentation mask, depth information 
- rewards: collision penalty with obstacles, task success reward 
- informative reward shaping: approximate shortest distance from target room to agent location 
- gated-CNN + DDPG (continuous action) & gated-LSTM + A3C (discrete action)
- gated fusion module to use target semantic embedding (interpreted as an attention mechanism)
- augmentation
    - pixel-level, domain randomization 
    - task-level, auxiliary targets 
    - scene-level, more diverse houses 

#### Evaluation

- metric: agent in the target room & consecutively see the designated object 

#### Future Work 

- generalization to unseen environments 


<!--- *********************************************************************************************************************************************** --->
--- 

### Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning 
[link](https://arxiv.org/pdf/1609.05143.pdf)

#### Intro 

- AI2-THOR -> Unity 3D + Tensorflow direct communication  
- policy conditions on current state and target, no need to re-train 

#### Modeling 

- observation and target/goal are both images 
- minimize trajectory length to navigation targets, goal reaching reward + time penalty 
- Siamese network, map observation and target images to shared embedding space then joint them 
- scene-specific layers for different scenes
- A3C, training with parallel threads run different navigation target 

#### Evaluation 

- metric: trajectory length, success rate  
- t-SNE visualization on observation embeddings, preserves spatial correlation! 

#### Future Work 

- agent to learn physical interaction & object manipulation 


<!--- *********************************************************************************************************************************************** --->
--- 

### Embodies Question Answering 
[link](https://arxiv.org/pdf/1711.11543.pdf)

#### Intro 

- agent to learn active perception, common sense reasoning, language grounding, credit assignment 
- represent each question as a **functional program**, able to be programmatically generated and executed (like CLEVR)
- EQA generation engine, v1 with 4 question types: location, color, color_room, preposition 

#### Modeling 

- 4 modules: vision, language, navigation, answering 
- uses Adaptive Computation Time navigator, planner + controller
- initialize agent via imitation learning 
- answering module attends to past observed frames, output logits to fixed set of possible answers 
- rewards: question answering accuracy + reward shaping as distance to target 
- REINFORCE with baseline -> should have something to encourage exploration 

#### Evaluation 

- mean rank of tround truth in sorted prediction list 
- navigation accuracy by distance to target at termination 
- baselines to justify the proposed effectiveness of multi-modal input 
- oracles: human nav, groud truth shortest path + VQA 

#### Future Work 

- explicit memory to LSTM 
- encourage exploration 
- ray tracing with frame rendering 


<!--- *********************************************************************************************************************************************** --->
--- 

### Learning a Semantic Prior for Guided Navigation 
[link](https://eccv18-vlease.github.io/static/papers/learning-a-semantic-prior.pdf), also **Learning and Planning with a Semantic Model**

#### **Need more careful read**

#### Intro 

- assume some low-dimensional discrete semantic signals from perceptino is available 
- learn a Bayesian model over the semantic structures to provide exploration guidances for subpolicies 
    - structured prior over semantics of the environment 
    - efficient inference and planning 
    - interpretable 
- structural similarities between environments that can be captured as a probabilistic graphical model over the semantic information 

#### Modeling 

- contextual Markov Decision Process 
- model as a probabilisticgraph ovear targets

#### Evaluation 

- RoomNav task 

#### Future Work 


<!--- *********************************************************************************************************************************************** --->
--- 

### On Evaluation of Embodied Navigation Agents
[link](https://arxiv.org/pdf/1807.06757.pdf)

#### Intro 

- propose common task definitions and evaluaoin protocols 
- Goal specification: PointGoal, ObjectGoal, AreaGoal 
- Generalization/Exploration: No prior exploration, Pre-recorded prior exploration, Time-limited exploration by the agent

#### Recommendations 

- The agent must be equipped with a special action that indicates that it has concluded the navigation episode and is ready to be evaluated. 
- To measure proximity, use the geodesic distance, i.e., the shortest-path distance in the environment 
- Adopt Success weighted by Path Length (SPL) as primary measure of navigation performance 
- structure of the internal representation that the agent constructs and maintains


<!--- *********************************************************************************************************************************************** --->
--- 

### Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments
[link](https://arxiv.org/pdf/1711.07280.pdf)

#### Intro  

- visually grounded sequence-to-sequence translation problems
- Matterport3D Simulator, based on real imagery -> Room-to-Room (R2R) dataset 


<!--- *********************************************************************************************************************************************** --->
--- 

### How agents see things: On visual representations in an emergent language game
[link](https://arxiv.org/pdf/1808.10696.pdf)

#### Intro 

- referential games of Lazaridou 
- pay attention to visual semantics agents associate to the symbols they use 


<!--- *********************************************************************************************************************************************** --->
--- 

### Virtual-to-Real: Learning to Control in Visual Semantic Segmentation
[link](https://arxiv.org/pdf/1802.00285.pdf)

#### Intro 

- perception modeule and control module, related by using semantic image segmentation as the meta representation 

#### Evaluation 

- obstacle avoidance & target following 


<!--- *********************************************************************************************************************************************** --->
--- 

### Learning to Navigate in Cities without a Map 
[link](https://arxiv.org/pdf/1804.00168.pdf)

#### Intro 

- developing internal representation of space, grounded by recognisable landmarks and robust visual processing, support continuous self-localisation and a representation of the goal 
- propose a dual pathway architecture that allows locale-specific features to be encapsulated, while still enabling transfer to multiple cities 
- use Google StreetView public API, with high-resolution imagery and graph connectivity 

#### Modeling 

- inputs: image and goal description, goal represented as its proximity to a set of fixed landmarks  
- architectures: GoalNav, CityNav, MultiCityNav
- auxiliary heading prediction to counter sparse rewards 
- curriculum learning 


<!--- *********************************************************************************************************************************************** --->
--- 

### TOUCHDOWN: Natural Language Navigation and Spatial Reasoning in Visual Street Environments
[link](https://arxiv.org/pdf/1811.12354.pdf)



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