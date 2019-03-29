# Embodies Question Answering 
[link](https://arxiv.org/pdf/1711.11543.pdf)

#### Intro 

- agent to learn active perception, common sense reasoning, language grounding, credit assignment 
- represent each question as a **functional program**, able to be programmatically generated and executed (like CLEVR)
- EQA generation engine, v1 with 4 question types: location, color, color_room, preposition 

## Modeling 

- 4 modules: vision, language, navigation, answering 
- uses Adaptive Computation Time navigator, planner + controller
- initialize agent via imitation learning 
- answering module attends to past observed frames, output logits to fixed set of possible answers 
- rewards: question answering accuracy + reward shaping as distance to target 
- REINFORCE with baseline -> should have something to encourage exploration 

## Evaluation 

- mean rank of tround truth in sorted prediction list 
- navigation accuracy by distance to target at termination 
- baselines to justify the proposed effectiveness of multi-modal input 
- oracles: human nav, groud truth shortest path + VQA 

## Future Work 

- explicit memory to LSTM 
- encourage exploration 
- ray tracing with frame rendering 