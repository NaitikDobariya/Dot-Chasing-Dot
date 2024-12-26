import numpy as np
from PIL import Image
import cv2 

from assets.playground import Playground
from assets.dot import Dot
from assets.Q_table import Q_table

class Q_learning:
    def __init__(self, playground : Playground, table : Q_table) -> None:
        self.length = playground.length
        self.breadth = playground.breadth

        self.move_penalty = playground.move_penalty
        self.food_reward = playground.food_reward
        self.enemy_penalty = playground.enemy_penalty

        self.move_dots = playground.move_dots
        
        self.table = table.table
    
    def learn(self, num_episodes : int, episode_len : int, 
              epsilon : float, epsilon_decay : float, 
              discount_rate : float, learning_rate : float, 
              show_every : int) -> None:
        
        self.episode_rewards = []
        for episode in range(num_episodes):
            player = Dot(color = (75, 0, 130), length = self.length, breadth = self.breadth)
            food = Dot(color = (50, 205, 50), length = self.length, breadth = self.breadth)
            enemy = Dot(color = (0, 10, 255), length = self.length, breadth = self.breadth)

            if episode % show_every == 0:
                print(f"current episode {episode}, epsilon : {epsilon}")
                show = True
            else:
                show = False
            
            episode_reward = 0
            for i in range(episode_len):
                obs = (player - food, player - enemy)
                if np.random.random() > epsilon:
                    action = np.argmax(self.table[obs])
                else:
                    action = np.random.randint(0, 4)

                player.action(action)

                if self.move_dots:
                    food.move()
                    enemy.move()

                if player.x == enemy.x and player.y == enemy.y:
                    reward = -self.enemy_penalty
                elif player.x == food.x and player.y == food.y:
                    reward = self.food_reward
                else:
                    reward = -self.move_penalty

                new_obs = (player - food, player - enemy)
                max_future_q = np.max(self.table[new_obs])
                current_q = self.table[obs][action]

                if reward  == self.food_reward:
                    new_q = self.food_reward
                elif reward == self.enemy_penalty:
                    new_q = -self.enemy_penalty
                else:
                    new_q = (1 - learning_rate) * current_q +  learning_rate * (reward + discount_rate * max_future_q)

                self.table[obs][action] = new_q

                if show:
                    # creating a blank RGB array to represent the environment 
                    env = np.zeros((self.breadth, self.length, 3), dtype = np.uint8)

                    # setting the color of the dots in the array
                    env[player.y][player.x] = player.color
                    env[food.y][food.x] = food.color
                    env[enemy.y][enemy.x] = enemy.color

                    img = Image.fromarray(env, "RGB")
                    img = img.resize((100, 100))

                    scale_factor = 50  # Adjust this to control the output size and sharpness
                    img = cv2.resize(env, (self.length * scale_factor, self.breadth * scale_factor), interpolation=cv2.INTER_NEAREST)
                    cv2.imshow(f"Episode {episode}", np.array(img))

                    wait_time = 500 if reward == self.food_reward or reward == -self.enemy_penalty else 70
                    if cv2.waitKey(wait_time) & 0xFF == ord("q"):
                        break

                episode_reward += reward
                if reward == self.food_reward or reward == -self.enemy_penalty:
                    break
            
            cv2.destroyAllWindows()

            self.episode_rewards.append(episode_reward)
            epsilon *= epsilon_decay


