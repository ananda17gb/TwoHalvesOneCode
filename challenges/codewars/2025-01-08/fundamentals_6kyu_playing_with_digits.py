def dig_pow(n, p):
    digits = []
    sum = 0
    for i in str(n):
        digits.append(int(i))
    for i in range(len(digits)):
        sum += digits[i]**(i+p)
    result = sum / n
    if (result == int(result)):
        return int(result)
    return -1
