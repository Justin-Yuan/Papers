# Learning to Navigate in Cities without a Map 
[link](https://arxiv.org/pdf/1804.00168.pdf)

## Intro 

- developing internal representation of space, grounded by recognisable landmarks and robust visual processing, support continuous self-localisation and a representation of the goal 
- propose a dual pathway architecture that allows locale-specific features to be encapsulated, while still enabling transfer to multiple cities 
- use Google StreetView public API, with high-resolution imagery and graph connectivity 

## Modeling 

- inputs: image and goal description, goal represented as its proximity to a set of fixed landmarks  
- architectures: GoalNav, CityNav, MultiCityNav
- auxiliary heading prediction to counter sparse rewards 
- curriculum learning 