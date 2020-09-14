# Self-supervised Robot Learning workshop

link: [https://www.brainlinks-braintools.uni-freiburg.de/rss-2020-workshop/](https://www.brainlinks-braintools.uni-freiburg.de/rss-2020-workshop/)

youtube link: 

[RSS 2020 Workshop on Self-Supervised Robot Learning](https://www.youtube.com/watch?v=VY4oaRIkzqI&feature=emb_err_woyt)

### Summary

- Dieter Fox
    - model-based mapping
        - short to long-range correspondence
    - autonomous data collection
- Self-supervised Curious Robots by Abhinav Gupta
    - stages/paradigm: pasive & visual → random & actions → active exploration (actions) → imitate → social (other agents)
    - super-sizing self-supervised learning (log-linear improvement)
    - curiosity reward
        - learn several environemnt model and reward based on disagreement on next state prediction
- Scalable Robot Learning with Play and Language by Pierre Sermanet
    - play data, rich, diverse and easy to collect (use hindsight instructions)
- Data scalability for robot learning by Chelsea Finn
    - develop algorithms that can train on scalable data sources
    - accumulate and reuse broad datasets across labs
        - collect dataset, e.g. RoboNet
        - evaluate if it's useful (on a set of tasks)
    - use other data ? e.g. video
        - challenge: domain shift and no action representation
        - use video prediction model
    - underfitting large, diverse dataset → modeling everything is hard
        - learn to model only what matters
        - scalable self-supervised approach & task-oriented representation and predictoin
        - Goal-aware prediction
            - redistribute model capacity
            - the worse the trajectory for the goal, the greater prediction error we can afford
    - to generalize broadly, train it on equally broad data
- Can learning from pixels be as efficient as learning from state ? by Pieter Abbeel
    - contrastive learning: SOTA in computer vision
    - keys encoded with momentum
    - CURL can be used even without rewards, fits for multitask
    - but current CURL contrastive representation do not incorporate temporal structure
    - state-based learning + data augmentation ?
- Learning to see actions for vision-based manipulation from Andy Zeng
    - definition of "object" varies by tasks and agents
    - Form2Fit, learning shape priors
    - vision based grasping with affordances
    - TossingBot: self-supervised learning + automatic resets
        - learns to cluster object visual features in learnt intermediate features
    - how should robots learn the semantics of the visual world ?
        - object detection, pose estimation: human defined "objects"
        - end-tp-end learning + self-supervision
        - on the other way round, attach vision problem where "objectness" emerges as a byproduct
- safe learning
- how do we verify / benchmark self-supervised learning ?
    - might need some external supervision

### Papers

- **[On the Sensory Commutativity of Action Sequences for Embodied Agents](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_2.pdf)Hugo Caselles-Dupré, Michael Garcia-Ortiz and David Filliat**
- **[From Images to Task Planning: How NLP Can Help Physical Reasoning](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_17.pdf)**Son Tung Nguyen, Ozgur S. Oguz, Danny Driess and Marc Toussaint
- **[Self-Supervised, Goal-Conditioned Policies for Navigation in Unstructured Environments](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_12.pdf)**Travis Manderson and Gregory Dudek
- **[Towards Self-Supervised Semantic Representation with a Viewpoint-Dependent Observation Model](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_10.pdf)**Yuri Feldman and Vadim Indelman
- **[Robot Perception enables Complex Navigation Behavior via Self-Supervised Learning](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_13.pdf)**Marvin Chancan and Michael Milford
- **[Using Variational Encoding and Generative Adversarial Learning for Inferring Missing Knowledge for Mobile Robots](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_14.pdf)**Francesco Riccio, Roberto Capobianco and Daniele Nardi
- **[Learning State-Dependent Losses for Inverse Dynamics Learning](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_15.pdf)**Neha Das, Kristen Morse, Yixin Lin, Austin Wang, Akshara Rai and Franziska Meier
- **[Just Go with the Flow: Self-Supervised Scene Flow Estimation](https://www.brainlinks-braintools.uni-freiburg.de/fileadmin/media/pdf/RSS20-SSRL/SSRL20_paper_16.pdf)**Himangi Mittal, Brian Okorn and David Held