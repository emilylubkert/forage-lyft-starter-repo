from needs_service import Needs_Service

class Car(Needs_Service):
    def __init__(self, engine, battery):
        self.engine: engine
        self.battery: battery
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else: 
            return False