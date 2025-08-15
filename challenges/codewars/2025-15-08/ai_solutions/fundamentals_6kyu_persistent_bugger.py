from math import prod


def persistence(n):
    count = 0
    while n >= 10:
        n = prod(int(d) for d in str(n))
        count += 1
    return count
