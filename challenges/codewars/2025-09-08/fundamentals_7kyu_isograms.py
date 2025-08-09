def is_isogram(string):
    print(string)
    lower_string=string.lower()
    curr_char = ""
    for i in range(len(string)):
        curr_char = lower_string[i]
        for j in range(i+1, len(string)):
            if curr_char == lower_string[j]:
                return False
    return True
