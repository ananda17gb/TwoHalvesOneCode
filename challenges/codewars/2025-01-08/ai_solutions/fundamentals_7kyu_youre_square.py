def is_square(n):
    if n < 0:
        return False
    x = int(n ** 0.5)
    return x * x == n

import math
def is_square(n):
    if n < 0:
        return False
    x = math.isqrt(n)  # Integer square root
    return x * x == n

def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    # Quick check: Perfect squares end with 0,1,4,5,6,9
    last_digit = n % 10
    if last_digit not in {0, 1, 4, 5, 6, 9}:
        return False
    # Main check
    x = int(n ** 0.5)
    return x * x == n
