def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]
    return None


def first_non_consecutive(arr):
    for i, num in enumerate(arr[:-1]):
        if arr[i + 1] != num + 1:
            return arr[i + 1]
    return None
