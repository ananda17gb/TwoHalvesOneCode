def remove_smallest(numbers):
    if not numbers:  # Handle empty list case
        return []
    
    min_value = min(numbers)
    min_index = numbers.index(min_value)  # Find first occurrence of min value
    return numbers[:min_index] + numbers[min_index+1:]

