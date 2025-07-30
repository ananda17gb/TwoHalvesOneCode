def validate_pin(pin):
    # return true or false
    symbols = ("!","@","#","$","%","^","&","*","(",")","-","_","=","+","]","[","{","}","/","?",",","<",".",">","\",`","~","\n")
    pin_len = len(pin)
    if pin_len == 4 or pin_len == 6:
        for digit in pin:
            if ("0" < digit and digit > "9") or digit in symbols:
                    return False
        return True
    return False
