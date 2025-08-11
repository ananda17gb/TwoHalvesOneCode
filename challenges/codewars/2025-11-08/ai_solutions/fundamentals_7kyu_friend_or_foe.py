def friend(x):
    x[:] = [name for name in x if len(name) == 4]
    return x
