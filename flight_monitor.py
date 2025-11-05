
# Function 1 for Altitued Check
def check_altitude(altitude):
    if altitude < 1000:
        return "LOW ALTITUDE WARNING"
    elif altitude > 40000:
        return "HIGH ALTITUDE WARNING"
    else:
        return "ALTITUDE OK"

# Function 2 for Fule chheck
def check_fuel_level(fuel_percentage):

    if fuel_percentage < 10:
        return "CRITICAL FUEL LEVEL"
    elif fuel_percentage < 30:
        return "LOW FUEL WARNING"
    else:
        return "FUEL LEVEL OK"

#Function 3 to take both value from above two function


def flight_status(altitude, fuel):
    """
    Now we ill Combine both checks and returns an overall flight status 
    """
    alt_status = check_altitude(altitude)
    fuel_status = check_fuel_level(fuel)

    if "WARNING" in alt_status or "WARNING" in fuel_status or "CRITICAL" in fuel_status:
        return f"ALERT: {alt_status}, {fuel_status}"
    else:
        return f"All Systems Normal: {alt_status}, {fuel_status}"


if __name__ == "__main__":
   
    altitude = 1200     # valus in feet
    fuel = 25           # valus in percentage
    print(flight_status(altitude, fuel))
