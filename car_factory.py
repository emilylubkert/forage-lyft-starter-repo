from abc import ABC
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car


class CarFactory(ABC):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        car = Car(battery, engine)
        return car

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage ):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car = Car(battery, engine)
        return car 

    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage ):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_on)
        car = Car(battery, engine)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        car = Car(battery, engine)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        car = Car(battery, engine)
        return car        