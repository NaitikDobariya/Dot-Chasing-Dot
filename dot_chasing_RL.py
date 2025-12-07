import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import PPO, A2C, DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor

from dot_chasing_env import DotChaseEnv

# Create the environment
env = DotChaseEnv()
env = Monitor(env)
env = DummyVecEnv([lambda: env])

# Instantiate the model
model = PPO("MlpPolicy", env, verbose=1, device='cuda')

# Training loop with render toggle and reward tracking
num_episodes = 10
episode_length = 100
reward_history = []

# env.envs[0].env.enable_render = True  # Enable rendering

for ep in range(num_episodes):

    obs = env.reset()
    done = False
    ep_reward = 0
    steps = 0
    while not done and steps < episode_length:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)

        # # start rendering for the last 10 episodes
        # if ep >= 90:
        #     env.envs[0].env.render()

        ep_reward += reward[0]
        steps += 1
    reward_history.append(ep_reward)
    model.learn(total_timesteps=100, reset_num_timesteps=False)

# Plotting rewards
plt.figure(figsize=(10, 6))
plt.plot(reward_history, label="Episode reward")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Reward vs Episode (Dot Chasing Game)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
