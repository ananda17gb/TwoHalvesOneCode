def tower_builder(n_floors):
    result = []
    for i in range(1, n_floors + 1):
        result.append(" "*(n_floors-i)+"*"*(i+i-1)+" "*(n_floors-i))
    return result
