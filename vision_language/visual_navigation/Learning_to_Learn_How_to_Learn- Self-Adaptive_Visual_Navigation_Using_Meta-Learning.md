# Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning
[link](https://arxiv.org/pdf/1812.00971.pdf)

## Intro 

- learning to learn at both training and inference time 
- meta-reinforcement leraning, agent learns a self-supervised interaction loss that encourages effective navigation 

## Modeling 

- Talyor expansion on training objective -> learning to minimize the navigation loss while maximizing the similarity between the gradients from self-supervised interaction loss and the supervised navigatoin loss 
- freeze parameters from interaction loss during inference 

## Evaluation 

- use AI2-THOR, evaluate using both Success Rate and Success weighted by Path Length (SPL), against non-adaptive A3C baseline 
