def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positive = 0
    sum_negative = 0
    result = []
    for i in arr:
        if i > 0:
            count_positive += 1
        elif i < 0:
            sum_negative += i
    result.extend([count_positive,sum_negative])
    return result
