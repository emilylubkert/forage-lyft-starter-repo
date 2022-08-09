import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_array = [1, 1, 1, .5]
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())
    def test_tire_should_not_be_serviced(self):
        tire_wear_array = [.1, .2, 0, .5]
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()