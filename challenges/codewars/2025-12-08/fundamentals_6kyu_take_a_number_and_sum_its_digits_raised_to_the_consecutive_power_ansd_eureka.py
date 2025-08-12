def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    curr = ""
    power = 1
    curr_sum = 0
    result = []
    for i in range(a, b + 1):
        curr += str(i)
        for j in curr:
            curr_sum += int(j) ** power
            power += 1
        if curr_sum == i:
            result.append(int(i))
        curr = ""
        power = 1
        curr_sum = 0
    return result
