# Dot-Chasing-Dot
Q learning agent learns to chase the prey while avoiding the predator.

This project implements a Q-Learning algorithm to train an agent in a grid-world environment. The agent (Player) learns to pursue prey (food) while avoiding a predator. The environment is dynamic, with the food and predator moving randomly, creating a challenging reinforcement learning problem. The environment promotes strategic behavior through rewards and penalties, with the agent learning to balance short-term and long-term goals effectively.

## Environment Description
The world is a two-dimensional grid where each cell can be occupied by the agent, food, or predator. The dynamics for the presented example are as follows:

- **Agent (Player):** Learns to chase food and avoid the predator.
- **Food:** Moves randomly and rewards the agent when captured.
- **Predator:** Moves randomly and penalizes the agent if captured.
- **Rewards and Penalties:**
  - Eating food: +250 reward
  - Being caught by the predator: -500 penalty
  - Each move: -5 penalty to encourage efficiency

The environment promotes quick decision-making and effective pathfinding using Q-learning.

## Q-Learning Implementation
### State Representation
The state is represented by the relative positions of the agent to the food and predator, encoded as tuples:
- `(player - food, player - predator)`

### Action Space
The agent can take one of four possible actions:
1. Move up
2. Move down
3. Move left
4. Move right

### Q-Table
The Q-table is initialized as a dictionary mapping states to action values, allowing the agent to estimate the expected utility of each action in a given state.

### Update Rule
The Q-values are updated using the following algorithm:
![image](https://github.com/user-attachments/assets/895ed2bc-c4eb-4933-a3dc-aad5ada64c54)


### Exploration vs. Exploitation
An epsilon-greedy strategy is used to balance exploration and exploitation, with epsilon decaying over time.

## Features
- **Dynamic Visualizations:** The grid-world environment is rendered using OpenCV for real-time visualization of the agent's behavior during training.
- **Hyperparameter Control:** Adjustable parameters for episodes, learning rate, discount factor, and exploration decay. There is full control over the hyperparameters and tunning them gives better performance.
- **Performance Tracking:** Rewards per episode are logged to track learning progress.

## Results
The agent learns to efficiently navigate the grid-world, optimizing its strategy to collect food while effectively avoiding the predator and learns to do that fatser and faster as it learns. The following video demonstrates the entire process, the purple dot is the agent, the green dot is the food for the agent, and the red dot is the predator:

![Dot_chasing](https://github.com/user-attachments/assets/a4707590-5c18-4b53-94ac-1dae2b803f9d)

## Future Work
- Extending to multi-agent environments.
- Using deep reinforcement learning to handle larger state spaces.



