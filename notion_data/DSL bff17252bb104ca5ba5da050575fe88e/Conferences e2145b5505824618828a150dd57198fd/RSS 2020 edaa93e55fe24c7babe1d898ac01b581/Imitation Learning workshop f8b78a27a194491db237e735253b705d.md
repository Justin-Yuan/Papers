# Imitation Learning workshop

link: [https://sites.google.com/utexas.edu/rss-2020-imitation-learning/home](https://sites.google.com/utexas.edu/rss-2020-imitation-learning/home) 

youtube link: 

[RSS 2020 Workshop on Advances & Challenges in Imitation Learning for Robotics](https://www.youtube.com/watch?v=PZeFYjcbnMA)

### Summary

- paradigm for learning from large scale interaction data
    - two aspects: mimicing and generalization
    - extract strong primitives for better generalization
        - what's the right way to learn primitives from data ?
            - disentanglement, simplicity
- how do we frame the imitation problem correctly ?
- focus on other information coming in, not just actions
- objective function
    - what kind of demonstration should be used
    - but at the same time should not be constrained at this
- find a relaxed, more generalized human model to interpret the information/supervision
- still need a likelihood model at the end
    - how to build in a structure
    - cannot be purely data-driven, since latent is not known and hard to assume it to be fixed
- how to create human models across different interfaces well ?
    - somehow parameterize model to accommodate all the different cognitive biases, but able to be marginalized or know the confidence bound during inference
    - connect to robust optimization
- human providing non-stationary, evolving feedback to the robot
    - figure when, what and how is it cost effective before collecting data
- distinction between imitation learning and human-in-a-loop learning
- what kind of metrics do we want to look at in the long run ?
- multi-dimensional objective function, imitation learning as part of a master algorithm

- need more intuitive and democratized interface to collect human demonstration
- key frames idea from Maya Cakmak
- inferring constraints from demonstrations
    - but specifying hard constraints is hard
- combining demonstration with comparisons
- generate constraints by simulation but not in physical system
- perform counterfactual reasoning for the robot

### Papers

APPLD: Adaptive Planner Parameter Learning from Demonstration 

Xuesu Xiao, Bo Liu, Garrett Warnell, Jonathan Fink and Peter Stone

ToolNet: Using Commonsense Generalization for Predicting Tool Use for Robot Plan Synthesis 

Rajas Bansal, Shreshth Tuli, Rohan Paul and Mausam

Residual Reinforcement Learning from Demonstrations 

Minttu Alakuijala, Gabriel Dulac-Arnold, Julien Mairal, Jean Ponce and Cordelia Schmid

Separating Manners of Execution of Forceful Tasks when Learning from Multimodal Demonstrations 

Yordan Y Hristov and Subramanian Ramamoorthy

Understanding Multi-Modal Perception Using Behavioral Cloning for Peg-In-a-Hole Insertion Tasks 

Diego Romeres, Yifang Liu, Devesh K Jha and Daniel Nikovski

DinerDash Gym: A Benchmark for Policy Learning in High-Dimensional Action Space 

Siwei Chen, Xiao Ma and David Hsu

Learning to Play by Imitating Humans 

Rostam Dinyari, Pierre Sermanet and Corey Lynch

Interactive Imitation Learning in State-space 

Snehal Jauhri, Carlos Celemin and Jens Kober

Augmenting GAIL with BC for sample efficient imitation learning 

Rohit Jena and Katia Sycara