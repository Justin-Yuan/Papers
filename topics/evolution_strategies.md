# Evolution Strategies (ES)

<!-- ***************************************************** -->

# Notes

Black-box optimization 

Problem formulation 
- given f(x), can evaluate f(x) given x, result deterministic 
- $p_{\theta}(x)$ probability distribution over x as as good solution to f(x) optimization 
- goal to find optimal configuration  of $\theta$

Algo
1. Generate a population of samples $D={(x_i,f(x_i))}$ where $x_i \sim p_{\theta}(x)$.
2. Evaluate the “fitness” of samples in D.
3. Select the best subset of individuals and use them to update θ, generally based on fitness or rank.

Simple Gaussian Evolution Strategies
- not able to rapidly adjust the exploration space when needed

Covariance Matrix Adaptation Evolution Strategies (CMA-ES)
- track pairwise dependencies between the samples in the distribution with a covariance matrix 

Natural Evolution Strategies
- use natural gradient to update distribution parameters 

Novelty-Search ES 
- encourages exploration by updating the parameter in the direction to maximize the novelty score 

CEM-RL
<https://arxiv.org/pdf/1810.01222.pdf>

Hyperparameter Tuning: PBT
<https://arxiv.org/pdf/1711.09846.pdf>


Network Topology Optimization: Weight Agnostic Neural Networks (WANN)
<https://arxiv.org/pdf/1906.04358.pdf>

