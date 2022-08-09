from tire.tire import Tire 

class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array
    
    def needs_service(self):
        for value in self.tire_wear_array:
            return value >= .9