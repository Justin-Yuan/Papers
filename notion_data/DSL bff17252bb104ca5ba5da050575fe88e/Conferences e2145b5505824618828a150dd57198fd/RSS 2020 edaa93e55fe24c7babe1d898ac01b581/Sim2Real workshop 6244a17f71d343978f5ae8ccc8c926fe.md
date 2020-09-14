# Sim2Real workshop

link: [https://sim2real.github.io/](https://sim2real.github.io/)

### Summary

- better/full model of uncertainty for dealing with dynamic vehicles
- sim2real will be a major tool in attacking prediction problem in robotics
- sim2real connect to model-based RL
    - approximate dynamic programming
    - when models are difficult to get, started steering towards model-free methods
    - selective planning → agents learns a model but knows the uncertainty, where estimation is accurate and where is uncertain
- sim2real is significant for robotics since the reality gap is non-trivial
- optimization bias in simulation ?
    - small things (contact forces) resulting in infinite disturbance
    - make policy create solution that is never realistic
    - might need to make the simulation more physical which beats the benefit
- how to define sim2real, problem setting or solution strategy ?
    - one is training offline and deploying online
    - the other one is using an interleaving process
- both sim2real and real2sim are necessary
    - close the loop and prevent simulation learning small artifacts
    - simulation can be self-building, self-healing and self-generalizing
        - very similar to model-based RL, same kind of issues likely to occur in both
    - how is that different from adaptive control ?
        - one cannot just write down the model ?
        - but you can use a non-parametric model ?
- simulator as physical system or an abstract system
    - if abstract, seems to be very internal to the system
- should always be suspicious to the model, sim2real is hard to believe
    - create series of guarantees for the model and keep updating them be tighter
    - connect to Bayesian RL
- simulation as prediction for long-term autonomy
    - connect to continual learning
- put prior to the learning model
    - online adaptation is powerful, might favor black-box models (hard to interpret)
- hierarchical simulation might be the way to go
    - combining perception and planning
    - coping with adaptation in the presence of failure

- only need to get the right details right in the simulators
- close the loop by knowing what we need to know about and gather data there
- using inaccurate simulator is also viable
    - easier to scale and can focus on diversity, subsetting the real world
    - combine simple but inaccurate model with real-world learning, e.g. residual learning
    - provide strong prior for planning
    - also for control, only need to learn good error residual
    - accurate simulation might be harder for system to adapt (to specialized)
- improving model accuracy doesn't correlated to robot performance
    - goodness doesn't 100% transfer to the policy
- human internal model is also sloppy
    - realistic domain randomization better than naive randomization
- accurate simulation for imperfect sensing
- hierarchical modeling and composable physics (engine) (something like CAD)

### Papers

**“Accurate High Fidelity Simulations for Training Robot Navigation Policies for Dense Crowds using Deep Reinforcement Learning”**

Jing Liang, Utsav Patel, Adarsh Jagan Sathyamoorthy, Dinesh Manocha

**“Augmenting Differentiable Simulators with Neural Networks to Close the Sim2Real Gap”**

Eric Heiden, David Millard, Erwin Coumans, Gaurav Sukhatme

**“CuNAS - CUriosity-driven Neural-Augmented Simulator”**

Sharath Chandra Raparthy, Melissa Mozifian, Liam Paull, Florian Golemo

**“Continual Learning on Incremental Simulations for Real-World Robotic Manipulation Tasks”**

Josip Josifovski, Mohammadhossein Malmir, Noah Klarmann, Alois Knoll

**“Extended Abstract: An Imitation from Observation Approach to Sim-to-Real Transfer”**

Siddharth Desai, Ishan Durugkar, Haresh Karnan, Garrett Warnell, Josiah Hanna, Peter Stone

**“How to Sim2Real with Gaussian Processes: Prior Mean versus Kernels as Priors”**

Rika Antonova, Akshara Rai, Danica Kragic

**“Learning to Walk without Dynamics Randomization”**

Jeremy Dao, Helei Duan, Kevin Green, Jonathan Hurst, Alan Fern

**“Modular Latent Space Transfer with Analytic Manifold Learning”**

Rika Antonova, Maksim Maydanskiy, Danica Kragic, Sam Devlin, Katja Hofmann

**“On Assessing the Value of Simulation for Robotics”**

Liam Paull, Anthony Courchesne

**“Online BayesSim for Combined Simulator Parameter Inference and Policy Improvement”**

Rafael Possas, Fabio Ramos, Dieter Fox, Lucas Barcelos, Rafael Oliveira

**“Robust Sim2Real Transfer by Learning Inverse Dynamics of Simulated Systems”**

Mohammadhossein Malmir, Josip Josifovski, Noah Klarmann, Alois Knoll

**“Sim2Real Learning of Vision-based Obstacle Avoidance for Robotic Manipulators”**

Kefang Zhang, Tan Zhang, Jiatao Lin, Lv Bi

**“Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?”**

Abhishek Kadian, Joanne Truong, Aaron Gokaslan, Alexander Clegg, Erik Wijmans, Stefan Lee, Manolis Savva, Sonia Chernova, Dhruv Batra