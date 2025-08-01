def abbrev_name(name):
    capitalized_name = name.upper()
    first = capitalized_name[0]
    second = ""
    for i in range(len(capitalized_name)):
        if capitalized_name[i] == " ":
            second = capitalized_name[i+1]
            break
    return first+"."+second
