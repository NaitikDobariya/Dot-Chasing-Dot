# Dot-Chasing-Dot
An agent learns to chase the prey while avoiding the predator. Previously, the agent was learning via a Q-learning table; now, we have something extra: the existing environment was made compatible with OpenAI Gym, and the agent can be trained with Stable Baselines 3.

This project implements a Q-Learning algorithm (and now Deep RL algorithms as well) to train an agent in a grid-world environment. The agent (Player) learns to pursue prey (food) while avoiding a predator. The environment is dynamic, with the food and predator moving randomly, creating a challenging reinforcement learning problem. The environment promotes strategic behavior through rewards and penalties, with the agent learning to balance short-term and long-term goals effectively.

----------------------------------------
## Quick Install

```bash
# Clone repository
git clone https://github.com/NaitikDobariya/Dot-Chasing-Dot.git
cd Dot-Chasing-Dot

# Install with dependencies
pip install -r requirements.txt
```
----------------------------------------
## Running the Files

```python
# To run table based Q-learning
python3 dot_chasing.py

python3 dot_chasing_RL.py
```

That’s it, both files are simple and easy to tweak. Hyperparameters are directly editable inside the scripts.

----------------------------------------
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

----------------------------------------
## Q-Learning Implementation
### State Representation
The state is represented by the relative positions of the agent to the food and predator, encoded as tuples:
- (player - food, player - predator)

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

----------------------------------------
## Features
- **Dynamic Visualizations:** The grid-world environment is rendered using OpenCV for real-time visualization of the agent's behavior during training.
- **Hyperparameter Control:** Adjustable parameters for episodes, learning rate, discount factor, and exploration decay. There is full control over the hyperparameters, and tuning them gives better performance.
- **Performance Tracking:** Rewards per episode are logged to track learning progress.

----------------------------------------
## Results
The agent learns to efficiently navigate the grid-world, optimizing its strategy to collect food while effectively avoiding the predator, and learns to do that faster and faster as it learns. Run the file dot_chasing.py to see it for yourself. Making tweaks is straightforward once you open the file and see it. The following video demonstrates the entire process. The purple dot is the agent, the green dot is the food for the agent, and the red dot is the predator:

![Dot_chasing](https://github.com/user-attachments/assets/a4707590-5c18-4b53-94ac-1dae2b803f9d)

For the Deep Reinforcement learning part, the best results were given by PPO during my attempts. The agent begins to get an average reward of ~42 points after just 10 episodes, which is the optimal reward value given the environment and rewards parameters. Learning within 10 episodes is a great marker of performance. To run this for yourself, run the dot_chasing_RL.py file. The code is very intuitive to read, and making tweaks is straightforward.
<img width="999" height="599" alt="results" src="https://github.com/user-attachments/assets/d6588bee-3607-4d2d-bf25-6f81ca2d1ab0" />

----------------------------------------
## Future Work
- Extending to multi-agent environments.
