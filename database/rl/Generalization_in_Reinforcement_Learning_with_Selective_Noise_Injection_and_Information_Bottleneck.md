## Generalization in Reinforcement Learning with Selective Noise Injection and Information Bottleneck

[link](https://arxiv.org/pdf/1910.12911.pdf)
[code](https://github.com/microsoft/IBAC-SNI/)

<!-- ***************************************************** -->
Selective Noise Injection (SNI), which maintains the regularizing effect the injected noise has, while mitigating the adverse effects it has on the gradient quality. 

Information Bottleneck (IB) is a particularly well suited regularization technique for RL. to bias our agent towards more general features even early on in training, we adapt the Information Bottleneck (IB) principle to an actor-critic agent.

<!-- ***************************************************** -->
---
#### Key Points

- Variational Information Bottleneck (VIB). Given a data distribution $p(X, Y)$, the learned model $p_{\theta}(y|x)$ is regularized by inserting a stochastic latent variable Z and minimizing the mutual information between the input X and Z, $I(X,Z)$, while maximizing the predictive power of the latent variable, i.e. $I(Z,Y)$.
$$
L_{VIB} = E_{p(x,y), p_{\theta}(z|x)}[-log q_{\theta}(y|z) + \beta D_{KL}[p_{\theta}(z|x) || q(z)]]
$$
- naive injection of noise can degrade performance in the following ways 
1. During rollouts using the rollout policy πθr, it can lead to undesirable actions, potentially ending episodes prematurely, and thereby deteriorating the quality of the observed data. (:point_right: rollout policy $\pi_{\theta}^r$) 
2. It leads to a higher variance of the off-policy correction term $\pi_{\theta}/\pi_{\theta}^r$ because the  injected noise can be different for $\pi_{\theta}$ and $\pi_{\theta}^r$, increasing gradient variance. (:point_right: off-policy corretion term $\pi_{\theta}/\pi_{\theta}^r$)
3. It increases variance in the gradient updates of both the policy and the critic through variance in the computation of $V_{\theta}$. (:point_right: critic $V_{\theta}$)


<!-- ***************************************************** -->
---
#### Results

- test on Multiroom and Coinrun. 


<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References

[1] DEEP VARIATIONAL INFORMATION BOTTLENECK [link](https://arxiv.org/pdf/1612.00410.pdf)

