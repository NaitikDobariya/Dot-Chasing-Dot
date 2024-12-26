import numpy as np
import pickle

class Q_table:
    def __init__(self, length : int, breadth : int, table_path : str = False) -> None:
        self.length = length
        self.breadth = breadth

        if not table_path:
            self.table = {}
            for x1 in range(-self.length + 1, self.length):
                for y1 in range(-self.length + 1, self.length):
                    for x2 in range(-self.breadth + 1, self.breadth):
                        for y2 in range(-self.breadth + 1, self.breadth):
                            self.table[((x1, y1), (x2, y2))] = np.random.uniform(-5, 0, 4).tolist()
        
        else:
            with open(table_path, "rb") as f:
                self.table = pickle.load(f)