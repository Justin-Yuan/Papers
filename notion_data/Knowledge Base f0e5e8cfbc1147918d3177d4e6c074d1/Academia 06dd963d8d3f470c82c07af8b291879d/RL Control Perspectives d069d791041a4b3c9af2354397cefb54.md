# RL: Control Perspectives

---

## Ten Key Ideas for Reinforcement Learning and Optimal Control (in progress)

link: [http://web.mit.edu/dimitrib/www/Slides_Extended_RL_Lecture.pdf](http://web.mit.edu/dimitrib/www/Slides_Extended_RL_Lecture.pdf)

### 1. principle of optimality

### 2. approximation in value space

### 3. approximation in policy space

### 4. model-free methods and simulation

### 5. policy improvement, rollout, self-learning

### 6. approximate policy improvement, adaptive simulation, Q-learning

### 7. approximation architectures, features, and deep neural nets

### 8. incremental and stochastic gradient optimization

### 9. direct policy optimization: a more general approach

### 10. gradient and random search methods for direct policy optimization

NOTE: need to read the book to know more details !

[https://web.mit.edu/dimitrib/www/RLbook.html](https://web.mit.edu/dimitrib/www/RLbook.html)

---

## An Outsider's Tour of Reinforcement Learning

link: [http://www.argmin.net/2018/06/25/outsider-rl/](http://www.argmin.net/2018/06/25/outsider-rl/)

### Reinforcement Learning As Predictive Analytics

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled.png)

### the linearization principle

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%201.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%201.png)

### Iterative Learning Control

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%202.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%202.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%203.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%203.png)

### policy gradient

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%204.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%204.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%205.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%205.png)

### nominal control

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%206.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%206.png)

### system identification

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%207.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%207.png)

### PID controller

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%208.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%208.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%209.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%209.png)

### PID connection with gradient descent

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2010.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2010.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2011.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2011.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2012.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2012.png)

### the Lur'e problem

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2013.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2013.png)

more references

- Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints ([https://arxiv.org/pdf/1408.3595.pdf](https://arxiv.org/pdf/1408.3595.pdf))
- A General Analysis of the Convergence of ADMM ([https://arxiv.org/pdf/1502.02009.pdf](https://arxiv.org/pdf/1502.02009.pdf))
- A Unified Analysis of Stochastic Optimization Methods Using Jump System Theory and Quadratic Constraints ([https://arxiv.org/pdf/1706.08141.pdf](https://arxiv.org/pdf/1706.08141.pdf))
- Control Interpretations for First-Order Optimization Methods ([https://arxiv.org/pdf/1703.01670.pdf](https://arxiv.org/pdf/1703.01670.pdf))

### PID control for iterative learning control

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2014.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2014.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2015.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2015.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2016.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2016.png)

### approximate dynamic progromming

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2017.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2017.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2018.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2018.png)

NOTE: receding horizon control (RHC) is also known as model predictive control 

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2019.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2019.png)

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2020.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2020.png)

### learning in RHC / MPC

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2021.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2021.png)

### Coarse-ID Control

![RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2022.png](RL%20Control%20Perspectives%20d069d791041a4b3c9af2354397cefb54/Untitled%2022.png)

reference: A Tour of Reinforcement Learning: The View from Continuous Control

([https://arxiv.org/abs/1806.09460](https://arxiv.org/abs/1806.09460))

---

---

## Papers

### A Tour of Reinforcement Learning: The View from Continuous Control

link: [https://arxiv.org/pdf/1806.09460.pdf](https://arxiv.org/pdf/1806.09460.pdf)