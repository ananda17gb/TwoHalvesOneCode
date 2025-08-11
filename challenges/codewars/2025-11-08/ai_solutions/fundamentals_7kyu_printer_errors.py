def printer_error(s):
    bad_count = sum(ch > "m" for ch in s)
    return f"{bad_count}/{len(s)}"


def printer_error(s):
    return f"{sum(ch > 'm' for ch in s)}/{len(s)}"


def printer_error(s):
    bad_letters = set("nopqrstuvwxyz")
    return f"{sum(ch in bad_letters for ch in s)}/{len(s)}"
