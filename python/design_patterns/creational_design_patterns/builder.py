from abc import ABC, abstractmethod


class House:
    basement = None
    walls = None
    windows = None
    doors = None
    roof = None

    def get_info(self):
        print(f"basement: {self.basement}")
        print(f"walls: {self.walls}")
        print(f"windows: {self.windows}")
        print(f"doors: {self.doors}")
        print(f"roof: {self.roof}")


class AbsHouseBuilder(ABC):
    house = None

    @abstractmethod
    def build_basement(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass


class SimpleHouseBuilder(AbsHouseBuilder):
    def __init__(self):
        self.house = House()

    def build_basement(self):
        self.house.basement = "rock solid basement"

    def build_walls(self):
        self.house.walls = "4 sand brick walls"

    def build_windows(self):
        self.house.windows = "2 wooden windows"

    def build_doors(self):
        self.house.doors = "2 wooden doors"

    def build_roof(self):
        self.house.roof = "Gable roof"
    
    def get_house(self):
        return self.house


class HouseDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def construct(self):
        self.builder.build_basement()
        self.builder.build_walls()
        self.builder.build_windows()
        self.builder.build_doors()
        self.builder.build_roof()
        return self.builder.get_house()


if __name__ == '__main__':
    builder = SimpleHouseBuilder()
    director = HouseDirector(builder)
    house = director.construct()
    house.get_info()
