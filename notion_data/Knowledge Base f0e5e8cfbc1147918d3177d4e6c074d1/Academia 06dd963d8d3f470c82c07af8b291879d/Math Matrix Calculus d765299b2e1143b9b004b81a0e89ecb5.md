# Math: Matrix Calculus

---

## 矩阵求导术（上）— scalar function derivatives

link: [https://zhuanlan.zhihu.com/p/24709748](https://zhuanlan.zhihu.com/p/24709748) 

### notations

- lower-case letter for scalar, e.g. x
- bold lower-case letter for vector, e.g. **x**
- upper-case letter for matrix, e.g. X
- scalar function f: X → R
- matrix derivative w.r.t scalar function $\frac{\partial f}{\partial X} = [\frac{\partial f}{\partial X_{ij}}]$

### motivation

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled.png)

### derivative rules

- NOTE: derivative of matrix determinant
    - Jacobi's formula: $d\ det(A) = tr(adj(A)dA)$
    - adjugate of A is the transpose of the cofactor matrix C of A: $adj(A) = C^T$
    - cofactor matrix: $C = ((=1)^{i+j}M_{ij})_{1\le i,j \le n}$
    - (i,j)-minor of A, denoted $M_{ij}$, is the determinant of the (n − 1) × (n − 1) matrix that results from deleting row i and column j of A

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%201.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%201.png)

### trace tricks

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%202.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%202.png)

### chain rule

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%203.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%203.png)

### key derivative principle

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%204.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%204.png)

### examples

- simple matrix multiplications

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%205.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%205.png)

- with per-element functions

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%206.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%206.png)

- with trace and function compound

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%207.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%207.png)

- linear regression

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%208.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%208.png)

- maximum likelihood estimation

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%209.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%209.png)

- multi-variate logistic regression

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2010.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2010.png)

- 2-layer neural network

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2011.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2011.png)

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2012.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2012.png)

---

## 矩阵求导术（下）— matrix function derivatives

link: [https://zhuanlan.zhihu.com/p/24863977](https://zhuanlan.zhihu.com/p/24863977)

### motivation (denominator layout)

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2013.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2013.png)

NOTES

- $\frac{\partial f}{\partial X} = vec(\nabla_{X}f)$  where $\nabla_{X}f$  is a m x n matrix

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2014.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2014.png)

- Hessian matrix

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2015.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2015.png)

- vectorization on matrix derivatives for optimization

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2016.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2016.png)

- other definitions for matrix derivatives

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2017.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2017.png)

- numerator layout and denominator layout

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2018.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2018.png)

### vectorization rules

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2019.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2019.png)

### identities (Kronecker product & commutation matrix)

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2020.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2020.png)

### chain rule

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2021.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2021.png)

### key principles

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2022.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2022.png)

### summary

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2023.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2023.png)

### examples

- simple matrix multiplication

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2024.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2024.png)

- simple per-element function

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2025.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2025.png)

- matrix multiplications + per-element function

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2026.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2026.png)

- logistic regression

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2027.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2027.png)

- multi-variate logistic regression

![Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2028.png](Math%20Matrix%20Calculus%20d765299b2e1143b9b004b81a0e89ecb5/Untitled%2028.png)

---

## References

- matrix cookbook

[](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)

- Matrix Calculus: Derivation and Simple Application

[](https://project.hupili.net/tutorial/hu2012-matrix-calculus/hu2012matrix-calculus.pdf)