def rot13(message):
    result = ''
    remain = 0
    for i in message:
        if i.isalpha():
            if ord(i) > 109:
                remain = ord(i) - 109
                result += chr(96+remain)
            elif ord(i) > 77 and ord(i) < 97:
                remain = ord(i) - 77
                result += chr(64+remain)
            else:
                result += chr((ord(i)+13))
        else:
            result += i
    print(result)
    return result

