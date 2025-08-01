def longest(a1, a2):
    longest = []
    for letter in a1:
        if letter not in longest:
            longest.append(letter)
    for letter in a2:
        if letter not in longest:
            longest.append(letter)
    for i in range(len(longest)):
        min = i
        for j in range(i+1, len(longest)):
            if longest[j] < longest[min]:
                min = j
        if min != i:
            temp = longest[i]
            longest[i] = longest[min]
            longest[min] = temp
    result = ''
    for i in longest:
        result += i
    return result
