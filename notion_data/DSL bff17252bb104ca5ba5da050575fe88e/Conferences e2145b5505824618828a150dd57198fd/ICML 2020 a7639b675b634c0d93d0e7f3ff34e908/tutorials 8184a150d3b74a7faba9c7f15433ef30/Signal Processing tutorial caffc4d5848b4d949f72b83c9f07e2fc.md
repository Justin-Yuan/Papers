# Signal Processing tutorial

link: 

### temporal models

- 1d problem
- spatio-temporal model
- long/unbounded data

### tools and discrete-time models

- moment representation
    - consider statistical properties of data jointly over time
- spectral (Fourier) representation
    - analyze in frequency-space
    - Fourier transform
    - analyze properties of "systems" (input-output mappings) by transfer functions
- state space (path) representation
    - description of sample behavior as a dynamic system over time
    - key to efficiency is the directed graph (Markov property)
    - linear-Gaussian filtering problems
        - nice closed-form solution, filtering $p(x_k | y_{1:k})$ or smoothing $p(x_k | y_{1:T})$
    - non-linear dynamics, measurements
        - e.g. sensor fusion by non-linear Kalman filtering
        - sequential Monte-Carlo (particle filtering)

### SDEs (continuous-time models)

- 

### Gaussian processes

### Applications