import Engine
import Battery

class Car:
    def __init__(self, name, engine: Engine, battery: Battery):
        self.name = name
        self.engine: engine
        self.battery: battery
    def needs_service(self):
        if self.engine.needs_service() is True or self.battery.needs_service() is True:
            return True
        else: 
            return False