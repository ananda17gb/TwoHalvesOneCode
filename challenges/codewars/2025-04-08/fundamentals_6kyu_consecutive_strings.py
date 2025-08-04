def longest_consec(strarr, k):
    if len(strarr) < k or k < 1 or strarr == []:
        return ""
    max_len_cons_word = ""
    curr_len_cons_word = ""
    for i in range(len(strarr)):
        if i + k  <= len(strarr):
            for j in range(i,i+k):
                curr_len_cons_word += strarr[j]    
            if len(curr_len_cons_word) > len(max_len_cons_word):
                max_len_cons_word = curr_len_cons_word
            curr_len_cons_word = ""
    return max_len_cons_word
