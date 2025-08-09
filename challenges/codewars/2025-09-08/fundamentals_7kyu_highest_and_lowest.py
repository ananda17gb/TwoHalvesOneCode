def high_and_low(numbers):
    splitted = numbers.split()
    list = []
    for i in splitted:
        list.append(int(i))
    return str(max(list)) + " " + str(min(list))   
