import unittest
from flight_monitor import check_altitude, check_fuel_level, check_engine_temp


class TestFlightMonitor(unittest.TestCase):

    def test_altitude(self):
        self.assertEqual(check_altitude(500), "LOW ALTITUDE WARNING")
        self.assertEqual(check_altitude(20000), "ALTITUDE OK")
        self.assertEqual(check_altitude(45000), "HIGH ALTITUDE WARNING")

    def test_fuel_level(self):
        self.assertEqual(check_fuel_level(5), "CRITICAL FUEL LEVEL")
        self.assertEqual(check_fuel_level(20), "LOW FUEL WARNING")
        self.assertEqual(check_fuel_level(50), "FUEL LEVEL OK")

    def test_engine_temp(self):
        self.assertEqual(check_engine_temp(40), "LOW TEMP WARNING")
        self.assertEqual(check_engine_temp(90), "ENGINE TEMP OK")
        self.assertEqual(check_engine_temp(130), "OVERHEAT WARNING")


if __name__ == '__main__':
    unittest.main()
