# Math: Duality

---

## Convex Optimization Lecture 11 — CMU

link: [http://www.stat.cmu.edu/~ryantibs/convexopt-F15/scribes/11-dual-gen-scribed.pdf](http://www.stat.cmu.edu/~ryantibs/convexopt-F15/scribes/11-dual-gen-scribed.pdf)

### Lagrangian

- key idea: $f^* = inf_x \ sup_{u \ge 0,v}\  L(x,u,v)$

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled.png)

### Lagrange dual function

- key idea: $g(u,v) = inf_x \ L(x,u,v)$
- NOTE: the infimum here does not require x to be taken in the feasible set

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%201.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%201.png)

### Lagrange dual problem

- key idea: $g^* = sup_{u\ge0,v}\  inf_x\ L(x,u,v)$

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%202.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%202.png)

### Weak duality

- key idea: $f^* \ge g^*$

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%203.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%203.png)

- max-min inequality

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%204.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%204.png)

- minimax theorem

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%205.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%205.png)

### Strong duality

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%206.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%206.png)

---

## Duality — Stanford

link: [https://web.stanford.edu/class/ee364a/lectures/duality.pdf](https://web.stanford.edu/class/ee364a/lectures/duality.pdf)

### formulation

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%207.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%207.png)

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%208.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%208.png)

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%209.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%209.png)

### examples

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2010.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2010.png)

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2011.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2011.png)

### Complementary slackness

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2012.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2012.png)

### KKT conditions

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2013.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2013.png)

---

## Fenchel's duality theorem — Wiki

link: [https://en.wikipedia.org/wiki/Fenchel's_duality_theorem](https://en.wikipedia.org/wiki/Fenchel%27s_duality_theorem)

### formulation

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2014.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2014.png)

### dual space

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2015.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2015.png)

### convex conjugate

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2016.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2016.png)

### illustration

![Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2017.png](Math%20Duality%20f763041d40f44bcf82a3dd0087e71c9b/Untitled%2017.png)

---

## References

- Reinforcement Learning via Fenchel-Rockafellar Duality

[](https://arxiv.org/pdf/2001.01866.pdf)

- convex optimization: fall 2015

[Convex Optimization](http://www.stat.cmu.edu/~ryantibs/convexopt-F15/)

- Duality Theory of Constrained Optimization

[](https://ocw.mit.edu/courses/sloan-school-of-management/15-084j-nonlinear-programming-spring-2004/lecture-notes/lec18_duality_thy.pdf)

- Duality in Optimization

[](https://www.imo.universite-paris-saclay.fr/IMG/pdf/paris1and2_cle085e32.pdf)