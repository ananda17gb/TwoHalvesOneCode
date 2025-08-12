def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        digit_sum = 0
        for power, digit in enumerate(str(num), start=1):
            digit_sum += int(digit) ** power
        if digit_sum == num:
            result.append(num)
    return result

