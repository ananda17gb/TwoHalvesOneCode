def validate_pin(pin):
    # Check length is 4 or 6
    if len(pin) not in {4, 6}:
        return False
    
    # Check all characters are digits
    return pin.isdigit()

def validate_pin(pin):
    if not isinstance(pin, str):
        return False
    
    pin = pin.strip()
    return len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    # Check length is 4 or 6
    if len(pin) not in {4, 6}:
        return False
    
    # Check each character is a digit
    for char in pin:
        if not ('0' <= char <= '9'):  # Fixed the digit check
            return False
    return True

def validate_pin(pin):
    if len(pin) not in (4, 6):
        return False
    
    try:
        int(pin)  # Try to convert to integer
        return True
    except ValueError:
        return False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
