# Model-Based Reinforcement Learning via Meta-Policy Optimization
[link](https://arxiv.org/pdf/1809.05214.pdf)

## Intro 

- Using an ensemble of learned dynamic models, MB-MPO meta-learns a policy that can quickly adapt to any model in the ensemble with one policy gradient step

- **model-bias**: policy optimization overfits on the deficiencies of the learnt dynamics model 

## Related work 

- model-based rl
    - learn a distribution of models 
    - learn adaptive models 
    - model predictive control (**MPC**) 
        - compensates for model imperfections by re-planning at each step, but it suffers from limited credit assignment and high computational cost

- model-based + model-free rl 
    - differentiable trajectory optimization methods 
        - propagate the gradients of the policy or value function through the learned dynamics model 
    - model-assisted model free approaches 
        - use dynamics model to imagine policy roll-outs 

- meta-learning 



## Results 

 - correlation between model unvertainty and policy plasticity 
    - hypothesize that the meta-optimization steers the policy towards higher plasticity in regions with high dynamics model uncertainty while embedding consistent model predictions into the pre-update policy 


## Future work 

- use  Bayesian neural networks instead of ensembles 

