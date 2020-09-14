# RL: Model-based RL

---

## Model-based Reinforcement Learning

link: [https://michaelrzhang.github.io/model-based-rl](https://michaelrzhang.github.io/model-based-rl) 

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled.png)

### Optimal control (OC)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%201.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%201.png)

### Linear-quadratic regulator (LQR)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%202.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%202.png)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%203.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%203.png)

### iterative LQR (iLQR)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%204.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%204.png)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%205.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%205.png)

### Learning dynamics model

- train policy with offline learnt dynamics model

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%206.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%206.png)

- train policy with learned dynamics, adds new trajectories and re-learn dynamics (DAgger)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%207.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%207.png)

- train policy with learnt dynamics but replanning for every step (MPC)

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%208.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%208.png)

- train policy by backprop through time with differentiable dynamics

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%209.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%209.png)

### More on dynamics model

- model parameterization
    - Gaussian process. data efficient but struggles with non-smooth dynamics and slow to train for large dataset
    - Neural network. expressive with large data but struggle with small amount of data
- local model v.s. global model
    - global model, a single function that models the dynamics in all of state space. can be difficult to encapsulate all the information, e.g. dynamics are different in different parts of state space
    - local models. for optimal control, actually don't need a global model, only need local gradients $\frac{df}{dx_t}$ and $\frac{df}{du_t}$. local models are easier to fit, but need to be thrown away whenever the policy updates because they are only accurate for trajectories collected under the old policy.
    - local models but use global model as prior → Bayesian linear regression. reduce sample complexity

### Optimal Control with Local Models

- 3-step loop (reference paper [Learning Contact Rich Manipulation Skills with Guided Policy Search](https://arxiv.org/pdf/1501.05611.pdf))
    1. Run controller (that we get from optimal control) on robot to collect trajectories. 

    ![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2010.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2010.png)

    2. Fit dynamics model to collected trajectories. 

    ![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2011.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2011.png)

    3. Update policy with new dynamics model. 

    ![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2012.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2012.png)

    ![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2013.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2013.png)

- dual gradient descent

![RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2014.png](RL%20Model-based%20RL%20eaa611fa627e46cf8eb8f013eab53db0/Untitled%2014.png)

---

---

## Papers

### Learning Contact-Rich Manipulation Skills with Guided Policy Search

link: [https://arxiv.org/pdf/1501.05611.pdf](https://arxiv.org/pdf/1501.05611.pdf) 

---

### Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning

link: [https://arxiv.org/pdf/1708.02596.pdf](https://arxiv.org/pdf/1708.02596.pdf) 

---

### Learning to Control a Low-Cost Manipulator using
Data-Efficient Reinforcement Learning

link: [https://rse-lab.cs.washington.edu/papers/robot-rl-rss-11.pdf](https://rse-lab.cs.washington.edu/papers/robot-rl-rss-11.pdf)

---

### 

---

## Tools