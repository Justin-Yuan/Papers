# DL: Meta-learning

---

## Meta-Learning Is All You Need

link: [https://medium.com/cracking-the-data-science-interview/meta-learning-is-all-you-need-3bd0bafdf289](https://medium.com/cracking-the-data-science-interview/meta-learning-is-all-you-need-3bd0bafdf289) 

### meta-learning intro

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled.png)

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%201.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%201.png)

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%202.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%202.png)

### Black-Box Meta-Learning

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%203.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%203.png)

### Optimization-Based Meta-Learning

e.g. Model-Agnostic Meta-Learning (MAML) [https://arxiv.org/abs/1703.03400](https://arxiv.org/abs/1703.03400) 

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%204.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%204.png)

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%205.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%205.png)

### Non-Parametric Meta-Learning

e.g. prototypical networks ([https://arxiv.org/abs/1703.05175](https://arxiv.org/abs/1703.05175))

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%206.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%206.png)

---

## Bayesian Meta-Learning Is All You Need

link: [https://medium.com/cracking-the-data-science-interview/bayesian-meta-learning-is-all-you-need-1bcff6b889fc](https://medium.com/cracking-the-data-science-interview/bayesian-meta-learning-is-all-you-need-1bcff6b889fc) 

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%207.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%207.png)

### Bayesian Black-Box Meta-Learners

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%208.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%208.png)

- condition inference network on training dataset

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%209.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%209.png)

- condition task-specific parameters on meta-parameters $\theta$

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2010.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2010.png)

- optimize across tasks

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2011.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2011.png)

### Bayesian Optimization-Based Meta-Learners

- recasting gradient-based meta-learning as hierarchical Bayes
- amortized Bayesian MAML
- an important algorithm for training a Bayesian Net, Stein Variational Gradient Descent (SVGD), is theoretically compatible with gradient-based meta-learning
- Probabilistic Model-Agnostic Meta-Learning (Probabilistic MAML)

![DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2012.png](DL%20Meta-learning%20c6c66a33fd9149c392c6cd07d351e262/Untitled%2012.png)

---

---

## Papers

---

## Tools