def count(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

from collections import defaultdict
def count(s):
    result = defaultdict(int)
    for char in s:
        result[char] += 1
    return dict(result)

from collections import Counter
def count(s):
    return dict(Counter(s))
