# Scene Dynamics: Counterfactual Critic Multi-Agent Training for Scene Graph Generation
[link](https://arxiv.org/pdf/1812.02347.pdf)

**mind-blowing formulatoin**

## Intro 

- existing methods exploit visual context by modeling message passing among objects; scene dynamic is not properly learned by using the prevailing cross-entropy based supervised learning paradigm, which is not sensitive to graph inconsistency
- 2 inherent mismatches
    - coherent objective v.s. independent reward
    - local action v.s. global pooling reward 
- propose a communicative multi-agent model, objects are viewed as cooperative agents that maximize graph-level metrics such as Recall@K or SPICE
- after several rounds of communication, use a visual relationship detection model for scene graph generation that triggers graph-level reward by comparing generated scene graph with ground-truth 
- to disentangle reward of individual agent action, subtract a counterfactual baseline from the reward by varying the target agent while fixing others before feeding into the reward function 
- discardf the widely-used relatioship nodes, reduce message passing complexity 