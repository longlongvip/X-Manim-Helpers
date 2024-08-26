import numpy as np


class Pos2D:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_numpy(self):
        return np.array([self.x, self.y, 0.0])

    def to_list(self):
        return [self.x, self.y, 0.0]

    def print(self):
        print(f"Position2D ==> x : {self.x}, y:{self.y}")


class Pos:
    x = 0.0
    y = 0.0
    z = 0.0
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def to_numpy(self):
        return np.array([self.x, self.y, self.z])

    def to_list(self):
        return [self.x, self.y, self.z]

    def print(self):
        print(f"Position2D ==> x : {self.x}, y:{self.y}, z:{self.z}")
