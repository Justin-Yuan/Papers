# ML: High-dimensional Statistics

---

## Mathematical Tricks Commonly Used in Machine Learning and Statistics

link: [https://danieltakeshi.github.io/2017/05/06/mathematical-tricks-commonly-used-in-machine-learning-and-statistics](https://danieltakeshi.github.io/2017/05/06/mathematical-tricks-commonly-used-in-machine-learning-and-statistics) 

### list of tricks

- Cauchy-Schwarz
- Integrating Probabilities into Expectations
- Introducing an Independent Copy
- Jensen’s Inequality
- Law of Iterated Expectation $E[E[X|Y]] = E[X]$
- Lipschitz Functions
- Markov’s Inequality
- Norm Properties
- Series Expansions (e.g. Taylor’s)
- Stirling’s Approximation
- Symmetrization
- Take a Derivative
- Union Bound
- Variational Representations

---

### Maximum of (Not Necessarily Independent!) sub-Gaussians

- sub-Gaussian distribution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%201.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%201.png)

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%202.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%202.png)

- The Union Bound / Boole's inequality

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%203.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%203.png)

- sub-Gaussian bound

$$X \sim N(\mu,\sigma^2)\  \rightarrow\  E[exp(sX)] = exp(s\mu + \frac{\sigma^2 s^2}{2})$$

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%204.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%204.png)

- extension 1

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%205.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%205.png)

- Markov's inequality

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%206.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%206.png)

- extension 2

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%207.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%207.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%208.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%208.png)

---

### Bounded Random Variables are Sub-Gaussian

- Rademacher distribution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%209.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%209.png)

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2010.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2010.png)

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2011.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2011.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2012.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2012.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2013.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2013.png)

---

### Concentration Around Median and Means

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2014.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2014.png)

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2015.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2015.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2016.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2016.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2017.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2017.png)

---

### Upper Bounds for ℓ0 “Balls”

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2018.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2018.png)

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2019.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2019.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2020.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2020.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2021.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2021.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2022.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2022.png)

---

### Gaussian Complexity of Ellipsoids

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2023.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2023.png)

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2024.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2024.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2025.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2025.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2026.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2026.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2027.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2027.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2028.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2028.png)

---

### Pairwise Incoherence

- problem

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2029.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2029.png)

- pairwise incoherence

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2030.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2030.png)

- solution

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2031.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2031.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2032.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2032.png)

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2033.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2033.png)

- notes

![ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2034.png](ML%20High-dimensional%20Statistics%2092bd48f4becc487b99c3ba5f494976e0/Untitled%2034.png)

---

## 

---

## References