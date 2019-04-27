# DIVERSITY IS ALL YOU NEED: LEARNING SKILLS WITHOUT A REWARD FUNCTION
[link](https://arxiv.org/pdf/1802.06070.pdf)

## Intro 

unsupervised emergence of diverse skills 

pretrained skills can provide a good parameter initialization for downstream tasks, and can be composed hierarchically to solve complex sparse reward tasks 

a skill is a latent-conditioned policy that alters the state of the environment in a consistent way 

train the skills that maximize coverage over the set of possible behaviors 

use maximum entropy policies to force our skills to be diverse 

fix the prior distribution over skills, rather than learning it (key difference to Variational Intrinsic Control)

to ensure that states, not actions, are used to distinguish skills, minimize the mutual information between skills and actions given the state 


## Related work 

meta-policy does not select "bad" options, so these options do not receive any reward signal to improve 

