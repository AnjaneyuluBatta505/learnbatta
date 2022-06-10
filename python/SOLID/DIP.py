from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: on")

    def turn_off(self):
        print("LightBulb: off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: on")

    def turn_off(self):
        print("Fan: off")

class PowerSwitch:
    def __init__(self, device: Switchable):
        self.device = device
        self.on = False
    
    def press(self):
        if self.on:
            self.device.turn_off()
        else:
            self.device.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    switch = PowerSwitch(light_bulb)
    switch.press()
    switch.press()

    fan = Fan()
    switch = PowerSwitch(fan)
    switch.press()
    switch.press()
