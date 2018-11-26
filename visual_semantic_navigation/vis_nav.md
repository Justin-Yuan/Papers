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

- agent to learn active perception, common sense reasoning, language grounding, 

#### Modeling 


#### Evaluation 


#### Future Work 