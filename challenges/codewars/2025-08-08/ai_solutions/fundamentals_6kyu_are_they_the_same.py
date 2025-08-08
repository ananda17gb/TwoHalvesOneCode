def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    if not array1 and not array2:  # both are empty
        return True
    
    # Square all elements in array1 (handle negatives) and sort
    squared = sorted([x * x for x in array1])
    sorted_array2 = sorted(array2)
    
    return squared == sorted_array2

