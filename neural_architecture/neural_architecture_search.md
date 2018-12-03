### Neural Architecture Optimization
[link](https://arxiv.org/pdf/1808.07233.pdf)

#### Intro 

- propose to optimize network architecture by mapping architectures into a contunuous vector space (network embedding)
- build a regression model on top as a performance predictor 
- optimize to obtain the continuous representation of a better network, use decoder to recover the new discrete architecture 

#### Modeling 

- decoder is a LSTM with attention 
- jointly training of encoder, predictor and decoder in a multi-task setting (image classification & language modeling)
- encoder takes string sequence describing an architecture, decoder decodes out the string tokens from embedding 

#### Future Work 

- more powerful models, e.g. mixture of softmax for language modeling 
- NAO for other applications, e.g. neural machine translation 
- apply **learning to teach**


<!--- *********************************************************************************************************************************************** --->
--- 

### Efficient neural architecture search via parameter sharing
[link](https://arxiv.org/pdf/1802.03268.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

###  Differentiable architecture search
[link](https://arxiv.org/pdf/1806.09055.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Neural architecture search with bayesian optimisation and optimal transport
[link](https://arxiv.org/pdf/1802.07191.pdf)



<!--- *********************************************************************************************************************************************** --->
--- 

### Understanding and Simplifying One-Shot Architecture Search
[link](http://proceedings.mlr.press/v80/bender18a/bender18a.pdf)




<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 





<!--- *********************************************************************************************************************************************** --->
--- 




<!--- *********************************************************************************************************************************************** --->
--- 