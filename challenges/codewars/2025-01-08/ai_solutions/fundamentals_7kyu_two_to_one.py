def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def longest(a1, a2):
    unique_letters = set(a1).union(set(a2))
    sorted_letters = sorted(unique_letters)
    return "".join(sorted_letters)

def longest(a1, a2):
    combined = a1 + a2
    unique_sorted = sorted(set(combined))
    return "".join(unique_sorted)
