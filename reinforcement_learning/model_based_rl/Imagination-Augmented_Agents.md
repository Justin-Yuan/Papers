# Imagination-Augmented Agents for Deep Reinforcement Learning
[link](https://arxiv.org/pdf/1707.06203.pdf)

- imagination core = environment model + rollout policy 

- rollout encoder to process the imagined rollouts and learns to interpret them separately --> rollout embedding

- aggregator converts different rollout embedding s to a single imagination code 

- policy takes imagination code, observation and output action and estimated value ( model-free path) 

- rollout policy is learnt by distillation from the output policy 

- further potential improvement by training rollout policiesthat "learn to query" imperfect models in a task-relevant way.
