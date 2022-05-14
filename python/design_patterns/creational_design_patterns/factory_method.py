from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        """prepare the pizza"""

    @abstractmethod
    def bake(self):
        """bake the pizza"""

    @abstractmethod
    def cut(self):
        """cut the baked pizza into a required shape"""

    @abstractmethod
    def box(self):
        """move the pizza into the box"""


class PizzaMixin:
    pizza_type = ""

    def prepare(self):
        """prepare the pizza"""
        print(f"prepare {self.pizza_type} pizza")

    def bake(self):
        """bake the pizza"""
        print(f"bake {self.pizza_type} pizza")

    def cut(self):
        """cut the baked pizza into a required shape"""
        print(f"cut {self.pizza_type} pizza")

    def box(self):
        """move the pizza into the box"""
        print(f"box {self.pizza_type} pizza")


class CheesePizza(PizzaMixin, Pizza):
    pizza_type = "cheese"


class VegPizza(PizzaMixin, Pizza):
    pizza_type = "veg"


class PizzaFactory:
    def create_pizza(self, pizza_type):
        pizza = None
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "veg":
            pizza = VegPizza()
        if pizza is None:
            raise Exception("Invalid pizza type")
        return pizza


# client
class PizzaStore:
    def order_pizza(self, pizza_type):
        """order and get pizza"""
        factory = PizzaFactory()
        pizza = factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


if __name__ == "__main__":
    store = PizzaStore()
    store.order_pizza("cheese")
