import numpy as np

class Dot:
    def __init__(self, color : tuple, length : int, breadth : int) -> None:

        self.color = color   # color is a tuple that represents RGB values
        self.playground_length = length
        self.playground_breadth = breadth
    
        self.x = np.random.randint(0, length)
        self.y = np.random.randint(0, breadth)

    def __str__(self) -> str:
        return f"{self.x} , {self.y}"

    def __sub__(self, other) -> tuple:
        return (self.x - other.x, self.y - other.y)
    
    def action(self, choice : int) -> None:
        # choice is one of the four possible moves in the playground, this function (action) is used for the player whose motion is guided by the Q_table
        if choice == 0:
            self.move(x = 1, y = 1)
        elif choice == 1:
            self.move(x = -1, y = -1)
        elif choice == 2:
            self.move(x = -1, y = 1)
        elif choice == 3:
            self.move(x = 1, y = -1)

    def move(self, x : bool = False, y : bool = False) -> None:
        # this function is used for the food and the enemy, to allow them to move randomly
        
        # making changes in the coordinates i.e. performing motion
        if not x:
            self.x += np.random.randint(-1, 2)
        else:
            self.x += x

        if not y:
            self.y += np.random.randint(-1, 2)
        else:
            self.y += y

        # verifying if the move is valid and the dot does not go out of the box/playground
        if self.x < 0:
            self.x = 0
        if self.x > self.playground_length - 1:
            self.x = self.playground_length - 1
        
        if self.y < 0:
            self.y = 0
        if self.y > self.playground_breadth - 1:
            self.y = self.playground_breadth - 1
        
    
