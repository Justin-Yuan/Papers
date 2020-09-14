# Math: Stochastic Approximation

---

## Stochastic approximation — Wiki

link: [https://en.wikipedia.org/wiki/Stochastic_approximation](https://en.wikipedia.org/wiki/Stochastic_approximation)

### Summary

- Stochastic approximation methods are a family of iterative methods typically used for root-finding problems or for optimization problems

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled.png)

### Robbins–Monro algorithm

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%201.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%201.png)

### Kiefer–Wolfowitz algorithm

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%202.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%202.png)

---

## Stochastic Approximation Theory — Cambridge

link: [http://cbl.eng.cam.ac.uk/pub/Intranet/MLG/ReadingGroup/sgd.pdf](http://cbl.eng.cam.ac.uk/pub/Intranet/MLG/ReadingGroup/sgd.pdf) 

### history

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%203.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%203.png)

### formulation

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%204.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%204.png)

### continuous gradient descent

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%205.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%205.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%206.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%206.png)

### discrete gradient descent

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%207.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%207.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%208.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%208.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%209.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%209.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2010.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2010.png)

NOTEs on the proof for discrete case 

- Lyapunov sequence is not guaranteed to be decreasing

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2011.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2011.png)

- consider variant of Lyapunov sequence

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2012.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2012.png)

- use of the extra condition for proof

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2013.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2013.png)

- show the Lyapunov variant converges

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2014.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2014.png)

- show the Lyapunov converges

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2015.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2015.png)

- show the Lyapunov converges to 0

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2016.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2016.png)

### stochastic gradient descent

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2017.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2017.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2018.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2018.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2019.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2019.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2020.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2020.png)

NOTE: similar proof 

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2021.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2021.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2022.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2022.png)

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2023.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2023.png)

### relaxation

![Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2024.png](Math%20Stochastic%20Approximation%20a2f2c1d9554847779c864e0f3563c861/Untitled%2024.png)

---

## References

- Introduction to Stochastic Approximation Algorithms

[](http://www.professeurs.polymtl.ca/jerome.le-ny/teaching/DP_fall09/notes/lec11_SA.pdf)