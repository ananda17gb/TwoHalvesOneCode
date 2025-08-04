def longest_consec(strarr, k):
    if not strarr or k <= 0 or k > len(strarr):
        return ""
    
    max_word = ""
    for i in range(len(strarr) - k + 1):
        current = ''.join(strarr[i:i+k])
        if len(current) > len(max_word):
            max_word = current
            
    return max_word
