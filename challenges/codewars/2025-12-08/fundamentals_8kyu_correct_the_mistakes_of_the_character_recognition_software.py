def correct(s):
    result = ""
    for i in s:
        if i == "0":
            result += "O"
        elif i == "5":
            result += "S"
        elif i == "1":
            result += "I"
        else:
            result += i
    return result
