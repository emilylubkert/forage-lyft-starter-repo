import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 80000
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    def test_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 20000
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()