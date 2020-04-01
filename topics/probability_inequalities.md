## Probability Inequalities

[link](http://cs229.stanford.edu/extra-notes/hoeffding.pdf)
[link](https://www.stat.cmu.edu/~larry/=stat705/Lecture2.pdf)

<!-- ***************************************************** -->

#### Probability bounds 
given a random variable Z with expectation E[Z], **how likely is Z to be close to its expectation**? Additionally, we would often like sharper—even **exponential—bounds** on the probability that a random variable Z exceeds its expectation by much.

for a random variable Z, its moment generating function is (which may be infinite for some $\lambda$) 
$$
M_z(\lambda) = E[exp(\lambda Z)]
$$
and for $Z_i$ that are independent, 
$$
M_{Z_1+...+Z_n}(\lambda) = \prod_{i=1}^n M_{Z_i}(\lambda)
$$
for a lot of examples, we can have convenient bounds of the form (for some $C$ depending on ddistribution of $Z$)
$$
M_z(\lambda) = E[e^{\lambda Z}] \leq exp(\frac{C^2 \lambda^2}{2})
$$

---
#### Markov's inequality
> Let Z ≥ 0 be a *non-negative* random variable. Then for all t ≥ 0, 
> $$
P(Z \geq t) \leq \frac{E[Z]}{t}
$$

Proof: 
> $P(Z \geq t) = E[1\{Z \geq t\}]$  
> if $Z \geq t$ then $Z/t \geq 1 \geq 1\{Z \geq t\}$  
> if $Z < t$ then $Z/t \geq 0 = 1\{Z \geq t\}$  
> :point_right: $P(Z \geq t) = E[1\{Z \geq t\}] \leq E[\frac{Z}{t}] = \frac{E[Z]}{t}$  
> Q.E.D

---
#### Chebyshev’s inequality
> Let Z be any random variable with Var(Z) < $\infty. Then
> $$
P(Z \geq E[Z] + t \ or \ Z \leq E[Z] - t) \leq \frac{Var(Z)}{t^2}
$$

Proof:
> if $Z \geq E[Z] + t$ then $(Z - E[Z])^2 \geq t^2$  
> use Markov's inequality with random variable $(Z - E[Z])^2$  
> :point_right: $P(Z \geq E[Z] + t \ or \ Z \leq E[Z] - t) = P((Z - E[Z])^2 \geq t^2) \leq \frac{E[(Z - E[Z])^2]}{t^2} = \frac{Var(Z)}{t^2}$
> Q.E.D

Note: can prove averages of random variables with finite variance converge to their mean.

---
#### Chernoff bounds 
> Let Z be any random variable. Then for any t ≥ 0,
> $$
P(Z \geq E[Z]+t) \leq min_{\lambda \geq 0}E[e^{\lambda(Z-E[Z])}]e^{-\lambda  t} =  min_{\lambda \geq 0}M_{Z-E[Z]}(\lambda)e^{-\lambda t}  
> $$
> and similarily,
> $$
P(Z \leq E[Z]-t) \leq min_{\lambda \geq 0}E[e^{\lambda(E[Z]-Z)}]e^{-\lambda  t} =  min_{\lambda \geq 0}M_{E[Z]-Z}(\lambda)e^{-\lambda t}
$$

Proof:
> $Z \geq E[Z]+t \Leftrightarrow e^{\lambda Z} \geq e^{\lambda E[Z] + \lambda t}$ or $e^{\lambda (Z - E[Z])} \geq e^{\lambda t}$  
> :point_right: $P(Z-E[Z] \geq t) = P(e^{\lambda (Z - E[Z])} \geq e^{\lambda t}) \leq E[e^{\lambda (Z-E[Z])}]e^{-\lambda t}$  
> since choice of $\lambda$ does not matter, can simple take minimum of right-hand-side
> Q.E.D

Note: when we calculate a Chernoff bound of a sum of i.i.d. variables, we need only calculate the moment generating function for one of them.

--- 
#### Hoeffding's inequality 
> Let $Z_1, . . . , Z_n$ be independent bounded random variables with $Z_i \in [a,b]$ for all i, where $- \infty < a \leq b < \infty$. Then for all $t \geq 0$ 
> $$
P(\frac{1}{n}\sum_{i=1}^n(Z_i - E[Z_i]) \geq t) \leq exp(-\frac{2nt^2}{(b-a)^2})
> $$  
> and similarily,
> $$
P(\frac{1}{n}\sum_{i=1}^n(Z_i - E[Z_i]) \leq -t) \leq exp(-\frac{2nt^2}{(b-a)^2})
> $$

---
####  Cauchy-Schwartz inequality 
> if $X$ and $Y$ have finite variances, then 
> $$
E[|XY|] \leq \sqrt{E[X^2]E[Y^2]}
> $$

---
#### Jensen's inequality 
> if $g$ is convex, then (if concave, flip sign)
> $$
E[g(X)] \geq g(E[X])
> $$

<!-- ***************************************************** -->
<!-- ---
#### List of works
- [XX](#1)
- [YY](#2) -->

<!-- ***************************************************** -->
<!-- ---
#### Work summaries

<a name="1"></a> 
XX
<link/url>

--- 
<a name="2"></a> 
YY
<link/url> -->


<!-- ***************************************************** -->
---
#### References
