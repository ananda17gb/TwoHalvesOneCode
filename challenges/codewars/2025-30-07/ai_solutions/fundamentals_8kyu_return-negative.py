def make_negative(number):
    return number if number < 0 else -number

def make_negative(number):
    return -abs(number)

make_negative = lambda n: -abs(n)
