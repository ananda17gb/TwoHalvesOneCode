def xo(s):
    s_lower = s.lower()  # Convert to lowercase for case-insensitive comparison
    count_x = s_lower.count('x')
    count_o = s_lower.count('o')
    return count_x == count_o  # True if equal, False otherwise
