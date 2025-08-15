def persistence(n):
    curr = str(n)
    curr_mul = 1
    count = 0
    while len(curr) > 1:
        for i in curr:
            curr_mul *= int(i)
        curr = str(curr_mul)
        curr_mul = 1
        count += 1
    return count
