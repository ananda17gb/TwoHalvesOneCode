def correct(s):
    mapping = {"0": "O", "5": "S", "1": "I"}
    return "".join(mapping.get(c, c) for c in s)


# above code is better than mine but pyright said that it possibly allows None and it need more type safety stuff
def correct(s: str) -> str:
    mapping: dict[str, str] = {"0": "O", "5": "S", "1": "I"}  # Explicit type
    return "".join(mapping.get(c, c) for c in s)


def correct(s: str) -> str:
    mapping = {"0": "O", "5": "S", "1": "I"}
    return "".join(mapping[c] if c in mapping else c for c in s)


def correct(s: str) -> str:
    mapping = {"0": "O", "5": "S", "1": "I"}
    return "".join(item for item in (mapping.get(c, c) for c in s) if item is not None)


def correct(s):
    return s.translate(str.maketrans("015", "OSI"))
