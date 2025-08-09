def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"

def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"
