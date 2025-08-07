def number(bus_stops):
    counter = 0
    for i in range(len(bus_stops)):
        counter += bus_stops[i][0]
        counter -= bus_stops[i][1]
    return counter
