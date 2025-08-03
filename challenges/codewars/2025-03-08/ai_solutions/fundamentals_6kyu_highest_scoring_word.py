def high(x):
    max_sum = 0
    max_word = ""
    current_sum = 0
    current_word = ""
    
    for char in x:
        if char != " ":
            current_sum += ord(char) - 96
            current_word += char
        else:
            if current_sum > max_sum:
                max_sum = current_sum
                max_word = current_word
            current_sum = 0
            current_word = ""
    
    # Check the last word (if no trailing space)
    if current_sum > max_sum:
        max_word = current_word
    
    return max_word

def high(x):
    max_sum = 0
    max_word = ""
    
    for word in x.split():  # splits into words, ignoring spaces
        current_sum = sum(ord(char) - 96 for char in word)
        if current_sum > max_sum:
            max_sum = current_sum
            max_word = word
    
    return max_word
