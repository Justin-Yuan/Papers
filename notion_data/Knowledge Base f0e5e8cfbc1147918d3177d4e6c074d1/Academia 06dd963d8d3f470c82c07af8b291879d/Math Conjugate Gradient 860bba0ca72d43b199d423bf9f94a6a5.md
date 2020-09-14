# Math: Conjugate Gradient

---

## Conjugate gradient method — Wiki

link: [https://en.wikipedia.org/wiki/Conjugate_gradient_method](https://en.wikipedia.org/wiki/Conjugate_gradient_method) 

### summary

- to solve the system of linear equations $Ax = b$ , where matrix $A$ is symmetric, positive-definite and real
- key idea: orthogonality of the residuals and conjugacy of the search directions
- conjugate vectors

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled.png)

- how to solve $Ax = b$

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%201.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%201.png)

- iterative method

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%202.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%202.png)

- Krylov subspace

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%203.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%203.png)

- resulting algorithm

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%204.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%204.png)

- computation of alpha and beta

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%205.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%205.png)

---

## Non-linear conjugate gradient method

link: [https://optimization.mccormick.northwestern.edu/index.php/Conjugate_gradient_methods](https://optimization.mccormick.northwestern.edu/index.php/Conjugate_gradient_methods) 

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%206.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%206.png)

---

## Conjugate Gradient Descent — CMU

link: [http://www.cs.cmu.edu/~pradeepr/convexopt/Lecture_Slides/conjugate_direction_methods.pdf](http://www.cs.cmu.edu/~pradeepr/convexopt/Lecture_Slides/conjugate_direction_methods.pdf)

### motivation

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%207.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%207.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%208.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%208.png)

### conjugacy

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%209.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%209.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2010.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2010.png)

### formulation

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2011.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2011.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2012.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2012.png)

### Expanding Subspace Theorem

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2013.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2013.png)

### conjugate gradient

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2014.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2014.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2015.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2015.png)

### non-quadratic problems

- NOTE: need to evaluate Hessian matrix at each point

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2016.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2016.png)

### line search methods

- Hessian is not used

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2017.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2017.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2018.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2018.png)

### acceleration

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2019.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2019.png)

---

## Conjugate Gradient Method — Stanford

link: [https://web.stanford.edu/class/ee364b/lectures/conj_grad_slides.pdf](https://web.stanford.edu/class/ee364b/lectures/conj_grad_slides.pdf) 

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2020.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2020.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2021.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2021.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2022.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2022.png)

### Krylov subspace

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2023.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2023.png)

### Cayley-Hamilton theorem

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2024.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2024.png)

### CG algorithm

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2025.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2025.png)

### Efficient matrix-vector multiply

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2026.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2026.png)

### Preconditioning

- key idea: apply CG after a linear change of coordinates $x = Ty$

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2027.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2027.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2028.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2028.png)

---

## Conjugate gradient method — UCLA

---

## Conjugate gradient method — UCLA

link: [http://www.seas.ucla.edu/~vandenbe/236C/lectures/cg.pdf](http://www.seas.ucla.edu/~vandenbe/236C/lectures/cg.pdf)

### conjugate gradient method for linear equations

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2029.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2029.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2030.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2030.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2031.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2031.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2032.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2032.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2033.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2033.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2034.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2034.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2035.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2035.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2036.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2036.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2037.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2037.png)

### complexity

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2038.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2038.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2039.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2039.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2040.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2040.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2041.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2041.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2042.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2042.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2043.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2043.png)

### Conjugate gradient method as iterative method

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2044.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2044.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2045.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2045.png)

### applications in nonlinear optimization

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2046.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2046.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2047.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2047.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2048.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2048.png)

![Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2049.png](Math%20Conjugate%20Gradient%20860bba0ca72d43b199d423bf9f94a6a5/Untitled%2049.png)

---

## References

- An Introduction to the Conjugate Gradient Method Without the Agonizing Pain

[](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf)