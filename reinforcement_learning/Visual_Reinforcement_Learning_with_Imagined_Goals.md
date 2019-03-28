# Visual Reinforcement Learning with Imagined Goals
[link](https://arxiv.org/pdf/1807.04742.pdf)

## Intro 

- combine unsupervised representatino learning and reinforcement leraning of goal-conditioned policies 
- agent performs a self-supervised phase where it imagines goals and attempts to achieve them 
- learn a visual representation that 
	- sample goals for self-supervised practice 
	- provide structured transformation of raw sensory inputs 
	- compute a reward signal for goal reaching (provide meaningful distances than that in the original observation space)
- visual representation -> learned latent variable model, VAE 
- retroactive goal relabeling scheme 

## Modeling 

- embed the state and goals into a latent space Z using an encoder, train a beta-VAE while executing a random policy and collecting state observations 
- use **TD3** as backbone 
- use the **negative Mahalanobis distance** in the latent space 
- could potentially convert a triplet (state, action, next state) transition into infinitely many valid training data by generating a new goal and new reward 
- similarity with **Hindsight experience replay (HER)**, but here half of the goals generated from the prior and half from goals seen along the trajectory 