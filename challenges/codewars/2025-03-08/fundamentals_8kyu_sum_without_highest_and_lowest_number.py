def sum_array(arr):
    if (arr == [] or arr == None):
        return 0
    result = 0
    sort_array = sorted(arr)
    for i in range(1, len(sort_array) - 1):
        result += sort_array[i]
    return result
