def greet(name, owner):
    return {'Hello boss': name == owner, 'Hello guest': name != owner}.get(True)


def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"
