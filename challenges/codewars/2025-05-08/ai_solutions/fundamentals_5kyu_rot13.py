def rot13(message):
    result = []
    for char in message:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters
            rotated = ord('a') + (ord(char) - ord('a') + 13) % 26
            result.append(chr(rotated))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            rotated = ord('A') + (ord(char) - ord('A') + 13) % 26
            result.append(chr(rotated))
        else:
            # Leave non-alphabetic characters as-is
            result.append(char)
    return ''.join(result)

