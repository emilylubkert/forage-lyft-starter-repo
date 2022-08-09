
from datetime import date


class Battery:
    def __init__ (self, name):
        self.name = name
    
    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, name, last_service_date: date, current_date: date):
        super().__init__(name="SpindlerBattery")
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        if self.current_date > self.last_service_date + 2:
            return True
        else:
            return False

class NubbinBattery(Battery):
    def __init__(self, name, last_service_date: date, current_date: date):
        super().__init__(name="NubbinBattery")
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        if self.current_date > self.last_service_date + 4:
            return True
        else:
            return False