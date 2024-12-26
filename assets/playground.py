import numpy as np

class Playground:
    def __init__(self, length : int, breadth : int, move_penalty : float, food_reward : float, enemy_penalty : float, move_dots : bool = False) -> None:
        self.length = length
        self.breadth = breadth

        self.move_penalty = move_penalty
        self.food_reward = food_reward
        self.enemy_penalty = enemy_penalty

        self.move_dots = move_dots