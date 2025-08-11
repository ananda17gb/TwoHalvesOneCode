def friend(x):
    print(x)
    i = 0
    while i < len(x):
        if len(x[i]) != 4:
            x.remove(x[i])
            i -= 1
        i += 1
    return x
