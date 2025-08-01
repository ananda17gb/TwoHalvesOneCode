def xo(s):
    xo = ["x","o","X","O"]
    count_x = 0
    count_o = 0
    flag = False
    if s == '':
        return True
    for i in s:
        if i == "x" or i == "X": 
            count_x += 1  
        elif i == "o" or i == "O": 
            count_o += 1  
    for i in s:
        if i not in xo:
            flag = True
        else:
            if count_x == count_o:
                return True
            else:
                return False
    return flag
