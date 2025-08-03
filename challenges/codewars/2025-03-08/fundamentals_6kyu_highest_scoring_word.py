def high(x):
    x += " "
    max_sum = 0
    max_word = ""
    current_sum = 0
    current_word = ""   
    for i in x:
        print(i)
        if i != " ":
            current_sum += ord(i) - 96
            current_word += i
        else:
            if current_sum > max_sum:
                max_sum = current_sum
                max_word = current_word
                print(max_word)
            current_sum = 0
            current_word = ""
    return max_word
