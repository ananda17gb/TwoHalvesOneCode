def first_non_consecutive(arr):
    i = 0
    while i < len(arr) - 1:
        next = arr[i + 1]
        if arr[i] + 1 != next:
            return next
        i += 1
    return None
