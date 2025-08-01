def dig_pow(n, p):
    total = 0
    for i, digit in enumerate(str(n)):
        total += int(digit) ** (p + i)
    if total % n == 0:
        return total // n
    return -1
