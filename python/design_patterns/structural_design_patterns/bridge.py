# bridge design pattern
from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def get_color(self):
        pass


class Red(Color):
    def get_color(self):
        print("Color Red")


class Blue(Color):
    def get_color(self):
        print("Color Blue")


class Shape(ABC):
    # composition
    def __init__(self, color: Color):
        self.color = color
    
    def get_color(self):
        self.color.get_color()

    @abstractmethod
    def display(self):
        pass


class Square(Shape):
    def display(self):
        print("square")


class Circle(Shape):
    def display(self):
        print("circle")


if __name__ == "__main__":
    # client
    color = Blue()
    blue_square = Square(color)

    blue_square.display()
    blue_square.get_color()
