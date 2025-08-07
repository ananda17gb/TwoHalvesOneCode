def two_sum(numbers, target):
    result = ()
    list_result = [] 
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                list_result = list(result)
                list_result.extend([i,j])
                break
    result = tuple(list_result)
    return result
