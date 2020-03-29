## INFOBOT: TRANSFER AND EXPLORATION VIA THE INFORMATION BOTTLENECK

link: https://openreview.net/pdf?id=rJg8yhAqKm

### Summary 

- inspired by information bottleneck approach, classifiers are trained
to achieve high accuracy while simultaneously encoding as little information about the input as possible
- show that minimizing goal information promotes generalization in an RL setting as well, ***$I(A;G|S)$***
-  refer to states where diversions from default behaviour occur as decision states
- use KL between goal-contioned policy and default policy (policy with goal marginalized out) as exploration bonus 
- return is ***$J(\theta) = J[r] - \beta I(A;G|S)$***
- estimate the marginalization over $Z$ using a single sample throughout experiment 
- to discourage agent from pursuing exploration bonus only, decay bonus with continued visits by weighting with a count-based exploration bonus 
$$
r_t = r_e(t) + \frac{\beta}{\sqrt{c(s_t)}}D_{KL}[p_{enc}(Z|s_t, g_t) | q(Z|s_t)]
$$

### Implementation 

- use mini-grid world environment https://github.com/maximecb/gym-minigrid/?fbclid=IwAR3SJrxby9JRHTouablg7NkJW6E7VN2y1n_cBbxnP0104Q28rDbnHHRFYzQ 
- use partially observed goal based MiniPacMan environment

### Comments 

- connection with meta-learning 
- focus on exploration methods, compared with count-based bonus, VIME and curiosity 
- connection between action-goal information and the structure of decision-making
- connection with "bottleneck states" used to define subgoals in shierarchical reinforcement learning
- connection with variational information bottleneck if maximize $I(A*; A|S)$ in imitation learning 


### Prerequisites

- data processing inequality (DPI) 
- bottleneck states in HRL 
- variational information bottleneck
