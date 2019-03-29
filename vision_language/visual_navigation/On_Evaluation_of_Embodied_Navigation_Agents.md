# On Evaluation of Embodied Navigation Agents
[link](https://arxiv.org/pdf/1807.06757.pdf)

## Intro 

- propose common task definitions and evaluaoin protocols 
- Goal specification: PointGoal, ObjectGoal, AreaGoal 
- Generalization/Exploration: No prior exploration, Pre-recorded prior exploration, Time-limited exploration by the agent

## Recommendations 

- The agent must be equipped with a special action that indicates that it has concluded the navigation episode and is ready to be evaluated. 
- To measure proximity, use the geodesic distance, i.e., the shortest-path distance in the environment 
- Adopt Success weighted by Path Length (SPL) as primary measure of navigation performance 
- structure of the internal representation that the agent constructs and maintains