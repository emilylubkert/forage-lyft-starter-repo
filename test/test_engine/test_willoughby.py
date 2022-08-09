import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 20000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    def test_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 20000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()