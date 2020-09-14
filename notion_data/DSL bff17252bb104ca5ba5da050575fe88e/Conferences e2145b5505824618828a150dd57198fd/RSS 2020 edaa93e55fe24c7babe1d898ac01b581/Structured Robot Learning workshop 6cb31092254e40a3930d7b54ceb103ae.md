# Structured Robot Learning workshop

link: [https://sites.google.com/view/rss20-sar](https://sites.google.com/view/rss20-sar)

youtube link: 

[RSS 2020 - SARL WS](https://www.youtube.com/channel/UCfVS4JoKJC1QresIkSCf21A)

### Summary

- we don't fully understand priors, also hard to encode them
- necessity of multi-task
- action representation makes a difference, but not yet know how to switch between them or the lower level primitives （motor basis)
- have diverse, large-scale data for algorithms to benchmark on
    - set of basis tasks to test with
    - but coming up with tasks is hard
        - could resort to goal-conditioned RL or Universal Value Functions
        - image-based goal-conditioned learning
        - represent goals via language commands
- computer vision is cheating with direct supervision, in comparison, robotics does not have those and babies do not learn with that (but instead with self-supervision)
- robotics simulation can also be seen as cheating
- robotics also have rish temporal supervision
- although simulation could have sim2real problems, but it still allows to explore diverse tasks
- simulation can generate partial sensory data, the hard part is figure out a mapping of these sensory data
- how to interface with the robot ?
- need to make progress additive, need to cluster problems that are important

- stochastic optimal control
- planning under nucertainty
    - how to define uncertainty
- how to testify systems
    - simulation, metrics
- attaching priors to data collection process and gain savings
- besides collecting more data, optimization is essential
- what kind of generalizations our systems are able to reach ?
- think about what must be true 10 years later down the line, e.g. robots having cameras → vision-based control
- need diverse sets of robotics platforms/environments running simulations for benchmarking
    - get simulators to tackle long-tail regions
    - sourcing variations from reality to simulations
    - simulator doesn't have to be accurate or complete to be useful
        - using simplified/biased simulator with real data to accelerate learning

### Papers

**1. [Learning Visuomotor Policies for Aerial Navigation Using Cross-Modal Representations](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F1_visuomotor.pdf&sa=D&sntz=1&usg=AFQjCNGUV1xiLB8982ghB95MOMbYUFrHdw) [[talk](https://youtu.be/AxE7qGKJWaw)]**

Rogerio Bonatti, Ratnesh Madaan, Vibhav Vineet, Sebastian Scherer, Ashish Kapoor

2. **[Learning topological motion primitives for knot planning](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F2_knotplanning.pdf&sa=D&sntz=1&usg=AFQjCNGJQ3_SEj9v8WL9I0sZ0QyCqeSW3g) [[supplementary video](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F2_knotplanning_supplemental.mp4&sa=D&sntz=1&usg=AFQjCNFqnKnP-LaeALoUr4wn1tgtlukgAA)] [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F2_knotplanning_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGKqwzR3iihi9DuEVNbiCNdfz2OEg)]**

Mengyuan Yan, Gen Li, Yilin Zhu, Jeannette Bohg

3. **[gradSLAM: Automagically differentiable SLAM](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F3_gradslam.pdf&sa=D&sntz=1&usg=AFQjCNH5ilFnZSGzNQcFTS0MFQxe0W86Rw) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F3_gradslam_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGz6VSzyfSCOWo4JC-znc12BFNY8w)]**

Krishna Murthy Jatavallabhula, Ganesh Iyer, Soroush Saryazdi, Liam Paull

4. **[BayesRace: Learning to race autonomously using prior experience](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F4_bayesrace.pdf&sa=D&sntz=1&usg=AFQjCNHwQlSQkVod8EtDX1pMBuWbrh2XIg) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F4_bayesrace_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGXKG-ggX3xeQb_hLlwVkNATtHZzg)]**

Achin Jain, Pratik Chaudhari, Manfred Morari

5. **[Hindsight for Foresight: Unsupervised Structured Dynamics Models from Physical Interaction](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F5_hindsight.pdf&sa=D&sntz=1&usg=AFQjCNGdSj77RXQW0qAVNw9AcyRLiDx2IA) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F5_hindsight_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNF6yzny2hUXoBBsI6CfkLjglvx8yg)]**

Iman Nematollahi, Oier Mees, Lukas Hermann, Wolfram Burgard

6. **[Learning State-Dependent Losses for Inverse Dynamics Learning](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F6_inversedynamics.pdf&sa=D&sntz=1&usg=AFQjCNEaiP36aCXjAVWLicyuLqYEmjZe7A) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F6_inversedynamics_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGhLVb_6G5Iq1ThLRiNJB82MZu-Tg)]**

Neha Das, Kristen Morse, Yixin Lin, Austin Wang, Akshara Rai, Franziska Meier

7. **[How to Train Your Differentiable Filter](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F7_differentiablefilter.pdf&sa=D&sntz=1&usg=AFQjCNHXaMQH9m5t3rpR6jS6Su9NkmlqnA) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F7_differentiablefilter_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGTyE6EB1r2uHMeXHfgRRBPcW8DsQ)]**

Alina Kloss, Georg Martius, Jeannette Bohg

8. **[Attention-Privileged Reinforcement Learning](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F8_april.pdf&sa=D&sntz=1&usg=AFQjCNEziM_eWA4h2mU6n31pO3yZROvwjQ) [[appendix](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F8_april_appendix.pdf&sa=D&sntz=1&usg=AFQjCNE6bVmplLLR4DpuKZbHjBEq9Yvg_g)] [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F8_april_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNHoTzSWpzV1upjvNSb0ASMfrNfspg)]**

Sasha Salter, Dushyant Rao, Markus Wulfmeier, Raia Hadsell, Ingmar Posner

9. **[Locally-Connected Interrelated Network: A Forward Propagation Primitive](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F9_lcinet.pdf&sa=D&sntz=1&usg=AFQjCNHoA-6QyA47TB2vbQTjUOXPbFPJUg) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F9_lcinet_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNH9BCrZx9m9cWtpTeJR8jI3P91JAQ)]**

Nicholas Collins, Hanna Kurniawati

10. **[Stein Variational Model Predictive Control](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F10_svmpc.pdf&sa=D&sntz=1&usg=AFQjCNGiR9o71TC_20_f8rDEJSqjOVKSBA) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F10_svmpc_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNHCla3g1RBPLFCvPleEqGfUEOKJbA)]**

Alexander Lambert, Fabio Ramos, Adam Fishman, Dieter Fox, Byron Boots

11. **[A Differentiable Newton Euler Algorithm for Multi-body Model Learning](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F11_newton_euler.pdf&sa=D&sntz=1&usg=AFQjCNHa3EOD-cHYn8wZj5DgTrz8Z2_Y3Q) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F11_newton_euler_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNH5uIZOW2V-6gIzJ2XgufvmN2XUzw)]**

Michael Lutter, Johannes Silberbauer, Joe Watson, Jan Peters

12. **[Learning Rewards via State Marginal Matching](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F12_rewstatemargin.pdf&sa=D&sntz=1&usg=AFQjCNGHRRsiDuiJLKKmWHOYjGmGOa9bsQ) [[appendix](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F12_rewstatemargin_appendix.pdf&sa=D&sntz=1&usg=AFQjCNFNjNXGmo7P3NY6NsmndC6NbLh5Kg)] [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F12_rewstatemargin_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNE54V0j-Ff5zDwoyEcJcl5FNtgPyg)]**

Tejus Gupta, Tianwei Ni, Harshit S Sikchi, Yufei Wang, Ben Eysenbach, Lisa Lee

13. **[Learning Off-Policy with Online Planning](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F13_loop.pdf&sa=D&sntz=1&usg=AFQjCNHzqMZftmYRmblLmusnz3rn2zpZFg) [[appendix](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F13_loop_appendix.pdf&sa=D&sntz=1&usg=AFQjCNFKylaEZ2h7daAxTpxyelUY73cOzg)] [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F13_loop_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNEwF-f36aWXicAMk8LnRtj8_b90PA)]**

Harshit S Sikchi, Wenxuan Zhou, David Held

14. **[Bayesian Residual Policy Optimization: Scalable Bayesian Reinforcement Learning with Clairvoyant Experts](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F14_brpo.pdf&sa=D&sntz=1&usg=AFQjCNEwR4qEf49NWndfrxqRXsykHqXauw) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F14_brpo_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGBE9uOEEYFx-ugISek4ePCou_4Ng)]**

Gilwoo Lee, Brian Hou, Sanjiban Choudhury, Siddhartha Srinivasa

15. **[Efficient Learning of Discontinuous Contact Dynamics with Smooth Parameterizations](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F15_contact.pdf&sa=D&sntz=1&usg=AFQjCNGgheaL6lwwfa6Iwbq0FBIWQo95dw) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F15_contact_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNFVSStTR31tjSd87XKmy0lBBktISQ)]**

Samuel Pfrommer, Mathew Halm, Michael Posa

16. **[Towards Differentiable Resampling](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F16_resampling.pdf&sa=D&sntz=1&usg=AFQjCNGjRs-UiueUuAQSL6T56nmbgUlmnw) [[talk](https://www.google.com/url?q=https%3A%2F%2Fhomes.cs.washington.edu%2F~barun%2Ffiles%2Fworkshops%2Frss2020_sarl%2Fsubmissions%2F16_resampling_spotlight.mp4&sa=D&sntz=1&usg=AFQjCNGtGt_uOD8MGikvN0tgRihTILA0AQ)]**

Michael H. Zhu, Kevin Murphy, Rico Jonschkowski