# test_flight_monitor.py
from flight_monitor import check_altitude, check_fuel_level, flight_status

def test_check_altitude():
    assert check_altitude(500) == "LOW ALTITUDE WARNING"
    assert check_altitude(5000) == "ALTITUDE OK"
    assert check_altitude(45000) == "HIGH ALTITUDE WARNING"

def test_check_fuel_level():
    assert check_fuel_level(50) == "FUEL LEVEL OK"
    assert check_fuel_level(20) == "LOW FUEL WARNING"
    assert check_fuel_level(5) == "CRITICAL FUEL LEVEL"

def test_flight_status():
    assert "ALERT" in flight_status(500, 20)
    assert "All Systems Normal" in flight_status(10000, 70)
