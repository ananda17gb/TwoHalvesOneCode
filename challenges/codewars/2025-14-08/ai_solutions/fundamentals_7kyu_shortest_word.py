def find_short(s):
    words = s.split()
    if not words:  # Handle empty string case
        return 0
    return min(len(word) for word in words)

def find_short(s):
return min((len(word) for word in s.split()), default=0)
