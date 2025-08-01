def abbrev_name(name):
    parts = name.upper().split()
    if len(parts) < 2:
        return parts[0][0]  # or raise an error, depending on requirements
    return f"{parts[0][0]}.{parts[1][0]}"


def abbrev_name(name):
    first, last = name.upper().split()
    return f"{first[0]}.{last[0]}"
