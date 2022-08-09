from battery.battery import Battery
from datetime import date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        if self.current_date > self.last_service_date + 2:
            return True
        else:
            return False