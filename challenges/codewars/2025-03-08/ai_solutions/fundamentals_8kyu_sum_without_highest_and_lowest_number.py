def sum_array(arr):
    if not arr or len(arr) <= 2:  # Handles None, [], or arrays with ≤2 elements
        return 0
    sorted_arr = sorted(arr)
    return sum(sorted_arr[1:-1])  # Sum all except first and last
