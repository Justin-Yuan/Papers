## Exploring Structural Inductive Biases in Emergent Communication

[link](https://arxiv.org/pdf/2002.01335.pdf)
[code]()

<!-- ***************************************************** -->
develop a systematically composi- tional language through playing co-operative refer- ential games.

propose novel graph referential games. Game-1 tests hierarchy of concepts and properties. Game-2 is on graph isomorphism test (whether the agents can learn graph topology).

compare the graph representation to a corresponding sequence and bag-of-words en- coding in terms of task success, out-of-domain generalization and language compositionality. 

<!-- ***************************************************** -->
---
#### Key Points

- A referential game consists of a perceptual input, agents, communication channel (discrete symbols without any predefined meaning) and an action to be rewarded (e.g. distinguishing the target input among distractors). variants of the Lewis Signaling Game.
- payoff does not depend on the message sent, and so the agents are rewarded for solving the task and not for the emerged communication protocol.
- speaker has graph encoder, output sequence as message, each output is applied Gumbel-Softmax to generate a token in vocabulary. 
- listen takes in message, output softmax distribution over candidate (target and distractors) embeddings. has graph encoder as well.
- graph encoder uses either GCN or GraphSAGE.
- evaluation uses **Topographic similarity**, essentially objects that are close in the meaning space are mapped to similar signals in message space.

<!-- ***************************************************** -->
---
#### Results

- 

<!-- ***************************************************** -->
---
#### Notes/Questions

- 

<!-- ***************************************************** -->
---
#### References



