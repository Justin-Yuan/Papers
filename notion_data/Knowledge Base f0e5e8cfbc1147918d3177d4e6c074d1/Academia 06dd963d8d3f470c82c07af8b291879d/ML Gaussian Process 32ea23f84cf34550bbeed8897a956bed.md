# ML: Gaussian Process

---

## Introduction to Gaussian Processes - Part I

link: [http://bridg.land/posts/gaussian-processes-1](http://bridg.land/posts/gaussian-processes-1)

### summary

- used to represent a distribution over functions
- nonparametric models that model the function directly
- not only can we model any black-box function, we can also model our uncertainty
- key idea behind GPs is that a function can be modeled using an infinite dimensional multivariate Gaussian distribution. In other words, every point in the input space is associated with a random variable and the joint distribution of these is modeled as a multivariate Gaussian.

### prediction with gaussian process

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled.png)

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%201.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%201.png)

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%202.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%202.png)

---

## Gaussian Processes

link: [https://borgwang.github.io/ml/2019/07/28/gaussian-processes.html](https://borgwang.github.io/ml/2019/07/28/gaussian-processes.html) 

### gp as distribution of functions

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%203.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%203.png)

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%204.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%204.png)

### hyperparameters optimization

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%205.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%205.png)

### gp pros & cons

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%206.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%206.png)

---

## Gaussian Process (from kernel perspective)

link: [https://zhuanlan.zhihu.com/p/69353432](https://zhuanlan.zhihu.com/p/69353432) 

### kernel linear regression

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%207.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%207.png)

### kernel density estimation

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%208.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%208.png)

NOTE: wrong here, should be $g(x) = \int f(x,t)dt$

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%209.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%209.png)

### gaussian process motivation

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2010.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2010.png)

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2011.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2011.png)

### gp for regression

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2012.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2012.png)

### gp as kernel regression

![ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2013.png](ML%20Gaussian%20Process%2032ea23f84cf34550bbeed8897a956bed/Untitled%2013.png)

---

---

## Tools