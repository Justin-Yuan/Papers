# Visual Translation Embedding Network for Visual Relation Detection
[link](https://arxiv.org/pdf/1702.08319.pdf)

## Intro 

- relation modeled as a vector translation, subject + predict ~ object 
- feature extraction layer for class probabilities, locations(bbox coordinates and scales), RoI visual features 

## Modeling 

- projection matrices from feature space to relation space 
- use large-margn metriclearning loss function 
