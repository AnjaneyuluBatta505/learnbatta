from abc import ABC
from copy import deepcopy

class Shape(ABC):

    def clone(self):
        return deepcopy(self)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# client
if __name__ == '__main__':
    c1 = Circle(10)
    c1_copy = c1.clone()
    print(id(c1), id(c1_copy))
    # False
