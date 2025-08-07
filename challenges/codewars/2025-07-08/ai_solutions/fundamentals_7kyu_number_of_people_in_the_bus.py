def number(bus_stops):
    counter = 0
    for on, off in bus_stops:  # More readable with unpacking
        counter += on - off    # Combine addition and subtraction
    return counter if bus_stops else 0  # Handle empty list (optional)

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
