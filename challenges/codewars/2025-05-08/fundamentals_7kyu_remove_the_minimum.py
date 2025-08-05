def remove_smallest(numbers):
    if not numbers:
        return []
    minimal = min(numbers)
    result = []
    flag = False
    for i in numbers:
        if i != minimal or flag:
            result.append(i)
        else:
            flag = True
    return result

