def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg <= 0:  # Avoid division by zero and nonsensical mpg
        return False
    return fuel_left >= distance_to_pump / mpg

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump  # No division, avoids floating-point issues
