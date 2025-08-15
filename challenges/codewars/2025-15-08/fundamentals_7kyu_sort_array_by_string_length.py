def sort_by_length(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if len(arr[j]) < len(arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
