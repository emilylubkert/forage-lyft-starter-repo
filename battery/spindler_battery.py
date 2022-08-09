from battery.battery import Battery
from utils import add_time_to_date

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        recommended_service_date = add_time_to_date(self.last_service_date, 3)
        if self.current_date > recommended_service_date:
            return True
        else:
            return False