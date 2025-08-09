def is_isogram(string):
    seen = set()
    for char in string.lower():
        if char in seen:
            return False
        seen.add(char)
    return True

def is_isogram(string):
    lower_str = string.lower()
    return len(lower_str) == len(set(lower_str))
