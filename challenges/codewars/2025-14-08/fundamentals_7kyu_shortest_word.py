def find_short(s):
    splitted = s.split()
    min = len(splitted[0])
    for i in splitted:
        if min > len(i):
            min = len(i)
    return min
