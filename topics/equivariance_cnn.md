## Equivariance CNN

<!-- ***************************************************** -->
#### equivariance and invariance 
- For any symmetry operation $\sigma$, applying $\sigma$ to our input and then passing it through the model should be the same as applying σ to the output of the model, for example, if $f$ is equivariant with respect to $\sigma$
$$
f(\sigma(x)) = \sigma(f(x))
$$
- $f$ is invariant if its output doesn’t change upon applying σ to the input.
$$
f(\sigma(x)) = f(x)
$$
- If a layer is an equivariant embedding of the input with respect to a certain symmetry, it can always be turned into an invariant embedding in a later layer. 

##### symmetry and group 
- A symmetry with respect to a property is a transformation that leaves the property unchanged.
- given set $X$ as all possible inputs, elements of $X$ have some property of interest as function $y$, a bijective function $g: X \rightarrow X$ :point_right: $g$ is a symmetry with respect to $y$ if, 
$$
y(g(x)) = y(x), \forall x \in X
$$
- the set of symmetries w.r.t $y$ form a **group**, a group is a set $G$ with an operation $*$ acting on pairs of elements from $G$, with 4 rules 
1. closure: $a * b \in G$
2. asssociativity, $a * (b * c) = (a * b) * c$
3. identity element, $\forall a \in G, \exists e \in G, a * e = e * a = a$
4. inverse elements, $\forall a \in G, \exists a^{-1} \in G, a * a^{-1} = a^{-1} * a = e$
- useful groups (for image): translations, rotations, reflections

#### convolution 
- key formula, with $Z^2$ is the (2D grid) pixel space
$$
(f \star \psi)(x) = \sum_{y \in Z^2} f(y)\psi(y-x) = \sum_{y \in Z^2} f(x+y)\psi(y)
$$
- now viewing $x$ as an element from translation group $t$, (note $f \star \psi$ has group-valued inputs)
$$
(f \star \psi)(t) = \sum_{y \in Z^2} f(t(y))\psi(y)
$$
- extend $f$ and $\psi$ to be defined on group $G$ instead of $Z^2$, now G-convolve becomes ($g,h \in G$)
$$
(f \star \psi)(g) = \sum_{g \in G} f(gh)\psi(g)
$$


<!-- ***************************************************** -->
---
#### List of works
- [Group Equivariant Convolutional Networks](#1)
- [Harmonic Networks: Deep Translation and Rotation Equivariance](#2)
- [STEERABLE CNNS](#3)
- [3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data](#4)
- [Learning to Convolve: A Generalized Weight-Tying Approach](#5)
- [Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data](#6)

<!-- ***************************************************** -->
---
#### Work summaries

<a name="1"></a> 
Group Equivariant Convolutional Networks

[link](https://arxiv.org/pdf/1602.07576.pdf)

--- 
<a name="2"></a> 
Harmonic Networks: Deep Translation and Rotation Equivariance

[link](https://arxiv.org/pdf/1612.04642.pdf)

--- 
<a name="3"></a> 
STEERABLE CNNS

[link](https://arxiv.org/pdf/1612.08498.pdf)

--- 
<a name="4"></a> 
3D Steerable CNNs: Learning Rotationally
Equivariant Features in Volumetric Data

[link](https://arxiv.org/pdf/1807.02547.pdf)

--- 
<a name="5"></a> 
Learning to Convolve: A Generalized Weight-Tying Approach 

[link](https://arxiv.org/pdf/1905.04663.pdf)

--- 
<a name="6"></a> 
Generalizing Convolutional Neural Networks for Equivariance to Lie Groups on Arbitrary Continuous Data

[link](https://arxiv.org/pdf/2002.12880.pdf) 
[code](https://github.com/mfinzi/LieConv)



<!-- ***************************************************** -->
---
#### References

[1] CNNs and Equivariance - Part 1/2 [link](https://fabianfuchsml.github.io/equivariance1of2/)

[2] Group CNNs - Equivariance Part 2/2 [link](https://fabianfuchsml.github.io/equivariance2of2/)


