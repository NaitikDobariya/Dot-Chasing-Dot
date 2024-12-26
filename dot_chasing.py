import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from assets.playground import Playground
from assets.Q_table import Q_table

from processes.Q_learning import Q_learning

# defining the playground 
length = 10
breadth = 10

move_penalty = 5
food_reward = 250
enemy_penalty = 500

move_dots = True

playground = Playground(length = length,
                        breadth = breadth,
                        move_penalty = move_penalty,
                        food_reward = food_reward,
                        enemy_penalty = enemy_penalty,
                        move_dots = move_dots)

# instantiating the Q_table class
q_table = Q_table(length = length,
                  breadth = breadth)

# instantiating the Q_learning class
q_learning = Q_learning(playground = playground,
                        table = q_table)

# defining the learning parameters
num_episodes = 60000
episode_len = 200
epsilon = 0.99
epsilon_decay = 0.95
learning_rate = 0.1
discount_rate = 0.5

show_every = 5000

q_learning.learn(num_episodes = num_episodes,
                 episode_len = episode_len,
                 epsilon = epsilon,
                 epsilon_decay = epsilon_decay,
                 discount_rate = discount_rate,
                 learning_rate = learning_rate,
                 show_every = show_every)

# instantiating the Q_table class
q_table_1 = Q_table(length = length,
                  breadth = breadth)

# instantiating the Q_learning class
q_learning_1 = Q_learning(playground = playground,
                        table = q_table_1)

# # defining the learning parameters
# num_episodes = 20000
# episode_len = 100
# epsilon = 0.7
# epsilon_decay = 0.95
# learning_rate = 0.35
# discount_rate = 0.9999

# show_every = 500

# q_learning_1.learn(num_episodes = num_episodes,
#                  episode_len = episode_len,
#                  epsilon = epsilon,
#                  epsilon_decay = epsilon_decay,
#                  discount_rate = discount_rate,
#                  learning_rate = learning_rate,
#                  show_every = show_every)

#plotting the results
returns = q_learning.episode_rewards
# returns_1 = q_learning_1.episode_rewards
plt.plot(np.convolve(np.array(returns), np.ones(200)/200, mode='valid'))
# plt.plot(np.convolve(np.array(returns_1), np.ones(200)/200, mode='valid'))
plt.show()
