class Engine():
    def __init__(self, name):
        self.name = name

    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def __init__(self,last_service_mileage: int, current_mileage: int):
        super().__init__(name="CapuletEngine")
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def needs_service(self):
        if self.current_mileage > self.last_service_mileage + 30000:
            return True
        else:
            return False

class WilloughbyEngine(Engine):
    def __init__(self,last_service_mileage: int, current_mileage: int):
        super().__init__(name="WilloughbyEngine")
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    def needs_service(self):
        if self.current_mileage > self.last_service_mileage + 60000:
            return True
        else:
            return False

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        super().__init__(name="SternmanEngine")
        self.warning_light_on = warning_light_on
    def needs_service(self):
        if self.warning_light_on is True:
            return True
        else:
            return False