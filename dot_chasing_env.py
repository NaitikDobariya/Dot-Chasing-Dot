import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2

from assets.dot import Dot
from assets.playground import Playground

class DotChaseEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, length=10, breadth=10, move_penalty=1, food_reward=50, enemy_penalty=50, move_dots=True):
        super().__init__()

        self.length = length
        self.breadth = breadth
        self.move_penalty = move_penalty
        self.food_reward = food_reward
        self.enemy_penalty = enemy_penalty
        self.move_dots = move_dots

        self.action_space = spaces.Discrete(4)

        obs_low = np.array([-self.length, -self.breadth, -self.length, -self.breadth], dtype=np.int32)
        obs_high = np.array([self.length, self.breadth, self.length, self.breadth], dtype=np.int32)
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.int32)

        self.render_on = False
        self.scale = 50  # for rendering

        self.reset()

    def _get_obs(self):
        # Returns relative positions as a single flattened observation
        return np.array((self.player - self.food) + (self.player - self.enemy), dtype=np.int32)


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.player = Dot((75, 0, 130), self.length, self.breadth)
        self.food = Dot((50, 205, 50), self.length, self.breadth)
        self.enemy = Dot((0, 10, 255), self.length, self.breadth)

        self.episode_reward = 0

        return self._get_obs(), {}

    def step(self, action):
        self.player.action(action)

        if self.move_dots:
            self.food.move()
            self.enemy.move()

        terminated = False
        reward = -self.move_penalty

        if self.player.x == self.enemy.x and self.player.y == self.enemy.y:
            reward = -self.enemy_penalty
            terminated = True
        elif self.player.x == self.food.x and self.player.y == self.food.y:
            reward = self.food_reward
            terminated = True

        self.episode_reward += reward

        if self.render_on:
            self._render_frame()

        return self._get_obs(), reward, terminated, False, {}

    def render(self):
        self.render_on = True

    def _render_frame(self):
        env = np.zeros((self.breadth, self.length, 3), dtype=np.uint8)
        env[self.player.y][self.player.x] = self.player.color
        env[self.food.y][self.food.x] = self.food.color
        env[self.enemy.y][self.enemy.x] = self.enemy.color

        frame = cv2.resize(env, (self.length * self.scale, self.breadth * self.scale), interpolation=cv2.INTER_NEAREST)
        cv2.imshow("DotChaseEnv", frame)
        if cv2.waitKey(70) & 0xFF == ord("q"):
            self.close()

    def close(self):
        cv2.destroyAllWindows()
        self.render_on = False
