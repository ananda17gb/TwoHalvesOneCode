def solution(s):
    i = 0
    result = ""
    while i < len(s):
        if s[i].isupper():
            result += " "
        result += s[i]
        i += 1
    return result


def solution(s):
    result = ""
    for i in range(len(s)):
        if s[i].isupper():
            result += " "
        result += s[i]
        i += 1
    return result


# have an idea to do the one liner but I think I should just put this in AI solution but I tried to do this only with one line.
def solution(s):
    return "".join([" " + i if i.isupper() else i for i in s])
