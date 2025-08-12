def binary_array_to_number(arr):
    i = len(arr) - 1
    power = 0
    result = 0
    while i >= 0:
        result += arr[i] * 2**power
        power += 1
        i -= 1
    return result
