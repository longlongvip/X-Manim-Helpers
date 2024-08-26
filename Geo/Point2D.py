import numpy as np

class Point2D:
    x = 0.0
    y = 0.0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_numpy(self):
        return np.array([self.x, self.y, 0.0])


    def print(self):
        print(f"Point2D ==> x : {self.x}, y:{self.y}")


if __name__ == "__main__":
    t = Point2D(2.0, 3.0)
    t.print()
    print(t.to_numpy())
