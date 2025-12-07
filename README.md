# Dot-Chasing-Dot

This project is exactly what it sounds like: a dot chasing another dot while running away from a third dot… except now the chasing dot is actually learning what to do.

It started as a simple Q-learning project where the agent learns to chase food and avoid a predator in a small grid. Later, I made the entire environment Gym-compatible, and now you can throw Stable Baselines 3 at it and watch PPO figure out the “life and death of dots” in barely 10 episodes.

If you want to see an agent panic, survive, strategize, and then suddenly become a genius, this project is perfect.

---

## Installation & Setup

Before running anything, just set things up cleanly:

1. Create a virtual environment:
    ```
    python3 -m venv venv
    ```

2. Activate it:

    **Linux/Mac**
    ```
    source venv/bin/activate
    ```

    **Windows**
    ```
    venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

That’s it. Very straightforward.

---

## Running the Project

### ▶ Q-Learning Version (classic)
If you want to see the old-school Q-learning table grind its way to intelligence, run:

````

python dot_chasing.py

```

This opens a nice OpenCV visualization where:
- Purple dot = Agent  
- Green dot = Food  
- Red dot = Predator  
- The agent starts by running around like an idiot but slowly becomes a pro.

### ▶ Deep RL Version (Stable Baselines 3)
If you want to see the “modern” agent that learns in just ~10 episodes:

```

python dot_chasing_RL.py

```

PPO performed the best in my experiments. The agent very quickly figures out the optimal reward (~42 points). It’s honestly satisfying to watch.

---

## Environment Description

The world is a simple 2D grid with three moving entities:

- **Agent (Player):** has to chase the food while avoiding the predator.
- **Food:** randomly moves around. Touch it → reward.
- **Predator:** also moves randomly. Touch it → *pain.*

### Rewards  
- Food eaten: **+250**  
- Predator catches you: **-500**  
- Every single move: **-5** (because wandering aimlessly shouldn’t pay off)

This forces the agent to learn efficient movement instead of dancing around doing nothing.

---

## Q-Learning Implementation

### State Representation
Each state looks like this:
```

(player - food, player - predator)

```
This captures the relative positions instead of absolute grid positions, which keeps the table compact.

### Actions
The agent can take:
1. Up  
2. Down  
3. Left  
4. Right  

Yep, just simple 4-way movement.

### Q-Table Format
A dictionary:
```

{ state : [Q_up, Q_down, Q_left, Q_right] }

```

### Update Rule  
The classical formula — here’s the reference image you’ve already seen a hundred times:

https://github.com/user-attachments/assets/895ed2bc-c4eb-4933-a3dc-aad5ada64c54

### Exploration
Epsilon-greedy with decay.  
Starts random → slowly becomes confident → eventually masters the grid.

---

## Features

- Smooth OpenCV visualization  
- Full control over every hyperparameter  
- Simple, readable code  
- Gym-compatible environment  
- Stable Baselines 3 support (PPO recommended)  
- Logs episode rewards for learning curves  

---

## Results

Here’s an actual clip of the agent learning.  
**Purple = agent, Green = food, Red = predator.**

https://github.com/user-attachments/assets/a4707590-5c18-4b53-94ac-1dae2b803f9d

And here’s the graph for the PPO version (the deep RL agent that learns insanely fast):

https://github.com/user-attachments/assets/d6588bee-3607-4d2d-bf25-6f81ca2d1ab0

The agent starts hitting ~42 points of reward after just 10 episodes, which is basically optimal given the reward structure.

---

## Future Work

- Expand this to a multi-agent ecosystem — maybe agents competing, cooperating, or even forming predator–prey hierarchies.  
- More chaos, more emergent behavior.






