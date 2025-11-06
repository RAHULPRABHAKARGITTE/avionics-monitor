# flight_monitor.py

def check_altitude(altitude):
  
    if altitude < 1000:
        return "LOW ALTITUDE WARNING"
    elif altitude > 40000:
        return "HIGH ALTITUDE WARNING"
    else:
        return "ALTITUDE OK"


def check_fuel_level(fuel_percentage):

    if fuel_percentage < 10:
        return "CRITICAL FUEL LEVEL"
    elif fuel_percentage < 30:
        return "LOW FUEL WARNING"
    else:
        return "FUEL LEVEL OK"


def check_engine_temp(temp_celsius):
   
    if temp_celsius < 50:
        return "LOW TEMP WARNING"
    elif temp_celsius > 120:
        return "OVERHEAT WARNING"
    else:
        return "ENGINE TEMP OK"


# Test print (you wan
print(check_altitude(100000),"\n" +  check_fuel_level(50),"\n" +  check_engine_temp(130))
