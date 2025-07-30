def simple_multiplication(number):
    return number * 9 if number % 2 else number * 8

def simple_multiplication(number):
    return number * (8 + number % 2)

def simple_multiplication(number):
    return number * {0: 8, 1: 9}[number % 2]
