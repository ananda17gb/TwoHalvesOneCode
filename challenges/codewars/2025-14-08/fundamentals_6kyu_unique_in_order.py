def unique_in_order(sequence):
    curr = ""
    result = []
    for i in sequence:
        if curr != i:
            curr = i
            result.append(i)
    return result
