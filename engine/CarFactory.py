from abc import ABC, abstractmethod
from datetime import date

class CarCreator(ABC):
    def factory_method(self):
        return Car

class CarFactory(ABC):
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ): Car(capulet_engine, spindler_battery)
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ): Car(willoughby_engine, spindler_battery)
    def create_palindrome(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ): Car(sternman_engine, spindler_battery)
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ): Car(willoughby_engine, nubbin_battery)
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int ): Car(capulet_engine, nubbin_battery)