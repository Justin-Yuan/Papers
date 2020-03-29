## Your GAN is Secretly an Energy-based Model and You Should Use

[link](https://arxiv.org/pdf/2003.06060.pdf)
[code](https://github.com/sodabeta7/gan_as_ebm)

<!-- ***************************************************** -->
sum of the implicit generator log-density log(p_g) of a GAN with the logit score of the discriminator defines an energy function which yields the true data density when the generator is imperfect but the discriminator is optimal.

samples can be generated from this modified density by sampling in latent space according to an energy-based model induced by the sum of the latent prior log-density and the discriminator output score.

running Markov Chain Monte Carlo in the latent space, and then applying the generator function.

major advantage of DDLS is that it allows MCMC sampling in the latent space, which enables efficient sampling and better mixing.

<!-- ***************************************************** -->
---
#### Key Points

- 

<!-- ***************************************************** -->
---
#### Results

- test on several toy distributions and CIFAR-10

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References



