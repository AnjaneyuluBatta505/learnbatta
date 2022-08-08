from abc import ABC, abstractmethod

class CarAbs(ABC):
    @abstractmethod
    def drive(self, driver_name):
        pass

class Car(CarAbs):
    def drive(self, driver_name):
        print(f"{driver_name} is driving the car.")

class CarProxy(ABC):
    def __init__(self, driver_name, age):
        self.driver_name = driver_name
        self.age = age

    def drive(self):
        if(self.age < 18):
            print("Sorry, the driver is too young to drive.")
            return
        car = Car()
        return car.drive(self.driver_name)

if __name__ == '__main__':
    # case-1
    car = CarProxy("Anji", 20)
    car.drive()
    # case-2
    car = CarProxy("Surya", 17)
    car.drive()
