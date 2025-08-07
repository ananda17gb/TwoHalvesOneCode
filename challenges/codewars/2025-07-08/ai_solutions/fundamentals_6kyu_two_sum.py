def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return ()  # Return empty tuple if no solution

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return ()
